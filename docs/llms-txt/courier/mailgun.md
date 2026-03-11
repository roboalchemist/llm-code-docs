# Source: https://www.courier.com/docs/external-integrations/email/mailgun.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mailgun

> Send emails with Mailgun via Courier. Covers profile setup, overrides, attachments, EU host config, delivery webhooks, and error handling.

## Setup

You will need a [Mailgun](https://www.mailgun.com/) account with a verified sending domain. In Mailgun, navigate to your domain settings to get your API key and domain name. In Courier, navigate to the [Mailgun Integration](https://app.courier.com/integrations/catalog/mailgun) page, enter your API key, domain, and From Address, then click "Save."

<Info>
  For EU-region Mailgun accounts, set the host to `api.eu.mailgun.net` in the integration settings or via a config override.
</Info>

## Profile Requirements

Courier uses the `email` key in the recipient profile to send messages through Mailgun.

```json  theme={null}
{
  "message": {
    "to": {
      "email": "user@example.com"
    },
    // …other message properties
  }
}
```

## Overrides

Use the `override` object to customize the payload sent to Mailgun’s Messages API. Example: add a Mailgun tag.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "user@example.com"
    },
    "providers": {
      "mailgun": {
        "override": {
          "body": {
            "o:tag": "notifications"
          },
          "config": {
            "apiKey": "<your API Key>",
            "domain": "<domain>",
            "host": "<host>"
          }
        }
      }
    }
  }
}
```

Courier replaces the full request body with the contents of `override`.

To customize the `fromAddress` or other Mailgun config options, set them under `override.config`.

Refer to the [Mailgun API docs](https://documentation.mailgun.com/en/latest/api-sending.html) for supported parameters.

<Info title="EU Host">
  To send through Mailgun’s EU region, set the `host` value to `api.eu.mailgun.net`.

  ```json  theme={null}
  "config": {
    "apiKey": "<your API Key>",
    "domain": "<domain>",
    "host": "api.eu.mailgun.net"
  }
  ```
</Info>

## Attachments

To include attachments, add an `attachments` array in the override. File content must be base64-encoded.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "user@example.com"
    },
    "data": {
      "hello": "world"
    },
    "providers": {
      "mailgun": {
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

## IP Allowlisting

Mailgun supports IP allowlists for API access. Courier runs on AWS and doesn’t use fixed outbound IPs.

To manage this, AWS provides a workaround:\
Subscribe to the [`AmazonIpSpaceChanged`](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html#subscribe-notifications) SNS topic. You’ll get notified whenever AWS updates its IP ranges, so you can update your allowlist accordingly.

## Delivery Tracking

Courier polls Mailgun for status by default. To get real-time delivery updates, set up Mailgun webhooks.

<Steps>
  <Step title="Copy the Courier Webhook URL">
    In Courier, go to the [Mailgun configuration page](https://app.courier.com/integrations/catalog/mailgun). Copy the generated Webhook URL.

    <Frame>
      <img src="https://mintcdn.com/courier-4f1f25dc/Okgc82MLlENV5nIi/assets/external-integrations/email/mailgun-webhook.png?fit=max&auto=format&n=Okgc82MLlENV5nIi&q=85&s=30796628d89c650cf9baad434f8f90c5" width="1322" height="1466" data-path="assets/external-integrations/email/mailgun-webhook.png" />
    </Frame>
  </Step>

  <Step title="Configure Webhooks in Mailgun">
    In Mailgun, navigate to **Sending → Webhooks**.\
    Add a webhook for **Delivered Messages**, and paste the URL.\
    Repeat for **Permanent Failure**.

    <Frame>
      <img src="https://mintcdn.com/courier-4f1f25dc/gOrhLCtuaRi0MQwP/assets/external-integrations/email/mailgun-ui.png?fit=max&auto=format&n=gOrhLCtuaRi0MQwP&q=85&s=d6121029a6cb6102b51018d6dc38bc74" width="2131" height="670" data-path="assets/external-integrations/email/mailgun-ui.png" />
    </Frame>

    <Frame>
      <img src="https://mintcdn.com/courier-4f1f25dc/gOrhLCtuaRi0MQwP/assets/external-integrations/email/mailgun-form.png?fit=max&auto=format&n=gOrhLCtuaRi0MQwP&q=85&s=3a08c5f5583ae312233a7e96b4214e12" width="1200" height="782" data-path="assets/external-integrations/email/mailgun-form.png" />
    </Frame>
  </Step>

  <Step title="Match the Domain">
    In Mailgun, ensure the selected domain matches the one configured in Courier.
  </Step>

  <Step title="Disable Polling (optional)">
    After \~1 hour (to allow in-flight updates), disable polling in Courier under **Enable polling for status updates**, then click **Save**.
  </Step>
</Steps>

## Troubleshooting

<Accordion title="550 Error – Missing MX Record">
  <Warning>
    Mailgun returns a 550 error when the sending domain doesn’t have an MX record.
  </Warning>

  **Fix:**\
  Add an MX record to your domain’s DNS. Wait \~2 hours for propagation.
</Accordion>

<Accordion title="Account Throttling or Probation">
  <Warning>
    Mailgun may throttle or suspend delivery for accounts with high bounce/spam rates or traffic spikes.
  </Warning>

  **Fix:**

  1. Complete Mailgun’s Business Verification.
  2. Remove addresses that bounce consistently. Avoid bulk sends to unverified users.
</Accordion>
