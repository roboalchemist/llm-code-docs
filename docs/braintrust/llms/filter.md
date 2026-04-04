# Source: https://braintrust.dev/docs/observe/filter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter and search logs

> Find specific traces using filters, SQL, and API access

Braintrust provides multiple ways to filter and search your logs, from quick UI filters to programmatic API access.

## Filter menu

Select <Icon icon="list-filter" /> **Filter** to open the filter menu with quick filters for common fields like tags, time range, and comments.

Use the **Basic** tab for point-and-click filtering, or switch to **SQL** to write precise queries. The SQL editor includes <Icon icon="blend" /> **Generate** button that creates queries from natural language descriptions.

### Write SQL queries

Write SQL queries for precise filtering. When filtering logs, you can use either SQL or BTQL syntax:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  WHERE scores.Factuality > 0.8
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  filter: scores.Factuality > 0.8
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  WHERE tags INCLUDES "production" AND metadata.user_id = "user-123"
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  filter: tags includes "production" and metadata.user_id == "user-123"
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  WHERE created >= "2024-01-01" AND duration < 2.0
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  filter: created >= "2024-01-01" and duration < 2.0
  ```
</CodeGroup>

Both syntaxes support standard operators (`=`, `!=`, `>`, `<`, `>=`, `<=`), logical operators (`AND`/`and`, `OR`/`or`, `NOT`/`not`), and functions like `INCLUDES`/`includes` for array membership.

For complete SQL documentation, see the [SQL reference](/reference/sql).

## Loop and deep search

Use AI-powered search to find traces based on meaning rather than exact keywords.

<Note>
  The search methods below help you filter and find traces across your entire project. To search within a single trace, use [thread view search](/observe/view-logs#view-as-a-thread).
</Note>

### Ask questions with Loop

Select <Icon icon="blend" /> **Loop** on the <Icon icon="activity" /> **Logs** page or when viewing individual traces to ask natural language questions. Loop understands your data structure and can answer questions, identify patterns, and help you find specific traces.

Example queries:

* "Show me traces where the user was confused"
* "Find requests that took longer than usual"
* "What are the most common error patterns?"
* "Summarize this trace" (when viewing an individual trace)

See [Analyze logs](/observe/loop#analyze-logs) and [Analyze individual traces](/observe/loop#analyze-individual-traces) for more details.

### Find similar traces

Select rows in the logs table and use <Icon icon="glasses" /> **Find similar traces**. Loop analyzes the selected traces to identify common traits and returns similar traces based on semantic meaning.

### Use deep search

Deep search finds traces based on semantic similarity rather than keyword matching. This helps you discover patterns, sentiment, and edge cases that traditional filtering might miss.

See [Use deep search](/observe/deep-search) for detailed examples and workflows.

## API access

Query logs programmatically using the Braintrust API for automation, integrations, and custom tooling.

### Basic filtering

Use the [project logs endpoint](/api-reference/logs/fetch-project-logs-get-form) for simple filters and programmatic access:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
curl -X GET "https://api.braintrust.dev/v1/project/<PROJECT_ID>/logs" \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Content-Type: application/json"
```

### Advanced SQL queries

For complex queries, use the [Braintrust API](/reference/sql#api-access):

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
curl -X POST https://api.braintrust.dev/btql \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "select: * | from: project_logs('"'<PROJECT_ID>'"') | filter: scores.Factuality > 0.8 | limit: 100"
  }'
```

The API accepts these parameters:

* `query` (required): Your BTQL query string
* `fmt`: Response format (`json` or `parquet`, defaults to `json`)
* `tz_offset`: Timezone offset in minutes for correct day boundaries
* `audit_log`: Include audit log data

## Next steps

* [Use deep search](/observe/deep-search) for semantic queries
* [Score online](/observe/score-online) to evaluate filtered traces
* [Create dashboards](/observe/dashboards) with filtered metrics
* Read the [SQL reference](/reference/sql) for complete query syntax
