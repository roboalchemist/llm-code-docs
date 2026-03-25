# Source: https://documentation.onesignal.com/docs/en/sms-messaging.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS overview

> Send SMS and MMS messages with OneSignal using the dashboard, Journeys, or the API — with segmentation, personalization, and delivery analytics.

OneSignal SMS lets you send **SMS** and **MMS** messages from the dashboard, Journeys, or the API. SMS is commonly used for time-sensitive transactional alerts, marketing campaigns, OTP verification, and multi-channel automation. For rich messaging with interactive elements, see [RCS messaging](./rcs-messaging).

<Warning>
  To comply with U.S. carrier regulations, proper consent and registration (e.g., 10DLC or toll-free) are **required** before sending SMS or MMS messages. See [SMS registration requirements](./sms-registration-requirements).
</Warning>

* **Send marketing and transactional messages** from the [dashboard](#send-from-the-dashboard) or via the [API](/reference/create-message)
* **Create automated multi-channel flows** with [Journeys](./journeys-overview)
* **Target users precisely** using [segments](./segmentation), filters, or user data
* **Personalize content** with user attributes and [dynamic content](./message-personalization)
* **Integrate with CRMs and tools** like HubSpot, Mixpanel, Amplitude, Zapier, and [more](./integrations)

## SMS setup

Before sending SMS, complete setup and carrier registration. See [which countries are supported](#which-countries-does-onesignal-sms-support).

<Columns cols={2}>
  <Card title="SMS setup" icon="message" href="./sms-setup">
    Get started with OneSignal SMS or integrate with a provider like Twilio.
  </Card>

  <Card title="Toll-free and 10DLC registration" icon="file-certificate" href="./sms-registration-requirements">
    Register for toll-free or 10DLC numbers to ensure carrier compliance and deliverability.
  </Card>

  <Card title="SMS consent keyword management" icon="keyboard" href="./sms-consent-keyword-management">
    Manage keywords like STOP, HELP, and START for compliance and user control.
  </Card>
</Columns>

***

## SMS opt-in

Users must explicitly consent to receive SMS messages. Collect and manage opt-in status before sending.

<Columns cols={2}>
  <Card title="SMS opt-in" icon="square-check" href="./sms-opt-in-and-collection">
    Capture valid user consent for SMS messaging.
  </Card>

  <Card title="Importing phone numbers" icon="upload" href="./import">
    Add existing phone numbers to your OneSignal audience.
  </Card>
</Columns>

***

## Features and use cases

OneSignal SMS supports personalization, localization, and transactional messaging out of the box.

<Columns cols={2}>
  <Card title="Message personalization" icon="user-pen" href="./message-personalization">
    Use dynamic content and user data to personalize messages.
  </Card>

  <Card title="Multi-language messaging" icon="language" href="./multi-language-messaging">
    Send SMS in multiple languages based on user preferences.
  </Card>

  <Card title="Transactional messages" icon="bolt" href="./transactional-messages">
    Send time-sensitive alerts and notifications.
  </Card>

  <Card title="Verification, OTP, and two-factor authentication" icon="lock" href="./example-verification-magic-link-otp">
    Implement secure verification and authentication methods.
  </Card>
</Columns>

***

## Analytics

Track SMS delivery, engagement, and costs:

<Columns cols={2}>
  <Card title="SMS message reports" icon="chart-line" href="./sms-message-reports">
    View message-level delivery and engagement metrics.
  </Card>

  <Card title="Event Streams" icon="signal-stream" href="./event-streams">
    Stream SMS events to your data warehouse or BI tools.
  </Card>

  <Card title="View messages API" icon="code" href="/reference/view-messages">
    Retrieve SMS delivery and engagement metrics programmatically.
  </Card>

  <Card title="Analytics overview" icon="chart-bar" href="./analytics-overview">
    Explore analytics across all OneSignal channels.
  </Card>
</Columns>

***

## Send SMS and MMS

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
    * Start from scratch
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

#### Delivery schedule

| Option               | Description                                        | API field    |
| -------------------- | -------------------------------------------------- | ------------ |
| **Send immediately** | Deliver to all recipients now.                     | —            |
| **Scheduled**        | Send at a specific time, up to 30 days in advance. | `send_after` |

<Info>
  All text messages are subject to a throughput rate (e.g., 1 message per second) determined by your sender type. Contact `support@onesignal.com` if you need higher throughput.
</Info>

### SMS content and encoding

SMS supports plain text and emojis. Formatting like bold and italics is **not supported**.

<Warning>
  Carrier pricing is based on the number of **message segments**. Segment count depends on your message length and character encoding. Messages with emojis or non-Latin characters use UCS-2 encoding, which significantly reduces the character limit per segment. Always review the estimated character and segment count in the OneSignal dashboard before sending.
</Warning>

| Encoding  | Characters per segment | Used for                           |
| --------- | ---------------------- | ---------------------------------- |
| **GSM-7** | Up to 160              | Basic Latin characters and symbols |
| **UCS-2** | Up to 70               | Emojis and non-Latin scripts       |

<Frame caption="GSM-7 encoded message — likely 2 message segments.">
  <img src="https://mintcdn.com/onesignal/l6hM8awIb5Rv0hpW/images/dashboard/gsm-7-encoded-message.png?fit=max&auto=format&n=l6hM8awIb5Rv0hpW&q=85&s=640d82de0683dcc207bfb9625d499510" alt="OneSignal SMS composer showing a GSM-7 encoded message with segment count" width="2650" height="1964" data-path="images/dashboard/gsm-7-encoded-message.png" />
</Frame>

<Frame caption="UCS-2 encoded message — likely 3 message segments.">
  <img src="https://mintcdn.com/onesignal/l6hM8awIb5Rv0hpW/images/dashboard/ucs-2-encoded-message.png?fit=max&auto=format&n=l6hM8awIb5Rv0hpW&q=85&s=3c00a572c45221eb662acb8406f2baea" alt="OneSignal SMS composer showing a UCS-2 encoded message with segment count" width="2650" height="1964" data-path="images/dashboard/ucs-2-encoded-message.png" />
</Frame>

### URLs and trackable links

SMS messages support clickable URLs, but space is limited — shortening links is essential. Do not use public URL shorteners like TinyURL or Bitly, as carriers often flag or block them.

OneSignal provides a built-in URL shortener that generates carrier-safe, trackable links.

<Columns cols={2}>
  <Card title="Create links in the dashboard" icon="link" href="./links#sms">
    Generate safe, trackable shortened URLs from the dashboard.
  </Card>

  <Card title="Create links via the API" icon="code" href="/reference/sms">
    Shorten and track URLs programmatically.
  </Card>
</Columns>

### MMS media

You can include up to **10 media URLs** per MMS, with a total size under **5 MB**. Supported types: `image/jpeg`, `image/gif`, `image/png`, and [other formats](https://www.twilio.com/docs/sms/accepted-mime-types#accepted-mime-types).

<Note>
  Twilio only supports MMS in the US, Canada, and Australia.
</Note>

<Frame caption="MMS media attachment interface.">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7553ebb-Screenshot_2024-05-01_at_1.23.31_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=7635e6588600b17091474012e1ba5443" alt="OneSignal MMS composer showing media attachment options" width="1160" height="1020" data-path="images/docs/7553ebb-Screenshot_2024-05-01_at_1.23.31_PM.png" />
</Frame>

***

## FAQ

### Which countries does OneSignal SMS support?

OneSignal supports sending SMS to the following countries:

| Americas      | Europe         | Asia                 | Oceania     |
| ------------- | -------------- | -------------------- | ----------- |
| Argentina     | Austria        | China                | Australia   |
| Brazil        | Belgium        | Hong Kong            | New Zealand |
| Canada        | Denmark        | India                |             |
| Chile         | Finland        | Japan                |             |
| Mexico        | France         | Macao                |             |
| Peru          | Germany        | Malaysia             |             |
| Puerto Rico   | Iceland        | Philippines          |             |
| United States | Ireland        | Singapore            |             |
|               | Italy          | South Korea          |             |
|               | Luxembourg     | Taiwan               |             |
|               | Netherlands    | Thailand             |             |
|               | Norway         | Turkey               |             |
|               | Poland         | United Arab Emirates |             |
|               | Portugal       |                      |             |
|               | Spain          |                      |             |
|               | Sweden         |                      |             |
|               | Switzerland    |                      |             |
|               | United Kingdom |                      |             |

Additional countries require an upgraded security package. [Contact our sales team](https://onesignal.com/contact) for details.

### What is the difference between SMS, MMS, and RCS?

**SMS** (Short Message Service) supports plain text messages up to 160 characters (GSM-7 encoding). **MMS** (Multimedia Messaging Service) supports images, GIFs, and longer text. **RCS** (Rich Communication Services) is a newer standard that supports richer media, read receipts, and interactive elements — availability depends on carrier and device support. See [RCS messaging](./rcs-messaging) for details.

### How does message segment pricing work?

Carriers charge per message segment, not per message. A standard SMS (GSM-7) allows 160 characters per segment. If your message exceeds that, it's split into multiple segments — each billed separately. Using emojis or non-Latin characters switches to UCS-2 encoding, which allows only 70 characters per segment.

### Why are my SMS messages being blocked by carriers?

Common causes include missing 10DLC or toll-free registration, using public URL shorteners (Bitly, TinyURL), sending without proper user consent, or exceeding throughput limits. See [SMS registration requirements](./sms-registration-requirements) for compliance details.

### How do I test SMS before sending to my audience?

Send a test message to your own phone number first. In the dashboard, use the **Send test message** option to verify content, encoding, link tracking, and segment count before sending to your full audience.

Built with [Mintlify](https://mintlify.com).
