# Source: https://docs.newrelic.com/docs/query-your-data/explore-query-data/get-started/introduction-querying-new-relic-data/

Title: How to query your New Relic data

URL Source: https://docs.newrelic.com/docs/query-your-data/explore-query-data/get-started/introduction-querying-new-relic-data/

Markdown Content:
[New Relic](https://one.newrelic.com/) is a powerful observability platform that gives you access to all your data throughout your entire system. We host telemetry data sent by [your entities](https://docs.newrelic.com/docs/new-relic-one/use-new-relic-one/core-concepts/what-entity-new-relic/), which basically is anything we can identify that has data you can monitor, including applications, services, hosts, etc. You name it!

While we provide you with an out of the box experience to see your data with curated [dashboards](https://docs.newrelic.com/docs/query-your-data/explore-query-data/dashboards/introduction-dashboards/), you can tailor the access to your data and custom the visibility in several ways, including [in the UI](https://docs.newrelic.com/docs/query-your-data/explore-query-data/get-started/introduction-querying-new-relic-data/#query-ui) or [via API](https://docs.newrelic.com/docs/query-your-data/explore-query-data/get-started/introduction-querying-new-relic-data/#query-apis).

#### Important

To better understand your data stored in New Relic, see [Data types](https://docs.newrelic.com/docs/using-new-relic/data/understand-data/new-relic-data-types/).

Our open door to your data
--------------------------

Regardless of your experience with New Relic, we'll help you discover, understand and visualize your data.

| You... | Then do this... |
| --- | --- |
| Just installed an agent and want to see your data in New Relic. | [Browse your data](https://docs.newrelic.com/docs/query-your-data/explore-query-data/get-started/introduction-querying-new-relic-data/#browse-data) easily without building queries. With [metrics and events](https://docs.newrelic.com/docs/query-your-data/explore-query-data/data-explorer/introduction-data-explorer/), you can understand the data we’ve stored, see its cardinality, or build charts in a few clicks. |
| Know what data is available, but you want to understand more about what else is coming with that data. | If you're an advanced user, use our [query builder](https://docs.newrelic.com/docs/chart-builder/use-chart-builder/choose-data/use-advanced-nrql-mode-specify-data/) to tailor the data you want to retrieve. |
| Want to build a dashboard. | Create a [custom dashboard](https://docs.newrelic.com/docs/query-your-data/explore-query-data/dashboards/introduction-dashboards/) from metrics and events or the query builder. |
| Want more options for querying than the UI query builder provides. | Use [our NerdGraph API](https://docs.newrelic.com/docs/apis/nerdgraph/examples/nerdgraph-nrql-tutorial/), which has more features, such as cross-account querying and historical data export. |

Browse your data in the UI
--------------------------

Our platform offers several experiences that don't require knowledge of NRQL or any query language:

*   To explore your New Relic data, you can use the [Data Explorer](https://docs.newrelic.com/docs/query-your-data/explore-query-data/browse-data/introduction-data-explorer/), an intuitive data navigator for exploring data and creating visualizations. You can also use the [query builder](https://docs.newrelic.com/docs/query-your-data/explore-query-data/query-builder/introduction-query-builder/) to refine your query.
*   To explore your trace data, you can use the [distributed tracing query](https://docs.newrelic.com/docs/understand-dependencies/distributed-tracing/ui-data/additional-distributed-tracing-features-new-relic-one/).
*   To explore logs, you can use the [logs UI](https://docs.newrelic.com/docs/logs/ui-data/use-logs-ui/).

Query data in the UI
--------------------

If you're ready to do more than browsing data, become an all-hands actor and personalize your queries in the New Relic UI. Use query languages, including our [New Relic query language](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/introduction-nrql-new-relics-query-language/) or [our PromQL-style query language](https://prometheus.io/docs/prometheus/latest/querying/basics/), to edit queries with full flexibility. For example, you can add more [`WHERE` clauses](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/nrql-syntax-clauses-functions/#sel-where), modify the returned value, change to [other types of visualizations](https://docs.newrelic.com/docs/query-your-data/explore-query-data/use-charts/chart-types/), etc.

There are two ways to write your own queries to retrieve data and build charts:

*   [Query builder in NRQL mode](https://docs.newrelic.com/docs/chart-builder/use-chart-builder/choose-data/use-advanced-nrql-mode-specify-data/): Query using [New Relic query language](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/introduction-nrql-new-relics-query-language/) (NRQL), the same language we use to build most of our UI experiences, and the most advanced way of querying data in New Relic.
*   [Query builder in PromQL-style mode](https://docs.newrelic.com/docs/query-your-data/explore-query-data/chart-builder/use-advanced-promql-mode-specify-data/): Write queries using a PromQL-style query.

You can also [query data from your IDE](https://docs.newrelic.com/docs/codestream/observability/query-builder/) using New Relic's CodeStream extension.

Query data via API
------------------

When you need programmatic options, or want to unlock more querying power, you can use APIs to query your New Relic data. Our NerdGraph API gives you more powerful options not available in the UI, such as querying across accounts, and exporting longer-term historical data sets. For more information, see [Intro to NerdGraph](https://docs.newrelic.com/docs/apis/nerdgraph/get-started/introduction-new-relic-nerdgraph/#tutorials).
