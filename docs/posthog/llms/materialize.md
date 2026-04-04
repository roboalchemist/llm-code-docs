# Source: https://posthog.com/docs/data-warehouse/views/materialize.md

# Creating materialized views - Docs

Views can be materialized and stored in the PostHog data warehouse. This means that the view is precomputed, which can significantly improve query performance. This is useful for expensive and frequently used queries like KPI dashboards or [embedded analytics](/tutorials/embedded-analytics.md) queries.

To materialize a view, go to the [SQL editor](https://us.posthog.com/sql), select the **Materialization** tab below the query, click **Save and materialize**, and give it a name without spaces. You can then query the view like any other table.

![Materialize view](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/Clean_Shot_2025_08_26_at_13_48_10_2x_88dc4ae252.png)![Materialize view](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/Clean_Shot_2025_08_26_at_13_48_31_2x_16e9dbe683.png)

Once materialized, you can query the view like any other.

## Scheduling a materialized view

After you create a view, you can also schedule it to be updated at a specific interval, anywhere from never to every five minutes to every month. This is useful when you have a view that is used frequently, and you want to ensure that the data synced at a specified cadence.

For example, if you sync your billing data to Postgres using a cron job daily and link Postgres as a source in PostHog, you could set up a materialized view with that billing data to resync daily as well.

![Materialize view](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/Clean_Shot_2025_08_26_at_13_52_13_2x_b0087e4228.png)![Materialize view](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/Clean_Shot_2025_08_26_at_13_52_28_2x_3b0febbf29.png)

## Tips for materializing views

-   The purpose of materialization is to speed up queries, so you don't need to materialize views that are already fast.

-   You can materialize only the slow part of a larger query, like a `with` expression or a subquery. Often times, materializing a subset is a good way to create a resource that's reusable, including insights and other data warehouse views.

-   Datasets generated from materialized views are only updated at the specified intervals and not in real-time. This means that if you have a view that is used in a dashboard or relied upon for another query, the dashboard will not update until the materialized view is updated. We offer a 5-minute refresh interval, but if the query takes longer than that to execute, it will only be updated once the query is finished and rerun at the next 5-minute interval.

-   Materialization runs have more compute and memory resources allocated to them than standard queries, but they still can timeout for inefficient queries. We time out after 1 hour of processing time.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better