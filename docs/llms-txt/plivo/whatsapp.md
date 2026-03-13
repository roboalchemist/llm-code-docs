# Source: https://plivo.com/docs/faq/messaging/whatsapp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# WhatsApp Business API

> WhatsApp Business API setup, templates, pricing, and message types

Frequently asked questions about WhatsApp Business messaging, account setup, message types, and integration with Plivo.

***

## What does WhatsApp Business API offer?

WhatsApp Business API enables direct customer communication on WhatsApp with:

* Real-time messaging
* Global reach (2+ billion users)
* Rich media support
* Message templates
* Delivery receipts

***

## What are the key features of WhatsApp Business?

| Feature                  | Description                                        |
| ------------------------ | -------------------------------------------------- |
| **Business Profile**     | Display business info (address, website, email)    |
| **Message Templates**    | Pre-approved messages for initiating conversations |
| **Rich Media**           | Images, documents, videos, audio                   |
| **Interactive Messages** | Buttons, lists, quick replies                      |
| **Delivery Status**      | Real-time delivery and read receipts               |

***

## What are the prerequisites for WhatsApp Business API?

1. Meta Business Account
2. Business verification with Meta
3. WhatsApp Business Account (WABA)
4. Phone number for WhatsApp

***

## How do I set up WhatsApp Business with Plivo?

1. **Create WABA**: Through Plivo's embedded signup flow
2. **Verify Business**: Complete Meta business verification
3. **Register Phone Number**: Use existing or rent from Plivo
4. **Configure Display Name**: Set business name for WhatsApp
5. **Create Templates**: Submit templates for approval
6. **Integrate API**: Connect your systems

See [WhatsApp concepts](https://www.plivo.com/docs/whatsapp/concepts/) for detailed setup.

***

## What is a WhatsApp Business Account (WABA)?

A WhatsApp Business Account contains:

* Your phone numbers
* Message templates
* Business profile
* Messaging configuration

When onboarding with Plivo, a WABA is created with Plivo as the partner.

***

## Why should I complete Meta business verification?

Complete Meta business verification to:

* Improve WABA approval chances
* Get higher messaging limits
* Get higher phone number limits
* Display verified business name

See [Meta's business verification guide](https://www.facebook.com/business/help/2058515294227817).

***

## What are the phone number requirements for WhatsApp?

* Must receive OTP via SMS or voice call
* Will be visible to customers on WhatsApp
* One number per WhatsApp registration

### Options

| Option              | Description                              |
| ------------------- | ---------------------------------------- |
| **Rent from Plivo** | Use Plivo phone number (where available) |
| **Bring your own**  | Use existing number                      |
| **Migrate**         | Transfer from another provider           |

***

## How do I migrate a number from another WhatsApp provider?

1. Request migration through Plivo
2. Follow Meta's migration requirements
3. Number transfers to your new WABA

***

## What is the WhatsApp display name?

The business display name appears in:

* Chat thread headers
* Chat lists
* Business profile

### Requirements

* Business must complete Meta verification
* Display name approved by Meta
* Set during embedded signup flow

***

## How do I change my WhatsApp display name?

Contact Plivo support to update your display name after initial setup.

***

## What are the WhatsApp message types?

### Template Messages

**Required to initiate conversations.**

| Template Type      | Use Case                              |
| ------------------ | ------------------------------------- |
| **Authentication** | OTPs, verification codes              |
| **Utility**        | Order updates, shipping notifications |
| **Marketing**      | Promotions, offers, announcements     |

### Session Messages

After customer responds, you have a **24-hour window** to send free-form messages without templates.

***

## What content types are supported in WhatsApp messages?

* Text messages
* Images
* Documents
* Videos
* Audio
* Interactive buttons
* List messages

***

## How do message templates work?

Templates must be approved by Meta before use.

**Status flow:**

1. Submitted → Pending review
2. Approved → Active (Quality pending)
3. Rejected → Edit and resubmit or appeal

***

## How do I create message templates?

Templates are created through Meta's WhatsApp Manager:

1. Access [WhatsApp Manager](https://business.facebook.com/wa/manage/)
2. Navigate to Message Templates
3. Create template with required components
4. Submit for approval

***

## What are the template guidelines?

* Follow Meta's content policies
* Use correct categorization
* Include required variables
* Avoid prohibited content

See [Meta's template guidelines](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/).

***

## How do I view my templates in Plivo?

View your templates in the Plivo console: **Messaging > WhatsApp > Templates**

***

## How do I send WhatsApp messages via API?

Use Plivo's existing Messaging endpoint:

```bash  theme={null}
curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Message/" \
  -u "{auth_id}:{auth_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "src": "whatsapp:+14151234567",
    "dst": "whatsapp:+14157654321",
    "type": "whatsapp",
    "template": {
      "name": "your_template_name",
      "language": "en"
    }
  }'
```

***

## How do I configure webhooks for WhatsApp?

Configure webhooks at WABA level:

1. Navigate to WhatsApp settings
2. Set webhook URL
3. Select events to receive
4. Save configuration

Webhooks apply to all numbers and templates under the WABA.

***

## What SDKs support WhatsApp integration?

Use Plivo's Server SDKs for WhatsApp integration:

* Node.js
* Python
* Ruby
* PHP
* Java
* .NET
* Go

***

## How do I view WhatsApp message logs?

1. Navigate to **Messaging > Logs**
2. Filter by WhatsApp messages
3. View delivery status, pricing, destination

### Log Details

| Field        | Description             |
| ------------ | ----------------------- |
| Message UUID | Unique identifier       |
| Status       | Delivery status         |
| Destination  | Recipient number        |
| Price        | Message cost            |
| Callbacks    | Status updates received |

***

## How do I export WhatsApp logs?

Download logs at:

* Individual message level
* Aggregate by time duration

***

## What if my template is rejected?

Review guidelines, edit and resubmit the template.

***

## What if my message is not delivered?

Check error code and verify the recipient number.

***

## What if my WABA is not approved?

Complete business verification with Meta.

***

## What if number migration fails?

Verify all Meta migration requirements are met.

***

## Where can I find error code descriptions?

Review [Plivo error codes](https://www.plivo.com/docs/messaging/troubleshooting/) for detailed descriptions and next steps.

***

## How do I get support for WhatsApp issues?

1. Note the message UUID
2. Gather relevant details
3. Contact [Plivo Support](https://support.plivo.com)

***

## Related Resources

* [WhatsApp Documentation](https://www.plivo.com/docs/whatsapp/)
* [WhatsApp API Reference](https://www.plivo.com/docs/whatsapp/api/)
* [Meta Business Help](https://www.facebook.com/business/help/)
* [Messaging API Overview](/docs/messaging/messaging-api)
