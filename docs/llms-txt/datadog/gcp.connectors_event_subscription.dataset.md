# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.connectors_event_subscription.dataset.md

---
title: Event Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Event Subscription
---

# Event Subscription

Event Subscription in Google Cloud is a configuration that allows services to receive notifications when specific events occur in other resources. It connects event sources, such as Cloud Storage or Pub/Sub, to event consumers, enabling event-driven architectures. This helps automate workflows and trigger actions in response to changes or updates across cloud services.

```
gcp.connectors_event_subscription
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                      | Description |
| ------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string        |
| ancestors                | core | array<string> |
| create_time              | core | timestamp     | Output only. Created time.                                                                                                                                                     |
| datadog_display_name     | core | string        |
| destinations             | core | json          | Optional. The destination to hit when we receive an event                                                                                                                      |
| event_type_id            | core | string        | Optional. Event type id of the event of current EventSubscription.                                                                                                             |
| gcp_status               | core | json          | Optional. Status indicates the status of the event subscription resource                                                                                                       |
| jms                      | core | json          | Optional. JMS is the source for the event listener.                                                                                                                            |
| labels                   | core | array<string> |
| name                     | core | string        | Required. Identifier. Resource name of the EventSubscription. Format: projects/{project}/locations/{location}/connections/{connection}/eventSubscriptions/{event_subscription} |
| organization_id          | core | string        |
| parent                   | core | string        |
| project_id               | core | string        |
| project_number           | core | string        |
| region_id                | core | string        |
| resource_name            | core | string        |
| subscriber               | core | string        | Optional. name of the Subscriber for the current EventSubscription.                                                                                                            |
| subscriber_link          | core | string        | Optional. Link for Subscriber of the current EventSubscription.                                                                                                                |
| tags                     | core | hstore_csv    |
| trigger_config_variables | core | json          | Optional. Configuration for configuring the trigger                                                                                                                            |
| update_time              | core | timestamp     | Output only. Updated time.                                                                                                                                                     |
| zone_id                  | core | string        |
