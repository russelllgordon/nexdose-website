from page import render, write, APPSTORE
ld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"MobileApplication","name":"Nexdose","operatingSystem":"iOS 18 or later","applicationCategory":"HealthApplication","description":"A simple, private injection tracker for weekly GLP-1 shots and other injections. One-tap logging, site rotation, reminders and reports. No account, no ads.","offers":[{"@type":"Offer","price":"0","priceCurrency":"USD","name":"Nexdose"},{"@type":"Offer","price":"14.99","priceCurrency":"USD","name":"Nexdose Plus (one-time purchase)"}],"author":{"@type":"Person","name":"Russell Gordon"},"url":"https://www.nexdose.app/"}
</script>
'''
shots = [("calendar","Nexdose calendar showing logged and upcoming shots for the month","See your month at a glance"),("calendar-logged","Calendar with a Logged message and Undo button after tapping a shot","Log a shot in one tap"),("today","Today's Shots list with the next injection site for each","Never miss a shot"),("upcoming","Upcoming Shots list showing the next dose and site for each peptide","See what's coming up"),("body-map","Body map showing recent injection sites by zone","Rotate sites without thinking"),("levels","Levels graph showing estimated levels between shots","See your levels"),("weight","Weight log with goal progress and chart","Track your progress")]
def fig(f,a,c,kind="",w=660,ht=1434):
    return f'<figure class="shot {kind}"><picture><source srcset="assets/shots/{f}.webp" type="image/webp"><img src="assets/shots/{f}.jpg" alt="{a}" width="{w}" height="{ht}" loading="lazy"></picture><figcaption>{c}</figcaption></figure>'
def ph(label,c,kind=""):
    return f'<figure class="shot {kind}"><div class="ph">{label}<br><small>Screenshot coming</small></div><figcaption>{c}</figcaption></figure>'
rows = [
 ("iPhone","The whole app, built to be quick.", "".join(fig(*s) for s in shots)),
 ("Widgets","Log from your Home Screen or Lock Screen without opening the app.", fig("widget-home","Home Screen widget listing next shots with check buttons","Your next shots on the Home Screen",w=660,ht=1435)+fig("widget-logged","Home Screen widget showing a shot marked Logged","Tap the check to log",w=660,ht=1435)+fig("widget-lock","Lock Screen widget showing the next shot and injection site","Your next shot on the Lock Screen")),
 ("Apple Watch","See today's shots and log from your wrist.", fig("watch-today","Apple Watch showing today's shots with check buttons","Today's shots on your wrist","watch",396,484)+fig("watch-logged","Apple Watch confirming a shot was logged, with the next shot below","Tap to log","watch",396,484)+fig("watch-complication","Watch face with the Nexdose complication showing the next shot day","Your next shot on your watch face","watch",396,484)),
 ("iPhone Duo","Made for the big screen: your calendar and today's shots side by side.", fig("duo-open","iPhone Duo unfolded with the calendar and Today's Shots side by side","Calendar and today, side by side","wide",1100,774)+fig("duo-body-map","iPhone Duo unfolded showing the full-size body map","A bigger body map","wide",1100,774)+fig("duo-cover","iPhone Duo cover screen with the calendar and today's shots","Works folded too","",660,960)),
 ("Siri","Log a shot with your voice.", ph("Siri logging a shot","Just ask Siri")),
]
shot_html = "".join(f'<div class="shot-row"><h3>{t}</h3><p class="row-intro">{d}</p><div class="shots">{s}</div></div>' for t,d,s in rows)
features = [
 ("Log in one tap","Tap a due shot to log it. Or log from a Lock Screen widget, your Apple Watch, or Siri."),
 ("Smart site rotation","A body map shows where you've injected and suggests the next spot, so you don't keep using the same one."),
 ("Flexible schedules","Weekly, daily, monthly, every weekday or custom. Several doses a day, on and off cycles, and mid-cycle starts."),
 ("Reminders","Optional notifications at each dose time. Move or skip a single dose without changing your schedule."),
 ("Dose increases","Plan your titration once, and Nexdose moves you up to the next dose on schedule. <span class=tag>Plus</span>"),
 ("Weight and body stats","Track weight, body fat and muscle against a goal, with charts from one month to all time."),
 ("Levels","See a half-life graph of your estimated levels between shots. <span class=tag>Plus</span>"),
 ("Supply tracking","Know how much is left in each pen or vial before you run out. <span class=tag>Plus</span>"),
 ("Reports for your provider","Export your history as a clean PDF report <span class=tag>Plus</span> or a CSV file."),
]
feat_html = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t,d in features)
body = f'''
<section class="hero"><div class="wrap">
<h1>Track every dose.<br>Rotate every site.</h1>
<p class="lead">Nexdose is a simple, private tracker for your weekly GLP-1 shot and other injections. Log a shot in one tap, see where to inject next, and never lose track of your schedule.</p>
<ul class="badges"><li>No account</li><li>No ads</li><li>No subscription</li><li>Your data stays on your iPhone</li></ul>
<a class="btn" href="{APPSTORE}">Download on the App Store</a>
<p class="note">Free for iPhone. Works with semaglutide (Wegovy, Ozempic), tirzepatide (Mounjaro, Zepbound) and other injections.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>See it in action</h2>
{shot_html}
</div></section>

<section><div class="wrap">
<h2>Everything you need for your shots. Nothing you don't.</h2>
<p class="section-intro">Nexdose was built by someone who injects on a schedule and got tired of trackers that were too complicated and asked for too much.</p>
<div class="grid">{feat_html}</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Private by design</h2>
<p class="section-intro">No sign-up. No ads. No personal questions. No analytics or tracking in the app. Everything you enter is stored on your iPhone, and optionally in your own private iCloud. We never see your data.</p>
<a href="privacy-policy/">Read the privacy policy</a>
</div></section>

<section><div class="wrap">
<h2>Free to use. Plus is yours to keep.</h2>
<p class="section-intro">The core app is free with no ads. Nexdose Plus adds advanced features for a one-time $14.99, shared with your family through Family Sharing. Never a subscription.</p>
<a class="btn secondary" href="plus/">Compare Free and Plus</a>
</div></section>

<section class="alt" id="get"><div class="wrap" style="text-align:center">
<h2>Get Nexdose</h2>
<p class="section-intro" style="margin-left:auto;margin-right:auto">Free on iPhone, with an Apple Watch app. Requires iOS 18 or later.</p>
<a class="btn" href="{APPSTORE}">Download on the App Store</a>
<p class="note">Questions? Visit <a href="support/">Support</a> or email <a href="mailto:contact@nexdose.app">contact@nexdose.app</a>.</p>
</div></section>
'''
write("", render("", "Nexdose: Simple, Private GLP-1 Shot Tracker for iPhone",
 "Track your weekly GLP-1 shot in one tap. Site rotation, reminders, dose increases and reports. No account, no ads, no subscription.", body, ld))
