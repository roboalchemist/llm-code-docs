# Source: https://posthog.com/docs/data-warehouse/query.md

# Querying the data warehouse with SQL - Docs

PostHog provides the full flexibility of SQL to query your data warehouse using the [SQL editor](/docs/data-warehouse/sql.md).

To create a query, go to the [SQL editor](https://us.posthog.com/sql). Here you can see and search the schema of all available sources and [PostHog tables](/docs/data-warehouse/sources/posthog.md) as well as saved views.

![SQL editor](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/Clean_Shot_2025_08_26_at_13_07_22_2x_f4bfc84ae3.png)![SQL editor](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/Clean_Shot_2025_08_26_at_13_07_45_2x_751fc31300.png)

Here you can:

1.  Write your SQL query using your table like `SELECT * FROM stripe.prod.charge`
2.  Click **Run** to see the results.
3.  Modify your query using [SQL commands](/docs/data-warehouse/sql.md) and [functions](/docs/data-warehouse/sql/useful-functions.md) as needed to get the data you want like `select amount / 100 as dollar_charge, status from stripe.prod.charge`.

![Querying a source in PostHog](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/Clean_Shot_2025_08_26_at_13_19_11_2x_b1d7ce399f.png)![Querying a source in PostHog](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/Clean_Shot_2025_08_26_at_13_18_51_2x_e62db75b67.png)

4.  Click **Create insight**.
5.  Choose and customize your visualization.
6.  Click **Save insight**.

**Having trouble writing SQL?**

[PostHog AI](/docs/posthog-ai.md) can help write SQL for you. Just click the icon in the corner of your screen and ask it to write or tweak your query for you.

## SQL visualizations

SQL queries have multiple different visualization options including:

-   Table (default)
-   Big number
-   Line chart
-   Bar chart
-   Stacked bar chart
-   Area chart

By clicking on the **Visualization** tab below the query, you can customize the X-axis, Y-axis, legend, scale, goal lines, and more. Each visualization type has its own set of customization options.

For example, with tables, you can add conditional formatting rules. These enable you to highlight cells based on their value and are set up in the **Conditional formatting** tab.

![Customizing a SQL visualization](https://res.cloudinary.com/dmukukwp6/image/upload/Clean_Shot_2025_07_01_at_13_01_00_2x_181ae75d28.png)![Customizing a SQL visualization](https://res.cloudinary.com/dmukukwp6/image/upload/Clean_Shot_2025_07_01_at_13_02_28_2x_b3ba2d2d8a.png)

## Querying multiple sources together

Much of the power of the data warehouse comes from combining multiple sources, like your Stripe or Hubspot data with your product analytics data. Two of the easiest ways of doing this are `WHERE IN` and `JOIN` SQL commands.

For example, to get a count of events for your Hubspot contacts you can filter `events.distinct_id` by `email FROM hubspot_contacts` like this:

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=SELECT+COUNT%28%29+AS+event_count%2C+distinct_id%0AFROM+events%0AWHERE+distinct_id+IN+%28SELECT+email+FROM+hubspot_contacts%29%0AGROUP+BY+distinct_id%0AORDER+BY+event_count+DESC)

PostHog AI

```sql
SELECT COUNT() AS event_count, distinct_id
FROM events
WHERE distinct_id IN (SELECT email FROM hubspot_contacts)
GROUP BY distinct_id
ORDER BY event_count DESC
```

You can also use a `JOIN` such as `INNER JOIN` or `LEFT JOIN` to combine data. For example, to get a count of events for your Stripe customers you can `INNER JOIN` on `distinct_id` and `email` like this:

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=SELECT+events.distinct_id%2C+COUNT%28%29+AS+event_count%0AFROM+events%0AINNER+JOIN+prod_stripe_customer+ON+events.distinct_id+%3D+prod_stripe_customer.email%0AGROUP+BY+events.distinct_id%0AORDER+BY+event_count+DESC)

PostHog AI

```sql
SELECT events.distinct_id, COUNT() AS event_count
FROM events
INNER JOIN prod_stripe_customer ON events.distinct_id = prod_stripe_customer.email
GROUP BY events.distinct_id
ORDER BY event_count DESC
```

To learn more about joining data, see our guide on [joining data](/docs/data-warehouse/join.md).

## Query execution details

After running a query, execution details can help you understand the resource usage and execution time:

-   **Memory usage**: Total memory consumed by the query
-   **Data read**: Total amount of data read by the query
-   **CPU time**: Processing time used by the CPU
-   **Duration**: Duration of query execution in ClickHouse

Hover over **Execution details** to see additional information about how the query was executed.

![SQL query execution details](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_11_20_T13_39_06_799_Z_92c7985c92.png)![SQL query execution details](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_11_20_T13_42_11_240_Z_6536dfc318.png)

These metrics are helpful for optimizing queries, especially when working with large datasets or complex joins. As you develop and change your query, keep an eye on the impact of your changes on the metrics. Seeing a spike in bytes read might prompt you to use a more selective filter.

## Optimizing queries

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

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better