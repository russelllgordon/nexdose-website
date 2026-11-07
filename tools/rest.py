from page import render, write
about = '''
<section><div class="wrap prose">
<h1>Why I built Nexdose</h1>
<div class="draft">Placeholder: Russ's original About page text goes here, copied from the Google Site so it's in his own words.</div>
<p>I'm a peptide user, and I built Nexdose for people like me, and for friends and family with the same frustrations: rotating injection sites, remembering doses and schedules, and planning cycles.</p>
<h2>Why I deleted other apps before I even got started</h2>
<ul>
<li><strong>Personal questions.</strong> I wanted a tracker, not a questionnaire about my goals, health and weight.</li>
<li><strong>Create an account.</strong> A log on my phone shouldn't need a sign-up.</li>
<li><strong>Too complex.</strong> Cluttered graphs, tables and logs. Nexdose uses a simple calendar.</li>
<li><strong>All the best stuff costs.</strong> Nexdose's free version covers the basics, and Plus is a one-time purchase, not a subscription.</li>
</ul>
<h2>I'd like to hear from you</h2>
<p>Send feedback from inside the app or email <a href="mailto:contact@nexdose.app">contact@nexdose.app</a>.</p>
</div></section>
'''
write("about/", render("about/", "About Nexdose: Built by a Peptide User",
 "Why Nexdose exists: a simple, private injection tracker built by a peptide user who was tired of apps that asked too much.", about))
