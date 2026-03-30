# Source: https://posthog.com/docs/cdp/destinations/gleap.md

# Send PostHog person data to Gleap - Docs

You'll also need access to the relevant Gleap account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=gleap) tab.
3.  Search for **Gleap** and click **\+ Create**.
4.  Add your Gleap access token at the configuration step.
5.  Press **Create & Enable** and watch your 'Contacts' list get populated in Gleap!

## Configuration

| Option | Description |
| --- | --- |
| Gleap.io API KeyType: stringRequired: True |
| User IDType: stringRequired: True | You can choose to fill this from an email property or an id property. If the value is empty nothing will be sent. See here for more information: [https://docs.gleap.io/server/rest-api](https://docs.gleap.io/server/rest-api) |
| Include all properties as attributesType: booleanRequired: True | If set, all person properties will be included as attributes. Individual attributes can be overridden below. |
| Attribute mappingType: dictionaryRequired: False | Map of Gleap.io attributes and their values. You can use the filters section to filter out unwanted events. |

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
    "name": "Gleap",
    "inputs": {
        "apiKey": {
            "value": ""
        },
        "userId": {
            "value": "{person.id}"
        },
        "include_all_properties": {
            "value": ""
        },
        "attributes": {
            "value": {
                "name": "{person.properties.name}",
                "email": "{person.properties.email}",
                "phone": "{person.properties.phone}"
            }
        }
    },
    "enabled": true,
    "template_id": "template-gleap"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/gleap/template_gleap.py) is available on GitHub.

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