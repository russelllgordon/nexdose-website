from page import render, write, APPSTORE
rows = [
 ("One-tap logging, calendar and list views",1,1),
 ("Scheduling and reminders",1,1),
 ("Simple body map (12 sites)",1,1),
 ("Weight, body fat and muscle tracking",1,1),
 ("CSV export",1,1),
 ("Siri, widgets and Apple Watch",1,1),
 ("Detailed body map (72 sites)",0,1),
 ("PDF report for your provider",0,1),
 ("Cycle scheduling (on and off cycles)",0,1),
 ("Weight import from CSV and Apple Health",0,1),
 ("Notes and symptoms after a shot",0,1),
 ("Auto dose-up (titration plans)",0,1),
 ("Supply tracking for pens and vials",0,1),
 ("Levels (half-life graph)",0,1),
]
def c(v): return '<span class="check" aria-label="Included">&#10003;</span>' if v else '<span aria-label="Not included">&ndash;</span>'
tr = "".join(f"<tr><td>{n}</td><td>{c(f)}</td><td>{c(p)}</td></tr>" for n,f,p in rows)
body = f'''
<section class="hero"><div class="wrap">
<h1>Nexdose Plus</h1>
<p class="lead">One purchase. $14.99. No subscription, ever. Shared with your family through Family Sharing.</p>
<a class="btn" href="{APPSTORE}">Get Nexdose free</a>
<p class="note">Download free, then unlock Plus inside the app whenever you're ready.</p>
</div></section>
<section class="alt"><div class="wrap plus-grid">
<div class="prose">
<h2>Free and Plus compared</h2>
<table class="compare">
<thead><tr><th>Feature</th><th>Free</th><th>Plus</th></tr></thead>
<tbody>{tr}</tbody>
</table>
</div>
<figure class="shot plus-shot"><picture><source srcset="../assets/shots/plus.webp" type="image/webp"><img src="../assets/shots/plus.jpg" alt="Support Nexdose screen listing free core features and Nexdose Plus features" width="660" height="1434" loading="lazy"></picture></figure>
</div></section>
<section><div class="wrap prose">
<h2>Questions about Plus</h2>
<details><summary>Is Plus a subscription?</summary><p>No. Plus is a single $14.99 purchase. You pay once and keep it.</p></details>
<details><summary>Can my partner or family use it?</summary><p>Yes. Plus works with Apple Family Sharing, so everyone in your family group gets it.</p></details>
<details><summary>I installed Nexdose 1.0. Do I need to buy Plus?</summary><p>No. If you first installed version 1.0, Plus is yours free as a thank-you.</p></details>
<details><summary>What does the Tip Jar do?</summary><p>Nothing extra. Tips of $1.99, $4.99 or $9.99 are an optional way to say thanks and don't unlock anything.</p></details>
<details><summary>Does Plus change my privacy?</summary><p>No. Purchases go through Apple. Nexdose still has no account, no ads and no tracking.</p></details>
</div></section>
'''
write("plus/", render("plus/", "Nexdose Plus: One-Time $14.99, No Subscription",
 "Compare Nexdose Free and Plus. Plus adds dose-up plans, Levels, supply tracking, PDF reports and more for a one-time $14.99 with Family Sharing.", body))
