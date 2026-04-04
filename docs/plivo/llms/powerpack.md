# Source: https://plivo.com/docs/messaging/concepts/powerpack.md

# Source: https://plivo.com/docs/messaging/api/powerpack.md

# Source: https://plivo.com/docs/faq/messaging/powerpack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Powerpack

> Powerpack number pools, sticky sender, and intelligent number selection for SMS

Frequently asked questions about Powerpack, Plivo's intelligent number pool for optimized message delivery.

***

## What is Powerpack?

Powerpack is a collection of phone numbers that work together to:

* Maximize message deliverability
* Manage opt-outs automatically
* Load balance across numbers
* Support multiple number types (long codes, toll-free, short codes)

***

## What are the benefits of Powerpack?

| Feature                 | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| **Intelligent routing** | Automatically selects best number for delivery         |
| **Sticky sender**       | Same number used for conversations with each recipient |
| **Opt-out management**  | Automatic STOP keyword handling                        |
| **Number pool**         | Combine long codes, toll-free, and short codes         |
| **Compliance**          | Respects carrier throughput limits                     |

***

## How do I create a Powerpack?

1. Navigate to **Messaging > Powerpack**
2. Click **Add New Powerpack**
3. Enter Powerpack name
4. Add phone numbers to the pool
5. Configure application settings
6. Save

***

## What types of numbers can I add to Powerpack?

### Long Codes

Add US/Canada long codes for A2P messaging:

* Requires 10DLC registration for optimal throughput
* Recommended: \< 200 messages/day per number

### Toll-Free Numbers

Add verified toll-free numbers:

* Higher throughput (25 MPS)
* Best for 2FA, notifications

### Short Codes

Add short codes for maximum throughput:

* One US short code per Powerpack
* One Canada short code per Powerpack
* Same short code cannot be in multiple Powerpacks

***

## Can I add a short code number to my Powerpack?

Yes. You can add one US short code and one Canada short code per Powerpack.

***

## Can I add multiple short code numbers to my Powerpack?

No. Only one US short code and one Canada short code per Powerpack.

***

## Can I add the same short code number to multiple Powerpacks?

No. A short code can only belong to one Powerpack.

***

## What are the benefits of adding a short code to my Powerpack?

* Maximum throughput (100+ MPS)
* Carrier-approved for A2P messaging
* Falls back to long codes if short code is unavailable

***

## Why are long code numbers being used for outbound messages when I have a short code in my Powerpack?

Even with short code priority enabled, long codes may be used when:

* Short code throughput exceeded
* Network compatibility issues
* Carrier-specific routing

***

## How do I remove a short code from my Powerpack?

To disable short code:

1. Disable "prioritize short code" feature
2. Messages will use other numbers

To permanently remove:

1. Open support ticket
2. Request short code removal

***

## How can I send SMS and MMS messages using Powerpack?

### SMS via API

```bash  theme={null}
curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Message/" \
  -u "{auth_id}:{auth_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "powerpack_uuid": "your-powerpack-uuid",
    "dst": "14157654321",
    "text": "Hello from Powerpack!"
  }'
```

### MMS via Powerpack

```json  theme={null}
{
  "powerpack_uuid": "your-powerpack-uuid",
  "dst": "14157654321",
  "type": "mms",
  "media_urls": ["https://example.com/image.jpg"]
}
```

***

## What is Smart Sender?

Smart Sender ensures that a destination number always receives texts from the same source number. This stickiness enables two-way conversations by keeping the conversation thread intact.

Once a Powerpack number is assigned to a destination, all subsequent texts to that destination are sent from the assigned source number.

Turn on Smart Sender from the Plivo console's Powerpack dashboard.

***

## What is Local Connect?

Local Connect is a Powerpack feature that personalizes conversations by using the same area codes and local numbers as your users.

It uses area code matching and prioritizes local numbers over other numbers in the Powerpack pool.

Manage Local Connect preferences from the Powerpack management console.

***

## What happens when a Powerpack SMS or MMS recipient replies with an opt-out keyword?

When recipient texts STOP:

1. Subscriber added to suppression list for that source number
2. Future messages to that recipient are blocked
3. Message marked "failed" with appropriate error code

### Suppression List

* Per-number suppression tracking
* Automatic compliance with opt-out requests
* View suppression list in console

***

## How are incoming messages to numbers in my Powerpack handled?

Assign an application to your Powerpack to handle incoming messages.

***

## How can I modify an application associated with a Powerpack?

1. Navigate to your Powerpack
2. In Application Configuration, select type:
   * **XML Application**
   * **PHLO**
3. Select the application name
4. Update

***

## How can I remove an application from Powerpack?

1. Open Powerpack settings
2. In application type, select any option
3. In application name dropdown, select "-------"
4. Update

***

## Can I use PHLOs to handle incoming messages in my Powerpack?

Yes. Use PHLO for visual message handling:

1. Create a PHLO for incoming messages
2. Add PHLO to Powerpack's application configuration
3. Incoming messages trigger PHLO workflow

***

## How can I send 6,000 or more SMS messages per day using a long code in the US?

For US long codes without 10DLC, the limit is \< 200 messages/day per number.

**Options:**

* Register for 10DLC to increase limits
* Add multiple numbers to your Powerpack
* Use toll-free or short codes

| Volume           | Recommended           |
| ---------------- | --------------------- |
| \< 2,000/day     | Registered long codes |
| 2,000-50,000/day | Toll-free             |
| 50,000+/day      | Short code            |

***

## How can I configure my Powerpack source number pool?

### Add Numbers

1. Navigate to Powerpack
2. Click **Add Numbers**
3. Select from available numbers
4. Add to pool

### Remove Numbers

1. Navigate to Powerpack
2. Select numbers to remove
3. Click **Remove**

***

## What happens if I unrent a Powerpack phone number?

The number is removed from the Powerpack. Messages will be sent from remaining numbers in the pool.

***

## Related Resources

* [Messaging API Overview](/docs/messaging/messaging-api)
* [US Messaging](/docs/messaging/us-messaging)
* [Powerpack API Reference](https://www.plivo.com/docs/messaging/api/powerpack/)
