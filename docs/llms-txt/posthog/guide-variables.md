# Source: https://posthog.com/docs/endpoints/guide-variables.md

# Create an endpoint with variables - Docs

This guide walks through creating an endpoint that accepts variables, allowing you to filter results at execution time. We'll create a customer-specific analytics endpoint that filters data by a `customer_id` property.

## Step 1: Write your SQL query with a variable

Open the [SQL editor](https://us.posthog.com/sql) and write a query that uses the `{variables.variable_name}` syntax:

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=SELECT%0A++++toDate%28timestamp%29+AS+date%2C%0A++++count%28%29+AS+event_count%0AFROM+events%0AWHERE%0A++++properties.customer_id+%3D+%7Bvariables.customer_id%7D%0A++++AND+timestamp+%3E%3D+now%28%29+-+INTERVAL+30+DAY%0AGROUP+BY+date%0AORDER+BY+date)

PostHog AI

```sql
SELECT
    toDate(timestamp) AS date,
    count() AS event_count
FROM events
WHERE
    properties.customer_id = {variables.customer_id}
    AND timestamp >= now() - INTERVAL 30 DAY
GROUP BY date
ORDER BY date
```

![SQL query with variable in the editor](https://res.cloudinary.com/dmukukwp6/image/upload/w_800,c_limit,q_auto,f_auto/pasted_image_2026_02_05_T12_59_55_871_Z_1c17ec304e.png)![SQL query with variable in the editor](https://res.cloudinary.com/dmukukwp6/image/upload/w_800,c_limit,q_auto,f_auto/pasted_image_2026_02_05_T12_59_18_267_Z_269f3e06f6.png)

## Step 2: Define the variable

In the **Variables** tab in the output pane, click **Add variable**, then **New variable** and fill in the modal.

1.  **Name**: A human-readable name (e.g., "Customer ID")
2.  **Type**: The variable type (String, Number, etc.)
3.  **Default value**: Optional default when no value is provided

![Configuring a variable in the SQL editor](https://res.cloudinary.com/dmukukwp6/image/upload/w_800,c_limit,q_auto,f_auto/pasted_image_2026_02_05_T13_03_07_830_Z_952563f31e.png)![Configuring a variable in the SQL editor](https://res.cloudinary.com/dmukukwp6/image/upload/w_800,c_limit,q_auto,f_auto/pasted_image_2026_02_05_T13_01_45_787_Z_44e98d6bcd.png)

## Step 3: Test your query

Enter a test value for your variable and run the query to verify it works:

![Testing the query with a variable value](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_05_T13_32_16_983_Z_b30a6a3f84.png)![Testing the query with a variable value](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_05_T13_32_31_647_Z_ce80d5a635.png)

## Step 4: Create the endpoint

Once your query works, click the **Endpoint** tab in the output pane:

1.  Enter a descriptive name (e.g., `customer_events_by_day`)
2.  Add an optional description
3.  Click **Create endpoint**

![Creating an endpoint from a SQL query](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_05_T13_33_42_282_Z_b8d9cfb8ae.png)![Creating an endpoint from a SQL query](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_05_T13_34_34_889_Z_d7de925054.png)

## Step 5: Execute with a variable

Now you can call your endpoint and pass the variable value:

Terminal

PostHog AI

```bash
curl -X POST \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"variables": {"customer_id": "acme-corp"}}' \
  "<ph_app_host>/api/projects/{project_id}/endpoints/customer_events_by_day/run"
```

The response will only include events where `properties.customer_id = 'acme-corp'`.

## Pay attention: Variables are required

If your endpoint has a variable defined, you **must** provide a value when executing. This is a safety feature to prevent accidentally returning unfiltered data.

Calling the endpoint without the required variable will return an error:

JSON

PostHog AI

```json
{
  "detail": "Required variable 'customer_id' not provided"
}
```

## Next steps

-   Learn more about [variables](/docs/endpoints/variables.md) including magic variables for insight-based endpoints
-   [Materialize your endpoint](/docs/endpoints/materialization.md) for better performance
-   [Generate a typed SDK](/docs/endpoints/openapi-sdk-generation.md) from your endpoint's OpenAPI spec

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better