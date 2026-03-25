# Source: https://docs.firehydrant.com/docs/chronosphere-event-source.md

# Chronosphere Event Source

The Chronosphere Event Source for Signals allows users to create events in FireHydrant from alerts sent from Chronosphere. [Alert Rules](https://docs.firehydrant.com/docs/alert-rules) can be configured to scan the payload body of Chronosphere events and ensure the right teams are notified of events they care about.

## Configuration

1. In FireHydrant, copy the Chronosphere ingress URL on the [Event Sources](https://app.firehydrant.io/signals/sources/integrations)  page.
2. Next, you'll want to follow Chronosphere's instructions for [creating a generic webhook notifier](https://docs.chronosphere.io/alerts/notifications/notifiers/webhook). In the URL field, enter the URL copied from step #1 above.

## Field Mappings

FireHydrant's Chronosphere transposer will map the following fields to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

| Chronosphere Parameter          | FireHydrant Parameter                                                                                                                                          |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alerts[0].fingerprint`         | `idempotency_key`                                                                                                                                              |
| `alerts[0].labels.alertname`    | `summary` - If no `alertname` label is supplied by Chronosphere, the **Summary** will be "Unknown"                                                             |
| `alerts[0].annotations.message` | `body` - If no `message` annotation is supplied by Chronosphere, the **Body** will be "No information provided"                                                |
| `alerts[0].status`              | `status` - Open when `status` is "firing", otherwise closed                                                                                                    |
| `alerts[0].annotations`         | `annotations['chronosphere/annotation-*']` - Chronosphere annotations are prefixed with `chronosphere/annotation-` and inserted into FireHydrant `annotations` |
| `alerts[0].labels`              | `annotations['chronosphere/label-*']` - Chronosphere labels are prefixed with `chronosphere/label-` and inserted into FireHydrant `annotations`                |

The above mappings will transpose the following example payload from GCP Service Health:

```json Chronosphere Example Payload
{
  "notifier": "test webhook",
  "status": "firing",
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "alertname": "test alert",
        "component": "remote_write",
        "instance": "localhost:3030",
        "job": "collector_binary",
        "severity": "critical",
        "pod_name": "prom-74cbfb46c9-2ftk9"
      },
      "annotations": {
        "ruleid": "32bb3fbe-c10b-44bb-a4c0-3d053f4a08cd",
        "monitor_slug": "test-monitor",
        "notification_policy_slug": "test-policy"
      },
      "startsAt": "2020-05-19T13:57:21.68227886Z",
      "endsAt": "0001-01-01T00:00:00Z",
      "fingerprint": "7424223989b20025"
    }
  ],
  "groupLabels": {
    "alertname": "test alert",
    "severity": "critical"
  },
  "commonLabels": {
    "alertname": "test alert",
    "component": "remote_write",
    "instance": "localhost:3030",
    "job": "collector_binary",
    "severity": "critical",
    "pod_name": "prom-74cbfb46c9-2ftk9"
  },
  "commonAnnotations": {
    "ruleid": "32bb3fbe-c10b-44bb-a4c0-3d053f4a08cd",
    "monitor_slug": "test-monitor",
    "notification_policy_slug": "test-policy"
  },
  "version": "4"
}
```

...into the resulting Signal:

```json Transposed Signal
{
  "summary": "test alert",
  "body": "No information provided",
  "idempotency_key": "7424223989b20025",
  "annotations": {
    "chronosphere/annotation-ruleid": "32bb3fbe-c10b-44bb-a4c0-3d053f4a08cd",
    "chronosphere/annotation-monitor_slug": "test-monitor",
    "chronosphere/annotation-notification_policy_slug": "test-policy",
    "chronosphere/label-alertname": "test alert",
    "chronosphere/label-component": "remote_write",
    "chronosphere/label-instance": "localhost:3030",
    "chronosphere/label-job": "collector_binary",
    "chronosphere/label-severity": "critical",
    "chronosphere/label-pod_name": "prom-74cbfb46c9-2ftk9"
  },
  "status": 0
}
```