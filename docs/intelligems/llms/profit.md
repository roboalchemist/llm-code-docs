# Source: https://docs.intelligems.io/analytics/experiment-analytics/metric-definitions/profit.md

# Profit

Intelligems can report down to gross profit. We recommend using gross profit per visitor to analyze most tests, especially those that may affect price, product mix, order volume, or shipping rates. There are three inputs Intelligems supports to estimate profit (see more [here](https://docs.intelligems.io/analytics/how-to-add-profit-to-intelligems-analytics) for instructions on how to input these assumptions):

* **COGS** (Cost of Goods Sold by variant): This is the most important input, and is required in order to enable profit reporting. You can provide a CSV with COGS for each variant, or we can sync the information from Shopify if it’s available there
* **Shipping cost per order**: An assumption for average shipping cost per order. You can also include other fulfillment costs, or costs that are incurred per-order, here
* **Transaction fee percent**: an assumption for fees as a percentage of net revenue. For example, this would include Shopify’s credit card processing fees, but could also include any other fees that you are charged on a percentage of revenue.

These assumptions can be set on the Intelligems settings page. See more [here](https://docs.intelligems.io/analytics/how-to-add-profit-to-intelligems-analytics).

If you do not provide COGS for some products (for example, if you start selling new products since the last time you’ve updated Intelligems’ COGS assumptions), you may see a message in analytics warning that some products do not have COGS. This warning will show if Intelligems detects that less than 90% of net product revenue has associated COGS information. We recommend updating COGS information so that your profit reporting remains accurate. If you leave out COGS information for some products, their COGS will be treated as 0, which inflates profit numbers (these products are treated as having a 100% gross margin).

Within the Profit tab, you will find:

#### Profit & Loss

This section provides a full profit and loss breakdown—including revenue, COGS, and profit for both products and shipping—along with total profit, profit per order, and profit per visitor.

#### Metric Details

This section provides statistical significance and time series for key profit metrics.

#### By Audience

This section shows key profit metrics by audience types. \\
