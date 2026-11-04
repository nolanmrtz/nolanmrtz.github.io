#!/usr/bin/env python3
"""Portfolio de Nolan Moritz : nom géant, compétences qui défilent, projets en lignes, accent cuivre.
Génère index.html (français) et en/index.html (anglais).
Modifier les textes dans T ci-dessous, puis lancer : python3 build.py"""
import os, html

EMAIL = "nolan.moritz@epitech.eu"
PHONE = "07 82 64 47 57"
PHONE_INTL = "+33782644757"
GITHUB = "https://github.com/nolanmrtz"
SITE_URL = "https://frontcraft.fr"
DEMO = "https://frontcraft.fr/demos/{}/"

T = {
"fr": dict(
  lang="fr", other="en", other_label="EN", other_name="English", other_href="en/", root="",
  title="Nolan Moritz · Étudiant à Epitech, dev web, jeux et outils",
  description="Portfolio de Nolan Moritz, étudiant en 1re année à Epitech Mulhouse (PGE) et fondateur du studio web Frontcraft. Recherche un stage de 2e année.",
  skip="Aller au contenu", tagline="Epitech PGE · Frontcraft",
  nav=[("À propos", "#apropos"), ("Projets", "#projets"), ("Contact", "#contact")], available="Disponible pour un stage",
  role="{DEV}", portrait_k="Nolan Moritz", portrait_r="Mulhouse · FR", logo_alt="Logo {E} de Nolan Moritz",
  intro="Étudiant à Epitech Mulhouse et fondateur de Frontcraft. Je code des sites sur mesure, des jeux et des outils, et je les mets en ligne.",
  status="Je cherche un stage de 2e année, puis une alternance.",
  btn_work="Voir mes projets", btn_contact="Me contacter", scroll="Défiler",
  about_k="Qui je suis", about_h="À propos",
  about_p=["Étudiant en <strong>1re année à Epitech Mulhouse</strong>, je touche à tout : <strong>dev web, jeux vidéo, cybersécurité et IA</strong>. Ce qui me plaît, c'est de comprendre comment ça marche, puis de le construire.",
           "En dehors des cours, j'ai lancé <strong>Frontcraft</strong>, mon studio de sites web : de vrais clients, de vrais délais, et des sites en ligne.",
           "Pour moi, on apprend en <strong>construisant et en livrant</strong>. Un projet fini vaut mieux que dix idées."],
  stats=[("1re année", "À Epitech"), ("15", "Projets construits"), ("Web · Game · Cyber · IA", "Mes domaines"), ("2026", "Frontcraft créé")],
  skills_k="Ce que j'utilise", skills_h="Compétences",
  skills=["HTML / CSS", "JavaScript", "Python", "C / CSFML", "Luau / Roblox", "Supabase / SQL", "WebGL / GLSL", "Swift", "Git / Linux", "Claude / IA"],
  proj_k="Ce que j'ai codé", proj_h="Projets", open_lbl="Ouvrir",
  projects=[
    dict(name="Epidash", kick="Outil perso · macOS", tags=["Python", "Swift"], desc="Mon tableau de bord Epitech : projets, crédits et planning, au même endroit.", url=None, img=None),
    dict(name="My Hunter", kick="Projet Epitech · Jeu", tags=["C", "CSFML", "Makefile"], desc="Un jeu de tir en C, codé avec la CSFML : boucle de jeu, sprites, événements souris.", url=None, img=None),
    dict(name="Steal a Mutant", kick="Jeu Roblox", tags=["Luau", "Roblox Studio"], desc="Un jeu Roblox que je code en Luau, du gameplay aux scripts serveur.", url=None, img=None),
    dict(name="Espace client", kick="Web · Sécurité", tags=["Supabase", "PostgreSQL", "RLS"], desc="Connexion par lien e-mail, et des règles de sécurité par ligne : chaque client ne voit que son propre projet.", url=None, img=None),
    dict(name="Ordinateur 3D", kick="Web · Graphisme", tags=["WebGL2", "GLSL", "JavaScript"], desc="Un ordinateur portable en 3D dessiné entièrement par un shader (ray marching), sans bibliothèque. Sur l'accueil de frontcraft.fr.", url=SITE_URL, img=None),
    dict(name="Générateur de site", kick="Outil · Multilingue", tags=["Python", "JSON", "HTML"], desc="Mon générateur de site statique : pages, traductions FR, EN, DE, liens hreflang et sitemap à partir de modèles.", url=None, img=None),
    dict(name="Six sites démo", kick="Web · Projets concept", tags=["HTML", "CSS", "JavaScript"], desc="Restaurant, boutique, appli de rendez-vous, photographe, salle de sport : six sites complets aux marques fictives.", url=DEMO.format("restaurant"), img="demo-restaurant",
         demos=[("restaurant", "Maison Opale"), ("mode", "Atelier Nuance"), ("agenda", "Créneau"), ("meditation", "Nuit claire"), ("photographe", "Heure Bleue"), ("sport", "Kinetik Club")]),
  ],
  out_k="Hors des cours", out_h="En vrai, pour de vrais clients",
  out_p="Ce qui ne tient pas dans un bulletin : un studio à faire tourner, et des sites livrés à des clients.",
  to_phone="Vue téléphone", to_desk="Vue ordinateur", visit="Voir le site", soon="En ligne prochainement",
  out=[
    dict(id="frontcraft", kick="Entrepreneuriat · Fondateur", name="Frontcraft", when="2026 · En cours", url=SITE_URL,
         desc="Mon studio de création de sites web dans le Haut-Rhin. Offre et prix, domaine, e-mail pro, site en trois langues hébergé sur Cloudflare, référencement local et prospection des commerces autour de moi.",
         tags=["Python", "HTML", "CSS", "JavaScript", "Cloudflare"], alt_d="Accueil de frontcraft.fr sur ordinateur.", alt_p="Accueil de frontcraft.fr sur téléphone."),
    dict(id="cigogne", kick="Client · Location saisonnière", name="La Cigogne Rêveuse", when="2026", url=None,
         desc="Remplacer un site issu d'un modèle par un site sur mesure qui donne envie de réserver en direct : quatre langues, réservation avec prix calculé en direct, carte des lieux à découvrir.",
         tags=["HTML", "CSS", "JavaScript", "Lodgify"], alt_d="Accueil de La Cigogne Rêveuse sur ordinateur.", alt_p="La Cigogne Rêveuse sur téléphone."),
    dict(id="marjorie", kick="Client · Sophrologue", name="Marjorie Moritz", when="2026", url=None,
         desc="Un site plus clair et plus apaisant pour une sophrologue : plusieurs pages, avis Google intégrés, exercice de respiration interactif et prise de rendez-vous.",
         tags=["HTML", "CSS", "JavaScript", "Apps Script"], alt_d="Accueil du site de Marjorie Moritz sur ordinateur.", alt_p="Le site de Marjorie Moritz sur téléphone."),
  ],
  contact_k="Contact", contact_h="Un stage ? Parlons-en.",
  contact_p="Un stage, une alternance, un projet ou juste une question : écrivez-moi, je réponds vite.",
  f_name="Nom", f_mail="E-mail", f_subj="Sujet", f_msg="Message", f_send="Envoyer", city="Mulhouse, Haut-Rhin",
  foot="© 2026 Nolan Moritz", top="Retour en haut ↑",
),
"en": dict(
  lang="en", other="fr", other_label="FR", other_name="Français", other_href="../", root="../",
  title="Nolan Moritz · Epitech student, web, games and tools",
  description="Portfolio of Nolan Moritz, first-year student at Epitech Mulhouse (PGE) and founder of the Frontcraft web studio. Looking for a second-year internship.",
  skip="Skip to content", tagline="Epitech PGE · Frontcraft",
  nav=[("About", "#apropos"), ("Projects", "#projets"), ("Contact", "#contact")], available="Open to internships",
  role="{DEV}", portrait_k="Nolan Moritz", portrait_r="Mulhouse · FR", logo_alt="Nolan Moritz's {E} logo",
  intro="Student at Epitech Mulhouse and founder of Frontcraft. I build custom websites, games and tools, and I ship them.",
  status="Looking for a second-year internship, then a work-study contract.",
  btn_work="See my work", btn_contact="Get in touch", scroll="Scroll",
  about_k="Who I am", about_h="About",
  about_p=["A <strong>first-year student at Epitech Mulhouse</strong>, I explore several fields: <strong>web, game development, cybersecurity and AI</strong>. I like understanding how things work, then building them.",
           "Outside school, I launched <strong>Frontcraft</strong>, my web design studio: real clients, real deadlines, real sites online.",
           "To me, you learn by <strong>building and shipping</strong>. One finished project beats ten ideas."],
  stats=[("1st year", "At Epitech"), ("15", "Projects built"), ("Web · Game · Cyber · AI", "My fields"), ("2026", "Founded Frontcraft")],
  skills_k="What I use", skills_h="Skills",
  skills=["HTML / CSS", "JavaScript", "Python", "C / CSFML", "Luau / Roblox", "Supabase / SQL", "WebGL / GLSL", "Swift", "Git / Linux", "Claude / AI"],
  proj_k="What I've coded", proj_h="Projects", open_lbl="Open",
  projects=[
    dict(name="Epidash", kick="Personal tool · macOS", tags=["Python", "Swift"], desc="My Epitech dashboard: projects, credits and schedule in one place.", url=None, img=None),
    dict(name="My Hunter", kick="Epitech project · Game", tags=["C", "CSFML", "Makefile"], desc="A shooting game in C built with CSFML: game loop, sprites, mouse events.", url=None, img=None),
    dict(name="Steal a Mutant", kick="Roblox game", tags=["Luau", "Roblox Studio"], desc="A Roblox game I'm building in Luau, from gameplay to server scripts.", url=None, img=None),
    dict(name="Client area", kick="Web · Security", tags=["Supabase", "PostgreSQL", "RLS"], desc="Email link sign-in and row-level security: each client only ever sees their own project.", url=None, img=None),
    dict(name="3D laptop", kick="Web · Graphics", tags=["WebGL2", "GLSL", "JavaScript"], desc="A 3D laptop drawn entirely by a shader (ray marching), with no library. On the frontcraft.fr home page.", url=SITE_URL, img=None),
    dict(name="Site generator", kick="Tool · Multilingual", tags=["Python", "JSON", "HTML"], desc="My static site generator: pages, FR, EN and DE translations, hreflang links and sitemap from templates.", url=None, img=None),
    dict(name="Six demo sites", kick="Web · Concept projects", tags=["HTML", "CSS", "JavaScript"], desc="Restaurant, fashion shop, booking app, photographer, gym: six complete sites for fictional brands.", url=DEMO.format("restaurant"), img="demo-restaurant",
         demos=[("restaurant", "Maison Opale"), ("mode", "Atelier Nuance"), ("agenda", "Créneau"), ("meditation", "Nuit claire"), ("photographe", "Heure Bleue"), ("sport", "Kinetik Club")]),
  ],
  out_k="Beyond class", out_h="For real, for real clients",
  out_p="What doesn't fit on a report card: a studio to run, and sites delivered to clients.",
  to_phone="Phone view", to_desk="Desktop view", visit="Visit the site", soon="Going live soon",
  out=[
    dict(id="frontcraft", kick="Entrepreneurship · Founder", name="Frontcraft", when="2026 · Ongoing", url=SITE_URL,
         desc="My web design studio in Alsace. Offer and pricing, domain, pro email, a three-language site hosted on Cloudflare, local SEO and reaching out to nearby businesses.",
         tags=["Python", "HTML", "CSS", "JavaScript", "Cloudflare"], alt_d="frontcraft.fr home page on a computer.", alt_p="frontcraft.fr home page on a phone."),
    dict(id="cigogne", kick="Client · Holiday rental", name="La Cigogne Rêveuse", when="2026", url=None,
         desc="Replacing a template-based site with a custom one that makes guests book directly: four languages, booking with a live price, a map of places to visit.",
         tags=["HTML", "CSS", "JavaScript", "Lodgify"], alt_d="La Cigogne Rêveuse home page on a computer.", alt_p="La Cigogne Rêveuse on a phone."),
    dict(id="marjorie", kick="Client · Sophrologist", name="Marjorie Moritz", when="2026", url=None,
         desc="A clearer, calmer site for a sophrologist: several pages, Google reviews, an interactive breathing exercise and online booking.",
         tags=["HTML", "CSS", "JavaScript", "Apps Script"], alt_d="Marjorie Moritz's home page on a computer.", alt_p="Marjorie Moritz's site on a phone."),
  ],
  contact_k="Contact", contact_h="An internship? Let's talk.",
  contact_p="An internship, a work-study role, a project or just a question: write to me, I reply quickly.",
  f_name="Name", f_mail="Email", f_subj="Subject", f_msg="Message", f_send="Send", city="Mulhouse, France",
  foot="© 2026 Nolan Moritz", top="Back to top ↑",
),
}

e = html.escape
ext = lambda u: ' target="_blank" rel="noopener"' if u and u.startswith("http") else ""
k = lambda txt, cls="": f'<p class="k {cls}">{e(txt)}</p>'
chips = lambda items: '<ul class="chips">' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"

def page(t):
    r, L = t["root"], t["lang"]
    img = lambda n: f"{r}img/{n}.jpg"
    nav = "".join(f'<a class="hide-m" href="{h}">{e(l)}</a>' for l, h in t["nav"])
    stats = "".join(f'<div class="stat" data-rise style="--i:{i}"><p class="big">{e(a)}</p><p class="k plain">{e(b)}</p></div>' for i, (a, b) in enumerate(t["stats"]))
    marquee = "".join(f"<span>{e(s)}</span>" for s in t["skills"])
    rows = []
    for i, p in enumerate(t["projects"], 1):
        body = f'<p>{e(p["desc"])}</p>'
        if p.get("demos"):
            body += '<div class="demos">' + "".join(f'<a href="{DEMO.format(d)}" target="_blank" rel="noopener"><span class="thumb"><img src="{img("demo-" + d)}" alt="" width="1000" height="750" loading="lazy"></span>{e(n)}</a>' for d, n in p["demos"]) + "</div>"
        if p["url"]:
            body += f'<p><a class="link" href="{p["url"]}" target="_blank" rel="noopener">{e(t["open_lbl"])} ↗</a></p>'
        prev = f'<img src="{img(p["img"])}" alt="" width="1000" height="750" loading="lazy">' if p.get("img") else ""
        rows.append(f'''<details class="row" data-rise>
      <summary><span class="num">{i:02d}</span><span class="title">{e(p["name"])}</span>{chips(p["tags"])}<span class="arrow" aria-hidden="true">↗</span></summary>
      <div class="body">{k(p["kick"])}{body}</div>
      <div class="preview" aria-hidden="true">{prev}{k(p["kick"])}<p class="pt">{e(p["name"])}</p><p class="pd">{e(p["desc"])}</p></div>
    </details>''')
    outs = []
    for i, o in enumerate(t["out"], 1):
        sid = o["id"]
        act = (f'<a class="sq" href="{o["url"]}" target="_blank" rel="noopener">{e(t["visit"])} ↗</a>' if o["url"] else f'<span class="sq off">{e(t["soon"])}</span>')
        outs.append(f'''<article class="venture" data-rise>
      <span class="num">{i:02d}</span>
      <div class="v-text">
        <div class="v-head">{k(o["kick"])}<p class="k when">{e(o["when"])}</p></div>
        <h3>{e(o["name"])}</h3><p>{e(o["desc"])}</p>{chips(o["tags"])}
        <div class="btns">{act}<button type="button" class="sq ghost" data-view-btn data-phone="{e(t["to_phone"])}" data-desk="{e(t["to_desk"])}" aria-pressed="false">{e(t["to_phone"])}</button></div>
      </div>
      <div class="v-shot" data-view="desk">
        <img class="desk" src="{img(sid + "-ordinateur")}" alt="{e(o["alt_d"])}" width="1100" height="1100" loading="lazy">
        <img class="phone" src="{img(sid + "-telephone")}" alt="{e(o["alt_p"])}" width="520" height="1040" loading="lazy">
      </div>
    </article>''')
    return f'''<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#070605">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["description"])}">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["description"])}">
<meta property="og:image" content="{r}img/logo-e.webp">
<link rel="alternate" hreflang="fr" href="{r}">
<link rel="alternate" hreflang="en" href="{r}en/">
<link rel="preload" href="{r}fonts/bebas-neue.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r}fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}style.css">
<link rel="icon" href="{r}img/logo-e.webp" type="image/webp">
<script>document.documentElement.classList.add('js')</script>
</head>
<body id="haut">
<a class="skip" href="#contenu">{e(t["skip"])}</a>
<div class="progress" aria-hidden="true"></div>
<header class="top">
  <a class="brand" href="#haut" aria-label="Nolan Moritz"><span class="badge"><img src="{r}img/logo-e.webp" alt="" width="320" height="320"></span><span class="k plain hide-m">{e(t["tagline"])}</span></a>
  <nav class="nav" aria-label="Menu">
    <a class="lang" href="{t["other_href"]}" hreflang="{t["other"]}" lang="{t["other"]}" aria-label="{e(t["other_name"])}">{t["other_label"]}</a>
    <span class="live" title="{e(t["available"])}"><span class="sr">{e(t["available"])}</span></span>
    {nav}
  </nav>
</header>
<main id="contenu">
  <section class="hero wrap" aria-labelledby="h1">
    <h1 id="h1" class="name"><span class="l1">Nolan</span><span class="l2">Moritz</span><span class="l3"><b>{{</b>Dev<b>}}</b></span></h1>
    <figure class="portrait">
      <figcaption class="cap-top"><span class="k plain">{e(t["portrait_k"])}</span><span class="k plain">Epitech · PGE</span></figcaption>
      <div class="disc"><img src="{r}img/logo-e.webp" alt="{e(t["logo_alt"])}" width="320" height="320" fetchpriority="high"></div>
      <div class="cap-bot"><span class="k plain">{e(t["status"])}</span><span class="k plain">{e(t["portrait_r"])}</span></div>
    </figure>
    <div class="hero-foot">
      <p class="intro">{e(t["intro"])}</p>
      <div class="btns"><a class="sq" href="#projets">{e(t["btn_work"])} →</a><a class="sq ghost" href="#contact">{e(t["btn_contact"])} →</a></div>
    </div>
  </section>

  <section class="sec wrap about" id="apropos" aria-labelledby="about-h">
    {k(t["about_k"])}<h2 id="about-h">{e(t["about_h"])}</h2>
    <div class="about-grid">
      <div class="about-text">{"".join(f"<p>{x}</p>" for x in t["about_p"])}</div>
      <div class="stats">{stats}</div>
    </div>
  </section>

  <section class="sec skills" aria-labelledby="skills-h">
    <div class="wrap">{k(t["skills_k"])}<h2 id="skills-h">{e(t["skills_h"])}</h2></div>
    <div class="marquee"><div class="track">{marquee}</div><div class="track" aria-hidden="true">{marquee}</div></div>
  </section>

  <section class="sec wrap" id="projets" aria-labelledby="proj-h">
    {k(t["proj_k"])}<h2 id="proj-h">{e(t["proj_h"])}</h2>
    <div class="rows">{"".join(rows)}</div>
  </section>

  <section class="sec wrap" id="hors" aria-labelledby="out-h">
    {k(t["out_k"])}<h2 id="out-h">{e(t["out_h"])}</h2>
    <p class="lede">{e(t["out_p"])}</p>
    <div class="ventures">{"".join(outs)}</div>
  </section>

  <section class="sec wrap contact" id="contact" aria-labelledby="contact-h">
    <div class="c-left">
      {k(t["contact_k"])}<h2 id="contact-h">{e(t["contact_h"])}</h2>
      {k("E-mail", "plain gap")}<a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
      <p class="lede">{e(t["contact_p"])}</p>
      <p class="k plain avail"><span class="dot" aria-hidden="true"></span>{e(t["available"])}</p>
    </div>
    <form class="c-form" data-mailto="{EMAIL}" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <label><span class="k plain">{e(t["f_name"])}</span><input name="nom" autocomplete="name" required></label>
      <label><span class="k plain">{e(t["f_mail"])}</span><input name="email" type="email" autocomplete="email" required></label>
      <label><span class="k plain">{e(t["f_subj"])}</span><input name="sujet"></label>
      <label><span class="k plain">{e(t["f_msg"])}</span><textarea name="message" rows="5" required></textarea></label>
      <button class="sq" type="submit">{e(t["f_send"])} →</button>
    </form>
    <ul class="links">
      <li><a class="k plain" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a></li>
      <li><a class="k plain" href="{SITE_URL}" target="_blank" rel="noopener">frontcraft.fr ↗</a></li>
      <li><a class="k plain" href="tel:{PHONE_INTL}">{PHONE}</a></li>
      <li class="k plain">{e(t["city"])}</li>
    </ul>
  </section>
</main>
<footer class="foot wrap"><span class="k plain">{e(t["foot"])}</span><span class="k plain avail"><span class="dot" aria-hidden="true"></span>{e(t["available"])}</span><a class="k plain" href="#haut">{e(t["top"])}</a></footer>
<script src="{r}main.js" defer></script>
</body></html>'''

here = os.path.dirname(os.path.abspath(__file__))
for lang, t in T.items():
    out = os.path.join(here, "index.html" if lang == "fr" else "en/index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(page(t))
    print("écrit", out)
