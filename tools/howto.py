from page import render, write
body = '''
<section><div class="wrap prose">
<h1>How to use Nexdose</h1>
<p class="section-intro">Short guides for setting up your shots and getting the most from Nexdose. Features marked <a class="tag" href="../plus/" title="Part of Nexdose Plus">Plus</a> are part of <a href="../plus/">Nexdose Plus</a>, a one-time purchase. Everything else is free.</p>
<nav class="toc" aria-label="On this page"><strong>On this page</strong><ul>
<li><a href="#add">Add your first shot</a></li>
<li><a href="#schedule">Set a schedule</a></li>
<li><a href="#log">Log a shot</a></li>
<li><a href="#move">Move or skip a dose</a></li>
<li><a href="#rotate">Rotate injection sites</a></li>
<li><a href="#badges">Badges and your Trophy case</a></li>
<li><a href="#reminders">Turn on reminders</a></li>
<li><a href="#weight">Track weight and body stats</a></li>
<li><a href="#export">Export a report</a></li>
<li><a href="#sync">Sync and lock</a></li>
<li><a href="#plus">Plus features: dose-up, supply and Levels</a></li>
</ul></nav>

<h2 id="add">Add your first shot</h2>
<p>Tap the <strong>+</strong> button and Nexdose walks you through it, one step at a time:</p>
<ol>
<li><strong>Goal:</strong> name the peptide or medicine and choose what you're taking it for.</li>
<li><strong>Schedule:</strong> choose how often you take it (see below).</li>
<li><strong>Cycle:</strong> set on and off cycles, or skip this step <a class="tag" href="../plus/" title="Part of Nexdose Plus">Plus</a>.</li>
<li><strong>Injection sites:</strong> choose the areas you use, or turn site tracking off for this peptide.</li>
<li><strong>Extras:</strong> anything else you'd like to add. These are optional.</li>
</ol>
<p>To change it later, open the <strong>All Peptides</strong> page. Each row shows the goal, schedule, cycle, sites and supply, and editing uses the same pages as setup, one for each part.</p>
<p>On the calendar, the <strong>+</strong> button opens the same steps. On a past day, it also lets you log a shot you took earlier.</p>

<h2 id="schedule">Set a schedule</h2>
<p>Choose <strong>Daily</strong>, <strong>Weekly</strong>, <strong>Monthly</strong>, <strong>Every weekday</strong> or <strong>Custom</strong>. The day of the week comes from the start date you pick, so for a weekly GLP-1 shot, set the start date to the day you inject.</p>
<ul>
<li><strong>Already mid-cycle?</strong> Pick the day you took the first dose of this cycle as the start date, and Nexdose works out where you are.</li>
<li><strong>More than one dose a day?</strong> Set Doses per day to 2 or 3 and choose a time for each.</li>
</ul>

<h2 id="log">Log a shot</h2>
<p>On the home screen, tap a shot that's due. Want a different site? Tap the body picture on its row first. Missed logging one? Tap a past day on the calendar and log it there.</p>
<p>You can also log without opening the app:</p>
<ul>
<li><strong>Widgets:</strong> add the Nexdose widget to your Home Screen or Lock Screen, then tap the check.</li>
<li><strong>Apple Watch:</strong> open Nexdose on your watch and tap the check. The watch-face complication shows your next shot.</li>
<li><strong>Siri:</strong> ask Siri to log your shot in Nexdose.</li>
</ul>
<p>Logged by mistake? Tap <strong>Undo</strong> in the message that appears.</p>

<h2 id="move">Move or skip a dose</h2>
<p>Swipe right on a due shot and choose <strong>Move</strong> to pick a new date and time for just that dose, or skip it if you missed it. You can also press and hold a due shot for <strong>Edit</strong>, <strong>Move or skip</strong>, and <strong>Remove</strong>. Your regular schedule carries on unchanged.</p>

<h2 id="rotate">Rotate injection sites</h2>
<p>Nexdose suggests your next site on a body map and shows which areas you've used recently. Free includes a simple map with 12 sites, and Plus adds a detailed map with 72 <a class="tag" href="../plus/" title="Part of Nexdose Plus">Plus</a>. Each site area shows a small body map with its zones highlighted, so it's easy to see what you're choosing. Don't need sites for a peptide? Turn site tracking off for just that one.</p>

<h2 id="badges">Badges and your Trophy case</h2>
<p>Nexdose celebrates your consistency with badges for streaks, doses logged, time with Nexdose, on-time shots, site rotation and more. When you reach a milestone, a small banner lets you know.</p>
<p>To see everything you've earned, tap the circle at the top of <strong>Today</strong> to open your Trophy case. You can add a photo or choose an avatar, and add a nickname. It all stays on your phone, with no account.</p>

<h2 id="reminders">Turn on reminders</h2>
<p>Turn on <strong>Remind me at each dose time</strong> in a peptide's schedule. If reminders don't appear, check iPhone Settings &gt; Notifications &gt; Nexdose.</p>

<h2 id="weight">Track weight and body stats</h2>
<p>Log your weight, body fat and muscle, set a goal, and see your progress over 1M, 3M, 6M, 1Y or All. With Plus, import past weights from a CSV file or Apple Health <a class="tag" href="../plus/" title="Part of Nexdose Plus">Plus</a>.</p>

<h2 id="export">Export a report</h2>
<p>Open the menu and choose <strong>Export</strong>. Create a CSV file (free) or a PDF report <a class="tag" href="../plus/" title="Part of Nexdose Plus">Plus</a> that shows each peptide's current dose and schedule. If you turn on notes and symptoms in Settings, they're included too. Share it with your provider or save it to Files.</p>

<h2 id="sync">Sync and lock</h2>
<ul>
<li><strong>iCloud sync:</strong> if you're signed in to iCloud with iCloud turned on for Nexdose, your data syncs through your own private iCloud account.</li>
<li><strong>Face ID lock:</strong> lock Nexdose with Face ID or your passcode in Settings.</li>
<li><strong>Background:</strong> pick a color, make your own, or use one of your photos.</li>
</ul>

<h2 id="plus">Plus features <a class="tag" href="../plus/" title="Part of Nexdose Plus">Plus</a></h2>
<p>These come with <a href="../plus/">Nexdose Plus</a>. <a href="../plus/">See what&rsquo;s included and how to get it</a>.</p>
<h3>Auto dose-up (titration)</h3>
<p>Plan your dose increases once, for example a few weeks at each step, and Nexdose moves you up to the next dose on schedule. A preview chart shows the whole plan, and quick <strong>+</strong> and <strong>&minus;</strong> buttons adjust each step.</p>
<h3>Supply tracking</h3>
<p>Enter what's in each pen or vial, and Nexdose counts down as you log. Supply cards show what's left with a progress bar. Click pens with 60 or 80 clicks are supported, with optional priming counted in. Reorder and new pen or vial reminders show up on your calendar.</p>
<h3>Levels</h3>
<p>A half-life graph shows your estimated levels between shots, and an example graph shows how it works before you start. It is an estimate for your own reference, not medical advice.</p>
<h3>Cycles</h3>
<p>Set on and off cycles, such as days on and days off or weeks on and weeks off, once, and Nexdose follows them.</p>

<p class="note">Still stuck? Visit <a href="../support/">Support</a> or email <a href="mailto:contact@nexdose.app">contact@nexdose.app</a>.</p>
</div></section>
'''
write("how-to/", render("how-to/", "How to Use Nexdose: Setup, Logging, Schedules and More",
 "Step-by-step guides for Nexdose: add a shot, set a weekly GLP-1 schedule, log from widgets, Watch or Siri, rotate sites, export reports, and use Plus features.", body))
