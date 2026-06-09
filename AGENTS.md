# AGENTS.md

Guide pour les agents Cursor travaillant sur ce dépôt.

## Nature du dépôt

Ce dépôt (`MEVENGUE/MEVENGUE`) est un **profil GitHub + hub de documentation portfolio**. Il ne contient pas d'application exécutable localement.

| Fichier | Rôle |
|---------|------|
| `README.md` | README de profil GitHub (affiché sur https://github.com/MEVENGUE) |
| `.devin/wiki.json` | Plan structuré du wiki portfolio (pages, projets, liens repo/démo) |

Les applications réelles (SUPFile, MentorGPT, 3D Canvas, etc.) vivent dans des **dépôts GitHub séparés** référencés dans `wiki.json`.

## Cursor Cloud specific instructions

### Services requis

**Aucun service local à démarrer** pour travailler sur ce dépôt. Pas de `npm install`, `docker compose`, ni serveur de dev.

| Service | Statut | Usage |
|---------|--------|-------|
| Git / éditeur | Requis | Édition du README et du wiki |
| Python 3 | Optionnel | Validation JSON (`python3 -m json.tool`) |
| Internet | Optionnel | Vérifier les liens externes (Vercel, GitHub) |

### Validation locale (équivalent lint/test)

```bash
# Valider le JSON du wiki
python3 -m json.tool .devin/wiki.json > /dev/null

# Vérifier la présence du contenu clé du profil
grep -q "MEVENGUE FRANCK" README.md
```

### Démos et sites hébergés (externes)

Les démos ne tournent pas dans ce dépôt. URLs principales :

- Site personnel : https://mevenguefranck-siteweb.vercel.app/
- DeepWiki : https://deepwiki.com/MEVENGUE/MEVENGUE
- SUPFile : https://supfile-webapp.vercel.app
- MentorGPT : https://supinfo-mentor-ai.vercel.app

Pour développer une application du portfolio, cloner le dépôt source correspondant (liens dans `.devin/wiki.json`) et suivre son propre README.

### Pièges à éviter

- Ne pas chercher `package.json`, `Dockerfile` ou `docker-compose` ici — ils n'existent pas.
- Les URLs dans `wiki.json` peuvent se terminer par un point dans le texte source (ex. `vercel.app.`). Nettoyer si vous extrayez des liens par regex.
- Modifier `README.md` impacte directement le profil GitHub public de l'utilisateur.
