# Source: https://www.courier.com/docs/platform/content/brands/email-domain-white-labeling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# White-Labeling Email Domains

> Send emails from your customer's domain by overriding email provider API keys and configuring sender addresses for a fully white-labeled email experience.

White-labeling lets you send emails that appear to come from your customer's domain. This involves two parts:

1. Using your customer's email service provider
2. Sending from your customer's email domain

## Prerequisites

* An email provider integration configured in your Courier workspace (e.g., Mailgun, SendGrid, Postmark)
* Your customer's email provider API key
* Your customer's verified sender domain on their provider

## Set Up Email Service Provider Integrations

1. Add an integration in your Courier workspace for each email provider you want to support
2. Add those integrations to the email channel of the notification template you want to white-label

<Note>
  The initial API keys for these integrations don't need to be valid if you always override them via the Send API.
</Note>

## Configure Provider Selection

Use provider-level conditions to determine which provider to use. For example, pass a `provider` field in your data object and set a condition that enables a specific provider only when that value matches.

## Override the API Key

When sending an email, provide your customer's API key using the `providers` override:

```json  theme={null}
{
  "message": {
    "to": {
      "email": "recipient@example.com"
    },
    "template": "white-label-welcome",
    "data": {
      "customer_name": "Acme Corp"
    },
    "providers": {
      "mailgun": {
        "override": {
          "config": {
            "apiKey": "CUSTOMER_MAILGUN_API_KEY"
          }
        }
      }
    }
  }
}
```

## Set the 'From' Email Address

To send from your customer's email address:

1. Use a variable in the email channel settings for the From field (e.g., `{customer_from_email}`)
2. Pass that variable in the `data` object when sending

For more details, see [Customizing Email Address Fields](/platform/content/template-settings/email-fields).

<CardGroup cols={2}>
  <Card title="Email Address Fields" href="/platform/content/template-settings/email-fields" icon="envelope">
    Customize From, Reply-To, CC, and BCC per notification
  </Card>

  <Card title="Brands Overview" href="/platform/content/brands/brands-overview" icon="palette">
    Configure visual branding for white-labeled notifications
  </Card>
</CardGroup>
