# MyWedGame — Changelog

## 2026-06-19 (suite) : Prix de base + menu

- Prix de base passé de 699€ à 499€ TTC. Grille des niveaux : 499 / 599 / 699 /
  799 (+100€ par niveau inchangé). Mis à jour partout : prix affiché, sélecteur
  du formulaire, meta description FR + EN, docs.
- Menu : libellés ton "romantique joueur". FR : Voir le jeu · Notre histoire ·
  Le prix · On crée le vôtre ? + CTA Je me lance. EN : See the game · Our story ·
  Pricing · Create yours + Let's go. Le sélecteur FR/EN navigue entre / et /en.

## 2026-06-19 : Favicon Google + version anglaise SEO

### Favicon
- Remplacement du favicon data-URI (illisible par le crawler Google) par de
  vrais fichiers : favicon.svg / favicon.png (512) / favicon-96 / favicon-32 /
  apple-touch-icon, référencés via `<link rel="icon">`. Coeur coral sur carré
  cream arrondi. Animation in-browser conservée, alignée sur le nouveau visuel.

### Version anglaise (/en)
- Vraie page anglaise à `/en` : `en.html` généré par `build.py` depuis
  `index.html` (source unique), `lang="en"` + title/meta/OG en anglais.
- Sélecteur FR/EN : navigation entre `/` et `/en` (URLs stables et indexables)
  au lieu d'une bascule en place via JS/localStorage.
- `hreflang` fr / en / x-default sur les deux pages + `canonical` self-referencing.
- `sitemap.xml` : 2 URLs avec alternates xhtml, `lastmod` 2026-06-19.
- `vercel.json` : `cleanUrls` + `trailingSlash:false` (sert `en.html` sur `/en`).
- og:image / twitter:image recalés sur `mywedgame.com` (au lieu de `vercel.app`).

### SEO
- Suppression de tous les tirets cadratins (title, OG, corps FR + EN).
- Search Console géré par Claude via `~/mywedgame-seo/gsc.py` (propriété Domaine
  `sc-domain:mywedgame.com`, robot Perso partagé, sitemap soumis).

## 2026-05-29 — Feedback amis : storytelling & pricing

- Prix retiré du hero (créer le désir avant d'annoncer le budget)
- Storytelling : "à trois jours du mariage" → "une semaine avant" (FR+EN)
- "En quelques heures" → "Quelques jours plus tard" (valoriser le travail)

## 2026-05-28 — Telegram bot + SEO

- Bot Telegram `@mywedgame_bot` créé + token sécurisé en env Vercel
- API serverless `/api/contact.js` : formulaire → message Telegram formaté
- Chat ID de Constantin (1274171252) en env var
- Formulaire envoie en POST JSON (plus de mailto)
- État loading + écran de succès post-envoi
- Pixel art cartes refait avec palette exacte du jeu Gustave & Caroline
  (palmier, Ford Raptor, couple, lagoon, crabe, cœur)
- OG image réduite à 200×200 (format compact WhatsApp comme Museum Studio)
- Google Search Console vérifié (méthode balise HTML)
- Sitemap.xml + robots.txt soumis
- `.fr` redirigé en 301 vers `.com` (anti duplicate content) via Vercel API
- Documentation projet : CLAUDE.md, ROADMAP.md, CHANGELOG.md

## 2026-05-27 — Lot 0 : Lancement

### Landing page
- Landing page single-file bilingue FR/EN
- Hero avec pixel hearts flottants animés
- Jeu Gustave & Caroline intégré en iframe avec overlay "Cliquez pour jouer"
- Section "Notre histoire" : récit genèse Île Maurice, citation mariés, stats
- 6 cartes personnalisation (décor, véhicule, personnages, musique, obstacles, collectibles)
- Pixel art dans les cartes avec couleurs exactes du jeu
- 3 étapes "Comment ça marche"
- Pricing unique : 699€ TTC + 100€/niveau
- Formulaire configurateur avec sélecteur collectibles pixel art (2 max)
- FAQ accordion (5 questions)
- Indication mute son (touche M / icône)

### Design
- Typographies : Terminal Grotesque (titres), Apfel Grotezk (logo, bold), DM Sans (corps)
- Logo : pixel heart SVG color-cycling (coral → gold → sage → blue → rose) + MyWEDGame
- Favicon : pixel heart dynamique, change couleur toutes les 2s
- Palette : cream, coral, gold, charcoal, dark
- Boutons arrondis (pill)
- 6 collectibles pixel art : cœur, alliance, bouquet, étoile, diamant, lettre d'amour

### Infra
- Repo GitHub : SuperKostia/mywedgame
- Deploy Vercel (auto sur push master)
- Domaines : mywedgame.com (principal) + mywedgame.fr (301 redirect)
- DNS IONOS : A → 76.76.21.21, CNAME www → cname.vercel-dns.com
- Bot Telegram @mywedgame_bot : réception demandes formulaire
- API serverless /api/contact.js (Vercel Function)

### SEO
- Meta tags : og:title, og:description, og:image, og:url, twitter:card
- OG image 200×200 (4 collectibles pixel art en grille 2×2)
- Google Search Console vérifié (balise HTML)
- Sitemap.xml + robots.txt soumis
- Redirect 301 .fr → .com (anti duplicate content)
