# Source: https://documentation.onesignal.com/docs/en/email-deliverability.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email deliverability

> Improve inbox placement by managing sender reputation, reducing bounces and spam complaints, and following email hygiene best practices.

Email deliverability is the ability of your messages to reach recipients' inboxes — instead of being blocked, sent to spam, or lost in transit. Deliverability depends on your sender reputation, email content, domain alignment, and recipient engagement. Internet service providers (ISPs) and mailbox providers (Gmail, Outlook, etc.) assess every incoming email to filter out unwanted or harmful messages.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/7fnleyW4ud8?si=-A96_-nwO5XuW1Eh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

***

## Reputation

Your **email sending reputation** — assigned by inbox providers — is a key driver of deliverability. It determines how much email providers accept from you, whether your messages get blocked, and where they land ([inbox, promotions, or spam](#inbox-placement)).

<Frame caption="Email Reputation Dashboard">
  <img src="https://mintcdn.com/onesignal/EkhxVhmyAbk73dJN/images/email/reputation-dashboard.png?fit=max&auto=format&n=EkhxVhmyAbk73dJN&q=85&s=0eef6a2e7ab5c096a14edd10bcc38777" alt="OneSignal Email Reputation dashboard showing bounce and spam complaint rates" width="2952" height="1692" data-path="images/email/reputation-dashboard.png" />
</Frame>

Your reputation functions like a credit score: it goes up or down based on the performance of your past emails.

### What helps reputation

* High engagement (e.g., [opens](#opened), [clicks](#clicked), replies)
* Clean, verified lists
* Consistent email sending patterns

### What hurts reputation

* High [spam complaint](#spam-complained) rates — see [Monitor spam reports](./email-reputation-best-practices#monitor-spam-reports-and-complaints)
* High [bounce](#bounced) rates — see [Avoid invalid emails](./email-reputation-best-practices#avoid-invalid-emails)
* Sending to [spam traps](#spam-traps) — see [Set up a clear opt-in process](./email-reputation-best-practices#set-up-a-clear-opt-in-process)

<Warning>
  A bounce rate over **5%** or a complaint rate over **0.08%** may result in mail blocking by providers and violates the [Acceptable Use Policy & Code of Conduct](https://onesignal.com/aup). See [Google's Sender Guidelines](https://support.google.com/a/answer/14229414?hl=en) for more details.
</Warning>

If you're using OneSignal Email, view your stats at **Settings > Email > Reputation**. For third-party services (e.g., SendGrid, Mailchimp, Mailgun), use their dashboards to monitor complaints and bounces.

### How reputation metrics are calculated

* **Bounce Rate** = Permanent bounces ÷ total sent
* **Reported Spam Rate (feedback loop providers only)** = Spam complaints received via feedback loop ÷ total sent
* Complaint data depends on provider feedback availability.

<Warning>
  The "Reported Spam Rate (feedback loop providers only)" does not account for complaints from Gmail recipients due to Gmail restrictions. To monitor Gmail-specific spam rates, connect [Google Postmaster Tools](./google-postmaster-tools).
</Warning>

<Card title="Email reputation best practices" icon="shield-check" href="./email-reputation-best-practices">
  Actionable steps to build and maintain a healthy sending reputation — opt-in, monitoring, frequency, warm-up, and list hygiene.
</Card>

***

## Key deliverability concepts

These terms appear in your email reports and reputation dashboard. Understanding them helps you diagnose and fix deliverability issues.

### Unsubscribed

Recipients who opt out via the unsubscribe link in your emails. These recipients are suppressed automatically to ensure compliance and protect your reputation.

Honor unsubscribe requests promptly — it's required by regulations like CAN-SPAM and protects your sender reputation.

<Info>
  See [Unsubscribe Links & Email Subscriptions](./unsubscribe-links-email-subscriptions) and how to [Create a custom unsubscribe page](./create-custom-unsubscribe-page).
</Info>

### Bounced

Emails that fail to deliver due to invalid addresses (usually they do not exist or are spelled incorrectly). Bounce data is stored in your [Suppression List](#suppression-list) and also visible in [Event Streams](./event-streams).

### Failed

Emails that are temporarily undeliverable due to:

* Misconfigured domain (e.g., DMARC/DKIM issues) — see [Email DNS configuration](./email-dns-configuration)
* Full inbox
* Low reputation or blocklisting

<Frame caption="&#x22;Too Old&#x22; deferral messages from Gmail for poor reputation">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/97e71b2-Failure_Message.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=e4c3b7550b0cd7a01d31a358022c4d3d" alt="Gmail deferral message showing 'Too Old' error due to poor sender reputation" width="1484" height="621" data-path="images/docs/97e71b2-Failure_Message.png" />
</Frame>

Failures appear in [Email Message Reports > Audience Activity](./email-message-reports#audience-activity) and [Event Streams](./event-streams).

Failures are not added to suppression lists.

### Spam complained

When recipients mark your email as spam, it triggers a spam complaint, also known as a "Spam Report."

<Frame caption="Yahoo Report Spam Button">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/cb9ef9f-Yahoo_Report_Spam_1.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=dacee976dec2ec56f7369125215098e7" alt="Yahoo mail interface showing the Report Spam button" width="486" height="245" data-path="images/docs/cb9ef9f-Yahoo_Report_Spam_1.png" />
</Frame>

Common reasons for complaints include:

* Irrelevant content
* Excessive frequency
* Recipients who did not opt in

<Note>
  Minimize complaint rates by analyzing feedback, adjusting content, and providing easy opt-out options. Follow the [email reputation best practices](./email-reputation-best-practices) to keep complaints low.
</Note>

These events are available in [Event Streams](./event-streams).

#### How spam rate is calculated

A feedback loop is a reporting system where inbox providers notify senders when a recipient marks their email as spam. Not all providers offer this — Yahoo and Outlook do; Gmail does not.

The “Reported Spam Rate (feedback loop providers only)” reflects spam complaints received from mailbox providers that share per-recipient feedback loop data (such as Yahoo and Outlook).

<Warning>
  Gmail does not provide per-recipient spam complaint feedback to senders — this is an industry-wide limitation. Spam complaints are only reported by providers that share feedback loop data. To monitor Gmail-specific spam rates, connect [Google Postmaster Tools](./google-postmaster-tools).
</Warning>

### Suppression list

A blocklist within your OneSignal app that prevents sending to emails that have bounced or been marked as spam. Manage it via the [Suppressions Guide](./suppressions).

### Blocklists

External or ISP-managed lists of spammy or harmful IPs/domains. Being listed will cause deliverability problems. Use tools like [Spamhaus](https://www.spamhaus.org/) to check your domain/IP status.

### Spam traps

Spam traps are email addresses not used by real individuals, set up by ISPs or anti-spam organizations to identify spammers. Sending emails to spam traps indicates poor list hygiene or acquisition practices and can severely damage your sending reputation.

<Accordion title="Learn more about spam traps">
  <Frame>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/r76EvxIUeRc?si=Lob4AV1_bLBg99SS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
  </Frame>

  Spam traps are email addresses not owned or operated by actual recipients. They are operated by inbox providers and third-party operators that report to, or are referenced by, inbox providers.

  Sending to spam traps can land your domain or IPs on a blocklist. Being on a blocklist means that some inboxes will reject your emails.

  Some common spam trap networks are [SpamHaus](https://www.spamhaus.org/), [Abusix](https://abusix.com/), and Microsoft's [SNDS](https://sendersupport.olc.protection.outlook.com/snds/).

  There are multiple types of spam traps that can be prevented by following email best practices.

  **Pristine**

  Email addresses set up for the sole purpose of being monitored as spam traps. Found on public websites and purchased lists.

  **Recycled**

  Email addresses that used to belong to an actual recipient but have been repurposed as spam traps. Often abandoned inboxes or domains.

  **Typo**

  Email addresses set up with common typos, such as "gnail.com", "tahoo.com", "gmail.con", "outlooj.com", etc.

  **How to avoid spam traps**

  List cleaning tools will not remove spam traps. Instead, focus on prevention and removal.

  **Prevent spam traps:** Implement a confirmed (double) opt-in process. When a new contact provides their email address, send an immediate confirmation email that verifies (a) the address is valid and (b) the address is actually operated by the recipient. Learn how to implement a double opt-in using OneSignal's [Magic Link](./example-verification-magic-link-otp#setting-up-double-opt-in-with-onesignal).

  **Remove spam traps:** Remove unengaged email addresses. Spam traps don't bounce as invalid but don't engage with your emails either. If a recipient has received multiple emails without opening or clicking, remove them from your list. Use [Journeys](./journeys-overview) with [Wait Until branches](./journeys-actions#wait-until) to tag unengaged recipients, then exclude them from further sends.
</Accordion>

***

## Email address validation

Email address validation detects common problems in email addresses before they reach your audience. It flags typos, invalid domains, role-based addresses, and disposable email services that could increase your bounce rate or hurt your sender reputation.

<Card title="Email address validation" icon="circle-check" href="./email-address-validation">
  Validate email addresses during CSV import and in bulk to reduce bounces and protect your sender reputation.
</Card>

***

## Engagement metrics

### Opened

The number of times recipients open your email messages. Open rates indicate the effectiveness of your subject lines, targeting, and sender identity. High open rates suggest good inbox placement and engagement. View open rates in [Email Message Reports](./email-message-reports).

### Clicked

The number of times recipients click links within your email messages. Click-through rates measure the effectiveness of your email content and calls-to-action. Since recipients must open emails before clicking, clicks are a strong indicator of engagement. View click rates in [Email Message Reports](./email-message-reports).

***

## Inbox placement

Inbox placement refers to where your emails land within recipients' inboxes. Proper placement ensures your emails are seen in the right context and increases the likelihood of engagement.

<Frame caption="Gmail Inbox Tabs">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/871abe6-Gmail_Inbox_Tabs.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=af06c78164fb1655446c6201e3b482ea" alt="Gmail inbox showing Primary, Social, and Promotions tabs" width="1319" height="284" data-path="images/docs/871abe6-Gmail_Inbox_Tabs.png" />
</Frame>

### Primary

The Primary tab is typically where important and personal communications are received. Achieving primary inbox placement indicates good sender reputation and email relevance.

### Promotions

The Promotions tab is a separate section within recipients' inboxes designated for promotional or marketing emails. Inbox providers use algorithms to categorize emails as promotions based on sender reputation and email content.

<Accordion title="Emails landing in Promotions">
  Landing in the Promotions tab is not an indicator of bad reputation and is not necessarily a bad outcome for marketing emails. If an email is inherently promotional, it may perform better in the context of the Promotions tab. Providers like Gmail actively draw recipient attention to their Promotions tab.

  The Promotions tab has been found to reduce spam complaints and increase engagement, as it helps emails meet recipient expectations. When a recipient visits their Promotions tab, they are more receptive to deals and shopping.

  To land more often in the Primary tab, avoid excessive promotional language, personalize content, and encourage recipients to move your emails to their Primary tab.
</Accordion>

### Spam

Emails filtered by inbox providers into recipients' spam or junk folders. Emails land in spam due to suspicious content, triggered spam filters, or low sender reputation.

<Accordion title="Emails landing in Spam">
  Landing in the spam folder usually indicates poor reputation. Check whether your complaint or bounce rate has been higher than acceptable. According to Google, senders should keep their spam rate below 0.1%.

  Follow the [email reputation best practices](./email-reputation-best-practices) to lower bounce and complaint rates. If spam placement does not seem reputation-related, verify that your DMARC is properly aligned. [About My Email](https://aboutmy.email/) is a great testing tool to check for alignment.

  See why [DMARC is required by Google and Yahoo](./new-google-and-yahoo-email-updates).
</Accordion>

***

## FAQ

### What is the difference between reputation and deliverability?

Reputation is the score inbox providers assign to your sending domain based on past email performance. Deliverability is the outcome — whether your emails reach the inbox, land in spam, or get blocked. A good reputation is the primary driver of good deliverability.

### What's the difference between a bounce and a failure?

A [bounce](#bounced) means the email address is permanently invalid (e.g., it doesn't exist). Bounced addresses are added to your [Suppression List](./suppressions). A [failure](#failed) is a temporary delivery issue (e.g., full inbox, DKIM misconfiguration) — failures are not suppressed and the email may be retried.

### Why are my emails landing in Promotions instead of Primary?

Landing in [Promotions](#promotions) is not a sign of bad reputation. Gmail and other providers categorize emails based on content and past recipient behavior. To reach the Primary tab, reduce promotional language, personalize content, and encourage recipients to move your emails to Primary.

### What are spam traps and how do they affect me?

[Spam traps](#spam-traps) are email addresses set up by ISPs to catch senders with poor list hygiene. Sending to spam traps can land your domain on a [blocklist](#blocklists), causing inbox providers to reject your emails. Implement confirmed opt-in and remove unengaged recipients to avoid them. See [Set up a clear opt-in process](./email-reputation-best-practices#set-up-a-clear-opt-in-process).

### How do I improve my deliverability?

Follow the [email reputation best practices](./email-reputation-best-practices) — it covers opt-in processes, monitoring spam reports, targeting engaged recipients, controlling send frequency, warming up your domain, and maintaining list hygiene.

***

## Related pages

<Columns cols={2}>
  <Card title="Email reputation best practices" icon="shield-check" href="./email-reputation-best-practices">
    Actionable steps to build and maintain a healthy sending reputation.
  </Card>

  <Card title="Email DNS configuration" icon="globe" href="./email-dns-configuration">
    Set up SPF, DKIM, and DMARC records for your sending domain.
  </Card>

  <Card title="Google Postmaster Tools" icon="chart-line" href="./google-postmaster-tools">
    Monitor Gmail-specific spam rates and domain reputation.
  </Card>

  <Card title="Suppressions" icon="ban" href="./suppressions">
    Manage your suppression list to prevent sending to invalid or unengaged addresses.
  </Card>
</Columns>

Built with [Mintlify](https://mintlify.com).
