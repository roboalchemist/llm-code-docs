# Source: https://www.courier.com/docs/external-integrations/push/nowpush.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# NowPush

> Send cross-platform messages via NowPush by configuring optional fields like device_type, message_type, url, and apiKey directly in your Courier notification template.

## Setup

You will need a [NowPush](https://nowpush.io/) account. In Courier, navigate to the [NowPush Integration](https://app.courier.com/integrations/catalog/nowpush) page, enter your API key, then click "Save."

## Profile Requirements

No profile data is required for NowPush. If `device_type`, `message_type`, `url` or `apiKey` are included in your notification template it will replace the configuration.

```json  theme={null}
{
  "message": {
    "to": {
      "nowpush": {
        "device_type": "browser",
        "message_type": "link",
        "url": "www.nowpush.com",
        "apiKey": ""
      }
    }
  }
}
```

## Overrides

### Body Overrides

Overrides can be used to change the request body that Courier sends to NowPush's API.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {},
    "providers": {
      "nowpush": {
        "override": {
          "body": {
            "device_type": "browser",
            "message_type": "nowpush_msg"
          }
        }
      }
    }
  }
}
```

### Config Overrides

You can swap the API key or URL at send time using a config override:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {},
    "providers": {
      "nowpush": {
        "override": {
          "config": {
            "apiKey": "RUNTIME_API_KEY"
          }
        }
      }
    }
  }
}
```
