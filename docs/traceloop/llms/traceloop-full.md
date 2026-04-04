# Traceloop Documentation

Source: https://www.traceloop.com/docs/llms-full.txt

---

# Create an auto monitor setup
Source: https://www.traceloop.com/docs/api-reference/auto-monitor-setups/create-an-auto-monitor-setup

post /v2/auto-monitor-setups
Create a new auto monitor setup for automatic monitor creation



# Delete an auto monitor setup
Source: https://www.traceloop.com/docs/api-reference/auto-monitor-setups/delete-an-auto-monitor-setup

delete /v2/auto-monitor-setups/{setup_id}
Delete an auto monitor setup by ID



# Get an auto monitor setup by ID
Source: https://www.traceloop.com/docs/api-reference/auto-monitor-setups/get-an-auto-monitor-setup-by-id

get /v2/auto-monitor-setups/{setup_id}
Get a specific auto monitor setup by its ID



# List auto monitor setups
Source: https://www.traceloop.com/docs/api-reference/auto-monitor-setups/list-auto-monitor-setups

get /v2/auto-monitor-setups
List all auto monitor setups for the organization with optional filters



# Update an auto monitor setup
Source: https://www.traceloop.com/docs/api-reference/auto-monitor-setups/update-an-auto-monitor-setup

put /v2/auto-monitor-setups/{setup_id}
Update an existing auto monitor setup by ID



# Get costs by property
Source: https://www.traceloop.com/docs/api-reference/costs/property_costs

GET https://api.traceloop.com/v2/costs/by-association-property

Query your LLM costs broken down by a specific association property. This helps you understand how costs are distributed across different values of a property (e.g., by user\_id, session\_id, or any other association property you track).

## Request Parameters

<ParamField type="string">
  The name of the association property to group costs by (e.g., "user\_id", "session\_id").
</ParamField>

<ParamField type="string">
  The start time in ISO 8601 format (e.g., "2025-04-15T00:00:00Z").
</ParamField>

<ParamField type="string">
  The end time in ISO 8601 format (e.g., "2025-04-28T23:00:00Z").
</ParamField>

<ParamField type="string">
  List of environments to include in the calculation. Separated by comma.
</ParamField>

<ParamField type="string">
  <span>NEW</span> Filter costs by specific token types. Separate multiple types with commas.

  **Supported token types:**

  * `input_tokens` or `prompt_tokens` (automatically normalized to `prompt_tokens`)
  * `output_tokens` or `completion_tokens` (automatically normalized to `completion_tokens`)
  * `cache_read_input_tokens`
  * `cache_creation_input_tokens`
  * Other token types as they appear in your data

  **Note:** `total_tokens` cannot be used as a filter.

  **Examples:**

  * `selected_token_types=input_tokens,output_tokens`
  * `selected_token_types=prompt_tokens,cache_read_input_tokens`
  * `selected_token_types=completion_tokens`

  When this parameter is omitted, costs for all token types are included.
</ParamField>

## Response

<ResponseField name="property_name" type="string">
  The name of the property that was queried.
</ResponseField>

<ResponseField name="values" type="PropertyValue[]">
  A list of property values and their associated costs.
</ResponseField>

<ResponseField name="total_cost" type="number">
  The total cost across all property values.
</ResponseField>

```json theme={null}
{
  "property_name": "session_id",
  "values": [
    {
      "value": "session_21",
      "cost": 1.23
    },
    {
      "value": "session_5",
      "cost": 4.56
    },
    {
      "value": "No_Value",
      "cost": 0.78
    }
  ],
  "total_cost": 6.57
}
```

The API can return special values:

* `"No_Association"` as property\_name if no spans have the requested association properties
* `"No_Value"` as a value for spans that don't have a value for the specified property
* `"Unknown_Value"` for spans where the property exists but has an empty value


# Execute agent-efficiency evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-efficiency-evaluator

post /v2/evaluators/execute/agent-efficiency
Evaluate agent efficiency - detect redundant calls, unnecessary follow-ups

**Request Body:**
- `input.trajectory_prompts` (string, required): JSON array of prompts in the agent trajectory
- `input.trajectory_completions` (string, required): JSON array of completions in the agent trajectory



# Execute agent-flow-quality evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-flow-quality-evaluator

post /v2/evaluators/execute/agent-flow-quality
Validate agent trajectory against user-defined conditions

**Request Body:**
- `input.trajectory_prompts` (string, required): JSON array of prompts in the agent trajectory
- `input.trajectory_completions` (string, required): JSON array of completions in the agent trajectory
- `config.conditions` (array of strings, required): Array of evaluation conditions/rules to validate against
- `config.threshold` (number, required): Score threshold for pass/fail determination (0.0-1.0)



# Execute agent-goal-accuracy evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-goal-accuracy-evaluator

post /v2/evaluators/execute/agent-goal-accuracy
Evaluate agent goal accuracy

**Request Body:**
- `input.question` (string, required): The original question or goal
- `input.completion` (string, required): The agent's completion/response
- `input.reference` (string, required): The expected reference answer



# Execute agent-goal-completeness evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-goal-completeness-evaluator

post /v2/evaluators/execute/agent-goal-completeness
Measure if agent accomplished all user goals

**Request Body:**
- `input.trajectory_prompts` (string, required): JSON array of prompts in the agent trajectory
- `input.trajectory_completions` (string, required): JSON array of completions in the agent trajectory
- `config.threshold` (number, required): Score threshold for pass/fail determination (0.0-1.0)



# Execute agent-tool-error-detector evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-tool-error-detector-evaluator

post /v2/evaluators/execute/agent-tool-error-detector
Detect errors or failures during tool execution

**Request Body:**
- `input.tool_input` (string, required): JSON string of the tool input
- `input.tool_output` (string, required): JSON string of the tool output



# Execute agent-tool-trajectory evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-agent-tool-trajectory-evaluator

post /v2/evaluators/execute/agent-tool-trajectory
Compare actual tool calls against expected reference tool calls

**Request Body:**
- `input.executed_tool_calls` (string, required): JSON array of actual tool calls made by the agent
- `input.expected_tool_calls` (string, required): JSON array of expected/reference tool calls
- `config.threshold` (float, optional): Score threshold for pass/fail determination (default: 0.5)
- `config.mismatch_sensitive` (bool, optional): Whether tool calls must match exactly (default: false)
- `config.order_sensitive` (bool, optional): Whether order of tool calls matters (default: false)
- `config.input_params_sensitive` (bool, optional): Whether to compare input parameters (default: true)



# Execute answer-completeness evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-answer-completeness-evaluator

post /v2/evaluators/execute/answer-completeness
Evaluate whether the answer is complete and contains all the necessary information

**Request Body:**
- `input.question` (string, required): The original question
- `input.completion` (string, required): The completion to evaluate for completeness
- `input.context` (string, required): The context that provides the complete information



# Execute answer-correctness evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-answer-correctness-evaluator

post /v2/evaluators/execute/answer-correctness
Evaluate factual accuracy by comparing answers against ground truth

**Request Body:**
- `input.question` (string, required): The original question
- `input.completion` (string, required): The completion to evaluate
- `input.ground_truth` (string, required): The expected correct answer



# Execute answer-relevancy evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-answer-relevancy-evaluator

post /v2/evaluators/execute/answer-relevancy
Check if an answer is relevant to a question

**Request Body:**
- `input.answer` (string, required): The answer to evaluate for relevancy
- `input.question` (string, required): The question that the answer should be relevant to



# Execute char-count evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-char-count-evaluator

post /v2/evaluators/execute/char-count
Count the number of characters in text

**Request Body:**
- `input.text` (string, required): The text to count characters in



# Execute char-count-ratio evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-char-count-ratio-evaluator

post /v2/evaluators/execute/char-count-ratio
Calculate the ratio of characters between two texts

**Request Body:**
- `input.numerator_text` (string, required): The numerator text (will be divided by denominator)
- `input.denominator_text` (string, required): The denominator text (divides the numerator)



# Execute context-relevance evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-context-relevance-evaluator

post /v2/evaluators/execute/context-relevance
Evaluate whether retrieved context contains sufficient information to answer the query

**Request Body:**
- `input.query` (string, required): The query/question to evaluate context relevance for
- `input.context` (string, required): The context to evaluate for relevance to the query
- `config.model` (string, optional): Model to use for evaluation (default: gpt-4o)



# Execute conversation-quality evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-conversation-quality-evaluator

post /v2/evaluators/execute/conversation-quality
Evaluate conversation quality based on tone, clarity, flow, responsiveness, and transparency

**Request Body:**
- `input.prompts` (string, required): JSON array of prompts in the conversation
- `input.completions` (string, required): JSON array of completions in the conversation



# Execute faithfulness evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-faithfulness-evaluator

post /v2/evaluators/execute/faithfulness
Check if a completion is faithful to the provided context

**Request Body:**
- `input.completion` (string, required): The LLM completion to check for faithfulness
- `input.context` (string, required): The context that the completion should be faithful to
- `input.question` (string, required): The original question asked



# Execute html-comparison evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-html-comparison-evaluator

post /v2/evaluators/execute/html-comparison
Compare two HTML documents for structural and content similarity

**Request Body:**
- `input.html1` (string, required): The first HTML document to compare
- `input.html2` (string, required): The second HTML document to compare



# Execute instruction-adherence evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-instruction-adherence-evaluator

post /v2/evaluators/execute/instruction-adherence
Evaluate how well responses follow given instructions

**Request Body:**
- `input.instructions` (string, required): The instructions that should be followed
- `input.response` (string, required): The response to evaluate for instruction adherence



# Execute intent-change evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-intent-change-evaluator

post /v2/evaluators/execute/intent-change
Detect changes in user intent between prompts and completions

**Request Body:**
- `input.prompts` (string, required): JSON array of prompts in the conversation
- `input.completions` (string, required): JSON array of completions in the conversation



# Execute json-validator evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-json-validator-evaluator

post /v2/evaluators/execute/json-validator
Validate JSON syntax

**Request Body:**
- `input.text` (string, required): The text to validate as JSON
- `config.enable_schema_validation` (bool, optional): Enable JSON schema validation
- `config.schema_string` (string, optional): JSON schema to validate against



# Execute perplexity evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-perplexity-evaluator

post /v2/evaluators/execute/perplexity
Measure text perplexity from logprobs

**Request Body:**
- `input.logprobs` (string, required): JSON array of log probabilities from the model



# Execute pii-detector evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-pii-detector-evaluator

post /v2/evaluators/execute/pii-detector
Detect personally identifiable information in text

**Request Body:**
- `input.text` (string, required): The text to scan for personally identifiable information
- `config.probability_threshold` (float, optional): Detection threshold (default: 0.8)



# Execute placeholder-regex evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-placeholder-regex-evaluator

post /v2/evaluators/execute/placeholder-regex
Validate text against a placeholder regex pattern

**Request Body:**
- `input.placeholder_value` (string, required): The regex pattern to match against
- `input.text` (string, required): The text to validate against the regex pattern
- `config.should_match` (bool, optional): Whether the text should match the regex
- `config.case_sensitive` (bool, optional): Case-sensitive matching
- `config.dot_include_nl` (bool, optional): Dot matches newlines
- `config.multi_line` (bool, optional): Multi-line mode



# Execute profanity-detector evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-profanity-detector-evaluator

post /v2/evaluators/execute/profanity-detector
Detect profanity in text

**Request Body:**
- `input.text` (string, required): The text to scan for profanity



# Execute prompt-injection evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-prompt-injection-evaluator

post /v2/evaluators/execute/prompt-injection
Detect prompt injection attempts

**Request Body:**
- `input.prompt` (string, required): The prompt to check for injection attempts
- `config.threshold` (float, optional): Detection threshold (default: 0.5)



# Execute prompt-perplexity evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-prompt-perplexity-evaluator

post /v2/evaluators/execute/prompt-perplexity
Measure prompt perplexity to detect potential injection attempts

**Request Body:**
- `input.prompt` (string, required): The prompt to calculate perplexity for



# Execute regex-validator evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-regex-validator-evaluator

post /v2/evaluators/execute/regex-validator
Validate text against a regex pattern

**Request Body:**
- `input.text` (string, required): The text to validate against a regex pattern
- `config.regex` (string, optional): The regex pattern to match against
- `config.should_match` (bool, optional): Whether the text should match the regex
- `config.case_sensitive` (bool, optional): Case-sensitive matching
- `config.dot_include_nl` (bool, optional): Dot matches newlines
- `config.multi_line` (bool, optional): Multi-line mode



# Execute secrets-detector evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-secrets-detector-evaluator

post /v2/evaluators/execute/secrets-detector
Detect secrets and credentials in text

**Request Body:**
- `input.text` (string, required): The text to scan for secrets (API keys, passwords, etc.)



# Execute semantic-similarity evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-semantic-similarity-evaluator

post /v2/evaluators/execute/semantic-similarity
Calculate semantic similarity between completion and reference

**Request Body:**
- `input.completion` (string, required): The completion text to compare
- `input.reference` (string, required): The reference text to compare against



# Execute sexism-detector evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-sexism-detector-evaluator

post /v2/evaluators/execute/sexism-detector
Detect sexist language and bias

**Request Body:**
- `input.text` (string, required): The text to scan for sexist content
- `config.threshold` (float, optional): Detection threshold (default: 0.5)



# Execute sql-validator evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-sql-validator-evaluator

post /v2/evaluators/execute/sql-validator
Validate SQL query syntax

**Request Body:**
- `input.text` (string, required): The text to validate as SQL



# Execute tone-detection evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-tone-detection-evaluator

post /v2/evaluators/execute/tone-detection
Detect the tone of the text

**Request Body:**
- `input.text` (string, required): The text to detect the tone of



# Execute topic-adherence evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-topic-adherence-evaluator

post /v2/evaluators/execute/topic-adherence
Evaluate topic adherence

**Request Body:**
- `input.question` (string, required): The original question
- `input.completion` (string, required): The completion to evaluate
- `input.reference_topics` (string, required): Comma-separated list of expected topics



# Execute toxicity-detector evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-toxicity-detector-evaluator

post /v2/evaluators/execute/toxicity-detector
Detect toxic or harmful language

**Request Body:**
- `input.text` (string, required): The text to scan for toxic content
- `config.threshold` (float, optional): Detection threshold (default: 0.5)



# Execute uncertainty-detector evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-uncertainty-detector-evaluator

post /v2/evaluators/execute/uncertainty-detector
Detect uncertainty in the text

**Request Body:**
- `input.prompt` (string, required): The text to detect uncertainty in



# Execute word-count evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-word-count-evaluator

post /v2/evaluators/execute/word-count
Count the number of words in text

**Request Body:**
- `input.text` (string, required): The text to count words in



# Execute word-count-ratio evaluator
Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-word-count-ratio-evaluator

post /v2/evaluators/execute/word-count-ratio
Calculate the ratio of words between two texts

**Request Body:**
- `input.numerator_text` (string, required): The numerator text (will be divided by denominator)
- `input.denominator_text` (string, required): The denominator text (divides the numerator)



# Introduction
Source: https://www.traceloop.com/docs/api-reference/introduction



The following is a list of publicly available APIs you can use with the [Traceloop platform](https://app.traceloop.com).

All APIs require an API key to be used for authentication.

## Authentication

Use your API key as a Bearer token in the `Authorization` header:

```bash theme={null}
Authorization: Bearer YOUR_API_KEY
```

<Tip>
  The same API key you use to send traces to Traceloop can be used to query your data via the API.
</Tip>

<Note>
  **To generate an API key:**

  1. [Sign up](https://app.traceloop.com) for a Traceloop account if you haven't already
  2. Go to [Settings → Organization](https://app.traceloop.com/settings/api-keys)
  3. Select a project and environment
  4. Click **Generate API key** and copy it immediately

  [Detailed instructions →](/settings/managing-api-keys)
</Note>


# Get metrics high water mark
Source: https://www.traceloop.com/docs/api-reference/metrics/get-metrics-high-water-mark

get /v2/metrics_hwm
Returns the timestamp of the last successfully processed evaluation (high water mark)



# Get metrics with filtering and grouping
Source: https://www.traceloop.com/docs/api-reference/metrics/get-metrics-with-filtering-and-grouping

post /v2/metrics
Retrieves metrics data with support for filtering, sorting, and pagination. Metrics are grouped by metric name with individual data points. Supports filtering by direct column fields (bool_value, trace_id, etc.), label fields (labels.agent_name, labels.trace_id), and attribute fields (attributes.*).



# Create a new organization
Source: https://www.traceloop.com/docs/api-reference/organizations/create-a-new-organization

post /v2/organizations
Create a new organization with environments and API keys.



# Delete specific user data
Source: https://www.traceloop.com/docs/api-reference/privacy/delete_request

DELETE https://app.traceloop.com/api/config/privacy/data-deletion

You can delete traces data for a specific user of yours by specifying their association properties.

## Request Body

<ParamField type="JSON">
  A list of users to delete, each specific using a specific criterion for deletion like `{userId: "123"}`.
</ParamField>

```json theme={null}
{
  "associationProperties": [
    {
      "userId": "123"
    }
  ]
}
```

## Response

<ResponseField name="requestId" type="string">
  The request ID for this deletion request. You can use it to query the status
  of the deletion.
</ResponseField>

```
```


# Status of user deletion request
Source: https://www.traceloop.com/docs/api-reference/privacy/delete_status

GET https://app.traceloop.com/api/config/privacy/data-deletion

Get the status of your user deletion request.

## Request Query Parameter

<ParamField type="string">
  The request ID from the user deletion request.
</ParamField>

## Response

<ResponseField name="completed" type="boolean">
  `true` if the process was completed, `false` otherwise.
</ResponseField>

<ResponseField name="deleted" type="string">
  The number of spans that were deleted.
</ResponseField>

<ResponseField name="total" type="string">
  The number of spans that needs to be deleted in total.
</ResponseField>


# Disable logging of prompts and responses for specific users
Source: https://www.traceloop.com/docs/api-reference/tracing/delete_whitelisted_user

DELETE https://app.traceloop.com/api/config/pii/tracing-allow-list

By default, all prompts and responses are logged.
If you've disabled this behavior by following [this guide](/openllmetry/privacy/traces),
and then [selectively enabled it for some of your users](/api-reference/tracing/whitelist_user) then you
can use this API to disable it for previously enabled ones.

## Request Body

<ParamField type="Associated Property Object">
  A single association property (like `{userId: "123"}`) that was previously allowed to be logged.
</ParamField>

Example:

```json theme={null}
{
  "associationProperty": {
    "userId": "123"
  }
}
```


# Get identifiers of users that are allowed to be logged
Source: https://www.traceloop.com/docs/api-reference/tracing/get_whitelisted_users

GET https://app.traceloop.com/api/config/pii/tracing-allow-list

By default, all prompts and responses are logged.
If you've disabled this behavior by following [this guide](/openllmetry/privacy/traces),
and then [selectively enabled it for some of your users](/api-reference/tracing/whitelist_user) then you
can use this API to view which users you've enabled.

## Response

<ResponseField name="associationPropertyAllowList" type="JSON">
  The list of users that are allowed to be logged. Listed using their
  association properties.
</ResponseField>

```json theme={null}
{
  "associationPropertyAllowList": [
    {
      "userId": "123"
    },
    {
      "userId": "456",
      "chatId": "abc"
    }
  ]
}
```


# Enable logging of prompts and responses
Source: https://www.traceloop.com/docs/api-reference/tracing/whitelist_user

POST https://app.traceloop.com/api/config/pii/tracing-allow-list

By default, all prompts and responses are logged.
If you want to disable this behavior by following [this guide](/openllmetry/privacy/traces),
you can selectively enable it for some of your users with this API.

## Request Body

<ParamField type="Associated Property Object">
  The list of association properties (like `{userId: "123"}`) that will be allowed to be logged.
</ParamField>

Example:

```json theme={null}
{
  "associationPropertyAllowList": [
    {
      "userId": "123"
    }
  ]
}
```


# Get Spans
Source: https://www.traceloop.com/docs/api-reference/warehouse/get_spans

GET https://api.traceloop.com/v2/warehouse/spans

Retrieve spans from the data warehouse with flexible filtering and pagination options. This endpoint returns spans from the environment associated with your API key. You can filter by time ranges, workflows, attributes, and more.

## Request Parameters

<ParamField type="int64">
  Start time in Unix seconds timestamp.
</ParamField>

<ParamField type="int64">
  End time in Unix seconds timestamp.
</ParamField>

<ParamField type="string">
  Filter spans by workflow name.
</ParamField>

<ParamField type="string">
  Filter spans by span name.
</ParamField>

<ParamField type="map[string]string">
  Simple key-value attribute filtering. Any query parameter not matching a known field is treated as an attribute filter.

  **Example:** `?llm.vendor=openai&llm.request.model=gpt-4`
</ParamField>

<ParamField type="string">
  Sort order for results. Accepted values: `ASC` or `DESC`. Defaults to `ASC`.
</ParamField>

<ParamField type="string">
  Field to sort by. Supported values:

  * `timestamp` - Span creation time
  * `duration_ms` - Span duration in milliseconds
  * `span_name` - Name of the span
  * `trace_id` - Trace identifier
  * `total_tokens` - Total token count
  * `traceloop_workflow_name` - Workflow name
  * `traceloop_entity_name` - Entity name
  * `llm_usage_total_tokens` - LLM token usage
  * `llm_response_model` - LLM model used
</ParamField>

<ParamField type="string">
  Pagination cursor for fetching the next set of results. Use the `next_cursor` value from the previous response.
</ParamField>

<ParamField type="int">
  Maximum number of spans to return per page.
</ParamField>

<ParamField type="FilterCondition[]">
  Array of filter conditions to apply to the query. Each filter should have `id`, `value`, and `operator` fields. Filters must be URL-encoded JSON.

  **Filter structure:**

  ```json theme={null}
  [{"id": "field_name", "operator": "equals", "value": "value"}]
  ```

  **Supported operators:**

  | Operator                | Description                            |
  | ----------------------- | -------------------------------------- |
  | `equals`                | Exact match                            |
  | `not_equals`            | Not equal to value                     |
  | `greater_than`          | Greater than (numeric)                 |
  | `greater_than_or_equal` | Greater than or equal (numeric)        |
  | `less_than`             | Less than (numeric)                    |
  | `less_than_or_equal`    | Less than or equal (numeric)           |
  | `contains`              | String contains value                  |
  | `starts_with`           | String starts with value               |
  | `in`                    | Value in list (use with array)         |
  | `not_in`                | Value not in list (use with array)     |
  | `exists`                | Field exists (no value needed)         |
  | `not_exists`            | Field does not exist (no value needed) |

  **Example - Filter by LLM vendor:**

  ```
  ?filters=[{"id":"llm.vendor","operator":"equals","value":"openai"}]
  ```
</ParamField>

## Response

Returns a paginated response containing span objects:

<ResponseField name="spans" type="object">
  <Expandable title="spans object">
    <ResponseField name="data" type="Span[]">
      Array of span objects.
    </ResponseField>

    <ResponseField name="page_size" type="int">
      Number of spans returned in this page.
    </ResponseField>

    <ResponseField name="total_results" type="int64">
      Total number of matching spans.
    </ResponseField>

    <ResponseField name="next_cursor" type="string">
      Cursor to use for fetching the next page of results.
    </ResponseField>
  </Expandable>
</ResponseField>

### Span Object

<ResponseField name="environment" type="string">
  The environment where the span was captured.
</ResponseField>

<ResponseField name="timestamp" type="int64">
  The timestamp when the span was created (Unix milliseconds).
</ResponseField>

<ResponseField name="trace_id" type="string">
  The unique trace identifier.
</ResponseField>

<ResponseField name="span_id" type="string">
  The unique span identifier.
</ResponseField>

<ResponseField name="parent_span_id" type="string">
  The parent span identifier.
</ResponseField>

<ResponseField name="trace_state" type="string">
  The trace state information.
</ResponseField>

<ResponseField name="span_name" type="string">
  The name of the span.
</ResponseField>

<ResponseField name="span_kind" type="string">
  The kind of span (e.g., `SPAN_KIND_CLIENT`, `SPAN_KIND_INTERNAL`).
</ResponseField>

<ResponseField name="service_name" type="string">
  The name of the service that generated the span.
</ResponseField>

<ResponseField name="resource_attributes" type="map">
  Key-value pairs of resource attributes.
</ResponseField>

<ResponseField name="scope_name" type="string">
  The instrumentation scope name.
</ResponseField>

<ResponseField name="scope_version" type="string">
  The instrumentation scope version.
</ResponseField>

<ResponseField name="span_attributes" type="map">
  Key-value pairs of span attributes (e.g., `llm.vendor`, `llm.request.model`).
</ResponseField>

<ResponseField name="duration" type="int64">
  The duration of the span in milliseconds.
</ResponseField>

<ResponseField name="status_code" type="string">
  The status code of the span (e.g., `STATUS_CODE_UNSET`, `STATUS_CODE_ERROR`).
</ResponseField>

<ResponseField name="status_message" type="string">
  The status message providing additional context.
</ResponseField>

<ResponseField name="prompts" type="map">
  Prompt data associated with the span (for LLM calls).
</ResponseField>

<ResponseField name="completions" type="map">
  Completion data associated with the span (for LLM calls).
</ResponseField>

<ResponseField name="input" type="string">
  Input data for the span.
</ResponseField>

<ResponseField name="output" type="string">
  Output data for the span.
</ResponseField>

## Example Response

```json theme={null}
{
  "spans": {
    "data": [
      {
        "environment": "production",
        "timestamp": 1734451200000,
        "trace_id": "a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7",
        "span_id": "1a2b3c4d5e6f7a8b",
        "parent_span_id": "9f8e7d6c5b4a3210",
        "trace_state": "",
        "span_name": "openai.chat",
        "span_kind": "SPAN_KIND_CLIENT",
        "service_name": "my-llm-app",
        "resource_attributes": {
          "service.name": "my-llm-app",
          "telemetry.sdk.language": "python",
          "telemetry.sdk.name": "opentelemetry",
          "telemetry.sdk.version": "1.38.0"
        },
        "scope_name": "opentelemetry.instrumentation.openai.v1",
        "scope_version": "0.47.5",
        "span_attributes": {
          "llm.vendor": "openai",
          "llm.request.model": "gpt-4",
          "llm.response.model": "gpt-4-0125-preview",
          "llm.usage.input_tokens": "150",
          "llm.usage.output_tokens": "85",
          "llm.usage.total_tokens": "235",
          "traceloop.workflow.name": "customer_support"
        },
        "duration": 1850,
        "status_code": "STATUS_CODE_UNSET",
        "status_message": "",
        "prompts": {
          "llm.prompts.0.role": "system",
          "llm.prompts.0.content": "You are a helpful assistant.",
          "llm.prompts.1.role": "user",
          "llm.prompts.1.content": "What is the weather like today?"
        },
        "completions": {
          "llm.completions.0.role": "assistant",
          "llm.completions.0.content": "I don't have access to real-time weather data...",
          "llm.completions.0.finish_reason": "stop"
        },
        "input": "",
        "output": ""
      }
    ],
    "page_size": 50,
    "total_results": 1250,
    "next_cursor": "1734451200000"
  }
}
```

## Pagination

To paginate through results:

1. Make an initial request without a cursor
2. Use the `next_cursor` value from the response in subsequent requests
3. Continue until `next_cursor` is empty or you've retrieved all needed data

```bash theme={null}
# Example Filter: [{"id":"llm.vendor","operator":"equals","value":"openai"}]
#
# First request with filter (URL-encoded)
curl "https://api.traceloop.com/v2/warehouse/spans?from_timestamp_sec=1702900800&limit=50&filters=%5B%7B%22id%22%3A%22llm.vendor%22%2C%22operator%22%3A%22equals%22%2C%22value%22%3A%22openai%22%7D%5D" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Next page (using next_cursor from previous response)
curl "https://api.traceloop.com/v2/warehouse/spans?from_timestamp_sec=1702900800&limit=50&cursor=1734451200000&filters=%5B%7B%22id%22%3A%22llm.vendor%22%2C%22operator%22%3A%22equals%22%2C%22value%22%3A%22openai%22%7D%5D" \
  -H "Authorization: Bearer YOUR_API_KEY"
```


# Quick Start
Source: https://www.traceloop.com/docs/datasets/quick-start



Datasets are simple data tables that you can use to manage your data for experiments and evaluation of your AI applications.
Datasets are available in the SDK, and they enable you to create versioned snapshots for reproducible testing.

<Frame>
  <img />

  <img />
</Frame>

<Steps>
  <Step title="Create a new dataset">
    Click **New Dataset** to create a dataset, give it a descriptive name that reflects its purpose or use case, add a description to help your team understand its context, and provide a slug that allows you to use the dataset in the SDK.
  </Step>

  <Step title="Add your data">
    Add rows and columns to structure your dataset.
    You can add different column types:

    * **Text**: For prompts, model responses, or any textual data
    * **Number**: For numerical values, scores, or metrics
    * **Boolean**: For true/false flags or binary classifications

    <Tip>
      Use meaningful column names that clearly describe what each field contains,
      making it easier to work with your dataset in code, ensure clarity when using evaluators, and collaborate with team members.
    </Tip>
  </Step>

  <Step title="Publish your dataset version">
    <Frame>
      <img />

      <img />
    </Frame>

    Once you're satisfied with your dataset structure and data:

    1. Click **Publish Version** to create a stable snapshot
    2. Published versions are immutable
    3. Publish versions are accessible in the SDK
  </Step>

  <Step title="View your version history">
    You can access all published versions of your dataset by opening the version history modal. This allows you to:

    * Compare different versions of your dataset
    * Track changes over time
    * Switch between versions
  </Step>
</Steps>


# SDK usage
Source: https://www.traceloop.com/docs/datasets/sdk-usage

Access your managed datasets with the Traceloop SDK

## SDK Initialization

First, initialize the Traceloop SDK.

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk import Traceloop

  # Initialize with dataset sync enabled
  client = Traceloop.init()
  ```

  ```js Typescript theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";

  // Initialize with comprehensive configuration
  traceloop.initialize({
    appName: "your-app-name",
    apiKey: process.env.TRACELOOP_API_KEY,
    disableBatch: true,
    traceloopSyncEnabled: true,
  });

  // Wait for initialization to complete
  await traceloop.waitForInitialization();

  // Get the client instance for dataset operations
  const client = traceloop.getClient();
  ```
</CodeGroup>

<Note>
  **Prerequisites:** You need an API key set as the environment variable `TRACELOOP_API_KEY`.
  [Generate one in Settings →](/settings/managing-api-keys)
</Note>

The SDK fetches your datasets from Traceloop servers. Changes made to a draft dataset version are immediately available in the UI.

## Dataset Operations

### Create a dataset

You can create datasets in different ways depending on your data source:

* **Python**: Import from CSV file or pandas DataFrame
* **TypeScript**: Import from CSV data or create manually

<CodeGroup>
  ```python Python theme={null}
  import pandas as pd
  from traceloop.sdk import Traceloop

  client = Traceloop.init()

  # Create dataset from CSV file
  dataset_csv = client.datasets.from_csv(
      file_path="path/to/your/data.csv",
      slug="medical-questions",
      name="Medical Questions",
      description="Dataset with patients medical questions"
  )

  # Create dataset from pandas DataFrame
  data = {
      "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
      "price": [999.99, 29.99, 79.99, 299.99],
      "in_stock": [True, True, False, True],
      "category": ["Electronics", "Accessories", "Accessories", "Electronics"],
  }
  df = pd.DataFrame(data)

  # Create dataset from DataFrame
  dataset_df = client.datasets.from_dataframe(
      df=df,
      slug="product-inventory",
      name="Product Inventory",
      description="Sample product inventory data",
  )
  ```

  ```js Typescript theme={null}
  const client = traceloop.getClient();

  // Option 1: Create dataset manually
  const myDataset = await client.datasets.create({
    name: "Medical Questions",
    slug: "medical-questions",
    description: "Dataset with patients medical questions"
  });

  // Option 2: Create and import from CSV data
  const csvData = `user_id,prompt,response,model,satisfaction_score
  user_001,"What is React?","React is a JavaScript library...","gpt-3.5-turbo",4
  user_002,"Explain Docker","Docker is a containerization platform...","gpt-3.5-turbo",5`;

  await myDataset.fromCSV(csvData, { hasHeader: true });
  ```
</CodeGroup>

### Get a dataset

The dataset can be retrieved using its slug, which is available on the dataset page in the UI

<CodeGroup>
  ```python Python theme={null}
  # Get dataset by slug - current draft version
  my_dataset = client.datasets.get_by_slug("medical-questions")

  # Get specific version as CSV
  dataset_csv = client.datasets.get_version_csv(
      slug="medical-questions", 
      version="v2"
  )
  ```

  ```js Typescript theme={null}
  // Get dataset by slug - current draft version
  const myDataset = await client.datasets.get("medical-questions");

  // Get specific version as CSV
  const datasetCsv = await client.datasets.getVersionCSV("medical-questions", "v1");

  ```
</CodeGroup>

### Adding a Column

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk.dataset import ColumnType

  # Add a new column to your dataset
  new_column = my_dataset.add_column(
      slug="confidence_score",
      name="Confidence Score", 
      col_type=ColumnType.NUMBER
  )
  ```

  ```js Typescript theme={null}
  // Define schema by adding multiple columns
  const columnsToAdd = [
    {
      name: "User ID",
      slug: "user-id",
      type: "string" as const,
      description: "Unique identifier for the user"
    },
    {
      name: "Satisfaction score",
      slug: "satisfaction-score",
      type: "number" as const,
      description: "User satisfaction rating (1-5)"
    }
  ];

  await myDataset.addColumn(columnsToAdd);
  console.log("Schema defined with multiple columns");
  ```
</CodeGroup>

### Adding Rows

Map the column slug to its relevant value

<CodeGroup>
  ```python Python theme={null}
  # Add new rows to your dataset
  row_data = {
      "product": "TV Screen",
      "price": 1500.0,
      "in_stock": True,
      "category": "Electronics"
  }

  my_dataset.add_rows([row_data])
  ```

  ```js Typescript theme={null}
  // Add individual rows to dataset
  const userId = "user_001";
  const prompt = "Explain machine learning in simple terms";
  const startTime = Date.now();

  const rowData = {
    user_id: userId,
    prompt: prompt,
    response: `This is the model response`,
    model: "gpt-3.5-turbo",
    satisfaction_score: 1,
  };

  await myDataset.addRow(rowData);
  ```
</CodeGroup>

## Dataset Versions

### Publish a dataset

Dataset versions and history can be viewed in the UI. Versioning allows you to run the same evaluations and experiments across different datasets, making valuable comparisons possible.

<CodeGroup>
  ```python Python theme={null}
  # Publish the current dataset state as a new version
  published_version = my_dataset.publish()
  ```

  ```js Typescript theme={null}
  // Publish dataset with version and description
  const publishedVersion = await myDataset.publish();
  ```
</CodeGroup>


# Custom Evaluators
Source: https://www.traceloop.com/docs/evaluators/custom-evaluator

Define an evaluator for your specific needs 

Create your own evaluator to match your specific needs. You can start right away with custom criteria for full flexibility, or use one of our recommended formats as a starting point.

<Frame>
  <img />

  <img />
</Frame>

## Do It Yourself

This option lets you write the evaluator prompt from scratch by adding the desired messages (System, Assistant, User, or Developer) and configuring the model along with its settings.

<Frame>
  <img />

  <img />
</Frame>

## Generate Evaluator

The evaluator prompt can be automatically configured by Traceloop by clicking on the **Generate Evaluator** button.
To enable the button, map the column you want to evaluate (such as an LLM response) and add any additional data columns required for prompt creation.
Describe the evaluator’s purpose and reference the relevant data columns in the description.

The system generates a prompt template that you can edit and customize as needed.

## Test Evaluator

Before creating an evaluator, you can test it on existing Playground data.
This allows you to refine and correct the evaluator prompt before saving the final version.

## Execute Evaluator

Evaluators can be executed in [playground columns](../playgrounds/columns/column-management) and in [experiments through the SDK](../experiments/running-from-code).


# Guardrails
Source: https://www.traceloop.com/docs/evaluators/guardrails

Real-time evaluation and safety checks for LLM applications

Guardrails are real-time evaluators that run inline with your application code, providing immediate safety checks, policy enforcement, and quality validation before outputs reach users. Unlike post-hoc evaluation in playgrounds, experiments, or monitors, guardrails execute synchronously during runtime to prevent issues before they occur.

## What Are Guardrails?

Guardrails act as protective middleware layers that intercept and validate LLM inputs and outputs in real-time. They enable you to:

* **Prevent harmful outputs** - Block inappropriate, biased, or unsafe content before it reaches users
* **Enforce business policies** - Ensure responses comply with company guidelines and regulatory requirements
* **Validate quality** - Check for hallucinations, factual accuracy, and relevance in real-time
* **Control behavior** - Enforce tone, style, and format requirements consistently
* **Protect sensitive data** - Detect and prevent leakage of PII, credentials, or confidential information

## How Guardrails Differ from Other Evaluators

| Feature              | Guardrails                  | Experiments          | Monitors                     | Playgrounds           |
| -------------------- | --------------------------- | -------------------- | ---------------------------- | --------------------- |
| **Timing**           | Real-time (inline)          | Post-hoc (batch)     | Post-hoc (continuous)        | Interactive (manual)  |
| **Execution**        | Synchronous with code       | Programmatic via SDK | Automated on production data | User-triggered        |
| **Purpose**          | Prevention & blocking       | Systematic testing   | Quality tracking             | Development & testing |
| **Latency Impact**   | Yes - adds to response time | No                   | No                           | N/A                   |
| **Can Block Output** | Yes                         | No                   | No                           | No                    |

The key distinction is that guardrails run **before** outputs are returned to users, allowing you to intercept and modify or block responses based on evaluation results.

## Use Cases

### Safety and Content Filtering

Prevent toxic, harmful, or inappropriate content from reaching users:

* Detect hate speech, profanity, or offensive language
* Block outputs containing violent or explicit content
* Filter responses that could cause psychological harm

### Regulatory Compliance

Ensure outputs meet legal and regulatory requirements:

* HIPAA compliance for medical information
* GDPR compliance for personal data handling
* Financial services regulations (e.g., avoiding financial advice)
* Industry-specific content guidelines

### Data Protection

Prevent sensitive information leakage:

* Detect PII (personally identifiable information)
* Block API keys, passwords, or credentials in responses
* Prevent disclosure of proprietary business information
* Ensure customer data confidentiality

### Quality Assurance

Maintain output quality standards:

* Detect hallucinations and factual errors
* Verify response relevance to user queries
* Enforce minimum quality thresholds
* Validate structured output formats

### Brand and Tone Control

Ensure consistent brand voice:

* Enforce communication style guidelines
* Maintain appropriate tone for audience
* Prevent off-brand language or messaging
* Control formality levels

## Implementation

### Basic Setup

First, initialize the Traceloop SDK in your application:

```python theme={null}
from traceloop.sdk import Traceloop

Traceloop.init(app_name="your-app-name")
```

### Using the @guardrail Decorator

Apply the `@guardrail` decorator to functions that interact with LLMs:

```python theme={null}
from traceloop.sdk.decorators import guardrail
from openai import AsyncOpenAI

client = AsyncOpenAI()

@guardrail(slug="content_safety_check")
async def get_ai_response(user_message: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
```

The `slug` parameter identifies which guardrail evaluator to apply. This corresponds to an evaluator you've defined in the Traceloop dashboard.

### Medical Chat Example

Here's a complete example showing guardrails for a medical chatbot:

```python theme={null}
import asyncio
import os
from openai import AsyncOpenAI
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import guardrail

Traceloop.init(app_name="medical-chat-example")

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@guardrail(slug="valid_medical_chat")
async def get_doctor_response(conversation_history: list) -> str:
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are a medical information assistant.
                You can provide general health information but you are NOT
                a replacement for professional medical advice.
                Always recommend consulting with qualified healthcare providers
                for specific medical concerns."""
            },
            *conversation_history
        ],
        temperature=0,
        max_tokens=500
    )
    return response.choices[0].message.content

async def medical_chat_session():
    conversation_history = []

    print("Medical Chat Assistant (type 'quit' to exit)")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using Medical Chat Assistant. Stay healthy!")
            break

        conversation_history.append({"role": "user", "content": user_input})

        try:
            response = await get_doctor_response(conversation_history)
            print(f"\nAssistant: {response}")
            conversation_history.append({"role": "assistant", "content": response})
        except Exception as e:
            print(f"Error: {e}")
            conversation_history.pop()

if __name__ == "__main__":
    asyncio.run(medical_chat_session())
```

### Multiple Guardrails

You can apply multiple guardrails to the same function for layered protection:

```python theme={null}
@guardrail(slug="content_safety")
@guardrail(slug="pii_detection")
@guardrail(slug="factual_accuracy")
async def generate_response(prompt: str) -> str:
    # Your LLM call here
    pass
```

Guardrails execute in the order they're declared (bottom to top in the decorator stack).

## Creating Guardrail Evaluators

Guardrails use the same evaluator system as experiments and monitors. To create a guardrail evaluator:

1. Navigate to the **Evaluator Library** in your Traceloop dashboard

2. Click **New Evaluator** or select a pre-built evaluator

3. Define your evaluation criteria:
   * For safety checks: Specify content categories to detect and block
   * For compliance: Define regulatory requirements and policies
   * For quality: Set thresholds for relevance, accuracy, or completeness

4. Test the evaluator in a playground to validate behavior

5. Note the evaluator's **slug** for use in your code

6. Apply the evaluator using `@guardrail(slug="your-evaluator-slug")`

See [Custom Evaluators](./custom-evaluator) for detailed instructions on creating evaluators.

## Best Practices

### Performance Considerations

Guardrails add latency to your application since they run synchronously:

* **Use selectively** - Apply guardrails only where needed, not to every function
* **Choose efficient evaluators** - Simpler checks run faster than complex LLM-based evaluations
* **Consider async execution** - Use async/await patterns to maximize throughput
* **Monitor latency** - Track guardrail execution times and optimize slow evaluators
* **Cache when possible** - Cache evaluation results for identical inputs

### Error Handling

Implement robust error handling for guardrail failures:

```python theme={null}
from traceloop.sdk.decorators import guardrail

@guardrail(slug="safety_check")
async def get_response(prompt: str) -> str:
    try:
        # Your LLM call
        response = await generate_llm_response(prompt)
        return response
    except Exception as e:
        # Log the error
        logger.error(f"Guardrail or LLM error: {e}")
        # Return safe fallback
        return "I apologize, but I cannot process this request at the moment."
```

### Layered Protection

Use multiple layers of guardrails for critical applications:

1. **Input validation** - Check user inputs before processing
2. **Output validation** - Verify LLM responses before returning
3. **Context validation** - Ensure proper use of retrieved information
4. **Post-processing** - Final safety check on formatted outputs

### Testing Guardrails

Before deploying to production:

* **Test in playgrounds** - Validate evaluator behavior with sample inputs
* **Run experiments** - Test guardrails against diverse datasets
* **Monitor false positives** - Track blocked outputs that should have been allowed
* **Monitor false negatives** - Watch for policy violations that weren't caught
* **A/B test** - Compare user experience with and without specific guardrails

### Compliance and Auditing

For regulated industries:

* **Log all evaluations** - Traceloop automatically tracks all guardrail executions
* **Document policies** - Maintain clear documentation of what each guardrail checks
* **Version control** - Track changes to guardrail configurations over time
* **Regular audits** - Review guardrail effectiveness and update as needed
* **Incident response** - Have procedures for when guardrails detect violations

## Configuration Options

When applying guardrails, you can configure behavior:

```python theme={null}
@guardrail(
    slug="safety_check",
    # Additional configuration options
    blocking=True,        # Whether to block on evaluation failure
    timeout_ms=5000,      # Maximum evaluation time
    fallback="safe"       # Behavior on timeout or error
)
async def get_response(prompt: str) -> str:
    # Your implementation
    pass
```

## Monitoring Guardrail Performance

Track guardrail effectiveness in your Traceloop dashboard:

* **Execution frequency** - How often each guardrail runs
* **Block rate** - Percentage of requests blocked by guardrails
* **Latency impact** - Time added by guardrail evaluation
* **Error rate** - Guardrail failures or timeouts
* **Policy violations** - Trends in detected issues over time

Use this data to optimize guardrail configuration and identify emerging safety concerns.

## Integration with Experiments and Monitors

Guardrails complement other evaluation workflows:

* **Experiments** - Test guardrail effectiveness on historical data before deployment
* **Monitors** - Continuously track guardrail performance in production
* **Playgrounds** - Develop and refine guardrail evaluators interactively

This integrated approach ensures comprehensive quality control across development, testing, and production environments.

## Next Steps

* [Create custom evaluators](./custom-evaluator) for your specific guardrail needs
* [Explore pre-built evaluators](./made-by-traceloop) for common safety and quality checks
* [Set up experiments](../experiments/introduction) to test guardrails before production
* [Configure monitors](../monitoring/introduction) to track guardrail performance over time


# Introduction
Source: https://www.traceloop.com/docs/evaluators/intro

Evaluating workflows and LLM outputs

The evaluation library is a core feature of Traceloop, providing comprehensive tools to assess LLM outputs, data quality, and performance across various dimensions. Whether you need automated scoring or human judgment, the evaluation system has you covered.

## Why Do We Need Evaluators?

LLM agents are more complex than single-turn completions.
They operate across multiple steps, use tools, and depend on context and external systems like memory or APIs. This complexity introduces new failure modes: agents may hallucinate tools, get stuck in loops, or produce final answers that hide earlier mistakes.

Evaluators make these issues visible by checking correctness, relevance, task completion, tool usage, memory retention, safety, and style. They ensure outputs remain consistent even when dependencies shift and provide a structured way to measure reliability. Evaluation is continuous, extending into production through automated tests, drift detection, quality gates, and online monitoring.
In short, evaluators turn outputs into trustworthy systems by providing measurable and repeatable checks that give teams confidence to deploy at scale.

## Evaluators types

The system supports:

* **Custom evaluators** - Create your own evaluation logic tailored to specific needs
* **Built-in evaluators** - pre-configured evaluators by Traceloop for common assessment tasks

In the Evaluator Library, select the evaluator you want to define.
You can either create a custom evaluator by clicking **New Evaluator** or choose one of the prebuilt **Made by Traceloop** evaluators.

<Frame>
  <img />

  <img />
</Frame>

Clicking on existing evaluators will present their input and output schema. This is valuable information in order to execute the evaluator [through the SDK](../experiments/running-from-code).

## Where to Use Evaluators

Evaluators can be used in multiple contexts within Traceloop:

* **[Guardrails](./guardrails)** - Apply evaluators in real-time as inline safety checks and quality gates that run synchronously with your application code to prevent issues before they reach users
* **[Playgrounds](../playgrounds/quick-start)** - Test and iterate on your evaluators interactively, compare different configurations, and validate evaluation logic before deployment
* **[Experiments](../experiments/introduction)** - Run systematic evaluations across datasets programmatically using the SDK, track performance metrics over time, and easily compare experiment results
* **[Monitors](../monitoring/introduction)** - Continuously evaluate your LLM applications in production with real-time monitoring and alerting on quality degradation


# Made by Traceloop
Source: https://www.traceloop.com/docs/evaluators/made-by-traceloop

Pre-configured evaluators by Traceloop for common assessment tasks

The Evaluator Library provides a comprehensive collection of pre-built quality checks designed to systematically assess AI outputs.

Each evaluator comes with a predefined input and output schema. When using an evaluator, you’ll need to map your data to its input schema.

<Frame>
  <img />

  <img />
</Frame>

## Evaluator Types

### Style

<CardGroup>
  <Card title="Character Count" icon="text">
    Analyze response length and verbosity to ensure outputs meet specific length requirements.
  </Card>

  <Card title="Character Count Ratio" icon="hashtag">
    Measure the ratio of characters to the input to assess response proportionality and expansion.
  </Card>

  <Card title="Word Count" icon="align-left">
    Ensure appropriate response detail level by tracking the total number of words in outputs.
  </Card>

  <Card title="Word Count Ratio" icon="hashtag">
    Measure the ratio of words to the input to compare input/output verbosity and expansion patterns.
  </Card>
</CardGroup>

### Quality & Correctness

<CardGroup>
  <Card title="Answer Relevancy" icon="bullseye">
    Verify responses address the query to ensure AI outputs stay on topic and remain relevant.
  </Card>

  <Card title="Faithfulness" icon="circle-check">
    Detect hallucinations and verify facts to maintain accuracy and truthfulness in AI responses.
  </Card>

  <Card title="Answer Correctness" icon="circle-check">
    Evaluate factual accuracy by comparing answers against ground truth.
  </Card>

  <Card title="Answer Completeness" icon="circle-check">
    Measure how completely responses use relevant context to ensure all relevant information is addressed.
  </Card>

  <Card title="Topic Adherence" icon="hashtag">
    Validate topic adherence to ensure responses stay focused on the specified subject matter.
  </Card>

  <Card title="Semantic Similarity" icon="hashtag">
    Validate semantic similarity between expected and actual responses to measure content alignment.
  </Card>

  <Card title="Instruction Adherence" icon="clipboard-check">
    Measure how well the LLM response follows given instructions to ensure compliance with specified requirements.
  </Card>

  <Card title="Measure Perplexity" icon="hashtag">
    Measure text perplexity from logprobs to assess the predictability and coherence of generated text.
  </Card>

  <Card title="Uncertainty Detector" icon="gauge">
    Generate responses and measure model uncertainty from logprobs to identify when the model is less confident in its outputs.
  </Card>

  <Card title="Conversation Quality" icon="comments">
    Evaluate conversation quality based on tone, clarity, flow, responsiveness, and transparency.
  </Card>

  <Card title="Context Relevance" icon="hashtag">
    Validate context relevance to ensure retrieved context is pertinent to the query.
  </Card>
</CardGroup>

### Security & Compliance

<CardGroup>
  <Card title="PII Detection" icon="shield">
    Identify personal information exposure to protect user privacy and ensure data security compliance.
  </Card>

  <Card title="Profanity Detection" icon="triangle-exclamation">
    Flag inappropriate language use to maintain content quality standards and professional communication.
  </Card>

  <Card title="Sexism Detection" icon="triangle-exclamation">
    Detect sexist and discriminatory content.
  </Card>

  <Card title="Prompt Injection" icon="shield-exclamation">
    Detect prompt injection attacks in user inputs.
  </Card>

  <Card title="Toxicity Detector" icon="skull">
    Detect toxic content including personal attacks, mockery, hate, and threats.
  </Card>

  <Card title="Secrets Detection" icon="lock">
    Monitor for credential and key leaks to prevent accidental exposure of sensitive information.
  </Card>
</CardGroup>

### Formatting

<CardGroup>
  <Card title="SQL Validation" icon="database">
    Validate SQL queries to ensure proper syntax and structure in database-related AI outputs.
  </Card>

  <Card title="JSON Validation" icon="code">
    Validate JSON responses to ensure proper formatting and structure in API-related outputs.
  </Card>

  <Card title="Regex Validation" icon="asterisk">
    Validate regex patterns to ensure correct regular expression syntax and functionality.
  </Card>

  <Card title="Placeholder Regex" icon="asterisk">
    Validate placeholder regex patterns to ensure proper template and variable replacement structures.
  </Card>
</CardGroup>

### Agents

<CardGroup>
  <Card title="Agent Goal Accuracy" icon="bullseye">
    Validate agent goal accuracy to ensure AI systems achieve their intended objectives effectively.
  </Card>

  <Card title="Agent Tool Error Detector" icon="wrench">
    Detect errors or failures during tool execution to monitor agent tool performance.
  </Card>

  <Card title="Agent Flow Quality" icon="route">
    Validate agent trajectories against user-defined natural language tests to assess agent decision-making paths.
  </Card>

  <Card title="Agent Efficiency" icon="zap">
    Evaluate agent efficiency by checking for redundant calls and optimal paths to optimize agent performance.
  </Card>

  <Card title="Agent Goal Completeness" icon="circle-check">
    Measure whether the agent successfully accomplished all user goals to verify comprehensive goal achievement.
  </Card>

  <Card title="Intent Change" icon="repeat">
    Detect whether the user's primary intent or workflow changed significantly during a conversation.
  </Card>
</CardGroup>


# Introduction
Source: https://www.traceloop.com/docs/experiments/introduction



Building reliable LLM applications means knowing whether a new prompt, model, or change of flow actually makes things better.

<Frame>
  <img />

  <img />
</Frame>

Experiments in Traceloop provide teams with a structured workflow for testing and comparing results across different prompt, model, and evaluator checks, all against real datasets.

## What You Can Do with Experiments

<CardGroup>
  <Card title="Run Multiple Evaluators" icon="list-check">
    Execute multiple evaluation checks against your dataset
  </Card>

  <Card title="View Complete Results" icon="table">
    See all experiment run outputs in a comprehensive table view with relevant indicators and detailed reasoning
  </Card>

  <Card title="Compare Experiment Runs Results" icon="code-compare">
    Run the same experiment across different dataset versions to see how it affects your workflow
  </Card>

  <Card title="Custom Task Pipelines" icon="code">
    Add a tailored task to the experiment to create evaluator input. For example: LLM calls, semantic search, etc.
  </Card>
</CardGroup>


# Result Overview
Source: https://www.traceloop.com/docs/experiments/result-overview



All experiments are logged in the Traceloop platform. Each experiment is executed through the SDK.

<Frame>
  <img />

  <img />
</Frame>

## Experiment Runs

An experiment can be run multiple times against different datasets and tasks. All runs are logged in the Traceloop platform to enable easy comparison.

<Frame>
  <img />

  <img />
</Frame>

## Experiment Tasks

An experiment run is made up of multiple tasks, where each task represents the experiment flow applied to a single dataset row.

The task logging captures:

* Task input – the data taken from the dataset row.

* Task outputs – the results produced by running the task, which are then passed as input to the evaluator.

* Evaluator results – the evaluator’s assessment based on the task outputs.

<Frame>
  <img />

  <img />
</Frame>


# Run via SDK
Source: https://www.traceloop.com/docs/experiments/running-from-code

Learn how to run experiments programmatically using the Traceloop SDK

You can run experiments programmatically using the Traceloop SDK. This allows you to systematically evaluate different AI model configurations, prompts, and approaches with your datasets.

## SDK Initialization

First, initialize the Traceloop SDK.

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk import Traceloop

  # Initialize with dataset sync enabled
  client = Traceloop.init()
  ```

  ```js Typescript theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";

  // Initialize with comprehensive configuration
  traceloop.initialize({
    appName: "your-app-name",
    apiKey: process.env.TRACELOOP_API_KEY,
    disableBatch: true,
    traceloopSyncEnabled: true,
  });

  // Wait for initialization to complete
  await traceloop.waitForInitialization();

  // Get the client instance for dataset operations
  const client = traceloop.getClient();
  ```
</CodeGroup>

<Note>
  **Prerequisites:** You need an API key set as the environment variable `TRACELOOP_API_KEY`.
  [Generate one in Settings →](/settings/managing-api-keys)
</Note>

## Basic Experiment Structure

An experiment consists of:

* A **dataset** to test against
* A **task function** that defines what your AI system should do
* **Evaluators** to measure performance

## Task Functions

Create a task function that define how your AI system processes each dataset row. The task is one of the experiments parameters, it will run it on each dataset row.

The task function signature expects:

* **Input**: An optional dictionary containing the dataset row data
* **Output**: A dictionary with your task results

<CodeGroup>
  ```python Python theme={null}
  task: Callable[[Optional[Dict[str, Any]]], Dict[str, Any]]
  ```

  ```typescript TypeScript theme={null}
  type dataValue = string | number | boolean;
  type TaskInput = Record<string, dataValue>;
  type TaskOutput = Record<string, dataValue>;
  interface ExperimentTaskFunction<TInput = TaskInput, TOutput = TaskOutput> {
      (input: TInput): Promise<TOutput> | TOutput;
  }
  ```
</CodeGroup>

A task can perform any desired internal operation—such as LLM calls, semantic search, RAG, or custom business logic. The task output is then used as the evaluator input and is automatically logged in the Traceloop platform.

<Note> Ensure that the evaluator input schema variables are included in the task output dictionary. </Note> <Tip> You can add extra attributes to the task output even if they are not evaluator input parameters—these will also be logged to the platform. </Tip>

<CodeGroup>
  ```python Python theme={null}
  from openai import AsyncOpenAI
  import os

  def provide_medical_info_prompt(question: str) -> str:
      """
      Provides comprehensive medical information without restrictions
      """
      return f"""You are a knowledgeable health educator.
      Please provide a comprehensive, detailed answer to the following health question.

      Question: {question}

      Please provide:
      1. A clear, factual explanation using accessible language
      2. Key benefits and important considerations
      3. Specific recommendations and actionable guidance
      4. Relevant details about treatments, symptoms, or health practices
      5. Any relevant medical or scientific context

      Be thorough and informative in your response."""

  async def medical_task(row):
      openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

      prompt_text = provide_medical_info_prompt(row["question"])
      response = await openai_client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": prompt_text}],
          temperature=0.7,
          max_tokens=500,
      )

      ai_response = response.choices[0].message.content

      return {"completion": ai_response, "text": ai_response}
  ```

  ```typescript TypeScript theme={null}
  import { OpenAI } from "openai";
  import type {
    ExperimentTaskFunction,
    TaskInput,
    TaskOutput,
  } from "@traceloop/node-server-sdk";

  function provideMedicalInfoPrompt(question: string): string {
    return `You are a health educator providing comprehensive medical information.

      Question: ${question}

      Please provide a detailed, educational response that includes:

      1. **Clear, factual explanation** of the medical concept or condition
      2. **Key benefits and considerations** related to the topic
      3. **Specific recommendations** based on current medical knowledge
      4. **Important disclaimers** about consulting healthcare professionals
      5. **Relevant context** that helps understand the topic better

      Guidelines:
      - Use evidence-based information
      - Explain medical terms in plain language
      - Include both benefits and risks when applicable
      - Emphasize the importance of professional medical consultation
      - Provide actionable, general health guidance

      Your response should be educational, balanced, and encourage informed healthcare decisions.`;
  }


  /**
   * Task function for medical advice prompt
   */
  const medicalTask: ExperimentTaskFunction = async (
    row: TaskInput,
  ): Promise<TaskOutput> => {
      const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });

    const promptText = provideMedicalInfoPrompt(row.question as string);
    const answer = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: promptText }],
      temperature: 0.7,
      max_tokens: 500,
    });

    const aiResponse = answer.choices?.[0]?.message?.content
    return { completion: aiResponse, text: aiResponse };
  };
  ```
</CodeGroup>

## Running Experiments

Use the `experiment.run()` method to execute your experiment by selecting a dataset as the source data, choosing the evaluators to run, and assigning a slug to make it easy to rerun later.

#### `experiment.run()` Parameters

* `dataset_slug` (str): Identifier for your dataset
* `dataset_version` (str): Version of the dataset to use, experiment can only run on a published version
* `task` (function): Async function that processes each dataset row
* `evaluators` (list): List of evaluator slugs to measure performance
* `experiment_slug` (str): Unique identifier for this experiment
* `stop_on_error` (boolean):  Whether to stop on first error (default: False)
* `wait_for_results` (boolean): Whether to wait for async tasks to complete, when not waiting the results will be found in the ui (default: True)

<CodeGroup>
  ```python Python theme={null}
  results, errors = await client.experiment.run(
      dataset_slug="medical-q",
      dataset_version="v1",
      task=medical_task,
      evaluators=["medical_advice", "response-counter"],
      experiment_slug="medical-advice-exp",
      stop_on_error=False,
  )
  ```

  ```typescript TypeScript theme={null}
  const results = await client.experiment.run(medicalTask, {
      datasetSlug: "medical-q",
      datasetVersion: "v1",
      evaluators: ["medical_advice", "response-counter"],
      experimentSlug: "medical-advice-exp-ts",
      stopOnError: false,
  });
  ```
</CodeGroup>

## Comparing Different Approaches

You can run multiple experiments to compare different approaches—whether by using different datasets, trying alternative task functionality, or testing variations in prompts, models, or business logic.

<CodeGroup>
  ```python Python theme={null}
  # Task function that provides comprehensive medical information
  async def medical_task_provide_info(row):
      openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
      
      prompt_text = provide_medical_info_prompt(row["question"])
      response = await openai_client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": prompt_text}],
          temperature=0.7,
          max_tokens=500,
      )
      
      ai_response = response.choices[0].message.content
      return {"completion": ai_response, "text": ai_response}

  # Task function that refuses to provide medical advice
  async def medical_task_refuse_advice(row):
      openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
      
      prompt_text = f"You must refuse to provide medical advice. Question: {row['question']}"
      response = await openai_client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": prompt_text}],
          temperature=0.7,
          max_tokens=500,
      )
      
      ai_response = response.choices[0].message.content
      return {"completion": ai_response, "text": ai_response}

  # Run both approches in the same experiment
  async def compare_medical_approaches():
      # Provide info approach
      provide_results, provide_errors = await client.experiment.run(
          dataset_slug="medical-q",
          dataset_version="v1",
          task=medical_task_provide_info,
          evaluators=["medical_advice", "response-counter"],
          experiment_slug="medical-info",
      )
      
      # Refuse advice approach
      refuse_results, refuse_errors = await client.experiment.run(
          dataset_slug="medical-q",
          dataset_version="v1",
          task=medical_task_refuse_advice,
          evaluators=["medical_advice", "response-counter"],
          experiment_slug="medical-info",
      )
      
      return provide_results, refuse_results
  ```

  ```typescript TypeScript theme={null}
  // Task function that provides comprehensive medical information
  const medicalTaskProvideInfo: ExperimentTaskFunction = async (
    row: TaskInput,
  ): Promise<TaskOutput> => {
    const promptText = provideMedicalInfoPrompt(row.question as string);
    const answer = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: promptText }],
      temperature: 0.7,
      max_tokens: 500,
    });

    const aiResponse = answer.choices?.[0]?.message?.content || "";
    return { completion: aiResponse, text: aiResponse };
  };

  // Task function that refuses to provide medical advice
  const medicalTaskRefuseAdvice: ExperimentTaskFunction = async (
    row: TaskInput,
  ): Promise<TaskOutput> => {
    const promptText = `You must refuse to provide medical advice. Question: ${row.question}`;
    const answer = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: promptText }],
      temperature: 0.7,
      max_tokens: 500,
    });

    const aiResponse = answer.choices?.[0]?.message?.content || "";
    return { completion: aiResponse, text: aiResponse };
  };

  // Run both approches in the same experiment
  async function compareMedicalApproaches() {
    // Provide info approach
    const provideResults = await client.experiment.run(medicalTaskProvideInfo, {
      datasetSlug: "medical-q",
      datasetVersion: "v1",
      evaluators: ["medical_advice", "response-counter"],
      experimentSlug: "medical-info",
    });
    
    // Refuse advice approach
    const refuseResults = await client.experiment.run(medicalTaskRefuseAdvice, {
      datasetSlug: "medical-q",
      datasetVersion: "v1",
      evaluators: ["medical_advice", "response-counter"],
      experimentSlug: "medical-info",
    });
    
    return [provideResults, refuseResults];
  }
  ```
</CodeGroup>

## Full Examples

For complete, working examples that you can run and modify:

<CardGroup>
  <Card title="Python Example" icon="python" href="https://github.com/traceloop/openllmetry/blob/main/packages/sample-app/sample_app/experiment/experiment_example.py" />

  <Card title="TypeScript Example" icon="js" href="https://github.com/traceloop/openllmetry-js/blob/main/packages/sample-app/src/sample_experiment.ts" />
</CardGroup>


# Hub Configuration
Source: https://www.traceloop.com/docs/hub/configuration

How to configure Traceloop Hub and connect it to different LLM providers

The hub configuration is done through the `config.yaml` file that should be placed in the root directory of the hub.

Here's an example of the configuration file:

```yaml theme={null}
providers:
  - key: azure-openai
    type: azure
    api_key: "<your-azure-api-key>"
    resource_name: "<your-resource-name>"
    api_version: "<your-api-version>"
  - key: openai
    type: openai
    api_key: "<your-openai-api-key>"
    # or use an environment variable
    api_key: ${OPENAI_API_KEY}

models:
  - key: gpt-4o-openai
    type: gpt-4o
    provider: openai
  - key: gpt-4o-azure
    type: gpt-4o
    provider: azure-openai
    deployment: "<your-deployment>"

pipelines:
  - name: default
    type: chat
    plugins:
      - logging:
          level: info
      - tracing:
          endpoint: "https://api.traceloop.com/v1/traces"
          api_key: "<your-traceloop-api-key>"
      - model-router:
          models:
            - gpt-4o-openai
            - gpt-4o-azure
```

## Providers

This is where you list the LLM providers that you want to use with the hub.
You can have multiple providers of the same type, just give them different keys.

## Models

This is where you list the models that you want to use with the hub. Each model should be associated with a provider.
You can have multiple models of the same type with different providers - for example, you can use GPT-4o on Azure and on OpenAI.
Then, you can define a pipeline (see below) that switches between them according to availabilty.
Each model has a `type` which is how the hub understands that 2 model specifications are actually the same "model",

## Pipelines

A pipeline is something you can execute when calling the hub. It contains a list of plugins that are executed in order.
Here are the plugins that are available:

* `logging`: Logs the request and response.
* `tracing`: Enables OpenTelemetry tracing for requests going through the pipeline.
* `model-router`: Routes the request to a model, according to the list specified in the `models` section.


# Getting Started with Traceloop Hub
Source: https://www.traceloop.com/docs/hub/getting-started

Set up Hub as a smart proxy to all your LLM calls.

Hub is a next generation smart proxy for LLM applications. It centralizes control and tracing of all LLM calls and traces.
It's built in Rust so it's fast and efficient. It's completely open-source and free to use.

## Installation

### Local

1. Clone the repo:

```bash theme={null}
git clone https://github.com/traceloop/hub
```

2. Copy the `config-example.yaml` file to `config.yaml` and set the correct values (see below for more information).

3. Run the hub by running `cargo run` in the root directory.

### With Docker

Traceloop Hub is available as a docker image named `traceloop/hub`. Make sure to create a `config.yaml` file
following the [configuration](./configuration) instructions.

```bash theme={null}
docker run --rm -p 3000:3000 -v $(pwd)/config.yaml:/etc/hub/config.yaml:ro -e CONFIG_FILE_PATH='/etc/hub/config.yaml'  -t traceloop/hub
```

## Connecting to Hub

After running the hub and [configuring it](./configuration), you can start using it to invoke available LLM providers.
Its API is the standard OpenAI API, so you can use it as a drop-in replacement for your LLM calls.

You can invoke different pipelines by passing the `x-traceloop-pipeline` header. If none is specified, the default pipeline will be used.

```python theme={null}
import openai

client = OpenAI(
    base_url="http://localhost:3000/api/v1",
    # default_headers={"x-traceloop-pipeline": "optional-pipeline-name"},
)
```


# GitHub
Source: https://www.traceloop.com/docs/integrations/github

Run experiments in CI and get evaluation results directly in your pull requests

# Track Experiment Results in CI

Instead of deploying blindly and hoping for the best, you can validate changes with real data before they reach production.

Create experiments that automatically run your agent flow in CI, test your changes against production-quality datasets, and get comprehensive evaluation results directly in your pull request. This ensures every change is validated with the same rigor as your application code.

## How It Works

Run an experiment in your CI/CD pipeline with the Traceloop GitHub App integration. Receive experiment evaluation results as comments on your pull requests, helping you validate AI model changes, prompt updates, and configuration modifications before merging to production.

<Steps>
  <Step title="Install the Traceloop GitHub App">
    Go to the [integrations page](https://app.traceloop.com/settings/integrations) within Traceloop and click on the GitHub card.

    Click "Install GitHub App" to be redirected to GitHub where you can install the Traceloop app for your organization or personal account.

    <Info>
      You can also install Traceloop GitHub app [here](https://github.com/apps/traceloop/installations/new)
    </Info>
  </Step>

  <Step title="Configure Repository Access">
    Select the repositories where you want to enable Traceloop experiment runs. You can choose:

    * All repositories in your organization
    * Specific repositories only

    After installing the app you will be redirected to a Traceloop authorization page.

    <Info>
      **Permissions Required:** The app needs read access to your repository contents and write access to pull requests to post evaluation results as comments.
    </Info>
  </Step>

  <Step title="Authorize GitHub app installation at Traceloop">
    <Frame>
      <img />

      <img />
    </Frame>
  </Step>

  <Step title="Create Your Experiment Script">
    Create an [experiment](/experiments/introduction) script that runs your AI flow. An experiment consists of three key components:

    * **[Dataset](/datasets/quick-start)**: A collection of test inputs that represent real-world scenarios your AI will handle
    * **Task Function**: Your AI flow code that processes each dataset row (e.g., calling your LLM, running RAG, executing agent logic)
    * **[Evaluators](/evaluators/intro)**: Automated quality checks that measure your AI's performance (e.g., accuracy, safety, relevance)

    The experiment runs your task function on every row in the dataset, then applies evaluators to measure quality. This validates your changes with real data before production.

    The script below shows how to test a question-answering flow:

    <CodeGroup>
      ```python Python theme={null}
      import asyncio
      import os
      from openai import AsyncOpenAI
      from traceloop.sdk import Traceloop
      from traceloop.sdk.experiment.model import RunInGithubResponse

      # Initialize Traceloop client
      client = Traceloop.init(
        app_name="research-experiment-ci-cd"
      )

      async def generate_research_response(question: str) -> str:
      """Generate a research response using OpenAI"""
      openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

      response = await openai_client.chat.completions.create(
          model="gpt-4",
          messages=[
              {
                  "role": "system",
                  "content": "You are a helpful research assistant. Provide accurate, well-researched answers.",
              },
              {"role": "user", "content": question},
          ],
          temperature=0.7,
          max_tokens=500,
      )

      return response.choices[0].message.content


      async def research_task(row):
      """Task function that processes each dataset row"""
      query = row.get("query", "")
      answer = await generate_research_response(query)

      return {
          "completion": answer,
          "question": query,
          "sentence": answer
      }


      async def main():
      """Run experiment in GitHub context"""
      print("🚀 Running research experiment in GitHub CI/CD...")

      # Execute tasks locally and send results to backend
      response = await client.experiment.run(
          task=research_task,
          dataset_slug="research-queries",
          dataset_version="v2",
          evaluators=["research-word-counter", "research-relevancy"],
          experiment_slug="research-exp",
      )

      if isinstance(response, RunInGithubResponse):
          print(f"Experiment {response.experiment_slug} completed!")


      if __name__ == "__main__":
      asyncio.run(main())
      ```

      ```typescript TypeScript theme={null}
      import * as traceloop from "@traceloop/node-server-sdk";
      import { OpenAI } from "openai";
      import type { ExperimentTaskFunction } from "@traceloop/node-server-sdk";

      // Initialize Traceloop
      traceloop.initialize({
      appName: "research-experiment-ci-cd",
      disableBatch: true,
      traceloopSyncEnabled: true,
      });

      await traceloop.waitForInitialization();
      const client = traceloop.getClient();

      /**
      * Generate a research response using OpenAI
      */
      async function generateResearchResponse(question: string): Promise<string> {
      const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
      });

      const response = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [
        {
          role: "system",
          content: "You are a helpful research assistant. Provide accurate, well-researched answers.",
        },
        { role: "user", content: question },
      ],
      temperature: 0.7,
      max_tokens: 500,
      });

      return response.choices?.[0]?.message?.content || "";
      }

      /**
      * Task function that processes each dataset row
      */
      const researchTask: ExperimentTaskFunction = async (row) => {
      const query = (row.query as string) || "";
      const answer = await generateResearchResponse(query);

      return {
      completion: answer,
      question: query,
      sentence: answer,
      };
      };

      /**
      * Run experiment in GitHub context
      */
      async function main() {
      console.log("🚀 Running research experiment in GitHub CI/CD...");

      // Execute tasks locally and send results to backend
      const response = await client.experiment.run(researchTask, {
      datasetSlug: "research-queries",
      datasetVersion: "v2",
      evaluators: ["research-word-counter", "research-relevancy"],
      experimentSlug: "research-exp",
      });

      console.log(`Experiment research-exp completed!`);
      }

      main().catch((error) => {
      console.error("Experiment failed:", error);
      process.exit(1);
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Set up Your CI Workflow">
    Add a GitHub Actions workflow to automatically run Traceloop experiments on pull requests.
    Below is an example workflow file you can customize for your project:

    ```yaml ci-cd configuration  theme={null}
    name: Run Traceloop Experiments

    on:
      pull_request:
        branches: [main, master]

    jobs:
      run-experiments:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout code
            uses: actions/checkout@v4

          - name: Set up Python
            uses: actions/setup-python@v5
            with:
              python-version: '3.11'

          - name: Install dependencies
            run: |
              pip install traceloop-sdk openai

          - name: Run experiments
            env:
              TRACELOOP_API_KEY: ${{ secrets.TRACELOOP_API_KEY }}
              OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
            run: |
              python experiments/run_ci_experiments.py
    ```

    <Note>
      **Add secrets to your GitHub repository**

      Make sure all secrets used in your experiment script (like `OPENAI_API_KEY`) are added to both:

      * Your GitHub Actions workflow configuration
      * Your GitHub repository secrets

      Traceloop requires you to add `TRACELOOP_API_KEY` to your GitHub repository secrets. [Generate one in Settings →](/settings/managing-api-keys)
    </Note>

    <Frame>
      <img />

      <img />
    </Frame>
  </Step>

  <Step title="View Results in Your Pull Request">
    Once configured, every pull request will automatically trigger the experiment run. The Traceloop GitHub App will post a comment on the PR with a comprehensive summary of the evaluation results.

    <Frame>
      <img />

      <img />
    </Frame>

    The PR comment includes:

    * **Overall experiment status**
    * **Evaluation metrics**
    * **Link to detailed results**

    ### Experiment Dashboard

    Click on the link in the PR comment to view the complete experiment run in the Traceloop experiment dashboard, where you can:

    * Review individual test cases and their evaluator scores
    * Analyze which specific inputs passed or failed
    * Compare results with previous runs to track improvements or regressions
    * Drill down into evaluator reasoning and feedback

    <Frame>
      <img />

      <img />
    </Frame>
  </Step>
</Steps>


# Posthog
Source: https://www.traceloop.com/docs/integrations/posthog

Connect Traceloop to Posthog to combine LLM insights with your product analytics

Connecting Traceloop to Posthog can be done by following these steps:

<Steps>
  <Step title="Get the needed data from Posthog">
    Go to your Posthog instance settings and get the following data:

    * API URL (should be something like `https://us.i.posthog.com`)
    * Project API key (should be in the format `phc_-<key>`)
  </Step>

  <Step title="Set up the Integration within Traceloop">
    Go to the [integrations page](https://app.traceloop.com/settings/integrations) within Traceloop and click on the Posthog card.

    <Frame>
      <img />

      <img />
    </Frame>
  </Step>

  <Step title="Fill in the form">
    Fill in the data you got from Posthog. Choose the environment you want to connect to Posthog and click on "Enable".

    <Frame>
      <img />

      <img />
    </Frame>
  </Step>
</Steps>

**That's it!**

Go to your Posthog instance, click "Activity" and search for events named `traceloop span`.

You can then create a new dashboard from the "LLM Metrics - Traceloop" template to visualize the data.

<Frame>
  <img />
</Frame>


# Slack
Source: https://www.traceloop.com/docs/integrations/slack

Get daily or weekly messages about your AI flows directly in Slack

Connecting Traceloop to Slack allows you to receive automated updates about your AI flows. You can configure daily or weekly messages to stay informed about your application's performance and insights.

<Steps>
  <Step title="Set up the Integration within Traceloop">
    Go to the [integrations page](https://app.traceloop.com/settings/integrations) within Traceloop and click on the Slack card.

    <Frame>
      <img />

      <img />
    </Frame>
  </Step>

  <Step title="Authorize Slack">
    Click on the Slack integration and follow the "Connect to Slack" button to authorize Traceloop to send messages to your Slack workspace.
  </Step>

  <Step title="Configure your preferences">
    Choose your notification preferences:

    * Select the Slack channel where you want to receive updates

    <Info>
      **Important:** Make sure to invite the Traceloop app to the channel before enabling the integration.
    </Info>

    <Frame>
      <img />
    </Frame>

    * Select the desired schedule -  daily/weekly
    * Set the required time and timezone
    * Choose which environment to monitor

    <Frame>
      <img />

      <img />
    </Frame>
  </Step>
</Steps>

**That's it!**

You'll now receive automated messages in your chosen Slack channel with insights about your AI flows, including key metrics and performance updates.

<Frame>
  <img />
</Frame>


# Introduction
Source: https://www.traceloop.com/docs/introduction

Monitor, debug and test the quality of your LLM outputs

Traceloop automatically monitors the quality of your LLM outputs. It helps you to debug and test changes to your models and prompts.

* Get real-time alerts about your model's quality
* Execution tracing for every request
* Gradually rollout changes to models and prompts
* Debug and re-run issues from production in your IDE

Need help using Traceloop? Ping us at [dev@traceloop.com](mailto:dev@traceloop.com)

### Get Started - with OpenLLMetry SDK or Traceloop Hub

Traceloop uses OpenTelemetry to monitor and trace your LLM application.
You can install the OpenLLMetry SDK in your application, or use Traceloop Hub as a smart proxy to all your LLM calls.

To get started, pick the language you are using and follow the instructions.

<CardGroup>
  <Card title="Hub" icon="arrows-to-dot" href="/hub/getting-started">
    Beta
  </Card>

  <Card title="Python SDK" icon="python" href="/openllmetry/getting-started-python">
    Available
  </Card>

  <Card title="Typescript SDK" icon="node" href="/openllmetry/getting-started-ts">
    Available
  </Card>

  <Card title="Go SDK" icon="golang" href="/openllmetry/getting-started-go">
    Beta
  </Card>

  <Card title="Ruby SDK" icon="gem" href="/openllmetry/getting-started-ruby">
    Beta
  </Card>
</CardGroup>


# Defining Monitors
Source: https://www.traceloop.com/docs/monitoring/defining-monitors

Learn how to create and configure monitors to evaluate your LLM outputs

Monitors in Traceloop allow you to continuously evaluate your LLM outputs in real time. This guide walks you through the process of creating and configuring monitors for your specific use cases.

## Creating a Monitor

To create a monitor, you need to complete these steps:

<Steps>
  <Step title="Send Traces">
    Connect the SDK to your system and add decorators to your flow. See [OpenLLMetry](/openllmetry/introduction) for setup instructions.
  </Step>

  <Step title="Choose an Evaluator">
    Select the evaluation logic that will run on matching spans. You can define your own custom evaluators or use the pre-built ones by Traceloop. See [Evaluators](/evaluators/intro) for more details.
  </Step>

  <Step title="Define Span Filter">
    Set criteria that determine which spans the monitor will evaluate.
  </Step>

  <Step title="Configure Settings">
    Set up how the monitor operates, including sampling rates and other advanced options.
  </Step>
</Steps>

### Basic Monitor Setup

Navigate to the Monitors page and click the **New** button to open the Evaluator Library. Choose the evaluator you want to run in your monitor.
Next, you will be able to configure which spans will be monitored.

## Span Filtering

The span filtering modal shows the actual spans from your system, letting you see how your chosen filters apply to real data.
Add filters by clicking on the  <kbd>+</kbd>  button.

<Frame>
  <img />

  <img />
</Frame>

### Filter Options

* **Environment**: Filter by a specific environment
* **Workflow Name**: Filter by the workflow name defined in your system
* **Service Name**: Target spans from specific services or applications
* **AI Data**: Filter based on LLM-specific attributes like model name, token usage, streaming status, and other AI-related metadata
* **Attributes**: Filter based on span attributes

<img />

<img />

## Monitor Settings

### Map Input

You need to map the appropriate span fields to the evaluator’s input schema.
This can be done easily by browsing through the available span field options—once you select a field, the real data is immediately displayed so you can see how it maps to the input.

<Frame>
  <img />

  <img />
</Frame>

When the field data is not plain text, you can use JSON key mapping or Regex to extract the specific content you need.

For example, if your content is an array and you want to extract the "text" field from the object:

```json theme={null}
[{"type":"text","text":"explain who are you and what can you do in one sentence"}]
```

You can use JSON key mapping like `0.text` to extract just the text content. The JSON key mapping will be applied to the Preview table, allowing you to see the extracted result in real-time.

<Frame>
  <img />

  <img />
</Frame>

You can use Regex like `text":"(.+?)"` to extract just the text content. The regex will be applied to the Preview table, allowing you to see the extracted result in real-time.

<Frame>
  <img />

  <img />
</Frame>

### Advanced

You can set a **Rate sample** to control the percentage of spans within the selected filter group that the monitor will run on.


# Introduction
Source: https://www.traceloop.com/docs/monitoring/introduction

Detect hallucinations and regressions in the quality of your LLMs

One of the key features of Traceloop is the ability to monitor the quality of your LLM outputs in **real time**. It helps you to detect hallucinations and regressions in the quality of your models and prompts.

To start monitoring your LLM outputs, make sure you installed OpenLLMetry and configured it to send data to Traceloop. If you haven't done that yet, you can follow the instructions in the [Getting Started](/openllmetry/getting-started) guide.
Next, if you're not using a [supported LLM framework](/openllmetry/tracing/supported#frameworks), [make sure to annotate workflows and tasks](/openllmetry/tracing/annotations).

<Frame>
  <img />

  <img />
</Frame>

## What is a Monitor?

A monitor is an evaluator that runs on a group of defined spans with specific characteristics in real time. For every span that matches the group filter, it will run the evaluator and log the monitor result. This allows you to continuously assess the quality and performance of your LLM outputs as they are generated in production.

Monitors can use two types of evaluators:

* **LLM-as-a-Judge**: uses a large language model to evaluate outputs based on semantic qualities. You can create custom evaluators with this method by writing prompts that capture your own criteria.
* **Traceloop built in evaluators**: deterministic evaluations for structural validation, safety checks, and syntactic analysis.

All monitors connect to our comprehensive [Evaluators](/evaluators/intro) library, allowing you to choose the right evaluation approach for your specific use case.


# Using Monitors
Source: https://www.traceloop.com/docs/monitoring/using-monitors

Learn how to view, analyze, and act on monitor results in your LLM applications

Once you've created monitors, Traceloop continuously evaluates your LLM outputs and provides insights into their performance. This guide explains how to interpret and act on monitor results.

## Monitor Dashboard

The Monitor Dashboard provides an overview of all active monitors and their current status.
It shows each monitor’s health, the number of times it has run, and the most recent execution time.

<Frame>
  <img />

  <img />
</Frame>

## Viewing Monitor Results

### Real-time Monitoring

Monitor results are displayed in real-time as your LLM applications generate new spans. You can view:

* **Run Details**: The span value that was evaluated and its result
* **Trend Analysis**: Performance over time
* **Volume Metrics**: Number of evaluations performed
* **Evaluator Output Rates**: Such as success rates for threshold-based evaluators

### Monitor Results Page

Click on any monitor to access its detailed results page. The monitor page provides comprehensive analytics and span-level details.

#### Chart Visualizations

The Monitor page includes multiple chart views to help you analyze your data, and you can switch between chart types using the selector in the top-right corner.

**Line Chart View** - Shows evaluation trends over time:

<Frame>
  <img />

  <img />
</Frame>

**Bar Chart View** - Displays evaluation results in time buckets:

<Frame>
  <img />

  <img />
</Frame>

#### Filtering and Time Controls

The top toolbar provides filtering options:

* **Environment**: Filter by production, staging, etc.
* **Time Range**: 24h, 7d, 14d, or custom ranges
* **Metric**: Select which evaluator output property to measure
* **Bucket Size**: 6h, Hourly, Daily, etc.
* **Aggregation**: Choose average, median, sum, min, max, or count

#### Matching Spans Table

The bottom section shows all spans that matched your monitor's filter criteria:

* **Timestamp**: When the evaluation occurred
* **Input**: The actual content that was mapped to be evaluated
* **Output**: The evaluation result/score
* **Completed Runs**: Total successful/error evaluations
* **Error Runs**: Failed evaluation attempts

Each row includes a link icon to view the full span details in the trace explorer:

<Frame>
  <img />

  <img />
</Frame>

For further information on tracing refer to [OpenLLMetry](/openllmetry/introduction).

<Tip>
  Ready to set up an evaluator for your monitor? Learn more about creating and configuring evaluators in the [Evaluators](/evaluators/intro) section.
</Tip>


# SDK Initialization Options
Source: https://www.traceloop.com/docs/openllmetry/configuration

Documentation of the initialization options for the SDKs.

Most configuration options can be set via environment variables or via the SDK's initialization options.

<Warning>
  The SDK initialization options always take precedence over the environment
  variables.
</Warning>

See below for the list of options.

## Application Name

You can customize the application name that will be logged with the traces. This is useful to identify if you have multiple services with
OpenLLMetry installed.

<CodeGroup>
  ```python Python theme={null}
  Traceloop.init(app_name="my app name")
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({ appName: "my app name" });
  ```
</CodeGroup>

## Resource Attributes

You can further add any custom attributes to the OpenTelemetry resource. This is useful to add information about the environment
where the application is running, such as the environment name, the application version, etc.

<CodeGroup>
  ```python Python theme={null}
  Traceloop.init(resource_attributes={"env": "prod", "version": "1.0.0"})
  ```
</CodeGroup>

## Base URL

This defines the OpenTelemetry endpoint to connect to. It defaults to [https://api.traceloop.com](https://api.traceloop.com)

If you prefix it with `http` or `https`, it will use the OTLP/HTTP protocol.
Otherwise, it will use the OTLP/GRPC protocol.

For configuring this to different observability platform, check out our [integrations section](/openllmetry/integrations).

<Note>
  The OpenTelemetry standard defines that the actual endpoint should always end
  with `/v1/traces`. Thus, if you specify a base URL, we always append
  `/v1/traces` to it. This is similar to how `OTEL_EXPORTER_OTLP_ENDPOINT` works
  in all OpenTelemetry SDKs.
</Note>

<CodeGroup>
  ```bash Environment Variable theme={null}
  TRACELOOP_BASE_URL=<OpenTelemetry Endpoint>
  ```

  ```python Python theme={null}
  Traceloop.init(api_endpoint=<opentelemetry endpoint>)
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({ baseUrl: <opentelemetry endpoint> })
  ```
</CodeGroup>

## API Key

If set, this is sent as a bearer token on the Authorization header.

[Traceloop](/openllmetry/integrations/traceloop), for example, use this to authenticate incoming traces and requests.

<Tip>
  If this is not set, and the base URL is set to `https://api.traceloop.com`,
  the SDK will generate a new API key automatically with the Traceloop
  dashboard.
</Tip>

<CodeGroup>
  ```bash Environment Variable theme={null}
  TRACELOOP_API_KEY=<api key>
  ```

  ```python Python theme={null}
  Traceloop.init(api_key=<api key>)
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({ apiKey: <api key> })
  ```
</CodeGroup>

## Headers

If set, this is sent as-is as HTTP headers. This is useful for custom authentication protocols that some observability platforms require.
The format follows the [W3C Correlation-Context](https://github.com/w3c/baggage/blob/master/baggage/HTTP_HEADER_FORMAT.md) format, i.e.
`key1=value1,key2=value2`. If you need spaces, use `%20`.
This is similar to how `OTEL_EXPORTER_OTLP_HEADERS` works in all OpenTelemetry SDKs.

<Note>If this is set, the API key is ignored.</Note>

<CodeGroup>
  ```bash Environment Variable theme={null}
  TRACELOOP_HEADERS=key1=value1,key2=value2
  ```

  ```python Python theme={null}
  Traceloop.init(headers={"key1": "value1", "key2": "value2"})
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({ headers: { key1: "value1", key2: "value2" } });
  ```
</CodeGroup>

## Custom Traces Exporter

If, for some reason, you cannot use the OTLP/HTTP or OTLP/GRPC exporter that is provided with the SDK, you can set a custom
exporter (for example, to Jaeger, Zipkin, or others)

<Note>
  If this is set, Base URL, API key and headers configurations are ignored.
</Note>

<CodeGroup>
  ```python Python theme={null}
  Traceloop.init(exporter=ZipkinExporter(endpoint="http://localhost:9411/api/v2/spans"))
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({ exporter: new ZipkinExporter() });
  ```
</CodeGroup>

## Disable Batch

By default, the SDK batches spans using the [OpenTelemetry batch span processor](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/batchprocessor/README.md).
When working locally, sometime you may wish to disable this behavior. You can do that with this flag.

<CodeGroup>
  ```python Python theme={null}
  Traceloop.init(disable_batch=True)
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({ disableBatch: true });
  ```
</CodeGroup>

## Disable Tracing of Prompt Content

By default, OpenLLMetry logs prompts, completions, and embeddings to span attributes.

However, you may want to disable this logging for privacy reasons, as they may contain highly sensitive data from your users.
You may also simply want to reduce the size of your traces.

<CodeGroup>
  ```bash Environment Variable theme={null}
  TRACELOOP_TRACE_CONTENT=false
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({ traceContent: false });
  ```
</CodeGroup>

## Control Logging

You can control the logging level of the SDK. By default, the SDK logs at the WARN level.

<CodeGroup>
  ```js Typescript / Javascript theme={null}
  // one of "debug", "info", "warn", "error"
  Traceloop.initialize({ logLevel: "debug" });
  ```
</CodeGroup>

## Control Telemetry

The SDK collects anonymous telemetry data to help us identify and fix issues with instrumentations.
You can disable this feature if needed.

<CodeGroup>
  ```bash Environment Variable theme={null}
  TRACELOOP_TELEMETRY=false
  ```

  ```python Python theme={null}
  Traceloop.init(telemetry_enabled=False)
  ```
</CodeGroup>

<Note>
  For more information about what telemetry data we collect, please see our
  [Privacy
  documentation](https://www.traceloop.com/docs/openllmetry/privacy/telemetry).
</Note>

## Enrich Collected Metrics and Traces

By default, the SDK enriches collected metrics and traces with additional information such as the OpenAI token usage for streaming requests.
This may affect latency on the first request, as it needs to fetch the embeddings.

<CodeGroup>
  ```python Python theme={null}
  Traceloop.init(should_enrich_metrics=False) 
  ```

  ```bash Environment Variable (JS/TS Only) theme={null}
  TRACELOOP_ENRICH_TOKENS=false
  ```
</CodeGroup>

## Traceloop Sync

By default, Traceloop Sync (for prompts and other configurations) is disabled, even if you're sending traces to Traceloop.
If you're using the prompt registry, you should enable it.
To enable it or change any defaults, see the example below. The values listed are the default values,
so you don't need to set them unless you want to change the defaults.

<Note>Traceloop Sync must be enabled in order to use the prompt registry.</Note>

<CodeGroup>
  ```bash Environment Variable theme={null}
  TRACELOOP_SYNC_ENABLED=true
  TRACELOOP_SYNC_MAX_RETRIES=3
  TRACELOOP_SYNC_POLLING_INTERVAL=60 # seconds
  TRACELOOP_SYNC_DEV_POLLING_INTERVAL=5 # seconds
  ```

  ```python Python theme={null}
  Traceloop.init(traceloop_sync_enabled=True)
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({
    traceloopSyncEnabled: true,
    traceloopSyncMaxRetries: 3,
    traceloopSyncPollingInterval: 60, // in seconds
    traceloopSyncDevPollingInterval: 5, // in seconds
  });
  ```
</CodeGroup>

## Instrumentations

By default, the SDK automatically detects which models and frameworks you are using and instruments them for you.
You can override this and specify specific frameworks and models you want to instrument. This, for example, allow you to
specify that you want to log calls to OpenAI, but not Anthropic, or vice-versa.

You can either explictly specify the instruments you want to enable, or the ones you want to block.

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk.instruments import Instruments

  Traceloop.init(instruments={Instruments.OPENAI, Instruments.PINECONE})

  # OR

  Traceloop.init(block_instruments={Instruments.ANTHROPIC})

  ```
</CodeGroup>

```
```


# Local Development
Source: https://www.traceloop.com/docs/openllmetry/contributing/developing



You can contribute both new instrumentations or update and improve the different SDKs.

[Join our Slack community](https://traceloop.com/slack) to chat and get help on any issues you may encounter.

The Python and Typescript are monorepos that use [nx](https://nx.dev) to manage the different packages.
Make sure you have `node >= 18` and `nx` installed globally.

## Basic guide for using nx

Most commands can be run from the root of the project. For example, to lint the entire project, run:

```bash theme={null}
nx run-many -t lint
```

Other commands you can use simiarily are `test`, or `build`, or `lock` and `install` (for Python).

To run a specific command on a specific package, run:

```bash theme={null}
nx run <package>:<command>
```

## Python

We use `poetry` to manage packages, and each package is managed independently under its own directory under `/packages`.
All instrumentations depends on `opentelemetry-semantic-conventions-ai`,
and `traceloop-sdk` depends on all the instrumentations.

If adding a new instrumentation, make sure to use it in `traceloop-sdk`, and write proper tests.

### Debugging

No matter if you're working on an instrumentation or on the SDK, we recommend testing the changes by using
the SDK in the sample app (`/packages/sample-app`) or the tests under the SDK.

### Running tests

We record HTTP requests and then replay them in tests to avoid making actual calls to the foundation model providers.
See [vcr.py](https://github.com/kevin1024/vcrpy) and [pollyjs](https://github.com/Netflix/pollyjs/) to do that, check out
their documentation to understand how to use them and re-record the requests.

You can run all tests by running:

```bash theme={null}
nx run-many -t test
```

Or run a specific test by running:

```bash theme={null}
nx run <package>:test
```

For example, to run the tests for the `openai` instrumentation package, run:

<CodeGroup>
  ```bash Python theme={null}
  nx run opentelemetry-instrumentation-openai:test
  ```

  ```bash Typescript theme={null}
  nx run @traceloop/instrumentation-openai:test
  ```
</CodeGroup>

## Typescript

We use `npm` with workspaces to manage packages in the monorepo. Install by running `npm install` in the root of the project.
Each package has its own test suite. You can use the sample app to run and test changes locally.


# Overview
Source: https://www.traceloop.com/docs/openllmetry/contributing/overview

We welcome any contributions to  OpenLLMetry, big or small.

## Community

It's the early days of our project and we're working hard to build an awesome, inclusive community. In order to grow this, all community members must adhere to our [Code of Conduct](https://github.com/traceloop/openllmetry/blob/main/CODE_OF_CONDUCT.md).

## Bugs and issues

Bug reports help make OpenLLMetry a better experience for everyone. When you report a bug, a template will be created automatically containing information we'd like to know.

Before raising a new issue, please search existing ones to make sure you're not creating a duplicate.

<Info>
  If the issue is related to security, please email us directly at
  [dev@traceloop.com](mailto:dev@traceloop.com).
</Info>

## Deciding what to work on

You can start by browsing through our list of issues or adding your own that improves on the test suite experience. Once you've decided on an issue, leave a comment and wait to get approved; this helps avoid multiple people working on the same issue.

If you're ever in doubt about whether or not a proposed feature aligns with OpenLLMetry as a whole, feel free to raise an issue about it and we'll get back to you promptly.

## Writing and submitting code

Anyone can contribute code to OpenLLMetry. To get started, check out the local development guide, make your changes, and submit a pull request to the main repository.

## Licensing

All of OpenLLMetry's code is under the Apache 2.0 license.

Any third party components incorporated into our code are licensed under the original license provided by the applicable component owner.


# GenAI Semantic Conventions
Source: https://www.traceloop.com/docs/openllmetry/contributing/semantic-conventions



With OpenLLMetry, we aim at defining an extension of the standard
[OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions) for gen AI applications.
We are also [leading OpenTelemetry's LLM semantic convention WG](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md)
to standardize these conventions.

It defines additional attributes for spans to so we can log prompts, completions, token usage, etc.
These attributes are reported on relevant spans when you use the OpenLLMetry SDK or the individual instrumentations.

This is a work in progress, and we welcome your feedback and contributions!

## Implementations

* [Python](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-semantic-conventions-ai)
* [TypeScript](https://github.com/traceloop/openllmetry-js/tree/main/packages/ai-semantic-conventions)
* [Go](https://github.com/traceloop/go-openllmetry/tree/main/semconv-ai)
* [Ruby](https://github.com/traceloop/openllmetry-ruby/tree/main/semantic_conventions_ai)

## Traces Definitions

### LLM Foundation Models

* `gen_ai.system` - The vendor of the LLM (e.g. OpenAI, Anthropic, etc.)

* `gen_ai.request.model` - The model requested (e.g. `gpt-4`, `claude`, etc.)

* `gen_ai.response.model` - The model actually used (e.g. `gpt-4-0613`, etc.)

* `gen_ai.request.max_tokens` - The maximum number of response tokens requested

* `gen_ai.request.temperature`

* `gen_ai.request.top_p`

* `gen_ai.prompt` - An array of prompts as sent to the LLM model

* `gen_ai.completion` - An array of completions returned from the LLM model

* `gen_ai.usage.prompt_tokens` - The number of tokens used for the prompt in the request

* `gen_ai.usage.completion_tokens` - The number of tokens used for the completion response

* `gen_ai.usage.total_tokens` - The total number of tokens used

* `gen_ai.usage.reasoning_tokens` (OpenAI) - The total number of reasoning tokens used as a part of `completion_tokens`

* `gen_ai.request.reasoning_effort` (OpenAI) - Reasoning effort mentioned in the request (e.g. `minimal`, `low`, `medium`, or `high`)

* `gen_ai.request.reasoning_summary` (OpenAI) - Level of reasoning summary mentioned in the request (e.g. `auto`, `concise`, or `detailed`)

* `gen_ai.response.reasoning_effort` (OpenAI) - Actual reasoning effort used

* `llm.request.type` - The type of request (e.g. `completion`, `chat`, etc.)

* `llm.usage.total_tokens` - The total number of tokens used

* `llm.request.functions` - An array of function definitions provided to the model in the request

* `llm.frequency_penalty`

* `llm.presence_penalty`

* `llm.chat.stop_sequences`

* `llm.user` - The user ID sent with the request

* `llm.headers` - The headers used for the request

### Vector DBs

* `db.system` - The vendor of the Vector DB (e.g. Chroma, Pinecone, etc.)
* `db.vector.query.top_k` - The top k used for the query
* For each vector in the query, an event named `db.query.embeddings` is fired with this attribute:
  * `db.query.embeddings.vector` - The vector used in the query
* For each vector in the response, an event named `db.query.result` is fired for each vector in the response with the following attributes:
  * `db.query.result.id` - The ID of the vector
  * `db.query.result.score` - The score of the vector in relation to the query
  * `db.query.result.distance` - The distance of the vector from the query vector
  * `db.query.result.metadata` - Related metadata that was attached to the result vector in the DB
  * `db.query.result.vector` - The vector returned
  * `db.query.result.document` - The document that is represented by the vector

#### Pinecone-specific

* `pinecone.query.id`
* `pinecone.query.namespace`
* `pinecone.query.top_k`
* `pinecone.usage.read_units` - The number of read units used (as reported by Pinecone)
* `pinecone.usage.write_units` - The number of write units used (as reported by Pinecone)

### LLM Frameworks

* `traceloop.span.kind` - One of `workflow`, `task`, `agent`, `tool`.
* `traceloop.workflow.name` - The name of the parent workflow/chain associated with this span
* `traceloop.entity.name` - Framework-related name for the entity (for example, in Langchain, this will be the name of the specific class that defined the chain / subchain).
* `traceloop.association.properties` - Context on the request (relevant User ID, Chat ID, etc.)

## Metrics Definition

### LLM Foundation Models


# Go
Source: https://www.traceloop.com/docs/openllmetry/getting-started-go

Install OpenLLMetry for Go by following these 3 easy steps and get instant monitoring.

<Steps>
  <Step title="Install the SDK">
    Run the following command in your terminal:

    ```bash theme={null}
    go get github.com/traceloop/go-openllmetry/traceloop-sdk
    ```

    In your LLM app, initialize the Traceloop tracer like this:

    ```go theme={null}
    import sdk "github.com/traceloop/go-openllmetry/traceloop-sdk"

    func main() {
      ctx := context.Background()

      traceloop := sdk.NewClient(config.Config{
        BaseURL: "api.traceloop.com",
        APIKey: os.Getenv("TRACELOOP_API_KEY"),
      })
      defer func() { traceloop.Shutdown(ctx) }()

      traceloop.Initialize(ctx)
    }
    ```
  </Step>

  <Step title="Log your prompts">
    <Frame>
      <img />

      <img />
    </Frame>

    For now, we don't automatically instrument libraries on Go (as opposed to Python and Javascript).
    This will change in later versions.

    This means that you'll need to manually log your prompts and completions.

    ```go theme={null}
    import (
        openai "github.com/sashabaranov/go-openai"
    )

    func call_llm() {
    	// Call OpenAI like you normally would
    	resp, err := client.CreateChatCompletion(
    		context.Background(),
    		openai.ChatCompletionRequest{
    			Model: openai.GPT3Dot5Turbo,
    			Messages: []openai.ChatCompletionMessage{
    				{
    					Role:    openai.ChatMessageRoleUser,
    					Content: "Tell me a joke about OpenTelemetry!",
    				},
    			},
    		},
    	)

    	// Log the request and the response
    	log := dto.PromptLogAttributes{
    		Prompt: dto.Prompt{
    			Vendor: "openai",
    			Mode:   "chat",
    			Model:  request.Model,
    		},
    		Completion: dto.Completion{
    			Model: resp.Model,
    		},
    		Usage: dto.Usage{
    			TotalTokens:      resp.Usage.TotalTokens,
    			CompletionTokens: resp.Usage.CompletionTokens,
    			PromptTokens:     resp.Usage.PromptTokens,
    		},
    	}

    	for i, message := range request.Messages {
    		log.Prompt.Messages = append(log.Prompt.Messages, dto.Message{
    			Index:   i,
    			Content: message.Content,
    			Role:    message.Role,
    		})
    	}

    	for _, choice := range resp.Choices {
    		log.Completion.Messages = append(log.Completion.Messages, dto.Message{
    			Index:   choice.Index,
    			Content: choice.Message.Content,
    			Role:    choice.Message.Role,
    		})
    	}

    	traceloop.LogPrompt(ctx, log)
    }
    ```

    }
  </Step>

  <Step title="Configure trace exporting">
    Lastly, you'll need to configure where to export your traces.
    The 2 environment variables controlling this are `TRACELOOP_API_KEY` and `TRACELOOP_BASE_URL`.

    For Traceloop, read on. For other options, see [Exporting](/openllmetry/integrations/introduction).

    ### Using Traceloop Cloud

    <Note>
      You need an API key to send traces to Traceloop.
      [Generate one in Settings](https://app.traceloop.com/settings/api-keys) by selecting
      a project and environment, then click **Generate API key**.

      ⚠️ **Important:** Copy the key immediately - it won't be shown again after you close or reload the page.

      [Detailed instructions →](/settings/managing-api-keys)
    </Note>

    Set the API key as an environment variable in your app named `TRACELOOP_API_KEY`:

    ```bash theme={null}
    export TRACELOOP_API_KEY=your_api_key_here
    ```

    Done! You'll get instant visibility into everything that's happening with your LLM.
    If you're calling a vector DB, or any other external service or database, you'll also see it in the Traceloop dashboard.

    <Tip>
      **Not seeing traces?** Make sure you're viewing the correct project and environment in the
      dashboard that matches your API key. See [Troubleshooting](/settings/managing-api-keys#troubleshooting).
    </Tip>
  </Step>
</Steps>


# Next.js
Source: https://www.traceloop.com/docs/openllmetry/getting-started-nextjs

Install OpenLLMetry for Next.js by following these 3 easy steps and get instant monitoring.

You can also check out our full working example with Next.js 13 [here](https://github.com/traceloop/openllmetry-nextjs-demo).

<Steps>
  <Step title="Install the SDK">
    <Tip>
      Want our AI to do it for you? <a href="">Click here</a>
    </Tip>

    Run the following command in your terminal:

    <CodeGroup>
      ```bash npm theme={null}
      npm install @traceloop/node-server-sdk
      ```

      ```bash pnpm theme={null}
      pnpm add @traceloop/node-server-sdk
      ```

      ```bash yarn theme={null}
      yarn add @traceloop/node-server-sdk
      ```
    </CodeGroup>

    <Tabs>
      <Tab title="With Pages Router">
        Create a file named `instrumentation.ts` in the root of your project (i.e., outside of the `pages` or 'app' directory) and add the following code:

        ```ts theme={null}
        export async function register() {
          if (process.env.NEXT_RUNTIME === "nodejs") {
            await import("./instrumentation.node.ts");
          }
        }
        ```

        <Warning>
          Please note that you might see the following warning: `An import path can only
                      end with a '.ts' extension when 'allowImportingTsExtensions' is enabled` To
          resolve it, simply add `"allowImportingTsExtensions": true` to your
          tsconfig.json
        </Warning>

        Create a file named `instrumentation.node.ts` in the root of your project and add the following code:

        ```ts theme={null}
        import * as traceloop from "@traceloop/node-server-sdk";
        import OpenAI from "openai";
        // Make sure to import the entire module you want to instrument, like this:
        // import * as LlamaIndex from "llamaindex";

        traceloop.initialize({
          appName: "app",
          disableBatch: true,
          instrumentModules: {
            openAI: OpenAI,
            // Add any other modules you'd like to instrument here
            // for example:
            // llamaIndex: LlamaIndex,
          },
        });
        ```

        <Warning>
          Make sure to explictly pass any LLM modules you want to instrument as
          otherwise auto-instrumentation won't work on Next.js. Also make sure to set
          `disableBatch` to `true`.
        </Warning>

        On Next.js v12 and below, you'll also need to add the following to your `next.config.js`:

        ```js theme={null}
        /** @type {import('next').NextConfig} */
        const nextConfig = {
          experimental: {
            instrumentationHook: true,
          },
        };

        module.exports = nextConfig;
        ```

        <Tip>
          See Next.js [official OpenTelemetry
          docs](https://nextjs.org/docs/pages/building-your-application/optimizing/open-telemetry)
          for more information.
        </Tip>
      </Tab>

      <Tab title="With App Router">
        Install the following packages by running the following commands in your terminal:

        <CodeGroup>
          ```bash npm theme={null}
          npm install --save-dev node-loader
          npm i supports-color@8.1.1
          ```

          ```bash pnpm theme={null}
          pnpm add -D node-loader
          pnpm add supports-color@8.1.1
          ```

          ```bash yarn theme={null}
          yarn add -D node-loader
          yarn add supports-color@8.1.1
          ```
        </CodeGroup>

        Edit your `next.config.js` file and add the following webpack configuration:

        ```js theme={null}
        const nextConfig = {
        webpack: (config, { isServer }) => {
          config.module.rules.push({
            test: /\.node$/,
            loader: "node-loader",
          });
          if (isServer) {
            config.ignoreWarnings = [{ module: /opentelemetry/ }];
          }
          return config;
        },
        };
        ```

        On every app API route you want to instrument, add the following code at the top of the file:

        ```ts theme={null}
        import * as traceloop from "@traceloop/node-server-sdk";
        import OpenAI from "openai";
        // Make sure to import the entire module you want to instrument, like this:
        // import * as LlamaIndex from "llamaindex";

        traceloop.initialize({
          appName: "app",
          disableBatch: true,
          instrumentModules: {
            openAI: OpenAI,
            // Add any other modules you'd like to instrument here
            // for example:
            // llamaIndex: LlamaIndex,
          },
        });
        ```

        <Tip>
          See Next.js [official OpenTelemetry
          docs](https://nextjs.org/docs/app/building-your-application/optimizing/open-telemetry)
          for more information.
        </Tip>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Annotate your workflows">
    <Frame>
      <img />

      <img />
    </Frame>

    If you have complex workflows or chains, you can annotate them to get a better understanding of what's going on.
    You'll see the complete trace of your workflow on Traceloop or any other dashboard you're using.

    We have a set of [methods and decorators](/openllmetry/tracing/annotations) to make this easier.
    Assume you have a function that renders a prompt and calls an LLM, simply wrap it in a `withWorkflow()` function call.

    We also have compatible Typescript decorators for class methods which are more convenient.

    <Tip>
      If you're using a [supported LLM framework](/openllmetry/tracing/supported#frameworks) -
      we'll do that for you. No need to add any annotations to your code.
    </Tip>

    <CodeGroup>
      ```js Functions (async / sync) theme={null}
      async function suggestAnswers(question: string) {
        return await withWorkflow({ name: "suggestAnswers" }, () => {
          ...
        });
      }
      ```

      ```js Class Methods theme={null}
      class MyLLM {
        @traceloop.workflow({ name: "suggest_answers" })
        async suggestAnswers(question: string) {
          ...
        }
      }
      ```
    </CodeGroup>

    For more information, see the [dedicated section in the docs](/openllmetry/tracing/annotations).
  </Step>

  <Step title="Configure trace exporting">
    Lastly, you'll need to configure where to export your traces.
    The 2 environment variables controlling this are `TRACELOOP_API_KEY` and `TRACELOOP_BASE_URL`.

    For Traceloop, read on. For other options, see [Exporting](/openllmetry/integrations/introduction).

    ### Using Traceloop Cloud

    <Note>
      You need an API key to send traces to Traceloop.
      [Generate one in Settings](https://app.traceloop.com/settings/api-keys) by selecting
      a project and environment, then click **Generate API key**.

      ⚠️ **Important:** Copy the key immediately - it won't be shown again after you close or reload the page.

      [Detailed instructions →](/settings/managing-api-keys)
    </Note>

    Set the API key as an environment variable in your app named `TRACELOOP_API_KEY`:

    ```bash theme={null}
    export TRACELOOP_API_KEY=your_api_key_here
    ```

    Done! You'll get instant visibility into everything that's happening with your LLM.
    If you're calling a vector DB, or any other external service or database, you'll also see it in the Traceloop dashboard.

    <Tip>
      **Not seeing traces?** Make sure you're viewing the correct project and environment in the
      dashboard that matches your API key. See [Troubleshooting](/settings/managing-api-keys#troubleshooting).
    </Tip>
  </Step>
</Steps>


# Python
Source: https://www.traceloop.com/docs/openllmetry/getting-started-python

Install OpenLLMetry for Python by following these 3 easy steps and get instant monitoring.

You can also check out our full working example of a RAG pipeline with Pinecone [here](https://github.com/traceloop/pinecone-demo).

<Steps>
  <Step title="Install the SDK">
    <Tip>
      Want our AI to do it for you? <a href="">Click here</a>
    </Tip>

    Run the following command in your terminal:

    <CodeGroup>
      ```bash pip theme={null}
      pip install traceloop-sdk
      ```

      ```bash poetry theme={null}
      poetry add traceloop-sdk
      ```
    </CodeGroup>

    In your LLM app, initialize the Traceloop tracer like this:

    ```python theme={null}
    from traceloop.sdk import Traceloop

    Traceloop.init()
    ```

    If you're running this locally, you may want to disable batch sending, so you can see the traces immediately:

    ```python theme={null}
    Traceloop.init(disable_batch=True)
    ```
  </Step>

  <Step title="Annotate your workflows">
    <Frame>
      <img />

      <img />
    </Frame>

    If you have complex workflows or chains, you can annotate them to get a better understanding of what's going on.
    You'll see the complete trace of your workflow on Traceloop or any other dashboard you're using.

    We have a set of [decorators](/openllmetry/tracing/annotations) to make this easier.
    Assume you have a function that renders a prompt and calls an LLM, simply add `@workflow`.

    <Warning>
      The `@aworkflow` decorator is deprecated and will be removed in a future
      version. Use `@workflow` for both synchronous and asynchronous operations.
    </Warning>

    <Tip>
      If you're using a [supported LLM framework](/openllmetry/tracing/supported#frameworks) -
      we'll do that for you. No need to add any annotations to your code.
    </Tip>

    ```python theme={null}
    from traceloop.sdk.decorators import workflow

    @workflow(name="suggest_answers")
    def suggest_answers(question: str):
      ...

    # Works seamlessly with async functions too
    @workflow(name="summarize")
    async def summarize(long_text: str):
      ...
    ```

    For more information, see the [dedicated section in the docs](/openllmetry/tracing/annotations).
  </Step>

  <Step title="Configure trace exporting">
    Lastly, you'll need to configure where to export your traces.
    The 2 environment variables controlling this are `TRACELOOP_API_KEY` and `TRACELOOP_BASE_URL`.

    For Traceloop, read on. For other options, see [Exporting](/openllmetry/integrations/introduction).

    ### Using Traceloop Cloud

    <Note>
      You need an API key to send traces to Traceloop.
      [Generate one in Settings](https://app.traceloop.com/settings/api-keys) by selecting
      a project and environment, then click **Generate API key**.

      ⚠️ **Important:** Copy the key immediately - it won't be shown again after you close or reload the page.

      [Detailed instructions →](/settings/managing-api-keys)
    </Note>

    Set the API key as an environment variable in your app named `TRACELOOP_API_KEY`:

    ```bash theme={null}
    export TRACELOOP_API_KEY=your_api_key_here
    ```

    Done! You'll get instant visibility into everything that's happening with your LLM.
    If you're calling a vector DB, or any other external service or database, you'll also see it in the Traceloop dashboard.

    <Tip>
      **Not seeing traces?** Make sure you're viewing the correct project and environment in the
      dashboard that matches your API key. See [Troubleshooting](/settings/managing-api-keys#troubleshooting).
    </Tip>
  </Step>
</Steps>


# Ruby
Source: https://www.traceloop.com/docs/openllmetry/getting-started-ruby

Install OpenLLMetry for Ruby by following these 3 easy steps and get instant monitoring.

<Warning>This is still in beta. Give us feedback at [dev@traceloop.com](mailto:dev@traceloop.com)</Warning>

<Steps>
  <Step title="Install the SDK">
    Run the following command in your terminal:

    <CodeGroup>
      ```bash gem theme={null}
      gem install traceloop-sdk
      ```

      ```bash bundler theme={null}
      bundle add traceloop-sdk
      ```
    </CodeGroup>

    In your LLM app, initialize the Traceloop tracer like this:

    <Tip>
      If you're using Rails, this needs to be in `config/initializers/traceloop.rb`
    </Tip>

    ```ruby theme={null}
    require "traceloop/sdk"

    traceloop = Traceloop::SDK::Traceloop.new
    ```
  </Step>

  <Step title="Log your prompts">
    <Frame>
      <img />

      <img />
    </Frame>

    For now, we don't automatically instrument libraries on Ruby (as opposed to Python and Javascript).
    This will change in later versions.

    This means that you'll need to manually log your prompts and completions.

    ```ruby theme={null}
    require "openai"

    client = OpenAI::Client.new

    # This tracks the latency of the call and the response
    traceloop.workflow("joke_generator") do
      traceloop.llm_call(provider="openai", model="gpt-3.5-turbo") do |tracer|
        # Log the prompt
        tracer.log_prompt(user_prompt="Tell me a joke about OpenTelemetry")

        # Or use the OpenAI Format
        # tracer.log_messages([{ role: "user", content: "Tell me a joke about OpenTelemetry" }])

        # Call OpenAI like you normally would
        response = client.chat(
          parameters: {
            model: "gpt-3.5-turbo",
            messages: [{ role: "user", content: "Tell me a joke about OpenTelemetry" }]
          })

        # Pass the response form OpenAI as is to log the completion and token usage
        tracer.log_response(response)
      end
    end
    ```
  </Step>

  <Step title="Configure trace exporting">
    Lastly, you'll need to configure where to export your traces.
    The 2 environment variables controlling this are `TRACELOOP_API_KEY` and `TRACELOOP_BASE_URL`.

    For Traceloop, read on. For other options, see [Exporting](/openllmetry/integrations/introduction).

    ### Using Traceloop Cloud

    <Note>
      You need an API key to send traces to Traceloop.
      [Generate one in Settings](https://app.traceloop.com/settings/api-keys) by selecting
      a project and environment, then click **Generate API key**.

      ⚠️ **Important:** Copy the key immediately - it won't be shown again after you close or reload the page.

      [Detailed instructions →](/settings/managing-api-keys)
    </Note>

    Set the API key as an environment variable in your app named `TRACELOOP_API_KEY`:

    ```bash theme={null}
    export TRACELOOP_API_KEY=your_api_key_here
    ```

    Done! You'll get instant visibility into everything that's happening with your LLM.
    If you're calling a vector DB, or any other external service or database, you'll also see it in the Traceloop dashboard.

    <Tip>
      **Not seeing traces?** Make sure you're viewing the correct project and environment in the
      dashboard that matches your API key. See [Troubleshooting](/settings/managing-api-keys#troubleshooting).
    </Tip>
  </Step>
</Steps>


# Node.js
Source: https://www.traceloop.com/docs/openllmetry/getting-started-ts

Install OpenLLMetry for Node.js by following these 3 easy steps and get instant monitoring. 

<Warning>
  If you're on Next.js, follow the [Next.js
  guide](/openllmetry/getting-started-nextjs).
</Warning>

<Steps>
  <Step title="Install the SDK">
    <Tip>
      Want our AI to do it for you? <a href="">Click here</a>
    </Tip>

    Run the following command in your terminal:

    <CodeGroup>
      ```bash npm theme={null}
      npm install @traceloop/node-server-sdk
      ```

      ```bash pnpm theme={null}
      pnpm add @traceloop/node-server-sdk
      ```

      ```bash yarn theme={null}
      yarn add @traceloop/node-server-sdk
      ```
    </CodeGroup>

    In your LLM app, initialize the Traceloop tracer like this:

    ```js theme={null}
    import * as traceloop from "@traceloop/node-server-sdk";

    traceloop.initialize();
    ```

    <Warning>
      Because of the way Javascript works, you must import the Traceloop SDK before
      importing any LLM module like OpenAI.
    </Warning>

    If you're running this locally, you may want to disable batch sending, so you can see the traces immediately:

    ```js theme={null}
    traceloop.initialize({ disableBatch: true });
    ```

    <Note>
      If you're using Sentry, make sure to disable their OpenTelemetry configuration
      as it overrides OpenLLMetry. When calling `Sentry.init`, pass
      `skipOpenTelemetrySetup: true`.
    </Note>
  </Step>

  <Step title="Annotate your workflows">
    <Frame>
      <img />

      <img />
    </Frame>

    If you have complex workflows or chains, you can annotate them to get a better understanding of what's going on.
    You'll see the complete trace of your workflow on Traceloop or any other dashboard you're using.

    We have a set of [methods and decorators](/openllmetry/tracing/annotations) to make this easier.
    Assume you have a function that renders a prompt and calls an LLM, simply wrap it in a `withWorkflow()` function call.

    We also have compatible Typescript decorators for class methods which are more convenient.

    <Tip>
      If you're using a [supported LLM framework](/openllmetry/tracing/supported#frameworks) -
      we'll do that for you. No need to add any annotations to your code.
    </Tip>

    <CodeGroup>
      ```js Functions (async / sync) theme={null}
      async function suggestAnswers(question: string) {
        return await withWorkflow({ name: "suggestAnswers" }, () => {
          ...
        });
      }
      ```

      ```js Class Methods theme={null}
      class MyLLM {
        @traceloop.workflow({ name: "suggest_answers" })
        async suggestAnswers(question: string) {
          ...
        }
      }
      ```
    </CodeGroup>

    For more information, see the [dedicated section in the docs](/openllmetry/tracing/annotations).
  </Step>

  <Step title="Configure trace exporting">
    Lastly, you'll need to configure where to export your traces.
    The 2 environment variables controlling this are `TRACELOOP_API_KEY` and `TRACELOOP_BASE_URL`.

    For Traceloop, read on. For other options, see [Exporting](/openllmetry/integrations/introduction).

    ### Using Traceloop Cloud

    <Note>
      You need an API key to send traces to Traceloop.
      [Generate one in Settings](https://app.traceloop.com/settings/api-keys) by selecting
      a project and environment, then click **Generate API key**.

      ⚠️ **Important:** Copy the key immediately - it won't be shown again after you close or reload the page.

      [Detailed instructions →](/settings/managing-api-keys)
    </Note>

    Set the API key as an environment variable in your app named `TRACELOOP_API_KEY`:

    ```bash theme={null}
    export TRACELOOP_API_KEY=your_api_key_here
    ```

    Done! You'll get instant visibility into everything that's happening with your LLM.
    If you're calling a vector DB, or any other external service or database, you'll also see it in the Traceloop dashboard.

    <Tip>
      **Not seeing traces?** Make sure you're viewing the correct project and environment in the
      dashboard that matches your API key. See [Troubleshooting](/settings/managing-api-keys#troubleshooting).
    </Tip>
  </Step>
</Steps>


# LLM Observability with Axiom and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/axiom



<Frame>
  <img />
</Frame>

Axiom is an [observability platform](https://axiom.co/) that natively supports OpenTelemetry, you just need to route the traces to Axiom's endpoint and set the dataset, and API key:

```bash theme={null}
TRACELOOP_BASE_URL="https://api.axiom.co"
TRACELOOP_HEADERS="Authorization=Bearer <YOUR_API_KEY>,X-Axiom-Dataset=<YOUR_DATASET>"
```

For more information check out the [docs link](https://axiom.co/docs/send-data/opentelemetry).


# Azure Application Insights
Source: https://www.traceloop.com/docs/openllmetry/integrations/azure



Traceloop supports sending traces to Azure Application Insights via standard OpenTelemetry integrations.

Review how to setup [OpenTelemetry with Python in Azure Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=python).

<Frame>
  <img />
</Frame>

1. Provision an Application Insights instance in the [Azure portal](https://portal.azure.com/).
2. Get your Connection String from the instance - [details here](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sdk-connection-string?tabs=python).
3. Install required packages

```bash theme={null}
pip install azure-monitor-opentelemetry-exporter traceloop-sdk openai
```

4. Example implementation

```python theme={null}
import os
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow, task, agent, tool
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Configure the tracer provider to export traces to Azure Application Insights.
# Get your complete connection string from the Azure Portal or CLI.
exporter = AzureMonitorTraceExporter(connection_string="INSERT_CONNECTION_STRING_HERE")

# Pass your exporter to Traceloop
Traceloop.init(app_name="your_app_name", exporter=exporter)


@task(name="joke_creation")
def create_joke():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Tell me a joke about opentelemetry"}],
    )

    return completion.choices[0].message.content

@task(name="signature_generation")
def generate_signature(joke: str):
    completion = client.completions.create(model="davinci-002",
    prompt="add a signature to the joke:\n\n" + joke)

    return completion.choices[0].text

@agent(name="joke_translation")
def translate_joke_to_pirate(joke: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Translate the below joke to pirate-like english:\n\n{joke}"}],
    )

    history_jokes_tool()

    return completion.choices[0].message.content


@tool(name="history_jokes")
def history_jokes_tool():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"get some history jokes"}],
    )

    return completion.choices[0].message.content


@workflow(name="pirate_joke_generator")
def joke_workflow():
    eng_joke = create_joke()
    pirate_joke = translate_joke_to_pirate(eng_joke)
    signature = generate_signature(pirate_joke)
    print(pirate_joke + "\n\n" + signature)
    
if __name__ == "__main__":
    joke_workflow()
```


# LLM Observability with BMC and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/bmc



BMC Helix provides the capability to export observability data directly using the OpenTelemetry Collector. This requires deploying an OpenTelemetry Collector in your cluster.

See also [BMC Helix documentation](https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Operations-Management/BMC-Helix-AIOps/aiops244/Administering/Enabling-BMC-Helix-applications-to-collect-service-traces-from-OpenTelemetry/).

Exporting Data to an OpenTelemetry Collector

```yaml theme={null}
otlp:
  receiver:
    protocols:
      http:
        enabled: true
```

Then, set this env var, and you're done!

```bash theme={null}
TRACELOOP_BASE_URL=http://<tenantURL>
```


# LLM Observability with Braintrust and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/braintrust



To set up Braintrust as an [OpenTelemetry](https://opentelemetry.io/docs/) backend, you'll need to route the traces to Braintrust's OpenTelemetry endpoint, set your API key, and specify a parent project or experiment. Braintrust supports common patterns from [OpenLLLMetry](https://github.com/traceloop/openllmetry).

For more information, see the [Braintrust documentation](https://www.braintrust.dev/docs/guides/tracing#traceloop).

<Frame>
  <img />
</Frame>

To export OTel traces from Traceloop OpenLLMetry to Braintrust, set the following environment variables:

```bash theme={null}
TRACELOOP_BASE_URL=https://api.braintrust.dev/otel
TRACELOOP_HEADERS="Authorization=Bearer%20<Your API Key>, x-bt-parent=project_id:<Your Project ID>"
```

Note: When setting the bearer token, make sure to URL encode the space between "Bearer" and your API key using `%20`. For example:

```bash theme={null}
# Incorrect format
TRACELOOP_HEADERS="Authorization=Bearer sk-RiPodT20anlA1d3ki4T5I0V24WHXFuwvlPivUUoUGOnczOVI, x-bt-parent=project_id:<Your Project ID>"

# Correct format
TRACELOOP_HEADERS="Authorization=Bearer%20sk-RiPodT20anlA1d3ki4T5I0V24WHXFuwvlPivUUoUGOnczOVI, x-bt-parent=project_id:<Your Project ID>"
```

Important: The project ID is not the same as your project name. To find your project ID:

1. Navigate to your project configuration page at: `https://www.braintrust.dev/app/ORG_NAME/p/PROJECT_NAME/configuration`
2. Scroll to the bottom of the page
3. Look for the "Copy Project ID" button to get the correct ID for the `x-bt-parent` header

Traces will then appear under the Braintrust project or experiment provided in the `x-bt-parent` header.

```python theme={null}
from openai import OpenAI
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow
 
Traceloop.init(disable_batch=True)
client = OpenAI()
 
 
@workflow(name="story")
def run_story_stream(client):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Tell me a short story about LLM evals."}],
    )
    return completion.choices[0].message.content
 
 
print(run_story_stream(client))
```


# LLM Observability with Dash0 and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/dash0



<Frame>
  <img />
</Frame>

[Dash0](https://www.dash0.com) is an OpenTelemetry-natively observability solution. You can route your traces directly to Dash0's ingest APIs.

```bash theme={null}
TRACELOOP_BASE_URL="https://ingress.eu-west-1.aws.dash0.com"
TRACELOOP_HEADERS="Authorization=Bearer <YOUR_AUTH_TOKEN>"
```

For more information check out the [documentation](https://www.dash0.com/documentation/dash0/get-started/sending-data-to-dash0).


# LLM Observability with Datadog and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/datadog



With datadog, there are 2 options - you can either export directly to a Datadog Agent in your cluster, or through an OpenTelemetry Collector (which requires that you deploy one in your cluster).

See also [Datadog documentation](https://docs.datadoghq.com/opentelemetry/).

Exporting directly to an agent is easiest.
To do that, first enable the OTLP HTTP collector in your agent configuration.
This depends on how you deployed your Datadog agent. For example, if you've used a Helm chart,
you can add the following to your `values.yaml`
(see [this](https://docs.datadoghq.com/opentelemetry/otlp_ingest_in_the_agent/?tab=kuberneteshelmvaluesyaml#enabling-otlp-ingestion-on-the-datadog-agent) for other options):

```yaml theme={null}
otlp:
  receiver:
    protocols:
      http:
        enabled: true
```

Then, set this env var, and you're done!

```bash theme={null}
TRACELOOP_BASE_URL=http://<datadog-agent-hostname>:4318
```


# LLM Observability with Dynatrace and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/dynatrace



<Frame>
  <img />
</Frame>

Analyze all collected LLM traces and logs within Dynatrace by using the native OpenTelemetry ingest endpoint of your Dynatrace environment.

Go to your Dynatrace environment and create a new access token under **Manage Access Tokens**.\
The access token needs the following permission scopes that allow the ingest of OpenTelemetry spans, metrics and logs
(openTelemetryTrace.ingest, metrics.ingest, logs.ingest).

Set `TRACELOOP_BASE_URL` environment variable to the URL of your Dynatrace OpenTelemetry ingest endpoint

```bash theme={null}
TRACELOOP_BASE_URL=https://<YOUR_ENV>.live.dynatrace.com\api\v2\otlp
```

Set the `TRACELOOP_HEADERS` environment variable to include your previously created access token

```bash theme={null}
TRACELOOP_HEADERS=Authorization=Api-Token%20<YOUR_ACCESS_TOKEN>
```

Done! All exported spans, along with their span attributes, will appear within the [Dynatrace trace view](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.genai.observability).


# LLM Observability with Elasticsearch APM Service
Source: https://www.traceloop.com/docs/openllmetry/integrations/elasticsearch-apm



Connect OpenLLMetry to [Elastic APM](https://www.elastic.co/guide/en/apm/guide/current/index.html) to visualize LLM traces in Kibana's native APM interface. This integration uses OpenTelemetry Protocol (OTLP) to route traces from your application through an OpenTelemetry Collector to Elastic APM Server.

<Note>
  This integration requires an OpenTelemetry Collector to route traces between Traceloop OpenLLMetry client and Elastic APM Server.
  Elastic APM Server 8.x+ supports OTLP natively.
</Note>

## Quick Start

<Steps>
  <Step title="Install OpenLLMetry">
    Install the Traceloop SDK alongside your LLM provider client:

    ```bash theme={null}
    pip install traceloop-sdk openai
    ```
  </Step>

  <Step title="Configure OpenTelemetry Collector">
    Configure your OpenTelemetry Collector to receive traces from OpenLLMetry and forward them to APM Server.

    Create an `otel-collector-config.yaml` file:

    ```yaml theme={null}
    receivers:
      otlp:
        protocols:
          http:
            endpoint: localhost:4318
          grpc:
            endpoint: localhost:4317

    processors:
      batch:
        timeout: 10s
        send_batch_size: 1024

      memory_limiter:
        check_interval: 1s
        limit_mib: 512

      resource:
        attributes:
          - key: service.name
            action: upsert
            value: your-service-name # Match this to app_name parameter value when calling Traceloop.init()

    exporters:
      # Export to APM Server via OTLP
      otlp/apm:
        endpoint: http://localhost:8200 # APM Server Endpoint
        tls:
          insecure: true # Allow insecure connection from OTEL Collector to APM Server (for demo purposes)
        compression: gzip

      # Logging exporter for debugging (can ignore if not needed)
      logging:
        verbosity: normal # This is the verbosity of the logging
        sampling_initial: 5
        sampling_thereafter: 200

      # Debug exporter to verify trace data
      debug:
        verbosity: detailed
        sampling_initial: 10
        sampling_thereafter: 10

    extensions:
      health_check:
        endpoint: localhost:13133 # Endpoint of OpenTelemetry Collector's health check extension

    service:
      extensions: [health_check] # Enable health check extension

      pipelines:
        traces:
          receivers: [otlp]
          processors: [memory_limiter, batch, resource]
          exporters: [otlp/apm, logging, debug]

        metrics:
          receivers: [otlp]
          processors: [memory_limiter, batch, resource]
          exporters: [otlp/apm, logging]

        logs:
          receivers: [otlp]
          processors: [memory_limiter, batch, resource]
          exporters: [otlp/apm, logging]
    ```

    <Warning>
      In production, enable TLS and use APM Server secret tokens for authentication.
      Set `tls.insecure: false` and configure `headers: Authorization: Bearer <token>`.
    </Warning>
  </Step>

  <Step title="Initialize Traceloop">
    Import and initialize Traceloop before any LLM imports:

    ```python theme={null}
    from os import getenv

    from traceloop.sdk import Traceloop
    from openai import OpenAI

    # Initialize Traceloop with OTLP endpoint
    Traceloop.init(
        app_name="your-service-name",
        api_endpoint="http://localhost:4318"
    )

    # Traceloop must be initialized before importing the LLM client
    # Traceloop instruments the OpenAI client automatically
    client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

    # Make LLM calls - automatically traced
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    ```

    <Note>
      The `app_name` parameter sets the service name visible in Kibana APM's service list.
    </Note>
  </Step>

  <Step title="View Traces in Kibana">
    Navigate to Kibana's APM interface:

    1. Open Kibana at `http://localhost:5601`
    2. Go to **Observability → APM → Services**
    3. Click on your service name (e.g., `your-service-name`)
    4. View transactions and trace timelines with full LLM metadata

    Each LLM call appears as a span containing:

    * Model name (`gen_ai.request.model`)
    * Token usage (`gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`)
    * Prompts and completions (configurable)
    * Request duration and latency
  </Step>
</Steps>

## Environment Variables

Configure OpenLLMetry behavior using environment variables:

| Variable                  | Description                      | Default                 |
| ------------------------- | -------------------------------- | ----------------------- |
| `TRACELOOP_BASE_URL`      | OpenTelemetry Collector endpoint | `http://localhost:4318` |
| `TRACELOOP_TRACE_CONTENT` | Capture prompts/completions      | `true`                  |

<Warning>
  Set `TRACELOOP_TRACE_CONTENT=false` in production to prevent logging sensitive prompt content.
</Warning>

## Using Workflow Decorators

For complex applications with multiple steps, use workflow decorators to create hierarchical traces:

```python theme={null}
from os import getenv
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow, task
from openai import OpenAI

Traceloop.init(
  app_name="recipe-service",
  api_endpoint="http://localhost:4318",
)

# Traceloop must be initialized before importing the LLM client
# Traceloop instruments the OpenAI client automatically
client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

@task(name="generate_recipe")
def generate_recipe(dish: str):
    """LLM call - creates a child span"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a chef."},
            {"role": "user", "content": f"Recipe for {dish}"}
        ]
    )
    return response.choices[0].message.content


@workflow(name="recipe_workflow")
def create_recipe(dish: str, servings: int):
    """Parent workflow - creates the root transaction"""
    recipe = generate_recipe(dish)
    return {"recipe": recipe, "servings": servings}

# Call the workflow
result = create_recipe("pasta carbonara", 4)
```

In Kibana APM, you'll see:

* `recipe_workflow.workflow` as the parent transaction
* `generate_recipe.task` as a child span
* `openai.chat.completions` as the LLM API span with full metadata

## Example Trace Visualization

### Trace View

<Frame>
  <img />
</Frame>

### Trace Details

<Frame>
  <img />
</Frame>

## Captured Metadata

OpenLLMetry automatically captures these attributes in each LLM span:

**Request Attributes:**

* `gen_ai.request.model` - Model identifier
* `gen_ai.request.temperature` - Sampling temperature
* `gen_ai.system` - Provider name (OpenAI, Anthropic, etc.)

**Response Attributes:**

* `gen_ai.response.model` - Actual model used
* `gen_ai.response.id` - Unique response identifier
* `gen_ai.response.finish_reason` - Completion reason

**Token Usage:**

* `gen_ai.usage.input_tokens` - Input token count
* `gen_ai.usage.output_tokens` - Output token count
* `llm.usage.total_tokens` - Total tokens

**Content (if enabled):**

* `gen_ai.prompt.{N}.content` - Prompt messages
* `gen_ai.completion.{N}.content` - Generated completions

## Production Considerations

<Tabs>
  <Tab title="Content Logging">
    Disable prompt/completion logging in production:

    ```bash theme={null}
    export TRACELOOP_TRACE_CONTENT=false
    ```

    This prevents sensitive data from being stored in Elasticsearch.
  </Tab>

  <Tab title="Sampling">
    Configure sampling in the OpenTelemetry Collector to reduce trace volume:

    ```yaml theme={null}
    processors:
      probabilistic_sampler:
        sampling_percentage: 10  # Sample 10% of traces
    ```
  </Tab>

  <Tab title="Security">
    Enable APM Server authentication:

    ```yaml theme={null}
    exporters:
      otlp/apm:
        endpoint: https://localhost:8200
        headers:
          Authorization: "Bearer <secret-token>"
        tls:
          insecure: false
    ```
  </Tab>
</Tabs>

## Resources

* [Elastic APM Documentation](https://www.elastic.co/docs/solutions/observability/apm)
* [OpenTelemetry Collector Configuration](https://opentelemetry.io/docs/collector/configuration/)
* [Traceloop SDK Configuration](https://www.traceloop.com/docs/openllmetry/configuration)


# LLM Observability with Google Cloud and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/gcp



[Google Cloud](https://cloud.google.com/?hl=en), also known as Google Cloud Platform (GCP), is a cloud
provider including [over 150+ products and services](https://cloud.google.com/products?hl=en). Among
these products and services are [Cloud Trace](https://cloud.google.com/trace/docs),
[Cloud Monitoring](https://cloud.google.com/monitoring/docs), and [Cloud Logging](https://cloud.google.com/logging/docs)
which together comprise [Google Cloud Observability](https://cloud.google.com/stackdriver/docs).

Traceloop's OpenLLMetry library enables instrumenting LLM frameworks in an OTel-aligned manner and
supports writing that instrumentation data to Google Cloud, primarily as distributed traces in Cloud Trace.

## Integration Instructions

### Step 1. Install Python Dependencies

```bash theme={null}
pip install \
   opentelemetry-exporter-gcp-trace \
   opentelemetry-exporter-gcp-monitoring \
   opentelemetry-exporter-gcp-logging \
   traceloop-sdk
```

### Step 2. Initialize OpenLLMetry

In your application code, invoke `Traceloop.init` as shown:

```python theme={null}

# ...
from opentelemetry.exporter.cloud_logging import CloudLoggingExporter
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.exporter.cloud_monitoring import CloudMonitoringMetricsExporter
from traceloop.sdk import Traceloop

# ...
trace_exporter = CloudTraceSpanExporter()
metrics_exporter = CloudMonitoringMetricsExporter()
logs_exporter = CloudLoggingExporter()

Traceloop.init(
    app_name='your-app-name',
    exporter=trace_exporter,
    metrics_exporter=metrics_exporter,
    logging_exporter=logs_exporter)
```

## Advanced Topics

### Large Span Attributes

You can use the [`CloudTraceLoggingSpanExporter`](https://github.com/GoogleCloudPlatform/agent-starter-pack/blob/3dfb0c444aa70a3b0c62313c4cba14f9bc9d1723/src/base_template/app/utils/tracing.py)
from the [Google Cloud `agent-starter-pack`](https://github.com/GoogleCloudPlatform/agent-starter-pack) as a drop-in replacement for the
`CloudTraceSpanExporter`. That exporter writes large attributes to Google Cloud Storage and writes a reference URL to Cloud Observability.


# LLM Observability with Grafana and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/grafana



First, go to the Grafana Cloud account page under `https://grafana.com/orgs/<your org name>`,
and click on **Send Traces** under Tempo. In **Grafana Data Source settings**,
note the `URL` value. Click **Generate now** to generate an API key and copy it.
Note also the `Stack ID` value (you can find it in the URL `https://grafana.com/orgs/<Your Org Name>/stacks/<Stack ID>`).

## With Grafana Agent

Make sure you have an agent installed and running in your cluster.
The host to target your traces is constructed is the hostname of the `URL` noted above, without the `https://` and the trailing `/tempo`.

Add this to the configuration of your agent:

```yaml theme={null}
traces:
  configs:
    - name: default
      remote_write:
        - endpoint: <Grafana Hostname>:443
          basic_auth:
            username: <Stack ID from Grafana Cloud>
            password: <Grafana Cloud API Token>
      receivers:
        otlp:
          protocols:
            grpc:
```

<Warning>
  Note the endpoint. The URL you need to use is without `https` and the trailing
  `/`. So `https://tempo-us-central1.grafana.net/tempo` should be used as
  `tempo-us-central1.grafana.net:443`.
</Warning>

Set this as an environment variable in your app:

```bash theme={null}
TRACELOOP_BASE_URL=<grafana-agent-hostname>:4317
```

## Without Grafana Agent

Grafana cloud currently only supports sending traces to some of its regions.
Before you begin, [check out this list](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/otlp/send-data-otlp/)
and make sure your region is supported.

In a terminal, type:

```bash theme={null}
echo -n "<your stack id>:<your api key>" | base64
```

Note the result which is a base64 encoding of your user id and api key.

The URL you'll use as the destination for the traces depends on your region/zone. For example, for AWS US Central this will be `prod-us-central-0`.
See [here](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/otlp/send-data-otlp/#before-you-begin) for the names of the zones you should use below.

Then, you can set the following environment variables when running your app with Traceloop SDK installed:

```bash theme={null}
TRACELOOP_BASE_URL=https://otlp-gateway-<zone>.grafana.net/otlp
TRACELOOP_HEADERS="Authorization=Basic%20<base64 encoded stack id and api key>"
```


# LLM Observability with groundcover and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/groundcover



<Frame>
  <img />
</Frame>

[groundcover](https://www.groundcover.com) is a BYOC, eBPF-powered, OpenTelemetry-native complete observability platform.

You have two options for sending traces to groundcover:

## Option 1 - Send directly to the groundcover sensor

No API key required. Saves on networking costs.

```bash theme={null}
TRACELOOP_BASE_URL=http://groundcover-sensor.groundcover.svc.cluster.local:4318
```

## Option 2 - Send directly to the groundcover BYOC endpoint

Allows sending traces from any runtime, e.g., Docker, serverless, ECS, etc. Requires an ingestion key.

First, [create an ingestion key](https://docs.groundcover.com/use-groundcover/remote-access-and-apis/ingestion-keys#creating-an-ingestion-key).

Then, set the following environment variables:

```bash theme={null}
TRACELOOP_BASE_URL=https://<GROUNDCOVER_BYOC_ENDPOINT>
TRACELOOP_HEADERS="apikey=<GROUNDCOVER_INGESTION_KEY>"
```

For more information, check out the [groundcover OpenTelemetry documentation](https://docs.groundcover.com/integrations/data-sources/opentelemetry).


# LLM Observability with Highlight and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/highlight



<Frame>
  <img />
</Frame>

Since [Highlight](https://www.highlight.io) natively supports OpenTelemetry, you just need to route the traces to Highlights's OTLP endpoint and set the
highlight project id in the headers:

```bash theme={null}
TRACELOOP_BASE_URL=https://otel.highlight.io:4318
TRACELOOP_HEADERS="x-highlight-project=<YOUR_HIGHLIGHT_PROJECT_ID>"
```


# LLM Observability with Honeycomb and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/honeycomb



<Frame>
  <img />
</Frame>

Since Honeycomb natively supports OpenTelemetry, you just need to route the traces to Honeycomb's endpoint and set the
API key:

```bash theme={null}
TRACELOOP_BASE_URL=https://api.honeycomb.io
TRACELOOP_HEADERS="x-honeycomb-team=<YOUR_API_KEY>"
```


# LLM Observability with HyperDX and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/hyperdx



<Frame>
  <img />
</Frame>

HyperDX is an [open source observability platform](https://github.com/hyperdxio/hyperdx) that natively supports OpenTelemetry.
Just route the traces to HyperDX's endpoint and set the API key:

```bash theme={null}
TRACELOOP_BASE_URL=https://in-otel.hyperdx.io
TRACELOOP_HEADERS="authorization=<YOUR_INGESTION_API_KEY>"
```


# LLM Observability with Instana and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/instana



<Frame>
  <img />
</Frame>

With Instana, you can export directly to an Instana Agent in your cluster.

The Instana Agent will report back the tracing and metrics to the Instana Backend and display them on the Instana UI.

If you are running your Instana Agent on a VM or physical machine, do the following to config:

Edit the agent config file `configuration.yaml` under the `/opt/instana/agent/etc/instana` folder.

```
cd /opt/instana/agent/etc/instana
vi configuration.yaml
```

Add the following to the file:

```
com.instana.plugin.opentelemetry:
  enabled: true
  grpc:
    enabled: true
```

Restart the Instana agent:

```
systemctl restart instana-agent.service
```

If you are running Instana Agent on OpenShift or Kubernetes, do the following to config:

In Instana Configmap, add the following content:

```yaml theme={null}
com.instana.plugin.opentelemetry:
  enabled: true
  grpc:
    enabled: true
```

For Instana Daemonset, add the following:

```yaml theme={null}
- mountPath: /opt/instana/agent/etc/instana/configuration-opentelemetry.yaml
  name: configuration
  subPath: configuration-opentelemetry.yaml
```

The Instana agent should be ready for OpenTelemetry data at port 4317.

Then, set this env var, and you're done!

```bash theme={null}
TRACELOOP_BASE_URL=<instana-agent-hostname>:4317
```

Instana now supports MCP Observability. The following span attributes are available for MCP traces :
mcp.method.name
mcp.request.argument
mcp.request.id
mcp.response.value
mcp.session.init\_options

Here is the MCP traces from Instana UI:

<Frame>
  <img />
</Frame>


# Overview
Source: https://www.traceloop.com/docs/openllmetry/integrations/introduction

Connect to any observability platform - Traceloop, Dynatrace, Datadog, Honeycomb, and others

Since Traceloop SDK is using OpenTelemetry under the hood, you can see everything
in any observability platform that supports OpenTelemetry.

## The Integrations Catalog

<CardGroup>
  <Card title="Traceloop" href="/openllmetry/integrations/traceloop" />

  <Card title="Axiom" href="/openllmetry/integrations/axiom" />

  <Card title="Azure Application Insights" href="/openllmetry/integrations/azure" />

  <Card title="Braintrust" href="/openllmetry/integrations/braintrust" />

  <Card title="BMC" href="/openllmetry/integrations/bmc" />

  <Card title="Dash0" href="/openllmetry/integrations/dash0" />

  <Card title="Datadog" href="/openllmetry/integrations/datadog" />

  <Card title="Dynatrace" href="/openllmetry/integrations/dynatrace" />

  <Card title="Elasticsearch APM" href="/openllmetry/integrations/elasticsearch-apm" />

  <Card title="Google Cloud" href="/openllmetry/integrations/gcp" />

  <Card title="Grafana Tempo" href="/openllmetry/integrations/grafana" />

  <Card title="groundcover" href="/openllmetry/integrations/groundcover" />

  <Card title="Highlight" href="/openllmetry/integrations/highlight" />

  <Card title="Honeycomb" href="/openllmetry/integrations/honeycomb" />

  <Card title="HyperDX" href="/openllmetry/integrations/hyperdx" />

  <Card title="Instana" href="/openllmetry/integrations/instana" />

  <Card title="KloudMate" href="/openllmetry/integrations/kloudmate" />

  <Card title="Laminar" href="/openllmetry/integrations/laminar" />

  <Card title="Langfuse" href="/openllmetry/integrations/langfuse" />

  <Card title="LangSmith" href="/openllmetry/integrations/langsmith" />

  <Card title="Middleware" href="/openllmetry/integrations/middleware" />

  <Card title="New Relic" href="/openllmetry/integrations/newrelic" />

  <Card title="OpenTelemetry Collector" href="/openllmetry/integrations/otel-collector" />

  <Card title="Oracle Cloud" href="/openllmetry/integrations/oraclecloud" />

  <Card title="Scorecard" href="/openllmetry/integrations/scorecard" />

  <Card title="Service Now Cloud Observability" href="/openllmetry/integrations/service-now" />

  <Card title="Sentry" href="/openllmetry/integrations/sentry" />

  <Card title="SigNoz" href="/openllmetry/integrations/signoz" />

  <Card title="Splunk" href="/openllmetry/integrations/splunk" />

  <Card title="Tencent Cloud" href="/openllmetry/integrations/tencent" />
</CardGroup>


# LLM Observability with KloudMate and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/kloudmate



<Frame>
  <img />
</Frame>

KloudMate is an [observability platform](https://kloudmate.com/) that natively supports OpenTelemetry, you just need to route the traces to KloudMate OpenTelemetry Collector endpoint and set Authorization header:

```bash theme={null}
TRACELOOP_BASE_URL="https://otel.kloudmate.com:4318"
TRACELOOP_HEADERS="Authorization=<YOUR_KM_SECRET_KEY>"
```

For more information check out the [docs](https://docs.kloudmate.com/).


# LLM observability with Laminar and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/laminar



## Introduction to Laminar

Laminar is an [open-source platform](https://github.com/lmnr-ai/lmnr) for tracing and evaluating AI applications.

Laminar is fully compatible with OpenTelemetry, so you can use OpenLLMetry to trace your applications on Laminar.

Laminar's OpenTelemetry backend supports both gRPC and HTTP trace exporters.

The recommended setup is to use gRPC, as it's more efficient. You will need to create a gRPC exporter and pass it to the Traceloop SDK.

### (Recommended) gRPC setup

<Steps>
  <Step title="Install dependencies">
    ```bash theme={null}
    pip install traceloop-sdk openai
    ```
  </Step>

  <Step title="Set up environment variables">
    To get your API key, either sign up on [Laminar](https://lmnr.ai) and get it from the project settings,
    or spin up [Laminar](https://github.com/lmnr-ai/lmnr) locally.

    ```python theme={null}
    import os
    os.environ["LMNR_PROJECT_API_KEY"] = "<YOUR_LMNR_PROJECT_API_KEY>"
    os.environ["LMNR_BASE_URL"] = "https://api.lmnr.ai:8443"
    ```
  </Step>

  <Step title="Initialize the OpenTelemetry gRPC exporter">
    ```python theme={null}
    import os
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
        OTLPSpanExporter,
    )

    exporter = OTLPSpanExporter(
        endpoint=os.environ["LMNR_BASE_URL"],
        # IMPORTANT: note that "authorization" must be lowercase
        headers={
            "authorization": f"Bearer {os.environ['LMNR_PROJECT_API_KEY']}"
        }
    )
    ```
  </Step>

  <Step title="Initialize the Traceloop SDK">
    ```python theme={null}
    from traceloop.sdk import Traceloop
    Traceloop.init(exporter=exporter)
    ```
  </Step>

  <Step title="Run your application">
    ```python theme={null}
    from openai import OpenAI
    openai_client = OpenAI()

    chat_completion = openai_client.chat.completions.create(
        messages=[
            {
              "role": "user",
              "content": "What is Laminar flow?",
            }
        ],
        model="gpt-4.1-nano",
    )

    print(chat_completion)
    ```
  </Step>

  <Step title="Example trace in Laminar">
    Example trace in Laminar. ([Direct link](https://www.lmnr.ai/shared/traces/af09c6ee-ec63-1cce-674c-86bd43d62683))
  </Step>
</Steps>

### (Alternative) HTTP quick setup

Laminar's backend also supports accepting traces over HTTP, so for a minimal configuration change you can do:

```bash theme={null}
TRACELOOP_BASE_URL="https://api.lmnr.ai"
TRACELOOP_HEADERS="Authorization=<YOUR_LMNR_PROJECT_API_KEY>"
```

and skip step 3 (exporter setup) above.

For more information check out the [Laminar docs](https://docs.lmnr.ai/).


# Enhance LLM Observability with Langfuse and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/langfuse



# LLM Observability with Langfuse and OpenLLMetry

Langfuse provides a backend built on OpenTelemetry for ingesting trace data, and you can use different instrumentation libraries to export traces from your applications.

> **What is Langfuse?** [Langfuse](https://langfuse.com) [(GitHub)](https://github.com/langfuse/langfuse) is an open-source platform for LLM engineering. It provides tracing and monitoring capabilities for AI agents, helping developers debug, analyze, and optimize their products. Langfuse integrates with various tools and frameworks via native integrations, OpenTelemetry, and SDKs.

[![Langfuse Overview Video](https://github.com/user-attachments/assets/3926b288-ff61-4b95-8aa1-45d041c70866)](https://langfuse.com/watch-demo)

## Step 1: Install Dependencies

Begin by installing the necessary Python packages. In this example, we need the `openai` library to interact with OpenAI’s API and `traceloop-sdk` for enabling OpenLLMetry instrumentation.

```python theme={null}
%pip install openai traceloop-sdk
```

## Step 2: Set Up Environment Variables

Before initiating any requests, configure your environment with the necessary credentials and endpoints. Here, we establish Langfuse authentication by combining your public and secret keys into a Base64-encoded token. Additionally, specify the Langfuse endpoint based on your preferred geographical region (EU or US) and provide your OpenAI API key.

```python theme={null}
import os
import base64

LANGFUSE_PUBLIC_KEY=""
LANGFUSE_SECRET_KEY=""
LANGFUSE_AUTH=base64.b64encode(f"{LANGFUSE_PUBLIC_KEY}:{LANGFUSE_SECRET_KEY}".encode()).decode()

os.environ["TRACELOOP_BASE_URL"] = "https://cloud.langfuse.com/api/public/otel" # EU data region
# os.environ["TRACELOOP_BASE_URL"] = "https://us.cloud.langfuse.com/api/public/otel" # US data region
os.environ["TRACELOOP_HEADERS"] = f"Authorization=Basic {LANGFUSE_AUTH}"

# your openai key
os.environ["OPENAI_API_KEY"] = ""
```

## Step 3: Initialize OpenLLMetry Instrumentation

Proceed to initialize the OpenLLMetry instrumentation using the `traceloop-sdk`. It is advisable to use `disable_batch=True` if you are executing this code in a notebook, as traces are sent immediately without waiting for batching. Once initialized, any action performed using the OpenAI SDK (such as a chat completion request) will be automatically traced and forwarded to Langfuse.

```python theme={null}
from openai import OpenAI
from traceloop.sdk import Traceloop

Traceloop.init(disable_batch=True)

openai_client = OpenAI()

chat_completion = openai_client.chat.completions.create(
    messages=[
        {
          "role": "user",
          "content": "What is LLM Observability?",
        }
    ],
    model="gpt-4o-mini",
)

print(chat_completion)
```

## Step 4: Analyze the Trace in Langfuse

After executing the above code, you can examine the generated trace in your Langfuse dashboard:

[Example Trace in Langfuse](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/e417c49b4044725e48aa0e089534fa12?timestamp=2025-02-02T22%3A04%3A04.487Z)

![OpenLLMetry OpenAI Trace](https://langfuse.com/images/cookbook/otel-integration-openllmetry/openllmetry-openai-trace.png)


# LLM Observability with LangSmith and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/langsmith



<Frame>
  <img />
</Frame>

LangSmith is an [all-in-one developer platform](https://www.langchain.com/langsmith) for every step of the LLM-powered application lifecycle.

LangSmith supports ingesting traces using OpenTelemetry / OpenLLMetry format. For more details, see [LangSmith's OpenTelemetry documentation](https://docs.smith.langchain.com/observability/how_to_guides/tracing/trace_with_opentelemetry).

### To Log Traces to Langsmith

Signup for LangSmith and create an API Key. Then setup your environment variables:

```bash theme={null}
TRACELOOP_BASE_URL=https://api.smith.langchain.com/otel
TRACELOOP_HEADERS="x-api-key=<LANGSMITH_API_KEY>"
```

You can then log traces with OpenLLMetry to LangSmith, here is an example:

```python theme={null}
from openai import OpenAI
from traceloop.sdk import Traceloop

client = OpenAI()
Traceloop.init()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
```


# LLM Observability with Middleware and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/middleware



<Frame>
  <img />

  <img />
</Frame>

<Frame>
  <img />

  <img />
</Frame>

To send OpenTelemetry metrics and traces generated by Traceloop from your LLM Application to Middleware, Follow the below steps.

<Steps>
  <Step title="Get your Middleware credentials">
    <Steps>
      1. Sign in to your [Middleware](https://app.middleware.io/) account.
      2. Go to settings and click on API Key. [Link](https://app.middleware.io/settings/api-keys)
      3. Copy and Save the value for `MW_API_KEY` and `MW_TARGET`
    </Steps>
  </Step>

  <Step title="Add the following lines to your application code:">
    <Tabs>
      <Tab title="Python">
        ```python theme={null}
        from traceloop.sdk import Traceloop

        Traceloop.init(
            app_name="YOUR_APPLICATION_NAME",
            api_endpoint="<MW_TARGET>",
            headers={
                "Authorization": "<MW_API_KEY>",
                "X-Trace-Source": "traceloop",
            },
            resource_attributes={"key": "value"},
        )
        ```
      </Tab>

      <Tab title="Typescript (Node js)">
        ```javascript theme={null}
        import * as traceloop from "@traceloop/node-server-sdk";
        traceloop.initialize({
          appName: "YOUR_APPLICATION_NAME",
          apiEndpoint: "<MW_TARGET>",
          headers: {
            Authorization: "<MW_API_KEY>",
            "X-Trace-Source": "traceloop",
          },
          resourceAttributes: { "key": "value" },
        });
        ```
      </Tab>
    </Tabs>

    Replace:

    1. `MW_TARGET` with your middleware target url

    * Example - `https://abcde.middleware.io`

    2. `MW_API_KEY` with your middleware api key.

    * Example - nxhqwpbvcmlkjhgfdsazxcvbnmkjhgtyui

    Refer to the Traceloop [Docs](https://www.traceloop.com/docs/introduction) for more advanced configurations and use cases.

    For detailed information on LLM Observability with Middleware and Traceloop, consult Middleware Documentation:
    [LLM Observability Documentation](https://docs.middleware.io/llm-observability/overview).
  </Step>

  <Step title="Visualize in Middleware">
    Once your LLM application is instrumented, you can view the traces, metrics and dashboards in the Middleware LLM Observability section. To access this:

    1. Log in to your Middleware account
    2. Navigate to the [LLM Observability Section](https://app.middleware.io/llm) in the sidebar
  </Step>
</Steps>

***


# LLM observability with New Relic and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/newrelic



<Frame>
  <img />
</Frame>

Since New Relic natively supports OpenTelemetry, you just need to route the traces to New Relic's endpoint and set the API key:

```bash theme={null}
TRACELOOP_BASE_URL=https://otlp.nr-data.net:443
TRACELOOP_HEADERS="api-key=<YOUR_NEWRELIC_LICENSE_KEY>"
```

For more information check out the [docs link](https://docs.newrelic.com/docs/more-integrations/open-source-telemetry-integrations/opentelemetry/get-started/opentelemetry-set-up-your-app/#review-settings).


# LLM Observability with Oracle Cloud Infrastructure Application Performance Monitoring(APM) service
Source: https://www.traceloop.com/docs/openllmetry/integrations/oraclecloud



<Frame>
  <img />
</Frame>

[Oracle Cloud Infrastructure Application Performance Monitoring(APM) service](https://docs.oracle.com/en-us/iaas/application-performance-monitoring/home.htm) natively supports and can ingest OpenTelemetry (OTLP) spans and metrics. Traceloop's OpenLLMetry library enables instrumenting LLM frameworks and applications in Open Telemetry format and can be routed to OCI Application Performance Monitoring for observability and evaluation of LLM applications.

## Initialize and export directly from application code

```python theme={null}
APM_BASE_URL=“<OCI APM dataUploadEndpoint>/20200101/opentelemetry/private"
APM_DATA_KEY="dataKey <OCI APM Private Data Key>"
APM_SERVICE_NAME=“My LLM Service”
 
Traceloop.init(
    disable_batch=True,
    app_name=APM_SERVICE_NAME,
    api_endpoint=APM_BASE_URL,
    headers={
      "Authorization": APM_DATA_KEY
      }
)
```

## Initialize using environment variables

```bash theme={null}
export TRACELOOP_BASE_URL=<OCI APM dataUploadEndpoint>/20200101/opentelemetry/private
export TRACELOOP_HEADERS="Authorization=dataKey <OCI APM Private Data Key>"
```

## Using an OpenTelemetry Collector

If you are using an OpenTelemetry Collector, you can route metrics and traces to OCI APM by simply adding an OTLP exporter to your collector configuration.

```yaml theme={null}
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
processors:
  batch:
exporters:
  otlphttp/apm:
    endpoint: "<OCI APM dataUploadEndpoint>/20200101/opentelemetry/private" 
    headers:
      "Authorization": "dataKey <OCI APM Private Data Key>"
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/apm]
```

For more information check out the [docs link](https://docs.oracle.com/en-us/iaas/application-performance-monitoring/doc/configure-open-source-tracing-systems.html#GUID-4D941163-F357-4839-8B06-688876D4C61F).


# LLM observability with OpenTelemetry Collector
Source: https://www.traceloop.com/docs/openllmetry/integrations/otel-collector



Since Traceloop is emitting standard OTLP HTTP (standard OpenTelemetry protocol), you can use any OpenTelemetry Collector, which gives you the flexibility
to then connect to any backend you want.
First, [deploy an OpenTelemetry Collector](https://opentelemetry.io/docs/kubernetes/operator/automatic/#create-an-opentelemetry-collector-optional)
in your cluster.
Then, point the output of the Traceloop SDK to the collector by setting:

```bash theme={null}
TRACELOOP_BASE_URL=https://<opentelemetry-collector-hostname>:4318
```

You can connect your collector to Traceloop by following the instructions in the [Traceloop integration section](/openllmetry/integrations/traceloop#using-an-opentelemetry-collector).


# LLM Observability with Scorecard and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/scorecard



Scorecard is an [AI evaluation and optimization platform](https://www.scorecard.io/) that helps teams build reliable AI systems with comprehensive testing, evaluation, and continuous monitoring capabilities.

## Setup

To integrate OpenLLMetry with Scorecard, you'll need to configure your tracing endpoint and authentication:

### 1. Get your Scorecard API Key

1. Visit your [Settings Page](https://app.scorecard.io/settings)
2. Copy your API Key

### 2. Configure Environment Variables

```bash theme={null}
TRACELOOP_BASE_URL="https://tracing.scorecard.io/otel"
TRACELOOP_HEADERS="Authorization=Bearer <YOUR_SCORECARD_API_KEY>"
```

### 3. Instrument your code

First, install OpenLLMetry and your LLM library:

<CodeGroup>
  ```sh Python theme={null}
  pip install traceloop-sdk openai
  ```

  ```sh JavaScript theme={null}
  npm install @traceloop/node-server-sdk openai
  ```
</CodeGroup>

Then initialize OpenLLMetry and structure your application using workflows and tasks:

<CodeGroup>
  ```py Python theme={null}
  from traceloop.sdk import Traceloop
  from traceloop.sdk.decorators import workflow, task
  from traceloop.sdk.instruments import Instruments
  from openai import OpenAI

  # Initialize OpenAI client
  openai_client = OpenAI()

  # Initialize OpenLLMetry (reads config from environment variables)
  Traceloop.init(disable_batch=True, instruments={Instruments.OPENAI})

  @workflow(name="simple_chat")
  def simple_workflow():
      completion = openai_client.chat.completions.create(
          model="gpt-4o-mini",
          messages=[{"role": "user", "content": "Tell me a joke"}]
      )
      return completion.choices[0].message.content

  # Run the workflow - all LLM calls will be automatically traced
  simple_workflow()
  print("Check Scorecard for traces!")
  ```

  ```js JavaScript theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";
  import OpenAI from "openai";

  // Initialize OpenAI client
  const openai = new OpenAI();

  // Initialize OpenLLMetry with automatic instrumentation
  traceloop.initialize({ 
      disableBatch: true,  // Ensures immediate trace sending
      instrumentModules: { openAI: OpenAI },
  });

  async function simpleWorkflow() {
  return await traceloop.withWorkflow({ name: "simple_chat" }, async () => {
      const completion = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: "Tell me a joke" }],
      });
      return completion.choices[0].message.content;
  });
  }

  # Run the workflow - all LLM calls will be automatically traced
  simpleWorkflow();
  console.log("Check Scorecard for traces!");
  ```
</CodeGroup>

## Features

Once configured, you'll have access to Scorecard's comprehensive observability features:

* **Automatic LLM instrumentation** for popular libraries (OpenAI, Anthropic, etc.)
* **Structured tracing** with workflows and tasks using `@workflow` and `@task` decorators
* **Performance monitoring** including latency, token usage, and cost tracking
* **Real-time evaluation** with continuous monitoring of AI system performance
* **Production debugging** with detailed trace analysis

For more detailed setup instructions and examples, check out the [Scorecard Tracing Quickstart](https://docs.scorecard.io/intro/tracing-quickstart).


# LLM Observability with Sentry and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/sentry



Install Sentry SDK with OpenTelemetry support:

<CodeGroup>
  ```bash Python theme={null}
  pip install --upgrade 'sentry-sdk[opentelemetry]'
  ```

  ```bash Typescript (Node.js) theme={null}
  npm install @sentry/node @sentry/opentelemetry-node
  ```
</CodeGroup>

Initialize Sentry and enable OpenTelemetry instrumentation:

<CodeGroup>
  ```python Python theme={null}
  import sentry_sdk

  sentry_sdk.init(
  dsn=<Your DSN>,
  enable_tracing=True,

      # set the instrumenter to use OpenTelemetry instead of Sentry
      instrumenter="otel",

  )

  ```

  ```javascript Typescript (Node.js) theme={null}
  Sentry.init({
    dsn: <Your DSN>,
    tracesSampleRate: 1.0,
    skipOpenTelemetrySetup: true,
  });
  ```
</CodeGroup>

Then, when initializing the Traceloop SDK, make sure to override the processor and propagator:

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk import Traceloop
  from sentry_sdk.integrations.opentelemetry import SentrySpanProcessor, SentryPropagator

  Traceloop.init(processor=SentrySpanProcessor(), propagator=SentryPropagator())

  ```

  ```javascript Typescript (Node.js) theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";
  import { SentrySpanProcessor, SentryPropagator, SentrySampler } from "@sentry/opentelemetry";

  traceloop.initialize({
    contextManager: new Sentry.SentryContextManager(),
    processor: new SentrySpanProcessor(),
    propagator: new SentryPropagator()
  })
  ```
</CodeGroup>


# LLM Observability with Service Now Cloud Observability and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/service-now



<Frame>
  <img />
</Frame>

Since Service Now Cloud Observability natively supports OpenTelemetry, you just need to route the traces to Service Now Cloud Observability's endpoint and set the
access token:

```bash theme={null}
TRACELOOP_BASE_URL=https://ingest.lightstep.com
TRACELOOP_HEADERS="lightstep-access-token=<YOUR_ACCESS_TOKEN>"
```


# LLM Observability with SigNoz and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/signoz



<Frame>
  <img />
</Frame>

SigNoz is an [open-source observability platform](https://github.com/signoz/signoz).

### With SigNoz cloud

Since SigNoz natively supports OpenTelemetry, you just need to route the traces to SigNoz's endpoint and set the
ingestion key (note no `https` in the URL):

```bash theme={null}
TRACELOOP_BASE_URL=ingest.{region}.signoz.cloud
TRACELOOP_HEADERS="signoz-access-token=<SIGNOZ_INGESTION_KEY>"
```

Where `region` depends on the choice of your SigNoz cloud region:

| Region | Endpoint                   |
| ------ | -------------------------- |
| US     | ingest.us.signoz.cloud:443 |
| IN     | ingest.in.signoz.cloud:443 |
| EU     | ingest.eu.signoz.cloud:443 |

Validate your configuration by [following these instructions](https://signoz.io/docs/instrumentation/python/#validating-instrumentation-by-checking-for-traces)

### With Self-Hosted version

Once you have an up and running instance of SigNoz, use the following environment variables to export your traces:

```bash theme={null}
TRACELOOP_BASE_URL="http://localhost:4318"
```


# LLM Observability with Splunk and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/splunk



<Frame>
  <img />
</Frame>

Collecting and analyzing LLM traces in [Splunk Observability Cloud](https://www.splunk.com/en_us/products/observability.html) can be achieved by configuring the **TRACELOOP\_BASE\_URL** environment variable to point to the [Splunk OpenTelemetry Collector](https://github.com/signalfx/splunk-otel-collector/releases) OTLP endpoint.

Have the Collector run in agent or gateway mode and ensure the OTLP receiver is configured, see [Get data into Splunk Observability Cloud](https://docs.splunk.com/observability/en/gdi/get-data-in/get-data-in.html).

```yaml theme={null}
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"
```

Secondly, ensure the OTLP exporter is configured to send to Splunk Observability Cloud:

```yaml theme={null}
exporters:
  # Traces
  sapm:
    access_token: "${SPLUNK_ACCESS_TOKEN}"
    endpoint: "https://ingest.${SPLUNK_REALM}.signalfx.com/v2/trace"
    sending_queue:
      num_consumers: 32
```

Thirdly, make sure `otlp` is defined in the traces pipeline:

```yaml theme={null}
  pipelines:
    traces:
      receivers: [jaeger, otlp, sapm, zipkin]
      processors:
      - memory_limiter
      - batch
      #- resource/add_environment
      exporters: [sapm]
```

Finally, define the `TRACELOOP_BASE_URL` environment variable to point to the Splunk OpenTelemetry Collector OTLP endpoint:

```bash theme={null}
TRACELOOP_BASE_URL=http://<splunk-otel-collector>:4318
```


# LLM Observability with Tencent APM and OpenLLMetry
Source: https://www.traceloop.com/docs/openllmetry/integrations/tencent



[Tencent APM](https://console.tencentcloud.com/apm), also known as `TAPM`, is a monitoring and observability platform that provides a comprehensive view of your application's performance and behavior.

Tencent APM natively supports OpenTelemetry, so you can use OpenLLMetry to trace your applications.

<Frame>
  <img />
</Frame>

To integrate OpenLLMetry with Tencent APM, you'll need to configure your tracing endpoint and authentication:

```bash theme={null}
TRACELOOP_BASE_URL="<TAPM_ENDPOINT>" # Use port `55681` rather than `4317` as the default port.
TRACELOOP_HEADERS="Authorization=Bearer%20<TAPM_TOKEN>" # header values in env variables must be URL‑encoded.
```

Tencent APM defaults to using port `4317` for the gRPC exporter, and we recommend using port `55681` instead here, which is the HTTP exporter port.


# LLM Observability with Traceloop
Source: https://www.traceloop.com/docs/openllmetry/integrations/traceloop



<Frame>
  <img />

  <img />
</Frame>

[Traceloop](https://app.traceloop.com) is a platform for observability and evaluation of LLM outputs.
It allows you to deploy changes to prompts and model configurations with confidence, without breaking existing functionality.

## Connecting OpenLLMetry to Traceloop directly

<Note>
  You need an API key to send traces to Traceloop. API keys are scoped to a specific **project** and **environment**.

  **To generate an API key:**

  1. Go to [Settings → Organization](https://app.traceloop.com/settings/api-keys)
  2. Click on your project (or create a new one)
  3. Select an environment (Development, Staging, Production, or custom)
  4. Click **Generate API key**
  5. **Copy the key immediately** - it won't be shown again after you close or reload the page

  [Detailed instructions →](/settings/managing-api-keys)
</Note>

Set the API key as an environment variable named `TRACELOOP_API_KEY`:

```bash theme={null}
export TRACELOOP_API_KEY=your_api_key_here
```

Done! You'll get instant visibility into everything that's happening with your LLM.
If you're calling a vector DB, or any other external service or database, you'll also see it in the Traceloop dashboard.

<Tip>
  **Want to organize your data?** Learn about [Projects and Environments](/settings/projects-and-environments)
  to separate traces for different applications and deployment stages.
</Tip>

## Using an OpenTelemetry Collector

If you are using an [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), you can route metrics and traces to Traceloop by simply adding an OTLP exporter to your collector configuration.

```yaml theme={null}
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
processors:
  batch:
exporters:
  otlphttp/traceloop:
    endpoint: "https://api.traceloop.com" # US instance
    headers:
      "Authorization": "Bearer <YOUR_API_KEY>"
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/traceloop]
```

You can route OpenLLMetry to your collector by following the [OpenTelemetry Collector](/openllmetry/integrations/otel-collector) integration instructions.


# What is OpenLLMetry?
Source: https://www.traceloop.com/docs/openllmetry/introduction



<Frame>
  <img />

  <img />
</Frame>

OpenLLMetry is an open source project that allows you to easily start monitoring and debugging the execution of your LLM app.
Tracing is done in a non-intrusive way, built on top of OpenTelemetry.
You can choose to export the traces to Traceloop, or to your existing observability stack.

<Tip>
  You can use OpenLLMetry whether you use a [supported LLM framework](/openllmetry/tracing/supported#frameworks), or
  directly interact with a foundation model API.
</Tip>

<CodeGroup>
  ```python Python theme={null}
  import os

  from openai import OpenAI
  from traceloop.sdk import Traceloop
  from traceloop.sdk.decorators import workflow

  Traceloop.init(app_name="joke_generation_service")

  @workflow(name="joke_creation")
  def create_joke():
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Tell me a joke about opentelemetry"}],
    )

    return completion.choices[0].message.content
  ```

  ```js Typescript theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";
  import OpenAI from "openai";

  traceloop.initialize({ appName: "joke_generation_service" })
  const openai = new OpenAI();

  class MyLLM {
    @traceloop.workflow("joke_creation")
    async create_joke() {
        completion = await openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [{"role": "user", "content": "Tell me a joke about opentelemetry"}],
        })

        return completion.choices[0].message.content
  }
  ```
</CodeGroup>

## Getting Started

Select from the following guides to learn more about how to use OpenLLMetry:

<CardGroup>
  <Card title="Start with Python" icon="python" href="/openllmetry/getting-started-python">
    Set up Traceloop Python SDK in your project
  </Card>

  <Card title="Start with Javascript / Typescript" icon="node" href="/openllmetry/getting-started-ts">
    Set up Traceloop Javascript SDK in your project
  </Card>

  <Card title="Start with Go" icon="golang" href="/openllmetry/getting-started-go">
    Set up Traceloop Go SDK in your project
  </Card>

  <Card title="Workflows, Tasks, Agents and Tools" icon="code" href="/openllmetry/tracing/annotations">
    Learn how to annotate your code to enrich your traces
  </Card>

  <Card title="Integrations" icon="bars-staggered" href="/openllmetry/integrations/introduction">
    Learn how to connect to your existing observability stack
  </Card>

  <Card title="Privacy" icon="shield" href="/openllmetry/privacy/traces">
    How we secure your data
  </Card>
</CardGroup>


# Telemetry
Source: https://www.traceloop.com/docs/openllmetry/privacy/telemetry



As of OpenLLMetry v0.49.2 and above or OpenLLMetry-js v0.21.1,
We no longer log or collect any telemetry or any other information in any of the packages (including Traceloop SDK).


# Prompts, Completions and Embeddings
Source: https://www.traceloop.com/docs/openllmetry/privacy/traces



**By default, OpenLLMetry logs prompts, completions, and embeddings to span attributes.**
This gives you a clear visibility into how your LLM application is working, and can make it easy to debug and evaluate the quality of the outputs.

However, you may want to disable this logging for privacy reasons, as they may contain highly sensitive data from your users.
You may also simply want to reduce the size of your traces.

## Disabling logging globally

To disable logging, set the `TRACELOOP_TRACE_CONTENT` environment variable to `false`.
On Typescript/Javascript you can also pass the `traceContent` option.

<CodeGroup>
  ```bash Environment Variable theme={null}
  TRACELOOP_TRACE_CONTENT=false
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.initialize({ traceContent: false });
  ```
</CodeGroup>

OpenLLMetry SDK, as well as all individual instrumentations will respect this setting.

## Enabling logging selectively in specific workflows / tasks

You can decide to selectively enable prompt logging for specific workflows, tasks, agents, or tools, using the annotations API.
If you don't specify a `traceContent` option, the global setting will be used.

<CodeGroup>
  ```js Typescript / Javascript theme={null}
  return await traceloop.withWorkflow(
      { name: "workflow_name", traceContent: false },
      async () => {
          ...
      }
    );
  ```

  ```js Typescript - with Decorators theme={null}
  class MyClass {
    @traceloop.workflow({ traceContent: false })
    async some_workflow() {
      ...
    }
  }
  ```
</CodeGroup>

## Enabling logging selectively for specific users

You can decide to selectively enable or disable prompt logging for specific users or workflows.

### Using the Traceloop Platform

We have an API to enable content tracing for specific users, as defined by [association entities](/openllmetry/tracing/association).
See the [Traceloop API documentation](/api-reference/tracing/whitelist_user) for more information.

### Without the Traceloop Platform

Set a key called `override_enable_content_tracing` in the OpenTelemetry context to `True` right before making the LLM call
you want to trace with prompts.
This will create a new context that will instruct instrumentations to log prompts and completions as span attributes.

```python Python theme={null}
from opentelemetry.context import attach, set_value

attach(set_value("override_enable_content_tracing", True))
```

Make sure to also disable it afterwards:

```python Python theme={null}
from opentelemetry.context import attach, set_value

attach(set_value("override_enable_content_tracing", False))
```


# Workflow Annotations
Source: https://www.traceloop.com/docs/openllmetry/tracing/annotations

Enrich your traces by annotating chains and workflows in your app

<Frame>
  <img />

  <img />
</Frame>

Traceloop SDK supports several ways to annotate workflows, tasks, agents and tools in your code to get a more complete picture of your app structure.

<Tip>
  If you're using a [supported LLM framework](/openllmetry/tracing/supported#frameworks) - no need
  to do anything! OpenLLMetry will automatically detect the framework and
  annotate your traces.
</Tip>

## Workflows and Tasks

Sometimes called a "chain", intended for a multi-step process that can be traced as a single unit.

<Tabs>
  <Tab title="Python">
    Use it as `@workflow(name="my_workflow")` or `@task(name="my_task")`.

    <Tip>
      The `name` argument is optional. If you don't provide it, we will use the
      function name as the workflow or task name.
    </Tip>

    <Tip>
      You can version your workflows and tasks. Just provide the `version` argument
      to the decorator: `@workflow(name="my_workflow", version=2)`
    </Tip>

    ```python theme={null}
    from openai import OpenAI
    from traceloop.sdk.decorators import workflow, task

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    @task(name="joke_creation")
    def create_joke():
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Tell me a joke about opentelemetry"}],
        )

        return completion.choices[0].message.content

    @task(name="signature_generation")
    def generate_signature(joke: str):
        completion = openai.Completion.create(
            model="davinci-002",[]
            prompt="add a signature to the joke:\n\n" + joke,
        )

        return completion.choices[0].text


    @workflow(name="pirate_joke_generator")
    def joke_workflow():
        eng_joke = create_joke()
        pirate_joke = translate_joke_to_pirate(eng_joke)
        signature = generate_signature(pirate_joke)
        print(pirate_joke + "\n\n" + signature)
    ```
  </Tab>

  <Tab title="Typescript">
    <Note>
      This feature is only available in Typescript. Unless you're on Nest.js, you'll need to update your `tsconfig.json` to enable decorators.
    </Note>

    Update `tsconfig.json` to enable decorators:

    ```json theme={null}
    {
      "compilerOptions": {
        "experimentalDecorators": true
      }
    }
    ```

    Use it in your code `@traceloop.workflow({ name: "my_workflow" })`.
    You can provide the parameters to the decorator directly or by providing a function that resolves to the parameters.
    The function will be called with the `this` parameter and the arguments of the decorated function
    (see [example](https://github.com/traceloop/openllmetry-js/blob/2178f1c5161218ffc7938bfe17fc1ced8190357c/packages/sample-app/src/sample_decorators.ts#L26)).

    <Tip>
      The name is optional. If you don't provide it, we will use the function
      qualified name as the workflow or task name.
    </Tip>

    ```js theme={null}
    import * as traceloop from "@traceloop/node-server-sdk";

    class JokeCreation {
      @traceloop.task({ name: "joke_creation" })
      async create_joke() {
        completion = await openai.chat.completions({
          model: "gpt-3.5-turbo",
          messages: [
            { role: "user", content: "Tell me a joke about opentelemetry" },
          ],
        });

        return completion.choices[0].message.content;
      }

      @traceloop.task({ name: "signature_generation" })
      async generate_signature(joke: string) {
        completion = await openai.completions.create({
          model: "davinci-002",
          prompt: "add a signature to the joke:\n\n" + joke,
        });

        return completion.choices[0].text;
      }

      @traceloop.workflow({ name: "pirate_joke_generator" })
      async joke_workflow() {
        eng_joke = create_joke();
        pirate_joke = await translate_joke_to_pirate(eng_joke);
        signature = await generate_signature(pirate_joke);
        console.log(pirate_joke + "\n\n" + signature);
      }
    }
    ```
  </Tab>

  <Tab title="Javascript - without Decorators">
    Use it as `withWorkflow("my_workflow", {}, () => ...)` or `withTask(name="my_task", () => ...)`.
    The function passed to `withWorkflow` or `withTask` witll be part of the workflow or task and can be async or sync.

    ```js theme={null}
    import * as traceloop from "@traceloop/node-server-sdk";

    async function create_joke() {
      return await traceloop.withTask({ name: "joke_creation" }, async () => {
        completion = await openai.chat.completions({
          model: "gpt-3.5-turbo",
          messages: [
            { role: "user", content: "Tell me a joke about opentelemetry" },
          ],
        });

        return completion.choices[0].message.content;
      });
    }

    async function generate_signature(joke: string) {
      return await traceloop.withTask(
        { name: "signature_generation" },
        async () => {
          completion = await openai.completions.create({
            model: "davinci-002",
            prompt: "add a signature to the joke:\n\n" + joke,
          });

          return completion.choices[0].text;
        }
      );
    }

    async function joke_workflow() {
      return await traceloop.withWorkflow(
        { name: "pirate_joke_generator" },
        async () => {
          eng_joke = create_joke();
          pirate_joke = await translate_joke_to_pirate(eng_joke);
          signature = await generate_signature(pirate_joke);
          console.log(pirate_joke + "\n\n" + signature);
        }
      );
    }
    ```
  </Tab>
</Tabs>

## Agents and Tools

<Tabs>
  <Tab title="Python">
    Similarily, if you use autonomous agents, you can use the `@agent` decorator to trace them as a single unit.
    Each tool should be marked with `@tool`.

    ```python theme={null}
    from openai import OpenAI
    from traceloop.sdk.decorators import agent, tool

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    @agent(name="joke_translation")
    def translate_joke_to_pirate(joke: str):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Translate the below joke to pirate-like english:\n\n{joke}"}],
        )

        history_jokes_tool()

        return completion.choices[0].message.content


    @tool(name="history_jokes")
    def history_jokes_tool():
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"get some history jokes"}],
        )

        return completion.choices[0].message.content
    ```
  </Tab>

  <Tab title="Typescript">
    Similarily, if you use autonomous agents, you can use the `@agent` decorator to trace them as a single unit.
    Each tool should be marked with `@tool`.

    <Note>
      If you're not on Nest.js, remember to set `experimentalDecorators` to `true` in your `tsconfig.json`.
    </Note>

    ```js theme={null}
    import * as traceloop from "@traceloop/node-server-sdk";

    class Agent {
    @traceloop.agent({ name: "joke_translation" })
    async translate_joke_to_pirate(joke: str) {
    completion = await openai.chat.completions.create({
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Translate the below joke to pirate-like english:\n\n{joke}"}],
    });

        history_jokes_tool();

        return completion.choices[0].message.content;

    }

    @traceloop.tool({ name: "history_jokes" })
    async history_jokes_tool() {
    completion = await openai.chat.completions.create({
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"get some history jokes"}],
    });

        return completion.choices[0].message.content;

    }

    ```
  </Tab>

  <Tab title="Javascript - without Decorators">
    Similarily, if you use autonomous agents, you can use the `withAgent` to trace them as a single unit.
    Each tool should be in `withTool`.

    ```js theme={null}
    import * as traceloop from "@traceloop/node-server-sdk";

    async function translate_joke_to_pirate(joke: str) {
      return await withAgent({name: "joke_translation" }, () => {
        completion = await openai.chat.completions.create({
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": f"Translate the below joke to pirate-like english:\n\n{joke}"}],
        });

        history_jokes_tool();

        return completion.choices[0].message.content;
      }
    }

    async function history_jokes_tool() {
      return await withTool({ name: "history_jokes" }, () => {
        completion = await openai.chat.completions.create({
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"get some history jokes"}],
        });

        return completion.choices[0].message.content;
      }
    }
    ```
  </Tab>
</Tabs>

## Async methods

In Typescript, you can use the same syntax for async methods.

In python, the decorators work seamlessly with both synchronous and asynchronous functions.
Use `@workflow`, `@task`, `@agent`, and so forth for both sync and async methods.

The async-specific decorators (`@aworkflow`, `@atask`, etc.) are deprecated and will be removed in a future version.

See also a [separate section on using threads in Python with OpenLLMetry](/openllmetry/tracing/python-threads).

## Decorating Classes (Python only)

While the examples above shows how to decorate functions, you can also decorate classes.
In this case, you will also need to provide the name of the method that runs the workflow, task, agent or tool.

```python Python theme={null}
from openai import OpenAI
from traceloop.sdk.decorators import agent

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@agent(name="base_joke_generator", method_name="generate_joke")
class JokeAgent:
    def generate_joke(self):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Tell me a joke about Traceloop"}],
        )

        return completion.choices[0].message.content
```

```
```


# Associating Entities with Traces
Source: https://www.traceloop.com/docs/openllmetry/tracing/association

How to associate traces with entities in your own application

Each trace you run is usually connected to entities in your own application -
things like `user_id`, `chat_id`, or anything else that is tied to the flow that triggered the trace.

OpenLLMetry allows you to easily mark traces with these IDs so you can track them in the UI.

<Tip>
  You can use any key-value pair to associate a trace with an entity - it can
  also be `org_id`, `team_id`, whatever you want. The only requirement is that
  the key and the value are strings.
</Tip>

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk import Traceloop
   
  Traceloop.set_association_properties({ "user_id": "user12345", "chat_id": "chat12345" })
  ```

  ```js Typescript theme={null}
  // Option 1 (for class methods only) - set association properties within a workflow, task, agent or tool
  class MyClass {
    @traceloop.workflow({ associationProperties: { userId: "user123" })
    myMethod() {
      // Your code here
    }
  }

  // Option 2 - set association properties within a workflow, task, agent or tool
  traceloop.withWorkflow(
    {
      name: "workflow_name",
      associationProperties: { userId: "user12345", chatId: "chat12345" },
    },
    () => {
      // Your code here
      // (function can be made async if needed)
    }
  );

  // Option 3  - set association properties directly
  traceloop.withAssociationProperties(
    {
      userId: "user12345",
      chatId: "chat12345",
    },
    () => {
      // Your code here
      // (can be async or sync)
    }
  );
  ```
</CodeGroup>


# Issues with Auto-instrumentation (Typescript / Javascript)
Source: https://www.traceloop.com/docs/openllmetry/tracing/js-force-instrumentations

How to overcome issues with automatic instrumentations on Next.js and some Webpack environments.

Some customers have reported issues with automatic instrumentations on some environments.
This means that even though the SDK was installed and configured properly, you might not be seeing any traces.

Specifically, we have seen issues with Next.js and some configurations of Webpack.
In order to resolve it, you can provide the SDK with the libraries that you use (like OpenAI, LlamaIndex, Langchain, etc.) to make sure they are instrumented properly.

<Tip>
  You won't need this on most environments. We recommend trying without it
  first.
</Tip>

Here is an example of how to do it:

```js theme={null}
import OpenAI from "openai";

import * as LlamaIndex from "llamaindex";

import * as ChainsModule from "langchain/chains";
import * as AgentsModule from "langchain/agents";
import * as ToolsModule from "langchain/tools";

traceloop.initialize({
  appName: "app",
  instrumentModules: {
    openAI: OpenAI,
    llamaIndex: LlamaIndex,
    langchain: {
        chains: ChainsModule,
        agents: AgentsModule,
        tools: ToolsModule,
    }
    // Add or omit other modules you'd like to instrument
  },
```

You only need to do it once, on app initialization.


# Manually reporting calls to LLMs and Vector DBs
Source: https://www.traceloop.com/docs/openllmetry/tracing/manual-reporting

What should I do if my favorite vector DB or LLM is not supported by OpenLLMetry?

The best thing about OpenLLMetry is that it supports a wide range of LLMs and vector DBs out of the box.
You just install the SDK and get metrics, traces and logs - without any extra work.

Checkout the list of supported systems on [Python](https://github.com/traceloop/openllmetry?tab=readme-ov-file#-what-do-we-instrument)
and on [Typescript](https://github.com/traceloop/openllmetry-js?tab=readme-ov-file#-what-do-we-instrument).

If your favorite vector DB or LLM is not supported by OpenLLMetry, you can still use OpenLLMetry to report the LLM and vector DB calls manually.
Please open an issue for us as well so we can prioritize adding support for your favorite system.

Here's how you can do that manually in the meantime:

## Reporting LLM calls

To track a call to an LLM, just wrap that call in your code with the `withLLMCall` function in Typescript or `track_llm_call` in Python.
These functions passes a parameter you can use to report the request and response from this call.

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk.tracing.manual import LLMMessage, LLMUsage, track_llm_call

  with track_llm_call(vendor="openai", type="chat") as span:
    span.report_request(
        model="gpt-3.5-turbo",
        messages=[
            LLMMessage(role="user", content="Tell me a joke about opentelemetry")
        ],
    )

    res = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Tell me a joke about opentelemetry"}
        ],
    )

    span.report_response(res.model, [text.message.content for text in res.choices])

    span.report_usage(
      LLMUsage(
          prompt_tokens=...,
          completion_tokens=...,
          total_tokens=...,
          cache_creation_input_tokens=...,
          cache_read_input_tokens=...,
      )
    )
  ```

  ```javascript Typescript theme={null}
  traceloop.withLLMCall(
    { vendor: "openai", type: "chat" },
    async ({ span }) => {
      const messages: ChatCompletionMessageParam[] = [
        { role: "user", content: "Tell me a joke about OpenTelemetry" },
      ];
      const model = "gpt-3.5-turbo";

      span.reportRequest({ model, messages });

      const response = await openai.chat.completions.create({
        messages,
        model,
      });

      span.reportResponse(response);

      return response;

  })
  ```
</CodeGroup>

## Reporting Vector DB calls

To track a call to a vector DB, just wrap that call in your code with the `withVectorDBCall` function.
This function passes a parameter you can use to report the query vector as well as the results from this call.

<CodeGroup>
  ```javascript Typescript theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";

  const results = await traceloop.withVectorDBCall(
      { vendor: "elastic", type: "query" },
      async ({ span }) => {
        span.reportQuery({ queryVector: [1, 2, 3] });

        // call the vector DB like you normally would
        const results = await client.knnSearch({
          ...
        });

        span.reportResults({
          results: [
            {
              ids: "1",
              scores: 0.5,
              distances: 0.1,
              metadata: { key: "value" },
              vectors: [1, 2, 3],
              documents: "doc",
            },
          ],
        });

        return results;
      },
    );
  ```
</CodeGroup>


# Multi-Modality Support
Source: https://www.traceloop.com/docs/openllmetry/tracing/multi-modality

Automatic logging and visualization of multi-modal LLM interactions

OpenLLMetry automatically captures and logs multi-modal content from your LLM interactions, including images, audio, video, and other media types. This enables comprehensive tracing and debugging of applications that work with vision models, audio processing, and other multi-modal AI capabilities.

<Note>
  Multi-modality logging and visualization is currently only available when using [Traceloop](/openllmetry/integrations/traceloop) as your observability backend. Support for other platforms may be added in the future.
</Note>

## What is Multi-Modality Support?

Multi-modality support means that OpenLLMetry automatically detects and logs all types of content in your LLM requests and responses:

* **Images** - Vision model inputs, generated images, screenshots, diagrams
* **Audio** - Speech-to-text inputs, text-to-speech outputs, audio analysis
* **Video** - Video analysis, frame extraction, video understanding
* **Documents** - PDFs, presentations, structured documents
* **Mixed content** - Combinations of text, images, audio in a single request

When you send multi-modal content to supported LLM providers, OpenLLMetry captures the full context automatically without requiring additional configuration.

## How It Works

OpenLLMetry instruments supported LLM SDKs to detect multi-modal content in API calls. When multi-modal data is present, it:

1. **Captures the content** - Extracts images, audio, video, and other media from requests
2. **Logs metadata** - Records content types, sizes, formats, and relationships
3. **Preserves context** - Maintains the full conversation flow with all modalities
4. **Enables visualization** - Makes content viewable in the Traceloop dashboard

All of this happens automatically with zero additional code required.

## Supported Models and Frameworks

Multi-modality logging works with any LLM provider and framework that OpenLLMetry instruments. Common examples include:

### Vision Models

* **OpenAI GPT-4 Vision** - Image understanding and analysis
* **Anthropic Claude 3** - Image, document, and chart analysis
* **Google Gemini** - Multi-modal understanding across images, video, and audio
* **Azure OpenAI** - Vision-enabled models

### Audio Models

* **OpenAI Whisper** - Speech-to-text transcription
* **OpenAI TTS** - Text-to-speech generation
* **ElevenLabs** - Voice synthesis and cloning

### Multi-Modal Frameworks

* **LangChain** - Multi-modal chains and agents
* **LlamaIndex** - Multi-modal document indexing and retrieval
* **Framework-agnostic** - Direct API calls to any provider

## Usage Examples

Multi-modality logging is automatic. Simply use your LLM provider as normal:

### Image Analysis with OpenAI

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    import os
    from openai import OpenAI
    from traceloop.sdk import Traceloop

    Traceloop.init(app_name="vision-app")

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://example.com/image.jpg"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )

    print(response.choices[0].message.content)
    ```

    The image URL and the model's response are automatically logged to Traceloop, where you can view the image alongside the conversation.
  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import OpenAI from "openai";
    import * as traceloop from "@traceloop/node-server-sdk";

    traceloop.initialize({ appName: "vision-app" });

    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY
    });

    async function analyzeImage() {
      const response = await openai.chat.completions.create({
        model: "gpt-4-vision-preview",
        messages: [
          {
            role: "user",
            content: [
              { type: "text", text: "What's in this image?" },
              {
                type: "image_url",
                image_url: {
                  url: "https://example.com/image.jpg"
                }
              }
            ]
          }
        ],
        max_tokens: 300
      });

      console.log(response.choices[0].message.content);
    }

    analyzeImage();
    ```
  </Tab>
</Tabs>

### Image Analysis with Base64

You can also send images as base64-encoded data:

```python theme={null}
import base64
from openai import OpenAI
from traceloop.sdk import Traceloop

Traceloop.init(app_name="vision-app")

client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_data = encode_image("path/to/image.jpg")

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this diagram in detail"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_data}"
                    }
                }
            ]
        }
    ]
)
```

Base64-encoded images are automatically captured and can be viewed in the Traceloop dashboard.

### Multi-Image Analysis

Analyze multiple images in a single request:

```python theme={null}
from openai import OpenAI
from traceloop.sdk import Traceloop

Traceloop.init(app_name="multi-image-analysis")

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Compare these two images and describe the differences"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/before.jpg"}
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/after.jpg"}
                }
            ]
        }
    ]
)
```

All images in the conversation are logged and viewable in sequence.

### Audio Transcription

```python theme={null}
from openai import OpenAI
from traceloop.sdk import Traceloop

Traceloop.init(app_name="audio-app")

client = OpenAI()

audio_file = open("speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

print(transcript.text)
```

Audio files and their transcriptions are automatically logged.

### Text-to-Speech

```python theme={null}
from openai import OpenAI
from traceloop.sdk import Traceloop

Traceloop.init(app_name="tts-app")

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Welcome to our application!"
)

response.stream_to_file("output.mp3")
```

The input text and generated audio metadata are captured automatically.

### Multi-Modal with Anthropic Claude

```python theme={null}
import anthropic
from traceloop.sdk import Traceloop

Traceloop.init(app_name="claude-vision")

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://example.com/chart.png"
                    }
                },
                {
                    "type": "text",
                    "text": "Analyze the trends in this chart"
                }
            ]
        }
    ]
)
```

### Using with LangChain

Multi-modality logging works seamlessly with LangChain:

```python theme={null}
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from traceloop.sdk import Traceloop

Traceloop.init(app_name="langchain-vision")

llm = ChatOpenAI(model="gpt-4-vision-preview")

message = HumanMessage(
    content=[
        {"type": "text", "text": "What's in this image?"},
        {
            "type": "image_url",
            "image_url": {"url": "https://example.com/photo.jpg"}
        }
    ]
)

response = llm.invoke([message])
```

## Viewing Multi-Modal Content in Traceloop

When you view traces in the Traceloop dashboard:

1. **Navigate to your trace** - Find the specific LLM call in your traces
2. **View the conversation** - See the full context including all modalities
3. **Inspect media content** - Click on images, audio, or video to view them inline
4. **Analyze relationships** - Understand how different content types interact
5. **Debug issues** - Identify problems with content formatting or model responses

The Traceloop dashboard provides a rich, visual interface for exploring multi-modal interactions that would be difficult to debug from logs alone.

## Privacy and Content Control

Multi-modal content may include sensitive or proprietary information. You have full control over what gets logged:

### Disable Content Tracing

To prevent logging of any content (including multi-modal data):

<CodeGroup>
  ```bash Environment Variable theme={null}
  TRACELOOP_TRACE_CONTENT=false
  ```

  ```python Python theme={null}
  Traceloop.init(trace_content=False)
  ```

  ```js TypeScript / JavaScript theme={null}
  Traceloop.initialize({ traceContent: false });
  ```
</CodeGroup>

When content tracing is disabled, OpenLLMetry only logs metadata (model name, token counts, latency) without capturing the actual prompts, images, audio, or responses.

### Selective Content Filtering

For more granular control, you can filter specific types of content or implement custom redaction logic. See our [Privacy documentation](/openllmetry/privacy/traces) for detailed options.

## Best Practices

### Storage and Performance

Multi-modal content can be large. Consider these best practices:

* **Monitor storage usage** - Large images and audio files increase trace storage requirements
* **Use appropriate image sizes** - Resize images before sending to LLMs when possible
* **Consider content tracing settings** - Disable content logging in high-volume production environments if not needed
* **Review retention policies** - Configure appropriate data retention in your Traceloop settings

### Debugging Multi-Modal Applications

Multi-modality logging is particularly valuable for:

* **Image quality issues** - See exactly what images were sent to the model
* **Format problems** - Verify that content is properly encoded and transmitted
* **Model behavior** - Understand how models respond to different types of content
* **User experience** - Review actual user-submitted content to improve handling
* **Compliance** - Audit what content is being processed by your application

### Security Considerations

When logging multi-modal content:

* **Review data policies** - Ensure compliance with data protection regulations
* **Filter sensitive content** - Don't log PII, confidential documents, or sensitive images
* **Access controls** - Limit who can view traces with multi-modal content
* **Encryption** - Traceloop encrypts all data in transit and at rest
* **Retention** - Set appropriate retention periods for multi-modal traces

## Limitations

Current limitations of multi-modality support:

* **Traceloop only** - Multi-modal visualization is currently exclusive to the Traceloop platform. When exporting to other observability tools (Datadog, Honeycomb, etc.), multi-modal content metadata is logged but visualization is not available.
* **Storage limits** - Very large media files (>10MB) may be truncated or linked rather than embedded
* **Format support** - Common formats (JPEG, PNG, MP3, MP4, PDF) are fully supported; exotic formats may have limited visualization

## Supported Content Types

OpenLLMetry automatically detects and logs these content types:

| Content Type   | Format Examples                     | Visualization      |
| -------------- | ----------------------------------- | ------------------ |
| Images         | JPEG, PNG, GIF, WebP, SVG           | Inline preview     |
| Audio          | MP3, WAV, OGG, M4A                  | Playback controls  |
| Video          | MP4, WebM, MOV                      | Video player       |
| Documents      | PDF, DOCX (when supported by model) | Document viewer    |
| Base64 Encoded | Any of the above as data URIs       | Automatic decoding |

## Next Steps

* Learn about [privacy controls](/openllmetry/privacy/traces) for multi-modal content
* Explore [supported models and frameworks](/openllmetry/tracing/supported)
* Set up [workflow annotations](/openllmetry/tracing/annotations) for complex multi-modal pipelines
* Configure [Traceloop integration](/openllmetry/integrations/traceloop) to enable multi-modal visualization


# Usage with Threads (Python)
Source: https://www.traceloop.com/docs/openllmetry/tracing/python-threads

How to use OpenLLMetry with `ThreadPoolExecutor` and other thread-based libraries.

Since many LLM operations tend to be I/O bound, it is often useful to use threads to perform multiple operations at once.
Usually, you'll use the `ThreadPoolExecutor` class from the `concurrent.futures` module in the Python standard library, like this:

```python theme={null}
indexes = [pinecone.Index(f"index{i}") for i in range(3)]
executor = ThreadPoolExecutor(max_workers=3)
for i in range(3):
    executor.submit(indexes[i].query, [1.0, 2.0, 3.0], top_k=10)
```

Unfortunately, this won't work as you expect and may cause you to see "broken" traces or missing spans.
The reason relies in how OpenTelemetry (which is what we use under the hood in OpenLLMetry, hence the name)
uses [Python's context](https://docs.python.org/3/library/contextvars.html) to propagate the trace.
You'll need to explictly propagate the context to the threads:

```python theme={null}
indexes = [pinecone.Index(f"index{i}") for i in range(3)]
executor = ThreadPoolExecutor(max_workers=3)
for i in range(3):
    ctx = contextvars.copy_context()
    executor.submit(
        ctx.run,
        functools.partial(index.query, [1.0, 2.0, 3.0], top_k=10),
    )
```

Also check out the [full example](https://github.com/traceloop/openllmetry/blob/main/packages/sample-app/sample_app/thread_pool_example.py).


# What's Supported?
Source: https://www.traceloop.com/docs/openllmetry/tracing/supported

A list of the models, vector DBs and frameworks that OpenLLMetry supports out of the box.

If your favorite system is not on the list, please open an issue for us in the respective Github repo and we'll take care of it.
In the meantime, you can still use OpenLLMetry to report the [LLM and vector DB calls manually](/openllmetry/tracing/manual-reporting).

## LLM Foundation Models

| Model SDK                                                                             | Python | Typescript |
| ------------------------------------------------------------------------------------- | ------ | ---------- |
| [Aleph Alpha](https://aleph-alpha.com/)                                               | ✅      | ❌          |
| [Amazon Bedrock](https://aws.amazon.com/bedrock/)                                     | ✅      | ✅          |
| [Amazon SageMaker](https://aws.amazon.com/sagemaker/)                                 | ✅      | ❌          |
| [Anthropic](https://www.anthropic.com/)                                               | ✅      | ✅          |
| [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) | ✅      | ✅          |
| [Cohere](https://cohere.com/)                                                         | ✅      | ✅          |
| [Google Gemini](https://ai.google.dev/)                                               | ✅      | ✅          |
| [Google VertexAI](https://cloud.google.com/vertex-ai)                                 | ✅      | ✅          |
| [Groq](https://groq.com/)                                                             | ✅      | ⏳          |
| [HuggingFace Transformers](https://huggingface.co/)                                   | ✅      | ⏳          |
| [IBM watsonx](https://www.ibm.com/watsonx)                                            | ✅      | ⏳          |
| [Mistral AI](https://mistral.ai/)                                                     | ✅      | ⏳          |
| [Ollama](https://ollama.com/)                                                         | ✅      | ⏳          |
| [OpenAI](https://openai.com/)                                                         | ✅      | ✅          |
| [Replicate](https://replicate.com/)                                                   | ✅      | ⏳          |
| [together.ai](https://together.ai/)                                                   | ✅      | ⏳          |
| [WRITER](https://writer.com/)                                                         | ✅      | ✅          |

## Vector DBs

| Vector DB                                              | Python | Typescript |
| ------------------------------------------------------ | ------ | ---------- |
| [Chroma DB](https://www.trychroma.com/)                | ✅      | ✅          |
| [Elasticsearch](https://www.elastic.co/elasticsearch/) | ✅      | ✅          |
| [LanceDB](https://lancedb.com/)                        | ✅      | ⏳          |
| [Marqo](https://www.marqo.ai/)                         | ✅      | ❌          |
| [Milvus](https://milvus.io/)                           | ✅      | ⏳          |
| [pgvector](https://github.com/pgvector/pgvector)       | ✅      | ✅          |
| [Pinecone](https://pinecone.io/)                       | ✅      | ✅          |
| [Qdrant](https://qdrant.tech/)                         | ✅      | ✅          |
| [Weaviate](https://weaviate.io/)                       | ✅      | ⏳          |

## Frameworks

| Framework                                                       | Python | Typescript |
| --------------------------------------------------------------- | ------ | ---------- |
| [Agno](https://github.com/agno-oss/agno)                        | ✅      | ❌          |
| [AWS Strands](https://github.com/awslabs/strands)               | ✅      | ❌          |
| [Burr](https://www.github.com/dagworks-inc/burr)                | ✅      | ❌          |
| [CrewAI](https://www.crewai.com/)                               | ✅      | ❌          |
| [Haystack by deepset](https://haystack.deepset.ai/)             | ✅      | ❌          |
| [Langchain](https://www.langchain.com/)                         | ✅      | ✅          |
| [LiteLLM](https://www.litellm.ai/)                              | ✅      | ❌          |
| [LlamaIndex](https://www.llamaindex.ai/)                        | ✅      | ✅          |
| [OpenAI Agents](https://github.com/openai/openai-agents-python) | ✅      | ❌          |


# Tracking User Feedback
Source: https://www.traceloop.com/docs/openllmetry/tracing/user-feedback



When building LLM applications, it quickly becomes highly useful and important to track user feedback on the result of your LLM workflow.

Doing that with OpenLLMetry is easy. First, make sure you [associate your LLM workflow with unique identifiers](/openllmetry/tracing/association).

Then, [create an Annotation Task](https://app.traceloop.com/annotation-tasks) within Traceloop to collect user feedback as annotations.
The annotation task should include:

* The [entity](/openllmetry/tracing/association) you want to collect feedback for (e.g., `chat_id`)
* Tags you want to track (e.g., `score`, `feedback_text`)

You can log user feedback by calling our Python SDK or TypeScript SDK.
All feedback must follow the structure defined in your annotation task.

For example, to implement thumbs-up/thumbs-down feedback, create an annotation task with a tag named `is_helpful` that accepts the values `thumbs-up` and `thumbs-down`.

<Note>
  The entity you report feedback for must match the one defined in your annotation
  task and association property.
</Note>

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk import Traceloop

  traceloop_client = Traceloop.get()
  traceloop_client.user_feedback.create(
      "your-annotation-task",
      "12345",
      {"is_helpful": "thumbs-up"},
  )
  ```

  ```js Typescript theme={null}
  const client = traceloop.getClient();
  await client.userFeedback.create({
      annotationTask: "your-annotation-task",
      entity: {
          id: "12345",
      },
      tags: {
          is_helpful: "thumbs-up",
      },
  });
  ```
</CodeGroup>


# Versioning
Source: https://www.traceloop.com/docs/openllmetry/tracing/versions

Learn how to enrich your traces by versioning your workflows and prompts

## Workflow Versions

You can version your workflows and tasks. Just provide the `version` argument to the decorator:

<CodeGroup>
  ```python Python theme={null}
  @workflow(name="my_workflow", version=2)
  def my_workflow():
      ...
  ```

  ```js Typescript theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";

  class JokeCreation {
    @traceloop.workflow({ name: "pirate_joke_generator", version: 2 })
    async joke_workflow() {
      eng_joke = create_joke();
      pirate_joke = await translate_joke_to_pirate(eng_joke);
      signature = await generate_signature(pirate_joke);
      console.log(pirate_joke + "\n\n" + signature);
    }
  }
  ```

  ```js Javascript - without Decorators theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";

  async function joke_workflow() {
    return await traceloop.withWorkflow(
      { name: "pirate_joke_generator", version: 2 },
      async () => {
        eng_joke = create_joke();
        pirate_joke = await translate_joke_to_pirate(eng_joke);
        signature = await generate_signature(pirate_joke);
        console.log(pirate_joke + "\n\n" + signature);
      }
    );
  }
  ```
</CodeGroup>

## Prompt Versions

You can enrich your prompt traces by providing data about the prompt's version, specifying the prompt template or the variables:

<CodeGroup>
  ```python Python theme={null}
  Traceloop.set_prompt(
      "Tell me a joke about {subject}", {"subject": subject}, version=1
  )
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": f"Tell me a joke about {subject}"}],
  )
  ```
</CodeGroup>


# Without OpenLLMetry SDK
Source: https://www.traceloop.com/docs/openllmetry/tracing/without-sdk



All the instrumentations are provided as standard OpenTelemetry instrumentations so you can use them directly if you're
already using OpenTelemetry.

## Installation

Install the appropriate packages for the modules you want to use.

### LLM Foundation Models

| Provider                                                                       | PyPi Package Name                         |
| ------------------------------------------------------------------------------ | ----------------------------------------- |
| [OpenAI](https://pypi.org/project/opentelemetry-instrumentation-openai/)       | `opentelemetry-instrumentation-openai`    |
| [Anthropic](https://pypi.org/project/opentelemetry-instrumentation-anthropic/) | `opentelemetry-instrumentation-anthropic` |
| [Bedrock](https://pypi.org/project/opentelemetry-instrumentation-bedrock/)     | `opentelemetry-instrumentation-bedrock`   |
| [Cohere](https://pypi.org/project/opentelemetry-instrumentation-cohere/)       | `opentelemetry-instrumentation-cohere`    |

### Vector DBs

| Vector DB                                                                    | PyPi Package Name                        |
| ---------------------------------------------------------------------------- | ---------------------------------------- |
| [Chroma](https://pypi.org/project/opentelemetry-instrumentation-chromadb/)   | `opentelemetry-instrumentation-chromadb` |
| [Pinecone](https://pypi.org/project/opentelemetry-instrumentation-pinecone/) | `opentelemetry-instrumentation-pinecone` |

### LLM Frameworks

| Framework                                                                        | PyPi Package Name                          |
| -------------------------------------------------------------------------------- | ------------------------------------------ |
| [Haystack](https://pypi.org/project/opentelemetry-instrumentation-haystack/)     | `opentelemetry-instrumentation-haystack`   |
| [Langchain](https://pypi.org/project/opentelemetry-instrumentation-langchain/)   | `opentelemetry-instrumentation-langchain`  |
| [LlamaIndex](https://pypi.org/project/opentelemetry-instrumentation-llamaindex/) | `opentelemetry-instrumentation-llamaindex` |

## Usage

Instantiate the instrumentations you want to use and call `instrument()` to register them with OpenTelemetry.

For example, to use the OpenAI instrumentation:

```python Python theme={null}
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

OpenAIInstrumentor().instrument()
```

<Tip>
  If you're setting OpenTelemetry's `TracerProvider` manually, make sure to do
  this before calling `instrument()`.
</Tip>


# Troubleshooting
Source: https://www.traceloop.com/docs/openllmetry/troubleshooting

Not seeing anything? Here are some things to check.

<Frame>
  <img />

  <img />
</Frame>

We've all been there. You followed all the instructions, but you're not seeing any traces. Let's fix this.

## 1. Disable batch sending

Sending traces in batch is useful in production, but can be confusing if you're working locally.
Make sure you've [disabled batch sending](/openllmetry/configuration#disable-batch).

<CodeGroup>
  ```python Python theme={null}
  Traceloop.init(disable_batch=True)
  ```

  ```js Typescript / Javascript theme={null}
  Traceloop.init({ disableBatch: true });
  ```
</CodeGroup>

## 2. Check the logs

When Traceloop initializes, it logs a message to the console, specifying the endpoint that it uses.
If you don't see that, you might not be initializing the SDK properly.

> **Traceloop exporting traces to `https://api.traceloop.com`**

## 3. (TS/JS only) Fix known instrumentation issues

If you're using Typescript or Javascript, make sure to import traceloop before any other LLM libraries.
This is because traceloop needs to instrument the libraries you're using, and it can only do that if it's imported first.

```js theme={null}
import * as traceloop from "@traceloop/traceloop";
import OpenAI from "openai";
...
```

If that doesn't work, you may need to manually instrument the libraries you're using.
See the [manual instrumentation guide](/openllmetry/tracing/js-force-instrumentations) for more details.

```js theme={null}
import OpenAI from "openai";
import * as LlamaIndex from "llamaindex";

traceloop.initialize({
  appName: "app",
  instrumentModules: {
    openAI: OpenAI,
    llamaIndex: LlamaIndex,
    // Add or omit other modules you'd like to instrument
  },
```

## 4. Is your library supported yet?

Check out [OpenLLMetry](https://github.com/traceloop/openllmetry#readme) or [OpenLLMetry-JS](https://github.com/traceloop/openllmetry-js#readme) README files to see which libraries and versions are currently supported.
Contributions are always welcome! If you want to add support for a library, please open a PR.

## 5. Try outputting traces to the console

Use the `ConsoleExporter` and check if you see traces in the console.

<CodeGroup>
  ```python Python theme={null}
  from opentelemetry.sdk.trace.export import ConsoleSpanExporter

  Traceloop.init(exporter=ConsoleSpanExporter())

  ```

  ```js Typescript / Javascript theme={null}
  import { ConsoleSpanExporter } from "@opentelemetry/sdk-trace-node";

  traceloop.initialize({ exporter: new ConsoleSpanExporter() });
  ```
</CodeGroup>

If you see traces in the console, then you probable haven't configured the exporter properly.
Check the [integration guide](/openllmetry/integrations) again, and make sure you're using the right endpoint and API key.

## 6. Talk to us!

We're here to help.
Reach out any time over
[Slack](https://traceloop.com/slack),
[email](mailto:dev@traceloop.com), and we'd love to assist you.


# Column Management
Source: https://www.traceloop.com/docs/playgrounds/columns/column-management

Learn all columns general functionalities

Columns in the Playground can be reordered, edited, or deleted at any time to adapt your workspace as your analysis evolves. Understanding how to manage columns effectively helps you maintain organized and efficient playgrounds.

## Columns Settings

Column Settings lets you hide specific columns from the Playground and reorder them as needed. To open the settings, click the Playground Action button and select Column Settings

<img />

<img />

To change the column order, use the six-dot handle on the right side of each column to simply drag the column into the desired position.

To hide a column, toggle its switch in the menu.

<Info>
  Columns can also be reordered by dragging them to your desired position in the playground
</Info>

<img />

<img />

## Columns Actions

Each column has a menu that lets you manage and customize it. From this menu, you can:

* Rename the column directly by editing its title
* Edit the column configuration
* Duplicate the column to create a copy with the same settings
* Delete the column if it’s no longer needed

<img />

<img />


# Data Columns
Source: https://www.traceloop.com/docs/playgrounds/columns/data-columns



Columns are the building blocks of playgrounds, defining what kind of data you can store, process, and analyze.

<img />

<img />

<Tip>
  **Need to reorder, edit, or delete columns?**

  Learn how to effectively manage your columns in the [Column Management](./column-management) guide.
</Tip>

## 📝 Data Input Columns

Store and manage static data entered manually or imported from external sources.

### Text field

Free-form text input with multiline support

### Numeric

Numbers, integers, and floating-point values

<img />

<img />

The last row allows you to choose a calculation method for the column, such as average, median, minimum, maximum, or sum.

<img />

<img />

### Single select

Single-choice columns let you define a set of predefined options and restrict each cell to one selection.
To create one, set the column name and add options in the Create Column drawer.
In the values box, type an option and press Enter to save it—once added, it will appear as a colored label.

In the table, each cell will then allow you to select only one of the defined options.
This column type is especially useful for manual tagging with a single tag.

<img />

<img />

<img />

<img />

### Multi select

Multi-select columns let you define a set of predefined options and allow each cell to contain multiple selections. The setup process is the same as for single-select columns: define the column name, add options in the Create Column drawer, and save them as labels.

In the table, each cell can then include several of the defined options. This column type is especially useful for manual tagging with multiple tags.

<img />

<img />

### JSON

A JSON column allows you to store and edit structured JSON objects directly in the Playground. Each cell can contain a JSON value, making it easy to work with complex data structures.

When editing a cell, an Edit JSON panel opens with syntax highlighting and formatting support, so you can quickly add or update fields.

<img />

<img />


# Prompt Column
Source: https://www.traceloop.com/docs/playgrounds/columns/prompt

Execute LLM prompts with full model configuration

### Prompt

A Prompt column allows you to define a custom prompt and run it directly on your Playground data.
You can compose prompts with messages (system, user, assistant or developer), insert playground variables, and configure which model to use.
Each row in your playground will be passed through the prompt, and the model’s response will be stored in the column.

<Info>
  Prompt columns make it easy to test different prompts against real data, compare model outputs side by side.
</Info>

<img />

<img />

## Prompt Writing

Write your prompt messages by selecting a specific role—System, User, Assistant, or Developer.

You can insert variables into the prompt using curly brackets (e.g., `{{variable_name}}`) or by adding column valuable with the top right `+` button in the message box. These variables can then be mapped to existing column data, allowing your prompt to dynamically adapt to the playground

<img />

<img />

## Configuration Options

### Model Selection

You can connect to a wide range of LLM providers and models. Common choices include OpenAI (GPT-4o, GPT-4o-mini), Anthropic (Claude-3.5-Sonnet, Claude-3-Opus), and Google (Gemini-2.5 family).
Other providers such as Groq and DeepSeek may also be supported, and additional integrations will continue to be added over time.

### Structured Output

Structured output can be enabled for models that support it. You can define a schema in several ways:

* **JSON Editor** - Write a JSON structure directly in the editor
* **Visual Editor** - Add parameters interactively, specifying their names and types
* **Generate Schema** - Use the "Generate schema" button on the top right to automatically create a schema based on your written prompt

<img />

<img />

## Tools

Tools let you extend prompts by allowing the model to call custom functions with structured arguments. Instead of plain text, the model can return a validated tool-call object that follows your schema.

To create a tool, give it a name and description so the model knows when to use it. Then define its parameters with a name, description, type (string, number, boolean, etc.), and whether they are required.

### Advanced Settings

Fine-tune model behavior options:

* **Temperature** (0.0-1.0): Control randomness and creativity
* **Max Tokens**: Limit model output length (1-8000+ depending on model)
* **Top P**: Nucleus sampling parameter (0.0-1.0)
* **Frequency Penalty**: Reduce repetition (0.0 to 1.0)
* **Presence Penalty**: Encourage topic diversity (0.0 to 1.0)
* **Logprobs**: When enabled, returns the probability scores for generated tokens
* **Thinking Budget** (512-24576): Sets the number of tokens the model can use for internal reasoning before producing the final output
  A higher budget allows more complex reasoning but increases cost and runtime
* **Exclude Reasoning from Response**: If enabled, the model hides its internal reasoning steps and only outputs the final response

## Prompt Execution

A prompt can be executed across all cells in a column or on a specific cell.

Prompt outputs can be mapped to different columns by clicking a cell and selecting the mapping icon, or by double-clicking the cell


# Quick Start
Source: https://www.traceloop.com/docs/playgrounds/quick-start



Playgrounds are interactive spreadsheets where you can organize your data and experiment with LLMs, evaluate outputs, and analyze data.
Think of them as powerful workbenches for AI development that combine the flexibility of a spreadsheet with the power of LLM evaluation and execution.
It’s designed for everyone, from product managers and analysts to QA, data engineers, and software developers.

<Frame>
  <img />

  <img />
</Frame>

<Tip>
  Playgrounds can be used to build datasets for experiments and evaluation. Once you've structured your data in a playground, you can export it to a dataset and publish a version for reproducible testing. Learn more about [datasets](../datasets/quick-start).
</Tip>

## Playground Structure

A playground is organized as a table-like structure with three fundamental components: **rows**, **columns**, and **cells**. Understanding how these work together is essential for effective playground usage.

### Rows

Rows represent individual **data points** or **test cases** in your playground. Each row is a complete record that spans across all columns.
Each row in the Playground is independent and can be executed on its own, maintains an order that can be rearranged as needed.

### Row Operations

* **Add Row**: Create new rows manually or through bulk operations
* **Generate Rows**: Use the AI row generator to create new rows based on the existing data in your Playground.
* **Delete Row**: Remove unwanted rows individually or in bulk
* **Execute Row**: Execute all cells in a specific row

## Columns

Columns are the building blocks of playgrounds, defining what kind of data you can store, process, and analyze. They come in different types to handle various data formats and use cases:

**Data Input Columns** store static data such as text, json, numbers and tags

**Prompt Columns** execute LLM prompts directly on your data with full model configuration, allowing you to test different prompts and compare outputs side by side.

**Evaluation Columns** assess AI outputs and data quality using pre-built evaluators or custom evaluators tailored to your specific needs. Learn more about [evaluators](../evaluators/intro).

You can manage columns by reordering, hiding, editing, duplicating, or deleting them as your analysis evolves. Learn more about [column types](./columns/data-columns) and [column management](./columns/column-management).

## Create a Playground

Data can be imported from different sources:

1. CSV files
2. JSON file
3. From A Dataset
4. From production spans

You can create a Playground from scratch and import data later. Simply set a name for the Playground and start adding columns, rows, and data.

<Frame>
  <img />

  <img />
</Frame>

## Running a Playground

Execute all cells in your playground by clicking the play button in the top right corner. This runs all prompt columns and evaluation columns across every row, allowing you to process your entire dataset at once.

You can also run individual cells, rows, or columns by clicking on their respective play buttons to test specific configurations. For example, you might run a single agent execution, test one user input, or evaluate a specific chat conversation.

Ready to build more sophisticated playgrounds? Dive into the [complete documentation](./index) or explore specific [column types](./columns/data-columns) to unlock the full power of Traceloop Playgrounds!


# Quick Start
Source: https://www.traceloop.com/docs/prompts/quick-start



<Frame>
  <img />

  <img />
</Frame>

You can use Traceloop to manage your prompts and model configurations.
That way you can easily experiment with different prompts, and rollout changes gradually and safely.

<Note>
  **Prerequisites:** You need an API key set as the environment variable `TRACELOOP_API_KEY`.
  [Generate one in Settings →](/settings/managing-api-keys)
</Note>

<Steps>
  <Step title="Create a new prompt">
    Click **New Prompt** to create a new prompt. Give it a name, which will be used to retrieve it in your code later.
  </Step>

  <Step title="Define it in the Prompt Registry">
    Set the system and/or user prompt. You can use variables in your prompt by
    following the [Jinja format](https://jinja.palletsprojects.com/en/3.1.x/templates/) of `{{ variable_name }}`.
    The values of these variables will be passed in when you retrieve the prompt in your code.

    For more information see the [Registry Documentation](/prompts/registry).

    <Tip>
      This screen is also a prompt playground. Give the prompt a try by clicking
      **Test** at the bottom.
    </Tip>
  </Step>

  <Step title="Deploy the prompt to your developement environement">
    Click **Deploy to Dev** to deploy the prompt to your development environment.
  </Step>

  <Step title="Use the prompt in your code">
    <Important>
      Make sure to initialize the SDK and enable traceloop sync (see below). On
      Typescript/Javascript, you should also wait for the initialization to
      complete.
    </Important>

    <CodeGroup>
      ```python Python theme={null}
      from traceloop.sdk import Traceloop

      Traceloop.init(traceloop_sync_enabled=True)
      ```

      ```js Typescript / Javascript theme={null}
      import * as traceloop from "@traceloop/node-server-sdk";

      traceloop.initialize({ traceloopSyncEnabled: true });
      await traceloop.waitForInitialization();
      ```
    </CodeGroup>

    Retrieve your prompt by using the `get_prompt` function.
    For example, if you've created a prompt with the key `joke_generator` and a single variable `persona`:

    <CodeGroup>
      ```python Python theme={null}
      from openai import OpenAI
      from traceloop.sdk.prompts import get_prompt

      client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

      prompt_args = get_prompt(key="joke_generator", variables={"persona": "pirate"})
      completion = client.chat.completions.create(**prompt_args)
      ```

      ```js Typescript / Javascript theme={null}
      import * as traceloop from "@traceloop/node-server-sdk";

      const prompt = traceloop.getPrompt("joke_generator", { persona: "pirate" });
      const chatCompletion = await openai.chat.completions.create(prompt);
      ```

      ```go Go theme={null}
      import "github.com/sashabaranov/go-openai"

      func call_llm() {
        // traceloop is the object you got when you initialized the SDK
        request, err := traceloop.GetOpenAIChatCompletionRequest("joke_generator", map[string]interface{}{ "persona": "pirate" })
        if err != nil {
          fmt.Printf("GetOpenAIChatCompletionRequest error: %v\n", err)
          return
        }
        client := openai.NewClient(os.Getenv("OPENAI_API_KEY"))
          resp, err := client.CreateChatCompletion(
            context.Background(),
            *request,
          )
      }
      ```
    </CodeGroup>

    <Note>
      The returned variable `prompt_args` is compatible with the API used by the
      foundation models SDKs (OpenAI, Anthropic, etc.) which means you can directly
      plug in the response to the appropriate API call.
    </Note>

    For more information see the [SDK Usage Documentation](/prompts/sdk-usage).
  </Step>
</Steps>


# Prompt Registry
Source: https://www.traceloop.com/docs/prompts/registry

Manage your prompts on the Traceloop platform

Traceloop's Prompt Registry is where you manage your prompts. You can create, edit, evaluate and deploy prompts to your environments.

## Configuring Prompts

<Frame>
  <img />

  <img />
</Frame>

The prompt configuration is composed of two parts:

* The prompt template (system and/or user prompts)
* The model configuration (temperature, top\_p, etc.)

<Tip>
  Your prompt template can include variables. Variables are defined according to
  the syntax of the parser specified. For example, if using `jinjia2` the syntax
  will be `{{ variable_name }}`. You can then pass variable values to the SDK
  when calling `get_prompt`. See the example on the [SDK
  Usage](/prompts/sdk-usage) section.
</Tip>

Initially, prompts are created in `Draft Mode`. In this mode, you can make changes to the prompt and configuration. You can also test your prompt in the playground (see below).

## Testing a Prompt Configuration (Prompt Playground)

By using the prompt playground you can iterate and refine your prompt before deploying it.

<Frame>
  <img />

  <img />
</Frame>

Simply click on the `Test` button in the playground tab at the bottom of the screen.

If your prompt includes variables, then you need to define values for them before testing.
Choose `Variables` in the right side bar and assign a value to each.

Once you click the `Test` button your prompt template will be rendered with the values you provided and will be sent to the configured LLM with the model configuration defined.
The completion response (including token usage) will be displayed in the playground.

## Deploying Prompts

<Frame>
  <img />

  <img />
</Frame>

Draft mode prompts can only be deployed to the `development` environment.

Once you are satisfied with the prompt, you can publish it and make it available to deploy in all environments.
Once published, the prompt version cannot be edited anymore.

Choose the `Deploy` Tab to navigate to the deployments page for your prompt.

Here, you can see all recent prompt versions, and which environments they are deployed to.
Simply click on the `Deploy` button to deploy a prompt version to an environment. Similarly, click `Rollback` to revert to a previous prompt version for a specific environment.

<Note>
  As a safeguard, you cannot deploy a prompt to the `Staging` environment before
  first deploying it to `Development`. Similarly, you cannot deploy to
  `Production` without first deploying to `Staging`.
</Note>

To fetch prompts from a specific environment, you must supply that environment's API key to the Traceloop SDK. See the [SDK Configuration](/openllmetry/integrations/traceloop) for details

## Prompt Versions

If you want to make changes to your prompt after deployment, simply create a new version by clicking on the `New Version` button. New versions will be created in `Draft Mode`.

<Warning>
  If you change the names of variables or add/remove existing variables, you
  will be required to create a new prompt.
</Warning>


# Fetching Prompts
Source: https://www.traceloop.com/docs/prompts/sdk-usage

Use your managed prompts with the Traceloop SDKs

### Using your prompt

Make sure to set `traceloop_sync_enabled=True` when initializing the SDK or the `TRACELOOP_SYNC_ENABLED` environment variable to `true`,
to enable the prompt sync.

The SDK fetches your prompts from Traceloop servers. Changes made to a prompt are available in the SDK during runtime.
The SDK polls the Traceloop servers for changes every every poll interval.

The default poll interval is 60 seconds but can be configured with the `TRACELOOP_SYNC_POLL_INTERVAL` environment variable, or the initialization function.
When in the `Development` environment, the poll interval is determined by the `TRACELOOP_SYNC_DEV_POLL_INTERVAL` environment variable or appropriate initialization argument, and defaults to 5 seconds.

Make sure you've configured the SDK with the right environment and API Key. See the [SDK documentation](/openllmetry/integrations/traceloop) for more information.

<Tip>
  The SDK uses smart caching mechanisms to proide zero latency for fetching
  prompts.
</Tip>

## Get Prompt API

Let's say you've created a prompt with a key `joke_generator` in the UI and set ot to:

```
Tell me a joke about OpenTelemetry as a {{persona}}
```

Then, you can retrieve it with in your code using `get_prompt`:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  from traceloop.sdk.prompts import get_prompt

  client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

  prompt_args = get_prompt(key="joke_generator", variables={"persona": "pirate"})
  completion = client.chat.completions.create(**prompt_args)
  ```

  ```js Typescript / Javascript theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";

  const prompt = traceloop.getPrompt("joke_generator", { persona: "pirate" });
  const chatCompletion = await openai.chat.completions.create(prompt);
  ```

  ```go Go theme={null}
  import "github.com/sashabaranov/go-openai"

  func call_llm() {
    // traceloop is the object you got when you initialized the SDK
    request, err := traceloop.GetOpenAIChatCompletionRequest("joke_generator", map[string]interface{}{ "persona": "pirate" })
      if err != nil {
        fmt.Printf("GetOpenAIChatCompletionRequest error: %v\n", err)
        return
      }
    client := openai.NewClient(os.Getenv("OPENAI_API_KEY"))
      resp, err := client.CreateChatCompletion(
        context.Background(),
        *request,
      )
  }
  ```
</CodeGroup>

<Tip>
  The returned variable `prompt_args` is compatible with the API used by the
  foundation models SDKs (OpenAI, Anthropic, etc.) which means you should
  directly plug in the response to the appropriate API call.
</Tip>


# Full Platform Self-Hosting
Source: https://www.traceloop.com/docs/self-host/full-deployment

Deploy the complete Traceloop platform in your infrastructure

The Full Platform deployment provides complete control over the entire Traceloop stack, perfect for organizations with strict security requirements or air-gapped environments.

## Infrastructure Requirements

### Core Components

1. **ClickHouse Database**

   * [ClickHouse Cloud](https://clickhouse.cloud)
   * [Self-hosted ClickHouse](https://clickhouse.com/docs/en/install)

2. **Kafka Message Queue**

   * [Confluent Cloud](https://confluent.cloud)
   * [Amazon MSK](https://aws.amazon.com/msk/)
   * [Apache Kafka](https://kafka.apache.org/quickstart)

3. **PostgreSQL Database**

   * [Amazon Aurora PostgreSQL](https://aws.amazon.com/rds/aurora/postgresql-features/)
   * [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/products/postgresql/)
   * [PostgreSQL](https://www.postgresql.org/download/)

4. **Kubernetes Cluster**
   * [Amazon EKS](https://aws.amazon.com/eks/)
   * [Google GKE](https://cloud.google.com/kubernetes-engine)
   * [Azure AKS](https://azure.microsoft.com/en-us/products/kubernetes-service)
   * Any Helm-compatible Kubernetes distribution

5. **S3 Object Storage**
   * [Amazon S3](https://aws.amazon.com/s3/)

## Compatibility Matrix

| Service                                    | Production version (May 30 2025) | Support & upgrade stance                                      |
| ------------------------------------------ | -------------------------------- | ------------------------------------------------------------- |
| **Traceloop (core services & Helm chart)** | **0.3.0**                        | Quarterly releases; 0.3.x receives critical fixes.            |
| **Aurora PostgreSQL**                      | 15.10                            | Managed patching. Minor versions ≥ 15.2 are *supported*.      |
| **ClickHouse**                             | 24.12                            | We track the 24.x LTS line; 23.x is **best‑effort**.          |
| **Kafka (Confluent Platform)**             | 3.8.x (KRaft)                    | Confluent GA releases promoted within 4 weeks.                |
| **Temporal**                               | 1.27.1                           | 1.27.\* patches supported; major ≥ 1.28 validated on request. |
| **Centrifugo**                             | 6.1.0                            | API‑stable; 6.x minor upgrades are drop‑in.                   |

### Validation requests

Submit desired versions via [dev@traceloop.com](mailto:dev@traceloop.com).
Minor‑version certification is typically completed within 2 business days; major‑version certification within 7 business days.

## Deployment Options

### Option 1: Infrastructure + Applications (Recommended for Production)

Use Terraform/CloudFormation to provision managed infrastructure components, then deploy Traceloop applications via Helm.

### Option 2: All-in-One Helm Deployment

Deploy everything including PostgreSQL, ClickHouse, and Kafka through Helm charts for development/testing environments.
Requires manual load balancer setup to forward traffic to NodePort 30080 and handle SSL termination.

***

## Option 1: Infrastructure + Applications Deployment

<Note>
  Contact our team to get the CloudFormation templates and Terraform configurations for deploying the infrastructure components.
  The deployment process below assumes your infrastructure is already provisioned and available.
</Note>

### Deployment Process

#### 1. Create Traceloop namespace

```bash theme={null}
kubectl create namespace traceloop
```

#### 2. Create required secrets under traceloop namespace

##### Docker Hub images pull secret.

Credentials will be provided by Traceloop via secure channel

```bash theme={null}
kubectl create secret docker-registry regcred \
  --namespace traceloop \
  --docker-server=docker.io \
  --docker-username=<dockerhub-username-provided-by-traceloop> \
  --docker-password=<dockerhub-password-provided-by-traceloop>
```

##### Postgres Secret (if not already present)

```bash theme={null}
kubectl create secret generic traceloop-postgres-secret \
  --namespace traceloop \
  --from-literal=POSTGRES_DATABASE_USERNAME=<postgres-username> \
  --from-literal=POSTGRES_DATABASE_PASSWORD=<postgres-password>
```

##### ClickHouse Secret (if not already present)

```bash theme={null}
kubectl create secret generic traceloop-clickhouse-secret \
  --namespace traceloop \
  --from-literal=CLICKHOUSE_USERNAME=<clickhouse-username> \
  --from-literal=CLICKHOUSE_PASSWORD=<clickhouse-password>
```

##### Kafka Secret (if not already present)

```bash theme={null}
kubectl create secret generic traceloop-kafka-secret \
  --namespace traceloop \
  --from-literal=KAFKA_API_KEY=<kafka-api-key> \
  --from-literal=KAFKA_API_SECRET=<kafka-api-secret>
```

#### 3. Download the Traceloop Helm chart to your local environment

```bash theme={null}
# Add Traceloop Helm repository
helm pull oci://registry-1.docker.io/traceloop/helm --untar
```

#### 4. Run subcharts and dependency extractions script

```bash theme={null}
chmod +x extract-subcharts.sh
./extract-subcharts.sh
```

#### 5. Update `values-customer.yaml` with your domain & auth configuration:

Configure your deployment settings including gateway, authentication, and image support:

```yaml theme={null}
kong-gateway:
  service:
    type: NodePort # Or ClusterIP
    proxy:
      # port: 8000
      # targetPort: 8000
      nodePort: 30080
    status:
      # port: 8100
      # targetPort: 8100
      nodePort: 30081
  kong:
    domain: "user-provided"
    appSubdomain: "app" # Can be overridden by customer
    apiSubdomain: "api" # Can be overridden by customer
    realtimeSubdomain: "realtime" # Can be overridden by customer

helm-api-service:
  app:
    imagesSupport:
      enabled: false # Set to true to enable image storage and processing
      s3ImagesBucket: "" # S3 bucket name where images will be stored
      eksRegion: "" # AWS region where your EKS cluster and S3 bucket are located

customerConfig:
  propelauth:
    authURL: "traceloop-provided"
  launchDarkly:
    clientId: "" # OPTIONAL traceloop-provided

customerSecret:
  openai:
    key: "user-provided"
  launchDarkly:
    apiKey: "" # OPTIONAL traceloop-provided
  propelauth:
    verifierKey: "traceloop-provided"
    apiKey: "traceloop-provided"
  centrifugo:
    apiKey: "user-provided"
    tokenHmacSecretKey: "user-provided"
  encryptionSecret:
    apiKey: "user-provided"
```

#### 6. Update the following files with relevant addresses

##### values-external-postgres.yaml

```yaml theme={null}
postgresql:
  enabled: false
  host: "" # Example: "my-postgres-server.example.com"
  port: "" # Example: "5432"
  database: "" # Example: "traceloop"
```

##### values-external-clickhouse.yaml

```yaml theme={null}
clickhouse:
  enabled: false
  host: "" # Example: "my-clickhouse-server.example.com"
  port: "" # Example: "9440"
  httpPort: "" # Example: "8443"
  database: "" # Example: "default"
  sslMode: "" # Example: "strict" or "none"
  sslEnabled: "" # Example: "true" or "false"
```

##### values-external-kafka.yaml

```yaml theme={null}
kafka:
  enabled: false
  bootstrapServer: "" # Example: "kafka-broker.example.com:9092"
  securityProtocol: "" # Example: "SASL_SSL" or "PLAINTEXT"
  saslMechanisms: "" # Example: "PLAIN" or "SCRAM-SHA-256"
  apiKey: "" # Your Kafka API key if required
  apiSecret: "" # Your Kafka API secret if required
```

##### values-temporal.yaml

Replace only these values to the values you have from postgres.

```yaml theme={null}
temporal:
  ...
  server:
    config:
      persistence:
        ...
        default:
          ...
          sql:
            ...
            host: "" # Example: "my-postgres-server.example.com"
            ...
            user: "" # Example: "traceloop"
            password: ""
            existingSecret: "" # Example: "traceloop-postgres-secret"
            existingSecretKey: "" # Example: "POSTGRES_DATABASE_PASSWORD"
            ...
      visibility:
        ...
        default:
          ...
          sql:
            ...
            host: "" # Example: "my-postgres-server.example.com"
            ...
            user: "" # Example: "traceloop"
            password: ""
            existingSecret: "" # Example: "traceloop-postgres-secret"
            existingSecretKey: "" # Example: "POSTGRES_DATABASE_PASSWORD"
            ...
```

#### 7. Install Traceloop Helm chart

```bash theme={null}
helm upgrade --install traceloop . \
  -n traceloop \
  --values values.yaml \
  --values values-customer.yaml \
  --values values-external-kafka.yaml \
  --values values-external-clickhouse.yaml \
  --values values-external-postgres.yaml \
  --values values-temporal.yaml \
  --values values-centrifugo.yaml \
  --create-namespace \
  --dependency-update
```

***

## Option 2: All-in-One Helm Deployment

<Note>
  This deployment includes a Kong API Gateway that listens on NodePort 30080.
  You will need to manually provision a load balancer that forwards traffic to your Kubernetes cluster's NodePort 30080 and handles SSL termination.
</Note>

This approach deploys all components including databases through Helm charts.

### Deployment Process

#### 1. Create Traceloop namespace

```bash theme={null}
kubectl create namespace traceloop
```

#### 2. Create required secrets under traceloop namespace

##### Docker Hub images pull secret.

Credentials will be provided by Traceloop via secure channel

```bash theme={null}
kubectl create secret docker-registry regcred \
  --namespace traceloop \
  --docker-server=docker.io \
  --docker-username=<dockerhub-username-provided-by-traceloop> \
  --docker-password=<dockerhub-password-provided-by-traceloop>
```

#### 3. Download the Traceloop Helm chart to your local environment

```bash theme={null}
# Add Traceloop Helm repository
helm pull oci://registry-1.docker.io/traceloop/helm --untar
```

#### 4. Run subcharts and dependency extractions script

```bash theme={null}
chmod +x extract-subcharts.sh
./extract-subcharts.sh
```

#### 5. Update `values-customer.yaml` with your domain & auth configuration:

Configure your deployment settings including gateway, authentication, and image support:

```yaml theme={null}
kong-gateway:
  service:
    type: NodePort
    proxy:
      nodePort: 30080
    status:
      nodePort: 30081
  kong:
    domain: "user-provided"
    appSubdomain: "app" # Can be overridden by customer
    apiSubdomain: "api" # Can be overridden by customer
    realtimeSubdomain: "realtime" # Can be overridden by customer

helm-api-service:
  app:
    imagesSupport:
      enabled: false # Set to true to enable image storage and processing
      s3ImagesBucket: "" # S3 bucket name where images will be stored
      eksRegion: "" # AWS region where your EKS cluster and S3 bucket are located

customerConfig:
  propelauth:
    authURL: "traceloop-provided"
  launchDarkly:
    clientId: "" # OPTIONAL traceloop-provided

customerSecret:
  openai:
    key: "user-provided"
  launchDarkly:
    apiKey: "" # OPTIONAL traceloop-provided
  propelauth:
    verifierKey: "traceloop-provided"
    apiKey: "traceloop-provided"
  centrifugo:
    apiKey: "user-provided"
    tokenHmacSecret: "user-provided"
  encryptionSecret:
    apiKey: "user-provided"
```

#### 6. Install complete Traceloop stack

```bash theme={null}
helm upgrade --install traceloop . \
  -n traceloop \
  --values values.yaml \
  --values values-customer.yaml \
  --values values-internal-kafka.yaml \
  --values values-internal-clickhouse.yaml \
  --values values-internal-postgres.yaml \
  --values values-temporal.yaml \
  --values values-centrifugo.yaml \
  --create-namespace \
  --dependency-update
```

***

## Verification

1. Check all pods are running:

```bash theme={null}
kubectl get pods -n traceloop
```

2. Verify infrastructure connectivity:

```bash theme={null}
kubectl logs -n traceloop deployment/traceloop-api
```

3. Access the dashboard at your configured ingress host

## Troubleshooting

* Check our [troubleshooting guide](/self-host/troubleshooting)
* [Schedule support](https://calendly.com/d/cq42-93s-kcx)
* Join our [Slack community](https://traceloop.com/slack)


# Hybrid Deployment
Source: https://www.traceloop.com/docs/self-host/hybrid-deployment

Set up Traceloop with data sovereignty

The Hybrid deployment model allows you to maintain full control over your data storage while leveraging Traceloop's managed services for processing, monitoring, and observability.

## Architecture Overview

* **Your Infrastructure**: Hosts only the ClickHouse database for data storage
* **Traceloop Managed**: Handles processing pipelines, monitoring, and the dashboard
* **Data Flow**: Data is processed through Traceloop's infrastructure but stored only in your ClickHouse instance

## Setup Process

<Steps>
  <Step title="Deploy ClickHouse">
    Choose one of these deployment methods:

    #### Option A: Using CloudFormation/Terraform (Recommended)

    <Note>
      Contact Traceloop team for the CloudFormation template or Terraform
      configuration
    </Note>

    #### Option B: Using Helm on Kubernetes

    ```bash theme={null}
    # Add Altinity Helm repository
    helm repo add altinity https://altinity.github.io/kubernetes-blueprints-for-clickhouse
    helm repo update

    # Install ClickHouse
    helm install ch altinity/clickhouse \
      --namespace traceloop \
      --create-namespace \
      --values clickhouse-values.yaml
    ```

    Example `clickhouse-values.yaml`:

    ```yaml theme={null}
    clickhouse:
      persistence:
        enabled: true
        size: "100Gi"

      service:
        type: LoadBalancer

      defaultUser:
        # Make sure to change these values
        password: "your-secure-password"
        allowExternalAccess: true
    ```
  </Step>

  <Step title="Configure Network Access">
    Provide the following details to the Traceloop team:

    1. **ClickHouse Connection Details**:

       * Endpoint URL
       * Port number (default: 9000)
       * Database credentials

    2. **Network Security Requirements**:
       * IP ranges for whitelisting
       * VPC peering requirements (if applicable)

    We support multiple security configurations:

    * **IP Whitelisting**: Restrict access to specific IP ranges
    * **VPC Peering**: Secure private connection between your VPC and Traceloop's environment
    * **SSL/TLS**: Encrypted communication for all data in transit
    * **Custom Certificates**: Support for your own SSL certificates

    <Warning>
      Store your database credentials securely and rotate them periodically.
    </Warning>
  </Step>

  <Step title="Verify Setup">
    After setup, the Traceloop team will:

    1. Configure the connection to your ClickHouse instance
    2. Perform connectivity tests
    3. Validate data flow and storage
    4. Provide access to the Traceloop dashboard
  </Step>
</Steps>

## Need Help?

* [Schedule a support call](https://calendly.com/d/cq42-93s-kcx)
* Join our [community Slack](https://traceloop.com/slack)


# Self-Hosting Overview
Source: https://www.traceloop.com/docs/self-host/introduction

Learn about Traceloop's deployment options

Traceloop offers two deployment models tailored to meet diverse customer needs while maintaining robust support for generative AI application workflows.

<Info>
  Need help with self-hosting? [Schedule a
  meeting](https://calendly.com/d/cq42-93s-kcx) with our team, and we'll guide
  you through the process.
</Info>

## Deployment Options

### [Hybrid Deployment](/self-host/hybrid-deployment)

Perfect for organizations seeking to:

* Maintain control over data storage while outsourcing compute
* Minimize operational overhead
* Comply with data residency requirements
* Leverage Traceloop's managed services for processing and monitoring

**Key Components:**

* Processing Pipelines: Managed by Traceloop
* Dashboard: Hosted and managed by Traceloop
* Data Storage: Remains entirely on your infrastructure
* Metadata Storage: Managed by Traceloop
* Monitoring Models: Managed by Traceloop

### [Full Platform Self-Hosting](/self-host/full-deployment)

Ideal for organizations requiring:

* Complete control over all components
* Air-gapped environments
* Maximum security and compliance
* Custom infrastructure requirements

**Key Components:**

* Processing Pipelines: On your infrastructure
* Dashboard: Hosted by Traceloop
* Data Storage: Fully within your infrastructure
* Metadata Storage: Fully within your infrastructure
* Monitoring Models: Fully within your infrastructure

## Comparison

| Feature               | Hybrid Deployment       | Full Platform                |
| --------------------- | ----------------------- | ---------------------------- |
| Processing Pipelines  | Traceloop-managed       | Customer-managed             |
| Dashboard             | Traceloop-hosted        | Traceloop-hosted             |
| Data Storage          | Customer infrastructure | Customer infrastructure      |
| Metadata Storage      | Traceloop-managed       | Customer-managed             |
| Monitoring Models     | Traceloop-managed       | Customer-managed             |
| Data in Motion        | Handled by Traceloop    | Handled entirely by customer |
| Security              | Shared responsibility   | Fully customer-controlled    |
| Deployment Complexity | Lower                   | Higher                       |

## Next Steps

Choose your deployment model:

* [Get started with Hybrid Deployment](/self-host/hybrid-deployment)
* [Set up Full Platform Self-Hosting](/self-host/full-deployment)

<Note>
  Need assistance? We're here to help: - [Schedule a support
  call](https://calendly.com/d/cq42-93s-kcx) - Join our [community
  Slack](https://traceloop.com/slack)
</Note>


# Troubleshooting Guide
Source: https://www.traceloop.com/docs/self-host/troubleshooting

Solutions to common issues when self-hosting Traceloop

# Troubleshooting Guide

This guide helps you diagnose and resolve common issues you might encounter when self-hosting Traceloop.

<Info>
  Need immediate assistance? [Schedule a support
  call](https://calendly.com/d/cq42-93s-kcx) with our team.
</Info>

## Connection Issues

### ClickHouse Connection Failures

The Traceloop Helm chart expects specific configuration for external ClickHouse connections:

**Required Configuration:**

* Fill out `values-external-clickhouse.yaml` with your ClickHouse host, port, and connection details
* Ensure `traceloop-clickhouse-secret` exists with required credentials:
  * `CLICKHOUSE_USERNAME`
  * `CLICKHOUSE_PASSWORD`
  * **Note:** This secret is automatically created if using Traceloop Terraform, otherwise create it manually

```bash theme={null}
# Verify the ClickHouse secret exists
kubectl get secret traceloop-clickhouse-secret -n traceloop

# Check secret keys (without exposing values)
kubectl describe secret traceloop-clickhouse-secret -n traceloop
```

Common issues and their solutions when connecting to ClickHouse:

* Verify the host and port are correct
* Ensure the database exists and the user has appropriate permissions
* Check if SSL is required (`secure: true`)
* Verify network connectivity and firewall rules
* Ensure `traceloop-clickhouse-secret` contains correct credentials
* Verify `values-external-clickhouse.yaml` has correct host and configuration

### Kafka Connection Issues

The Traceloop Helm chart expects specific configuration for external Kafka connections:

**Required Configuration:**

* Fill out `values-external-kafka.yaml` with your Kafka broker addresses, connection details, and credentials
* Ensure the following Kafka topics exist: `traces`, `spans`, and `metrics`
  * **Note:** These topics are automatically created if using Traceloop Terraform, otherwise create them manually

```bash theme={null}
# Verify your Kafka configuration is properly applied
kubectl get configmap -n traceloop | grep kafka
```

If you're having trouble connecting to Kafka:

* Confirm broker addresses are accessible from the Kubernetes cluster
* Ensure required topics exist: `traces`, `spans`, and `metrics`
* For Confluent Cloud:
  * Ensure SASL authentication is properly configured
  * Verify SSL is enabled
* Check topic creation permissions
* Verify network policies allow Kafka connectivity
* Verify `values-external-kafka.yaml` has correct broker addresses, credentials, and configuration

### PostgreSQL Connection Problems

The Traceloop Helm chart expects specific configuration for external PostgreSQL connections:

**Required Configuration:**

* Fill out `values-external-postgres.yaml` with your PostgreSQL address and connection details
* Ensure `traceloop-postgres-secret` exists with required credentials:
  * `POSTGRES_DATABASE_USERNAME`
  * `POSTGRES_DATABASE_PASSWORD`
  * **Note:** This secret is automatically created if using Traceloop Terraform, otherwise create it manually

```bash theme={null}
# Verify the PostgreSQL secret exists
kubectl get secret traceloop-postgres-secret -n traceloop

# Check secret keys (without exposing values)
kubectl describe secret traceloop-postgres-secret -n traceloop
```

Common PostgreSQL connectivity issues:

* Verify database exists and is accessible
* Check user permissions (needs ability to create schemas and tables)
* For SSL connections, ensure proper SSL mode is set
* Verify PostgreSQL version compatibility (9.6 or higher)
* Ensure `traceloop-postgres-secret` contains correct credentials
* Verify `values-external-postgres.yaml` has correct database address and configuration

## Kubernetes Deployment Issues

### Pod Startup Failures

If pods aren't starting properly:

```bash theme={null}
# Check pod status
kubectl get pods -n traceloop

# Check pod events
kubectl describe pod -n traceloop <pod-name>

# Check pod logs
kubectl logs -n traceloop <pod-name>
```

Common solutions:

* Verify resource requests and limits are appropriate
* Ensure all secrets are properly created
* Check container image pull permissions

### Ingress Issues

**Our Ingress Architecture:**
Traceloop uses a custom ingress setup rather than traditional Kubernetes ingress controllers.
A load balancer handles SSL termination and forwards HTTP traffic directly to port 30800 on the Kubernetes cluster.
This port maps to a Kong gateway pod, which serves as the unified ingress point for all HTTP endpoints.

If you can't access Traceloop through your load balancer:

**Load Balancer Configuration:**

* Verify the load balancer is properly provisioned
* Check DNS records point to the correct load balancer endpoint
* Verify SSL certificate is properly attached to load balancer for HTTPS termination
* Ensure security groups allow traffic from load balancer to Kubernetes cluster on port 30800
* Check load balancer target group health - targets should be healthy on port 30800

**Kong Gateway Pod Health:**

* Verify Kong gateway pod is running and healthy
* Check that Kong is listening on the correct port (default mapped to 30800)
* Ensure Kong domain configuration is correct in `values-customer.yaml` - verify `kong-gateway.kong.domain` is properly filled

```bash theme={null}
# Check Kong gateway pod status
kubectl get pods -n traceloop | grep kong

# Check Kong pod logs
kubectl logs -n traceloop -l app=kong

# Verify port mapping and service
kubectl get svc -n traceloop
```

### Image Pull Failures

Traceloop images are stored on Docker Hub and require authentication. A `regcred` secret is provided by Traceloop and must be manually created in the traceloop namespace.

**Setup Requirements:**

* Create the `regcred` secret in the traceloop namespace using credentials provided by Traceloop
* Ensure the secret is properly referenced in your Helm values

```bash theme={null}
# Verify the regcred secret exists
kubectl get secret regcred -n traceloop

# Check secret details (without exposing credentials)
kubectl describe secret regcred -n traceloop
```

**Common Issues:**

* `regcred` secret not created in the traceloop namespace
* Incorrect Docker Hub credentials in the secret
* Secret not properly referenced in pod specifications
* Network connectivity issues to Docker Hub

## Common Error Messages

### "Error: connection refused"

Check component connectivity:

```bash theme={null}
# Test ClickHouse connectivity
kubectl exec -it -n traceloop deploy/traceloop-api -- nc -vz your-clickhouse-host 9000

# Test Kafka connectivity
kubectl exec -it -n traceloop deploy/traceloop-api -- nc -vz your-kafka-broker 9092

# Test PostgreSQL connectivity
kubectl exec -it -n traceloop deploy/traceloop-api -- nc -vz your-postgres-host 5432
```

### "Error: authentication failed"

Traceloop uses PropelAuth as the authentication provider. Ensure proper configuration:

**Required Configuration:**

* Fill out `values-customer.yaml` with PropelAuth settings:
  ```yaml theme={null}
  customerConfig:
    propelauth:
      authURL: "traceloop-provided"

  customerSecret:
    propelauth:
      verifierKey: "traceloop-provided"
      apiKey: "traceloop-provided"
  ```

Authentication issues:

* Ensure service accounts have necessary permissions
* Verify SSL/TLS configuration if required
* Ensure PropelAuth configuration is correct in `values-customer.yaml`
* Verify PropelAuth secrets contain the correct keys provided by Traceloop

### "Error: insufficient permissions"

Permission-related problems:

* Check RBAC configuration
* Verify service account permissions
* Ensure necessary Kubernetes roles are created
* Check database user permissions

## Quick Validation Checklist

1. Component Connectivity

   * All infrastructure components are reachable
   * Proper ports are open
   * Network policies allow required traffic

2. Authentication & Permissions

   * Database credentials are correct
   * Kubernetes secrets exist and are mounted
   * Service accounts have required permissions

3. Infrastructure Health

   * Kubernetes nodes are healthy
   * Sufficient resources are available
   * Storage is properly configured

4. Logging & Monitoring
   * Check pod logs: `kubectl logs -n traceloop -l app=traceloop`
   * Monitor resource usage
   * Review infrastructure metrics

<Note>
  Still having issues? We're here to help: - [Schedule a support
  call](https://calendly.com/d/cq42-93s-kcx) for personalized assistance - Join
  our [community Slack](https://traceloop.com/slack) for discussions and updates
</Note>


# Managing API Keys
Source: https://www.traceloop.com/docs/settings/managing-api-keys

Generate and manage API keys for sending traces and accessing Traceloop features

API keys are required to authenticate your application with Traceloop. Each API key is tied to a specific project and environment combination, determining where your traces and data will appear.

<Frame>
  <img />

  <img />
</Frame>

## Quick Start: Generate Your First API Key

<Steps>
  <Step title="Navigate to Settings">
    Go to [Settings → Organization](https://app.traceloop.com/settings/api-keys) in your Traceloop dashboard.
  </Step>

  <Step title="Select Your Project">
    Click on the project where you want to generate an API key (e.g., "Default project").

    If you haven't created a project yet, see [Projects and Environments](/settings/projects-and-environments).
  </Step>

  <Step title="Generate API Key for an Environment">
    Find the environment you want to use (dev, stg, or prd) and click **Generate API key**.

    <Warning>
      **Copy the API key immediately!** The full key is only shown once and cannot be retrieved later.
      After you close or reload the page, you'll need to revoke and generate a new key if you lose it.
    </Warning>

    The key will be displayed partially masked, but you can copy the full key using the copy button.
  </Step>

  <Step title="Set as Environment Variable">
    Export the API key in your application:

    ```bash theme={null}
    export TRACELOOP_API_KEY=your_api_key_here
    ```

    Or set it in your `.env` file:

    ```bash theme={null}
    TRACELOOP_API_KEY=your_api_key_here
    ```
  </Step>
</Steps>

Done! Your application can now send traces and access Traceloop features.

## Understanding API Keys

### How API Keys Work

Each API key is scoped to a specific **project + environment** combination:

* **Project**: Isolates data for different applications or teams (e.g., "orders-service", "users-service")
* **Environment**: Separates deployment stages (dev, stg, prd)

When you use an API key, Traceloop automatically knows where to save your data based on the key itself.

<Note>
  If the `TRACELOOP_API_KEY` environment variable is set, the SDK will automatically use it. You don't need to pass it explicitly in your code.
</Note>

**Example:**

* API key from "web-app" → "dev" sends traces to the "web-app" project's dev environment
* API key from "api-service" → "prd" sends traces to the "api-service" project's prd environment

### Viewing Your Data

To see your traces in the dashboard:

1. Select the correct **project** from the project dropdown
2. Filter by **environment** if needed

<Tip>
  **Not seeing your traces?** Make sure you're viewing the same project and environment
  that matches your API key.
</Tip>

## Common Scenarios

### Local Development

Use your dev environment API key:

```bash theme={null}
# In your .env or shell
export TRACELOOP_API_KEY=your_development_key
```

### CI/CD Pipeline

Use stg or prd keys in your deployment configuration:

```yaml theme={null}
# Example: GitHub Actions
env:
  TRACELOOP_API_KEY: ${{ secrets.TRACELOOP_STG_KEY }}
```

```yaml theme={null}
# Example: Docker Compose
environment:
  - TRACELOOP_API_KEY=${TRACELOOP_PRD_KEY}
```

### Multiple Projects from One Application

If you need to send data to different projects from the same codebase, pass the API key directly in code instead of using environment variables:

<CodeGroup>
  ```python Python theme={null}
  from traceloop.sdk import Traceloop

  # Initialize with specific API key
  Traceloop.init(api_key="your_project_specific_key")
  ```

  ```javascript TypeScript / JavaScript theme={null}
  import * as traceloop from "@traceloop/node-server-sdk";

  // Initialize with specific API key
  traceloop.initialize({
    apiKey: "your_project_specific_key"
  });
  ```

  ```go Go theme={null}
  import "github.com/traceloop/go-sdk/traceloop"

  // Initialize with specific API key
  traceloop.Init(traceloop.Config{
    APIKey: "your_project_specific_key",
  })
  ```
</CodeGroup>

## Managing Your API Keys

### Revoking an API Key

If your API key is compromised or you need to rotate keys:

1. Go to Settings → Organization → Select your project
2. Find the environment with the key you want to revoke
3. Click **Revoke API key**
4. Generate a new key immediately
5. Update your application configuration with the new key

<Warning>
  Revoking a key immediately stops all applications using it from sending data.
  Make sure to update your configuration before revoking production keys.
</Warning>

### Lost Your API Key?

If you lose your API key and didn't save it:

1. You **cannot** retrieve the original key
2. You must **revoke** the old key and **generate** a new one
3. Update your application with the new key

This is a security feature - API keys are never stored in retrievable form.

### Best Practices

<CardGroup>
  <Card title="Use Secret Management" icon="key">
    Store API keys in secret management systems like AWS Secrets Manager, Azure Key Vault,
    HashiCorp Vault, or 1Password instead of hardcoding them.
  </Card>

  <Card title="Rotate Keys Regularly" icon="rotate">
    Periodically rotate your API keys, especially for production environments.
    Schedule key rotation as part of your security practices.
  </Card>

  <Card title="Separate Keys Per Environment" icon="layer-group">
    Never use prd API keys in dev or stg.
    This prevents accidental data mixing and security risks.
  </Card>

  <Card title="Limit Key Exposure" icon="eye-slash">
    Don't commit API keys to version control. Use environment variables
    or secret management systems instead.
  </Card>
</CardGroup>

## Troubleshooting

### Authentication Failed

**Problem:** Getting authentication errors when initializing the SDK.

**Solutions:**

* Verify the API key is correctly set as `TRACELOOP_API_KEY`
* Check if the key has been revoked (generate a new one if needed)
* Ensure there are no extra spaces or characters in the key

### Not Seeing Traces

**Problem:** Application runs but traces don't appear in dashboard.

**Solutions:**

* Confirm you're viewing the correct **project** in the dashboard dropdown
* Check you're filtering by the correct **environment**
* Verify the API key matches the project + environment you're viewing
* Check SDK initialization logs for connection errors

### Wrong Data Appearing

**Problem:** Seeing unexpected traces or data in your project.

**Solutions:**

* Double-check which API key you're using (`echo $TRACELOOP_API_KEY`)
* Verify the API key belongs to the intended project + environment
* Check if other team members are using the same project

### Multiple Applications Sending to Same Project

**Problem:** Want to separate data from different services but they're in the same project.

**Solutions:**

* Create a separate project for each application/service
* Generate unique API keys for each project
* See [Projects and Environments](/settings/projects-and-environments) for more details

## Related Resources

<CardGroup>
  <Card title="Projects and Environments" icon="folder-tree" href="/settings/projects-and-environments">
    Learn about organizing your applications and deployment stages
  </Card>

  <Card title="Getting Started" icon="rocket" href="/openllmetry/getting-started-python">
    Set up OpenLLMetry SDK with your API key
  </Card>

  <Card title="Dashboard API" icon="webhook" href="/api-reference/introduction">
    Use API keys to access Traceloop's REST API
  </Card>

  <Card title="Self-Hosting" icon="server" href="/self-host/introduction">
    Configure API keys in self-hosted deployments
  </Card>
</CardGroup>


# Projects and Environments
Source: https://www.traceloop.com/docs/settings/projects-and-environments

Organize your applications and deployment stages with Projects and Environments

Projects and Environments help you keep your LLM observability data organized and isolated across different applications, services, and deployment stages.

<Frame>
  <img />

  <img />
</Frame>

## Why Projects and Environments?

### The Problem

When you have multiple applications or deployment stages:

* Traces from different services get mixed together
* Production data appears alongside development experiments
* Team members see irrelevant data from other projects
* Testing changes risks affecting production monitoring

### The Solution

**Projects** completely isolate data for different applications:

* Each project has its own traces, datasets, prompts, evaluators, and experiments
* Switch between projects to view specific application data
* Generate separate API keys per project

**Environments** separate deployment stages within a project:

* dev, stg, and prd environments (built-in)
* Custom environments (e.g., "qa", "eu-prd", "preview")
* Each environment has its own API key and data stream

## Understanding Projects

### What is a Project?

A project is a complete isolation boundary for all your Traceloop data. Think of it as a workspace for a specific application or service.

**Each project contains:**

* Traces and spans
* Datasets for experiments
* Prompt configurations
* Evaluators and monitors
* Experiment results

**Common use cases for creating projects:**

* Separate applications (e.g., "web-app", "mobile-app", "api-service")
* Microservices in a distributed system
* Different teams or product areas
* Major feature branches or product lines

### When to Create a New Project

✅ **Create a new project when:**

* Building a new application or service
* Separating data for different teams
* Testing major architectural changes in isolation
* Managing multi-tenant applications (one project per tenant)

❌ **Don't create a new project for:**

* Different deployment stages (use environments instead)
* Temporary experiments (use Development environment)
* A/B tests (use datasets and experiments features)

## Understanding Environments

### What is an Environment?

An environment represents a deployment stage within a project. Each environment has its own API key, allowing you to send traces from different stages without mixing the data.

**Default environments** (cannot be deleted):

* **dev**: Local development and testing
* **stg**: Pre-production testing and validation
* **prd**: Live production traffic

**Custom environments**: Add your own based on your workflow

* Examples: "qa", "uat", "preview", "eu-prd", "us-prd"

### Organization-Level vs. Project-Level Environments

Traceloop supports two types of environments:

**Organization-Level Environments**

* Created at the organization settings level
* Automatically cascade to **all projects** (existing and new)
* Use this for environments that apply across your entire organization

**Project-Specific Environments**

* Created within a single project
* Only appear in that specific project
* Use this for project-specific deployment stages

<Tip>
  **Best practice:** Create organization-level environments for company-wide deployment stages
  (dev, stg, prd, qa). Create project-specific environments only when needed
  for unique deployment scenarios.
</Tip>

### How Environment Cascading Works

When you create an organization-level environment:

1. It immediately appears in all existing projects
2. It automatically appears in any new projects you create
3. Each project can independently generate API keys for that environment

**Example:**

```
Organization creates "QA" environment
  ↓
Appears in "web-app" project (can generate its own QA API key)
Appears in "api-service" project (can generate its own QA API key)
Appears in "mobile-app" project (can generate its own QA API key)
```

## Setting Up Projects and Environments

<Steps>
  <Step title="Navigate to Settings">
    Go to **Settings** in your Traceloop dashboard, then select the **Organization** tab.

    You'll see two sections:

    * **Projects and API keys**: Manage your projects
    * **Organization environments**: Manage org-wide environments
  </Step>

  <Step title="Create a Project (Optional)">
    If you need a new project:

    1. Click the **+** button next to "Projects and API keys"
    2. Enter a descriptive name (e.g., "web-app", "payment-service", "mobile-app")
    3. Click **Create**

    The project is created instantly with all organization-level environments included.

    <Note>
      A "Default project" is created automatically when you sign up.
      You can rename or delete it if needed.
    </Note>
  </Step>

  <Step title="Create Custom Environments (Optional)">
    If you need additional environments beyond dev, stg, and prd:

    **For organization-wide environments:**

    1. Click the **+** button next to "Organization environments"
    2. Enter an environment name (e.g., "qa", "preview", "eu-prd")
    3. Click **Create**
    4. The environment appears in all projects immediately

    **For project-specific environments:**

    1. Click on your project
    2. Click the **+** button next to "Project environments"
    3. Enter an environment name
    4. Click **Create**
    5. The environment appears only in this project

    <Tip>
      An environment **slug** is automatically created for SDK usage. For example,
      "EU Production" becomes "eu-production" as the slug. The default environments
      use "dev", "stg", and "prd" as their slugs.
    </Tip>
  </Step>

  <Step title="Generate API Keys">
    API keys are generated per project + environment:

    1. Click on your project
    2. Find the environment you want to use
    3. Click **Generate API key**
    4. Copy the key immediately (it won't be shown again)
    5. Use it in your application as `TRACELOOP_API_KEY`

    See [Managing API Keys](/settings/managing-api-keys) for detailed instructions.
  </Step>
</Steps>

## Viewing Your Data

### Switching Between Projects

The Traceloop dashboard shows **one project at a time**. To switch projects:

1. Click the project dropdown from the main menu on the left-hand side of the dashboard
2. Select the project you want to view
3. All traces, datasets, and other data will update to show only that project

<Note>
  You cannot view multiple projects simultaneously. This is by design to maintain
  clear data isolation and prevent confusion.
</Note>

### Filtering by Environment

Within a project, you can filter data by environment:

1. Select your project from the dropdown
2. Use the environment filter to show only specific environments
3. This filters traces, monitors, and other real-time data by environment

## Managing Projects and Environments

### Renaming

**Projects**: Can be renamed at any time

* Click on the project → Settings → Rename

**Environments**: Cannot be renamed

* Delete and recreate if needed (see warnings below)

### Deleting Projects

<Warning>
  **Deleting a project is permanent and irreversible.**

  When you delete a project:

  * All traces and spans are permanently deleted
  * All datasets and their versions are lost
  * All prompts, evaluators, and experiments are removed
  * All API keys for that project are revoked

  **There is no way to recover this data.**
</Warning>

To delete a project:

1. Open the app settings
2. Find the project you want to delete
3. Click the 3-dot menu
4. Click **Delete project**
5. Confirm the deletion

### Deleting Environments

<Warning>
  **Deleting an environment is permanent and irreversible.**

  When you delete an environment:

  * All traces for that environment are permanently deleted
  * The API key is revoked immediately
  * Applications using that key will stop sending data

  **There is no way to recover this data.**
</Warning>

To delete an environment:

1. Open the app settings
2. Find the environment you want to delete
3. Click the 3-dot menu
4. Click **Delete environment**
5. Confirm the deletion

**Organization-level environments:**

* Cannot delete the three default environments (dev, stg, prd)
* Can delete custom organization-level environments
* Deleting removes the environment from all projects

**Project-specific environments:**

* Can delete any project-specific environment
* Only affects that specific project

### Limitations and Permissions

**Current limitations:**

* ❌ Cannot move or copy data between projects
* ❌ Cannot merge projects
* ❌ Cannot transfer datasets or prompts between projects
* ❌ No per-project access control (everyone in the organization can see all projects)

**What you can do:**

* ✅ Create unlimited projects and environments
* ✅ Rename projects (but not environments)
* ✅ Everyone in your organization can manage all projects and API keys

## Best Practices

### Project Organization

<CardGroup>
  <Card title="By Application" icon="layer-group">
    Create one project per application or major service.

    **Example:**

    * "web-app" (frontend)
    * "api-gateway" (backend)
    * "auth-service" (microservice)
  </Card>

  <Card title="By Team" icon="users">
    Create projects based on team ownership.

    **Example:**

    * "checkout-team"
    * "recommendations-team"
    * "infrastructure-team"
  </Card>

  <Card title="By Product Line" icon="box">
    Separate different products or customer segments.

    **Example:**

    * "consumer-app"
    * "enterprise-app"
    * "internal-tools"
  </Card>

  <Card title="By Environment Type" icon="globe">
    For complex deployments with regional separation.

    **Example:**

    * "app-us-production"
    * "app-eu-production"
    * "app-asia-production"
  </Card>
</CardGroup>

### Environment Strategy

**Use built-in environments for standard workflows:**

```
dev  → Local development and unit testing
stg  → Integration testing and QA
prd  → Live customer traffic
```

**Add custom environments for special cases:**

```
qa       → Dedicated QA team testing
preview  → Preview deployments for each PR
canary   → Canary deployments before full rollout
eu-prd   → Regional production environments
```

### Naming Conventions

**Projects:**

* Use descriptive, lowercase names with hyphens
* Include the service or application name
* Examples: `payment-api`, `mobile-app`, `ml-inference`

**Environments:**

* Keep names short and clear
* Use standard terms when possible
* Examples: `dev`, `stg`, `prd`, `qa`, `preview`

## Common Scenarios

### Microservices Architecture

Create one project per microservice:

```
Projects:
├── api-gateway (dev, stg, prd environments)
├── auth-service (dev, stg, prd environments)
├── payment-service (dev, stg, prd environments)
└── notification-service (dev, stg, prd environments)
```

Each service has its own API keys per environment, keeping traces completely isolated.

### Monorepo with Multiple Apps

Create projects per deployable application:

```
Projects:
├── web-frontend (dev, stg, prd)
├── mobile-backend (dev, stg, prd)
└── admin-dashboard (dev, stg, prd)
```

### Multi-Region Deployment

Option 1: Use custom environments per region within one project:

```
Project: global-app
Environments:
├── dev
├── stg
├── us-prd
├── eu-prd
└── apac-prd
```

Option 2: Use separate projects per region:

```
Projects:
├── app-us (dev, stg, prd)
├── app-eu (dev, stg, prd)
└── app-apac (dev, stg, prd)
```

## Troubleshooting

### Can't See My Project in Dashboard

**Problem:** Created a project but it doesn't appear in the dropdown.

**Solutions:**

* Refresh the page
* Check if you're logged into the correct organization
* Verify the project wasn't deleted

### Data Appearing in Wrong Project

**Problem:** Traces showing up in unexpected project.

**Solutions:**

* Verify which API key you're using: `echo $TRACELOOP_API_KEY`
* Check which project + environment the API key belongs to
* Ensure you haven't accidentally used the wrong key in your configuration

### Need to Move Data Between Projects

**Problem:** Want to transfer datasets or traces to a different project.

**Solution:**

* Data cannot be moved between projects (this is a security/isolation feature)
* For datasets: Export as CSV and import into the new project
* For traces: Cannot be transferred (must regenerate in new project)

### Accidentally Deleted Environment

**Problem:** Deleted an environment and lost data.

**Solution:**

* Unfortunately, there is no way to recover deleted data
* Prevention: Always confirm before deleting
* Best practice: Back up critical datasets regularly

## Related Resources

<CardGroup>
  <Card title="Managing API Keys" icon="key" href="/settings/managing-api-keys">
    Learn how to generate and manage API keys for your projects
  </Card>

  <Card title="Getting Started" icon="rocket" href="/openllmetry/getting-started-python">
    Set up your first project and start sending traces
  </Card>

  <Card title="Datasets" icon="table" href="/datasets/quick-start">
    Create datasets within your projects for experiments
  </Card>

  <Card title="Prompts" icon="message" href="/prompts/quick-start">
    Manage prompts within projects and deploy to environments
  </Card>
</CardGroup>


