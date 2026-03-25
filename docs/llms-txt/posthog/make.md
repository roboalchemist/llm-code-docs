# Source: https://posthog.com/docs/cdp/destinations/make.md

# Send PostHog event data to Make - Docs

Trigger scenarios in Make based on PostHog events.

## Requirements

You'll also need access to the relevant Make account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=make) tab.
3.  Search for **Make** and click **\+ Create**.
4.  Add your Make webhook URL at the configuration step.
5.  Set up your event and property filters to remove unnecessary events. You only want to send events that you want to trigger scenarios. Filter out unrelated events or ones missing required data.
6.  Press **Create & Enable** and watch your **scenarios** get triggered in Make!

## Configuration

| Option | Description |
| --- | --- |
| Webhook URLType: stringRequired: True | See this page on how to generate a Webhook URL: [https://www.make.com/en/help/tools/webhooks](https://www.make.com/en/help/tools/webhooks) |
| JSON BodyType: jsonRequired: True |

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
    "name": "Make",
    "inputs": {
        "webhookUrl": {
            "value": ""
        },
        "body": {
            "value": {
                "data": {
                    "event": "{event.event}",
                    "person": {
                        "uuid": "{person.id}",
                        "properties": "{person.properties}"
                    },
                    "teamId": "{project.id}",
                    "eventUuid": "{event.uuid}",
                    "timestamp": "{event.timestamp}",
                    "distinctId": "{event.distinct_id}",
                    "properties": "{event.properties}",
                    "elementsChain": "{event.elementsChain}"
                }
            }
        }
    },
    "enabled": true,
    "template_id": "template-make"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/make/template_make.py) is available on GitHub.

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