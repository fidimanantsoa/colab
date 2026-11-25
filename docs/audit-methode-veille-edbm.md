# Audit de la méthode de veille EDBM et proposition d’évolution

**Version de l’audit : 25 novembre 2026**
**Périmètre examiné :** méthode de référence mise à jour le 24/11/2026, documentation Data Factory disponible dans son dossier, et exemples de récapitulatifs publiés pour les semaines du 2 octobre au 19 novembre 2026. Cet audit porte sur la cohérence du dispositif décrit et sur les indices visibles dans les livrables; il ne remplace pas un audit du code de production, des journaux internes ou une vérification indépendante de chaque fait.

## Synthèse

La méthode a de solides fondations : elle part des besoins, distingue collecte et analyse, conserve les articles avant tri, sépare les faits de leur interprétation, conserve une base et prévoit une boucle de retour humain. Le principe de ne pas faire rédiger directement le récapitulatif depuis les articles bruts est particulièrement utile pour la traçabilité et la reproductibilité.

Le problème principal n’est donc pas l’absence de méthode, mais **l’écart entre la méthode, les descriptions d’implémentation et la forme des livrables**. Le corpus et les règles de traitement ont beaucoup évolué; les versions successives ne sont pas comparables; et le dernier contrôle éditorial effectué par un agent externe n’a pas de place formalisée dans le cycle. Les récapitulatifs deviennent également très volumineux au regard de la priorité décisionnelle annoncée pour l’EDBM.

**Verdict :** conserver l’architecture de collecte et de base de faits, mais rendre obligatoires quatre contrôles avant diffusion : (1) périmètre et complétude, (2) provenance et dates, (3) cohérence/qualité factuelle, (4) revue éditoriale externe versionnée suivie d’une approbation humaine. Le livrable devrait distinguer clairement le corpus documentaire exhaustif du produit court destiné à la décision.

## Documents examinés

- [Méthode de Veille EDBM — cadre conceptuel, MAJ 24/11/2026](https://docs.google.com/document/d/151gbuLgdwuthSc1E5Q6pGzBWiGRZ0boy/edit)
- [00_README_DATA_FACTORY.md — documentation de conception/implémentation datée d’août](https://docs.google.com/document/d/1YRluyQJlsFStGjKkGjA6hgHiS7WYeVzn/edit)
- [Récapitulatif des faits, 6–12 novembre 2026](https://drive.google.com/file/d/13RKvWqhDdC0vSjYVzTVD2ytkDz7pPHxo/view)
- [Récapitulatif des faits, 13–19 novembre 2026](https://drive.google.com/file/d/1xqUvIWtrKKtVAm4lhO-5TYGAp7ZZM6Ua/view)
- Échantillons plus anciens : [2–8 octobre](https://drive.google.com/file/d/1TP4uYG3MbTb6nnfPNoKSGJD9imJFH-tG/view), [9–15 octobre](https://drive.google.com/file/d/18wfJZ7ncJ3YEkMI3PI9hX6dsAFyecjNJ/view), [23–29 octobre](https://drive.google.com/file/d/173CQifuAvi2VY1Ie8XUdMkkh68zMlF23/view) et [30 octobre–5 novembre](https://drive.google.com/file/d/1PQcrjQ6k6I6i408blcb9f4QxN8GPnufR/view).

Les PDF ont été lus par extraction de texte. Les mises en page, hyperliens, journaux complets et éventuelles pages graphiques n’ont pas tous pu être inspectés; les observations ci-dessous sont donc des constats documentaires, pas des conclusions sur les données internes non fournies.

## Points forts à préserver

1. **Cadrage explicite.** Les quatre objectifs O1–O4, les besoins B1–B8 et les secteurs prioritaires donnent une finalité à la collecte. La distinction veille / intelligence économique est pertinente.
2. **Collecte sans filtre prématuré, puis lecture rationnée.** L’archive exhaustive peut protéger contre la perte de signaux qui ne semblent pas pertinents au premier regard, à condition d’avoir des règles de conservation et un tri gouverné.
3. **Séparation des étapes et base de faits.** La collecte, la sélection, l’extraction, la base et le récapitulatif sont décrits comme des étapes distinctes. L’utilisation de la base plutôt que des articles au moment de rédiger le récapitulatif aide à stabiliser les entrées.
4. **Intervention humaine identifiable.** Le classement YES/NO et le journal de corrections apportent un point d’arbitrage et une possibilité de retour d’expérience.
5. **Résilience opérationnelle.** La documentation mentionne quotas, relais, rattrapage et coupure par source; c’est préférable à un échec silencieux.
6. **Amélioration visible du livrable du 6–12 novembre.** Il annonce 1 106 notices examinées, 590 retenues, 516 exclues avec motif, et renvoie à une annexe de traçabilité. C’est une base plus auditable que des comptes de faits sans dénominateur.

## Incohérences et difficultés prioritaires

### 1. La documentation ne décrit pas un état unique du système — **critique**

La méthode, mise à jour le 24 novembre, décrit environ 452 sources uniques, moisson horaire, sélection à 10 h 30, extraction en lots via NotebookLM/Gemini, base SQLite et récapitulatif hebdomadaire généré depuis cette base. Le README Data Factory, daté d’août, décrit un autre dispositif : 157 sources, crons et horaires différents, des agents d’analyse, VERITAS, SAGE-IO et deux livrables quotidiens. Il se présente à la fois comme conception et implémentation, alors que la méthode de novembre dit explicitement que le dispositif a changé.

Ce décalage peut conduire à appliquer une procédure, un horaire, un périmètre ou un KPI périmé. Il s’agit vraisemblablement d’un document ancien plutôt que d’une preuve que le dispositif actuel suit les deux architectures; il faut néanmoins le marquer **ARCHIVÉ / NON NORMATIF** ou le réconcilier et publier une seule source de vérité, avec date d’effet et responsable.

**À faire :** versionner les règles, préciser pour chaque composant « cible / en production / retiré », lier les paramètres réellement chargés, et ajouter un contrôle automatique qui signale une documentation dont la date ou la version ne correspond plus au pipeline.

### 2. L’objectif décisionnel se perd dans le volume du digest — **critique**

Le cycle prévoit un plafond de sélection de 800 articles par semaine, mais les exemples montrent des récapitulatifs à 1 071 faits (9–15 octobre), 1 189 (23–29 octobre), 1 603 (30 octobre–5 novembre) puis 590 faits retenus après examen pour le 6–12 novembre. Le dernier échantillon, 13–19 novembre, annonce 1 259 faits. Les volumes ne sont pas nécessairement contradictoires — période, inclusion, déduplication et règles d’édition ont changé — mais ils démontrent qu’ils ne sont pas comparables sans dictionnaire de métriques et version de méthode.

Un document de 114 à 226 pages et couvrant 12 rubriques mondiales peut servir de **corpus de consultation**, mais n’est pas à lui seul une synthèse décisionnelle pour l’EDBM. Le lien entre les faits conservés et O1–O4/B1–B8 n’est pas visible systématiquement dans les échantillons. Le volume peut masquer les informations Madagascar, investissement, concurrence, cadre des affaires et secteurs prioritaires.

**À faire :** produire deux vues distinctes : (a) archive/recueil exhaustif, (b) brief exécutif court, hiérarchisé par impact pour Madagascar, urgence, horizon et décision/action attendue. Pour chaque fait retenu, enregistrer au moins un besoin B et un objectif O, ou une justification « signal faible / contexte ». Ne pas utiliser le nombre de faits comme proxy de valeur.

### 3. Le filtrage n’est pas encore une règle de sélection auditable de bout en bout — **élevé**

La méthode décrit un classement d’abord automatique (registre YES, priorités, seuil JEV, score lexical), puis une décision humaine binaire. C’est un bon mécanisme de présélection, mais le résultat est sensible aux scores, seuils, plafonds, qualité des labels et disponibilité du relecteur. Une décision YES/NO ne dit pas pourquoi un article sert un besoin; l’apprentissage lexical à partir des seuls choix humains risque de renforcer les habitudes du lecteur et d’écarter les sujets rares. Les critères hiérarchisés O1→O4, les signaux faibles et le seuil de priorité ne sont pas traduits en critères mesurables communs dans les sorties consultées.

**À faire :** conserver la décision et son motif, le score et la version du modèle/règle, et les tags besoin/objectif/territoire/secteur. Prévoir « à surveiller / incertain » au lieu de forcer YES/NO, un quota de revue aléatoire des rejets, une revue des faux négatifs, et une voie de rattrapage pour les signaux faibles. Toute modification de seuil doit être datée et mesurée sur un corpus test.

### 4. Fiabilité de la source et véracité d’un énoncé sont deux choses différentes — **élevé**

La méthode emploie une fiabilité d’article OTAN et un score lexical/JEV; la documentation Data Factory plus ancienne décrit des classes A1–F6, S1–S5 et un contrôle VERITAS à double source. Ces référentiels peuvent être utiles, mais leurs versions et leur articulation ne sont pas explicitées dans les documents disponibles. Une source habituellement fiable ne rend pas chaque affirmation vérifiée; inversement, plusieurs articles reprenant le même communiqué ne constituent pas plusieurs corroborations indépendantes.

**À faire :** séparer dans le schéma de données (1) fiabilité de la source, (2) preuve pour chaque assertion, (3) corroboration indépendante, (4) niveau de confiance et (5) statut de vérification. Distinguer fait confirmé, déclaration attribuée, projection, allégation et information non corroborée. La double source doit être indépendante et pertinente pour l’assertion exacte.

### 5. Dates de l’événement, de publication, de mesure et de période restent un risque sémantique — **élevé**

La méthode a déjà ajouté des conventions de dates, mais les exemplaires montrent que les articles peuvent couvrir des périodes antérieures, des statistiques mensuelles/annuelles, une annonce et un événement futur. Le PDF du 13–19 novembre, par exemple, contient une notice annonçant une simulation électorale le 28 novembre; c’est un événement futur au regard de la période du récapitulatif. Cela peut être un fait d’anticipation pertinent, mais le statut « prévu / à venir » doit être explicite pour éviter de le lire comme réalisé. Les chiffres historiques cités hors période doivent aussi être séparés des événements de la semaine.

**À faire :** imposer des champs distincts `date_publication`, `date_evenement`, `periode_statistique`, `date_verification` et `statut_evenement` (réalisé, annoncé, prévu, reporté, annulé, inconnu). Afficher une alerte automatique si un événement réalisé est daté après la date d’arrêté, ou si le récit transforme une prévision en constat.

### 6. Traçabilité et conventions de citation varient entre éditions — **élevé**

Le récapitulatif du 6–12 novembre cite des références de type A-ID et numéro de notice et annonce des annexes de sources et de méthode. L’exemplaire du 13–19 novembre utilise des citations numériques, et les échantillons plus anciens emploient d’autres styles (A-ID, références multiples, parfois notices sans identifiant visible). Cette évolution rend les renvois moins uniformes et complique le rapprochement entre fait, notice de base et article source.

**À faire :** choisir un identifiant stable de fait, conserver un ou plusieurs identifiants d’article source, et générer les renvois automatiquement depuis la base. Chaque paragraphe devrait être relié à une notice, une URL, un titre, un média, les dates et le niveau de vérification. Une correction doit garder l’ancienne valeur, la nouvelle valeur, le motif, l’auteur et l’horodatage.

### 7. Les chiffres de production ne sont pas des indicateurs de qualité comparables — **élevé**

Les comptes de faits passent fortement d’une édition à l’autre; le PDF du 6–12 novembre fournit un excellent dénominateur (1 106 examinées, 590 retenues), mais les autres échantillons n’affichent pas tous le même dénominateur ou les mêmes définitions. Une hausse peut signifier une collecte plus complète, une fenêtre plus large, plus de doublons, ou un filtre plus permissif. Une baisse peut être le résultat d’un filtre amélioré, d’un quota, d’une panne ou d’un changement de périmètre.

**À faire :** versionner le dictionnaire des KPI; publier examinées, retenues, surveillées, rejetées par motif, taux de doublons, sources attendues/actives, taux d’échec extraction, taux de citation valide, délai publication→détection et couverture des B1–B8. Comparer seulement à périmètre et règles identiques, ou annoter la rupture de série.

### 8. Le modèle « tout collecter, conserver définitivement » appelle une politique de gouvernance — **moyen/élevé**

Une moisson exhaustive maximise la possibilité de réanalyse, mais « cache permanent » plus centaines de sources implique gestion du stockage, de la provenance, du retrait/correction, de la rétention, du droit d’auteur, et des données personnelles éventuellement présentes dans les articles. Le coût n’est pas seulement disque : les échecs, retentatives, volumes à examiner et quotas LLM sont aussi des ressources. Les limites par source peuvent en outre rendre l’exhaustivité apparente trompeuse si le taux de couverture n’est pas affiché.

**À faire :** établir une politique de conservation, stocker les métadonnées et extraits nécessaires plutôt que des copies complètes lorsque c’est suffisant, documenter les limites de collecte, purger ou archiver selon le besoin et signaler les articles indisponibles. Ne jamais interpréter « moissonné » comme « exhaustif » sans mesure de couverture.

### 9. Le contrôle externe de vérification/mise en forme est absent du cycle formel — **critique pour la diffusion**

Le cycle conceptuel se termine par diffusion et capitalisation; le dispositif opérationnel décrit génération/assemblage, mais ne définit pas de contrat pour la revue externe. Sans contrôle de version, empreinte du document et résultat structuré, il est impossible de savoir quelle édition a été vérifiée, si des faits ont été modifiés par une retouche de forme, ou si des réserves restent ouvertes. Une retouche de style peut modifier une date, un montant, une attribution ou le degré de certitude.

**À faire :** insérer une étape obligatoire après assemblage et avant publication. L’agent externe doit **signaler et proposer**, pas ajouter de faits; toute modification factuelle doit être renvoyée à la notice/source, journalisée et soumise à une nouvelle validation. L’approbation finale reste humaine. La procédure et un premier outil de contrôle local sont proposés plus bas et dans `tools/final_qa.py`.

## Méthode cible proposée

### Avant collecte — cadrage versionné

Pour chaque campagne/période, figer un manifeste indiquant période, fuseau horaire, date/heure d’arrêté, objectifs et besoins prioritaires, secteurs/territoires, sources attendues, seuils de sélection, version du schéma et version de méthode. Prioriser les questions, pas seulement les mots-clés.

### Collecte et sélection — conserver les états, mesurer les pertes

1. Capturer les métadonnées et la provenance dès l’entrée; dédoublonner au niveau article puis au niveau événement/fait, sans fusionner les preuves.
2. Maintenir une file distincte : retenir, surveiller, rejeter, à vérifier. Chaque décision comporte un motif et une version de règle.
3. Échantillonner les rejets pour estimer les faux négatifs; suivre les sources muettes ou en panne et le volume non extrait.
4. Garder l’archive exhaustive distincte du périmètre des faits à lire/rédiger. Une limite de quota doit laisser un statut « incomplet », pas une apparence de couverture totale.

### Extraction et vérification — une assertion, une preuve

Pour chaque fait : identifiant immuable, énoncé atomique, pays/territoire, secteur, B/O, dates séparées, acteur, chiffres avec unités et période, source(s), extrait de preuve, statut de vérification, confiance, doublons associés et historique de correction. Les faits dérivés de la même dépêche doivent être regroupés comme sources dépendantes. Les nombres et dates doivent être comparés à la preuve avant rédaction; les sujets à fort impact, allégations, décisions réglementaires et indicateurs macroéconomiques ont un niveau de revue renforcé.

### Rédaction — deux produits, un registre source

- **Brief décisionnel** : bref, Madagascar/EDBM d’abord, 5–10 faits prioritaires, pourquoi cela compte, horizon, opportunité/risque et action ou question pour la décision. Toute interprétation est séparée des faits et marquée comme analyse.
- **Recueil de faits** : corpus plus large, navigable, avec rubriques, compteurs définis, renvois stables et annexes de sources/méthode.

Les 12 rubriques peuvent rester utiles dans le recueil, mais le brief doit refléter O1–O4/B1–B8 et le périmètre prioritaire, pas le simple ordre de collecte.

### Étape externe de QA — nouvelle étape obligatoire

1. **Gel du candidat** : produire un candidat de diffusion et son SHA-256; inscrire période, méthode, lot de sources et heure d’arrêté.
2. **Précontrôle déterministe local** : présence des métadonnées, sections attendues selon le profil, références résolubles, dates hors période signalées, champs manquants, incohérences de compteurs et format. Les contrôles automatiques émettent des alertes; ils ne déclarent pas la vérité d’un fait.
3. **Revue par l’agent externe** : lui transmettre uniquement le candidat et les preuves nécessaires, pas de secrets, `.env`, jetons, données internes non autorisées ou accès non requis. Demander un retour JSON structuré avec empreinte du candidat, décision, contrôles, défauts, sévérité, localisation, preuve et correction suggérée. Éviter qu’il réécrive silencieusement le document.
4. **Résolution** : corriger les défauts bloquants/majeurs dans le registre source; toute modification produit une nouvelle empreinte et oblige à relancer les contrôles et la revue externe.
5. **Approbation humaine et publication** : publier seulement si la revue est liée à la version exacte, les critères obligatoires sont passés, aucun défaut bloquant/majeur n’est ouvert, et une personne responsable a approuvé. Conserver candidat, rapport QA, version finale et journal de corrections.
6. **Capitalisation** : mesurer défauts détectés avant/après QA, modifications factuelles indues, taux de relecture et durée; ajuster les règles sans confondre conformité de forme et exactitude de fond.

La connexion directe à l’agent externe n’est pas implémentable de manière fiable dans ce dépôt : son fournisseur, son protocole, ses identifiants et sa politique de données ne sont pas fournis. L’outil ajouté formalise donc un **contrat d’échange indépendant du fournisseur** (génération du paquet de revue et vérification de l’approbation/empreinte) sans inventer d’API ni publier automatiquement.

## Critères d’acceptation avant diffusion

- [ ] Période, fuseau, date d’arrêté, statut complet/incomplet et version de méthode visibles.
- [ ] Le nombre de notices examinées se réconcilie avec retenues, surveillées, rejetées et non traitées.
- [ ] Chaque fait publié a au moins un identifiant et une référence source résoluble; données et citations pointent vers les preuves exactes.
- [ ] Dates d’événement/publication/période statistique distinctes; événements futurs clairement marqués.
- [ ] Les faits prioritaires ont un besoin B1–B8 / objectif O1–O4; les exceptions ont un motif explicite.
- [ ] Aucune correction silencieuse, doublon d’événement non justifié ou interprétation présentée comme fait.
- [ ] Contrôles automatiques sans erreur bloquante; avertissements revus et consignés.
- [ ] L’agent externe a rendu un résultat structuré pour l’empreinte exacte; critères obligatoires passés, aucun défaut bloquant/majeur ouvert.
- [ ] Une personne responsable a approuvé cette même version; PDF et source éditable sont archivés ensemble.

## Plan d’action priorisé

**P0 — avant le prochain livrable**
1. Formaliser l’étape de QA externe et le responsable de l’approbation.
2. Figer un candidat et lier rapport externe, document et version par empreinte.
3. Ajouter un statut provisoire/incomplet et un contrôle de date future.
4. Stabiliser une seule convention de citations et d’identifiants.

**P1 — 1 à 2 cycles**
1. Réconcilier le README Data Factory ancien avec la méthode de novembre; archiver les éléments retirés.
2. Mettre en place le manifeste par édition et le dictionnaire des KPI.
3. Générer un brief décisionnel distinct du recueil, avec B/O et territoire explicites.
4. Séparer source, corroboration, preuve et confiance dans la base.

**P2 — amélioration continue**
1. Évaluer les faux négatifs via revue d’échantillons de rejets et analyses des corrections.
2. Mesurer couverture, fraîcheur, qualité de provenance, exactitude échantillonnée et charge de lecture.
3. Définir rétention, droits, sécurité de transfert vers l’agent externe et procédure de retrait/correction.

## Limites de l’audit

Le dépôt de code fourni dans cette session ne contient qu’un README initial de 7 octets; les scripts de collecte, base SQLite, configurations, prompts et tests cités dans Drive ne sont pas dans ce checkout. Je n’ai donc pas pu confirmer les comportements réels du pipeline ni auditer ses calculs, ses permissions ou ses journaux. Le contrôle ajouté dans ce dépôt est une base d’intégration pour l’étape finale, pas une intégration au pipeline de production distant.
