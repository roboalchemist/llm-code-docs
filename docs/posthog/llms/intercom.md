# Source: https://posthog.com/docs/cdp/destinations/intercom.md

# Send contacts and PostHog events to Intercom - Docs

You'll also need access to the relevant Intercom account.

## Setting up Intercom as a PostHog destination

1.  In PostHog, click the **[Data pipeline](https://app.posthog.com/data-management/destinations)** tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=intercom) tab.
3.  Search for **Intercom** and click the **Create** button for either **Contacts** or **Events**.
4.  In the destination editor, click **Select Intercom connection** to log into your Intercom account.
5.  You can test your destination by sending a test event with **Test function**.
6.  When all is as you like it, click **Create & enable**.

## Configuration details

The Intercom destination requires that contacts **already exist** in Intercom before you can send events associated with them.

You can use the Intercom contact creation destination to ensure those records exist. It is pre-configured to fire on [identify](/docs/product-analytics/identify.md) events, enabling Intercom to capture the same information on each user that PostHog does.

| Option | Description |
| --- | --- |
| Intercom accountType: integrationRequired: True |
| Email of the userType: stringRequired: True | Where to find the email of the user. |
| Include all properties as attributesType: booleanRequired: True | If set, all person properties will be included. Individual attributes can be overridden below. |
| Default property mappingType: dictionaryRequired: False | Map of Intercom properties and their values. |
| Custom property mappingType: dictionaryRequired: False | Map of custom properties and their values. Check out this page for more details: [https://www.intercom.com/help/en/articles/179-create-and-track-custom-data-attributes-cdas](https://www.intercom.com/help/en/articles/179-create-and-track-custom-data-attributes-cdas) |

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
    "name": "Intercom",
    "inputs": {
        "oauth": {
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
                "name": "{f'{person.properties.first_name} {person.properties.last_name}' == ' ' ? null : f'{person.properties.first_name} {person.properties.last_name}'}",
                "phone": "{person.properties.phone}",
                "last_seen_at": "{toUnixTimestamp(event.timestamp)}"
            }
        },
        "customProperties": {
            "value": {}
        }
    },
    "enabled": true,
    "template_id": "template-intercom"
}'
```

## FAQ

### Can I send session replays to Intercom?

Yes, you can add a link to the session replay in Intercom by setting the `integrations` config option when initializing PostHog's Web SDK to `{ intercom: true }`. See [our tutorial on adding session replays to Intercom](/tutorials/intercom-session-replays.md) for more details.

### Can I add PostHog person profile data to Intercom?

Yes, you can add a link to the PostHog person profile in Intercom by setting the `integrations` config option when initializing PostHog's Web SDK to `{ intercom: true }`. See [our tutorial on adding session replays to Intercom](/tutorials/intercom-session-replays.md) for more details.

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/intercom/template_intercom.py) is available on GitHub.

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