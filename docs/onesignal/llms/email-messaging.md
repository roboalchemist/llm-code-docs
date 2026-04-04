# Source: https://documentation.onesignal.com/docs/en/email-messaging.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email overview

> Send marketing and transactional emails with OneSignal using the dashboard, Journeys, or the API — with built-in personalization, analytics, and deliverability tools.

OneSignal Email lets you send **marketing** and **transactional** emails from the dashboard, Journeys, or the API.

* **Send marketing campaigns and transactional messages** from the dashboard or API
* **Build automated email and multi-channel flows** with Journeys
* **Design emails** using drag-and-drop or HTML
* **Personalize content** with dynamic fields, conditional logic, and language variants
* **Track performance and A/B test** with detailed analytics
* **Segment your audience** for precise targeting
* **Integrate with CRMs and tools** like HubSpot, Mixpanel, Amplitude, Zapier, and [more](./integrations)

***

## Email setup

Before sending emails, follow these setup guides:

<Note>
  Authenticate your domain (SPF, DKIM, DMARC) and enable [Auto warm-up](./email-warm-up) before sending at scale to protect your sender reputation and inbox placement.
</Note>

<Columns cols={2}>
  <Card title="Email setup guide" icon="envelope" href="./email-setup">
    Verify your sending domain and enable email in OneSignal.
  </Card>

  <Card title="DNS configuration" icon="globe" href="./email-dns-configuration">
    Automatically configure DNS with one click or complete setup manually.
  </Card>

  <Card title="Senders" icon="at" href="./senders">
    Manage from names, from addresses, reply-to addresses, and multiple sending domains.
  </Card>

  <Card title="Email template forwarding" icon="forward" href="./email-template-forwarding">
    Import existing email templates by forwarding them directly to OneSignal.
  </Card>

  <Card title="Transactional email setup" icon="bolt" href="./setup-transactional-emails">
    Trigger emails based on user actions or custom events.
  </Card>

  <Card title="Custom unsubscribe pages" icon="link-slash" href="./create-custom-unsubscribe-page">
    Replace the default unsubscribe page using OneSignal APIs.
  </Card>
</Columns>

***

## Deliverability, reputation, and analytics

Deliverability determines whether your emails reach the inbox or land in spam. OneSignal provides tools and guidance to help you build and maintain a healthy sending reputation.

<Columns cols={3}>
  <Card title="Email deliverability" icon="inbox" href="./email-deliverability">
    Understand how inbox placement works and how OneSignal supports it.
  </Card>

  <Card title="Email reputation best practices" icon="shield" href="./email-reputation-best-practices">
    Warm domains, manage volume, and avoid spam filters.
  </Card>

  <Card title="Auto warm-up" icon="temperature-arrow-up" href="./email-warm-up">
    Automatically ramp sending volume for new domains.
  </Card>

  <Card title="Google Postmaster Tools" icon="google" href="./google-postmaster-tools">
    Monitor Gmail reputation and delivery signals.
  </Card>

  <Card title="Suppressions" icon="ban" href="./suppressions">
    Manage blocked and suppressed email addresses.
  </Card>

  <Card title="Email message reports" icon="chart-line" href="./email-message-reports">
    Track open, click, and conversion rates.
  </Card>

  <Card title="Email troubleshooting" icon="wrench" href="./email-troubleshooting">
    Diagnose and resolve common delivery issues.
  </Card>

  <Card title="Create a confirmed opt-in journey" icon="envelope-open" href="./double-opt-in-email">
    Use Tags, Segments, and Journeys to create a confirmed opt-in journey.
  </Card>

  <Card title="Add your own verification links" icon="link" href="./example-verification-magic-link-otp">
    Learn how to add your own verification links to your emails.
  </Card>
</Columns>

***

## Design your emails

OneSignal supports visual and code-based email creation. Use the drag-and-drop editor for quick campaigns or the HTML editor for full design control. You can also start from a template and customize from there.

<Columns cols={3}>
  <Card title="Drag-and-drop editor" icon="palette" href="./design-emails-with-drag-and-drop">
    Build emails visually without writing code.
  </Card>

  <Card title="HTML editor" icon="code" href="./design-emails-with-html">
    Design fully custom emails using HTML.
  </Card>

  <Card title="Templates" icon="copy" href="./templates">
    Start from pre-built templates or create and save your own layouts.
  </Card>

  <Card title="Unsubscribe links and headers" icon="link-slash" href="./unsubscribe-links-email-subscriptions">
    Control unsubscribe behavior, headers, and compliance settings.
  </Card>

  <Card title="Message personalization" icon="user-pen" href="./message-personalization">
    Personalize content using user data and conditional logic.
  </Card>

  <Card title="Multi-language messaging" icon="language" href="./multi-language-messaging">
    Send localized emails in multiple languages.
  </Card>

  <Card title="Email template forwarding" icon="forward" href="./email-template-forwarding">
    Import existing email templates by forwarding them directly to OneSignal.
  </Card>

  <Card title="Copy template to another app API" icon="clone" href="/reference/copy-template-to-another-app">
    Move templates between OneSignal apps.
  </Card>
</Columns>

***

## Send emails

Send messages from the dashboard, automate them with Journeys, or trigger them programmatically via the API.

<Columns cols={2}>
  <Card title="Dashboard" icon="window-maximize" href="#send-from-the-dashboard">
    Compose a message quickly within the dashboard.
  </Card>

  <Card title="Send via API" icon="code" href="/reference/create-message">
    Send messages programmatically using the REST API.
  </Card>

  <Card title="Journeys" icon="route" href="./journeys-overview">
    Build automated, multi-step, and multi-channel flows.
  </Card>

  <Card title="A/B testing" icon="flask" href="./ab-testing">
    Test up to 10 message variants to optimize performance.
  </Card>
</Columns>

### Send from the dashboard

<Steps>
  <Step title="Select the message channel" icon="window-maximize">
    Select **Create...** then choose your message channel. You can also navigate to **Messages** or **Templates** to view previous messages.

    <Frame caption="Create a new message in the OneSignal dashboard.">
      <img src="https://mintcdn.com/onesignal/UDk6E5NjA3sdGdRN/images/dashboard/create-message.png?fit=max&auto=format&n=UDk6E5NjA3sdGdRN&q=85&s=97504cf71555ac4aeb263a36ad2d28b3" alt="OneSignal dashboard showing create message options" width="2128" height="1374" data-path="images/dashboard/create-message.png" />
    </Frame>
  </Step>

  <Step title="Choose a composition method" icon="pencil">
    * Start from scratch with the [block editor](./design-emails-with-drag-and-drop) or [HTML editor](./design-emails-with-html)
    * Use a pre-built [template](./templates)
  </Step>

  <Step title="Set a name and label" icon="tag">
    Add internal metadata for tracking and reporting. API equivalent: `name`
  </Step>

  <Step title="Select your audience" icon="users">
    Choose which users receive the message. You can include and exclude [segments](./segmentation) to target specific groups. Defaults to all "Subscribed Users" if no segment is set.

    <Frame caption="Name, label, and audience segment selection in the dashboard.">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/message-name-label-audience.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=1f41b0e42d31211b1c1badf87ba84056" alt="Dashboard fields for message name, label, and audience segment selection" width="1650" height="518" data-path="images/dashboard/message-name-label-audience.png" />
    </Frame>

    | Targeting method                                    | Dashboard | API |
    | --------------------------------------------------- | :-------: | :-: |
    | [**Segments**](./segmentation)                      |    Yes    | Yes |
    | **Filters** ([API only](/reference/create-message)) |     No    | Yes |
    | **Aliases** ([API only](/reference/create-message)) |     No    | Yes |
  </Step>
</Steps>

#### Sender

Configure the sender details used for this email:

* From name
* From address
* Reply-to address
* Sending domain

<Note>
  Multi-domain sending is supported. See [Senders](./senders).
</Note>

API fields: `email_from_address`, `email_sender_domain`, `email_reply_to_address`

#### Subject and preheader

Set a required subject line and optional preheader text. Preheader display varies by inbox provider — not all inboxes show it.

* API fields: `email_subject` and `email_preheader`
* Supports [message personalization](./message-personalization) and [multi-language messaging](./multi-language-messaging)

#### Tracking and compliance

**Link tracking** — Enabled by default. Supports multi-link tracking. See [Links](./links#email) and [Deep linking](./deep-linking) for details.

* API field: `disable_email_click_tracking`

**Send to unsubscribed users** — Enable only for compliance or non-marketing messages.

* API field: `include_unsubscribed`

<Frame caption="Tracking and compliance options when composing an email.">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/Screenshot2025-06-09at4.15.02PM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=b4496406dae7c2a7a9dd07cf35cf1069" alt="Email composition panel showing link tracking and unsubscribe send options" width="1127" height="427" data-path="images/docs/Screenshot2025-06-09at4.15.02PM.png" />
</Frame>

#### Delivery schedule and optimization

Choose when the message should start sending.

| Option                              | Description                                        | API field    |
| ----------------------------------- | -------------------------------------------------- | ------------ |
| **Send immediately**                | Deliver to all recipients now.                     | —            |
| **Scheduled**                       | Send at a specific time, up to 30 days in advance. | `send_after` |
| **[Auto warm-up](./email-warm-up)** | Gradually ramp volume for new or cold domains.     | —            |

**Per-user optimization:**

Set when users should receive the message.

| Option                        | Description                                                                                             | API field                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Everyone at the same time** | All recipients receive the email at once. Best for urgent messages.                                     | —                                                  |
| **Intelligent Delivery**      | Sends at the optimal time for each user based on their open and click activity (excludes bot activity). | `delayed_option: last-active`                      |
| **Custom time per timezone**  | Sends at a set local time in each user's timezone.                                                      | `delayed_option: timezone`, `delivery_time_of_day` |

<Info>
  The "start sending" time determines the audience cutoff. OneSignal evaluates segment membership at that moment — anyone in the audience receives the message, regardless of per-user optimization settings.
</Info>

Click **Review and Send** to send immediately or on schedule, or **Save** as draft to edit later. Once sending begins, monitor performance under **Messages > Email** or in **Delivery > Sent Messages**. See [Email message reports](./email-message-reports) for details.

***

## Analytics

Track message performance and engagement.

<Columns cols={2}>
  <Card title="Email message reports" icon="chart-line" href="./email-message-reports">
    Message-level delivery, open rate, and click-through reporting.
  </Card>

  <Card title="Analytics overview" icon="chart-bar" href="./analytics-overview">
    All analytics options available in OneSignal.
  </Card>

  <Card title="Event Streams" icon="signal-stream" href="./event-streams">
    Stream push events to your data warehouse or BI tools in real time.
  </Card>

  <Card title="View messages API" icon="code" href="/reference/view-messages">
    Pull message analytics programmatically via the REST API.
  </Card>
</Columns>

***

## FAQ

### What's the difference between marketing and transactional emails?

Marketing emails are campaigns sent to a segment of users, such as promotions or newsletters. Transactional emails are triggered by a user action or event, such as a password reset or order confirmation. See [Transactional email setup](./setup-transactional-emails) for configuration details.

### Why are my emails going to spam?

Common causes include missing DNS authentication (SPF, DKIM, DMARC), sending to unengaged users, or ramping volume too quickly on a new domain. See [Email deliverability](./email-deliverability) and [Email reputation best practices](./email-reputation-best-practices) for guidance.

### Can I send emails to users who unsubscribed?

Only for compliance or non-marketing messages, such as legal notices. Enable the **Send to unsubscribed users** option when composing or set `include_unsubscribed` via the API. Using this for marketing emails violates anti-spam regulations.

### How do I test emails before sending to Users?

Set up [test Subscriptions](./find-set-test-subscriptions) to verify delivery, rendering, and deep links without affecting real Users. You can also send to a single-user segment for quick testing.

Built with [Mintlify](https://mintlify.com).
