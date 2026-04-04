# Source: https://documentation.onesignal.com/docs/en/elasticsearch.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Elasticsearch

> Sync custom events from Elasticsearch to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Elasticsearch"

export const DATA_TYPE_0 = "event document fields"

export const COLUMN_HEADER_0 = "Elasticsearch Field"

export const PROPERTIES_DESCRIPTION_0 = "Nested object or flattened fields"

## Overview

The OneSignal + Elasticsearch integration enables automatic syncing of custom events from your Elasticsearch cluster to OneSignal. This allows you to trigger automated Journeys and personalized messaging campaigns based on user behavioral data stored in your search and analytics engine.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Elasticsearch

* **Elasticsearch cluster** (version 7.0 or higher recommended)
* **Authentication credentials** (API key, username/password, or certificate)
* **Event indices** containing behavioral data with proper document structure
* **Network access** from OneSignal to your Elasticsearch cluster

***

## Setup

<Steps>
  <Step title="Configure Elasticsearch access">
    Ensure OneSignal can connect to your Elasticsearch cluster:

    **For Elasticsearch Cloud:**

    * Navigate to **Security** in your Elasticsearch Cloud console
    * Create an API key with read permissions for event indices
    * Note your **Cloud ID** and **API Key**

    **For Self-hosted Elasticsearch:**

    * Configure authentication (basic auth or API key)
    * Ensure your cluster is accessible from OneSignal's IP addresses
    * Note your cluster **endpoint URL** and **credentials**
  </Step>

  <Step title="Create dedicated user (recommended)">
    Create a dedicated user for OneSignal with read-only access to event indices:

    ```json  theme={null}
    PUT _security/user/onesignal_reader
    {
      "password": "strong_password",
      "roles": ["onesignal_events_reader"]
    }

    PUT _security/role/onesignal_events_reader
    {
      "indices": [
        {
          "names": ["events-*", "user_events"],
          "privileges": ["read", "view_index_metadata"]
        }
      ]
    }
    ```
  </Step>

  <Step title="Add integration in OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Elasticsearch** and provide:

    * **Cluster URL**: Your Elasticsearch endpoint (e.g., `https://your-cluster.es.amazonaws.com`)
    * **Authentication Method**: API Key, Basic Auth, or Certificate
    * **Username/Password** or **API Key**: Authentication credentials
    * **Cloud ID** (if using Elasticsearch Cloud): Your deployment Cloud ID
  </Step>

  <Step title="Configure event data source">
    Specify the Elasticsearch index containing your event data:

    * **Index Pattern**: Index or index pattern containing events (e.g., `events-*`)
    * **Event Query**: Optional Elasticsearch Query DSL to filter event documents
    * **Time Field**: Timestamp field for time-based filtering (e.g., `@timestamp`)

    Your event documents should contain fields for:

    * Event name/type (String)
    * User identifier (String)
    * Event timestamp (Date)
    * Additional event properties (Object)
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can access your Elasticsearch cluster and read event data.
  </Step>
</Steps>

***

### Event data mapping

Map your {PLATFORM_0} {DATA_TYPE_0} to OneSignal's custom events format:

| OneSignal Field | {COLUMN_HEADER_0} | Description                | Required |
| --------------- | ----------------- | -------------------------- | -------- |
| `name`          | `event_name`      | Event identifier           | Yes      |
| `external_id`   | `user_id`         | User identifier            | Yes      |
| `timestamp`     | `event_timestamp` | When event occurred        | No       |
| `properties`    | `event_data`      | {PROPERTIES_DESCRIPTION_0} | No       |

***

## Advanced Configuration

### Query DSL Filtering

Use Elasticsearch Query DSL to filter and transform event data before syncing to OneSignal:

```json  theme={null}
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "@timestamp": {
              "gte": "now-7d"
            }
          }
        },
        {
          "terms": {
            "event_name": ["purchase", "signup", "upgrade"]
          }
        }
      ],
      "must_not": [
        {
          "term": {
            "test_user": true
          }
        }
      ]
    }
  },
  "_source": [
    "event_name",
    "user_id",
    "@timestamp",
    "properties.*"
  ]
}
```

### Index Pattern Configuration

Efficiently query across multiple indices:

* **Time-based indices**: Use patterns like `events-2024-*` for time-partitioned data
* **Routing**: Ensure consistent routing for user-based queries
* **Aliases**: Use index aliases for simplified management

### Performance Optimization

Optimize queries for large event volumes:

* **Field filtering**: Use `_source` filtering to retrieve only necessary fields
* **Scroll API**: For large result sets, OneSignal uses scroll pagination
* **Date math**: Use Elasticsearch date math for efficient time-based filtering

<Warning>
  Ensure your Elasticsearch cluster has sufficient resources to handle OneSignal's queries without affecting other applications using the cluster.
</Warning>

***

## FAQ

### How often does OneSignal sync events from Elasticsearch?

OneSignal syncs event data based on your configured schedule, with a minimum interval of 15 minutes.

### Can I sync events from multiple Elasticsearch indices?

Yes, you can use index patterns (e.g., `events-*`) to query across multiple indices, or create multiple integrations for different index groups.

### What happens if my Elasticsearch cluster is temporarily unavailable?

OneSignal will retry connections with exponential backoff. Event syncing will resume automatically once your cluster is accessible again.

Built with [Mintlify](https://mintlify.com).
