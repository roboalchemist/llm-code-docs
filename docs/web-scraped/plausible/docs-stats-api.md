# Source: https://plausible.io/docs/stats-api

Title: Stats API reference | Plausible docs

URL Source: https://plausible.io/docs/stats-api

Published Time: Wed, 11 Mar 2026 09:21:49 GMT

Markdown Content:
Plausible Stats API is a powerful single endpoint HTTP interface to **view historical and real-time stats**. In a nutshell, the endpoint `/api/v2/query` accepts both simple and complex stats queries in the POST request body and returns the metrics as JSON.

[Try it now for your own site!](https://plausible.io/docs/stats-api#examples)

Authentication[​](https://plausible.io/docs/stats-api#authentication "Direct link to Authentication")
-----------------------------------------------------------------------------------------------------

To create a new stats API key, log in to your Plausible Analytics account. In the top-right menu, click on your account name and go to settings.

Next, go to the "**API Keys**" section in the left-hand sidebar. Click the "**New API Key**" button, choose "**Stats API**" and save the key as it will only be shown once. After saving the key, click on "**Create API Key**" to confirm its creation.

After creating an API key, you can authenticate your request by sending the key in the Authorization header of your request.

### Example curl request[​](https://plausible.io/docs/stats-api#example-curl-request "Direct link to Example curl request")

In the following request, replace `YOUR-KEY` with a reference to your stats API key and `site_id` value with your domain as you've added it to your Plausible account.

`curl \--request POST \--header 'Authorization: Bearer YOUR-KEY' \--header 'Content-Type: application/json' \--url 'https://plausible.io/api/v2/query' \--data '{ "site_id": "dummy.site", "metrics": ["visitors"], "date_range": "7d" }'`

API keys have a rate limit of 600 requests per hour by default. If you have special needs for more requests, [please contact us](https://plausible.io/contact) to request more capacity.

Request structure[​](https://plausible.io/docs/stats-api#request-structure "Direct link to Request structure")
--------------------------------------------------------------------------------------------------------------

`/api/v2/query` endpoint accepts a `query` object. Example:

`{  "site_id": "dummy.site",  "metrics": ["visitors", "pageviews", "bounce_rate"],  "date_range": "7d",  "filters": [    ["is_not", "visit:country_name", [""]]  ],  "dimensions": ["visit:country_name", "visit:city_name"]}`

Query can contain the following keys:

### site_id REQUIRED[​](https://plausible.io/docs/stats-api#site_id- "Direct link to site_id-")

Domain of your site on Plausible to be queried.

### date_range REQUIRED[​](https://plausible.io/docs/stats-api#date_range "Direct link to date_range")

Date range to be queried.

| Option | Description |
| --- | --- |
| `["2024-01-01", "2024-07-01"]` | Custom date range (ISO8601) |
| `["2024-01-01T12:00:00+02:00", "2024-01-01T15:59:59+02:00"]` | Custom date-time range (ISO8601) |
| `["2024-01-01T12:00:00+02:00", "2024-01-01T12:05:00+02:00"]` | Real time |
| `"day"` | Current day (e.g. 2024-07-01) |
| `"24h"` | Last 24 hours relative to now |
| `"7d"` | Last 7 days relative to today |
| `"28d"` | Last 28 days relative to today |
| `"30d"` | Last 30 days relative to today |
| `"91d"` | Last 91 days relative to today |
| `"month"` | Since the start of the current month |
| `"6mo"` | Last 6 months relative to start of this month |
| `"12mo"` | Last 12 months relative to start of this month |
| `"year"` | Since the start of this year |
| `"all"` | Since the start of stats in Plausible |

### metrics REQUIRED[​](https://plausible.io/docs/stats-api#metrics "Direct link to metrics")

Metrics represent values to be calculated with the query.

Valid metrics are:

| Metric name | Type | Description | Requirements |
| --- | --- | --- | --- |
| `visitors` | `int` | The number of unique visitors |  |
| `visits` | `int` | The number of visits/sessions |  |
| `pageviews` | `int` | The number of pageview events |  |
| `views_per_visit` | `float` | The number of pageviews divided by the number of visits. |  |
| `bounce_rate` | `float` | Bounce rate percentage |  |
| `visit_duration` | `int` | Visit duration in seconds |  |
| `events` | `int` | The number of events (pageviews + custom events). When filtering by a goal, this metric corresponds to "Total Conversions" in the dashboard. |  |
| `scroll_depth` | `int` | Page scroll depth averaged per session | Requires `event:page` filter or dimension being set |
| `percentage` | `float` | The percentage of visitors of total who fall into this category | Requires non-empty `dimensions` |
| `conversion_rate` | `float` | The percentage of visitors who completed the goal. The number of total visitors (divisor) gets calculated across all dimensions. | Requires `event:goal` filter or dimension being set. |
| `group_conversion_rate` | `float` | The percentage of visitors who completed the goal with the same dimension. The number of total visitors (divisor) gets calculated for each dimension group individually. | Requires `event:goal` filter or dimension being set. |
| `average_revenue` | `Revenue` or null | Average revenue per revenue goal conversion | Requires [revenue goals](https://plausible.io/docs/ecommerce-revenue-tracking), `event:goal` filter or dimension for a relevant revenue goal. |
| `total_revenue` | `Revenue` or null | Total revenue from revenue goal conversions | Requires [revenue goals](https://plausible.io/docs/ecommerce-revenue-tracking), `event:goal` filter or dimension for a relevant revenue goal. |
| `time_on_page` | `int` | Average time in seconds spent on a page per visit | Requires `event:page` filter or dimension being set. |

Read more about revenue metrics

### dimensions optional[​](https://plausible.io/docs/stats-api#dimensions "Direct link to dimensions")

Default: `[]`

List of dimensions to group by. [See example](https://plausible.io/docs/stats-api#example-utm)

Dimensions are attributes of your dataset. Using them in queries enables analyzing and compare multiple groups against each other. Think of them as `GROUP BY` in SQL.

#### Event dimensions[​](https://plausible.io/docs/stats-api#event-dimensions "Direct link to Event dimensions")

Valid dimensions include:

| Dimension | Example | Description |
| --- | --- | --- |
| `event:goal` | Register | A custom action that you want your users to take. To use this property, you first need to configure some goals in the [site settings](https://plausible.io/docs/website-settings), or via the [Sites API](https://plausible.io/docs/sites-api). The value is the goal's `display_name`. Learn more about goals [here](https://plausible.io/docs/goal-conversions). |
| `event:page` | /blog/remove-google-analytics | Pathname of the page where the event is triggered. You can also use an asterisk to group multiple pages (`/blog*`) |
| `event:hostname` | example.com | Hostname of the event. |

warning

Mixing session metrics `bounce_rate`, `views_per_visit` and `visit_duration` with event dimensions is not allowed.

#### Visit dimensions[​](https://plausible.io/docs/stats-api#visit-dimensions "Direct link to Visit dimensions")

Values of these dimensions are determined by the first pageview in a session.

| Dimension | Example | Description |
| --- | --- | --- |
| `visit:entry_page` | /home | Page on which the visit session started (landing page). |
| `visit:exit_page` | /home | Page on which the visit session ended (last page viewed). |
| `visit:source` | Twitter | Visit source, populated from an url query parameter tag (`utm_source`,`source`or`ref`) or the Referer HTTP header. |
| `visit:referrer` | t.co/fzWTE9OTPt | Raw`Referer`header without`http://`,`http://`or `www.`. |
| `visit:channel` | Organic Search | Acquisition channel for visit. |
| `visit:utm_medium` | social | Raw value of the`utm_medium`query param on the entry page. |
| `visit:utm_source` | twitter | Raw value of the`utm_source`query param on the entry page. |
| `visit:utm_campaign` | profile | Raw value of the`utm_campaign`query param on the entry page. |
| `visit:utm_content` | banner | Raw value of the`utm_content`query param on the entry page. |
| `visit:utm_term` | keyword | Raw value of the`utm_term`query param on the entry page. |
| `visit:device` | Desktop | Device type. Possible values are `Desktop`, `Laptop`, `Tablet` and `Mobile`. |
| `visit:browser` | Chrome | Name of the browser vendor. Most popular ones are `Chrome`, `Safari` and `Firefox`. |
| `visit:browser_version` | 88.0.4324.146 | Version number of the browser used by the visitor. |
| `visit:os` | Mac | Name of the operating system. Most popular ones are `Mac`, `Windows`, `iOS` and `Android`. Linux distributions are reported separately. |
| `visit:os_version` | 10.6 | Version number of the operating system used by the visitor. |
| `visit:country` | US | ISO 3166-1 alpha-2 code of the visitor country. |
| `visit:region` | US-MD | ISO 3166-2 code of the visitor region. |
| `visit:city` | 4347778 | [GeoName ID](https://www.geonames.org/) of the visitor. |
| `visit:country_name` | United States | Name of the visitor country. |
| `visit:region_name` | California | Name of the visitor region. |
| `visit:city_name` | San Francisco | Name of the visitor city. |

#### Time dimensions[​](https://plausible.io/docs/stats-api#time-dimensions "Direct link to Time dimensions")

It's useful to be able to group data by time, which can be done via the following dimensions.

| Dimension | Example | Description |
| --- | --- | --- |
| `time` | `2024-01-01` | Time or date to group by. Automatically figures out the appropriate time:bucket value from date range. Response is a valid ISO8601 date or timestamp |
| `time:hour` | `2021-01-27 23:43:10` | Time grouped by hour. |
| `time:day` | `2021-01-27` | Time grouped by date. ISO8601 date |
| `time:week` | `2021-01-04` | Time grouped by start of the week. ISO8601 date |
| `time:month` | `2021-01-01` | Time grouped by start of month. ISO8601 date |

Note that:

*   `time` dimensions are not usable in filters. Set [`date_range`](https://plausible.io/docs/stats-api#date_range) instead.
*   If no data falls into a given time bucket, no values are returned. [See `include.time_labels` option](https://plausible.io/docs/stats-api#time-labels) for a workaround.
*   These dates and timestamps are reported in sites Reporting Timezone.

[See example](https://plausible.io/docs/stats-api#example-timeseries)

#### Custom properties[​](https://plausible.io/docs/stats-api#custom-properties "Direct link to Custom properties")

[Custom properties](https://plausible.io/docs/custom-props/introduction) can also be used as dimensions with the form `event:props:<custom_prop_name>`. [See example](https://plausible.io/docs/stats-api#example-custom-properties)

### filters optional[​](https://plausible.io/docs/stats-api#filters- "Direct link to filters-")

Default: `[]`

Filters allow limiting which events or sessions are included in the query. [See example](https://plausible.io/docs/stats-api#example-filtering).

#### Simple filters[​](https://plausible.io/docs/stats-api#simple-filters "Direct link to Simple filters")

Each simple filter is an array with three or four elements `[operator, dimension, clauses]` or `[operator, dimension, clauses, modifiers]`.

##### operators[​](https://plausible.io/docs/stats-api#operators "Direct link to operators")

The following operators are currently supported:

| Operator | Example | Explanation |
| --- | --- | --- |
| `is` | `["is", "visit:country_name", ["Germany", "Poland"]]` | Sessions originating from Germany or Poland. |
| `is_not` | `["is_not", "event:page", ["/pricing"]]` | Events that did not visit /pricing page |
| `contains` | `["contains", "event:page", ["/login"]]` | Events visited any page containing /login |
| `contains_not` | `["contains_not", "event:page", ["docs", "pricing"]]` | Events that did not visit any page containing docs or pricing |
| `matches` | `["matches", "event:page", ["^/user/\d+$"]]` | Events where page matches regular expression `^/user/\d+$`. [Uses re2 syntax](https://github.com/google/re2/wiki/Syntax) |
| `matches_not` | `["matches", "event:page", ["^/user/\d+$"]]` | Events where page does not match regular expression `^/user/\d+$`. [Uses re2 syntax](https://github.com/google/re2/wiki/Syntax) |

##### dimension[​](https://plausible.io/docs/stats-api#dimension "Direct link to dimension")

[Event and visit dimensions](https://plausible.io/docs/stats-api#dimensions) are valid for filters.

Note that only `is` and `contains` operators are valid for `event:goal` dimension.

##### clauses[​](https://plausible.io/docs/stats-api#clauses "Direct link to clauses")

List of values to match against. A data point matches filter if _any_ of the clauses matches.

##### modifiers optional[​](https://plausible.io/docs/stats-api#modifiers- "Direct link to modifiers-")

`contains` and `is` filters also support a 4th, modifier argument. For example, to match countries ignoring casing, you can use the following filter:

`["contains", "event:country", ["united", "EST], { "case_sensitive": false }]`. [See full example](https://plausible.io/docs/stats-api#example-filtering-case-insensitive)

#### Logical operations[​](https://plausible.io/docs/stats-api#logical-operations "Direct link to Logical operations")

Filters can be combined using `and`, `or` and `not` operators.

| Operator | Example | Explanation |
| --- | --- | --- |
| `and` | `["and", [["is", "visit:country_name", ["Germany"]], ["is", "visit:city_name", ["Berlin"]]]]` | Sessions originating from Berlin, Germany |
| `or` | `["or", [["is", "visit:country_name", ["Germany"]], ["is", "visit:city_name", ["Tallinn"]]]]` | Sessions originating from Germany or city of Tallinn |
| `not` | `["not", ["is", "visit:country_name", ["Germany"]]]` | Sessions not originating from Germany |

Note that top level filters is wrapped in an implicit `and`.

#### Behavioral filters[​](https://plausible.io/docs/stats-api#behavioral-filters "Direct link to Behavioral filters")

When filtering by multiple simple event dimension(s), our Stats API selects only events which match all event filters. This means that it's not possible to filter sessions based on whether multiple (separate) events occurred.

For this usecase, `has_done` and `has_not_done` operators allow filtering sessions based on whether another event occurred within it or not.

[See example](https://plausible.io/docs/stats-api#example-behavioral-filters)

#### Segments[​](https://plausible.io/docs/stats-api#segments "Direct link to Segments")

[Segments](https://plausible.io/docs/filters-segments#how-to-save-a-segment) can be used in filters, in the form `["is", "segment", [<segment_id>]]`. [See example](https://plausible.io/docs/stats-api#example-filtering-by-segment)

### order_by optional[​](https://plausible.io/docs/stats-api#order_by- "Direct link to order_by-")

Allows for custom ordering of query results.

List of tuples `[dimension_or_metric, direction]`, where:

*   `dimension_or_metric` needs to be listed in query [`metrics`](https://plausible.io/docs/stats-api#metrics) or [`dimensions`](https://plausible.io/docs/stats-api#dimensions) respectively.
*   `direction` can be one of `"asc"` or `"desc"`

For example:

`[["visitors", "desc"], ["visit:country_name", "asc"]]`

When not specified, the default ordering is:

1.   If a [time dimensions](https://plausible.io/docs/stats-api#time-dimensions) is present, `[time_dimension, "asc"]`
2.   By the first metric specified, descending.

[See full query example](https://plausible.io/docs/stats-api#example-custom-properties)

### include optional[​](https://plausible.io/docs/stats-api#include- "Direct link to include-")

Default: `{}`

Additional options for the query as to what data to include.

#### include.imports[​](https://plausible.io/docs/stats-api#include.imports "Direct link to include.imports")

Default: `false`

If true, tries to include imported data in the result. See [imported stats](https://plausible.io/docs/stats-api#imported-stats) for more details, [query example](https://plausible.io/docs/stats-api#example-imports).

Read more on limitations of including imported data

If set, `meta.imports_included` field will be set as a boolean.

If the applied combination of filters and dimensions is not supported for imported stats, the results are still returned based only on native stats. Additionally, `meta.imports_skip_reason` and `meta.imports_warning` response fields will contain more information on why including imported data failed. [See example](https://plausible.io/docs/stats-api#example-imports-warning)

#### include.time_labels[​](https://plausible.io/docs/stats-api#include.time_labels "Direct link to include.time_labels")

Default: `false`

Requires a `time` dimension being set. If true, sets `meta.time_labels` in response containing all time labels valid for `date_range`.

[See example](https://plausible.io/docs/stats-api#example-time-labels)

#### include.total_rows[​](https://plausible.io/docs/stats-api#include.total_rows "Direct link to include.total_rows")

Default: `false`

Should be used for [pagination](https://plausible.io/docs/stats-api#pagination). If true, sets `meta.total_rows` in response containing the total number of rows for this query.

[See example](https://plausible.io/docs/stats-api#example-pagination)

Default: `{ "limit": 10000, "offset: 0 }`

[See example](https://plausible.io/docs/stats-api#example-pagination)

Response structure[​](https://plausible.io/docs/stats-api#response-structure "Direct link to Response structure")
-----------------------------------------------------------------------------------------------------------------

Example response:

`{  "results": [    {"metrics": [99, 98, 94], "dimensions": ["Estonia", "Tallinn"]},    {"metrics": [98, 82, 97], "dimensions": ["Brazil", "São Paulo"]},    {"metrics": [97, 77, 98], "dimensions": ["Germany", "Berlin"]},    {"metrics": [94, 86, 93], "dimensions": ["Italy", "Rome"]},    {"metrics": [89, 77, 96], "dimensions": ["United States", "San Francisco"]},    {"metrics": [82, 78, 92], "dimensions": ["Poland", "Warsaw"]}  ],  "meta": {},  "query": {    "site_id": "dummy.site",    "metrics": ["visitors", "pageviews", "bounce_rate"],    "date_range": ["2024-09-04T00:00:00+00:00", "2024-09-10T23:59:59+00:00"],    "filters": [["is_not", "visit:country_name", [""]]],    "dimensions": ["visit:country_name", "visit:city_name"],    "order_by": [["visitors", "desc"]],    "include": {}  }}`

### results[​](https://plausible.io/docs/stats-api#results "Direct link to results")

Results is an ordered list query results.

Each result row contains:

*   `dimensions` - values for each `dimension` listed in query. In the same order as query `dimensions`, empty if no dimensions requested.
*   `metrics` - List of metric values, in the same order as query `metrics`

### meta[​](https://plausible.io/docs/stats-api#meta "Direct link to meta")

Meta information about this query, including warnings and auxiliary data. Related: [include](https://plausible.io/docs/stats-api#include).

`{  // Whether imported data was included  // Only set if include.imports was set  "imports_included": false,  // Information about why including imported data failed  "imports_skip_reason": "unsupported_interval",  "imports_warning": "Imported stats are not included because the time dimension (i.e. the interval) is too short.",  // Warnings about specific metrics  // Currently only set if a revenue metric was used and was unable to be calculated  "metric_warnings": {    "total_revenue": {      "code": "no_revenue_goals_matching",      "warning": "Revenue metrics are null as there are no matching revenue goals."    }  },  // Only set if include.time_labels was set  "time_labels": [    "2024-09-10 00:00:00",    "2024-09-10 01:00:00",    "2024-09-10 02:00:00",    "2024-09-10 03:00:00",    "2024-09-10 04:00:00",    "2024-09-10 05:00:00",    "2024-09-10 06:00:00"  ],  // Only set if include.total_rows was set  "total_rows": 342}`

### query[​](https://plausible.io/docs/stats-api#query "Direct link to query")

The query that was executed, after manipulations performed on the backend.

Looking for legacy stats API v1 docs?

Examples[​](https://plausible.io/docs/stats-api#examples "Direct link to Examples")
-----------------------------------------------------------------------------------

The following examples are interactive and can be edited and run against your own data if you're logged in.

### Simple aggregate query[​](https://plausible.io/docs/stats-api#example-aggregate "Direct link to Simple aggregate query")

*   Query
*   Example Response

### Custom date range[​](https://plausible.io/docs/stats-api#example-custom-date-range "Direct link to Custom date range")

*   Query
*   Example Response

### Country and city analysis[​](https://plausible.io/docs/stats-api#example-country-and-city "Direct link to Country and city analysis")

*   Query
*   Example Response

### UTM medium, source analysis[​](https://plausible.io/docs/stats-api#example-utm "Direct link to UTM medium, source analysis")

*   Query
*   Example Response

### Filtering by page and country[​](https://plausible.io/docs/stats-api#example-filtering "Direct link to Filtering by page and country")

*   Query
*   Example Response

### Case insensitive filtering[​](https://plausible.io/docs/stats-api#example-filtering-case-insensitive "Direct link to Case insensitive filtering")

*   Query
*   Example Response

### Filtering by segment[​](https://plausible.io/docs/stats-api#example-filtering-by-segment "Direct link to Filtering by segment")

*   Query
*   Example Response

### Timeseries query[​](https://plausible.io/docs/stats-api#example-timeseries "Direct link to Timeseries query")

*   Query
*   Example Response

### Timeseries query hourly, with labels[​](https://plausible.io/docs/stats-api#example-time-labels "Direct link to Timeseries query hourly, with labels")

*   Query
*   Example Response

### Using custom properties[​](https://plausible.io/docs/stats-api#example-custom-properties "Direct link to Using custom properties")

*   Query
*   Example Response

*   Query
*   Example Response

### Including imported data[​](https://plausible.io/docs/stats-api#example-imports "Direct link to Including imported data")

*   Query
*   Example Response

### Including imported data failed[​](https://plausible.io/docs/stats-api#example-imports-warning "Direct link to Including imported data failed")

In this example, imported data could not be included due to dimension and filter combination not supporting imports. [More information](https://plausible.io/docs/stats-api#include.imports)

*   Query
*   Example Response

### Revenue metrics[​](https://plausible.io/docs/stats-api#example-revenue-metrics "Direct link to Revenue metrics")

*   Query
*   Example Response

### Revenue metrics could not be calculated[​](https://plausible.io/docs/stats-api#example-revenue-warning "Direct link to Revenue metrics could not be calculated")

In this example, revenue metrics could not be calculated due to different currency filters. [More information](https://plausible.io/docs/stats-api#metrics)

*   Query
*   Example Response

### Behavioral filters[​](https://plausible.io/docs/stats-api#example-behavioral-filters "Direct link to Behavioral filters")

In this example, we're counting goal completions for a goal named "Signup" for users who visited the `/pricing` page.

*   Query
*   Example Response

Quirks[​](https://plausible.io/docs/stats-api#quirks "Direct link to Quirks")
-----------------------------------------------------------------------------

The stats API is created to be able to both pragmatically and performantly query the underlying dataset Plausible stores. To make it possible, the API has certain limitations and quirks. These include:

### Imported data can not always be included[​](https://plausible.io/docs/stats-api#imported-data-can-not-always-be-included "Direct link to Imported data can not always be included")

As imported data from Google Analytics or other sources is stored as aggregates, responses for queries with certain metrics, filters and dimensions may not contain imported data. [See example](https://plausible.io/docs/stats-api#example-imports-warning)

### Metric values may change depending on metrics requested[​](https://plausible.io/docs/stats-api#metric-values-may-change-depending-on-metrics-requested "Direct link to Metric values may change depending on metrics requested")

When requesting metrics such as `visits` or `visitors`, the system may use different database tables depending on your query and use different heuristics to calculate values. As such, the value may slightly change depending on the result.

Our testing has shown this to be a small effect (less than 1 percent).
