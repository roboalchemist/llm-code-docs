# Source: https://docs.statsig.com/infra-analytics/logs-explorer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Logs Explorer Overview

> Search and analyze all of your product’s logs in one place.

Logs Explorer lets you query logs, traces, and ingested events from a single interface. Use it the same way whether you’re debugging infrastructure issues or investigating product event streams.

* **Search**: Slice logs down to only what's relevant (by service, host, status code, etc.)
* **Group**: Aggregate logs by dimensions like region, status, or browser.
* **Visualize**: Plot log groupings over time to spot spikes, regressions, or anomalies instantly.

***

### Getting Started with Log Explorer

To get started with Log Explorer, follow the [OTEL onboarding guide](/infra-analytics/getting-started.mdx) to set up log ingestion. Once that's ready, you can navigate from **Infra Analytics → Log Explorer** from the Statsig left menu.

You can also use Logs Explorer in [Events Mode](/infra-analytics/events-mode-logs-explorer) to search and analyze your existing Statsig Events — no additional instrumentation needed. You can switch between Logs and Events mode using the dropdown left of the search bar.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/2n-l9m8AAwu0tPze/images/infra-analytics/lex-toggle.png?fit=max&auto=format&n=2n-l9m8AAwu0tPze&q=85&s=7aadc3a953d1947ecf182b8234f40074" alt="Logs Explorer Switch Mode" width="666" height="428" data-path="images/infra-analytics/lex-toggle.png" />
</Frame>

***

### Searching in Logs Explorer

* **Write custom queries**: Check out our [syntax guide](/infra-analytics/logs-explorer-queries) to craft your search
* **Using the query builder**: Point-and-click to construct filters without syntax overhead.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/infra-analytics/logs-explorer-1.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=40581f6c91a1ed66b57c6be481d83508" alt="Logs Explorer Overview" width="1581" height="755" data-path="images/infra-analytics/logs-explorer-1.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).