# Source: https://posthog.com/docs/cdp/destinations/braze.md

# Send PostHog event data to Braze - Docs

You'll also need access to the relevant Braze account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=braze) tab.
3.  Search for 'Braze' and click **\+ Create**.
4.  Add your Braze API Key at the configuration step.
5.  Press **Create & Enable** and watch your 'Users' list get populated in Braze!

## Configuration

| Option | Description |
| --- | --- |
| Braze REST EndpointType: choiceRequired: True | The endpoint identifier where your Braze instance is located, see the docs here: [https://www.braze.com/docs/api/basics](https://www.braze.com/docs/api/basics) |
| Your Braze API KeyType: stringRequired: True | See the docs here: [https://www.braze.com/docs/api/api_key/](https://www.braze.com/docs/api/api_key/) |
| Attributes to setType: jsonRequired: True |
| Event payloadType: jsonRequired: True |

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
    "name": "Braze",
    "inputs": {
        "brazeEndpoint": {
            "value": ""
        },
        "apiKey": {
            "value": ""
        },
        "attributes": {
            "value": {
                "email": "{person.properties.email}"
            }
        },
        "event": {
            "value": {
                "name": "{event.event}",
                "time": "{event.timestamp}",
                "properties": "{event.properties}",
                "external_id": "{event.distinct_id}"
            }
        }
    },
    "enabled": true,
    "template_id": "template-braze"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/braze/template_braze.py) is available on GitHub.

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