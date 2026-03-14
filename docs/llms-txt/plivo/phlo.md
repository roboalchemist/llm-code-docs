# Source: https://plivo.com/docs/faq/messaging/phlo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PHLO for Messaging

> Using PHLO visual workflow builder for messaging automation

Frequently asked questions about using PHLO (Plivo High Level Objects) for SMS workflows.

***

## What is PHLO?

PHLO provides a visual workflow builder for messaging automation without writing code. Common use cases include:

* Forwarding incoming SMS to another number
* Auto-responding to inbound messages
* Tracking outbound message delivery status

***

## How can I forward messages to Plivo numbers using PHLO?

1. Create a new PHLO
2. Add a **Send SMS** node connected to **Incoming SMS** in the start node
3. Rename the node (e.g., "Forward\_SMS")
4. Configure the node:

| Field   | Value                                                               |
| ------- | ------------------------------------------------------------------- |
| From    | `{{Start.message.from}}` (dynamic) or a valid Plivo number (static) |
| To      | Your destination number                                             |
| Message | `{{Start.message.text}}` (forwards original message)                |

5. Click **Validate** to save
6. Click **Save**
7. Attach the PHLO to an SMS-enabled Plivo number

**Note:** Using `{{Start.message.from}}` takes the actual source from the received message. If the source is a short code not rented in your account, forwarding will fail. Using a Plivo number in the From field is recommended.

***

## How do I set up an autoresponder for inbound SMS?

1. Create a new PHLO
2. Connect a **Send SMS** node to **Incoming SMS** in the start node
3. Configure the node:

| Field   | Value                                                               |
| ------- | ------------------------------------------------------------------- |
| From    | `{{Start.message.to}}` (the Plivo number that received the message) |
| To      | `{{Start.message.from}}` (the sender's number)                      |
| Message | Your auto-reply text                                                |

4. Click **Validate** and **Save**
5. Attach the PHLO to your Plivo number

See [Getting Started with SMS Autoresponder](https://www.plivo.com/docs/messaging/quickstart/sms-autoresponder/) for detailed configuration.

***

## How do I receive message details for an outbound SMS?

Use the **Event Callbacks** option in the Send SMS component:

1. In your PHLO, select the **Send SMS** component
2. Locate the **Event Callbacks** option
3. Add your callback URL
4. Select which message states to receive callbacks for

### Available Status Events

| Status      | Description                       |
| ----------- | --------------------------------- |
| queued      | Message accepted, waiting to send |
| sent        | Message sent to carrier           |
| delivered   | Confirmed delivery to recipient   |
| undelivered | Failed to deliver                 |
| failed      | Error occurred before sending     |

Each selected status triggers a callback to your URL with message details.

***

## What variables can I use in PHLO for messaging?

### Inbound Message Variables

| Variable                 | Description                            |
| ------------------------ | -------------------------------------- |
| `{{Start.message.from}}` | Sender's phone number                  |
| `{{Start.message.to}}`   | Plivo number that received the message |
| `{{Start.message.text}}` | Message content                        |

Variables can be used in any text field within PHLO nodes including message content, From/To fields, and callback URLs.

***

## How do I attach a PHLO to a phone number?

**Via Phone Number:**

1. Navigate to **Phone Numbers > Active**
2. Click on your phone number
3. Select **PHLO** for Application Type
4. Choose your PHLO from the dropdown
5. Click **Update**

**Via Powerpack:**

1. Navigate to your Powerpack
2. In Application Configuration, select **PHLO**
3. Select your PHLO application
4. Update

***

## Related Resources

* [PHLO Overview](https://www.plivo.com/docs/phlo/)
* [Messaging API](/docs/messaging/messaging-api)
* [Powerpack](/docs/messaging/powerpack)
