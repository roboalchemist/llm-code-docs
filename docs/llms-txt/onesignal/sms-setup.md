# Source: https://documentation.onesignal.com/docs/en/sms-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS/RCS setup

> Configure your SMS/RCS provider, set a default sender number, send a test message, and add subscribers in OneSignal.

Set up SMS in your OneSignal dashboard to start sending SMS and MMS messages. The process takes about 10 minutes, but carrier registration (10DLC or toll-free) may take weeks.

Before you begin:

* Review [SMS regulatory compliance](./sms-regulatory-compliance) and [RCS details](./rcs-messaging)
* Understand [SMS registration requirements](./sms-registration-requirements), including user consent
* Have your SMS provider credentials ready (if using Twilio)

<Frame caption="SMS channel setup overview.">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/3146e1e2dcb023bc1ca20d841f6dd5c9c40ed9bd484f07a6d34b9f1fd241b387-channel-setup-sms.jpg?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=5f18ce368b17a99d98251a59023d12ce" alt="OneSignal SMS setup flow diagram showing provider, number, and subscriber steps" width="1280" height="720" data-path="images/docs/3146e1e2dcb023bc1ca20d841f6dd5c9c40ed9bd484f07a6d34b9f1fd241b387-channel-setup-sms.jpg" />
</Frame>

***

## Step 1: Select a provider

In your OneSignal dashboard, navigate to **Settings > Set up SMS / RCS**.

<Frame caption="SMS/RCS provider selection in the OneSignal dashboard.">
  <img src="https://mintcdn.com/onesignal/l6hM8awIb5Rv0hpW/images/dashboard/sms-rcs-provider-selection.png?fit=max&auto=format&n=l6hM8awIb5Rv0hpW&q=85&s=7fddde7e47d394cbf3c254a322925c85" alt="OneSignal dashboard showing OneSignal and Twilio provider options" width="2658" height="1736" data-path="images/dashboard/sms-rcs-provider-selection.png" />
</Frame>

<Tabs>
  <Tab title="OneSignal">
    OneSignal leverages Twilio under the hood. Choose this if:

    * You send more than 5,000 SMS per month
    * You are on a paid OneSignal plan (see [pricing](https://onesignal.com/pricing))

    Click **Book Demo with SMS Expert** to get started.

    <Note>
      While waiting for verification, you can begin designing [SMS templates](./templates) and completing [registration requirements](./sms-registration-requirements).
    </Note>
  </Tab>

  <Tab title="Twilio">
    Use your own Twilio account if:

    * You send fewer than 5,000 SMS per month
    * You want full control of your Twilio configuration

    Add your **Twilio Account SID** and **Auth Token** from the Twilio dashboard, then click **Next: Add Phone Numbers**.

    <Frame caption="Enter Twilio credentials in OneSignal.">
      <img src="https://mintcdn.com/onesignal/l6hM8awIb5Rv0hpW/images/dashboard/twilio-credentials.png?fit=max&auto=format&n=l6hM8awIb5Rv0hpW&q=85&s=cfeaa0502717f14e227c6a7e1c1d4909" alt="OneSignal SMS configuration screen with Twilio Account SID and Auth Token fields" width="2736" height="2020" data-path="images/dashboard/twilio-credentials.png" />
    </Frame>
  </Tab>
</Tabs>

***

## Step 2: Set the default "From" number

Once verified, OneSignal retrieves all phone numbers linked to your account. Select a **default number** to use when sending. You can override this per message.

### Send a test SMS

Enter your phone number and click **Send Test SMS**.

If the message does not arrive:

* Confirm the default number supports SMS
* Check Twilio logs for errors

<Warning>
  Twilio trial accounts require recipient numbers to be [pre-registered](https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account).
</Warning>

Click **Next: Add Subscribers**.

***

## Step 3: Add subscribers

Each phone number is a separate SMS Subscription in OneSignal. You can add subscribers through:

* **Dashboard** — Upload phone numbers via CSV. See [Import phone numbers](./import).
* **SDK** — Use the `addSms()` method to associate a phone number with a user.
* **API** — Create or update users via the [REST API](/reference/create-user).
* **Web prompt** — Capture phone numbers with [permission requests](./permission-requests).

All phone numbers must be in [E.164 format](https://en.wikipedia.org/wiki/E.164) (e.g., `+19999999999`). Phone numbers are anonymous until you assign an [External ID](./users).

***

## Step 4: Configure compliance

Carrier regulations require proper consent and registration before sending SMS.

<Warning>
  With iOS 26, SMS messages from "unknown" senders are screened out. To be recognized as a known sender, use opt-in methods where the user sends the first message — such as text-to-join keywords, tap-to-join links, or QR codes that open a pre-filled text thread.
</Warning>

<Columns cols={2}>
  <Card title="SMS regulatory compliance" icon="scale-balanced" href="./sms-regulatory-compliance">
    Applicable laws and requirements for SMS messaging.
  </Card>

  <Card title="SMS registration requirements" icon="file-certificate" href="./sms-registration-requirements">
    10DLC, toll-free, and short code registration.
  </Card>
</Columns>

***

## Senders and consent management

After setup, manage your sender numbers and consent keywords in your OneSignal dashboard.

**Senders** — Under **Settings > SMS > Senders**, update your default sender number and configure whether it can receive replies.

**Consent keywords** — Under **Settings > SMS > Consent Management**, configure opt-in, opt-out (STOP), resubscribe (START), and help keywords with auto-responses.

<Columns cols={2}>
  <Card title="SMS consent keyword management" icon="keyboard" href="./sms-consent-keyword-management">
    Configure default and custom consent keywords.
  </Card>

  <Card title="SMS keywords" icon="reply" href="./keywords">
    Set up custom auto-response keywords.
  </Card>
</Columns>

***

## FAQ

### Do I need a Twilio account to send SMS with OneSignal?

No. You can use OneSignal's managed SMS infrastructure, which handles Twilio under the hood. This option is available on paid plans for accounts sending more than 5,000 messages per month. Alternatively, you can connect your own Twilio account for direct control.

### What phone number format does OneSignal require?

All phone numbers must use E.164 format: a `+` prefix followed by the country code and subscriber number with no spaces. For example, a US number `999 999 9999` becomes `+19999999999`. See [E.164 format](./sms-faq#what-is-e164-format) for more examples.

### How long does SMS registration take?

It depends on the registration type. Toll-free verification typically takes 1–2 weeks. 10DLC brand and campaign registration can take a few days to several weeks depending on your trust score. Short code approval takes 8–12 weeks. You can begin building templates while waiting.

### Can I use multiple sender numbers?

Yes. OneSignal retrieves all phone numbers linked to your Twilio account. You set one as the default, but you can override the sender number per message.

***

## After setup

Once setup is complete, you're ready to start sending messages.

<Columns cols={3}>
  <Card title="SMS overview" icon="message" href="./sms-messaging">
    Send, personalize, and track SMS and MMS messages.
  </Card>

  <Card title="Templates" icon="file-lines" href="./templates">
    Create reusable SMS and MMS templates.
  </Card>

  <Card title="Journeys" icon="route" href="./journeys-overview">
    Build automated multi-channel messaging flows.
  </Card>

  <Card title="Message personalization" icon="user-pen" href="./message-personalization">
    Use dynamic content and user data in messages.
  </Card>

  <Card title="SMS message reports" icon="chart-line" href="./sms-message-reports">
    View delivery and engagement metrics.
  </Card>

  <Card title="SMS FAQ" icon="circle-question" href="./sms-faq">
    Troubleshooting, encoding, and sender types.
  </Card>
</Columns>

Built with [Mintlify](https://mintlify.com).
