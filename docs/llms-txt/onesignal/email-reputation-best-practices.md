# Source: https://documentation.onesignal.com/docs/en/email-reputation-best-practices.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email reputation best practices

> Build and maintain a healthy email sending reputation to improve deliverability and avoid spam complaints.

<Note>
  New to email deliverability? Read the [Email deliverability overview](./email-deliverability) first to understand key concepts like reputation, bounces, spam traps, and inbox placement.
</Note>

## Protect your reputation

### Monitor spam reports and complaints

A high volume of [spam reports](./email-deliverability#spam-complained) will quickly destroy your sending reputation. Monitor them closely — more often than open or click rates.

Most inbox providers (like Outlook, Hotmail, and Yahoo) report spam complaints and bounces back to OneSignal. Unfortunately Gmail does not. Gmail only surfaces this data through Google Postmaster Tools, which you must set up separately.

Currently, the OneSignal dashboard includes Gmail send volume when calculating [reputation rates](./email-deliverability#reputation) but because Google does not provide the complaint and bounced data for Gmail, the reported rates can appear lower than reality.

<Warning>
  Your dashboard spam rate may be underreported because Gmail complaints are not included. For example, 10 spam complaints across 1000 emails shows as a 1% spam rate if those complaints come from Outlook or Yahoo — but 0% if they come from Gmail.
</Warning>

To monitor Gmail-specific spam rates and domain reputation — especially since Gmail is the largest mailbox provider — set up [Google Postmaster Tools](./google-postmaster-tools).

<Columns cols={2}>
  <Card title="Google Postmaster Tools" icon="envelope-circle-check" href="./google-postmaster-tools">
    Track aggregate spam rates and domain reputation for Gmail recipients.
  </Card>

  <Card title="Reputation dashboard" icon="shield-check" href="./email-deliverability#reputation">
    Monitor spam and bounce rates for all providers except Gmail in your OneSignal dashboard.
  </Card>
</Columns>

<Frame caption="Google Postmaster Tools">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/email/postmastertools.gif?s=78fcd5c308208638d7e32428f599cea3" alt="Google Postmaster Tools dashboard showing domain reputation and spam rate" width="800" height="612" data-path="images/email/postmastertools.gif" />
</Frame>

<Note>
  Consider why recipients might report your emails as spam:

* Did they disengage over time?
* Did they knowingly opt in?
* Were they sent too many emails?
* Was the content aligned with their expectations?
</Note>

#### What to monitor regularly

To maintain a healthy sending reputation, regularly review:

* **Reported Spam Rate** — [Reputation dashboard](./email-deliverability#reputation)
* **Gmail spam rate** — [Google Postmaster Tools](./google-postmaster-tools)
* **Bounce rate** — [Reputation dashboard](./email-deliverability#reputation)
* **Unsubscribe rate** — [Email Message Reports](./email-message-reports)
* **Open and click engagement trends** — [Email Message Reports](./email-message-reports)

### Set up a clear opt-in process

Sending emails to people who have not given clear permission often leads to spam reports. This negatively impacts your sending reputation and may result in all your emails going directly to spam.

At minimum, when collecting emails, include a checkbox asking for permission to send marketing emails. If the checkbox is unchecked when the form is submitted, do not add that address to your marketing list. You can either not send the email address to OneSignal or use a [Tag](./add-user-data-tags) like `opt_in_consent: false` to track opt-in status and exclude those recipients from campaigns.

<Warning>
  Collecting the email as part of your sign-up process or account creation is not enough. Consent needs to be explicitly given.
</Warning>

<Frame caption="Opt-in checkbox example">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/email/email-opt-in-click.gif?s=00a66e284056451d12f1b500f23cc0a6" alt="Animated example of an opt-in checkbox on a sign-up form" width="1039" height="1079" data-path="images/email/email-opt-in-click.gif" />
</Frame>

#### Implement confirmed opt-in (double opt-in)

A confirmed opt-in process requires the recipient to verify their interest by clicking a link in a confirmation email. This method:

* Increases engagement
* Verifies compliance (e.g., GDPR, CAN-SPAM)
* Filters out fake or mistyped addresses
* Reduces complaint and bounce rates
* Prevents abuse and list bombing

<Columns cols={2}>
  <Card title="Create a confirmed opt-in journey" icon="envelope-open" href="./double-opt-in-email">
    Use Tags, Segments, and Journeys to create a confirmed opt-in journey.
  </Card>

  <Card title="Add your own verification links" icon="link" href="./example-verification-magic-link-otp">
    Learn how to add your own verification links to your emails.
  </Card>
</Columns>

#### Offer email preferences

Give recipients the option to choose what types of emails they receive — newsletters, rewards, deals, product updates, etc. Make it easy to adjust these preferences anytime via an email preference center.

<Frame caption="Email preference center example">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/email/email-preferences-example.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=10f08eb6033c304fbd7570a87b6c6ef1" alt="Example email preference center with category toggles" width="564" height="361" data-path="images/email/email-preferences-example.png" />
</Frame>

<Columns cols={2}>
  <Card title="Create a preference center" icon="sliders" href="./preference-center">
    Build a preference center so recipients can manage their email preferences.
  </Card>

  <Card title="Use Tags to manage email preferences" icon="tag" href="./add-user-data-tags">
    Use Tags to manage recipient preferences.
  </Card>
</Columns>

### Exclude or sunset unengaged recipients

Low open rates indicate poor engagement and hurt your reputation.

Implement a sunset policy to remove recipients who haven't opened or clicked emails in 2–3 months (depending on your send frequency). If you're using omni-channel messaging, you can also use last session date to identify inactive recipients across all channels.

<Card title="Message Event Filter Segments" icon="filter" href="./segmentation#message-event-filters">
  Track recipients who have not opened or clicked emails in more than 3 months — or filter by last session date for omni-channel inactivity — and exclude or delete them from further sends using Message Event Filters or Last Session Date.
</Card>

***

## Set up for success

### Authenticate your sending domain

Inbox providers check that your emails are authenticated before accepting them. Without proper DNS records (SPF, DKIM, DMARC), your emails may be rejected or sent to spam regardless of your content or engagement.

<Card title="Email DNS configuration" icon="globe" href="./email-dns-configuration">
  Set up SPF, DKIM, and DMARC records for your sending domain.
</Card>

### Warm up your sending domain

Inbox providers may block high-volume sends from domains with no sending history. A new domain starts with no [reputation](./email-deliverability#reputation), so you need to build trust gradually.

If you're sending large volumes — especially from a new domain or provider — gradually increase volume to build trust.

<Card title="Warm Up" icon="sun" href="./email-warm-up">
  Use OneSignal's Auto Warm Up feature to automate the ramp-up process.
</Card>

### Avoid invalid emails

High [bounce](./email-deliverability#bounced) rates hurt your reputation. Validate your list before importing and use confirmed opt-in to prevent bad addresses from entering.

<Card title="Email address validation" icon="circle-check" href="./email-address-validation">
  Validate email addresses during CSV import and in bulk to reduce bounces and protect your sender reputation.
</Card>

***

## Improve deliverability

### Control send frequency

Sending too many emails increases the risk of unsubscribes and spam complaints. Evaluate frequency from the recipient's perspective. Daily emails may be too much for most audiences.

<Columns cols={2}>
  <Card title="Wait steps" icon="clock" href="./journeys-actions#wait">
    Add delays between Journey messages to control send frequency.
  </Card>

  <Card title="Wait Until branches" icon="code-branch" href="./journeys-actions#wait-until">
    Send Journey follow-ups based on open/click behavior.
  </Card>
</Columns>

<Frame caption="Example of what NOT to do in a Journey. Wait steps need more spacing and emails should be sent strategically with Wait Until branches.">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/email/email-excessive-journey.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=8d85f9c8f14655c47f667b3bcb09cf26" alt="Journey example showing excessive email sends without wait nodes" width="770" height="526" data-path="images/email/email-excessive-journey.png" />
</Frame>

### Target engaged recipients

Inbox providers reward high engagement. Recipients who open and click are more likely to receive future emails in their inbox.

<Columns cols={2}>
  <Card title="Wait Until branches" icon="code-branch" href="./journeys-actions#wait-until">
    Send Journey follow-ups based on open/click behavior.
  </Card>

  <Card title="Message Event Filter Segments" icon="filter" href="./segmentation#message-event-filters">
    When sending less-urgent emails, target more engaged recipients.
  </Card>
</Columns>

<Frame caption="Journey with a Wait Until branch based on email open behavior">
  <img src="https://mintcdn.com/onesignal/EkhxVhmyAbk73dJN/images/email/wait-until-journey-email-open.png?fit=max&auto=format&n=EkhxVhmyAbk73dJN&q=85&s=39f53824a9e01ef260913cb751884742" alt="Journey with a Wait Until branch based on whether the email was opened" width="2960" height="2024" data-path="images/email/wait-until-journey-email-open.png" />
</Frame>

### Deliver value, not just promotions

Every email should provide real value — insights, tips, solutions, or relevant updates. A discount code alone does not equal value.

**Evaluate content performance**

Your audience expects specific content types. Make sure you're meeting those expectations.

<Columns cols={2}>
  <Card title="Multi-link tracking" icon="link" href="./email-messaging#track-link-clicks">
    Identify which content and links recipients click most.
  </Card>

  <Card title="A/B testing" icon="flask" href="./ab-testing#email-a-b-testing">
    Test subject lines, content, and layouts to see what resonates.
  </Card>
</Columns>

**Use email to build relationships and get feedback**

Email is a conversation channel — not a billboard. Use it to build trust and invite responses — replies improve your sending reputation.

<Note>
  Use a valid reply-to address. Avoid "no-reply" emails.
</Note>

***

## FAQ

### Why are my emails going to spam?

The most common causes are:

* DNS records are not properly configured
* A poor sending reputation
* High spam complaint rates
* Sending to recipients who did not explicitly opt in

Review your [Email Setup](./email-setup) for DNS records configuration, [Google Postmaster Tools](./google-postmaster-tools) for spam rate data, ensure you have a clear [opt-in process](#set-up-a-clear-opt-in-process), and [Exclude or sunset unengaged recipients](#exclude-or-sunset-unengaged-recipients).

### What spam complaint rate is too high?

Google recommends staying below 0.10% and never exceeding 0.30%. Use [Google Postmaster Tools](./google-postmaster-tools) to monitor your spam rate.

OneSignal's [Acceptable Use Policy & Code of Conduct](https://onesignal.com/aup) recommends keeping bounce rates below 5% and spam complaint rates below 0.08%.

### How do I check my domain reputation?

For Gmail — the largest email provider — set up [Google Postmaster Tools](./google-postmaster-tools) to view your domain reputation.

For other providers, you can monitor bounce rates and spam reports in your OneSignal dashboard via:

* [Reputation dashboard](./email-deliverability#reputation)
* [Suppression List](./suppressions)
* [Email Message Reports](./email-message-reports)

### How long does warm-up take?

Warm-up timelines depend on your target volume and current reputation. Typically, plan for 2–4 weeks of gradually increasing volume. See the [Warm Up guide](./email-warm-up) for details on using OneSignal's Auto Warm Up feature.

### Should I remove unengaged recipients from my list?

Yes. Implement a sunset policy to stop sending to recipients who haven't opened or clicked emails in 2–3 months. Low engagement signals to inbox providers that your emails are unwanted, which hurts deliverability for all recipients. Use [Message Event Filter Segments](./segmentation#message-event-filters) to target recipients based on open/click behavior.

***

## Related pages

<Columns cols={2}>
  <Card title="Email deliverability" icon="inbox" href="./email-deliverability">
    Understand key concepts like reputation, bounces, spam traps, and inbox placement.
  </Card>

  <Card title="Email DNS configuration" icon="globe" href="./email-dns-configuration">
    Set up SPF, DKIM, and DMARC records for your sending domain.
  </Card>

  <Card title="Google Postmaster Tools" icon="chart-line" href="./google-postmaster-tools">
    Monitor Gmail-specific spam rates and domain reputation.
  </Card>

  <Card title="Email warm up" icon="sun" href="./email-warm-up">
    Gradually increase sending volume to build trust with inbox providers.
  </Card>
</Columns>

***

Built with [Mintlify](https://mintlify.com).
