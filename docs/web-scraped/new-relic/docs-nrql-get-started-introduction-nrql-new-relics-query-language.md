# Source: https://docs.newrelic.com/docs/nrql/get-started/introduction-nrql-new-relics-query-language/

Title: Get started with NRQL: the language of data

URL Source: https://docs.newrelic.com/docs/nrql/get-started/introduction-nrql-new-relics-query-language/

Markdown Content:
The New Relic Query Language (NRQL) is a powerful tool you can use to [query](https://docs.newrelic.com/docs/using-new-relic/data/understand-data/query-new-relic-data/) and understand nearly any type of data, but it can seem overwhelming at first glance. Don't worry! Here's some information to give you a foundational understanding of NRQL, including what it is, how to use it, and some tips and tricks that will help you get the most out of your queries. Once you've learned about NRQL, you can capture and interpret your data, letting you break down the big picture into easily understandable pieces and helping you identify problems as they occur.

Here's a quick video to help introduce you to using NRQL by showing you how to find a query from a [dashboard](https://docs.newrelic.com/docs/query-your-data/explore-query-data/dashboards/introduction-dashboards/) and modify it in the [query builder](https://docs.newrelic.com/docs/query-your-data/explore-query-data/query-builder/introduction-query-builder/). For more detailed information on querying, including a listing of clauses, functions, and example queries, see our [NRQL reference](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/nrql-syntax-clauses-functions/).

What is NRQL?
-------------

NRQL is an acronym of New Relic query language. It's a query language similar to ANSI SQL ([see the syntax](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/introduction-nrql-how-nrql-works/#syntax)), and you can use it to retrieve detailed New Relic data to get insight into your applications, hosts, and business-important activity. NRQL can help you:

*   Create a new chart
*   Answer a specific question for the purpose of troubleshooting or business analysis
*   Set up [NRQL-based alerts](https://docs.newrelic.com/docs/alerts-applied-intelligence/new-relic-alerts/alert-conditions/create-nrql-alert-conditions/) (our primary and most powerful type of alert)
*   Make API queries of New Relic data (for example, using our [NerdGraph](https://docs.newrelic.com/docs/apis/graphql-api/tutorials/nerdgraph-graphiql-nrql-tutorial/) API)

You can use NRQL to create simple queries, such as fetching rows of data in a raw tabular form that gives insight on individual events. You can also use NRQL to run powerful calculations on the data before it's presented to you, such as crafting funnels based on how end users interact with your site or application.

We use NRQL behind the scenes to generate many of the charts and dashboards in our curated UI experiences.

Where can you use NRQL?
-----------------------

You can use NRQL across the platform to access your data. Those places include:

#### Tip

NRQL is one of several ways to query New Relic data. For more on all query options, see [Query your data](https://docs.newrelic.com/docs/using-new-relic/data/understand-data/query-new-relic-data/).

How is NRQL structured?
-----------------------

If you're already familiar with writing SQL queries, you'll be happy to know that NRQL has a lot of similarities. Here's a quick breakdown of the structure of a NRQL query:

Here are the rules that NRQL follows:

| **NRQL rule** | Details |
| --- | --- |
| Required values | The [`SELECT`](https://docs.newrelic.com/docs/nrql/get-started/introduction-nrql-new-relics-query-language/#state-select) clause and [`FROM`](https://docs.newrelic.com/docs/nrql/get-started/introduction-nrql-new-relics-query-language/#sel-from) clause are required. All other clauses are optional. You can start your query with either `SELECT` or `FROM`. |
| Query string size | The query string must be less than 4 KB. |
| Case sensitivity | * The data type names and attribute names are case sensitive. * [NRQL clauses](https://docs.newrelic.com/docs/insights/new-relic-insights/using-new-relic-query-language/nrql-reference/#clauses) and [functions](https://docs.newrelic.com/docs/insights/new-relic-insights/using-new-relic-query-language/nrql-reference/#functions) are not case sensitive. |
| Syntax for strings | NRQL uses single quotes to designate strings. For example: `... WHERE traceId = '030a573f0df02c57'` |
| Non-standard custom event and attribute names | Events that we report by default have names that contain alphanumeric characters, colons (`:`), and underscores (`_`). Attribute names can have those characters and periods (`.`). Default-reported names start with a letter. Custom names that don't follow these guidelines must be enclosed with backticks in NRQL queries. For example: `... FACET `Logged-in user`` |
| Data type coercion | We don't support data type "coercion." For more information, see [Data type conversion](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/nrql-reference/nrql-syntax-components-functions/#type-conversion). |

If you need any more information, you can check out our [NRQL reference](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/nrql-syntax-clauses-functions/) to help you build your queries.

What data can you query with NRQL?
----------------------------------

NRQL lets you query nearly every type of our telemetry data, including:

*   [Event data](https://docs.newrelic.com/docs/using-new-relic/data/understand-data/new-relic-data-types/#event-data) from all New Relic products. Examples include:
    *   [APM events](https://docs.newrelic.com/docs/insights/insights-data-sources/default-data/apm-default-events-insights/), like `Transaction`
    *   [Browser monitoring events](https://docs.newrelic.com/docs/insights/insights-data-sources/default-data/browser-default-events-insights/), like `PageView`
    *   [Mobile monitoring events](https://docs.newrelic.com/docs/insights/insights-data-sources/default-data/mobile-default-events-insights/), like `Mobile`
    *   [Infrastructure events](https://docs.newrelic.com/docs/infrastructure/manage-your-data/data-instrumentation/default-infrastructure-events/), like `ProcessSample`
    *   [Synthetic events](https://docs.newrelic.com/docs/insights/insights-data-sources/default-data/synthetics-default-events-insights/), like `SyntheticCheck`
    *   Custom events, like those reported by the [Event API](https://docs.newrelic.com/docs/insights/insights-data-sources/custom-data/introduction-event-api/)

*   [Metric timeslice data](https://docs.newrelic.com/docs/using-new-relic/data/understand-data/new-relic-data-types/#timeslice-data) (metrics reported by APM)
*   The [`Metric` data type](https://docs.newrelic.com/docs/data-apis/understand-data/new-relic-data-types/#dimensional-metrics) (metrics reported by the Metric API and data sources that use that API)
*   The [`Span` data type](https://docs.newrelic.com/docs/using-new-relic/data/understand-data/new-relic-data-types/#trace-data) (distributed tracing data)
*   The [`Log` data type](https://docs.newrelic.com/docs/using-new-relic/data/understand-data/new-relic-data-types/#log-data) (data from our log management capabilities)

#### Tip

Some data, like relationships between monitored entities, is not available via NRQL but is available using our [NerdGraph API](https://docs.newrelic.com/docs/apis/nerdgraph/get-started/introduction-new-relic-nerdgraph/).

Ready to learn more? We have information on [how to use NRQL](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/introduction-nrql-how-nrql-works/) and [how to use charts and dashboards with NRQL](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/charts-and-dashboards-with-nrql/). If you want to start using NRQL instead, jump straight into our [guided NRQL tutorial](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/introduction-nrql-tutorial/).
