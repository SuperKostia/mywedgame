# MyWedGame — Landing Page

## Projet
Landing page bilingue (FR/EN) pour **MyWedGame** — service de création de jeux vidéo pixel-art sur mesure pour les mariages. Le jeu de démonstration (Gustave & Caroline, Île Maurice) est intégré en iframe.

## Stack
- **HTML/CSS/JS** single-file (`index.html`), zéro framework, zéro build step
- **Vercel** : hébergement + serverless function (`/api/contact.js`)
- **Telegram Bot** : réception des demandes via `@mywedgame_bot`
- **Polices** : Terminal Grotesque (titres), Apfel Grotezk (logo/corps bold), DM Sans (corps)
- **Domaines** : `mywedgame.com` (principal), `mywedgame.fr` (301 → .com)
- **DNS** : IONOS, A record → 76.76.21.21, CNAME www → cname.vercel-dns.com
- **Git** : github.com/SuperKostia/mywedgame → auto-deploy Vercel

## Commandes
```bash
# Dev local
npx serve .

# Deploy (auto via git push, ou manuel)
vercel --prod
```

## Structure
```
index.html          — Landing page complète (HTML + CSS + JS inline)
api/contact.js      — Serverless function : form → Telegram
fonts/              — Terminal Grotesque + Apfel Grotezk (woff2, self-hosted)
og-image.png        — Image OG 200×200 (4 collectibles pixel art)
og-template.html    — Template pour générer og-image via Playwright
collectibles.html   — Showcase des 6 collectibles pixel art
sitemap.xml         — Sitemap pour Google
robots.txt          — Robots.txt
```

## Env vars (Vercel)
- `TELEGRAM_BOT_TOKEN` — Token du bot @mywedgame_bot
- `TELEGRAM_CHAT_ID` — Chat ID de Constantin (1274171252)

## DA & Design
- **Palette** : cream #FAF7F2, coral #D4736C, gold #C9A96E, charcoal #2A2724, dark #1C1917
- **Logo** : pixel heart SVG (color-cycling) + "My" Apfel Grotezk + "WED" Terminal Grotesque (coral) + "Game" Apfel Grotezk
- **Favicon** : pixel heart SVG, change de couleur toutes les 2s (JS)
- **Pixel art** : couleurs extraites du jeu Gustave & Caroline (palette.ts)
- **Boutons** : arrondis (pill), pas carrés
- **Sections** : Hero → Démo (iframe jeu) → Notre histoire → Personnalisation (6 cartes) → Comment ça marche → Tarif → Formulaire → FAQ → Footer

## Pricing
- **699€ TTC** : jeu sur mesure, 1 niveau
- **+100€** par niveau supplémentaire
- Formulaire avec sélecteur de niveaux (1-4) et collectibles (6 options, 2 max)

## Collectibles disponibles
Cœur, Alliance, Bouquet, Étoile, Diamant, Lettre d'amour — pixel art SVG inline

## SEO
- Google Search Console vérifié (meta tag)
- Sitemap soumis
- og:image, twitter:card, robots.txt
- `.fr` redirige en 301 vers `.com` (pas de duplicate content)

## Décisions prises
- "Wed" comme abréviation de wedding dans le nom → validé, c'est un nom de marque
- Domaine principal = `.com`, `.fr` en redirect 301
- Terminal Grotesque pour les titres (H1, H2) — cohérent avec le logo
- Formulaire envoie sur Telegram, pas mailto
- Délai de création annoncé : 3-4 jours (pas semaines)
- Boutons arrondis préférés aux carrés retro
- OG image : format compact 200×200 (4 collectibles en grille 2×2)
