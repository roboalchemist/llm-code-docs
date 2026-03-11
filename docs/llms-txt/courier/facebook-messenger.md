# Source: https://www.courier.com/docs/external-integrations/direct-message/facebook-messenger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Facebook Messenger

> Send notifications via Facebook Messenger by including the recipient's Page-Scoped ID (facebookPSID) in their profile, with support for body and config overrides.

## Setup

You will need a [Facebook Page](https://www.facebook.com/pages/create) with Messenger enabled and a Facebook App with the Messenger platform configured. In Courier, navigate to the [Facebook Messenger Integration](https://app.courier.com/integrations/catalog/facebook-messenger) page, enter your Page Access Token, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Facebook Messenger, Courier must be provided the recipient's Page-Scoped ID (PSID). The value should be included in the recipient profile as `facebookPSID`.

```json  theme={null}
{
  "message": {
    "to": {
      "facebookPSID": "1254477777772919"
    }
  }
}
```

## Overrides

### Body Overrides

You can override any of the fields in the request body that Courier sends to the Messenger [Send API](https://developers.facebook.com/docs/messenger-platform/reference/send-api/).

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "facebookPSID": "1254477777772919"
    },
    "providers": {
      "facebook-messenger": {
        "override": {
          "body": {
            "messaging_type": "UPDATE"
          }
        }
      }
    }
  }
}
```

### Config Overrides

You can swap the Page Access Token or API URL at send time:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "facebookPSID": "1254477777772919"
    },
    "providers": {
      "facebook-messenger": {
        "override": {
          "config": {
            "access_token": "RUNTIME_PAGE_ACCESS_TOKEN"
          }
        }
      }
    }
  }
}
```
