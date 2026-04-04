# Source: https://posthog.com/docs/cdp/destinations/brevo.md

# Create and update Brevo contacts from analytics events - Docs

You can use your PostHog event data to create and update contacts in Brevo. Here's everything you need to get started.

## Configuring Brevo

First, [create](https://app.brevo.com/settings/keys/api) a new **API key** in Brevo and copy it for the next step.

## Configuring PostHog’s Brevo destination

1.  In PostHog, click the **[Data pipeline](https://app.posthog.com/data-management/destinations)** tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=brevo) tab.
3.  Click **New destination** and choose Brevo's **Create** button.

Paste your API key and then add any other values you want to pipe from PostHog person properties into Brevo, using the **attributes** fields.

### Filtering

At a minimum, you should filter to only send events that have an email property set, as Brevo will use this to identify contacts.

### Testing

Once you’ve configured your Brevo destination, click **Start testing** to verify everything works the way you want. Clicking **Test function** will send a test event to Brevo, creating a new contact if it doesn't exist in your account.

 | --- |
| Brevo API KeyType: stringRequired: True | Check out this page on how to get your API key: [https://help.brevo.com/hc/en-us/articles/209467485-Create-and-manage-your-API-keys](https://help.brevo.com/hc/en-us/articles/209467485-Create-and-manage-your-API-keys) |
| Email of the userType: stringRequired: True | Where to find the email for the contact to be created. You can use the filters section to filter out unwanted emails or internal users. |
| AttributesType: dictionaryRequired: True | For information on potential attributes, refer to the following page: [https://help.brevo.com/hc/en-us/articles/10617359589906-Create-and-manage-contact-attributes](https://help.brevo.com/hc/en-us/articles/10617359589906-Create-and-manage-contact-attributes) |

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
    "name": "Brevo",
    "inputs": {
        "apiKey": {
            "value": ""
        },
        "email": {
            "value": "{person.properties.email}"
        },
        "attributes": {
            "value": {
                "EMAIL": "{person.properties.email}",
                "LASTNAME": "{person.properties.lastname}",
                "FIRSTNAME": "{person.properties.firstname}"
            }
        }
    },
    "enabled": true,
    "template_id": "template-brevo"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/webhook/template_airtable.py) is available on GitHub.

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