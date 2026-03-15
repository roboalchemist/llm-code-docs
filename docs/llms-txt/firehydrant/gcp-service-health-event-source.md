# Source: https://docs.firehydrant.com/docs/gcp-service-health-event-source.md

# GCP Service Health Event Source

The Google Cloud Platform Service Health Event Source for Signals allows users to create events in FireHydrant from alerts sent from GCP. [Alert Rules](https://docs.firehydrant.com/docs/alert-rules) can be configured to scan the payload body of GCP Health events and ensure the right teams are notified of events they care about.

## Configuration

There are two portions in GCP: you'll need to configure the alerts, and then you'll need to set up notification channels and link them to the alerts via alerting policies. This document assumes you already have or know how to configure service health notifications in GCP.

1. In FireHydrant, copy the Google Service Health ingress URL on the [Event Sources](https://app.firehydrant.io/signals/sources/integrations)  page.
2. Next, you'll want to follow Google's instructions for [creating and managing notification channels](https://cloud.google.com/monitoring/support/notification-options#creating_channels). Add a new **Webhook** notification channel and set the URL you copied above as the destination. Once done, you can click **Test Connection**, and you should see something pop up on the [Event Logs](https://app.firehydrant.io/signals/logs) page.

## Field Mappings

FireHydrant's GCP Service Health transposer will map the following fields to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

| GCP Service Health Parameter | FireHydrant Parameter                                                               |
| :--------------------------- | :---------------------------------------------------------------------------------- |
| `incident.incident_id`       | `idempotency_key`                                                                   |
| `incident.policy_name`       | `summary`                                                                           |
| `incident.summary`           | `body`                                                                              |
| `incident.state`             | `status` - Open when `incident.state` is "OPEN" or "ACKNOWLEDGED," otherwise closed |
| `incident.url`               | `links['GCP Service Health Trigger']`                                               |

The above mappings will transpose the following example payload from GCP Service Health:

```json GCP Service Health Example Payload
{
  "version": "test",
  "incident": {
    "incident_id": "12345",
    "scoping_project_id": "12345",
    "scoping_project_number": 12345,
    "url": "http://www.example.com",
    "started_at": 0,
    "ended_at": 0,
    "state": "OPEN",
    "summary": "Test Incident",
    "apigee_url": "http://www.example.com",
    "observed_value": "1.0",
    "resource": {
      "type": "example_resource",
      "labels": {
        "example": "label"
      }
    },
    "resource_type_display_name": "Example Resource Type",
    "resource_id": "12345",
    "resource_display_name": "Example Resource",
    "resource_name": "projects/12345/example_resources/12345",
    "metric": {
      "type": "test.googleapis.com/metric",
      "displayName": "Test Metric",
      "labels": {
        "example": "label"
      }
    },
    "metadata": {
      "system_labels": {
        "example": "label"
      },
      "user_labels": {
        "example": "label"
      }
    },
    "policy_name": "projects/12345/alertPolicies/12345",
    "policy_user_labels": {
      "example": "label"
    },
    "documentation": "Test documentation",
    "condition": {
      "name": "projects/12345/alertPolicies/12345/conditions/12345",
      "displayName": "Example condition",
      "conditionThreshold": {
        "filter": "metric.type=\"test.googleapis.com/metric\" resource.type=\"example_resource\"",
        "comparison": "COMPARISON_GT",
        "thresholdValue": 0.5,
        "duration": "0s",
        "trigger": {
          "count": 1
        }
      }
    },
    "condition_name": "Example condition",
    "threshold_value": "0.5"
  }
}
```

...into the resulting Signal:

```json Transposed Signal
{
  "summary": "projects/12345/alertPolicies/12345",
  "body": "Test Incident",
  "idempotency_key": "12345",
  "links": [
    {
      "href": "http://www.example.com",
      "text": "GCP Service Health Trigger"
    }
  ],
  "status": 0
}
```