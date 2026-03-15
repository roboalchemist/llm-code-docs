# Source: https://posthog.com/docs/cdp/destinations/engage.md

# Send PostHog person data to Engage - Docs

You'll also need access to the relevant Engage account.

## Installation

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=engage) tab.
3.  Search for **Engage** and click **\+ Create**.
4.  Add your Engage Public key and Private key at the configuration step.
5.  Press **Create & Enable** and watch your 'Customers' list get populated in Engage!

## Configuration

| Option | Description |
| --- | --- |
| Public keyType: stringRequired: True | Get your public key from your Engage dashboard (Settings -> Account) |
| Private keyType: stringRequired: True | Get your private key from your Engage dashboard (Settings -> Account) |

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
    "name": "Engage.so",
    "inputs": {
        "public_key": {
            "value": ""
        },
        "private_key": {
            "value": ""
        }
    },
    "enabled": true,
    "template_id": "template-engage-so"
}'
```

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/engage/template_engage.py) is available on GitHub.

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