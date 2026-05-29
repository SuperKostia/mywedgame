# MyWedGame — Changelog

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
