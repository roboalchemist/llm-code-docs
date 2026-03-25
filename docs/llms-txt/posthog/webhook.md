# Source: https://posthog.com/docs/cdp/destinations/webhook.md

# Send PostHog event data using webhooks - Docs

With webhook destinations, you can send event data from PostHog to any HTTP endpoint, whether it's to your own backend, an internal system, or a third-party platform.

Want to send PostHog data to a particular platform like Slack?

Browse all the **Destinations** listed in the sidenav to integrate with well-known platforms like [Slack](/docs/cdp/destinations/slack.md), [HubSpot](/docs/cdp/destinations/hubspot.md), or [Zapier](/docs/cdp/destinations/zapier.md).

Want to bring your data into PostHog?

Check out [Sources](/docs/cdp/sources.md) to learn how to connect your systems like CRM, payment processor, or database with PostHog data for all-in-one analytics.

## Setting up destination webhooks

### 1\. Create a new destination

In PostHog, navigate to the [data pipelines](https://app.posthog.com/data-management/destinations) section in the sidebar. Click **\+ New** > **Destination** in the top-right corner. Search for "Webhook" then click **\+ Create**.

![Create new destination](https://res.cloudinary.com/dmukukwp6/image/upload/webhook_destination_cd495788fc.png)

### 2\. Configure the webhook

On the configuration page, enter a **Webhook URL**. This is the HTTP endpoint that will receive the event data from PostHog. By default, PostHog sends a `POST` request with a templated JSON body.

Click **Create & Enable**.

![Configure webhook](https://res.cloudinary.com/dmukukwp6/image/upload/webhook_url_config_5900a5a9b7.png)

**Webhook services**

You can use services like [webhook.site](https://webhook.site/) or [ngrok](https://ngrok.com/) to create **Webhook URLs** for quick testing.

### 3\. Test the webhook

Now that the webhook is enabled, let's see it in action. In the **Testing** section of the configuration page, click **Start testing** > **Test function** to send an example event.

You should see the webhook endpoint receive a `POST` request with event data.

**Debugging**

Try enabling **Log responses** to help debug HTTP calls.

### 4\. Customize the webhook (optional)

You can further configure and customize webhook destinations by:

-   Adding filters, match rules, and trigger options in the **Filters** section
-   Customizing the [payload](/docs/cdp/destinations/customizing-destinations.md#customizing-payload)
-   Using [global variables](/docs/cdp/destinations/customizing-destinations.md#global-object)
-   Modifying the [source code](/docs/cdp/destinations/customizing-destinations.md#modifying-destinations-with-hog) in the **Edit source** section

## Configuration

| Option | Description |
| --- | --- |
| Webhook URLType: stringRequired: True | Endpoint URL to send event data to. |
| MethodType: choiceRequired: False | HTTP method to use for the request. |
| JSON BodyType: jsonRequired: False | JSON payload to send in the request body. |
| HeadersType: dictionaryRequired: False | HTTP headers to send in the request. |
| Log responsesType: booleanRequired: False | Logs the response of http calls for debugging. |

How to create this via the API

Using our REST API you can create this destination like so:

Terminal

PostHog AI

```bash
# Create a new destination
curl --location 'https://us.i.posthog.com/api/environments/:project_id/hog_functions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <POSTHOG_PERSONAL_API_KEY>' \
--data '{
    "type": "destination",
    "name": "HTTP Webhook",
    "inputs": {
        "url": {
            "value": ""
        },
        "method": {
            "value": "POST"
        },
        "body": {
            "value": {
                "event": "{event}",
                "person": "{person}"
            }
        },
        "headers": {
            "value": {
                "Content-Type": "application/json"
            }
        }
    },
    "enabled": true,
    "template_id": "template-webhook"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/webhook/template_webhook.py) is available on GitHub.

### Who maintains this?

This is maintained by PostHog. If you have issues with it not functioning as intended, please [let us know](https://us.posthog.com/#panel=support%3Asupport%3Aapps%3A%3Atrue)!

### What if I have feedback on this destination?

We love feature requests and feedback. Please [tell us what you think](https://us.posthog.com/#panel=support%3Afeedback%3Aapps%3Alow%3Atrue).

### What if my question isn't answered above?

We love answering questions. Ask us anything via [our community forum](/questions.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better