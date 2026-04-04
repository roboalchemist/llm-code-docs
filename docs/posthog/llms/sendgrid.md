# Source: https://posthog.com/docs/cdp/destinations/sendgrid.md

# Send PostHog person data to Sendgrid - Docs

You can also send person properties to custom fields in Sendgrid.

You'll also need access to the relevant Sendgrid account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=sendgrid) tab.
3.  Search for 'Sendgrid' and click **\+ Create**.
4.  Add your Sendgrid API Key at the configuration step.
5.  Press **Create & Enable** and watch your 'Contacts' list get populated in Sendgrid!

## Configuration

| Option | Description |
| --- | --- |
| Sendgrid API KeyType: stringRequired: True | See [https://app.sendgrid.com/settings/api_keys](https://app.sendgrid.com/settings/api_keys) |
| The email of the userType: stringRequired: True |
| Reserved fieldsType: dictionaryRequired: True | The following field names are allowed: address_line_1, address_line_2, alternate_emails, anonymous_id, city, country, email, external_id, facebook, first_name, last_name, phone_number_id, postal_code, state_province_region, unique_name, whatsapp. |
| Custom fieldsType: dictionaryRequired: False | Configure custom fields in SendGrid before using them here: [https://mc.sendgrid.com/custom-fields](https://mc.sendgrid.com/custom-fields) |

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
    "name": "Sendgrid",
    "inputs": {
        "api_key": {
            "value": ""
        },
        "email": {
            "value": "{person.properties.email}"
        },
        "properties": {
            "value": {
                "city": "{person.properties.city}",
                "country": "{person.properties.country}",
                "last_name": "{person.properties.last_name}",
                "first_name": "{person.properties.first_name}",
                "postal_code": "{person.properties.postal_code}"
            }
        },
        "custom_fields": {
            "value": {}
        }
    },
    "enabled": true,
    "template_id": "template-sendgrid"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/sendgrid/template_sendgrid.py) is available on GitHub.

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