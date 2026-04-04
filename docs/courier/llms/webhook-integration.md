# Source: https://www.courier.com/docs/external-integrations/other/webhook-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhook Integration

> Send HTTP requests via Courier's Webhook provider using static or per-recipient dynamic destinations, with support for customizable methods, headers, authentication, and payload overrides.

## Setup

To configure a static webhook destination, specify the Webhook URL and Authorization type in the [webhook integration setup page](https://app.courier.com/integrations/webhook).

## Profile Requirements

To deliver an HTTP request, Courier must be provided with a destination.

### Dynamic Destination

If you need to specify the webhook destination on a per-recipient basis, choose "Dynamic Destination" and pass the information in the recipient profile as `webhook`.

```json  theme={null}
{
  "message": {
    "to": {
      "webhook": {
        "url": "https://www.example.com",
        "method": "POST",
        "headers": {
          "Content-Type": "application/json"
        },
        "authentication": {
          "mode": "basic",
          "username": "AzureDiamond",
          "password": "hunter2"
        },
        "profile": "expanded"
      }
    }
  }
}
```

#### Authentication

The webhooks provider supports basic and bearer authentication. Set `authentication.mode` to `basic` or `bearer` and provide the credentials. Authentication defaults to `none` if not provided.

```json  theme={null}
{
  "mode": "basic",
  "username": "AzureDiamond",
  "password": "hunter2"
}
```

```json  theme={null}
{
  "mode": "bearer",
  "token": "ABCDEFG123456"
}
```

#### Expanded Profile

You can control what profile information is included in the request payload by setting `profile` to either `limited` or `expanded`. The default is `limited`, which only includes profile data provided when the send API was called. Setting `expanded` includes profile data merged from the profile database.

## Request Payload

Based on how the profile is configured, the webhook provider sends the following payload using what was passed into the send method.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "stan.pines@mysteryshack.com",
      "phone_number": "+12025550165"
    },
    "data": {
      "name": "Stan Pines",
      "location": "Gravity Falls, OR"
    }
  }
}
```

## Overrides

You can use a provider override to replace what Courier sends to the destination. The `url`, `method`, `headers`, and `body` fields are all overridable.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "data": {
      "hello": "world"
    },
    "providers": {
      "webhook": {
        "override": {
          "url": "https://www.example.com",
          "method": "PUT",
          "headers": {
            "X-Custom-Header": "Hello from Courier"
          },
          "body": {
            "key": "value"
          }
        }
      }
    }
  }
}
```
