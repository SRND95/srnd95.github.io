# -*- coding: utf-8 -*-
"""Builds index.html (fr) and en.html from one template."""
import os

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "capy_shift")

APPLE = '<svg viewBox="0 0 24 24"><path d="M16.4 12.7c0-2.5 2-3.7 2.1-3.8-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.3.8c1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9-.1 0-2.8-1-2.8-4.2zM14 5.3c.7-.8 1.2-2 1-3.1-1 0-2.2.7-2.9 1.5-.6.7-1.2 1.9-1 3 1.1.1 2.2-.6 2.9-1.4z"/></svg>'
PLAY = '<svg viewBox="0 0 24 24"><path d="M3.6 2.2c-.3.3-.4.7-.4 1.2v17.2c0 .5.1.9.4 1.2l9.5-9.8L3.6 2.2zm10.6 8.7l2.7-2.8L5.2 1.4l9 9.5zm0 2.2l-9 9.5 11.7-6.7-2.7-2.8zm6.1-2.6l-2.4-1.4-3 3 3 3 2.4-1.4c.8-.4.8-1.7 0-2.2z"/></svg>'

TEXT = {
    "fr": {
        "file": "index.html", "html_lang": "fr",
        "title": "Capy Shift — le jeu kawaii de Dr Capy",
        "desc": "Aide Dr Capy à trier ses fioles ! Un jeu d'arcade kawaii et rapide pour iPhone et Android.",
        "lead": "Aide Dr Capy à trier ses fioles avant que le tapis ne s'emballe !",
        "soon": "Bientôt sur", "free": "Gratuit",
        "s1": "Glisse !", "s2": "Kawaii !",
        "shots_title": "Un labo plein de surprises",
        "shots_sub": "Consignes qui changent, caïmans à repousser, décors à débloquer…",
        "feat_title": "Pourquoi tu vas l'adorer",
        "features": [
            ("pink", "↔", "Facile à prendre en main", "Glisse à gauche ou à droite pour lancer chaque fiole dans le bon bac. Une partie dure quelques minutes."),
            ("orange", "!", "La consigne change", "Couleur, forme, bouchon, effet, chaud ou froid : reste concentré, tout s'accélère palier après palier."),
            ("green", "↓", "Gare aux prédateurs", "Repousse les caïmans, l'anaconda… et le caïman géant du palier légendaire !"),
            ("yellow", "★", "Des bonus fous", "Yuzu frénétique, bain onsen, ami oiseau, bébés capys, bulle zen…"),
            ("blue", "♥", "Habille ton capy", "Chapeaux, tenues, lunettes, effets et décors : jungle, plage, Noël, espace…"),
            ("purple", "✓", "Un défi chaque jour", "Récompense quotidienne, défis du jour, missions et niveaux. En 16 langues."),
        ],
        "shots": ["shot_fr_1.jpg", "shot_fr_2.jpg", "shot_fr_3.jpg", "shot_fr_5.jpg"],
        "alt": "Capture du jeu",
        "privacy": "Politique de confidentialité", "privacy_url": "privacy.html",
        "other": "English", "other_url": "en.html",
    },
    "en": {
        "file": "en.html", "html_lang": "en",
        "title": "Capy Shift — Dr Capy's kawaii game",
        "desc": "Help Dr Capy sort the vials! A fast, kawaii arcade game for iPhone and Android.",
        "lead": "Help Dr Capy sort the vials before the belt goes wild!",
        "soon": "Coming soon on", "free": "Free",
        "s1": "Swipe!", "s2": "Kawaii!",
        "shots_title": "A lab full of surprises",
        "shots_sub": "Changing rules, caimans to push back, decors to unlock…",
        "feat_title": "Why you'll love it",
        "features": [
            ("pink", "↔", "Easy to pick up", "Swipe left or right to throw each vial into the right beaker. A run lasts a few minutes."),
            ("orange", "!", "The rule keeps changing", "Color, shape, cork, effect, hot or cold: stay sharp, it speeds up stage after stage."),
            ("green", "↓", "Watch out for predators", "Push back the caimans, the anaconda… and the giant caiman of the legendary stage!"),
            ("yellow", "★", "Crazy bonuses", "Yuzu frenzy, onsen bath, bird buddy, baby capys, zen bubble…"),
            ("blue", "♥", "Dress up your capy", "Hats, outfits, glasses, effects and decors: jungle, beach, Christmas, space…"),
            ("purple", "✓", "A challenge every day", "Daily reward, daily challenges, missions and levels. In 16 languages."),
        ],
        "shots": ["shot_en_1.jpg", "shot_en_2.jpg", "shot_en_3.jpg", "shot_en_5.jpg"],
        "alt": "Game screenshot",
        "privacy": "Privacy policy", "privacy_url": "privacy-en.html",
        "other": "Français", "other_url": "index.html",
    },
}

for lang, t in TEXT.items():
    features = "\n".join(
        f'\t\t\t<div class="feature"><div class="dot" style="background:var(--{c})">{icon}</div><h3>{h}</h3><p>{p}</p></div>'
        for c, icon, h, p in t["features"])
    shots = "\n".join(f'\t\t\t<img src="{s}" alt="{t["alt"]}" loading="lazy">' for s in t["shots"])
    fr_on = ' class="on"' if lang == "fr" else ""
    en_on = ' class="on"' if lang == "en" else ""
    page = f'''<!doctype html>
<html lang="{t["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta property="og:title" content="Capy Shift">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:image" content="https://srnd95.github.io/capy_shift/hero.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="hero">
	<div class="wrap">
		<div class="top">
			<a class="brand" href="{t["file"]}"><img src="favicon.png" alt="">Yuzu Studio</a>
			<div class="lang"><a href="index.html"{fr_on}>FR</a><a href="en.html"{en_on}>EN</a></div>
		</div>
		<div class="hero-grid">
			<div>
				<h1><span class="c1">Capy</span><br><span class="c2">Shift</span></h1>
				<p class="lead">{t["lead"]}</p>
				<div class="badges">
					<span class="badge soon">{APPLE}<span><small>{t["soon"]}</small>App Store</span></span>
					<span class="badge soon">{PLAY}<span><small>{t["soon"]}</small>Google Play</span></span>
				</div>
			</div>
			<div class="hero-art">
				<img src="hero.jpg" alt="Dr Capy">
				<span class="sticker s1">{t["s1"]}</span>
				<span class="sticker s2">{t["free"]}</span>
			</div>
		</div>
	</div>
</div>

<section>
	<div class="wrap">
		<h2>{t["shots_title"]}</h2>
		<p class="sub">{t["shots_sub"]}</p>
		<div class="shots">
{shots}
		</div>
	</div>
</section>

<section class="features">
	<div class="wrap">
		<h2>{t["feat_title"]}</h2>
		<p class="sub">&nbsp;</p>
		<div class="grid">
{features}
		</div>
	</div>
</section>

<footer>
	<div class="wrap">
		<nav><a href="{t["privacy_url"]}">{t["privacy"]}</a><a href="mailto:sebastien018@outlook.fr">Contact : sebastien018@outlook.fr</a><a href="{t["other_url"]}">{t["other"]}</a></nav>
		<p>© 2026 Yuzu Studio</p>
	</div>
</footer>
</body>
</html>
'''
    with open(os.path.join(HERE, t["file"]), "w", encoding="utf-8") as f:
        f.write(page)
print("ok")
