# Source: https://posthog.com/docs/endpoints/internal-tools.md

# Enrich internal tools with data from endpoints - Docs

This guide walks through integrating PostHog Endpoints with [Retool](https://retool.com/) to build internal dashboards and tools powered by your analytics data.

**Prerequisites**

Before starting, create an endpoint you want to use in your internal tool. See [Create an insight-based endpoint with variables](/docs/endpoints/guide-breakdown.md) for a step-by-step example.

## Step 1: Create a Retool REST API resource

In Retool, resources are reusable connections to external APIs. Create one for PostHog Endpoints:

1.  Go to **Resources** in your Retool workspace
2.  Click **Create new** and select **REST API**
3.  Configure the resource:
    -   **Name**: `PostHog Endpoints` (or similar)
    -   **Base URL**: `https://us.posthog.com/api/projects/{your_project_id}/endpoints` (replace with your project ID)
    -   **Headers**: Add an `Authorization` header with value `Bearer {your_personal_api_key}`

![Creating a Retool REST API resource for PostHog Endpoints](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T14_43_47_573_Z_c8bb5a05e5.png)![Creating a Retool REST API resource for PostHog Endpoints](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T14_43_47_573_Z_c8bb5a05e5.png)

4.  Click **Create resource**

## Step 2: Use the resource in your Retool app

Once your resource is set up, you can query your PostHog endpoints directly from Retool apps.

### Using Retool AI

The fastest way to get started is using Retool's AI assistant. Simply describe what you want:

> Create a simple chart that shows pageviews by OS by querying the PostHog Endpoints REST API resource, and executing the pageviews\_by\_os/run endpoint.

Retool AI will:

1.  Create a query using your PostHog Endpoints resource
2.  Configure the correct endpoint path (e.g., `/pageviews_by_os/run`)
3.  Set up a chart component to visualize the results

![Retool app with a chart showing pageviews by OS from PostHog Endpoints](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T14_44_33_086_Z_5c21fc4443.png)![Retool app with a chart showing pageviews by OS from PostHog Endpoints](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T14_44_33_086_Z_5c21fc4443.png)

### Manual query setup

To create a query manually:

1.  In your Retool app, click **+** to add a new query
2.  Select your **PostHog Endpoints** resource
3.  Set the **Action** to `POST`
4.  Set the **URL path** to your endpoint name followed by `/run` (e.g., `/pageviews_by_os/run`)
5.  Add a **Body** with any required variables:

JSON

PostHog AI

```json
{
  "variables": {
    "$os": "Mac OS X"
  }
}
```

6.  Run the query to fetch data

## Step 3: Build your dashboard

With your query returning data, you can:

-   **Add charts**: Bind chart components to your query results
-   **Create filters**: Use Retool inputs to dynamically pass variables to your endpoint
-   **Build tables**: Display raw data in table components
-   **Combine endpoints**: Query multiple endpoints to build comprehensive dashboards

## Tips for internal tools

-   **Use descriptive endpoint names** like `daily_active_users` or `signup_funnel` so they're easy to find in Retool
-   **Enable materialization** on frequently-queried endpoints for faster response times
-   **Pass variables dynamically** by binding Retool input components to your query's body parameters

## Next steps

-   [Generate a typed SDK](/docs/endpoints/openapi-sdk-generation.md) for more complex integrations
-   [Learn about materialization](/docs/endpoints/materialization.md) to speed up your dashboards
-   [Monitor usage](/docs/endpoints/usage-analytics.md) to track which endpoints power your tools

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better