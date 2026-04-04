# Source: https://docs.prefect.io/v3/how-to-guides/cloud/create-a-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to create a webhook

> Learn how to setup a webhook in the UI to trigger automations from external events.

This page shows you how to quickly set up a webhook using the Prefect Cloud UI, invoke it, and create an automation based on the received event.

## Trigger an Automation from an External Event

Here's how to set up a webhook and trigger an automation using the Prefect Cloud UI.

### 1. Create a Webhook in the UI

Navigate to the **Webhooks** page in Prefect Cloud and click **Create Webhook**.

You will need to provide a name for your webhook and a Jinja2 template. The template defines how the incoming HTTP request data is transformed into a Prefect event. For example, to capture a model ID and a friendly name from the request body:

```JSON  theme={null}
{
    "event": "model-update",
    "resource": {
        "prefect.resource.id": "product.models.{{ body.model_id}}",
        "prefect.resource.name": "{{ body.friendly_name }}",
        "run_count": "{{body.run_count}}"
    }
}
```

This template will look for `model_id`, `friendly_name`, and `run_count` in the body of the incoming request.

<img src="https://mintcdn.com/prefect-bd373955/rm4-_dTLtkmSX6eG/v3/img/guides/webhook-simple.png?fit=max&auto=format&n=rm4-_dTLtkmSX6eG&q=85&s=40ad34d41e5e706a624c91ed79312ff9" alt="Create a webhook in the Prefect Cloud UI, showing the template editor." width="2450" height="256" data-path="v3/img/guides/webhook-simple.png" />

After saving, Prefect Cloud will provide you with a unique URL for your webhook.

### 2. Invoke the Webhook Endpoint

Use any HTTP client to send a `POST` request to the unique URL provided for your webhook. Include the data you want to pass in the request body. For the example template above:

```console  theme={null}
curl -X POST https://api.prefect.cloud/hooks/YOUR_UNIQUE_WEBHOOK_ID \
  -d "model_id=my_model_123" \
  -d "friendly_name=My Awesome Model" \
  -d "run_count=15"
```

Replace `YOUR_UNIQUE_WEBHOOK_ID` with your actual webhook ID.

### 3. Observe the Event in Prefect Cloud

After invoking the webhook, navigate to the **Event Feed** in Prefect Cloud. You should see a new event corresponding to your webhook invocation.

<img src="https://mintcdn.com/prefect-bd373955/rm4-_dTLtkmSX6eG/v3/img/guides/webhook-created.png?fit=max&auto=format&n=rm4-_dTLtkmSX6eG&q=85&s=1a348eaf056244f5fe2d36a4bfc55417" alt="Event feed in Prefect Cloud showing a newly created event from a webhook." width="740" height="354" data-path="v3/img/guides/webhook-created.png" />

### 4. Create an Automation from the Event

From the event details page (click on the event in the feed), you can click the **Automate** button.

<img src="https://mintcdn.com/prefect-bd373955/rm4-_dTLtkmSX6eG/v3/img/guides/webhook-automate.png?fit=max&auto=format&n=rm4-_dTLtkmSX6eG&q=85&s=2ff4522c881fa28f9ebcbb944e552b12" alt="Event details page with the Automate button highlighted." width="2504" height="292" data-path="v3/img/guides/webhook-automate.png" />

This will pre-fill an automation trigger based on the event you just created.

<img src="https://mintcdn.com/prefect-bd373955/rm4-_dTLtkmSX6eG/v3/img/guides/automation-custom.png?fit=max&auto=format&n=rm4-_dTLtkmSX6eG&q=85&s=b89876f934154273d59cf6778fb55d45" alt="Automation trigger definition pre-filled from a webhook event." width="2506" height="1284" data-path="v3/img/guides/automation-custom.png" />

Click **Next** to define the action(s) this automation should perform, such as running a deployment or sending a notification.

## Troubleshooting Event Reception

If you've invoked your webhook but don't see the expected event in Prefect Cloud, or the event data isn't what you anticipated:

* **Check the Event Feed**: Look for any events related to your webhook, even if they don't match your exact expectations.
* **Look for `prefect-cloud.webhook.failed` events**: If Prefect Cloud encountered an error processing the webhook (e.g., an invalid template or malformed request), it will generate a `prefect-cloud.webhook.failed` event. This event contains details about the received request and any template rendering errors.
* **Verify your request**: Double-check the URL, HTTP method, headers, and body of the request you sent to the webhook.
* **Review your template**: Ensure your Jinja2 template correctly accesses the parts of the HTTP request you intend to use (e.g., `body.field_name`, `headers['Header-Name']`).

For more in-depth troubleshooting of webhook configuration and template rendering, see [Troubleshooting Webhook Configuration in the Concepts documentation](/v3/concepts/webhooks#troubleshooting-webhook-configuration).

## Further reading

For more on webhooks, see the [Webhooks Concepts](/v3/concepts/webhooks) page.


Built with [Mintlify](https://mintlify.com).