# Source: https://posthog.com/docs/endpoints/guide-breakdown.md

# Create an insight-based endpoint with variables - Docs

This guide walks through creating an endpoint from an insight that has a breakdown, then querying it using the `variables` field to filter results at execution time. We'll create an endpoint that shows daily active users by OS, filterable by a specific OS.

## Step 1: Create an insight with a breakdown

Open [Product analytics](https://us.posthog.com/insights) and create a Trends insight that breaks down by a property. For example:

1.  Create a **Trends** insight for the **$pageview** event.
2.  Add a breakdown by **OS** (the `$os` property).

![Creating an insight with a breakdown by OS](https://res.cloudinary.com/dmukukwp6/image/upload/h_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T13_42_07_696_Z_763bdd2831.png)![Creating an insight with a breakdown by OS](https://res.cloudinary.com/dmukukwp6/image/upload/h_1000,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T13_42_00_047_Z_3fac2784d6.png)

## Step 2: Create an endpoint from the insight

1.  Click the three dots menu in the top right of your insight.
2.  Select `Create endpoint`. This opens up a modal.
3.  Name your endpoint (e.g., `pageviews_by_os`), and optionally give it a description.
4.  Click `Create endpoint`.

![Creating an endpoint from an insight with breakdown](https://res.cloudinary.com/dmukukwp6/image/upload/h_800,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T13_43_50_013_Z_2a6ec80c06.png)![Creating an endpoint from an insight with breakdown](https://res.cloudinary.com/dmukukwp6/image/upload/h_800,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T13_43_52_166_Z_b00b004aa0.png)

## Step 3: Execute with the breakdown variable

For insight-based endpoints with a single breakdown, the breakdown property name automatically becomes a **magic variable**. Pass the variable in your request to filter results to a specific breakdown value.

Terminal

PostHog AI

```bash
curl -X POST \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"variables": {"$os": "Mac OS X"}}' \
  "<ph_app_host>/api/projects/{project_id}/endpoints/pageviews_by_os/run"
```

The response will only include data where `$os` equals "Mac OS X".

![Executing an insight-based endpoint in the Playground tab](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T13_49_06_262_Z_270a8b8cd9.png)![Executing an insight-based endpoint in the Playground tab](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T13_49_23_820_Z_316f7168e8.png)

**Variable required for materialized endpoints**

If your endpoint is [materialized](/docs/endpoints/materialization.md), you **must** provide the breakdown variable. This prevents accidentally returning all breakdown values when you intended to filter.

## Step 4: Use date variables (non-materialized only)

For non-materialized insight endpoints, you can also filter by date range using `date_from` and `date_to`:

Terminal

PostHog AI

```bash
curl -X POST \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"variables": {"$os": "Chrome", "date_from": "2024-01-01", "date_to": "2024-01-31"}}' \
  "<ph_app_host>/api/projects/{project_id}/endpoints/pageviews_by_os/run"
```

![Executing a non-materialized insight-based endpoint in the Playground tab with date filters](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T13_53_47_825_Z_715502b0ad.png)![Executing a non-materialized insight-based endpoint in the Playground tab with date filters](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T13_53_50_886_Z_bcbbf9ef29.png)

**Materialized endpoints do not accept date variables.**

Materialized endpoints have pre-computed data, so `date_from` and `date_to` variables are not supported. Passing them will fail the request.

Only the breakdown variable can be passed to a materialized insight-based endpoint..

## Supported insight types

Breakdown variables work with:

-   **TrendsQuery** - filter trend data by breakdown value
-   **FunnelsQuery** - filter funnel results by breakdown value
-   **RetentionQuery** - filter retention cohorts by breakdown value

**Single breakdown only**

The breakdown variable is only available for insights with a **single** breakdown configured. Insights with multiple breakdowns can still be used as endpoints but won't have a breakdown variable available.

## Next steps

-   Learn more about [variables in endpoints](/docs/endpoints/variables.md)
-   [Materialize your endpoint](/docs/endpoints/materialization.md) for faster response times
-   [Generate a typed SDK](/docs/endpoints/openapi-sdk-generation.md) from your endpoint's OpenAPI spec

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better