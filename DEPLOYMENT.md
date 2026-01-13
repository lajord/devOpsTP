# Guide de déploiement GitHub Pages

## Configuration complétée ✅

Les fichiers suivants ont été configurés pour le déploiement:

1. ✅ `web/vite.config.ts` - Configuration Vite avec base URL
2. ✅ `.github/workflows/deploy.yml` - Workflow de déploiement automatique
3. ✅ `api/main.py` - CORS configuré pour GitHub Pages
4. ✅ `web/public/.nojekyll` - Évite le traitement Jekyll

---

## Étapes pour activer GitHub Pages

### 1. Push votre code sur GitHub

```bash
git add .
git commit -m "Configure GitHub Pages deployment"
git push origin main
```

### 2. Activer GitHub Pages dans les settings

1. Allez sur https://github.com/lajord/devOpsTP
2. Cliquez sur **Settings**
3. Dans le menu de gauche, cliquez sur **Pages**
4. Dans "Build and deployment":
   - Source: **GitHub Actions**
5. Cliquez sur **Save**

### 3. Déclencher le déploiement

Le workflow se lance automatiquement après le push. Vous pouvez suivre:
- Aller dans l'onglet **Actions**
- Cliquer sur le workflow "Deploy to GitHub Pages"
- Attendre 2-3 minutes

### 4. Accéder à votre site

Une fois déployé, votre site sera accessible à:
```
https://lajord.github.io/devOpsTP/
```

---

## Structure des workflows

### `ci.yml` - Tests et CI
- Se déclenche sur: push et PR
- Teste l'API avec pytest
- Vérifie le code avec Ruff
- Build les images Docker

### `deploy.yml` - Déploiement frontend
- Se déclenche sur: push vers main/master
- Build le frontend Vue.js
- Déploie sur GitHub Pages
- Site accessible publiquement

---

## Notes importantes

### API Backend
⚠️ GitHub Pages héberge uniquement le frontend (fichiers statiques).

Pour l'API backend, vous avez 2 options:

**Option 1: Héberger l'API ailleurs**
- Render.com (gratuit)
- Railway.app (gratuit avec limites)
- Fly.io (gratuit avec limites)

Puis mettre à jour l'URL de l'API dans le frontend.

**Option 2: Utiliser directement Open-Meteo**
Votre frontend peut appeler directement l'API Open-Meteo sans passer par votre backend:
```javascript
const response = await fetch('https://api.open-meteo.com/v1/forecast?...')
```

### CORS
Le CORS est déjà configuré pour accepter:
- `http://localhost:5173` (dev local)
- `https://lajord.github.io` (production)

---

## Troubleshooting

### Le site affiche une page blanche
- Vérifiez que `base: '/devOpsTP/'` dans vite.config.ts correspond au nom de votre repo
- Vérifiez les logs du workflow dans Actions

### Erreur 404 sur les assets
- Le `base` dans vite.config.ts doit correspondre au nom du repo
- Nettoyez le cache: `npm run build` en local

### Le workflow échoue
- Vérifiez que `package-lock.json` existe dans le dossier web
- Sinon, lancez `npm install` en local puis commitez

---

## Commandes utiles

```bash
# Build local pour tester
cd web
npm run build
npm run preview

# Voir le site local
# Ouvrir http://localhost:4173/devOpsTP/
```

---

## Prochaines étapes

1. ✅ Push le code
2. ✅ Activer GitHub Pages dans Settings
3. ✅ Attendre le déploiement (2-3 min)
4. ✅ Visiter https://lajord.github.io/devOpsTP/
5. 🚀 Profit!
