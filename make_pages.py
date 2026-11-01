# -*- coding: utf-8 -*-
"""Builds index.html (fr) and en.html from one template."""
import os
import random

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "capy_shift")
EMAIL = "sebastien018@outlook.fr"

APPLE = '<svg viewBox="0 0 24 24"><path d="M16.4 12.7c0-2.5 2-3.7 2.1-3.8-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.3.8c1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9-.1 0-2.8-1-2.8-4.2zM14 5.3c.7-.8 1.2-2 1-3.1-1 0-2.2.7-2.9 1.5-.6.7-1.2 1.9-1 3 1.1.1 2.2-.6 2.9-1.4z"/></svg>'
PLAY = '<svg viewBox="0 0 24 24"><path d="M3.6 2.2c-.3.3-.4.7-.4 1.2v17.2c0 .5.1.9.4 1.2l9.5-9.8L3.6 2.2zm10.6 8.7l2.7-2.8L5.2 1.4l9 9.5zm0 2.2l-9 9.5 11.7-6.7-2.7-2.8zm6.1-2.6l-2.4-1.4-3 3 3 3 2.4-1.4c.8-.4.8-1.7 0-2.2z"/></svg>'
WAVE = '<svg class="wave{extra}" viewBox="0 0 1440 80" preserveAspectRatio="none"><path d="M0,40 C180,90 360,-10 540,35 C720,80 900,5 1080,40 C1260,75 1350,25 1440,40 L1440,90 L0,90 Z"/></svg>'
VIAL_COLORS = ["#ff6fae", "#5ab0ff", "#3ddc84", "#ffd25e", "#a77dff", "#ff9f43"]


def vial_svg(color: str) -> str:
    return (f'<svg class="vial" viewBox="0 0 34 56"><rect x="11" y="2" width="12" height="8" rx="3" fill="#c98f5b" stroke="#3d2619" stroke-width="3"/>'
            f'<path d="M12 10 L12 22 Q2 30 4 42 Q6 54 17 54 Q28 54 30 42 Q32 30 22 22 L22 10 Z" fill="#fff" stroke="#3d2619" stroke-width="3"/>'
            f'<path d="M6 38 Q8 52 17 52 Q26 52 28 38 Z" fill="{color}"/></svg>')


def floaties() -> str:
    rng = random.Random(4)
    items = []
    for k in range(16):
        left = rng.uniform(2, 96)
        top = rng.uniform(4, 88)
        delay = rng.uniform(0, 6)
        dur = rng.uniform(7, 12)
        style = f'left:{left:.0f}%;top:{top:.0f}%;animation-delay:-{delay:.1f}s;animation-duration:{dur:.1f}s'
        kind = k % 3
        if kind == 0:
            size = rng.randint(18, 54)
            items.append(f'<span class="floaty bubble" style="{style};width:{size}px;height:{size}px"></span>')
        elif kind == 1:
            items.append(f'<span class="floaty" style="{style};opacity:0.85">{vial_svg(VIAL_COLORS[k % len(VIAL_COLORS)])}</span>')
        else:
            items.append(f'<span class="floaty spark" style="{style}">✦</span>')
    return "\n\t".join(items)


TEXT = {
    "fr": {
        "file": "index.html", "html_lang": "fr",
        "title": "Capy Shift — le jeu kawaii de Dr Capy",
        "desc": "Aide Dr Capy à trier ses fioles ! Un jeu d'arcade kawaii et rapide pour iPhone et Android, gratuit.",
        "pill": "Nouveau jeu mobile ✦ gratuit",
        "lead": "Aide Dr Capy à trier ses fioles avant que le tapis ne s'emballe !",
        "soon": "Bientôt sur",
        "s1": "Glisse !", "s2": "Gratuit", "s3": "Kawaii ♥",
        "how_title": "Comment on joue ?", "how_sub": "Trois gestes, et c'est parti pour des parties endiablées.",
        "steps": [
            ("← →", "var(--pink)", "Glisse pour lancer", "À gauche ou à droite : chaque fiole doit finir dans le bon bac, selon la consigne du panneau."),
            ("↓", "var(--green)", "Repousse les caïmans", "Un caïman sur le tapis ? Glisse vers le bas avant qu'il n'atteigne Dr Capy !"),
            ("↑", "var(--orange)", "Attrape les bonus", "Glisse vers le haut pour croquer un yuzu et déclencher la frénésie !"),
        ],
        "shots_title": "Un labo <span class=\"hl\">plein de surprises</span>",
        "shots_sub": "Consignes qui changent, caïman géant, décors de folie…",
        "decor_title": "Débloque des <span class=\"hl\">décors</span>",
        "decor_sub": "Transforme le labo et habille Dr Capy comme tu veux.",
        "decors": [("lab", "Labo"), ("jungle", "Jungle"), ("beach", "Plage"), ("christmas", "Noël"), ("halloween", "Halloween"), ("space", "Espace")],
        "feat_title": "Pourquoi tu vas <span class=\"hl\">l'adorer</span>",
        "features": [
            ("pink", "!", "La consigne change", "Couleur, forme, bouchon, effet, chaud ou froid : reste concentré, ça accélère palier après palier."),
            ("green", "★", "Des bonus fous", "Yuzu frénétique, bain onsen, ami oiseau, bébés capys, bulle zen…"),
            ("orange", "♛", "Le caïman géant", "Au palier légendaire, un boss à repousser trois fois. Oseras-tu ?"),
            ("blue", "♥", "Habille ton capy", "Chapeaux, pyjamas, lunettes cœur, couronne, casque d'astronaute…"),
            ("purple", "✓", "Un défi chaque jour", "Récompense quotidienne, défis, missions, niveaux et partie du jour."),
            ("yellow", "✦", "En 16 langues", "Français, English, Español, Deutsch, 日本語, 한국어, 中文… et plus."),
        ],
        "shots": ["shot_fr_1.jpg", "shot_fr_2.jpg", "shot_fr_3.jpg", "shot_fr_5.jpg"],
        "alt": "Capture du jeu",
        "cta_title": "Prêt à aider Dr Capy ?", "cta_sub": "Capy Shift arrive très bientôt sur iPhone et Android. Gratuit !",
        "privacy": "Politique de confidentialité", "privacy_url": "privacy.html",
        "contact": "Contact",
        "other": "English", "other_url": "en.html",
    },
    "en": {
        "file": "en.html", "html_lang": "en",
        "title": "Capy Shift — Dr Capy's kawaii game",
        "desc": "Help Dr Capy sort the vials! A fast, kawaii arcade game for iPhone and Android, free.",
        "pill": "New mobile game ✦ free",
        "lead": "Help Dr Capy sort the vials before the belt goes wild!",
        "soon": "Coming soon on",
        "s1": "Swipe!", "s2": "Free", "s3": "Kawaii ♥",
        "how_title": "How do you play?", "how_sub": "Three gestures, and you're off for frantic runs.",
        "steps": [
            ("← →", "var(--pink)", "Swipe to throw", "Left or right: every vial must land in the right beaker, following the rule on the sign."),
            ("↓", "var(--green)", "Push back the caimans", "A caiman on the belt? Swipe down before it reaches Dr Capy!"),
            ("↑", "var(--orange)", "Grab the bonuses", "Swipe up to munch a yuzu and start a frenzy!"),
        ],
        "shots_title": "A lab <span class=\"hl\">full of surprises</span>",
        "shots_sub": "Changing rules, a giant caiman, crazy decors…",
        "decor_title": "Unlock <span class=\"hl\">decors</span>",
        "decor_sub": "Transform the lab and dress Dr Capy up your way.",
        "decors": [("lab", "Lab"), ("jungle", "Jungle"), ("beach", "Beach"), ("christmas", "Christmas"), ("halloween", "Halloween"), ("space", "Space")],
        "feat_title": "Why you'll <span class=\"hl\">love it</span>",
        "features": [
            ("pink", "!", "The rule keeps changing", "Color, shape, cork, effect, hot or cold: stay sharp, it speeds up stage after stage."),
            ("green", "★", "Crazy bonuses", "Yuzu frenzy, onsen bath, bird buddy, baby capys, zen bubble…"),
            ("orange", "♛", "The giant caiman", "On the legendary stage, a boss to push back three times. Dare you?"),
            ("blue", "♥", "Dress up your capy", "Hats, pyjamas, heart glasses, a crown, an astronaut helmet…"),
            ("purple", "✓", "A challenge every day", "Daily reward, challenges, missions, levels and the daily run."),
            ("yellow", "✦", "In 16 languages", "English, Français, Español, Deutsch, 日本語, 한국어, 中文… and more."),
        ],
        "shots": ["shot_en_1.jpg", "shot_en_2.jpg", "shot_en_3.jpg", "shot_en_5.jpg"],
        "alt": "Game screenshot",
        "cta_title": "Ready to help Dr Capy?", "cta_sub": "Capy Shift is coming very soon to iPhone and Android. Free!",
        "privacy": "Privacy policy", "privacy_url": "privacy-en.html",
        "contact": "Contact",
        "other": "Français", "other_url": "index.html",
    },
}

for lang, t in TEXT.items():
    badges = f'''<div class="badges">
					<span class="badge">{APPLE}<span><small>{t["soon"]}</small>App Store</span></span>
					<span class="badge">{PLAY}<span><small>{t["soon"]}</small>Google Play</span></span>
				</div>'''
    steps = "\n".join(
        f'\t\t\t<div class="step"><span class="num">{k + 1}</span><div class="gesture" style="color:{color}">{g}</div><h3>{h}</h3><p>{p}</p></div>'
        for k, (g, color, h, p) in enumerate(t["steps"]))
    features = "\n".join(
        f'\t\t\t<div class="feature"><div class="dot" style="background:var(--{c})">{icon}</div><h3>{h}</h3><p>{p}</p></div>'
        for c, icon, h, p in t["features"])
    shots = "\n".join(f'\t\t\t<img src="{s}" alt="{t["alt"]}" loading="lazy">' for s in t["shots"])
    decors = "\n".join(f'\t\t\t<div class="decor"><img src="decor2_{d}.jpg" alt="{name}" loading="lazy"><span>{name}</span></div>' for d, name in t["decors"])
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
<meta name="theme-color" content="#ffc4dc">
<link rel="icon" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero">
	{floaties()}
	<div class="wrap">
		<div class="top">
			<a class="brand" href="{t["file"]}"><img src="favicon.png" alt="">Yuzu Studio</a>
			<div class="lang"><a href="index.html"{fr_on}>FR</a><a href="en.html"{en_on}>EN</a></div>
		</div>
		<div class="hero-grid">
			<div>
				<span class="pill">{t["pill"]}</span>
				<h1><span class="c1">Capy</span><br><span class="c2">Shift</span></h1>
				<p class="lead">{t["lead"]}</p>
				{badges}
			</div>
			<div class="hero-art">
				<img class="portrait" src="hero.jpg" alt="Dr Capy">
				<div class="phone"><video src="gameplay.mp4" poster="poster.jpg" autoplay muted loop playsinline></video></div>
				<span class="sticker s1">{t["s1"]}</span>
				<span class="sticker s2">{t["s2"]}</span>
				<span class="sticker s3">{t["s3"]}</span>
			</div>
		</div>
	</div>
	{WAVE.format(extra="")}
</header>

<section>
	<div class="wrap">
		<h2>{t["how_title"]}</h2>
		<p class="sub">{t["how_sub"]}</p>
		<div class="steps">
{steps}
		</div>
	</div>
</section>

<section class="screens">
	<div class="wrap">
		<h2>{t["shots_title"]}</h2>
		<p class="sub">{t["shots_sub"]}</p>
		<div class="shots">
{shots}
		</div>
	</div>
</section>

<section>
	<div class="wrap">
		<h2>{t["decor_title"]}</h2>
		<p class="sub">{t["decor_sub"]}</p>
		<div class="decors">
{decors}
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

<section class="cta">
	<div class="wrap">
		<img src="apple-touch-icon.png" alt="">
		<h2>{t["cta_title"]}</h2>
		<p class="sub" style="margin-bottom:0">{t["cta_sub"]}</p>
		{badges}
	</div>
</section>

<footer>
	<div class="wrap">
		<nav><a href="{t["privacy_url"]}">{t["privacy"]}</a><a href="mailto:{EMAIL}">{t["contact"]} : {EMAIL}</a><a href="{t["other_url"]}">{t["other"]}</a></nav>
		<p>© 2026 Yuzu Studio</p>
	</div>
</footer>
</body>
</html>
'''
    if lang == "en":
        page = page.replace(f"{t['contact']} : {EMAIL}", f"{t['contact']}: {EMAIL}")
    with open(os.path.join(HERE, t["file"]), "w", encoding="utf-8") as f:
        f.write(page)
print("ok")
