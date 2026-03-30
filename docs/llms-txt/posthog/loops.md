# Source: https://posthog.com/docs/cdp/destinations/loops.md

# Send PostHog person data to Loops - Docs

You'll also need access to the relevant Loops account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=loops) tab.
3.  Search for **Loops** and click **\+ Create**.
4.  Add your Loops API Key at the configuration step.
5.  Press **Create & Enable** and watch your 'Audience' list get populated in Loops!

## Configuration

| Option | Description |
| --- | --- |
| Loops API KeyType: stringRequired: True | Loops API Key |
| Email of the userType: stringRequired: True | Where to find the email of the user. |
| Include all properties as attributesType: booleanRequired: True | If set, all person properties will be included. Individual attributes can be overridden below. |
| Property mappingType: dictionaryRequired: False | Map of Loops.so properties and their values. You can use the filters section to filter out unwanted events. |

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
    "name": "Loops",
    "inputs": {
        "apiKey": {
            "value": ""
        },
        "email": {
            "value": "{person.properties.email}"
        },
        "include_all_properties": {
            "value": ""
        },
        "properties": {
            "value": {
                "lastName": "{person.properties.lastname}",
                "firstName": "{person.properties.firstname}"
            }
        }
    },
    "enabled": true,
    "template_id": "template-loops"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/loops/template_loops.py) is available on GitHub.

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