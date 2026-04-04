# Source: https://posthog.com/docs/revenue-analytics/connect-to-customers.md

# Connect to customers - Docs

**Revenue analytics is in beta**

Revenue analytics is currently works best for:

1.  Small to medium-sized companies
2.  Companies with subscription models (mostly SaaS)

If you process more than 20,000 transactions per month, or your revenue comes primarily from one-off payments rather than recurring subscriptions, revenue analytics may feel less useful, slower, or provide less insight than expected.

You can connect your revenue data to `persons` and `groups` in the [revenue analytics settings](https://app.posthog.com/data-management/revenue).

This is automatically done when you're using revenue events (since we know what person/group an event belongs to) but we need your help to manually map them in case you're using a data warehouse source.

![Revenue analytics persons and groups setup](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_09_05_at_16_20_38_743c93fff2.png)![Revenue analytics persons and groups setup](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_09_05_at_16_20_29_8ec0f4633a.png)

Once this is connected you'll be able to properly see who your top customers are in the [Top customers dashboard](https://app.posthog.com/revenue_analytics#top-customers).

You'll also get access to the `persons_revenue_analytics` and `groups_revenue_analytics` tables in the [data warehouse](https://app.posthog.com/data-warehouse). This is a simple map of `person_id`/`group_key` to what their all-time revenue is. We plan on expanding that soon with more fields and also making that data available on the soon-to-be-released [CRM](/teams/crm.md) page.

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=--+Count+the+number+of+persons+with+revenue+greater+than+1%2C000%2C000%0ASELECT+COUNT%28*%29%0AFROM+persons_revenue_analytics%0AWHERE+amount+%3E+1000000)

PostHog AI

```sql
-- Count the number of persons with revenue greater than 1,000,000
SELECT COUNT(*)
FROM persons_revenue_analytics
WHERE amount > 1000000
```

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better