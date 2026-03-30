# Source: https://posthog.com/docs/endpoints/start-here/define-your-data.md

# Define the data for your endpoint - Docs

1.  1

    ## Choose your data source

    Required

    Endpoints can be created from existing insights or SQL queries in PostHog. Choose the approach that best fits your use case.

    > Not sure where to start? Try building an insight with [PostHog AI](/docs/posthog-ai/example-prompts.md).

    ## Insight-based

    **Best for:** Exposing data from existing insights you've already built.

    [Create an insight](/docs/product-analytics/insights.md) in PostHog that shows the data you want to expose. This could be:

    -   A trend showing daily active users
    -   A funnel tracking user conversion
    -   A retention analysis
    -   Any other insight type

    ![Create an insight in PostHog](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/abe_insight_funnel_example_r_eb45dee714.png)![Create an insight in PostHog](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/abe_insight_funnel_example_r_eb45dee714.png)

    ## SQL-based

    **Best for:** Custom queries, complex joins, or when you need [variables](/docs/endpoints/variables.md).

    Create a SQL query in the [SQL editor](https://us.posthog.com/sql) that returns the data you need. SQL-based endpoints give you full control over the query structure.

    SQL

    [Run in PostHog](https://us.posthog.com/sql?open_query=SELECT%0A++++toDate%28timestamp%29+as+day%2C%0A++++count%28%29+as+event_count%0AFROM+events%0AWHERE+timestamp+%3E+now%28%29+-+interval+30+day%0AGROUP+BY+day%0AORDER+BY+day)

    PostHog AI

    ```sql
    SELECT
        toDate(timestamp) as day,
        count() as event_count
    FROM events
    WHERE timestamp > now() - interval 30 day
    GROUP BY day
    ORDER BY day
    ```

    ![Write a SQL query](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T12_19_52_008_Z_34e3227830.png)![Write a SQL query](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/pasted_image_2026_02_06_T12_19_25_138_Z_c1bcd9501d.png)

2.  2

    ## Verify results of your query

    Recommended

    Before creating an endpoint, make sure your insight or SQL query returns the expected results:

    1.  For **insights**: Check the visualization shows the data you expect
    2.  For **SQL queries**: Click **Run** and review the results table

    This ensures your endpoint will return meaningful data when executed.

3.  3

    ## Next step

    Once you have your data defined, create an endpoint from it.

    [Create an endpoint](/docs/endpoints/start-here/create-endpoint.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better