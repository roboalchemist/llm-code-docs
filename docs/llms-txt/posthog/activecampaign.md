# Source: https://posthog.com/docs/cdp/destinations/activecampaign.md

# Send PostHog person data to ActiveCampaign - Docs

You'll also need access to the relevant ActiveCampaign account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=activecampaign) tab.
3.  Search for 'ActiveCampaign' and click **\+ Create**.
4.  Add your ActiveCampaign API Key at the configuration step.
5.  Press **Create & Enable** and watch your 'Events' list get populated in ActiveCampaign!

## Configuration

| Option | Description |
| --- | --- |
| Account nameType: stringRequired: True | Usually in the form of .activehosted.com. You can use this page to figure our your account name: [https://www.activecampaign.com/login/lookup.php](https://www.activecampaign.com/login/lookup.php) |
| Your ActiveCampaign API KeyType: stringRequired: True | See the docs here: [https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API#h_01HJ6REM2YQW19KYPB189726ST](https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API#h_01HJ6REM2YQW19KYPB189726ST) |
| Email of the userType: stringRequired: True | Where to find the email for the contact to be created. You can use the filters section to filter out unwanted emails or internal users. |
| First name of the userType: stringRequired: True | Where to find the first name for the contact to be created. |
| Last name of the userType: stringRequired: True | Where to find the last name for the contact to be created. |
| Phone number of the userType: stringRequired: True | Where to find the phone number for the contact to be created. |
| Additional person fieldsType: dictionaryRequired: True | Map any values to ActiveCampaign person fields. (fieldId:value) |

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
    "name": "ActiveCampaign",
    "inputs": {
        "accountName": {
            "value": ""
        },
        "apiKey": {
            "value": ""
        },
        "email": {
            "value": "{person.properties.email}"
        },
        "firstName": {
            "value": "{person.properties.firstName}"
        },
        "lastName": {
            "value": "{person.properties.lastName}"
        },
        "phone": {
            "value": "{person.properties.phone}"
        },
        "attributes": {
            "value": {
                "1": "{person.properties.company}",
                "2": "{person.properties.website}"
            }
        }
    },
    "enabled": true,
    "template_id": "template-activecampaign"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/activecampaign/template_activecampaign.py) is available on GitHub.

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