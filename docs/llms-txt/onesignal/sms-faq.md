# Source: https://documentation.onesignal.com/docs/en/sms-faq.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS FAQ

> Troubleshooting, encoding, sender types, and compliance answers for OneSignal SMS and MMS messaging.

Common questions about SMS messaging, encoding, sender configuration, and compliance.

## Troubleshooting

### Why are my messages not displaying?

Check the following:

* **Sender number does not support MMS.** If images are missing, verify the "From" number you purchased from Twilio supports MMS.
* **You are on Twilio's unsubscribe list.** Text `START` to the "From" number and try again.
* **Phone number is not in E.164 format.** OneSignal requires all phone numbers in [E.164 format](#what-is-e164-format).

### How do I send international SMS?

The steps depend on your SMS provider:

* **OneSignal SMS** — International sending is supported to [specific countries](./sms-messaging#which-countries-does-onesignal-sms-support). Additional countries require an upgraded security package — [contact sales](https://onesignal.com/contact).
* **Twilio** — Enable international texting in your Twilio console under **Messaging > Settings > Geo permissions**.

***

## Message format and encoding

### What is E.164 format?

E.164 is an international standard for phone number formatting. OneSignal requires all phone numbers in this format: a `+` prefix, country code, and subscriber number with no spaces or leading zeros.

* US: `999 999 9999` → `+19999999999`
* UK (London): `020 9999 9999` → `+442099999999`

### What is the SMS character limit and how does encoding affect it?

SMS uses **GSM-7** encoding by default (Latin characters, numbers, common symbols), which allows 160 characters per segment. Messages containing emojis or non-Latin scripts (e.g., Chinese, Arabic) switch to **UCS-2** encoding, which allows only 70 characters per segment.

Messages exceeding these limits are split into multiple segments, with 7 bytes reserved per segment for reassembly — reducing usable characters to 153 (GSM-7) or 67 (UCS-2). You can use the [Twilio message segment calculator](https://twiliodeved.github.io/message-segment-calculator/) to verify counts. For more detail, see [SMS content and encoding](./sms-messaging#sms-content-and-encoding).

### Can I send MMS?

Yes, depending on your country and if your "From" number supports MMS. You can attach up to 10 media URLs per message (total size under 5 MB). For supported media types and regional availability, see [MMS media](./sms-messaging#mms-media).

***

## Subscribers and consent

### How do I add SMS subscribers?

You can add SMS subscribers in several ways:

* **SDK** — Use the `addSms()` method to associate a phone number with a user.
* **Import** — Upload a CSV of phone numbers through the dashboard. See [Import phone numbers](./import).
* **API** — Create or update users with phone numbers via the [REST API](/reference/create-user).

All phone numbers must be in [E.164 format](#what-is-e164-format).

### How do users unsubscribe or resubscribe?

Users can text **STOP** to your sending number to unsubscribe from all SMS, and **START** to resubscribe. You can configure additional keywords (like HELP) and auto-responses in your OneSignal dashboard under **Settings > SMS > Consent Management**. See [SMS consent keyword management](./sms-consent-keyword-management).

### Does OneSignal support two-way SMS?

OneSignal supports keyword-based replies for consent management, including text-to-subscribe and double opt-in flows. Full conversational two-way SMS (where you receive and respond to arbitrary user messages) is not supported. Configure keyword replies in your OneSignal dashboard under **Settings > SMS > Consent Management**.

***

## Sender types

### What are the different SMS sender types?

The sender type determines the phone number or ID that appears in the "From" field of your messages.

| Type                       | Format                                 | Throughput         | Notes                                                                                                                                                                    |
| -------------------------- | -------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Long code**              | 10-digit number (e.g., `999-999-9999`) | Low                | Subject to carrier filtering for A2P traffic                                                                                                                             |
| **Short code**             | 5–6 digits                             | High               | Carrier-approved; 8–12 week setup. US, CA, UK only. See [Twilio short codes](https://www.twilio.com/guidelines/short-code)                                               |
| **Toll-free**              | 10-digit, 8XX prefix                   | Medium (3 msg/sec) | Can be carrier-verified to reduce filtering                                                                                                                              |
| **Alphanumeric sender ID** | Custom string, up to 11 chars          | Varies             | One-way only; not supported in US/CA. See [supported countries](https://support.twilio.com/hc/en-us/articles/223133767-International-support-for-Alphanumeric-Sender-ID) |

To use an alphanumeric sender ID, create one and add it to a Twilio Messaging Service. Characters allowed: A–z, 0–9, and space (no special characters). Some countries require pre-registration — see the [Twilio setup guide](https://support.twilio.com/hc/en-us/articles/223181348-Getting-started-with-Alphanumeric-Sender-ID).

### What is a Twilio Messaging Service?

A [Messaging Service](https://www.twilio.com/docs/sms/services) is a Twilio feature that pools multiple sender numbers (long codes, short codes, toll-free) under a shared configuration. Benefits include:

* **Load balancing** — Distributes outbound traffic across pooled numbers for higher throughput.
* **Geo-matching** — Routes messages through local numbers when available.
* **Short code priority** — Sends via short code first when one is in the pool.
* **MMS fallback** — Converts MMS to an SMS with a media URL link if the carrier or device does not support MMS.

A Messaging Service is also required for 10DLC compliance in the US. Even if you do not send through the Messaging Service directly, your sender numbers must be linked to one.

***

## Compliance and regulations

### What is A2P 10DLC?

A2P 10DLC (Application-to-Person 10-Digit Long Code) is a US carrier system that allows businesses to send SMS over standard 10-digit phone numbers with improved deliverability. All Twilio traffic in the US is classified as A2P.

Businesses must register their brand and campaigns through Twilio. Message throughput is determined by your brand's trust score and campaign type. Registration helps reduce carrier filtering and improves delivery speed compared to unregistered long codes.

### What SMS regulations should I follow?

<Warning>
  This section is not legal advice. Consult your legal team for detailed guidance on SMS regulations in your region.
</Warning>

At a minimum:

* Send only to users who have explicitly opted in
* Clearly communicate what users are subscribing to
* Maintain opt-in records including consent type, timestamp, and frequency
* Honor opt-out requests immediately (e.g., STOP keyword)

For US-specific guidance:

* [Twilio SMS compliance guide](https://www.twilio.com/learn/call-and-text-marketing/guide-to-us-sms-compliance)
* [CTIA Messaging Principles and Best Practices](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)

<Note>
  Regulations vary by country. Review [Twilio's country-specific guidelines](https://www.twilio.com/guidelines/sms) and research local laws before sending international messages.
</Note>

***

<Card title="SMS overview" icon="message" href="./sms-messaging">
  Set up, send, and track SMS and MMS messages with OneSignal.
</Card>

Built with [Mintlify](https://mintlify.com).
