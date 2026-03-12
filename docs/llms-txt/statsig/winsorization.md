# Source: https://docs.statsig.com/statsig-warehouse-native/features/statistics/methodologies/winsorization.md

# Source: https://docs.statsig.com/experiments/statistical-methods/methodologies/winsorization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Winsorization

Winsorization is a common technique for removing noise in experiment results, specifically from outliers.

Winsorization refers to the practice of measuring the percentile Px of a metric and setting all values over Px to Px.

Statsig computes the Px value using all non-zero and non-null unit-level values of the metric; metrics are aggregated from rows or events, and then the Px'th unit's value is used as the threshold to adjust other units' values.

<Tabs>
  <Tab title="Statsig Cloud">
    At Statsig, the default percentile for winsorization is 99.9%. This reduces the influence of extreme outliers caused by factors such as logging errors or bad actors.

    Winsorization is applied to sum, event count, mean, ratio, and funnel metrics, including imported metrics. Winsorization will not be applied to Participation or User Accounting metrics.
  </Tab>

  <Tab title="Warehouse Native">
    Statsig Warehouse Native lets you configure this per metric - and choose explicitly the upper and/or lower bounds to apply.

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/stats-methods/winsorization/6d058842-27f7-4b6b-9bd8-245a5f894f90.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=46076a54e836d3e66806de28526bbd34" alt="Winsorization configuration interface" width="1042" height="344" data-path="images/snippets/stats-methods/winsorization/6d058842-27f7-4b6b-9bd8-245a5f894f90.png" />
    </Frame>

    Winsorization is applied to to sum, event count, mean and ratio metrics.
  </Tab>
</Tabs>

## Metric Capping

This is a very simple, but  effective technique to handle outliers. With this capability, you can define max values for a metric for whatever unit type(s) are configured for this metric. Any value surpassing the set cap will automatically be adjusted downward to match it.

For instance, if you determine that purchases greater than \$10,000 per day on your E-commerce platform should not skew analysis, any transaction exceeding this threshold will be adjusted downward to this limit, ensuring the integrity of your experiment analysis. Capped metrics are available for Event Count and Aggregation (sum) metric types.


Built with [Mintlify](https://mintlify.com).