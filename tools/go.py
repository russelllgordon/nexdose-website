"""Short tracking links: nexdose.app/go/<source>/ is counted in Cloudflare, then forwards.
Default target is the App Store (tagged with the campaign); ?to=/path sends to that page instead."""
from page import SOURCES, store_link, write

BEACON = """<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "7fc7dd84de7d45c392822e8bfa5e17fb"}'></script><!-- End Cloudflare Web Analytics -->"""

for s in SOURCES:
    dest = "/" if s == "app" else store_link(s)
    write(f"go/{s}/", f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nexdose</title>
<meta name="robots" content="noindex">
<meta name="description" content="A simple, private shot tracker for iPhone. Tap to log, rotate injection sites, get reminders. No account, no ads.">
<meta property="og:type" content="website">
<meta property="og:title" content="Nexdose: Simple, Private Shot Tracker for iPhone">
<meta property="og:description" content="Tap to log, rotate injection sites, get reminders. No account, no ads, and your data stays on your phone.">
<meta property="og:url" content="https://www.nexdose.app/">
<meta property="og:site_name" content="Nexdose">
<meta property="og:image" content="https://www.nexdose.app/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://www.nexdose.app/assets/og-image.jpg">
<link rel="canonical" href="https://www.nexdose.app/">
<style>body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:#fff;color:#1d1433;display:grid;place-items:center;min-height:100vh;margin:0;padding:16px;text-align:center}}@media (prefers-color-scheme:dark){{body{{background:#140c26;color:#f1ecfb}}}}a{{color:#6a3fd6}}</style>
<script>(function(){{var d="{dest}",t=new URLSearchParams(location.search).get("to");if(t&&t.charAt(0)=="/"&&t.charAt(1)!="/")d=t;document.addEventListener("DOMContentLoaded",function(){{document.getElementById("c").href=d}});setTimeout(function(){{location.replace(d)}},700)}})()</script>
</head>
<body><p>Opening Nexdose&hellip; <a id="c" href="{dest}">Continue</a></p>
{BEACON}
</body>
</html>
''')
