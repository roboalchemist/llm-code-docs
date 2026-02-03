# Source: https://braintrust.dev/docs/reference/sql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SQL queries

SQL queries in Braintrust provide a precise, standard syntax for querying Braintrust experiments, logs, and datasets. Use SQL to better analyze and understand your data.

Braintrust supports two syntax styles: standard **SQL syntax**, and the native **BTQL syntax** with pipe-delimited clauses. The parser automatically detects which style you're using.

## Why use SQL?

SQL gives you precise control over your AI application data. You can:

* Filter and search for relevant logs and experiments
* Create consistent, reusable queries for monitoring
* Build automated reporting and analysis pipelines
* Write complex queries to analyze model performance

## SQL in Braintrust

Use SQL when filtering logs and experiments, in the SQL sandbox, and programmatically through the Braintrust API.

### Filter logs and experiments

Use SQL to filter logs and experiments based on specific criteria. You can filter logs by tags, metadata, or any other relevant fields. Filtering in logs and experiments only supports [`WHERE` clauses](#where).

At the top of your experiment or log view, select **Filter** to open the filter editor and select **SQL** to switch to SQL mode.

### SQL sandbox

To test SQL with autocomplete, validation, and a table of results, use the **SQL sandbox** in the dashboard. In your project, select **SQL sandbox** at the bottom of the sidebar.

### API access

Access SQL programmatically with the Braintrust API:

<CodeGroup>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl -X POST https://api.braintrust.dev/btql \
    -H "Authorization: Bearer <YOUR_API_KEY>" \
    -H "Content-Type: application/json" \
    -d '{"query": "SELECT * FROM project_logs('"'<YOUR_PROJECT_ID>'"') WHERE tags INCLUDES '"'triage'"'"}'
  ```
</CodeGroup>

The API accepts these parameters:

* `query` (required): your SQL query string
* `fmt`: response format (`json` or `parquet`, defaults to `json`)
* `tz_offset`: timezone offset in minutes for time-based operations
* `audit_log`: include audit log data

<Note>
  For correct day boundaries, set `tz_offset` to match your timezone. For example, use `480` for US Pacific Standard Time.
</Note>

## Query structure

SQL queries follow a familiar structure that lets you define what data you want, how you want it returned, and how to analyze it.

This example returns every log from a project where Factuality is greater than 0.8, sorts by created date descending, and limits the results to 100.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('<PROJECT_ID>', shape => 'spans')
  WHERE scores.Factuality > 0.8
  ORDER BY created DESC
  LIMIT 100
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *                           -- Fields to retrieve
  from: project_logs('<PROJECT_ID>') spans  -- Data source (identifier or function call)
  filter: scores.Factuality > 0.8     -- Filter conditions
  sample: 25%                         -- Random sampling (optional, BTQL-only)
  sort: created desc                  -- Sort order
  limit: 100                          -- Result size limit
  cursor: '<CURSOR>'                  -- Pagination token (BTQL-only)
  ```
</CodeGroup>

* `SELECT` / `select:`: choose which fields to retrieve
* `FROM` / `from:`: specify the data source. Has an optional designator for the shape of the data: `spans`, `traces`, `summary`. If not specified, defaults to `spans`
* `WHERE` / `filter:`: define conditions to filter the data
* `sample:`: (BTQL-only) randomly sample a subset of the filtered data (rate or count-based)
* `ORDER BY` / `sort:`: set the order of results (`ASC`/`DESC` or `asc`/`desc`)
* `LIMIT` / `limit:`: control result size
* `cursor:`: (BTQL-only) enable pagination

### BTQL syntax

Braintrust also supports BTQL, an alternative pipe-delimited clause syntax. The parser automatically detects whether your query is SQL or BTQL:

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
  **Full-text search:** Use the `MATCH` infix operator for full-text search:

  * `WHERE input MATCH 'search term'` → `filter: input MATCH 'search term'`
  * Multiple columns require OR: `WHERE input MATCH 'x' OR output MATCH 'x'` → `filter: input MATCH 'x' OR output MATCH 'x'`
</Note>

<Warning>
  **Unsupported SQL features:** The SQL parser does not support `JOIN`, subqueries, `UNION`/`INTERSECT`/`EXCEPT`, `HAVING`, or window functions. For `PIVOT`, only `IN (ANY)` is supported (explicit value lists, subqueries, and `ORDER BY` are not supported). Use BTQL's native syntax for queries that would require these features.
</Warning>

### `FROM` data source options

The `FROM` clause in SQL specifies the data source for your query.

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

When retrieving records with SQL, you can either use `SELECT` or `SELECT ... GROUP BY`. You can use most tools when using either method, but you must use `GROUP BY` if you want to aggregate functions to retrieve results.

Both retrieval methods work with all data shapes (`spans`, `traces`, and `summary`). Using `GROUP BY` with the `summary` shape enables trace-level aggregations.

### `SELECT`

`SELECT` in SQL lets you choose specific fields, compute values, or use `*` to retrieve every field.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Get specific fields
  SELECT
    metadata.model AS model,
    scores.Factuality AS score,
    created AS timestamp
  FROM project_logs('my-project-id')
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Get specific fields
  select:
    metadata.model as model,
    scores.Factuality as score,
    created as timestamp
  from: project_logs('my-project-id')
  ```
</CodeGroup>

<Note>
  **Implicit aliasing**: Multi-part identifiers like `metadata.model` automatically create implicit aliases using their last component (e.g., `model`), which you can use in `WHERE`, `ORDER BY`, and `GROUP BY` clauses when unambiguous. See [Field access](#implicit-aliasing) for details.
</Note>

SQL allows you to transform data directly in the `SELECT` clause. This query returns `metadata.model`, whether `metrics.tokens` is greater than 1000, and a quality indicator of either "high" or "low" depending on whether or not the Factuality score is greater than 0.8.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT
    -- Simple field access
    metadata.model,

    -- Computed values
    metrics.tokens > 1000 AS is_long_response,

    -- Conditional logic
    (scores.Factuality > 0.8 ? "high" : "low") AS quality
  FROM project_logs('my-project-id')
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select:
    -- Simple field access
    metadata.model,

    -- Computed values
    metrics.tokens > 1000 as is_long_response,

    -- Conditional logic
    (scores.Factuality > 0.8 ? "high" : "low") as quality
  from: project_logs('my-project-id')
  ```
</CodeGroup>

You can also use functions in the `SELECT` clause to transform values and create meaningful aliases for your results. This query extracts the day the log was created, the hour, and a Factuality score rounded to 2 decimal places.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT
    -- Date/time functions
    day(created) AS date,
    hour(created) AS hour,

    -- Numeric calculations
    round(scores.Factuality, 2) AS rounded_score
  FROM project_logs('my-project-id')
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select:
    -- Date/time functions
    day(created) as date,
    hour(created) as hour,

    -- Numeric calculations
    round(scores.Factuality, 2) as rounded_score
  from: project_logs('my-project-id')
  ```
</CodeGroup>

### `GROUP BY` for aggregations

Instead of a simple `SELECT`, you can use `SELECT ... GROUP BY` to group and aggregate data. This query returns a row for each distinct model with the day it was created, the total number of calls, the average Factuality score, and the latency percentile.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Analyze model performance over time
  SELECT
    metadata.model AS model,
    day(created) AS date,
    count(1) AS total_calls,
    avg(scores.Factuality) AS avg_score,
    percentile(latency, 0.95) AS p95_latency
  FROM project_logs('my-project-id')
  GROUP BY metadata.model, day(created)
  ```

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
</CodeGroup>

The available aggregate functions are:

* `count(expr)`: number of rows
* `count_distinct(expr)`: number of distinct values
* `sum(expr)`: sum of numeric values
* `avg(expr)`: mean (average) of numeric values
* `min(expr)`: minimum value
* `max(expr)`: maximum value
* `percentile(expr, p)`: a percentile where `p` is between 0 and 1

## `FROM`

The `FROM` clause identifies where the records are coming from. This can be an identifier like `project_logs` or a function call like `experiment("id")`.

You can add an optional parameter to the `FROM` clause that defines how the data is returned. The options are `spans` (default), `traces`, and `summary`.

### `spans`

`spans` returns individual spans that match the filter criteria. This example returns 10 LLM call spans that took more than 0.2 seconds to use the first token.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id', shape => 'spans')
  WHERE span_attributes.type = 'llm' AND metrics.time_to_first_token > 0.1
  LIMIT 10
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id') spans
  filter: span_attributes.type = 'llm' and metrics.time_to_first_token > 0.1
  limit: 10
  ```
</CodeGroup>

The response is an array of spans. Check out the [Extend traces](/instrument/advanced-tracing#underlying-format) page for more details on span structure.

### `traces`

`traces` returns all spans from traces that contain at least one matching span. This is useful when you want to see the full context of a specific event or behavior, for example if you want to see all spans in traces where an error occurred.

This example returns all spans for a specific trace where one span in the trace had an error.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id', shape => 'traces')
  WHERE root_span_id = 'trace-id' AND error IS NOT NULL
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id') traces
  filter: root_span_id = 'trace-id' and error IS NOT NULL
  ```
</CodeGroup>

The response is an array of spans. Check out the [Extend traces](/instrument/advanced-tracing#underlying-format) page for more details on span structure.

### `summary`

`summary` provides trace-level views of your data by aggregating metrics across all spans in a trace. This shape is useful for analyzing overall performance and comparing results across experiments.

The `summary` shape can be used in two ways:

* **Individual trace summaries** (using `SELECT`): Returns one row per trace with aggregated span metrics. Use this to see trace-level details. Example: "What are the details of traces with errors?"
* **Aggregated trace analytics** (using `GROUP BY`): Groups multiple traces and computes statistics. Use this to analyze patterns across many traces. Example: "What's the average cost per model per day?"

#### Individual trace summaries

Use `SELECT` with the `summary` shape to retrieve individual traces with aggregated metrics. This is useful for inspecting specific trace details, debugging issues, or exporting trace-level data.

This example returns 10 summary rows from the project logs for 'my-project-id':

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id', shape => 'summary')
  LIMIT 10
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id') summary -- Returns one row per trace with aggregated metrics across all spans in that trace
  preview_length: 1024 -- Optional, controls truncation of preview fields. Default is 124.
  limit: 10
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

Use `GROUP BY` with the `summary` shape to group and aggregate traces. This is useful for analyzing patterns, monitoring performance trends, and comparing metrics across models or time periods.

This example shows how to group traces by model to track performance over time:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
</CodeGroup>

## `WHERE`

The `WHERE` clause lets you specify conditions to narrow down results. It supports a wide range of [operators](#sql-operators) and [functions](#sql-functions), including complex conditions.

This example `WHERE` clause only retrieves data where:

* Factuality score is greater than 0.8
* model is "gpt-4"
* tag list includes "triage"
* input contains the word "question" (case-insensitive)
* created date is later than January 1, 2024
* more than 1000 tokens were used or the data being traced was made in production

<CodeGroup>
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
</CodeGroup>

### Single span filters

By default, each returned trace includes at least one span that matches all filter conditions. Use single span filters to find traces where different spans match different conditions. This is helpful for finding errors in tagged traces where the error may not be on the root span.

Wrap any filter expression with `any_span()` to mark it as a single span filter. This `WHERE` example returns traces with a "production" tag that encountered an error.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  WHERE
    any_span(tags INCLUDES "production") AND
    any_span(error IS NOT NULL)
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  filter:
    any_span(tags includes "production") and
    any_span(error IS NOT NULL)
  ```
</CodeGroup>

Single span filters work with the `traces` and `summary` data shapes.

### Pattern matching

SQL supports the `%` wildcard for pattern matching with `LIKE` (case-sensitive) and `ILIKE` (case-insensitive).

The `%` wildcard matches any sequence of zero or more characters.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Match any input containing "question"
  WHERE input ILIKE '%question%'

  -- Match inputs starting with "How"
  WHERE input LIKE 'How%'

  -- Match emails ending with specific domains
  WHERE metadata.email ILIKE '%@braintrust.com'

  -- Escape literal wildcards with backslash
  WHERE metadata.description LIKE '%50\% off%'  -- Matches "50% off"
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Match any input containing "question"
  filter: input ILIKE '%question%'

  -- Match inputs starting with "How"
  filter: input LIKE 'How%'

  -- Match emails ending with specific domains
  filter: metadata.email ILIKE '%@braintrust.com'

  -- Escape literal wildcards with backslash
  filter: metadata.description LIKE '%50\% off%'  -- Matches "50% off"
  ```
</CodeGroup>

### Time intervals

SQL supports intervals for time-based operations.

This query returns all project logs from 'my-project-id' that were created in the last day.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id')
  WHERE created > now() - interval 1 day
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id')
  filter: created > now() - interval 1 day
  ```
</CodeGroup>

This query returns all project logs from 'my-project-id' that were created up to an hour ago.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT *
  FROM project_logs('my-project-id')
  WHERE created > now() - interval 1 hour
    AND created < now()
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: *
  from: project_logs('my-project-id')
  filter:
    created > now() - interval 1 hour and
    created < now()
  ```
</CodeGroup>

This query returns all project logs from 'my-project-id' that were created last week and last month.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Examples with different units
  SELECT *
  FROM project_logs('my-project-id')
  WHERE created > now() - interval 7 day    -- Last week
    AND created > now() - interval 1 month  -- Last month
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Examples with different units
  select: *
  from: project_logs('my-project-id')
  filter:
    created > now() - interval 7 day and    -- Last week
    created > now() - interval 1 month      -- Last month
  ```
</CodeGroup>

## `ORDER BY`

The `ORDER BY` clause determines the order of results. The options are `DESC` (descending) and `ASC` (ascending) on a numerical field. You can sort by a single field, multiple fields, or computed values.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Sort by single field
  ORDER BY created DESC

  -- Sort by multiple fields
  ORDER BY scores.Factuality DESC, created ASC

  -- Sort by computed values
  ORDER BY len(tags) DESC
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Sort by single field
  sort: created desc

  -- Sort by multiple fields
  sort: scores.Factuality desc, created asc

  -- Sort by computed values
  sort: len(tags) desc
  ```
</CodeGroup>

## `PIVOT` and `UNPIVOT`

`PIVOT` and `UNPIVOT` are advanced operations that transform your results for easier analysis and comparison. Both SQL and BTQL syntax support these operations.

### `PIVOT`

`PIVOT` transforms rows into columns, which makes comparisons easier by creating a column for each distinct value. This is useful when comparing metrics across different categories, models, or time periods.

**Structure:**

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
SELECT <non-pivoted columns>, <pivoted columns>
FROM <table>
PIVOT(
  <AggregateFunction>(<ColumnToBeAggregated>)
  FOR <PivotColumn>
  IN (ANY)
)
```

**Requirements:**

* The pivot column must be a single identifier (e.g., `metadata.model`)
* Must include at least one aggregate measure (e.g., `SUM(value)`, `AVG(score)`)
* Only `IN (ANY)` is supported (explicit value lists, subqueries, `ORDER BY`, and `DEFAULT ON NULL` are not supported)
* `SELECT` list must include the pivot column, all measures, and all `GROUP BY` columns (or use `SELECT *`)

Pivot columns are automatically named by combining the pivot value and measure name. For example, if you pivot `metadata.model` with a model named "gpt-4" for measure `avg_score`, the column becomes `gpt-4_avg_score`. When using aliases, the alias replaces the measure name in the output column.

**Single aggregate** - pivot one metric across categories:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Compare total score values across all scores
  SELECT score, SUM(value)
  FROM project_logs('my-project-id')
  UNPIVOT (value FOR score IN (scores))
  PIVOT(SUM(value) FOR score IN (ANY))
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  dimensions: score
  measures: sum(value) as sum_value
  from: project_logs('my-project-id')
  unpivot: scores as (score, value)
  pivot: sum_value
  ```
</CodeGroup>

**Multiple aggregates** - pivot multiple metrics at once:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Compare model performance metrics across models
  SELECT day(created) AS date, metadata.model, AVG(scores.Factuality), COUNT(1)
  FROM project_logs('my-project-id')
  WHERE metadata.model IN ('gpt-4', 'gpt-3.5-turbo')
  GROUP BY day(created), metadata.model
  PIVOT(
    AVG(scores.Factuality),
    COUNT(1)
    FOR metadata.model IN (ANY)
  )
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  dimensions: day(created) as date
  measures:
    avg(scores.Factuality) as avg_factuality,
    count(1) as call_count
  from: project_logs('my-project-id')
  filter: metadata.model IN ['gpt-4', 'gpt-3.5-turbo']
  pivot: avg_factuality, call_count
  ```
</CodeGroup>

**With aliases** - name your pivoted columns:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Use custom column names
  SELECT score, total
  FROM project_logs('my-project-id')
  UNPIVOT (value FOR score IN (scores))
  PIVOT(SUM(value) AS total FOR score IN (ANY))
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  dimensions: score
  measures: sum(value) as total
  from: project_logs('my-project-id')
  unpivot: scores as (score, value)
  pivot: total
  ```
</CodeGroup>

**With grouping** - combine `PIVOT` with `GROUP BY` for multi-dimensional analysis:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Analyze scores by both model and date
  SELECT day(created) AS date, metadata.model, AVG(scores.Factuality)
  FROM project_logs('my-project-id')
  GROUP BY day(created), metadata.model
  PIVOT(AVG(scores.Factuality) FOR metadata.model IN (ANY))
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  dimensions: day(created) as date, metadata.model as model
  measures: avg(scores.Factuality) as factuality
  from: project_logs('my-project-id')
  pivot: factuality
  ```
</CodeGroup>

**Using `SELECT *`** - automatically includes all required columns:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- SELECT * includes pivot column, measures, and GROUP BY columns automatically
  SELECT *
  FROM project_logs('my-project-id')
  UNPIVOT (value FOR score IN (scores))
  PIVOT(SUM(value) FOR score IN (ANY))
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  dimensions: score
  measures: sum(value) as sum_value
  from: project_logs('my-project-id')
  unpivot: scores as (score, value)
  pivot: sum_value
  ```
</CodeGroup>

### `UNPIVOT`

`UNPIVOT` transforms columns into rows, which is useful when you need to analyze arbitrary scores and metrics without specifying each field name in advance. This is helpful when working with dynamic sets of metrics or when you want to normalize data for aggregation.

**Key-value unpivot** - transforms an object into rows with key-value pairs:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Convert scores object into rows with score names and values
  SELECT id, score, value
  FROM project_logs('my-project-id')
  UNPIVOT (value FOR score IN (scores))
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  select: id, score, value
  from: project_logs('my-project-id')
  unpivot: scores as (score, value)
  ```
</CodeGroup>

<Note>
  When using key-value unpivot, the source column must be an object (e.g., `scores`). When using array unpivot with `_`, the source column must be an array (e.g., `tags`).
</Note>

**Array unpivot** - expands arrays by using `_` as the name column:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Expand tags array into individual rows
  SELECT id, tag
  FROM project_logs('my-project-id')
  UNPIVOT (tag FOR _ IN (tags))
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  select: id, tag
  from: project_logs('my-project-id')
  unpivot: tags as (tag)
  ```
</CodeGroup>

**Multiple unpivots** - chain multiple `UNPIVOT` operations to expand multiple columns:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Expand both scores and tags
  SELECT score, tag
  FROM project_logs('my-project-id')
  UNPIVOT (value FOR score IN (scores))
  UNPIVOT (tag FOR _ IN (tags))
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  select: score, tag
  from: project_logs('my-project-id')
  unpivot: scores as (score, value), tags as (tag)
  ```
</CodeGroup>

**With aggregations** - use `UNPIVOT` with `GROUP BY` to aggregate across unpivoted rows:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Calculate average value for each score across all logs
  SELECT score, AVG(value) AS avg_value, COUNT(1) AS count
  FROM project_logs('my-project-id')
  UNPIVOT (value FOR score IN (scores))
  GROUP BY score
  ORDER BY avg_value DESC
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Equivalent BTQL syntax
  dimensions: score
  measures: avg(value) as avg_value, count(1) as count
  from: project_logs('my-project-id')
  unpivot: scores as (score, value)
  sort: avg_value desc
  ```
</CodeGroup>

## `LIMIT` and cursors

### `LIMIT`

The `LIMIT` clause controls the size of the result in number of records.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Basic limit
  LIMIT 100
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Basic limit
  limit: 100
  ```
</CodeGroup>

### Cursors for pagination

<Note>
  Cursors are only supported in BTQL syntax, not in SQL syntax.
</Note>

Cursors implement pagination in BTQL queries. Cursors are automatically returned in query responses. A default limit is applied in a query without a limit clause, and the number of returned results can be overridden by using an explicit `limit`. In order to implement pagination, after an initial query, provide the subsequent cursor token returned in the results in the `cursor` clause in follow-on queries. When a cursor has reached the end of the result set, the `data` array will be empty, and no cursor token will be returned by the query.

```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Pagination using cursor (only works without sort)
select: *
from: project_logs('<PROJECT_ID>')
limit: 100
cursor: '<CURSOR_TOKEN>'  -- From previous query response
```

Cursors can only be used for pagination when no `sort` clause is specified. If you need sorted results, you'll need to implement offset-based pagination by using the last value from your sort field as a filter in the next query.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Offset-based pagination with sorting
  -- Page 1 (first 100 results)
  SELECT *
  FROM project_logs('<PROJECT_ID>')
  ORDER BY created DESC
  LIMIT 100

  -- Page 2 (next 100 results)
  SELECT *
  FROM project_logs('<PROJECT_ID>')
  WHERE created < '2024-01-15T10:30:00Z'  -- Last created timestamp from previous page
  ORDER BY created DESC
  LIMIT 100
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Offset-based pagination with sorting
  -- Page 1 (first 100 results)
  select: *
  from: project_logs('<PROJECT_ID>')
  sort: created desc
  limit: 100

  -- Page 2 (next 100 results)
  select: *
  from: project_logs('<PROJECT_ID>')
  filter: created < '2024-01-15T10:30:00Z'  -- Last created timestamp from previous page
  sort: created desc
  limit: 100
  ```
</CodeGroup>

## Expressions

### SQL operators

You can use the following operators in your SQL queries.

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

### SQL functions

You can use the following functions in `SELECT`, `WHERE`, `GROUP BY` clauses, and aggregate measures.

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

-- Aggregate functions (only in measures/with GROUP BY)
count(expr)                       -- Count number of rows
count_distinct(expr)              -- Count number of distinct values
sum(expr)                        -- Sum numeric values
avg(expr)                        -- Calculate mean of numeric values
min(expr)                        -- Find minimum value
max(expr)                        -- Find maximum value
percentile(expr, p)              -- Calculate percentile (p between 0 and 1)
```

### Field access

SQL provides flexible ways to access nested data in arrays and objects:

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

When you have JSON data stored as a string field (rather than as native SQL objects), use the [`json_extract` function](#extract-data-from-json-strings) to access values within it. The path parameter is treated as a literal string key name:

```sql  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
-- Extract from JSON string fields
json_extract(metadata.config, 'api_key')           -- Extract the "api_key" field
json_extract(metadata.config, 'user_id')           -- Extract the "user_id" field
json_extract(output, 'result')                     -- Extract the "result" field
```

#### Implicit aliasing

When you reference multi-part identifiers (e.g., `metadata.category`), SQL automatically creates an implicit alias using the last component of the path (e.g., `category`). This allows you to use the short form in your queries when unambiguous.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Use short form in WHERE clause
  SELECT metadata.category, metadata.model
  FROM project_logs('my-project-id')
  WHERE category = 'support' AND model = 'gpt-4'

  -- Use short form in ORDER BY
  SELECT metadata.user.name
  FROM project_logs('my-project-id')
  ORDER BY name

  -- Use short form in GROUP BY
  SELECT metadata.model, COUNT(*) as cnt
  FROM project_logs('my-project-id')
  GROUP BY model
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Use short form in filter
  select: metadata.category, metadata.model
  from: project_logs('my-project-id')
  filter: category = 'support' and model = 'gpt-4'

  -- Use short form in sort
  select: metadata.user.name
  from: project_logs('my-project-id')
  sort: name

  -- Use short form in measure
  dimensions: metadata.model
  measures: count(1) as cnt
  from: project_logs('my-project-id')
  ```
</CodeGroup>

**Important notes about implicit aliasing:**

* **Ambiguity prevention**: If multiple fields share the same last component (e.g., `metadata.name` and `user.name`), the short form `name` becomes ambiguous and cannot be used. You must use the full path instead.

* **Top-level field priority**: Top-level fields take precedence over nested fields. If you have both `id` and `metadata.id`, the short form `id` refers to the top-level field.

* **Explicit aliases override**: When you provide an explicit alias (e.g., `metadata.category AS cat`), the implicit alias is disabled and you must use either the explicit alias or the full path.

* **Duplicate alias detection**: SQL will detect and reject queries with duplicate aliases in the SELECT list, whether explicit or implicit. For example, `SELECT id, user.number AS id` will raise an error.

**Examples of ambiguous references:**

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- ERROR: Cannot use 'name' - ambiguous between two fields
  SELECT metadata.name, user.name
  FROM project_logs('my-project-id')
  ORDER BY name  -- Error: ambiguous

  -- CORRECT: Use full path when ambiguous
  SELECT metadata.name, user.name
  FROM project_logs('my-project-id')
  ORDER BY metadata.name
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- ERROR: Cannot use 'name' - ambiguous between two fields
  select: metadata.name, user.name
  from: project_logs('my-project-id')
  sort: name  -- Error: ambiguous

  -- CORRECT: Use full path when ambiguous
  select: metadata.name, user.name
  from: project_logs('my-project-id')
  sort: metadata.name
  ```
</CodeGroup>

**Freeing up short forms with explicit aliases:**

When one field uses an explicit alias, its short form becomes available for other fields:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- 'user_name' is the explicit alias, 'name' now refers to metadata.name
  SELECT user.name AS user_name, metadata.name
  FROM project_logs('my-project-id')
  WHERE name = 'configuration'  -- Refers to metadata.name
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- 'user_name' is the explicit alias, 'name' now refers to metadata.name
  select: user.name as user_name, metadata.name
  from: project_logs('my-project-id')
  filter: name = 'configuration'  -- Refers to metadata.name
  ```
</CodeGroup>

### Conditional expressions

SQL supports conditional logic using the ternary operator (`? :`):

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Basic conditions
  SELECT
    (scores.Factuality > 0.8 ? "high" : "low") AS quality,
    (error IS NOT NULL ? -1 : metrics.tokens) AS valid_tokens
  FROM project_logs('my-project-id')
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Basic conditions
  select:
    (scores.Factuality > 0.8 ? "high" : "low") as quality,
    (error IS NOT NULL ? -1 : metrics.tokens) as valid_tokens
  from: project_logs('my-project-id')
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Nested conditions
  SELECT
    (scores.Factuality > 0.9 ? "excellent" :
     scores.Factuality > 0.7 ? "good" :
     scores.Factuality > 0.5 ? "fair" : "poor") AS rating
  FROM project_logs('my-project-id')
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Nested conditions
  select:
    (scores.Factuality > 0.9 ? "excellent" :
     scores.Factuality > 0.7 ? "good" :
     scores.Factuality > 0.5 ? "fair" : "poor") as rating
  from: project_logs('my-project-id')
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Use in calculations
  SELECT
    (metadata.model = "gpt-4" ? metrics.tokens * 2 : metrics.tokens) AS adjusted_tokens,
    (error IS NULL ? metrics.latency : 0) AS valid_latency
  FROM project_logs('my-project-id')
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Use in calculations
  select:
    (metadata.model = "gpt-4" ? metrics.tokens * 2 : metrics.tokens) as adjusted_tokens,
    (error IS NULL ? metrics.latency : 0) as valid_latency
  from: project_logs('my-project-id')
  ```
</CodeGroup>

## Examples

### Track token usage

This query helps you monitor token consumption across your application.

<CodeGroup>
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
</CodeGroup>

<CodeGroup>
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
</CodeGroup>

<CodeGroup>
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
</CodeGroup>

### Analyze errors

Identify and investigate errors in your application.

<CodeGroup>
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
</CodeGroup>

<CodeGroup>
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
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Exclude known error types from analysis
  SELECT *
  FROM project_logs('<PROJECT_ID>')
  WHERE error IS NOT NULL
    AND error.type NOT IN ('rate_limit', 'timeout', 'network_error')
    AND metadata.is_production = true
    AND created > now() - interval 1 day
  ORDER BY created DESC
  LIMIT 100
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
</CodeGroup>

### Analyze latency

Monitor and optimize response times.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Track p95 latency by endpoint
  SELECT
    metadata.endpoint AS endpoint,
    hour(created) AS hour,
    percentile(metrics.latency, 0.95) AS p95_latency,
    percentile(metrics.latency, 0.50) AS median_latency,
    count(1) AS requests
  FROM project_logs('<PROJECT_ID>')
  WHERE created > now() - interval 1 day
  GROUP BY 1, 2
  ORDER BY hour DESC, p95_latency DESC
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Find slow requests
  SELECT
    metadata.endpoint,
    metrics.latency,
    metrics.tokens,
    input,
    created
  FROM project_logs('<PROJECT_ID>')
  WHERE metrics.latency > 5000  -- Requests over 5 seconds
    AND created > now() - interval 1 hour
  ORDER BY metrics.latency DESC
  LIMIT 20
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
</CodeGroup>

### Analyze prompts

Analyze prompt effectiveness and patterns.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Track prompt token efficiency
  SELECT
    metadata.prompt_template AS template,
    day(created) AS date,
    avg(metrics.prompt_tokens) AS avg_prompt_tokens,
    avg(metrics.completion_tokens) AS avg_completion_tokens,
    avg(metrics.completion_tokens) / avg(metrics.prompt_tokens) AS token_efficiency,
    avg(scores.Factuality) AS avg_factuality
  FROM project_logs('<PROJECT_ID>')
  WHERE created > now() - interval 7 day
  GROUP BY 1, 2
  ORDER BY date DESC, token_efficiency DESC
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Find similar prompts
  SELECT *
  FROM project_logs('<PROJECT_ID>')
  WHERE input MATCH 'explain the concept of recursion'
    AND scores.Factuality > 0.8
  ORDER BY created DESC
  LIMIT 10
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Find similar prompts
  select: *
  from: project_logs('<PROJECT_ID>')
  filter:
    input MATCH 'explain the concept of recursion' and
    scores.Factuality > 0.8
  sort: created desc
  limit: 10
  ```
</CodeGroup>

### Analyze based on tags

Use tags to track and analyze specific behaviors.

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Monitor feedback patterns
  SELECT
    tags[0] AS primary_tag,
    metadata.model AS model,
    count(1) AS feedback_count,
    avg(scores.Factuality > 0.8 ? 1 : 0) AS high_quality_rate
  FROM project_logs('<PROJECT_ID>')
  WHERE tags INCLUDES 'feedback'
    AND created > now() - interval 30 day
  GROUP BY 1, 2
  ORDER BY feedback_count DESC
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Track issue resolution
  SELECT
    created,
    tags,
    metadata.model,
    scores.Factuality,
    response
  FROM project_logs('<PROJECT_ID>')
  WHERE tags INCLUDES 'needs-review'
    AND NOT tags INCLUDES 'resolved'
    AND created > now() - interval 1 day
  ORDER BY scores.Factuality ASC
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
</CodeGroup>

### Extract data from JSON strings

Use `json_extract` to extract values from a JSON string using a key name. This is useful when you have JSON data stored as a string field and need to access specific values within it. The path parameter is treated as a literal key name (not a path expression with traversal).

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract a simple field
  SELECT
    id,
    json_extract(metadata.config, 'api_key') AS api_key
  FROM project_logs('my-project-id')
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract a simple field
  select:
    id,
    json_extract(metadata.config, 'api_key') as api_key
  from: project_logs('my-project-id')
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract fields with special characters in the key name
  SELECT
    id,
    json_extract(metadata.settings, 'user.preferences.theme') AS theme_key
  FROM project_logs('my-project-id')
  -- Note: This extracts a key literally named "user.preferences.theme", not a nested path
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract fields with special characters in the key name
  select:
    id,
    json_extract(metadata.settings, 'user.preferences.theme') as theme_key
  from: project_logs('my-project-id')
  -- Note: This extracts a key literally named "user.preferences.theme", not a nested path
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract and filter
  SELECT *
  FROM project_logs('my-project-id')
  WHERE json_extract(metadata.config, 'environment') = 'production'
    AND json_extract(metadata.config, 'version') > 2.0
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  -- Extract and filter
  select: *
  from: project_logs('my-project-id')
  filter:
    json_extract(metadata.config, 'environment') = 'production' and
    json_extract(metadata.config, 'version') > 2.0
  ```
</CodeGroup>

<Note>
  `json_extract` returns `null` for invalid JSON or missing keys rather than raising an error, making it safe to use in filters and aggregations. The path parameter is a literal key name, not a path expression - characters like dots, brackets, etc. are treated as part of the key name itself.
</Note>
