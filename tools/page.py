import os, sys
SITE = "https://www.nexdose.app"
NAV = [("", "Home"), ("plus/", "Plus"), ("how-to/", "How-to"), ("about/", "About"), ("support/", "Support")]
FOOT = [("privacy-policy/", "Privacy Policy"), ("support/", "Support")]
APPSTORE = "https://apps.apple.com/app/id6824021246"
# App Store Connect provider token (Analytics > Acquisition > Campaigns). Empty until Russ shares it.
PT = "129632683"
# Channels that get their own short link, nexdose.app/go/<name>/, counted as a page in Cloudflare.
SOURCES = ["app", "telegram", "reddit", "instagram", "threads", "facebook", "tiktok", "youtube", "x", "email", "producthunt"]

def store_link(campaign):
    """App Store link tagged with a campaign, so App Store Connect shows installs per channel."""
    return f"{APPSTORE}?pt={PT}&ct={campaign}&mt=8" if PT else APPSTORE

# Cloudflare Web Analytics ignores query strings, so ?utm_source=x visits are sent through /go/x/ to be counted.
UTM_JS = "<script>(function(){try{var q=new URLSearchParams(location.search),s=(q.get('utm_source')||'').toLowerCase();if(%s.indexOf(s)>-1&&location.pathname.indexOf('/go/')<0){location.replace('/go/'+s+'/?to='+encodeURIComponent(location.pathname+location.hash))}}catch(e){}})()</script>" % str(SOURCES).replace(" ", "")

def render(slug, title, desc, body, extra_head=""):
    depth = slug.count("/")
    r = "../" * depth
    nav = "".join(f'<a href="{r}{p}"{" aria-current=page" if p==slug else ""}>{n}</a>' for p, n in NAV)
    foot = "".join(f'<a href="{r}{p}">{n}</a>' for p, n in FOOT)
    url = f"{SITE}/{slug}"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{UTM_JS}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Nexdose">
<meta name="twitter:card" content="summary_large_image">
<meta name="apple-itunes-app" content="app-id=6824021246">
<meta name="theme-color" content="#6a3fd6">
<link rel="icon" href="{r}assets/favicon-32.png" type="image/png">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Five iPhones showing Nexdose: calendar, peptide list, levels, weight and supply">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<link rel="stylesheet" href="{r}assets/style.css?v=7">
{extra_head}</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{r}"><img src="{r}assets/logo-96.png" alt="" width="32" height="32">Nexdose</a>
<nav class="main" aria-label="Main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap">
<div>&copy; 2026 Russell Gordon &middot; St. George, Utah<br>Nexdose is a tracking tool only. It does not provide medical advice. Always follow your healthcare provider's guidance.</div>
<nav aria-label="Footer">{foot}<a href="mailto:contact@nexdose.app">contact@nexdose.app</a></nav>
</div></footer>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "7fc7dd84de7d45c392822e8bfa5e17fb"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
'''

def write(slug, html):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), slug, "index.html") if slug else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(html)
