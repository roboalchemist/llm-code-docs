# Source: https://www.courier.com/docs/external-integrations/other/drift.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Drift

> Use Courier to trigger Drift conversations by providing a recipient email and optionally overriding Drift's API request body and access token configuration.

## Setup

Install the Drift integration from the [Courier integrations catalog](https://app.courier.com/integrations/catalog/drift). You will need your Drift access token.

<Note>
  Drift was acquired by Salesloft. The legacy Drift API documentation at `devdocs.drift.com` may no longer be available. Refer to [Salesloft's documentation](https://developers.salesloft.com/) for current API details.
</Note>

## Profile Requirements

To start a conversation with a recipient over Drift, you must provide the recipient's email as `email` in the profile.

```json  theme={null}
{
  "message": {
    "to": {
      "email": "alice@acme.com"
    }
  }
}
```

## Overrides

You can override the request body, access token, URL, and headers. Below is an example of overriding the body and access token:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "drift": {
        "override": {
          "body": {
            "message": {
              "body": "Custom message body"
            }
          },
          "config": {
            "accessToken": "RUNTIME_ACCESS_TOKEN"
          }
        }
      }
    }
  }
}
```
