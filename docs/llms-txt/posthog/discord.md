# Source: https://posthog.com/docs/cdp/destinations/discord.md

# Send PostHog analytics events to your Discord server - Docs

Send event data from PostHog into the Discord server and channel of your choice.

## Setup

### Discord: create a webhook

1.  In Discord, go to the server you want to send events to.
2.  Click the server name in the top left and select **Server Settings**.
3.  Select **Integrations**, in the Apps section.
4.  Select **Webhooks**, then **New Webhook**.
5.  Give the webhook a name and pick the channel you want to send events to.
6.  Copy the webhook URL.

### PostHog: create a destination

1.  Back in PostHog, click the **[Data pipelines](https://app.posthog.com/data-management/destinations)** tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=discord) tab.
3.  Search for **Discord** and click **\+ Create**.
4.  Add your Webhook URL.
5.  Use the **Content** field to format your message. You can include any properties that exist on `event` or `person`.
6.  Use the **Filters** panel to set up a query to filter the events you want to send, otherwise you'll get a firehose of all events filling your channel.
7.  Press **Create & enable**. Events will now be sent to Discord. If you'd like to send a test event to your channel, hit the **Start testing** button.

## Configuration

| Option | Description |
| --- | --- |
| Webhook URLType: stringRequired: True | See this page on how to generate a Webhook URL: [https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) |
| ContentType: stringRequired: True | (see [https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline](https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline)) |

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
    "name": "Discord",
    "inputs": {
        "webhookUrl": {
            "value": ""
        },
        "content": {
            "value": "**{person.name}** triggered event: '{event.event}'"
        }
    },
    "enabled": true,
    "template_id": "template-discord"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/discord/template_discord.py) is available on GitHub.

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