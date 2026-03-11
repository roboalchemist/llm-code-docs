# Source: https://www.courier.com/docs/external-integrations/other/splunk-on-call.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Splunk On Call

> Send incident alerts via Splunk On Call by specifying a target type and slug in the recipient profile, with support for summary configuration and override of API credentials.

## Setup

Install the Splunk On Call integration from the [Courier integrations catalog](https://app.courier.com/integrations/catalog/splunk-on-call). You will need your Splunk On Call API key and API ID.

<Note>
  Splunk On Call was formerly known as VictorOps. The API documentation at `portal.victorops.com` may redirect to Splunk's current documentation.
</Note>

## Profile Requirements

To deliver a message to a recipient over Splunk On Call, you must provide a target object containing the recipient's type and slug as `splunk-on-call` in the profile.

```json  theme={null}
{
  "message": {
    "to": {
      "splunk-on-call": {
        "target": {
          "type": "User",
          "slug": "userSlug"
        }
      }
    }
  }
}
```

## Template Requirements

To deliver a message to a recipient over Splunk On Call, you must provide a summary in the notification's integration settings.

## Overrides

You can override the API key, API ID, username, URL, and request body. Below is an example of overriding the API key and username via the `config` override:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "splunk-on-call": {
        "target": {
          "type": "User",
          "slug": "kpryde"
        }
      }
    },
    "providers": {
      "splunk-on-call": {
        "override": {
          "config": {
            "apiKey": "RUNTIME_API_KEY",
            "userName": "RUNTIME_USERNAME"
          }
        }
      }
    }
  }
}
```
