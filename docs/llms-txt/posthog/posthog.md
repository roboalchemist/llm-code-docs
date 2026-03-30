# Source: https://posthog.com/docs/data-warehouse/sources/posthog.md

# Source: https://posthog.com/docs/cdp/destinations/posthog.md

# Send PostHog event data to another PostHog instance - Docs

You'll also need access to the destination PostHog account.

## Installation

1.  In PostHog, click the **[Data pipelines](https://app.posthog.com/data-management/destinations)** tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=posthog) tab.
3.  Search for **PostHog** and click **\+ Create**.
4.  Add the Host and API Key of the destination at the configuration step.
5.  Press **Create & Enable** and watch your 'Events' list get populated in the destination PostHog instance!

## Configuration

| Option | Description |
| --- | --- |
| PostHog hostType: stringRequired: True | For cloud accounts this is either [https://us.i.posthog.com](https://us.i.posthog.com) or [https://eu.i.posthog.com](https://eu.i.posthog.com) |
| PostHog API keyType: stringRequired: True |
| Include all properties by defaultType: booleanRequired: True | If set, all event properties will be included in the payload. Individual properties can be overridden below. |
| Property overridesType: dictionaryRequired: False | Provided values will override the event properties. |

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
    "name": "PostHog",
    "inputs": {
        "host": {
            "value": "https://us.i.posthog.com"
        },
        "token": {
            "value": ""
        },
        "include_all_properties": {
            "value": true
        },
        "properties": {
            "value": {}
        }
    },
    "enabled": true,
    "template_id": "template-posthog-replicator"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/posthog/template_posthog.py) is available on GitHub.

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