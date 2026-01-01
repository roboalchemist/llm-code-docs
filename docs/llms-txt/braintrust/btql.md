# Source: https://braintrust.dev/docs/reference/btql.md

# Braintrust Query Language (BTQL)

Braintrust Query Language (BTQL) is a precise, SQL-like syntax for querying Braintrust experiments, logs, and datasets. Use BTQL to better analyze and understand your data.

BTQL supports two syntax styles: the native **BTQL syntax** with pipe-delimited clauses, and standard **SQL syntax**. The parser automatically detects which style you're using.

## Why use BTQL?

BTQL gives you precise control over your AI application data. You can:

* Filter and search for relevant logs and experiments
* Create consistent, reusable queries for monitoring
* Build automated reporting and analysis pipelines
* Write complex queries to analyze model performance

## BTQL in Braintrust

Use BTQL when filtering logs and experiments, in the BTQL sandbox, and programmatically through the Braintrust API.

### Filter logs and experiments

Use BTQL to filter logs and experiments based on specific criteria. You can filter logs by tags, metadata, or any other relevant fields. Filtering in logs and experiments only supports [`filter` clauses](#filter).

At the top of your experiment or log view, select **Filter** to open the filter editor and select **BTQL** to switch to BTQL mode.

<img src="https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-filter.png?fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=c3509fec166dbfddb2d4d5b6588c35af" alt="BTQL filter editor" data-og-width="511" width="511" data-og-height="203" height="203" data-path="images/reference/btql-filter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-filter.png?w=280&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=912f65ea85520f9a4f5f6d915fb225a1 280w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-filter.png?w=560&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=505b210e684e9e9d8f11869bb4c0cd19 560w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-filter.png?w=840&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=b6fdfbec5bc28028b294c6249b432885 840w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-filter.png?w=1100&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=0b4b22fda1b81568151ae3984a3eca7e 1100w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-filter.png?w=1650&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=0017d77eabaf1c38c9d8c9be39fbd555 1650w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-filter.png?w=2500&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=8d9882b8a9baa6b1243428e6f4a6ed1c 2500w" />

### BTQL sandbox

To test BTQL with autocomplete, validation, and a table of results, use the **BTQL sandbox** in the dashboard. In your project, select **BTQL sandbox** at the bottom of the sidebar.

<img src="https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-sandbox.png?fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=9ab48cd65e05e571097aa498f1a0449e" alt="BTQL sandbox" data-og-width="791" width="791" data-og-height="539" height="539" data-path="images/reference/btql-sandbox.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-sandbox.png?w=280&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=50092a604a675ede43d5970a469a63de 280w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-sandbox.png?w=560&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=f32ea8615f91db55efac339095f09d08 560w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-sandbox.png?w=840&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=f3512801e93596f700a6f0e88a785472 840w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-sandbox.png?w=1100&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=7b907b13fe5b2d5937109c9c2c98eb68 1100w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-sandbox.png?w=1650&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=381456c3d0529f4597862dce7bacf454 1650w, https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/btql-sandbox.png?w=2500&fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=1b587c96c72a0bac15fef46d1df2c5ac 2500w" />

### API access

Access BTQL programmatically with the Braintrust API:

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl -X POST https://api.braintrust.dev/btql \
    -H "Authorization: Bearer <YOUR_API_KEY>" \
    -H "Content-Type: application/json" \
    -d '{"query": "select: * | from: project_logs('"'<YOUR_PROJECT_ID>'"') | filter: tags includes '"'triage'"'"}'
  ```
</CodeGroup>

The API accepts these parameters:

* `query` (required): your BTQL query string
* `fmt`: response format (`json` or `parquet`, defaults to `json`)
* `tz_offset`: timezone offset in minutes for time-based operations
* `audit_log`: include audit log data

<Note>
  For correct day boundaries, set `tz_offset` to match your timezone. For example, use `480` for US Pacific Standard Time.
</Note>

## Query structure

BTQL queries follow a familiar SQL-like structure that lets you define what data you want, how you want it returned, and how to analyze it.

This example returns every log from a project where Factuality is greater than 0.8, sorts by created date descending, and limits the results to 100.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *                           -- Fields to retrieve
  from: project_logs('<PROJECT_ID>') spans  -- Data source (identifier or function call)
  filter: scores.Factuality > 0.8     -- Filter conditions
  sample: 25%                         -- Random sampling (optional)
  sort: created desc                  -- Sort order
  limit: 100                          -- Result size limit
  cursor: '<CURSOR>'                  -- Pagination token
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('<PROJECT_ID>', shape => 'spans')
  WHERE scores.Factuality > 0.8
  ORDER BY created DESC
  LIMIT 100
  ```
</CodeGroup>

* `select`: choose which fields to retrieve
* `from`: specify the data source. Has an optional designator for the shape of the data: `spans`, `traces`, `summary`. If not specified, defaults to `spans`
* `filter`: define conditions to filter the data
* `sample`: randomly sample a subset of the filtered data (rate or count-based)
* `sort`: set the order of results (`asc` or `desc`)
* `limit` and `cursor`: control result size and enable pagination

### SQL syntax

BTQL supports standard SQL syntax as an alternative to the native clause-based syntax. The parser automatically detects whether your query is SQL or BTQL:

* **SQL queries** start with `SELECT`, `WITH`, etc. followed by whitespace
* **BTQL queries** use clause syntax like `select:`, `filter:`, etc.

| SQL Clause                            | BTQL Clause                |
| ------------------------------------- | -------------------------- |
| `SELECT ...`                          | `select: ...`              |
| `FROM table('id', shape => 'traces')` | `from: table('id') traces` |
| `WHERE ...`                           | `filter: ...`              |
| `GROUP BY ...`                        | `dimensions: ...`          |
| `ORDER BY ...`                        | `sort: ...`                |
| `LIMIT n`                             | `limit: n`                 |

<Note>
  SQL syntax specifies the shape with a named parameter (e.g., `FROM experiment('id', shape => 'traces')`), while BTQL uses a trailing token (e.g., `from: experiment('id') traces`). Table aliases (e.g., `AS t`) are reserved for future use.
</Note>

<Note>
  **Full-text search:** Use MySQL's `MATCH...AGAINST` syntax for BTQL's `MATCH` operator:

  * `WHERE MATCH(input) AGAINST ('search term')` → `filter: input MATCH 'search term'`
  * Multiple columns are OR'd: `MATCH(col1, col2) AGAINST ('x')` → `col1 MATCH 'x' OR col2 MATCH 'x'`
</Note>

<Warning>
  **Unsupported SQL features:** The SQL parser does not support `JOIN`, subqueries, `UNION`/`INTERSECT`/`EXCEPT`, `HAVING`, or window functions. Use BTQL's native syntax for queries that would require these features.
</Warning>

### `from` data source options

The `from` clause in BTQL specifies the data source for your query.

* `experiment('<experiment_id1>', <experiment_id2>)`: a specific experiment or list of experiments
* `dataset('<dataset_id1>', <dataset_id2>)`: a specific dataset or list of datasets
* `prompt('<prompt_id1>', <prompt_id2>)`: a specific prompt or list of prompts
* `function('<function_id1>', <function_id2>)`: a specific function or list of functions
* `view('<view_id1>', <view_id2>)`: a specific saved view or list of saved views
* `project_logs('<project_id1>', <project_id2>)`: all logs for a specific project or list of projects
* `project_prompts('<project_id1>', <project_id2>)`: all prompts for a specific project or list of projects
* `project_functions('<project_id1>', <project_id2>)`: all functions for a specific project or list of projects
* `org_prompts('<org_id1>', <org_id2>)`: all prompts for a specific organization or list of organizations
* `org_functions('<org_id1>', <org_id2>)`: all functions for a specific organization or list of organizations

## Retrieve records

When retrieving records with BTQL, you can either use `select` or `dimensions` and `measures`. You can use most tools when using either method, but you must use `dimensions` and `measures` if you want to aggregate functions to retrieve results.

Both retrieval methods work with all data shapes (`spans`, `traces`, and `summary`). Using `dimensions` and `measures` with the `summary` shape enables trace-level aggregations.

### `select`

`select` in BTQL is identical to the `select` clause in SQL. You can select specific fields, compute values, or use `*` to retrieve every field.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Get specific fields
select:
  metadata.model as model,
  scores.Factuality as score,
  created as timestamp
from: project_logs('my-project-id')
```

BTQL allows you to transform data directly in the `select` clause. This query returns `metadata.model`, whether `metrics.tokens` is greater than 1000, and a quality indicator of either "high" or "low" depending on whether or not the Factuality score is greater than 0.8.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
select:
  -- Simple field access
  metadata.model,

  -- Computed values
  metrics.tokens > 1000 as is_long_response,

  -- Conditional logic
  (scores.Factuality > 0.8 ? "high" : "low") as quality
from: project_logs('my-project-id')
```

You can also use functions in the `select` clause to transform values and create meaningful aliases for your results. This query extracts the day the log was created, the hour, and a Factuality score rounded to 2 decimal places.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
select:
  -- Date/time functions
  day(created) as date,
  hour(created) as hour,

  -- Numeric calculations
  round(scores.Factuality, 2) as rounded_score
from: project_logs('my-project-id')
```

{/* are there other examples we should include here? */}

### `dimensions` and `measures`

Instead of `select`, you can use `dimensions` and `measures` to group and aggregate data. This query returns a row for each distinct model with the day it was created, the total number of calls, the average Factuality score, and the latency percentile.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Analyze model performance over time
  dimensions:
    metadata.model as model,
    day(created) as date
  measures:
    count(1) as total_calls,
    avg(scores.Factuality) as avg_score,
    percentile(latency, 0.95) as p95_latency
  from: project_logs('my-project-id')
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Analyze model performance over time (SQL)
  SELECT
    metadata.model AS model,
    day(created) AS date,
    count(1) AS total_calls,
    avg(scores.Factuality) AS avg_score,
    percentile(latency, 0.95) AS p95_latency
  FROM project_logs('my-project-id')
  GROUP BY metadata.model, day(created)
  ```
</CodeGroup>

The available aggregate functions are:

* `count(expr)`: number of rows
* `count_distinct(expr)`: number of distinct values
* `sum(expr)`: sum of numeric values
* `avg(expr)`: mean (average) of numeric values
* `min(expr)`: minimum value
* `max(expr)`: maximum value
* `percentile(expr, p)`: a percentile where `p` is between 0 and 1

## `from`

The `from` clause identifies where the records are coming from. This can be an identifier like `project_logs` or a function call like `experiment("id")`.

You can add an optional parameter to the `from` clause that defines how the data is returned. The options are `spans` (default), `traces`, and `summary`.

### `spans`

`spans` returns individual spans that match the filter criteria. This example returns 10 LLM call spans that took more than 0.2 seconds to use the first token.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
select: *
from: project_logs('my-project-id') spans
filter: span_attributes.type = 'llm' and metrics.time_to_first_token > 0.1
limit: 10
```

The response is an array of spans. Check out the [Customize traces](/guides/traces/customize#underlying-format) page for more details on span structure.

### `traces`

`traces` returns all spans from traces that contain at least one matching span. This is useful when you want to see the full context of a specific event or behavior, for example if you want to see all spans in traces where an error occurred.

This example returns all spans for a specific trace where one span in the trace had an error.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id') traces
  filter: root_span_id = 'trace-id' and error IS NOT NULL
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id', shape => 'traces')
  WHERE root_span_id = 'trace-id' AND error IS NOT NULL
  ```
</CodeGroup>

The response is an array of spans. Check out the [Customize traces](/guides/traces/customize#underlying-format) page for more details on span structure.

### `summary`

`summary` provides trace-level views of your data by aggregating metrics across all spans in a trace. This shape is useful for analyzing overall performance and comparing results across experiments.

The `summary` shape can be used in two ways:

* **Individual trace summaries** (using `select`): Returns one row per trace with aggregated span metrics. Use this to see trace-level details. Example: "What are the details of traces with errors?"
* **Aggregated trace analytics** (using `dimensions` and `measures`): Groups multiple traces and computes statistics. Use this to analyze patterns across many traces. Example: "What's the average cost per model per day?"

#### Individual trace summaries

Use [`select`](#select) with the `summary` shape to retrieve individual traces with aggregated metrics. This is useful for inspecting specific trace details, debugging issues, or exporting trace-level data.

This example returns 10 summary rows from the project logs for 'my-project-id'.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id') summary -- Returns one row per trace with aggregated metrics across all spans in that trace
  preview_length: 1024 -- Optional, controls truncation of preview fields. Default is 124.
  limit: 10
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id', shape => 'summary')
  LIMIT 10
  ```
</CodeGroup>

Summary rows include some aggregated metrics and some preview fields that show data from the root span of the trace.

The following fields are aggregated metrics across all spans in the trace.

* `scores`: an object with all scores averaged across all spans
* `metrics`: an object with aggregated metrics across all spans
  * `prompt_tokens`: total number of prompt tokens used
  * `completion_tokens`: total number of completion tokens used
  * `prompt_cached_tokens`: total number of cached prompt tokens used
  * `prompt_cache_creation_tokens`: total number of tokens used to create cache entries
  * `total_tokens`: total number of tokens used (prompt + completion)
  * `estimated_cost`: total estimated cost of the trace in US dollars (prompt + completion costs)
  * `llm_calls`: total number of LLM calls
  * `tool_calls`: total number of tool calls
  * `errors`: total number of errors (LLM + tool errors)
  * `llm_errors`: total number of LLM errors
  * `tool_errors`: total number of tool errors
  * `start`: Unix timestamp of the first span start time
  * `end`: Unix timestamp of the last span end time
  * `duration`: maximum duration of any span in seconds. Note: this is not the total trace duration.
  * `llm_duration`: sum of all durations across LLM spans in seconds
  * `time_to_first_token`: the average time to first token across LLM spans in seconds
* `span_type_info`: an object with span type info. Some fields in this object are aggregated across all spans and some reflect attributes from the root span.
  * `cached`: true only if all LLM spans were cached
  * `has_error`: true if any span had an error

Root span preview fields include `input`, `output`, `expected`, `error`, and `metadata`.

#### Aggregated trace analytics

Use [`dimensions` and `measures`](#dimensions-and-measures) with the `summary` shape to group and aggregate traces. This is useful for analyzing patterns, monitoring performance trends, and comparing metrics across models or time periods.

These examples show how to group traces by model to track performance over time, and how to compare workflows across experiments:

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Group traces by model to analyze performance over time
  from: project_logs('my-project-id') summary
  dimensions:
    metadata.model as model,
    day(created) as date
  measures:
    count(1) as trace_count,
    avg(scores.Factuality) as avg_score,
    avg(metrics.estimated_cost) as avg_cost
  sort: date desc
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Group traces by model to analyze performance over time
  SELECT
    metadata.model AS model,
    day(created) AS date,
    count(1) AS trace_count,
    avg(scores.Factuality) AS avg_score,
    avg(metrics.estimated_cost) AS avg_cost
  FROM project_logs('my-project-id', shape => 'summary')
  GROUP BY 1, 2
  ORDER BY date DESC
  ```
</CodeGroup>

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Compare workflows across experiments
  from: experiment('<EXPERIMENT_ID_1>', '<EXPERIMENT_ID_2>') summary
  dimensions:
    metadata.workflow_type as workflow,
    origin.experiment_id as experiment
  measures:
    count(1) as trace_count,
    avg(metrics.estimated_cost) as avg_cost,
    avg(scores.Success) as success_rate
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Compare workflows across experiments
  SELECT
    metadata.workflow_type AS workflow,
    origin.experiment_id AS experiment,
    count(1) AS trace_count,
    avg(metrics.estimated_cost) AS avg_cost,
    avg(scores.Success) AS success_rate
  FROM experiment('<EXPERIMENT_ID_1>', '<EXPERIMENT_ID_2>', shape => 'summary')
  GROUP BY 1, 2
  ```
</CodeGroup>

## `filter`

The `filter` clause lets you specify conditions to narrow down results. Similar to the `WHERE` clause in SQL, it supports a wide range of [operators](#btql-operators) and [functions](#btql-functions), including complex conditions.

This example `filter` only retrieves data where:

* Factuality score is greater than 0.8
* model is "gpt-4"
* tag list includes "triage"
* input contains the word "question" (case-insensitive)
* created date is later than January 1, 2024
* more than 1000 tokens were used or the data being traced was made in production

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id')
  filter:
    -- Simple comparisons
    scores.Factuality > 0.8 and
    metadata.model = "gpt-4" and

    -- Array operations
    tags includes "triage" and

    -- Text search (case-insensitive)
    input ILIKE '%question%' and

    -- Date ranges
    created > '2024-01-01' and

    -- Complex conditions
    (
      metrics.tokens > 1000 or
      metadata.is_production = true
    )
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id')
  WHERE
    -- Simple comparisons
    scores.Factuality > 0.8 AND
    metadata.model = 'gpt-4' AND

    -- Array operations
    tags INCLUDES 'triage' AND

    -- Text search (case-insensitive)
    input ILIKE '%question%' AND

    -- Date ranges
    created > '2024-01-01' AND

    -- Complex conditions
    (
      metrics.tokens > 1000 OR
      metadata.is_production = true
    )
  ```
</CodeGroup>

<Note>
  Note: Negative filters on tags (e.g., `NOT tags includes "resolved"`) may not work as expected. Since tags are only applied to the root span of a trace, and queries return complete traces, negative tag filters will match child spans (which don't have tags) and return the entire trace. We recommend using positive tag filters instead.
</Note>

### Single span filters

By default, each returned trace includes at least one span that matches all filter conditions. Use single span filters to find traces where different spans match different conditions. This is helpful for finding errors in tagged traces where the error may not be on the root span.

Wrap any filter expression with `any_span()` to mark it as a single span filter. This `filter` example returns traces with a "production" tag that encountered an error.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
filter:
  any_span(tags includes "production") and
  any_span(error IS NOT NULL)
```

Single span filters work with the `traces` and `summary` data shapes.

### Pattern matching

BTQL supports the `%` SQL wildcard for pattern matching with `LIKE` (case-sensitive) and `ILIKE` (case-insensitive).

The `%` wildcard matches any sequence of zero or more characters.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Match any input containing "question"
filter: input ILIKE '%question%'

-- Match inputs starting with "How"
filter: input LIKE 'How%'

-- Match emails ending with specific domains
filter: metadata.email ILIKE '%@braintrust.com'

-- Escape literal wildcards with backslash
filter: metadata.description LIKE '%50\% off%'  -- Matches "50% off"
```

### Time intervals

BTQL supports intervals for time-based operations.

This query returns all project logs from 'my-project-id' that were created in the last day.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id')
  filter: created > now() - interval 1 day
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id')
  WHERE created > now() - interval 1 day
  ```
</CodeGroup>

This query returns all project logs from 'my-project-id' that were created up to an hour ago.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id')
  filter:
    created > now() - interval 1 hour and
    created < now()
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id')
  WHERE created > now() - interval 1 hour
    AND created < now()
  ```
</CodeGroup>

This query returns all project logs from 'my-project-id' that were created last week and last month.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Examples with different units
select: *
from: project_logs('my-project-id')
filter:
  created > now() - interval 7 day and    -- Last week
  created > now() - interval 1 month      -- Last month
```

## `sort`

The `sort` clause determines the order of results. The options are `desc` (descending) and `asc` (ascending) on a numerical field. You can sort by a single field, multiple fields, or computed values.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Sort by single field
sort: created desc

-- Sort by multiple fields
sort: scores.Factuality desc, created asc

-- Sort by computed values
sort: len(tags) desc
```

## `pivot` and `unpivot`

`pivot` and `unpivot` are advanced clauses that transform your results for easier analysis and comparison.

### `pivot`

The `pivot` clause transforms your results to make comparisons easier by converting rows into columns. This is useful when comparing metrics across different categories or time periods.

Syntax:

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pivot: <measure1>, <measure2>, ...
```

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Compare model performance metrics across models
dimensions: day(created) as date
measures:
  avg(scores.Factuality) as avg_factuality,
  avg(metrics.tokens) as avg_tokens,
  count(1) as call_count
from: project_logs('my-project-id')
pivot: avg_factuality, avg_tokens, call_count

-- Results will look like:
-- {
--   "date": "2024-01-01",
--   "gpt-4_avg_factuality": 0.92,
--   "gpt-4_avg_tokens": 150,
--   "gpt-4_call_count": 1000,
--   "gpt-3.5-turbo_avg_factuality": 0.85,
--   "gpt-3.5-turbo_avg_tokens": 120,
--   "gpt-3.5-turbo_call_count": 2000
-- }
```

This query returns a record for each model with Factuality score and latency percentile across time periods.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Compare metrics across time periods
dimensions: metadata.model as model
measures:
  avg(scores.Factuality) as avg_score,
  percentile(latency, 0.95) as p95_latency
from: project_logs('my-project-id')
pivot: avg_score, p95_latency

-- Results will look like:
-- {
--   "model": "gpt-4",
--   "0_avg_score": 0.91,
--   "0_p95_latency": 2.5,
--   "1_avg_score": 0.89,
--   "1_p95_latency": 2.8,
--   ...
-- }
```

This query returns a record for each tag and aggregates the number of instances of that tag per model.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Compare tag distributions across models
dimensions: tags[0] as primary_tag
measures: count(1) as tag_count
from: project_logs('my-project-id')
pivot: tag_count

-- Results will look like:
-- {
--   "primary_tag": "quality",
--   "gpt-4_tag_count": 500,
--   "gpt-3.5-turbo_tag_count": 300
-- }
```

<Note>
  Pivot columns are automatically named by combining the dimension value and measure name. For example, if you pivot by `metadata.model` and a model named "gpt-4" to measure `avg_score`, the name becomes `gpt-4_avg_score`.
</Note>

### `unpivot`

The `unpivot` clause transforms columns into rows, which is useful when you need to analyze arbitrary scores and metrics without specifying each score name. This is helpful when working with dynamic sets of metrics or when you need to know all possible score names in advance.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Convert wide format to long format for arbitrary scores
dimensions: created as date
measures: count(1) as count
from: project_logs('my-project-id')
unpivot: count as (score_name, score_value)

-- Results will look like:
-- {
--   "date": "2024-01-01",
--   "score_name": "Factuality",
--   "score_value": 0.92
-- },
-- {
--   "date": "2024-01-01",
--   "score_name": "Coherence",
--   "score_value": 0.88
-- }
```

## `limit` and `cursor`

### `limit`

The `limit` clause controls the size of the result in number of records.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Basic limit
limit: 100
```

### `cursor`

The `cursor` clause implements pagination. Cursors are automatically returned in BTQL responses. A default limit is applied in a query without a limit clause, and the number of returned results can be overridden by using an explicit `limit`. In order to implement pagination, after an initial query, provide the subsequent cursor token returned in the results in the `cursor` clause in follow-on queries. When a cursor has reached the end of the result set, the `data` array will be empty, and no cursor token will be returned by the query.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Pagination using cursor (only works without sort)
select: *
from: project_logs('<PROJECT_ID>')
limit: 100
cursor: '<CURSOR_TOKEN>'  -- From previous query response
```

Cursors can only be used for pagination when no `sort` clause is specified. If you need sorted results, you'll need to implement offset-based pagination by using the last value from your sort field as a filter in the next query.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Offset-based pagination with sorting
-- Page 1 (first 100 results)
select: *
from: project_logs('<PROJECT_ID>')
sort: created desc
limit: 100
```

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Page 2 (next 100 results)
select: *
from: project_logs('<PROJECT_ID>')
filter: created < '2024-01-15T10:30:00Z'  -- Last created timestamp from previous page
sort: created desc
limit: 100
```

## Expressions

### BTQL operators

You can use the following operators in your BTQL queries.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Comparison operators
=           -- Equal to (alias for 'eq')
!=          -- Not equal to (alias for 'ne', can also use '<>')
>           -- Greater than (alias for 'gt')
<           -- Less than (alias for 'lt')
>=          -- Greater than or equal (alias for 'ge')
<=          -- Less than or equal (alias for 'le')
IN          -- Check if value exists in a list of values

-- Null operators
IS NULL     -- Check if value is null
IS NOT NULL -- Check if value is not null
ISNULL      -- Unary operator to check if null
ISNOTNULL   -- Unary operator to check if not null

-- Text matching
LIKE        -- Case-sensitive pattern matching (supports % wildcard)
NOT LIKE    -- Negated case-sensitive pattern matching
ILIKE       -- Case-insensitive pattern matching (supports % wildcard)
NOT ILIKE   -- Negated case-insensitive pattern matching
MATCH       -- Full-word semantic search (faster but requires exact word matches, e.g. 'apple' won't match 'app')
NOT MATCH   -- Negated full-word semantic search

-- Array operators
INCLUDES    -- Check if array/object contains value (alias: CONTAINS)
NOT INCLUDES -- Check if array/object does not contain value

-- Logical operators
AND         -- Both conditions must be true
OR          -- Either condition must be true
NOT         -- Unary operator to negate condition

-- Arithmetic operators
+           -- Addition (alias: add)
-           -- Subtraction (alias: sub)
*           -- Multiplication (alias: mul)
/           -- Division (alias: div)
%           -- Modulo (alias: mod)
-x          -- Unary negation (alias: neg)
```

### BTQL functions

You can use the following functions in `select`, `filter`, `dimensions`, and `measures` clauses.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Date/time functions
second(timestamp)          -- Extract second from timestamp
minute(timestamp)         -- Extract minute from timestamp
hour(timestamp)          -- Extract hour from timestamp
day(timestamp)           -- Extract day from timestamp
week(timestamp)          -- Extract week from timestamp
month(timestamp)         -- Extract month from timestamp
year(timestamp)          -- Extract year from timestamp
date_trunc(interval, timestamp)  -- Truncate timestamp to specified interval
                                 -- Intervals: 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'
current_timestamp()      -- Get current timestamp (alias: now())
current_date()          -- Get current date

-- String functions
lower(text)                       -- Convert text to lowercase
upper(text)                       -- Convert text to uppercase
concat(text1, text2, ...)         -- Concatenate strings

-- Array functions
len(array)                        -- Get length of array
contains(array, value)            -- Check if array contains value (alias: includes)

-- JSON functions
json_extract(json_str, path)      -- Extract value from JSON string using a path expression

-- Null handling functions
coalesce(val1, val2, ...)        -- Return first non-null value
nullif(val1, val2)               -- Return null if val1 equals val2
least(val1, val2, ...)           -- Return smallest non-null value
greatest(val1, val2, ...)        -- Return largest non-null value

-- Type conversion
round(number, precision)          -- Round to specified precision

-- Cast functions
to_string(value)                 -- Cast value to string
to_boolean(value)                -- Cast value to boolean
to_integer(value)                -- Cast value to integer
to_number(value)                 -- Cast value to number
to_date(value)                   -- Cast value to date
to_datetime(value)               -- Cast value to datetime
to_interval(value)               -- Cast value to interval

-- Aggregate functions (only in measures)
count(expr)                       -- Count number of rows
count_distinct(expr)              -- Count number of distinct values
sum(expr)                        -- Sum numeric values
avg(expr)                        -- Calculate mean of numeric values
min(expr)                        -- Find minimum value
max(expr)                        -- Find maximum value
percentile(expr, p)              -- Calculate percentile (p between 0 and 1)
```

### Field access

BTQL provides flexible ways to access nested data in arrays and objects:

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Object field access
metadata.model             -- Access nested object field  e.g. {"metadata": {"model": "value"}}
metadata."field name"      -- Access field with spaces	  e.g. {"metadata": {"field name": "value"}}
metadata."field-name"      -- Access field with hyphens   e.g. {"metadata": {"field-name": "value"}}
metadata."field.name"      -- Access field with dots	  e.g. {"metadata": {"field.name": "value"}}

-- Array access (0-based indexing)
tags[0]                    -- First element
tags[-1]                   -- Last element

-- Combined array and object access
metadata.models[0].name    -- Field in first array element
responses[-1].tokens       -- Field in last array element
spans[0].children[-1].id   -- Nested array traversal
```

<Note>
  Array indices are 0-based, and negative indices count from the end (-1 is the last element).
</Note>

When you have JSON data stored as a string field (rather than as native BTQL objects), use the [`json_extract` function](#extract-data-from-json-strings) to access values within it. The function supports the same path expressions as direct field access:

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Extract from JSON string fields
json_extract(metadata.config, 'api.endpoint')      -- Dot notation
json_extract(output, 'results[0].score')           -- Array indexing
json_extract(metadata.settings, 'options[-1]')     -- Negative indices
```

### Conditional expressions

BTQL supports conditional logic using the ternary operator (`? :`):

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Basic conditions
select:
  (scores.Factuality > 0.8 ? "high" : "low") as quality,
  (error IS NOT NULL ? -1 : metrics.tokens) as valid_tokens
from: project_logs('my-project-id')
```

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Nested conditions
select:
  (scores.Factuality > 0.9 ? "excellent" :
   scores.Factuality > 0.7 ? "good" :
   scores.Factuality > 0.5 ? "fair" : "poor") as rating
from: project_logs('my-project-id')
```

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Use in calculations
select:
  (metadata.model = "gpt-4" ? metrics.tokens * 2 : metrics.tokens) as adjusted_tokens,
  (error IS NULL ? metrics.latency : 0) as valid_latency
from: project_logs('my-project-id')
```

## Examples

{/* we should add a "Run in sandbox" button for each of these examples -- are there examples here that may not run in every sandbox?*/}

### Track token usage

This query helps you monitor token consumption across your application.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from: project_logs('<YOUR_PROJECT_ID>')
  filter: created > '<ISO_8601_TIME>'
  dimensions: day(created) as time
  measures:
    sum(metrics.total_tokens) as total_tokens,
    sum(metrics.prompt_tokens) as input_tokens,
    sum(metrics.completion_tokens) as output_tokens
  sort: time asc
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT
    day(created) AS time,
    sum(metrics.total_tokens) AS total_tokens,
    sum(metrics.prompt_tokens) AS input_tokens,
    sum(metrics.completion_tokens) AS output_tokens
  FROM project_logs('<YOUR_PROJECT_ID>')
  WHERE created > '<ISO_8601_TIME>'
  GROUP BY 1
  ORDER BY time ASC
  ```

  ```sql SQL syntax (using date_trunc) theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Alternative using date_trunc function
  SELECT
    date_trunc('day', created) AS time,
    sum(metrics.total_tokens) AS total_tokens,
    sum(metrics.prompt_tokens) AS input_tokens,
    sum(metrics.completion_tokens) AS output_tokens
  FROM project_logs('<YOUR_PROJECT_ID>')
  WHERE created > '<ISO_8601_TIME>'
  GROUP BY date_trunc('day', created)
  ORDER BY time ASC
  ```
</CodeGroup>

The response shows daily token usage:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
  "time": "2024-11-09T00:00:00Z",
  "total_tokens": 100000,
  "input_tokens": 50000,
  "output_tokens": 50000
}
```

### Monitor model quality

Track model performance across different versions and configurations.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Compare factuality scores across models
  dimensions:
    metadata.model as model,
    day(created) as date
  measures:
    avg(scores.Factuality) as avg_factuality,
    percentile(scores.Factuality, 0.05) as p05_factuality,
    percentile(scores.Factuality, 0.95) as p95_factuality,
    count(1) as total_calls
  filter: created > '2024-01-01'
  sort: date desc, model asc
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Compare factuality scores across models
  SELECT
    metadata.model AS model,
    day(created) AS date,
    avg(scores.Factuality) AS avg_factuality,
    percentile(scores.Factuality, 0.05) AS p05_factuality,
    percentile(scores.Factuality, 0.95) AS p95_factuality,
    count(1) AS total_calls
  FROM project_logs('<PROJECT_ID>')
  WHERE created > '2024-01-01'
  GROUP BY 1, 2
  ORDER BY date DESC, model ASC
  ```
</CodeGroup>

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Find potentially problematic responses
  select: *
  from: project_logs('<PROJECT_ID>')
  filter:
    scores.Factuality < 0.5 and
    metadata.is_production = true and
    created > now() - interval 1 day
  sort: scores.Factuality asc
  limit: 100
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Find potentially problematic responses
  SELECT *
  FROM project_logs('<PROJECT_ID>')
  WHERE scores.Factuality < 0.5
    AND metadata.is_production = true
    AND created > now() - interval 1 day
  ORDER BY scores.Factuality ASC
  LIMIT 100
  ```
</CodeGroup>

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Compare performance across specific models
  select: *
  from: project_logs('<PROJECT_ID>')
  filter:
    metadata.model IN ["gpt-4", "gpt-4-turbo", "claude-3-opus"] and
    scores.Factuality IS NOT NULL and
    created > now() - interval 7 day
  sort: scores.Factuality desc
  limit: 500
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Compare performance across specific models
  SELECT *
  FROM project_logs('<PROJECT_ID>')
  WHERE metadata.model IN ('gpt-4', 'gpt-4-turbo', 'claude-3-opus')
    AND scores.Factuality IS NOT NULL
    AND created > now() - interval 7 day
  ORDER BY scores.Factuality DESC
  LIMIT 500
  ```
</CodeGroup>

### Analyze errors

Identify and investigate errors in your application.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Error rate by model
  dimensions:
    metadata.model as model,
    hour(created) as hour
  measures:
    count(1) as total,
    count(error) as errors,
    count(error) / count(1) as error_rate
  filter: created > now() - interval 1 day
  sort: error_rate desc
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Error rate by model
  SELECT
    metadata.model AS model,
    hour(created) AS hour,
    count(1) AS total,
    count(error) AS errors,
    count(error) / count(1) AS error_rate
  FROM project_logs('<PROJECT_ID>')
  WHERE created > now() - interval 1 day
  GROUP BY 1, 2
  ORDER BY error_rate DESC
  ```
</CodeGroup>

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Find common error patterns
  dimensions:
    error.type as error_type,
    metadata.model as model
  measures:
    count(1) as error_count,
    avg(metrics.latency) as avg_latency
  filter:
    error IS NOT NULL and
    created > now() - interval 7 day
  sort: error_count desc
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Find common error patterns
  SELECT
    error.type AS error_type,
    metadata.model AS model,
    count(1) AS error_count,
    avg(metrics.latency) AS avg_latency
  FROM project_logs('<PROJECT_ID>')
  WHERE error IS NOT NULL
    AND created > now() - interval 7 day
  GROUP BY 1, 2
  ORDER BY error_count DESC
  ```
</CodeGroup>

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Exclude known error types from analysis
select: *
from: project_logs('<PROJECT_ID>')
filter:
  error IS NOT NULL and
  error.type NOT IN ["rate_limit", "timeout", "network_error"] and
  metadata.is_production = true and
  created > now() - interval 1 day
sort: created desc
limit: 100
```

### Analyze latency

Monitor and optimize response times.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Track p95 latency by endpoint
dimensions:
  metadata.endpoint as endpoint,
  hour(created) as hour
measures:
  percentile(metrics.latency, 0.95) as p95_latency,
  percentile(metrics.latency, 0.50) as median_latency,
  count(1) as requests
filter: created > now() - interval 1 day
sort: hour desc, p95_latency desc
```

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Find slow requests
select:
  metadata.endpoint,
  metrics.latency,
  metrics.tokens,
  input,
  created
from: project_logs('<PROJECT_ID>')
filter:
  metrics.latency > 5000 and  -- Requests over 5 seconds
  created > now() - interval 1 hour
sort: metrics.latency desc
limit: 20
```

### Analyze prompts

Analyze prompt effectiveness and patterns.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Track prompt token efficiency
dimensions:
  metadata.prompt_template as template,
  day(created) as date
measures:
  avg(metrics.prompt_tokens) as avg_prompt_tokens,
  avg(metrics.completion_tokens) as avg_completion_tokens,
  avg(metrics.completion_tokens) / avg(metrics.prompt_tokens) as token_efficiency,
  avg(scores.Factuality) as avg_factuality
filter: created > now() - interval 7 day
sort: date desc, token_efficiency desc
```

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Find similar prompts
select: *
from: project_logs('<PROJECT_ID>')
filter:
  input MATCH 'explain the concept of recursion' and
  scores.Factuality > 0.8
sort: created desc
limit: 10
```

### Analyze based on tags

Use tags to track and analyze specific behaviors.

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Monitor feedback patterns
dimensions:
  tags[0] as primary_tag,
  metadata.model as model
measures:
  count(1) as feedback_count,
  avg(scores.Factuality > 0.8 ? 1 : 0) as high_quality_rate
filter:
  tags includes 'feedback' and
  created > now() - interval 30 day
sort: feedback_count desc
```

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Track issue resolution
select:
  created,
  tags,
  metadata.model,
  scores.Factuality,
  response
from: project_logs('<PROJECT_ID>')
filter:
  tags includes 'needs-review' and
  NOT tags includes 'resolved' and
  created > now() - interval 1 day
sort: scores.Factuality asc
```

### Extract data from JSON strings

Use `json_extract` to extract values from a JSON string using a path expression. This is useful when you have JSON data stored as a string field and need to access specific values within it.

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract a simple field
  select:
    id,
    json_extract(metadata.config, 'api_key') as api_key
  from: project_logs('my-project-id')
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract a simple field
  SELECT
    id,
    json_extract(metadata.config, 'api_key') AS api_key
  FROM project_logs('my-project-id')
  ```
</CodeGroup>

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract from nested objects
  select:
    id,
    json_extract(metadata.settings, 'user.preferences.theme') as theme
  from: project_logs('my-project-id')
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract from nested objects
  SELECT
    id,
    json_extract(metadata.settings, 'user.preferences.theme') AS theme
  FROM project_logs('my-project-id')
  ```
</CodeGroup>

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract array elements
  select:
    id,
    json_extract(metadata.results, 'scores[0]') as first_score,
    json_extract(metadata.results, 'scores[-1]') as last_score
  from: project_logs('my-project-id')
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract array elements
  SELECT
    id,
    json_extract(metadata.results, 'scores[0]') AS first_score,
    json_extract(metadata.results, 'scores[-1]') AS last_score
  FROM project_logs('my-project-id')
  ```
</CodeGroup>

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract and filter
  select: *
  from: project_logs('my-project-id')
  filter:
    json_extract(metadata.config, 'environment') = 'production' and
    json_extract(metadata.config, 'version') > '2.0'
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract and filter
  SELECT *
  FROM project_logs('my-project-id')
  WHERE json_extract(metadata.config, 'environment') = 'production'
    AND json_extract(metadata.config, 'version') > '2.0'
  ```
</CodeGroup>

<CodeGroup>
  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Handle nested arrays
  select:
    id,
    json_extract(output, 'results[0][1].value') as nested_value
  from: project_logs('my-project-id')
  ```

  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Handle nested arrays
  SELECT
    id,
    json_extract(output, 'results[0][1].value') AS nested_value
  FROM project_logs('my-project-id')
  ```
</CodeGroup>

<Note>
  `json_extract` returns `null` for invalid JSON or missing paths rather than raising an error, making it safe to use in filters and aggregations.
</Note>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt