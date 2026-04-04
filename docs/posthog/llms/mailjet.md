# Source: https://posthog.com/docs/cdp/destinations/mailjet.md

# Send PostHog person data to Mailjet - Docs

You'll also need access to the relevant Mailjet account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=mailjet) tab.
3.  Search for **Mailjet** and click **\+ Create**.
4.  Add your Mailjet API Key at the configuration step.
5.  Press **Create & Enable** and watch your 'Contacts' list get populated in Mailjet!

## Configuration

| Option | Description |
| --- | --- |
| Mailjet API KeyType: stringRequired: True |
| Mailjet Secret KeyType: stringRequired: True |
| Email of the userType: stringRequired: True | Where to find the email for the user to be checked with Mailjet |
| NameType: stringRequired: False | Name of the contact |
| Is excluded from campaignsType: booleanRequired: False | Whether the contact should be excluded from campaigns |

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
    "name": "Mailjet",
    "inputs": {
        "api_key": {
            "value": ""
        },
        "secret_key": {
            "value": ""
        },
        "email": {
            "value": "{person.properties.email}"
        },
        "name": {
            "value": "{person.properties.first_name} {person.properties.last_name}"
        }
    },
    "enabled": true,
    "template_id": "template-mailjet-create-contact"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/mailjet/template_mailjet.py) is available on GitHub.

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