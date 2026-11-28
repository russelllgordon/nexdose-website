"""Search landing pages: one page per thing people search for. Text comes from Russ's approved drafts doc."""
from page import render, write, store_link

PAGES = [
    ("glp-1-shot-tracker/", "GLP-1 shot tracker"),
    ("injection-site-rotation/", "Injection site rotation"),
    ("shot-schedule/", "Shot schedule calendar"),
    ("cycle-scheduler/", "On and off cycles"),
    ("printable-shot-log/", "Free printable shot log"),
]
BLURB = {
    "glp-1-shot-tracker/": "Never miss your weekly shot.",
    "injection-site-rotation/": "Know where to inject next.",
    "shot-schedule/": "Schedule it once. Nexdose remembers.",
    "cycle-scheduler/": "Cycles that run themselves.",
    "printable-shot-log/": "A free PDF log and site chart to print.",
}
PLUS = '<a class="tag" href="../plus/" title="Part of Nexdose Plus">Plus</a>'


def shot(f, alt):
    return (f'<figure class="shot plus-shot"><picture><source srcset="../assets/shots/{f}.webp" type="image/webp">'
            f'<img src="../assets/shots/{f}.jpg" alt="{alt}" width="660" height="1434"></picture></figure>')


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def page(slug, title, desc, h1, intro, img, alt, sections, campaign, note="", faq=None):
    btn = f'<a class="btn" href="{store_link(campaign)}">Get Nexdose free</a>'
    secs = "".join(f"<h2>{h}</h2>{b}" for h, b in sections)
    faq_html = ld = ""
    if faq:
        faq_html = "<h2>Questions</h2>" + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
        import json
        ld = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]
        }) + "</script>\n"
    more = "".join(f'<a class="card" href="../{s}" style="text-decoration:none;color:inherit"><h3>{n}</h3><p>{BLURB[s]}</p></a>'
                   for s, n in PAGES if s != slug)
    note_html = f'<p class="note">{note}</p>' if note else ""
    body = f'''
<section><div class="wrap landing">
<div class="l-head">
<h1>{h1}</h1>
<p class="lead">{intro}</p>
{btn}
<p class="note">Free for iPhone, with an Apple Watch app. No account, no ads, no subscription.</p>
</div>
<div class="l-shot">{shot(img, alt)}</div>
<div class="l-body prose">
{secs}
{faq_html}
{note_html}
<p style="margin-top:32px">{btn}</p>
</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>More from Nexdose</h2>
<div class="grid">{more}</div>
</div></section>
'''
    write(slug.rstrip("/"), render(slug, title, desc, body, ld))


page("glp-1-shot-tracker/",
     "GLP-1 Shot Tracker for iPhone: Log Your Weekly Shot | Nexdose",
     "Track your weekly GLP-1 shot in one tap. Nexdose schedules it on a calendar, reminds you on shot day, rotates sites and tracks your weight. Free, private, no account.",
     "Never miss a shot",
     "Let's face it, you're busy and a once-a-week shot is easy to forget. Nexdose puts your GLP-1 shot on a calendar, reminds you on shot day, and logs it in one tap. Next week, you'll know.",
     "calendar-logged", "Nexdose calendar with a weekly shot just logged",
     [("Built around a weekly shot", ul([
         "<strong>Set it once.</strong> Choose Weekly and pick the day and time you inject. Start from your last shot and Nexdose picks up from there.",
         "<strong>Shot-day reminder</strong> at the time you choose.",
         "<strong>Life happens.</strong> Move a single dose to another day, or skip it, and your schedule carries on.",
         "<strong>Log from anywhere:</strong> a single tap in the app, tap a Lock Screen widget, tap your Apple Watch, or tell Siri to do it for you.",
     ])),
      ("Track what changes", ul([
          "<strong>View weight loss, body fat loss and muscle gain</strong> against a goal, with charts from one month to all time.",
          f"<strong>Dose increases.</strong> Plan your steps up once, and Nexdose moves you to the next dose on schedule. {PLUS}",
          f"<strong>Pens and vials.</strong> Know how much is left before you run out. {PLUS}",
          f"<strong>Reports for your provider.</strong> Export your history as a CSV, or as a clean PDF. {PLUS}",
      ])),
      ("Private by design", "<p>No account, no ads, and no tracking. Your data stays on your iPhone, with optional backup to your own iCloud.</p>"),
      ("Works with", "<p>Semaglutide, tirzepatide and other weekly or daily injections. Nexdose is a tracking tool and doesn't give medical advice. It helps you follow your provider's instructions.</p>"),
      ],
     "web-glp1",
     faq=[("Is it free?", "Yes. The core tracker is free. Plus is a one-time purchase, not a subscription."),
          ("Does it work for daily injections too?", "Yes: daily, weekly, monthly, every weekday or custom, with up to 3 doses a day.")])

page("injection-site-rotation/",
     "Injection Site Rotation Tracker for iPhone | Nexdose",
     "See every injection site you've used on a body map and know where to go next. Nexdose remembers your sites so you don't have to. Free, private, no account.",
     "Know where to inject next",
     "Left thigh or right? Was that last week or the week before? Nexdose keeps a body map of every site you've used and shows where you went last, so rotating takes no thought.",
     "body-map", "Nexdose body map showing recent injection sites by zone",
     [("How it works", ol([
         "Log a shot, and Nexdose records the site with it.",
         "The body map shows which areas you've used recently.",
         "Your next shot comes with a suggested site. Want a different one? Tap the body picture on that shot and pick it.",
     ])),
      ("Two levels of detail", ul([
          "<strong>Simple map (free):</strong> 12 sites, including the abdomen, thighs and arms.",
          f"<strong>Detailed map:</strong> 72 sites, for people who want finer control. {PLUS}",
      ])),
      ("Several injections? Each keeps its own history", "<p>Every peptide or medicine in Nexdose has its own schedule and its own site history, so you can see where each one went.</p>"),
      ("Don't need it?", "<p>Turn site tracking off for any single peptide and use Nexdose just for scheduling and reminders.</p>"),
      ],
     "web-sites",
     note="Nexdose records the sites you choose. It doesn't give medical advice about where or how to inject. Make sure to follow your provider's guidance.")

page("shot-schedule/",
     "Injection Schedule and Peptide Calendar App for iPhone | Nexdose",
     "Put every injection on one calendar, set it once, and let Nexdose remember. Daily, weekly or custom schedules, reminders, and moves or skips that don't break your plan.",
     "Schedule it once. Nexdose remembers.",
     "Nexdose is a calendar first. Add each peptide or medicine and your preferred schedule, and every dose appears on the right day, now and months ahead, so you won't forget.",
     "calendar", "Nexdose month calendar with four peptides, each with its own color and symbol, and Today's Shots below",
     [("Any schedule", ul([
         "Daily, weekly, monthly, every weekday, or custom",
         "Up to 3 doses a day, each at its own time",
         "Start mid-cycle: pick the day of your first dose and Nexdose works out where you are",
         f'On and off cycles {PLUS}: see <a href="../cycle-scheduler/">cycle scheduling</a>',
     ])),
      ("Your whole routine in one view", "<p>Several peptides? Each gets its own color and symbol on the calendar, so a busy week reads at a glance. Today's Shots lists what's due now, with the site for each.</p>"),
      ("Reminders that follow your plan", "<p>Get a notification at each dose time. Move one dose or skip it, and only that dose changes. The rest of your schedule stays put.</p>"),
      (f"Plans that change on schedule {PLUS}", ul([
          "<strong>Dose increases:</strong> plan your steps once and Nexdose moves you up on the right date.",
          "<strong>Supply:</strong> Nexdose counts down your pens and vials as you log, so you know when to reorder.",
      ])),
      ("See it anywhere", "<p>Widgets on your Home Screen and Lock Screen, an Apple Watch app and complication, and Siri.</p>"),
      ],
     "web-schedule")

page("cycle-scheduler/",
     "Peptide Cycle Tracker: Schedule On and Off Cycles | Nexdose",
     "Set your on and off cycles once, such as 8 weeks on and 4 weeks off, and Nexdose follows them on your calendar. No more counting weeks in your head.",
     "Cycles that run themselves",
     "Many protocols call for cycling off. Keeping track of when to stop, and when to start again, is a hassle, and harder still with several peptides on different cycles. Nexdose does the counting.",
     "cycle", "Nexdose schedule screen set to every weekday at 10 PM, for 8 weeks, then a 4 week break, repeating",
     [("Set it once", "<p>It works like a repeating event in your calendar app, all on one screen:</p>" + ol([
         "Choose how often: weekly, daily, or every weekday (Monday to Friday), with up to 3 doses a day.",
         "Set how long you're on, for example <strong>For 8 weeks</strong>.",
         "Turn on <strong>Then take a break</strong> and choose how long, for example <strong>4 weeks</strong>.",
         "Nexdose shows &ldquo;8 weeks on, 4 weeks off, then it starts again&rdquo; and keeps going until you change it.",
     ]) + "<p>Already partway through? Pick the day of your first dose this cycle, and Nexdose tells you where you are, for example &ldquo;Today is week 4 of 8 in this cycle&rdquo;.</p>"),
      ("Different cycles, side by side", "<p>Each peptide keeps its own cycle, so one can be on while another is off, all on the same calendar.</p>"),
      ("Weekdays on, weekends off", "<p>Some schedules pulse: doses on weekdays and a break at weekends. Choose <strong>Every weekday</strong> and Nexdose handles the weekend gaps, inside your longer on and off cycle too.</p>"),
      (f"Part of Nexdose Plus {PLUS}", '<p>Cycle scheduling is a Plus feature, a one-time purchase that also includes dose increases, supply tracking, Levels and PDF reports. <a href="../plus/">See Plus</a></p>'),
      ],
     "web-cycles",
     note="Nexdose follows the cycle you enter. It doesn't recommend cycle lengths or give medical advice.")
