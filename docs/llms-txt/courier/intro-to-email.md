# Source: https://www.courier.com/docs/external-integrations/email/intro-to-email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Providers

> Learn how to integrate Courier with email providers and use channel-level overrides to customize subjects, content, branding, and tracking in email notifications.

Courier integrates with a wide range of email providers. To send an email, the recipient profile must include an `email` field:

```json  theme={null}
{
  "message": {
    "to": {
      "email": "alice@acme.com"
    },
    "template": "NOTIFICATION_TEMPLATE_ID"
  }
}
```

When a notification template includes an email channel, Courier selects the configured email provider based on your [channel priority](/platform/sending/channel-priority) and routing rules. If the primary provider fails, Courier automatically [fails over](/platform/sending/failover) to backup providers when configured.

## Available Email Providers

| Provider                                                        | Description                                                |
| --------------------------------------------------------------- | ---------------------------------------------------------- |
| [Amazon SES](/external-integrations/email/aws-ses)              | AWS-hosted sending with IAM role or access key auth        |
| [SendGrid](/external-integrations/email/sendgrid)               | Twilio SendGrid with template import and delivery tracking |
| [Postmark](/external-integrations/email/postmark)               | Transactional email with MessageStream support             |
| [Mailgun](/external-integrations/email/mailgun)                 | Email delivery with webhooks and EU region support         |
| [Resend](/external-integrations/email/resend)                   | Modern email API with tagging and attachments              |
| [SMTP](/external-integrations/email/smtp)                       | Generic SMTP relay via NodeMailer                          |
| [Mandrill](/external-integrations/email/mandrill)               | Mailchimp Transactional with template import               |
| [SparkPost](/external-integrations/email/sparkpost)             | High-volume email delivery                                 |
| [Mailjet](/external-integrations/email/mailjet)                 | Transactional and marketing email                          |
| [MailerSend](/external-integrations/email/mailersend)           | Domain-verified transactional email                        |
| [Amply](/external-integrations/email/amply)                     | Email delivery with attachment support                     |
| [Gmail](/external-integrations/email/gmail)                     | OAuth-based sending for testing and small-scale use        |
| [OneSignal Email](/external-integrations/email/onesignal-email) | Email via OneSignal's notification platform                |

## Email Channel Overrides

Overrides let you modify parts of an email at send time without changing your notification template. They are passed in the `message` payload of a [Send request](/api-reference/send/message) and applied just before Courier hands the message off to the provider.

There are two levels of override:

* **Channel overrides** (`message.channels.email.override`) apply to every email provider configured on the template. Use these when you want to change the subject, from address, HTML body, or add attachments regardless of which provider sends the email.
* **Provider overrides** (`message.providers.<key>.override`) target a single provider and can pass through fields specific to that provider's API. Each provider page documents its supported override schema.

Channel overrides and provider overrides can be used together. If both set the same field, the provider override takes precedence.

<Note>
  Overrides are applied **after** the render step in the notification lifecycle. This means the Rendered tab in the Courier logs **will not reflect** overrides; it shows the pre-override output. To verify the final payload, check the provider request in the Raw tab.
</Note>

### Data structure for the email channel override:

<Note>
  BCC fields need to be introduced as strings. For multiple bcc recipients, addresses need to be in comma-separated strings. Courier will transform them to arrays required by some providers.
</Note>

```json  theme={null}
{
  "message": {
    // ...rest of request
    "channels": {
      "email": {
        "override": {
          "attachments": [],
          "bcc": "", // "alice@acme.com,bob@acme.com" or "Alice <alice@acme.com>,Bob <bob@acme.com>"
          "brand": {},
          "cc": "",
          "from": "",
          "html": "",
          "reply_to": "",
          "subject": "",
          "text": "",
          "tracking": {
            "open": false
          }
        }
      }
    }
  }
}
```

## Brand Override

The `channels.email.override.brand` property uses same schema as the API request payload for the [POST /brands](/api-reference/brands/create-a-new-brand) endpoint.

Brand elements that can be overridden:

* logo
* top bar color
* brand colors

**Example:**

```json  theme={null}
{
  "message": {
    // ...rest of request
    "channels": {
      "email": {
        "override": {
          "brand": {
            "settings": {
              "email": {
                "header": {
                  "logo": {
                    "image": "https://www.courier.com/logo.png",
                    "href": "https://www.courier.com"
                  },
                  "barColor": "#674ea7"
                }
              }
            }
          }
        }
      }
    }
  }
}
```

## Allowlist for AWS IP Addresses

Some email providers, such as Mailgun, offer [additional security](https://help.mailgun.com/hc/en-us/articles/360012244474-IP-Allowlist) to allowlist IP addresses to access their API. Courier is hosted on AWS and does not provide an IP range in the form of an allowlist.

As a workaround, users can subscribe to the `AmazonIpSpaceChanged` topic, and receive notifications about any changes to the AWS IP address ranges. For details, refer to the [AWS documentation](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html#subscribe-notifications).
