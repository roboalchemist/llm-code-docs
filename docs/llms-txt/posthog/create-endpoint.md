# Source: https://posthog.com/docs/endpoints/start-here/create-endpoint.md

# Create an endpoint - Docs

1.  1

    ## Create your endpoint

    Required

    Once you have your insight or SQL query, create an endpoint from it. This will give you a stable API endpoint you can call to retrieve the data.

    ## From insight

    **From an existing insight:**

    1.  Open your insight
    2.  Click on the info & actions button (the three dots button in the top right)
    3.  Click **Create endpoint**

        ![Creating an endpoint from an insight](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/endpoint_from_insight_b9567d7ef7.png)![Creating an endpoint from an insight](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/endpoint_from_insight_b9567d7ef7.png)

    **From the Endpoints page:**

    1.  Go to the [Endpoints page](https://app.posthog.com/endpoints) and click **New endpoint** > **Insight-based endpoint**
    2.  Select an existing insight from the list, or create a new one

    Once you've selected your insight:

    1.  Give your endpoint a descriptive name and optionally a description

    -   **Recommended** - `daily_active_users`, `account_users_activity`, `signup_funnel`
    -   **Avoid** - `endpoint1`, `test`, `query`

    2.  Create the endpoint

    ## From SQL

    1.  In the SQL editor, click on the **Endpoint** tab in the output pane:

        ![Creating an endpoint from a SQL query](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T12_00_54_246_Z_a8d31a1299.png)![Creating an endpoint from a SQL query](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T12_00_26_709_Z_11f8e467e6.png)

    2.  Give your endpoint a descriptive name and optionally a description

    -   **Recommended** - `daily_active_users`, `account_users_activity`, `signup_funnel`
    -   **Avoid** - `endpoint1`, `test`, `query`

    3.  Create the endpoint

2.  2

    ## Verify endpoint data

    Recommended

    Before integrating your endpoint into your application, use the **Playground** tab to verify it returns the expected data.

    1.  Open your endpoint from the [Endpoints page](https://posthog.com/endpoints)

    2.  Click the **Playground** tab

        ![Endpoint playground tab](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T12_31_26_778_Z_c5108ec55b.png)![Endpoint playground tab](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T12_30_54_702_Z_2d3d04c01b.png)

    3.  If your endpoint has [variables](/docs/endpoints/variables.md), enter test values

    4.  Click **Execute endpoint** to retrieve the data

    5.  Review the results to understand the response structure

3.  3

    ## Next step

    Now retrieve data from your endpoint using your preferred language.

    [Retrieve your data](/docs/endpoints/start-here/retrieve-data.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better