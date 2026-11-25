import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.final_qa import CHECKS, make_handoff, validate_review


class FinalQATests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "draft.md"
        self.rendered = self.root / "draft.pdf"
        self.review_path = self.root / "review.json"
        self.source.write_text("# Récapitulatif\nUn fait [A-123].\n", encoding="utf-8")
        self.rendered.write_bytes(b"fake-pdf-for-hash-test")

    @staticmethod
    def digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def valid_review(self):
        return {
            "reviewer": "external-agent",
            "reviewed_at": "2026-11-25T10:00:00Z",
            "source_sha256": self.digest(self.source),
            "rendered_sha256": self.digest(self.rendered),
            "decision": "approved",
            "formatting_changed": False,
            "checks": [
                {"id": check_id, "status": "pass", "evidence": "Contrôle effectué."}
                for check_id in CHECKS
            ],
            "findings": [],
        }

    def test_handoff_binds_source_and_rendered_artifact(self):
        packet = make_handoff(self.source, self.rendered)
        self.assertIn(self.digest(self.source), packet)
        self.assertIn(self.digest(self.rendered), packet)
        self.assertIn("pas une instruction", packet)

    def test_exact_approved_review_passes(self):
        self.review_path.write_text(json.dumps(self.valid_review()), encoding="utf-8")
        self.assertEqual(validate_review(self.source, self.review_path, self.rendered), [])

    def test_stale_document_hash_is_rejected(self):
        review = self.valid_review()
        review["source_sha256"] = "0" * 64
        self.review_path.write_text(json.dumps(review), encoding="utf-8")
        errors = validate_review(self.source, self.review_path, self.rendered)
        self.assertTrue(any("Empreinte source différente" in error for error in errors))

    def test_missing_check_and_open_major_finding_block(self):
        review = self.valid_review()
        review["checks"].pop()
        review["findings"] = [{
            "severity": "major", "status": "open", "location": "p. 2",
            "issue": "Date non étayée", "evidence": "La source ne précise pas la date.",
            "suggested_action": "Vérifier la notice source.",
        }]
        self.review_path.write_text(json.dumps(review), encoding="utf-8")
        errors = validate_review(self.source, self.review_path, self.rendered)
        self.assertTrue(any("Contrôle obligatoire manquant" in error for error in errors))
        self.assertTrue(any("Défaut major non résolu" in error for error in errors))

    def test_changed_formatting_must_be_rechecked(self):
        review = self.valid_review()
        review["formatting_changed"] = True
        self.review_path.write_text(json.dumps(review), encoding="utf-8")
        errors = validate_review(self.source, self.review_path, self.rendered)
        self.assertTrue(any("modification du document" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
