# Source: https://www.courier.com/docs/tutorials/ops/how-to-send-webhook-notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Send Webhook Notifications

> Use Courier's webhook integration to deliver notification payloads to any HTTP endpoint, with support for static or dynamic destinations, authentication, and payload overrides.

Courier's webhook integration lets you deliver notification payloads as HTTP requests to any endpoint. This is useful for syncing notification events to internal systems, triggering third-party APIs, or building custom audit trails; all managed through the same routing and template infrastructure you use for email, SMS, and push.

## Prerequisites

* A Courier workspace with an active [API key](https://app.courier.com/settings/api-keys)
* An HTTP endpoint that can receive POST requests (for testing, [webhook.site](https://webhook.site) works well)

## Step 1: Install the webhook integration

Go to [Integrations > Webhook](https://app.courier.com/integrations/webhook) in the Courier dashboard and configure a default destination:

* **Webhook URL**: the endpoint that receives requests (e.g., `https://api.yourapp.com/courier-events`)
* **Authorization**: choose None, Basic, or Bearer and provide credentials if needed

This default destination is used for all webhook sends unless you override it per-recipient (see Step 4).

## Step 2: Create a template with a webhook channel

Open the [Template Designer](https://app.courier.com/designer) and create a new template (or open an existing one). Add a **Webhook** channel to define the content structure Courier sends to your endpoint.

The webhook channel uses the same content blocks as other channels. The rendered content is included in the HTTP request payload that Courier sends to your destination.

## Step 3: Send with a static destination

Send a notification using the template you created. Courier delivers the payload to the default webhook URL you configured in Step 1.

<CodeGroup>
  ```bash curl theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": { "user_id": "user-123" },
        "template": "YOUR_TEMPLATE_ID",
        "data": {
          "order_id": "ORD-456",
          "status": "shipped"
        }
      }
    }'
  ```

  ```javascript Node theme={null}
  import { CourierClient } from "@trycourier/courier";

  const courier = new CourierClient({ authorizationToken: "YOUR_API_KEY" });

  await courier.send({
    message: {
      to: { user_id: "user-123" },
      template: "YOUR_TEMPLATE_ID",
      data: {
        order_id: "ORD-456",
        status: "shipped",
      },
    },
  });
  ```

  ```python Python theme={null}
  from courier.client import Courier

  client = Courier(authorization_token="YOUR_API_KEY")

  client.send(
      message={
          "to": {"user_id": "user-123"},
          "template": "YOUR_TEMPLATE_ID",
          "data": {
              "order_id": "ORD-456",
              "status": "shipped",
          },
      }
  )
  ```
</CodeGroup>

Your endpoint receives a POST request with the rendered template content and the data you passed in.

## Step 4: Send with a dynamic destination

If different recipients need payloads delivered to different endpoints, use a dynamic destination. Pass the webhook configuration in the recipient's profile under the `webhook` key:

```json  theme={null}
{
  "message": {
    "to": {
      "webhook": {
        "url": "https://partner-api.example.com/events",
        "method": "POST",
        "headers": {
          "Content-Type": "application/json"
        },
        "authentication": {
          "mode": "bearer",
          "token": "PARTNER_API_TOKEN"
        }
      }
    },
    "template": "YOUR_TEMPLATE_ID",
    "data": {
      "order_id": "ORD-456"
    }
  }
}
```

Dynamic destinations override the default URL configured in the integration settings. Authentication supports `basic` (username/password) and `bearer` (token) modes.

You can also set `"profile": "expanded"` in the webhook object to include the full merged user profile in the request payload instead of just the data passed at send time.

## Step 5: Customize with overrides

Use provider overrides to change the HTTP method, headers, or body for a specific send without modifying the integration settings or recipient profile:

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user-123" },
    "template": "YOUR_TEMPLATE_ID",
    "data": { "event": "order.completed" },
    "providers": {
      "webhook": {
        "override": {
          "url": "https://hooks.slack.com/services/T00/B00/xxx",
          "method": "POST",
          "headers": {
            "X-Custom-Header": "courier-event"
          },
          "body": {
            "text": "Order completed for user-123"
          }
        }
      }
    }
  }
}
```

When you provide a `body` override, it replaces the entire request payload. Use this when the receiving system expects a specific schema (e.g., Slack incoming webhooks).

<CardGroup cols={2}>
  <Card title="Webhook Integration Reference" href="/external-integrations/other/webhook-integration" icon="webhook">
    Full configuration options for the webhook provider
  </Card>

  <Card title="Outbound Webhooks" href="/platform/workspaces/outbound-webhooks" icon="bell">
    Subscribe to Courier event webhooks for message status changes
  </Card>

  <Card title="Custom Provider" href="/external-integrations/other/custom-provider" icon="puzzle-piece">
    Build a fully custom integration with your own provider logic
  </Card>

  <Card title="Send API" href="/api-reference/send/send-a-message" icon="paper-plane">
    Full Send API reference
  </Card>
</CardGroup>
