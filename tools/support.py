from page import render, write
faq = [
("Reminders aren't showing up.","Check that \"Remind me at each dose time\" is turned on in the peptide's schedule. Then check iPhone Settings &gt; Notifications &gt; Nexdose and make sure notifications are allowed. Focus modes can also hide them."),
("My data isn't syncing between devices.","Sync uses your own private iCloud account. Make sure you're signed in to the same Apple Account on each device and that iCloud is turned on for Nexdose in iPhone Settings &gt; your name &gt; iCloud. We can't see or restore your iCloud data."),
("How do I delete my data?","Delete shots or peptides inside the app. Deleting the app removes the data stored on your device. To also remove iCloud copies, go to iPhone Settings &gt; your name &gt; iCloud &gt; Manage Account Storage &gt; Nexdose, then delete the data."),
("Is Nexdose free?","Yes. The core app is free, with no ads and no account. <a href=\"../plus/\">Nexdose Plus</a> is an optional one-time $14.99 purchase, shared through Family Sharing."),
("I installed version 1.0. Do I have to pay for Plus?","No. If you first installed version 1.0, Plus is yours free."),
("Which devices does Nexdose work on?","iPhone with iOS 18 or later. The Apple Watch app needs watchOS 11 or later."),
("Is the calculator medical advice?","No. The calculators only do arithmetic. Always confirm any dose or reconstitution with your healthcare provider."),
("Does Nexdose collect my data?","No. There's no account, no ads and no analytics. Your data stays on your iPhone and, if you choose, your own iCloud. See the <a href=\"../privacy-policy/\">Privacy Policy</a>."),
]
items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
body = f'''
<section><div class="wrap prose">
<h1>Nexdose Support</h1>
<p>Need help or want to share an idea? Email <a href="mailto:contact@nexdose.app"><strong>contact@nexdose.app</strong></a> and we'll reply as soon as we can. Including your iPhone model and iOS version helps.</p>
<p>Looking for how to do something, like setting a schedule or logging from your watch? See the <a href="../how-to/">How-to guide</a>.</p>
<h2>Troubleshooting and common questions</h2>
{items}
<h2>Medical disclaimer</h2>
<p>Nexdose is a personal tracking tool. It does not diagnose, treat or give medical or dosing advice, and it is not a substitute for a healthcare professional. Always consult your provider about your treatment.</p>
</div></section>
'''
write("support/", render("support/", "Nexdose Support and FAQ",
 "Get help with Nexdose: reminders, iCloud sync, deleting your data, Plus and device requirements. Contact contact@nexdose.app.", body))

privacy = '''
<section><div class="wrap prose">
<h1>Nexdose Privacy Policy</h1>
<p>Effective date: October 20, 2026</p>
<p>Nexdose ("the app") is developed by Russell Gordon in St. George, Utah. This policy explains what happens to your information when you use Nexdose.</p>
<h2>The short version</h2>
<p>We do not collect your data. Nexdose has no accounts, no ads, no analytics, no third-party tracking, and no servers of ours that receive your information.</p>
<h2>Information you enter</h2>
<p>You may enter peptide names, doses, injection sites, dates and times, schedules, notes, and optionally body weight and a goal weight. This information is stored on your device so the app can work. We do not receive it, and we cannot see it.</p>
<h2>iCloud sync (optional)</h2>
<p>If you are signed in to iCloud and iCloud is enabled for Nexdose, your app data is stored in your own private iCloud account using Apple's CloudKit so it can sync between your devices. This data is protected by your Apple ID and is handled under Apple's terms and privacy policy. It is not accessible to us. You can turn this off in iPhone Settings and remove the data from iCloud storage at any time.</p>
<h2>Apple Health (optional)</h2>
<p>If you choose to import weight from Apple Health, Nexdose asks for permission to read your weight data. You choose what to allow in iPhone Settings &gt; Health &gt; Data Access &amp; Devices &gt; Nexdose, and you can turn it off at any time. Nexdose reads this data only to show it in the app, and only when you ask it to import. Nexdose does not write any data to Apple Health. We never receive your Apple Health data, and it is never used for advertising or marketing, shared with third parties, or sold.</p>
<h2>Notifications</h2>
<p>If you turn on reminders, Nexdose schedules local notifications on your device. These are created and delivered by your iPhone. No notification data is sent to us.</p>
<h2>Exports and sharing</h2>
<p>When you export a PDF or CSV, the file is created on your device. It goes only where you choose to send it, such as Mail, Messages or Files. We do not receive exports.</p>
<h2>Feedback</h2>
<p>If you choose to email us from within the app or at contact@nexdose.app, we receive only what you write and the email address you send from. We use it only to reply to you.</p>
<h2>Information we do not collect</h2>
<p>We do not collect your name, email address (unless you write to us), location, contacts, device identifiers, advertising identifiers, usage analytics or crash data. We do not sell or share personal information, and we do not track you across other apps or websites.</p>
<h2>Health information</h2>
<p>Nexdose lets you record personal health-related entries such as doses and weight. This information stays on your device (and your private iCloud if enabled). It is not shared with us or anyone else. Nexdose does not provide medical advice.</p>
<h2>Data retention and deletion</h2>
<p>Your data remains on your device until you delete it. You can delete shots and peptides in the app, or delete the app to remove local data. To remove iCloud copies, go to iPhone Settings &gt; your name &gt; iCloud &gt; Manage Account Storage &gt; Nexdose.</p>
<h2>This website</h2>
<p>The Nexdose website (nexdose.app) uses Cloudflare Web Analytics to count visits in aggregate, such as page views and which pages are popular. It uses no cookies, does not identify you, and does not track you across other websites. The Nexdose app itself has no analytics of any kind.</p>
<h2>Children</h2>
<p>Nexdose is intended for adults and is not directed to children under 13. We do not knowingly collect information from children.</p>
<h2>Changes to this policy</h2>
<p>If this policy changes, we will update the effective date above. Material changes will be reflected in the app's next update.</p>
<h2>Contact</h2>
<p>Questions about privacy? Email <a href="mailto:contact@nexdose.app"><strong>contact@nexdose.app</strong></a>.</p>
</div></section>
'''
write("privacy-policy/", render("privacy-policy/", "Nexdose Privacy Policy",
 "Nexdose collects no data: no accounts, ads, analytics or tracking. Your entries stay on your device and, optionally, your private iCloud.", privacy))
