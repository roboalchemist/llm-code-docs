# Source: https://www.courier.com/docs/external-integrations/email/resend.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Resend

> Send email notifications via Courier using Resend by setting up an API key, configuring sender details, and using overrides for advanced customization.

## Setup

You will need both a [Courier](https://app.courier.com/signup) and a [Resend](https://resend.com/signup) account.

<Steps>
  <Step title="Create a Resend API Key">
    In Resend, navigate to [API Keys](https://resend.com/api-keys). Create an API key with appropriate permissions and copy it.
  </Step>

  <Step title="Configure in Courier">
    In Courier, navigate to the [Resend Integration](https://app.courier.com/integrations/catalog/resend) page. Paste your API key into the "API Key" field.
  </Step>

  <Step title="Set From Address">
    Add a verified email address to the "From Address" field (e.g., `noreply@yourdomain.com`). Click "Add Integration" then "Save."
  </Step>
</Steps>

## Profile Requirements

To deliver a message to a recipient over Resend, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

```json  theme={null}
{
  "message": {
    "to": {
      "email": "alice@acme.com"
    }
    // ... rest of message definition
  }
}
```

## Overrides

You can use a provider override to customize what Courier sends to Resend's [/emails endpoint](https://resend.com/docs/api-reference/emails/send-email). Overrides are useful when a field is not yet supported by Courier or you want to replace a value that Courier generates.

For example, you can use Resend's tagging feature:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "resend": {
        "override": {
          "body": {
            "tags": [{ "name": "environment", "value": "development" }]
          }
        }
      }
    }
  }
}
```

Everything inside `message.providers.resend.override.body` is merged with Courier's generated request body. You can also override config values:

```json  theme={null}
{
  "message": {
    "providers": {
      "resend": {
        "override": {
          "config": {
            "apiKey": "<your override API key>",
            "fromAddress": "alternate-sender@yourdomain.com"
          }
        }
      }
    }
  }
}
```

### Attachments

To include an attachment, add an `attachments` array in the override. File content must be base64-encoded.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "resend": {
        "override": {
          "attachments": [
            {
              "filename": "billing.pdf",
              "contentType": "application/pdf",
              "data": "Q29uZ3JhdHVsYXRpb25zLCB5b3UgY2FuIGJhc2U2NCBkZWNvZGUh"
            }
          ]
        }
      }
    }
  }
}
```
