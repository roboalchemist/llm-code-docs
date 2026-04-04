# Source: https://planetscale.com/docs/postgres/extensions/pginsights.md

# Extensions: pginsights

> The pginsights extension is a PlanetScale Insights plugin that provides query performance monitoring and analysis capabilities. This extension is always enabled for PlanetScale databases and integrates with the Query Insights feature.

## Dashboard Configuration

This extension is always enabled for PlanetScale databases and requires activation via the PlanetScale Dashboard. While the extension itself is always active, some of its parameters can be configured through the dashboard.

To configure pginsights parameters:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Clusters** page from the menu on the left</Step>
  <Step>Choose the branch whose extensions you'd like to configure in the "**Branch**" dropdown</Step>
  <Step>Select the **Extensions** tab</Step>
  <Step>Enable pginsights and configure its parameters</Step>
  <Step>Click **Queue extension changes** to apply the configuration</Step>
  <Step>Once you're ready to apply the changes, click "**Apply changes**"</Step>
</Steps>

## Parameters

### pginsights.raw\_queries

* **Type**: Boolean
* **Default**: `false`
* **Description**: Send full query text for slow, large, or failed queries (may include sensitive data).
* **Documentation**: [Raw Query Collection](/docs/postgres/monitoring/query-insights#raw-query-collection)

### pginsights.normalize\_schema\_names

* **Type**: Boolean
* **Default**: `false`
* **Description**: Merge queries patterns that differ only by schema name.
* **Documentation**: [Schema Name Normalization](/docs/postgres/monitoring/query-insights#schema-name-normalization)

## Usage

The pginsights extension is automatically installed and enabled for all PlanetScale databases. You don't need to manually create the extension - it's always active and collecting query insights.

The extension integrates with PlanetScale's Query Insights dashboard to provide:

* Query performance metrics
* Slow query identification
* Query pattern analysis
* Resource usage tracking

## External Documentation

For more information about Query Insights and how to use the collected data, see the [Query Insights documentation](/docs/postgres/monitoring/query-insights).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt