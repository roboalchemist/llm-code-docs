# Source: https://plivo.com/docs/faq/messaging/sms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS

> SMS delivery, encoding, concatenation, sender ID, and country-specific rules

Frequently asked questions about SMS messaging, character limits, concatenation, and delivery.

***

## What is the character limit for SMS text messages?

### GSM-7 Encoding (Standard Characters)

| Message Length      | Segments | Characters per Segment   |
| ------------------- | -------- | ------------------------ |
| 1-160 characters    | 1        | 160                      |
| 161-1600 characters | Multiple | 153 (7 chars for header) |

**Maximum:** 1,600 characters (splits into \~11 segments)

### Unicode Encoding (Special Characters)

| Message Length  | Segments | Characters per Segment  |
| --------------- | -------- | ----------------------- |
| 1-70 characters | 1        | 70                      |
| 71+ characters  | Multiple | 67 (3 chars for header) |

When any Unicode character appears in your message, the entire message uses UCS-2 encoding.

***

## What is automatic encoding?

Automatic encoding replaces Unicode characters with GSM-7 equivalents to prevent accidental segmentation from smart quotes, em dashes, etc.

### Enable Auto-Replace

1. Navigate to **Messaging > Settings > Other Settings**
2. Enable **Auto-replace**

***

## How does SMS concatenation work?

Long messages are automatically split and reassembled:

1. Plivo splits message into segments
2. Concatenation header added to each segment
3. Carrier reassembles at delivery
4. Recipient sees single message

### Billing

Each segment is billed separately. A 200-character message = 2 segments = 2x SMS cost.

***

## How do I send SMS via API?

### Single Message

```bash  theme={null}
curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Message/" \
  -u "{auth_id}:{auth_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "src": "14151234567",
    "dst": "14157654321",
    "text": "Hello from Plivo!"
  }'
```

### Can I send bulk SMS?

Yes. Send to multiple recipients in one request:

```bash  theme={null}
curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Message/" \
  -u "{auth_id}:{auth_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "src": "14151234567",
    "dst": "14157654321<14158765432<14159876543",
    "text": "Bulk message to multiple recipients"
  }'
```

Separate destinations with `<` character.

***

## How can I receive SMS messages on my Plivo numbers?

1. Create an application with a `message_url`
2. Assign a Plivo number to the application
3. Plivo POSTs inbound messages to your URL

***

## How is an incoming message delivered to my application?

| Stage           | Description                               |
| --------------- | ----------------------------------------- |
| **Received**    | Plivo receives from carrier (charged)     |
| **Delivered**   | Successfully posted to your `message_url` |
| **Undelivered** | Failed to deliver to your URL             |

If `message_url` is not configured, messages remain in "received" status.

***

## Can the source number for an outbound text message be a non-Plivo number?

### US and Canada

* **Must use Plivo number** as source
* Non-Plivo numbers not permitted (telecom regulations)

### International

* Dynamic sender IDs may be used
* Delivery not guaranteed for non-Plivo numbers
* Check [country coverage](https://www.plivo.com/coverage/) for sender ID support

***

## What are Geo-Permissions and why should I use them?

Geo-Permissions control which countries can receive your SMS, protecting against fraud.

### Default Enabled Countries

* United States
* United Kingdom
* India

### How Can I Manage Geo-Permissions?

1. Navigate to **Messaging > Settings > [Geo Permissions](https://cx.plivo.com/messaging-settings)**
2. Enable/disable countries as needed
3. Set messages-per-hour fraud thresholds

***

## Can I configure SMS Geo Permissions for each subaccount separately?

Yes. By default, subaccounts inherit main account settings.

**Override for subaccount:**

1. Go to Geo Permissions
2. Select subaccount from dropdown
3. Customize settings
4. Subaccount shows "Overridden" tag

**Remove override:**

1. Select overridden subaccount
2. Click **Remove Override**

***

## Why are my outbound messages failing with error code 450?

Error 450 means "destination country barred." The destination country is not enabled in your Geo Permissions.

Enable the country in **Messaging > Settings > Geo Permissions**.

***

## What is SMS Pumping and how does Plivo protect against it?

SMS pumping is fraud where attackers flood OTP fields with fake requests to premium numbers.

### Protection Features

Enabled by default for all accounts:

* Automated traffic analysis
* Suspicious pattern detection
* Alerts for unusual activity

### How to Prevent SMS Pumping Attacks?

* Enable [Geo Permissions](#what-are-geo-permissions-and-why-should-i-use-them)
* Set rate limits on OTP endpoints
* Implement CAPTCHA on forms
* Monitor traffic patterns
* Use Plivo's fraud detection tools

***

## How to access the message content?

Message content is stored for **7 days**.

### View in Console

1. Navigate to **Messaging > Logs**
2. Search by timeframe or UUID
3. View message details

**Note:** Only available if data logging is enabled.

***

## Why should I authorize Plivo to view my SMS content?

Allow Plivo support to view content for debugging:

* Helps identify spam filter triggers
* Assists with delivery issues
* Enables content policy review

***

## What happens to my outbound messages if I don't have sufficient balance?

When balance is insufficient:

1. Messages fail with error code 900
2. API requests fail for 2 minutes with "Insufficient Credit"
3. Queued messages continue to fail until recharged

Set up [auto-recharge](/docs/billing/payments) to prevent interruptions.

***

## Why were we charged for an undelivered SMS message?

Plivo charges when a message is successfully handed off to downstream carriers. Once accepted by the carrier, Plivo has no control over final delivery.

Reasons for undelivered status:

* Invalid or unreachable destination number
* Carrier filtering
* Device issues (phone off, full inbox)

***

## What are the different SMS statuses in Plivo?

| Status          | Description                                          |
| --------------- | ---------------------------------------------------- |
| **queued**      | Message accepted, waiting to send                    |
| **sent**        | Successfully passed to downstream carrier (charged)  |
| **delivered**   | Confirmed delivery to recipient device               |
| **undelivered** | Carrier could not deliver to recipient               |
| **failed**      | Internal error before reaching carrier (not charged) |

***

## What are the Toll-Free Surcharges?

US carriers impose surcharges on toll-free messaging:

| Carrier  | Surcharge per Segment |
| -------- | --------------------- |
| Verizon  | \$0.0025              |
| T-Mobile | Varies                |
| AT\&T    | Varies                |

Surcharges appear as separate invoice line items.

***

## What is the Number Lookup API?

Get information about phone numbers:

* Local and E.164 formatting
* Carrier information
* Caller ID name (CNAM)

See [Lookup API documentation](https://www.plivo.com/docs/lookup/).

***

## Related Resources

* [Messaging API Overview](/docs/messaging/messaging-api)
* [MMS](/docs/messaging/mms)
* [US Messaging](/docs/messaging/us-messaging)
* [SMS API Reference](https://www.plivo.com/docs/messaging/api/message/)
