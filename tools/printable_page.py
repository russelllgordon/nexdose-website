"""Free printables page: links to the PDFs made by printables.py."""
from page import render, write, store_link

SHEETS = [
    ("nexdose-shot-log", "Shot log", "Two pages, 52 rows: a full year of weekly shots. Columns for date, time, medicine, dose, site number, weight and notes.",
     "Preview of the Nexdose shot log: a table with date, time, medicine, dose, site, weight and notes columns"),
    ("nexdose-site-rotation-chart", "Site rotation chart", "A body outline with the 12 numbered sites from the Nexdose body map, and boxes to write the date each time you use a site.",
     "Preview of the Nexdose site rotation chart: a body outline with 12 numbered injection sites and a table of date boxes"),
]

cards = "".join(f'''<div class="card printable">
<a href="../assets/printables/{f}.pdf"><picture><source srcset="../assets/printables/{f}-preview.webp" type="image/webp"><img src="../assets/printables/{f}-preview.jpg" alt="{alt}" width="600" height="776" loading="lazy"></picture></a>
<h3>{t}</h3><p>{d}</p>
<a class="btn secondary" href="../assets/printables/{f}.pdf" download>Download PDF</a>
</div>''' for f, t, d, alt in SHEETS)

body = f'''
<section class="alt"><div class="wrap">
<h1 class="page-h1">Free printable shot log and site rotation chart</h1>
<p class="lead page-lead">Prefer paper, or want a backup on the fridge? Print these two free sheets to keep track of every shot: the date, the dose, the site and your weight. No sign-up, no email.</p>
<div class="grid printables">{cards}</div>
<p class="note">US Letter PDFs. They also print fine on A4.</p>
</div></section>

<section><div class="wrap prose">
<h2>How to use them together</h2>
<ol>
<li>Before each shot, look at the rotation chart for the site with the oldest date, or one you haven't used yet.</li>
<li>Write today's date in that site's next empty box.</li>
<li>Add a row to the shot log with the date, dose and that site's number. Add your weight if you're tracking it.</li>
</ol>
<p>Works for a weekly GLP-1 shot such as semaglutide or tirzepatide, and for daily or other injections too.</p>

<h2>Want it done for you?</h2>
<p>Paper works, until you forget where you left it. Nexdose is the same idea on your iPhone: it <a href="../shot-schedule/">puts every shot on a calendar</a>, reminds you on shot day, logs a shot in one tap, and <a href="../injection-site-rotation/">shows where to inject next</a> on a body map with the same 12 sites. Free, with no account and no ads.</p>
<p><a class="btn" href="{store_link('web-printable')}">Get Nexdose free</a></p>
<p class="note">These sheets are for your own records. They don't give medical advice. Ask your healthcare provider which sites suit your medicine and how to space your shots.</p>
</div></section>
'''

write("printable-shot-log", render("printable-shot-log/",
    "Free Printable Shot Log and Injection Site Rotation Chart (PDF) | Nexdose",
    "Free printable injection log and site rotation chart. Two PDFs to track your weekly GLP-1 shot or any injection on paper: date, dose, site and weight. No sign-up.",
    body))
