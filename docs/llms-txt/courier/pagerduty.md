# Source: https://www.courier.com/docs/external-integrations/other/pagerduty.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PagerDuty

> Send real-time alerts to PagerDuty by connecting your service’s Events API v2 integration with Courier, including support for severity/source overrides and per-user routing key configuration.

## Setup

### Prerequisites

* Pagerduty [account](https://www.pagerduty.com/sign-up/) with elevated privileges
* Pagerduty Service created and configured with Events API v2 integration

### Configure PagerDuty Integration

1. In your PagerDuty account, navigate to the desired Service and access its "Integrations" settings.
2. Add a new "Events API v2" integration and configure it according to your requirements.
3. Copy the Integration Key provided by PagerDuty for the newly created integration.
4. Navigate to the [PagerDuty integration setup page](https://app.courier.com/channels/pagerduty) in your Courier account and provide the necessary information, including the Integration Key.

|                  |                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| **Routing Key**  | Paste the Integration Key obtained from PagerDuty.                                                  |
| **Event Action** | Specify the event action (e.g., trigger) for the notifications.                                     |
| **Source**       | Enter the host name or fully qualified domain name (FQDN) of the source sending the notifications.  |
| **Severity**     | Choose the appropriate severity level (e.g., info, warning, error, critical) for the notifications. |

## Overrides

### Routing Key

You can override the routing key by specifying a `routing_key` in the user profile using `profile.pagerduty.routing_key`.

```json  theme={null}
{
  "profile": {
    "pagerduty": {
      "routing_key": "PROFILE_SPECIFIC_ROUTING_KEY"
    }
  }
}
```

If a `routing_key` is specified in `profile.pagerduty`, it will take precedence over the routing key from the main configuration.

### Payload

You can use the provider override the payload sent to PagerDuty's Events API. Supported overrides include the Severity and Source.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "user_id": "1234567890"
    },
    "providers": {
      "pagerduty": {
        "override": {
          "body": {
            "payload": {
              "severity": "error",
              "source": "a different source"
            }
          }
        }
      }
    }
  }
}
```

For more information on supported payload overrides, refer to the [PagerDuty Events API v2 documentation](https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2).
