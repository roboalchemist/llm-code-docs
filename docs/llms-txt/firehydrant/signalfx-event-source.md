# Source: https://docs.firehydrant.com/docs/signalfx-event-source.md

# SignalFX Event Source

The SignalFX Integration (Splunk Cloud Observability) for Signals allows users to create events in FireHydrant from webhooks configured in SignalFX. Anytime that SignalFX sends an event to FireHydrant, we’ll evaluate the event payload to see if it matches a rule setup by one of your teams. If it matches that rule, we’ll alert the team. Learn more about [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) here.

> 📘 Notice:
>
> The Splunk Cloud Platform requires that all external webhook URLs be added to a webhook allow list before Splunk can send it a payload. The webhook allow list is a list of URL endpoints to which webhook alert actions in Splunk Cloud Platform are permitted to send HTTP POST requests.
>
> Before a triggered alert can send a request to a specified webhook URL, Splunk Cloud Platform checks to ensure that the URL is on the allow list. You can add URLs to the allow list using the webhook allow list page in Splunk Web.
>
> * [Configure webhook allow list using Splunk Web](https://docs.splunk.com/Documentation/SplunkCloud/9.3.2408/Admin/ConfigureWebhookAllowList)

### Configuring SignalFX Webhook

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find a webhook URL that you will use when creating a webhook in SignalFX.
2. In SignalFX, create a new webhook and add the URL from step 1 to your webhook.
3. Create a webhook integration, and then add that webhook integrations as a detector alert recipient in SignalFX.
4. Click “Add Webhook” to save your webhook.

You can learn more about SignalFX webhooks by reading their [Webhooks documentation](https://docs.splunk.com/observability/en/admin/notif-services/webhook.html#send-alert-notifications-to-a-webhook-using-splunk-observability-cloud).

### Testing your SignalFX Webhook

1. When creating the webhook integration, send a test webhook to the Signals Sources URL.
2. Confirm that FireHydrant received your webhook by visiting Alerting > Webhook Logs in the web app. You should see a new event created. You can open the drawer to see the full payload from SignalFX.

## Field Mappings/Behaviors

The payload from SignalFX will be directly mapped to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model). The following table explains the behavior once the payload hits our system:

| Inbound Parameter     | FireHydrant Parameter  |
| :-------------------- | :--------------------- |
| `payload.incidentId`  | `idempotency_key`      |
| `payload.detector`    | `summary`              |
| `payload.description` | `body`                 |
| `payload.detectorURL` | `links`                |
| `payload.imageURL`    | `images`               |
|                       | `status` - Always Open |

These mappings mean that an inbound webhook from SignalFX with the following content:

```json
{
  "sf_schema": 2,
  "detector": "My detector",
  "detectorUrl": "https://app.us1.signalfx.com/#/detector/123456/edit",
  "incidentId": "13168413514",
  "eventType": "&lt;event-type&gt;",
  "rule": "My detector rule",
  "severity": "Critical",
  "description": "Latency of host myserver is 43.4, over a datacenter-wide latency of 42.9",
  "status": "anomalous",
  "statusExtended": "anomalous",
  "imageUrl": "https://org.us1.signalfx.com/#/chart/abCDefGHij",
  "timestamp": "20122-10-25T21:19:38Z",
  "detectOnCondition": "when(a > b and b > 40)",
  "inputs": {
    "a": {
      "key": {
        "host": "myserver",
        "dc": "us-west-1"
      },
      "value": 43.4,
      "fragment": "data('latency').p99(by=['host', 'dc'])"
    },
    "b": {
      "key": {
        "dc": "us-west-1"
      },
      "value": 42.9,
      "fragment": "data('latency').p99(by='dc')"
    },
    "_S2": {
      "value": 40,
      "fragment": "40"
    }
  }
}
```

Will be transposed to the following FireHydrant Signal:

```json
{
  "summary": "My detector",
  "body": "Latency of host myserver is 43.4, over a datacenter-wide latency of 42.9",
  "links": [
    {
      "href": "https://app.us1.signalfx.com/#/detector/123456/edit",
      "text": "Splunk Observability Cloud Trigger"
    }
  ],
  "images": [
    {
      "src": "https://org.us1.signalfx.com/#/chart/abCDefGHij",
      "alt": "My detector"
    }
  ],
  "idempotency_key": "13168413514"
}
```