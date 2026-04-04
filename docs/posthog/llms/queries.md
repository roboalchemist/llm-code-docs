# Source: https://posthog.com/docs/how-posthog-works/queries.md

# Source: https://posthog.com/docs/api/queries.md

# API queries - Docs

API queries enable you to query your data in PostHog. This is useful for:

-   Building [embedded analytics](/tutorials/embedded-analytics.md).
-   Pulling aggregated PostHog data into your own or other apps.

> **When should you *not* use API queries?**
>
> 1.  When you want to export large amounts of data. Use [batch exports](/docs/cdp/batch-exports.md) instead.
> 2.  When you want to send data to destinations like Slack or webhooks immediately. Use [real-time destinations](/docs/cdp/destinations.md) instead.
> 3.  If you need data from long-running queries with high memory usage at regular intervals. In this case, you should use [materialized views](/docs/data-warehouse/views/materialize.md) with a schedule instead. You can [query these through SQL](#2-materialize-a-view-for-the-data-you-need) and get faster results.

## Prerequisites

Using API queries requires:

1.  A PostHog project and its project ID which you can get from [your project settings](https://us.posthog.com/settings/project#variables).
2.  A personal API key for your project with the **Query Read** permission. You can create this in [your user settings](https://us.posthog.com/settings/user-api-keys#personal-api-keys).

## Creating a query

To create a query, you make a `POST` request to the `/api/projects/:project_id/query/` endpoint. The body of the request should be a JSON object with a `query` property with a `kind` and `query` property.

**Query limits**

By default, API queries return up to 100 rows. If you specify your own `LIMIT` value, you can return up to 50k rows per query before we suggest [paginating](#5-use-timestamp-based-pagination-instead-of-offset).

For example, to create a query that gets events where the `$current_url` contains blog, you use `kind: HogQLQuery` and SQL like:

PostHog AI

### Terminal

```bash
curl \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" \
  <ph_app_host>/api/projects/:project_id/query/ \
  -d '{
        "query": {
          "kind": "HogQLQuery",
          "query": "select properties.$current_url from events where properties.$current_url like '\''%/blog%'\'' limit 100"
        },
        "name": "get 100 blog urls"
      }'
```

### Python

```python
import requests
import json
url = "<ph_app_host>/api/projects/{project_id}/query/"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {POSTHOG_PERSONAL_API_KEY}'
}
payload = {
    "query": {
        "kind": "HogQLQuery",
        "query": "select properties.$current_url from events where properties.$current_url like '%/blog%' limit 100"
    },
    "name": "get 100 blog urls"
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

### Node.js

```javascript
import fetch from "node-fetch";
async function createQuery() {
  const url = "<ph_app_host>/api/projects/:project_id/query/";
  const headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {POSTHOG_PERSONAL_API_KEY}"
  };
  const payload = {
    "query": {
      "kind": "HogQLQuery",
      "query": "select properties.$current_url from events where properties.$current_url like '%/blog%' limit 100"
    },
    "name": "get 100 blog urls"
  }
  const response = await fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  console.log(data);
}
createQuery()
```

This is also useful for querying non-event data like persons, data warehouse, session replay metadata, and more. For example, to get a list of all people with the `email` property:

PostHog AI

### Terminal

```bash
curl \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" \
  <ph_app_host>/api/projects/:project_id/query/ \
  -d '{
        "query": {
          "kind": "HogQLQuery",
          "query": "select properties.email from persons where properties.email is not null"
        },
        "name": "get user emails"
      }'
```

### Python

```python
import requests
import json
url = "<ph_app_host>/api/projects/{project_id}/query/"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {POSTHOG_PERSONAL_API_KEY}'
}
payload = {
    "query": {
        "kind": "HogQLQuery",
        "query": "select properties.email from persons where properties.email is not null"
    },
    "name": "get user emails"
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

### Node.js

```javascript
import fetch from "node-fetch";
async function createQuery() {
  const url = "<ph_app_host>/api/projects/:project_id/query/";
  const headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {POSTHOG_PERSONAL_API_KEY}"
  };
  const payload = {
    "query": {
      "kind": "HogQLQuery",
      "query": "select properties.email from persons where properties.email is not null"
    },
    "name": "get user emails"
  }
  const response = await fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  console.log(data);
}
createQuery()
```

Every query you run is logged in the [`query_log` table](/docs/data/query-log.md) along with details like duration, read bytes, read rows, and more. The `name` parameter you provide appears in this log, making it easier to identify and analyze your queries.

## Writing performant queries

When writing custom queries, the burden of performance falls onto you. PostHog handles performance for queries we own (for example, in product analytics insights and experiments, etc.), but because performance depends on how queries are structured and written, we can't optimize them for you. Large data sets particularly require extra careful attention to performance.

Here is some advice for making sure your queries are quick and don't read over too much data (which can increase costs):

### 1\. Use shorter time ranges

You should almost always include a time range in your queries, and the shorter the better. There are a variety of SQL features to help you do this including `now()`, `INTERVAL`, and `dateDiff`. See more about these in our [SQL docs](/docs/product-analytics/sql.md#date-and-time).

[Run in PostHog](https://us.posthog.com/sql?open_query=SELECT+count%28%29+FROM+events+WHERE+timestamp+%3E%3D+now%28%29+-+INTERVAL+7+DAY)

PostHog AI

### SQL

```sql
SELECT count() FROM events WHERE timestamp >= now() - INTERVAL 7 DAY
```

### Terminal

```bash
curl \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" \
  <ph_app_host>/api/projects/:project_id/query/ \
  -d '{
        "query": {
          "kind": "HogQLQuery",
          "query": "SELECT count() FROM events WHERE timestamp >= now() - INTERVAL 7 DAY"
        },
        "name": "event count in last 7 days"
      }'
```

### Python

```python
import requests
import json
url = "<ph_app_host>/api/projects/{project_id}/query/"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {POSTHOG_PERSONAL_API_KEY}'
}
payload = {
    "query": {
        "kind": "HogQLQuery",
        "query": """
          SELECT count()
          FROM events
          WHERE timestamp >= now() - INTERVAL 7 DAY
        """
    },
    "name": "event count in last 7 days"
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

### Node.js

```javascript
import fetch from "node-fetch";
async function createQuery() {
  const url = "<ph_app_host>/api/projects/:project_id/query/";
  const headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {POSTHOG_PERSONAL_API_KEY}"
  };
  const payload = {
    "query": {
      "kind": "HogQLQuery",
      "query": `
        SELECT count()
        FROM events
        WHERE timestamp >= now() - INTERVAL 7 DAY
        LIMIT 100
      `
    },
    "name": "event count in last 7 days"
  }
  const response = await fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  console.log(data);
}
createQuery()
```

### 2\. Materialize a view for the data you need

The data warehouse enables you to [save and materialize views](/docs/data-warehouse/views/materialize.md) of your data. This means that the view is precomputed, which can significantly improve query performance.

To do this, write your query in the [SQL editor](https://us.posthog.com/sql), click **Materialize**, then **Save and materialize**, and give it a name without spaces (I chose `mat_event_count`). You can also schedule to update the view at a specific interval.

![Materialize view](https://res.cloudinary.com/dmukukwp6/image/upload/Clean_Shot_2025_06_19_at_16_12_28_2x_db1e37a5cf.png)![Materialize view](https://res.cloudinary.com/dmukukwp6/image/upload/Clean_Shot_2025_06_19_at_16_12_44_2x_90bd8f28ca.png)

Once done, you can query the view like any other table.

[Run in PostHog](https://us.posthog.com/sql?open_query=SELECT+*+FROM+mat_event_count)

PostHog AI

### SQL

```sql
SELECT * FROM mat_event_count
```

### Terminal

```bash
curl \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" \
  <ph_app_host>/api/projects/:project_id/query/ \
  -d '{
        "query": {
          "kind": "HogQLQuery",
          "query": "SELECT * FROM mat_event_count"
        },
        "name": "get materialized event count"
      }'
```

### Python

```python
import requests
import json
url = "<ph_app_host>/api/projects/{project_id}/query/"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {POSTHOG_PERSONAL_API_KEY}'
}
payload = {
    "query": {
        "kind": "HogQLQuery",
        "query": """
          SELECT *
          FROM mat_event_count
        """
    },
    "name": "get materialized event count"
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

### Node.js

```javascript
import fetch from "node-fetch";
async function createQuery() {
  const url = "<ph_app_host>/api/projects/:project_id/query/";
  const headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {POSTHOG_PERSONAL_API_KEY}"
  };
  const payload = {
    "query": {
      "kind": "HogQLQuery",
      "query": `
        SELECT *
        FROM mat_event_count
      `
    },
    "name": "get materialized counts"
  }
  const response = await fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  console.log(data);
}
createQuery()
```

### 3\. Don't scan the same table multiple times

Reading a large table like `events` or `persons` more than once in the same query multiplies the work PostHog has to do (more I/O, more CPU, more memory). For example, this query is inefficient:

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=WITH+us_events+AS+%28%0A++++SELECT+*%0A++++FROM+events%0A++++WHERE+properties.%24geoip_country_code+%3D+'US'%0A%29%2C%0Aca_events+AS+%28%0A++++SELECT+*%0A++++FROM+events%0A++++WHERE+properties.%24geoip_country_code+%3D+'CA'%0A%29%0ASELECT+*%0AFROM+us_events%0AUNION+ALL%0ASELECT+*%0AFROM+ca_events)

PostHog AI

```sql
WITH us_events AS (
    SELECT *
    FROM events
    WHERE properties.$geoip_country_code = 'US'
),
ca_events AS (
    SELECT *
    FROM events
    WHERE properties.$geoip_country_code = 'CA'
)
SELECT *
FROM us_events
UNION ALL
SELECT *
FROM ca_events
```

Instead, pull the rows you need **once** and save it as a [materialized view](/docs/data-warehouse/views/materialize.md). You can then query from that materialized view in all the other steps.

Start by saving this materialized view, e.g. as `base_events`:

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=SELECT+event%2C+properties.%24geoip_country_code+as+country%0AFROM+events%0AWHERE+properties.%24geoip_country_code+IN+%28'US'%2C+'CA'%29)

PostHog AI

```sql
SELECT event, properties.$geoip_country_code as country
FROM events
WHERE properties.$geoip_country_code IN ('US', 'CA')
```

You can then query from `base_events` in your main query, which avoids scanning the raw `events` table multiple times:

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=WITH+us_events+AS+%28%0A++++SELECT+event%0A++++FROM+base_events%0A++++WHERE+country+%3D+'US'%0A%29%2C%0Aca_events+AS+%28%0A++++SELECT+event%0A++++FROM+base_events%0A++++WHERE+country+%3D+'CA'%0A%29%0ASELECT+*%0AFROM+us_events%0AUNION+ALL%0ASELECT+*%0AFROM+ca_events)

PostHog AI

```sql
WITH us_events AS (
    SELECT event
    FROM base_events
    WHERE country = 'US'
),
ca_events AS (
    SELECT event
    FROM base_events
    WHERE country = 'CA'
)
SELECT *
FROM us_events
UNION ALL
SELECT *
FROM ca_events
```

### 4\. Name your queries for easier debugging

Always provide a meaningful `name` parameter for your queries. This helps you:

-   Identify slow or problematic queries in the [`query_log` table](/docs/data/query-log.md)
-   Analyze query performance patterns over time
-   Debug issues more efficiently
-   Track resource usage by query type

Good query names are descriptive and include the purpose:

-   `daily_active_users_last_7_days`
-   `funnel_signup_to_activation`
-   `revenue_by_country_monthly`

Bad names are generic and vague:

-   `query1`
-   `test`
-   `data`

### 5\. Use timestamp-based pagination instead of OFFSET

When querying large datasets like `events` or `query_log` over multiple batches, avoid using `OFFSET` for pagination. Instead, use timestamp-based pagination, which is much more efficient and scales better.

**❌ Inefficient approach using OFFSET:**

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=--+First+batch%0ASELECT+timestamp%2C+event%2C+distinct_id%0AFROM+events%0AWHERE+timestamp+%3E%3D+'2024-01-01'%0AORDER+BY+timestamp%0ALIMIT+1000%3B%0A%0A--+Second+batch%0ASELECT+timestamp%2C+event%2C+distinct_id%0AFROM+events%0AWHERE+timestamp+%3E%3D+'2024-01-01'%0AORDER+BY+timestamp%0ALIMIT+1000+OFFSET+1000%3B++--+This+gets+slower+with+each+page)

PostHog AI

```sql
-- First batch
SELECT timestamp, event, distinct_id
FROM events
WHERE timestamp >= '2024-01-01'
ORDER BY timestamp
LIMIT 1000;
-- Second batch
SELECT timestamp, event, distinct_id
FROM events
WHERE timestamp >= '2024-01-01'
ORDER BY timestamp
LIMIT 1000 OFFSET 1000;  -- This gets slower with each page
```

**✅ Efficient approach using timestamp pagination:**

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=--+First+batch%0ASELECT+timestamp%2C+event%2C+distinct_id%0AFROM+events%0AWHERE+timestamp+%3E%3D+'2024-01-01'%0AORDER+BY+timestamp%0ALIMIT+1000%3B%0A%0A--+Second+batch+%28use+timestamp+of+last+event+from+previous+batch%29%0ASELECT+timestamp%2C+event%2C+distinct_id%0AFROM+events%0AWHERE+timestamp+%3E+'2024-01-01+12%3A34%3A56.789'++--+timestamp+from+last+row+of+previous+batch%0AORDER+BY+timestamp%0ALIMIT+1000%3B)

PostHog AI

```sql
-- First batch
SELECT timestamp, event, distinct_id
FROM events
WHERE timestamp >= '2024-01-01'
ORDER BY timestamp
LIMIT 1000;
-- Second batch (use timestamp of last event from previous batch)
SELECT timestamp, event, distinct_id
FROM events
WHERE timestamp > '2024-01-01 12:34:56.789'  -- timestamp from last row of previous batch
ORDER BY timestamp
LIMIT 1000;
```

This approach is more efficient because:

-   **Constant performance**: Each query executes in similar time regardless of how many rows you've already retrieved
-   **Index-friendly**: Uses the timestamp index effectively for filtering
-   **Scalable**: Performance doesn't degrade as you paginate through millions of rows

**For geeks:** OFFSET-based pagination gets progressively slower because the database must scan and skip all the offset rows for each query. With timestamp-based pagination, the database uses the timestamp index to directly jump to the right starting point, maintaining consistent performance across all pages.

### 6\. Other SQL optimizations

Options 1-5 make the most difference, but other generic SQL optimizations work too. See our [SQL docs](/docs/product-analytics/sql.md) for commands, useful functions, and more to help you with this.

## Query parameters

Top level request parameters include:

-   `query` (required): Specifies what data to retrieve. This must include a `kind` property that defines the query type.
-   `client_query_id` (optional): A client-provided identifier for tracking the query.
-   `refresh` (optional): Controls caching behavior and execution mode (sync vs async).
-   `filters_override` (optional): Dashboard-specific filters to apply.
-   `variables_override` (optional): Variable overrides for queries that support variables.
-   `name` (optional): A descriptive name for the query to better identify it in the [`query_log` table](/docs/data/query-log.md). We strongly recommend providing meaningful names for easier debugging and performance analysis.

### Caching and execution modes

The `refresh` parameter controls the execution mode of the query. It can be one of the following values:

-   `blocking` (default): Executes synchronously unless fresh results exist in cache
-   `async`: Executes asynchronously unless fresh results exist in cache
-   `force_blocking`: Always executes synchronously
-   `force_async`: Always executes asynchronously
-   `force_cache`: Only returns cached results (never calculates)
-   `lazy_async`: Use extended cache period before asynchronous calculation
-   `async_except_on_cache_miss`: Use cache but execute synchronously on cache miss

> **Tip:** To cancel a running query, send a `DELETE` request to the `/api/projects/:project_id/query/:query_id/` endpoint.

### Query types

The `kind` property in the `query` parameter can be one of the following values.

-   `HogQLQuery`: Queries using [PostHog's version of SQL](/docs/sql.md).
-   `EventsQuery`: Raw event data retrieval
-   `TrendsQuery`: Time-series trend analysis
-   `FunnelsQuery`: Conversion funnel analysis
-   `RetentionQuery`: User retention analysis
-   `PathsQuery`: User journey path analysis

Beyond `HogQLQuery`, these are mostly used to power PostHog internally and are not useful for you, but you can see the [frontend query schema](https://github.com/PostHog/posthog/blob/master/frontend/src/queries/schema/schema-general.ts) for a complete list and more details.

## Response structure

The response format depends on the query type, but all responses include:

-   `results`: The data returned by the query
-   `is_cached` (for cached responses): Indicates the result came from cache
-   `timings` (when available): Performance metrics for the query execution

### Cached responses

API queries are cached by default. You can check if a response is cached by checking the `is_cached` property. Responses also contain cache-related details like:

-   `cache_key`: A unique identifier for the cached result
-   `cache_target_age`: The timestamp until which the cached result is considered valid
-   `last_refresh`: When the data was last computed
-   `next_allowed_client_refresh`: The earliest time when a client can request a fresh calculation

### Asynchronous queries

For asynchronous queries (like ones with `refresh: async`), the initial response includes a query status with its completion status, query ID, start time, and more:

JSON

PostHog AI

```json
{
  "query_status": {
    "id": "2fbd4b19413342a4ad08c307155187bc",
    "team_id": 123,
    "complete": false
  }
}
```

You can then poll the status by sending a `GET` request to the `/api/projects/:project_id/query/:query_id/` endpoint.

Terminal

PostHog AI

```bash
curl \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" \
  <ph_app_host>/api/projects/:project_id/query/$QUERY_ID/
```

## Rate limits

API queries are limited at the project-level to:

-   2400 requests per hour
-   240 requests per minute
-   3 queries running concurrently
-   60 threads per query
-   10 seconds of max execution time
    -   applies to query execution time, not HTTP request duration

At this time, we are not offering higher limits than these, but you may wish to try our [endpoints product](/docs/endpoints.md) which offers query customization and higher limits. Alternatively you may be able to use our [batch exports product](/docs/cdp/batch-exports.md), to pull the data that you need from our events or persons tables on a faster cadence.

If the project's concurrency quota is exhausted, we put the query in queue and wait. The query may wait up to 30 seconds in a queue before executing, being canceled, or timing out.

**Legacy query limits**

Some customers haven't been migrated to the above limit and are on an old limit of 120 queries/hour.

## Further reading

-   [How to set up embedded analytics with PostHog, Next.js, and Recharts](/tutorials/embedded-analytics.md)
-   [How to use Recharts to visualize analytics data (with examples)](/tutorials/recharts.md)
-   [How Mintlify launched user-facing analytics, powered by PostHog](/customers/mintlify.md)
-   [The query endpoint API reference](/docs/api/query.md)
-   [The query API endpoint code on GitHub](https://github.com/PostHog/posthog/blob/master/posthog/api/query.py)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better