# Source: https://www.courier.com/docs/external-integrations/email/mailersend.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MailerSend

> Send emails via MailerSend using Courier by verifying your domain, providing the recipient's email, and optionally overriding fields like API key, sender address, or subject.

## Setup

You will need a [MailerSend](https://www.mailersend.com/) account with a verified sending domain.

<Steps>
  <Step title="Verify Your Domain">
    In MailerSend, add your domain and complete DNS verification.

    <Frame>
      <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/channels/mailersend-domains.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=9b31eb79ef7c1d6635317f0398df4d27" width="1244" height="390" data-path="assets/platform/channels/mailersend-domains.png" />
    </Frame>
  </Step>

  <Step title="Generate an API Token">
    Click "Manage" on your domain and generate an API token.

    <Frame>
      <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/channels/mailersend-api-tokens.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=045cf6dd3effa904a261e72446f2e13d" width="1242" height="270" data-path="assets/platform/channels/mailersend-api-tokens.png" />
    </Frame>
  </Step>

  <Step title="Configure in Courier">
    In Courier, navigate to the [MailerSend Integration](https://app.courier.com/integrations/catalog/mailersend) page. Enter your API token and From Address, then click "Save."
  </Step>
</Steps>

## Profile Requirements

To deliver a message to a recipient over MailerSend, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

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

You can override any of the fields supported by MailerSend's [/v1/email endpoint](https://developers.mailersend.com/api/v1/email.html#send-an-email). Overrides are useful when a field is not yet supported by Courier or you want to replace a value that Courier generates.

**Config override example:**

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "mailersend": {
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
      "mailersend": {
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

## Troubleshooting

<Accordion title="MailerSend 422 Response Code">
  A [422 error](https://www.mailersend.com/help/how-to-start-sending-emails#rest-api) from MailerSend can have several causes:

  | Error                                 | Cause                                                                                                                    |
  | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
  | From email must be verified           | The domain of the from email address must match the domain that the API token is from.                                   |
  | Must provide HTML/text or template ID | The API request is missing content; provide either an HTML/text body or a template ID.                                   |
  | File type not supported               | The attachment is not a [supported file type](https://developers.mailersend.com/api/v1/email.html#supported-file-types). |
  | Reply-to must be a valid email        | The `reply_to` parameter is not a valid email address.                                                                   |
  | Email quota reached                   | The account's quota has been reached. Ensure your account is approved for production sending.                            |

  The most common cause is an unverified sending domain. Make sure your domain is [verified with MailerSend](https://www.mailersend.com/help/how-to-verify-and-authenticate-a-sending-domain) before using it with Courier.
</Accordion>
