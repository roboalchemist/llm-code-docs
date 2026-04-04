# Source: https://docs.intelligems.io/analytics/experiment-analytics/metric-definitions/subscriptions.md

# Subscriptions

Intelligems provides a set of metrics related to subscription orders and subscription take rate. These are all based on **first subscription orders** — **automatically placed recurring subscription refills are ignored from** Intelligems results.

For Intelligems to provide subscription reporting, it needs to be able to identify these first subscription orders. To do this, Intelligems looks for a variety of order tags. For example, we look for “subscription first order” (case insensitive, for first orders) to include and “subscription recurring order” (case insensitive, for automated recurring orders) to exclude.

If your site offers subscriptions, and the Subscriptions tab within your Intelligems analytics is not displaying any results, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) with the name of the subscription software you use, the tag that is added to first time subscription orders in Shopify, and a screenshot of a first time subscription order. This will help our team ensure we are set up for your subscription software to track correctly.

Within the Subscriptions tab, you will find:

#### Subscription Metrics

* **Subscription Orders per Visitor:** Number of new subscription orders divided by number of unique visitors.
* **Subscription Revenue per Visitor:** Total revenue from new subscription orders divided by number of unique site visitors - revenue includes both product and shipping revenue, net of discounts.
* **Subscription Profit per Visitor:** Total profit from new subscription orders divided by number of unique site visitors - profit includes product and shipping revenue, net of discounts, COGS, and cost of shipping.
* **Subscription % of Orders:** Percentage of orders that contained a subscription.
* **Subscription AOV:** Average net revenue per new subscription order.
* **Subscription Avg Units per Order:** Average quantity of product units contained in each new subscription order.
* **Subscription Product Revenue per Unit:** Average net price for a single unit in a subscription order (net of discounts).

#### Metric Details

This section provides statistical significance and time series for key subscription metrics.

#### By Audience

This section shows key subscription metrics by audience types.
