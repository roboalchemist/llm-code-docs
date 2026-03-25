# Source: https://posthog.com/docs/cdp/destinations/google-pubsub.md

# Send PostHog event data to Google Pub/Sub - Docs

You'll also need access to the relevant Google Cloud account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=googlepubsub) tab.
3.  Search for **Google Pub/Sub** and click **\+ Create**.
4.  Connect your Google Cloud account at the configuration step.
5.  Press **Create & Enable** and watch your 'topic' list get populated in Google Pub/Sub!

## Configuration

| Option | Description |
| --- | --- |
| Google Cloud service accountType: integrationRequired: True |
| Topic nameType: stringRequired: True |
| Message PayloadType: jsonRequired: False |
| AttributesType: jsonRequired: False |

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
    "name": "Google Pub/Sub",
    "inputs": {
        "auth": {
            "value": ""
        },
        "topicId": {
            "value": ""
        },
        "payload": {
            "value": {
                "event": "{event}",
                "person": "{person}"
            }
        },
        "attributes": {
            "value": {}
        }
    },
    "enabled": true,
    "template_id": "template-google-pubsub"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/google_pubsub/template_google_pubsub.py) is available on GitHub.

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