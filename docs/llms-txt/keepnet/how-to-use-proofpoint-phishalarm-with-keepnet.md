# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/how-to-use-proofpoint-phishalarm-with-keepnet.md

# How to Use Proofpoint PhishAlarm with Keepnet

A short, customer-facing guide that explains why you should connect Proofpoint’s PhishAlarm to Keepnet, the benefits you’ll get, and clear step-by-step setup instructions so simulated phishing reports land in Keepnet automatically.

## Why connect Proofpoint PhishAlarm to Keepnet?

Connecting Proofpoint’s PhishAlarm button to Keepnet gives you a single, accurate place to track all reported emails, including simulated phishing, so you can measure human risk, run campaigns, and take automated remediation actions.

Key benefits:

* **Accurate campaign measurement** — Simulated phishing reports show up in your Keepnet phishing campaign stats (reporters, reporter rate, phishing dwell time).
* **Cleaner metrics (no noise)** — Keepnet’s Incident Responder and reporting pipeline distinguishes real threats from simulation telemetry and bots, so your human risk scores are reliable.
* **Faster remediation** — When an email (real or simulated) is reported, Keepnet can trigger automated scanning, inbox sweep/removal, and incident workflows.
* **Better behaviour insights** — Reports feed into human risk scoring, leaderboards, repeat-offender lists and targeted learning paths.
* **Single-pane visibility** — All reported emails (simulated + real) are visible alongside campaign context, so security and HR can make data-driven decisions.

## High-level flow

1. Employee clicks Proofpoint PhishAlarm to report an email.
2. Proofpoint forwards that reported email to your unique Keepnet inbound address (in <companyID@reporttokeepnet.com> format).
3. Keepnet ingests the report, links it to the correct phishing campaign (if it was part of a simulation), and updates Human Risk Score, campaign metrics, and dashboards.
4. (Optional) Keepnet Incident Responder runs automated analysis and remediation.

## What you need

* Proofpoint PhishAlarm is enabled for users in your org.
* Your unique Keepnet inbound address (format): **<yourCompanyID@reporttokeepnet.com>** — **use the exact domain address.**
  * To get your **Keepnet inbound address**, please log in to the **Keepnet platform** and go to **Phishing Reporter > Settings > Other Settings** to find your unique CompanyID.
* Admin access in Proofpoint (or someone who can add/modify the PhishAlarm forwarding address).

## Step-by-step setup in Proofpoint

These are concise, generic steps — your Proofpoint UI layout/version may look a little different. If you need screenshots, we can add them.

1. Login to **Proofpoint Admin Console**.
2. **Open the PhishAlarm** or **Report Button configuration** (often under End User Tools / PhishAlarm settings).
3. **Configure the forward / destination address** for reported items:
   1. Set the report/forward recipient to your Keepnet inbound address: <yourCompanyID@reporttokeepnet.com>
   2. If Proofpoint requires a display name, use something simple like: Keepnet Report Ingest
4. **Save and deploy** the configuration so it applies to your user groups.
5. **Test the flow** (see next section).

{% hint style="warning" %}
If Proofpoint allows per-group settings, apply the forwarding to the groups you’re piloting first (e.g., 50–200 users) before rolling out org-wide.
{% endhint %}

## Testing & verification (quick test)

1. From an internal test account, send a simulated phishing email to a test user (or use an existing Keepnet simulation).
2. Ask the test user to click the Proofpoint **PhishAlarm** button on that email.
3. In Keepnet: go to **Phishing Campaigns → \[Your Campaign] → Reported** (or **Inbox > Reported Emails** depending on your UI).
4. You should see the reported item appear within 1–2 minutes, with fields such as: Reporter, Report Time, Subject, Original Sender, Attachment indicator, and Campaign tag (if it was part of a simulation).

**Example of how a reported simulated phishing email will display in Keepnet**

(Your Keepnet UI may look different — this is a representative example.)

<table><thead><tr><th width="227.546875">Field</th><th>Example</th></tr></thead><tbody><tr><td>Reporter</td><td>jane.doe@yourcompany.com</td></tr><tr><td>Report Time</td><td>2025-10-27 09:12:03 (Europe/London)</td></tr><tr><td>Subject</td><td>Urgent: Password Expiry Notice</td></tr><tr><td>Original Sender</td><td>payroll@fakesender.com</td></tr><tr><td>Campaign</td><td>Q4 Security Awareness — Payroll Phish</td></tr><tr><td>Report Type</td><td>Simulated (auto-linked to campaign)</td></tr><tr><td>Action Taken</td><td>Scanned by Incident Responder; quarantined in 12 inboxes</td></tr><tr><td>Human Risk Impact</td><td>+0.6 on Reporter Score (improved)</td></tr></tbody></table>

## What Keepnet will do after receiving a report

* **Auto-link** the report to the phishing campaign (if the message ID or campaign headers match).
* **Update human risk & campaign** **metrics** (reporter rates, dwell time, repeat offenders).
* **Run Incident Responder** integrations (sandbox analysis, sandbox verdicts, remove/quarantine) if configured.
* **Present the report** in dashboards, leaderboards, and executive reports.

## Common troubleshooting

* Reports not showing in Keepnet
  * Check the forwarding address in Proofpoint — ensure it’s exactly <yourCompanyID@reporttokeepnet.com> with no typos.
  * Confirm Proofpoint logs show successful delivery to that address.
  * In Keepnet, check ingestion logs for the inbound address (or ask Keepnet Support to check ingestion queue).
* Reports arrive but not linked to campaign
  * Ensure simulations include the campaign headers or Message-ID mapping that Keepnet uses to auto-link. If not, Keepnet can link by subject + timestamp but header linkage is more reliable.
* Delayed reports
  * Check email routing / proofpoint processing delays and Keepnet ingestion queue. Network retries could cause short delays.
* Duplicate reports
  * If multiple report buttons or auto-forward rules exist, deduplication settings in Keepnet can be enabled — ask your Keepnet admin.<br>

## FAQs

### Q: Can I use one inbound address for multiple companies?

A: No — use the exact Keepnet address assigned to your company (the companyID is unique). This ensures reports are routed to the correct tenant in Keepnet.

### Q: Will Keepnet distinguish simulated vs real phishing?

A: Yes — Keepnet links reported items to campaigns and flags simulation reports. Analysis and remediation policies can be different for simulations vs confirmed threats.

### Q: How quickly will reports update my human risk score?

A: Reports typically update dashboards and scores within minutes after ingestion and analysis.

## Next steps & support

* Provide the Keepnet inbound address to your Proofpoint admin and apply the forwarding rule.
* Run a small pilot (50–200 users) and verify reports appear in Keepnet and link to campaigns.
* If you want, Keepnet can validate header mapping so simulated campaign emails are always auto-linked.
* For help troubleshooting Proofpoint or Keepnet ingestion logs, contact: **<support@keepnetlabs.com>** or your Keepnet Customer Success Manager.
