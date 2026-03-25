# Source: https://posthog.com/docs/cdp/destinations/customerio.md

# Send PostHog event data to Customer.io - Docs

You'll also need access to the relevant Customer.io account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=customerio) tab.
3.  Search for 'Customer.io' and click **\+ Create**.
4.  Add your Customer.io site ID and API Key at the configuration step. Note that our integration requires Track API credentials.
5.  Press **Create & Enable** and watch your 'People' list get populated in Customer.io!

## Configuration

| Option | Description |
| --- | --- |
| Customer.io site IDType: stringRequired: True |
| Customer.io API KeyType: stringRequired: True | You can find your API key in your Customer.io account settings ([https://fly.customer.io/settings/api_credentials](https://fly.customer.io/settings/api_credentials)) |
| Customer.io regionType: choiceRequired: True | Use the EU variant if your Customer.io account is based in the EU region |
| Identifier keyType: choiceRequired: True | The kind of identifier to be used. See here for more information: [https://customer.io/docs/api/track/#operation/entity](https://customer.io/docs/api/track/#operation/entity) |
| Identifier valueType: stringRequired: True | The value to be used for the identifier. If the value is empty nothing will be sent. See here for more information: [https://customer.io/docs/api/track/#operation/entity](https://customer.io/docs/api/track/#operation/entity) |
| ActionType: choiceRequired: True | Choose the action to be tracked. Automatic will convert $identify, $pageview and $screen to identify, page and screen automatically - otherwise defaulting to event |
| Include all properties as attributesType: booleanRequired: True | If set, all event properties will be included as attributes. Individual attributes can be overridden below. For identify events the Person properties will be used. |
| Attribute mappingType: dictionaryRequired: False | Map of Customer.io attributes and their values. You can use the filters section to filter out unwanted events. |

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
    "name": "Customer.io",
    "inputs": {
        "site_id": {
            "value": ""
        },
        "token": {
            "value": ""
        },
        "host": {
            "value": "track.customer.io"
        },
        "identifier_key": {
            "value": "email"
        },
        "identifier_value": {
            "value": "{person.properties.email}"
        },
        "action": {
            "value": "automatic"
        },
        "include_all_properties": {
            "value": ""
        },
        "attributes": {
            "value": {
                "email": "{person.properties.email}",
                "lastname": "{person.properties.lastname}",
                "firstname": "{person.properties.firstname}"
            }
        }
    },
    "enabled": true,
    "template_id": "template-customerio"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/customerio/template_customerio.py) is available on GitHub.

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