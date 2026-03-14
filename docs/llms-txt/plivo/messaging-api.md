# Source: https://plivo.com/docs/faq/messaging/messaging-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Messaging API

> Common questions about sending and receiving SMS and MMS via Plivo API

Frequently asked questions about Plivo's Messaging API, throughput limits, message expiry, and data logging.

***

## What does Plivo's Messaging API offer?

Plivo's Messaging API enables SMS and MMS messaging to 200+ countries with:

* Programmable SMS/MMS via REST API
* High throughput delivery
* Delivery receipts and callbacks
* Message logging and analytics

***

## What is Messages Per Second (MPS)?

MPS limits control how fast your account can send messages.

### Default Limits

| Type | Default MPS |
| ---- | ----------- |
| SMS  | 5 MPS       |
| MMS  | 0.25 MPS    |

View your allocated MPS at **SMS > Overview** in the console.

***

## What is the throughput for US numbers?

| Number Type                | SMS Throughput   | MMS Throughput | Daily Limit |
| -------------------------- | ---------------- | -------------- | ----------- |
| Long Code (Unregistered)   | 1 msg/sec        | 1 msg/sec      | 2,000/day   |
| Long Code (10DLC Low)      | 0.2-0.75 msg/sec | Varies         | Varies      |
| Long Code (10DLC Standard) | 3.75-15 msg/sec  | Varies         | Varies      |
| Toll-Free (Verified)       | 25 msg/sec       | 2 msg/sec      | No limit    |
| Short Code                 | 100+ msg/sec     | Not supported  | No limit    |

***

## What is the throughput for Canada numbers?

| Number Type | SMS       | MMS           |
| ----------- | --------- | ------------- |
| Long Code   | 15/minute | 15/minute     |
| Toll-Free   | 25/second | 2/second      |
| Short Code  | 10/second | Not supported |

**Note:** Verify toll-free numbers to avoid sending limits.

***

## What happens when a message expires?

Messages remaining in queue after **3 hours** expire automatically.

* Message marked as "failed"
* Error code: 420
* No charge applied

Messages may expire due to carrier delays, invalid destination numbers, or network issues.

***

## How can I control my data logging preferences?

Control how Plivo stores your message data:

| Setting                  | Destination Number | Message Content |
| ------------------------ | ------------------ | --------------- |
| **Store Both** (Default) | Stored             | Stored          |
| **Store Number Only**    | Stored             | Not stored      |
| **Store Content Only**   | Not stored         | Stored          |
| **Store Neither**        | Not stored         | Not stored      |

Set the `log` parameter in the [Send Message API](https://www.plivo.com/docs/messaging/api/message/#send-a-message).

***

## What's the difference between promotional and transactional SMS?

| Type              | Purpose               | Examples                          |
| ----------------- | --------------------- | --------------------------------- |
| **Promotional**   | Marketing, sales      | Offers, discounts, advertisements |
| **Transactional** | Essential information | OTPs, order confirmations, alerts |

Different countries have varying regulations for each type.

***

## How does Plivo protect against fraud?

### Geo Permissions

Restrict messaging to specific countries:

1. Navigate to **SMS > Settings > [Geo Permissions](https://cx.plivo.com/messaging-settings)**
2. Enable only required destination countries
3. Set messaging thresholds per country

### Unusual Traffic Alerts

Plivo monitors for suspicious patterns:

* Sudden traffic spikes
* Unusual destinations
* Potential account takeover

You'll receive alerts via email when anomalies are detected.

### Monthly Limits

Set spending caps to prevent runaway costs from fraud.

***

## How do I export Message Detail Records (MDR)?

### Via Console

1. Navigate to **SMS > Logs**
2. Click **Filter Logs** to refine
3. Select records to export
4. Click **Export**

Small exports download directly; large exports are emailed.

### Via API

Use the [Message API](https://www.plivo.com/docs/messaging/api/message/#list-all-messages) to retrieve records programmatically.

***

## How can I add a line break in my SMS or MMS message?

Use `\n` for line breaks:

```bash  theme={null}
curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Message/" \
  -u "{auth_id}:{auth_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "src": "14151234567",
    "dst": "14157654321",
    "text": "Line 1\nLine 2\nLine 3"
  }'
```

***

## What countries do you support for SMS?

| Direction    | Coverage                                                                          |
| ------------ | --------------------------------------------------------------------------------- |
| Outbound SMS | 200+ countries                                                                    |
| Inbound SMS  | US, Canada, UK, Australia, France, Germany, Netherlands, Sweden, Austria, Belgium |

See [Plivo Coverage](https://www.plivo.com/coverage/) for details.

***

## What are the compliance standards for messaging?

All messaging must follow:

* Regional laws and regulations
* Carrier policies
* [Plivo Acceptable Use Policy](https://www.plivo.com/aup/)

### Prohibited Content

* Unsolicited spam
* Fraudulent or deceptive content
* Violence, hate speech, obscenity
* Illegal substances promotion

See [Messaging Compliance](/docs/messaging/messaging-compliance) for details.

***

## How do I integrate with Bitrix24?

1. Install Plivo from Bitrix24 Marketplace
2. Enter Auth ID, Auth Token, and sender ID
3. Click **Test SMS** to validate

***

## Related Resources

* [SMS](/docs/messaging/sms)
* [MMS](/docs/messaging/mms)
* [US Messaging (10DLC, Toll-Free)](/docs/messaging/us-messaging)
* [Short Codes](/docs/messaging/short-codes)
* [PHLO for Messaging](/docs/messaging/phlo)
* [ISV Guidelines](/docs/messaging/isv-guidelines)
* [Messaging API Reference](https://www.plivo.com/docs/messaging/api/)
