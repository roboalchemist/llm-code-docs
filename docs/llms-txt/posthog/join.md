# Source: https://posthog.com/docs/data-warehouse/join.md

# Joining data - Docs

The real power of the data warehouse is the ability to combine data from multiple tables in a single query. Joins enable you to do this. They enable you to choose fields that act as connections between PostHog and external sources.

## Table joins

You can join external data on existing PostHog schemas and other external data tables. These joins are saved and interpreted anytime they're accessed on the origin table.

To define a join, go to the [SQL editor](https://app.posthog.com/sql), click the three dots next to your source table, and click **Add join**. Here you define the source table key, joining table, and joining table key as well as how the fields are accessed.

For example, if you import your Stripe data, you can define a join between the PostHog's `events` table's `distinct_id` key and the `stripe_customer` table's `email` key. You can then access the `stripe_customer` table through the `events` table like `SELECT stripe_customer.id FROM events`.

![Create a join](https://res.cloudinary.com/dmukukwp6/image/upload/join_light_9b369cc72f.png)![Create a join](https://res.cloudinary.com/dmukukwp6/image/upload/join_dark_41d32574ec.png)

Once joined, source properties can be used in filters, breakdowns, and [SQL expressions](/docs/sql/expressions.md).

To edit or delete a table join, click the three dots next to your source table, click **View table schema**, click the three dots next to your joined table, and select **Edit** or **Delete**.

## Person joins

Person joins are a special type of table joins. They are joins on the `persons` table in PostHog. When you join external data on this table, we enable you to use it like a person filter in insights.

> **Note:** To see `extended person properties` in filters, be sure to start the join on the `persons` table as the source table. To do that, go to the [SQL editor](https://app.posthog.com/sql), find the persons table in the left column, click the three dots next to the `persons` table, and click **Add join**.

![Filter on joined person properties](https://res.cloudinary.com/dmukukwp6/image/upload/p_light_b0d3101335.png)![Filter on joined person properties](https://res.cloudinary.com/dmukukwp6/image/upload/p_dark_fc9634f06e.png)

> **Note:** Be sure that your joined keys actually match. For example `persons.id` returns a UUID, even if you use an email as a `distinct_id` when capturing events. You might need to add a person property like `email`.

## Query joins

If you only want to join data together for a single insight or query, you can use SQL commands like `WHERE IN` and `JOIN` SQL commands.

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

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better