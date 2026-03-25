# Source: https://posthog.com/docs/cdp/destinations/microsoft-teams.md

# Send PostHog analytics events to your Microsoft Teams server - Docs

Send event data from PostHog into the Microsoft Teams server and channel of your choice.

## Setup

### Microsoft Teams: create a webhook

1.  In Microsoft Teams, go to the channel you want to send events to.
2.  Click the three dots next to the channel name and select **Workflows**.
3.  Select the **Post to a channel when a webhook request is received**, in the templates section.
4.  Click **Next**, then **Add workflow**.
5.  Copy the webhook URL.

> **Note:** The Microsoft Teams destination supports webhook URLs from:
>
> -   Azure Logic Apps (`logic.azure.com`)
> -   Power Platform (`webhook.office.com`)
> -   Power Automate (`powerautomate.com` or `flow.microsoft.com`)

### PostHog: create a destination

1.  Back in PostHog, click the **[Data pipelines](https://app.posthog.com/data-management/destinations)** tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=microsoft) tab.
3.  Search for **Microsoft Teams** and click **\+ Create**.
4.  Add your Webhook URL.
5.  Use the **Text** field to format your message. You can include any properties that exist on `event` or `person`.
6.  Use the **Filters** panel to set up a query to filter the events you want to send, otherwise you'll get a firehose of all events filling your channel.
7.  Press **Create & enable**. Events will now be sent to Microsoft Teams. If you'd like to send a test event to your channel, hit the **Start testing** button.

> **Note:** For advanced customization, you can click the **Edit source** button to modify the destination's code directly. This allows you to tailor the destination to your specific needs beyond the standard configuration options. See our guide on [customizing destinations](/docs/cdp/destinations/customizing-destinations.md) for more details.

## Configuration

| Option | Description |
| --- | --- |
| Webhook URLType: stringRequired: True | You can use any of these options: Azure Logic Apps (logic.azure.com), Power Platform webhooks (create through Microsoft Teams by adding an incoming webhook connector to your channel), Power Automate (powerautomate.com or flow.microsoft.com), or Power Platform environment endpoints (environment.api.powerplatform.com) |
| TextType: stringRequired: True | (see [https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet#example](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet#example)) |

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
    "name": "Microsoft Teams",
    "inputs": {
        "webhookUrl": {
            "value": ""
        },
        "text": {
            "value": "**{person.name}** triggered event: '{event.event}'"
        }
    },
    "enabled": true,
    "template_id": "template-microsoft-teams"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/microsoft_teams/template_microsoft_teams.py) is available on GitHub.

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