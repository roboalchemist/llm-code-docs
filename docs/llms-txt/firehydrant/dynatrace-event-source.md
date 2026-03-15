# Source: https://docs.firehydrant.com/docs/dynatrace-event-source.md

# Dynatrace Event Source

The Dynatrace Event Source for Signals allows users to create events in FireHydrant from alerts sent from Dynatrace. [Alert Rules](https://docs.firehydrant.com/docs/alert-rules) can be configured to scan the payload body of Dynatrace events and ensure the right teams are notified of events they care about.

In Dynatrace, you can customize the payload and subsequently you can use the [Generic Webhook](https://docs.firehydrant.com/docs/signals-generic-webhook) event source  or create a [Custom Event Source](https://docs.firehydrant.com/docs/signals-custom-event-sources). FireHydrant does provide an out-of-box transposer with some defaults.

## Basic Configuration

1. In FireHydrant, go to **Signals > Event Sources** and copy the ingest URL for Dynatrace.
2. Follow [Dynatrace's instructions](https://docs.dynatrace.com/docs/observe-and-explore/notifications-and-alerting/problem-notifications/webhook-integration) for setting up a custom integration for problem notifications.
   1. Set the URL you copied above in step 1 as the webhook URL.
   2. FireHydrant assumes you will use the example JSON payload provided in their docs:
      ```
      {
        "ImpactedEntities": {ImpactedEntities},
        "ImpactedEntity": "{ImpactedEntity}",
        "PID": "{PID}",
        "ProblemDetailsHTML": "{ProblemDetailsHTML}",
        "ProblemDetailsJSON": {ProblemDetailsJSON},
        "ProblemID": "{ProblemID}",
        "ProblemImpact": "{ProblemImpact}",
        "ProblemTitle": "{ProblemTitle}",
        "Problem URL": "https://example.com",
        "State": "{State}",
        "Tags": "{Tags}"
      }
      ```
3. You can test the connection with **Send test notification**, and you should see an event reflected in the FireHydrant Event Log.

## Field Mappings

FireHydrant's Dynatrace transposer will map the following fields to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

| Dynatrace Parameter  | FireHydrant Parameter                                   |
| :------------------- | :------------------------------------------------------ |
| `ProblemID`          | `idempotency_key`                                       |
| `ProblemTitle`       | `summary`                                               |
| `ProblemDetailsHTML` | `body`                                                  |
| `Problem URL`        | `links['Dynatrace Link']`                               |
| `State`              | `status` - Open when `State` is "Open" otherwise closed |

The above mappings mean that the following example payload from Dynatrace:

```json Dynatrace Payload Example
{
  "ImpactedEntities": [
    {"type": "HOST", "name": "MyHost1", "entity": "HOST-XXXXXXXXXXXXX" },
    {"type": "SERVICE", "name": "MyService1", "entity": "SERVICE-XXXXXXXXXXXXX"}
  ],
  "ImpactedEntity": "MyHost1, MyService1",
  "PID": "99999",
  "ProblemDetailsHTML": "Dynatrace problem notification test run details",
  "ProblemDetailsJSON": {"ID" : "99999" },
  "ProblemID": "999",
  "ProblemImpact": "INFRASTRUCTURE",
  "ProblemTitle": "Dynatrace problem notification test run",
  "Problem URL": "https://example.com",
  "State": "OPEN",
  "Tags": "testtag1, testtag2"
}
```

...will be transposed to the following FireHydrant Signal:

```json Transposed Output
{
  "summary": "Dynatrace problem notification test run",
  "body": "Dynatrace problem notification test run details",
  "links": [
    {
      "href": "https://example.com",
      "text": "Dynatrace Link"
    }
  ],
  "idempotency_key": "999",
  "status": 0
}
```