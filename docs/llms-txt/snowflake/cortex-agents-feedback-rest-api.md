# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-feedback-rest-api.md

# Feedback REST API

Use this API to collect feedback about Cortex Agents from end users.

## Collect feedback about a Cortex Agent

`POST /api/v2/databases/{database}/schemas/{schema}/agents/{name}:feedback`

Creates a feedback event for a Cortex Agent response.

### Request

#### Path parameters

| Parameter | Description |
| --- | --- |
| `database` | (Required) Identifier for the database to which the resource belongs. You can use the /api/v2/databases GET request to get a list of available databases. |
| `schema` | (Required) Identifier for the schema to which the resource belongs. You can use the /api/v2/databases/{database}/schemas GET request to get a list of available schemas for the specified database. |
| `name` | (Required) Identifier for the agent. |

#### Request headers

| Header | Description |
| --- | --- |
| `Authorization` | (Required) Authorization token. For more information, see [Authentication](cortex-agents.md). |
| `Content-Type` | (Required) application/json |

#### Request body

The request body contains the feedback details for the agent response.

| Field | Type | Description |
| --- | --- | --- |
| `orig_request_id` | string | Request ID for the message associated with the feedback. If this value is not set, then feedback is logged for the agent. |
| `positive` | boolean | Whether the response was good (`true`) or bad (`false`). |
| `feedback_message` | string | The text for the detailed feedback message. |
| `categories` | array of strings | List of categories for the feedback. Each category is a string that represents a specific category of feedback. |
| `thread_id` | integer | The id of the thread. |

#### Example request body for agent-level feedback

```json
{
  "categories": [
    "Something worked well"
  ],
  "feedback_message": "this is fantastic!",
  "positive": true
}
```

#### Example request body for request-level feedback

```json
{
  "orig_request_id": "aa123456-789a-a1-2a34-a1a234a56789",
  "categories": [
    "Something worked well"
  ],
  "feedback_message": "this is fantastic!",
  "positive": true
}
```

### Response

A successful response returns a confirmation message.

#### Response headers

| Header | Description |
| --- | --- |
| `X-Snowflake-Request-ID` | Unique ID of the API request. |

#### Response body

```json
{
  "status": "Feedback submitted successfully"
}
```

## View feedback for Cortex Agents

For information about required privileges and how to query feedback events (including example SQL), see [View feedback provided by users](cortex-agents-monitor.md).
