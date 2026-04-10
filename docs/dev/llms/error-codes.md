# Source: https://dev.writer.com/api-reference/error-codes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understand error codes

This page provides a comprehensive reference for all error codes, HTTP status codes, and error handling patterns used across Writer APIs.

## Error code reference

<Tip>
  **Quickstart**: Most issues fall into these categories. Check here first!
</Tip>

<CardGroup cols={2}>
  <Card title="Authentication Issues" icon="shield-check" color="#ef4444">
    **401 Unauthorized**: check your API key format and permissions
  </Card>

  <Card title="Bad Request Data" icon="triangle-exclamation" color="#f59e0b">
    **400 + validation\_error**: verify required fields and data types
  </Card>

  <Card title="Rate Limiting" icon="clock" color="#8b5cf6">
    **429 Too Many Requests**: implement exponential backoff
  </Card>

  <Card title="Server Problems" icon="server" color="#6b7280">
    **5xx Errors**: check our status page or retry your request
  </Card>
</CardGroup>

## Error types

Jump to specific error types to find the cause and suggested action:

* [Authentication and authorization errors](#authentication-and-authorization-errors)
* [Request validation errors](#request-validation-errors)
* [Rate limiting and quota errors](#rate-limiting-and-quota-errors)
* [Server and processing errors](#server-and-processing-errors)
* [Error codes by service](#error-codes-by-service)

## Error response format

All API endpoints return errors in a consistent JSON format:

```json  theme={null}
{
  "tpe": "error_type",
  "errors": [
    {
      "description": "Human-readable error description",
      "key": "error.message.key",
      "extras": {}
    }
  ],
  "extras": {}
}
```

### Response structure

<Accordion title="🔧 Core fields (always present)">
  | Field    | Type   | Description                                                       |
  | -------- | ------ | ----------------------------------------------------------------- |
  | `tpe`    | string | Error type identifier (for example, "BadRequest", "Unauthorized") |
  | `errors` | array  | Array of error messages with details                              |
  | `extras` | object | Additional error context and metadata                             |
</Accordion>

<Accordion title="📋 Error message details">
  | Field         | Type   | Description                                     |
  | ------------- | ------ | ----------------------------------------------- |
  | `description` | string | Human-readable error description for developers |
  | `key`         | string | Message key for internationalization            |
  | `extras`      | object | Additional context specific to the error        |
</Accordion>

## HTTP status codes

Writer APIs use standard HTTP status codes to indicate the nature of errors:

| Status | Error code            | Type           | Description                                          | Common causes                           |
| ------ | --------------------- | -------------- | ---------------------------------------------------- | --------------------------------------- |
| 400    | `BadRequest`          | Validation     | Invalid request parameters or malformed request body | Missing required fields, invalid format |
| 401    | `Unauthorized`        | Authentication | Missing or invalid authentication credentials        | Missing API key, invalid format         |
| 403    | `Forbidden`           | Authorization  | Valid credentials but insufficient permissions       | Insufficient access rights              |
| 404    | `NotFound`            | Validation     | Requested resource does not exist                    | Invalid resource ID, deleted resource   |
| 409    | `Conflict`            | Validation     | Request conflicts with current state                 | Duplicate resource, version conflict    |
| 410    | `Gone`                | Validation     | Resource was permanently removed                     | Deleted/expired resource                |
| 413    | `PayloadTooLarge`     | Validation     | Request body too large                               | Exceeds configured size limits          |
| 422    | `UnprocessableEntity` | Validation     | Semantically invalid request                         | Fails business rules/constraints        |
| 429    | `TooManyRequests`     | Rate Limiting  | Rate limit or quota exceeded                         | Too many requests per time period       |
| 500    | `InternalServerError` | Server         | Internal server error                                | Server-side processing issue            |
| 503    | `ServiceUnavailable`  | Server         | Service temporarily unavailable                      | Maintenance, high load                  |
| 507    | `InsufficientStorage` | Server         | Insufficient storage to complete request             | Storage quota exhausted                 |

## Error codes by service

This section provides a comprehensive reference of all possible error codes organized by service and endpoint.

<AccordionGroup>
  <Accordion title="Chat Completions API" icon="comments">
    ### Text generation

    **Endpoint:** `POST /v1/completion`

    | Error Type                        | HTTP Status | Description              | Possible Causes                                          |
    | --------------------------------- | ----------- | ------------------------ | -------------------------------------------------------- |
    | `BadRequest`                      | 400         | Invalid model parameter  | Model name not supported or malformed                    |
    | `InvalidInputParameters`          | 400         | Invalid prompt format    | Empty prompt or invalid encoding                         |
    | `InvalidContentType`              | 400         | Invalid parameters       | Invalid `temperature`, `max_tokens`, or other parameters |
    | `BadCredentials`                  | 401         | Invalid API key          | Missing or malformed API key                             |
    | `BadToken`                        | 401         | API key expired          | API key has expired                                      |
    | `InsufficientAccessRights`        | 403         | Insufficient permissions | API key lacks required permissions                       |
    | `QuotaExceeded`                   | 429         | Rate limit exceeded      | Too many requests per minute                             |
    | `CompletionModelQuotaError`       | 429         | Quota exceeded           | Monthly usage limit reached                              |
    | `CompletionModelUnavailableError` | 500         | Model unavailable        | AI model temporarily unavailable                         |
    | `CompletionModelInternalError`    | 500         | Service overloaded       | High load, retry with backoff                            |

    ### Chat completions

    **Endpoint:** `POST /v1/chat/completions`

    | Error Type                          | HTTP Status | Description                   | Possible Causes                         |
    | ----------------------------------- | ----------- | ----------------------------- | --------------------------------------- |
    | `BadRequest`                        | 400         | Invalid messages format       | Malformed messages array or role        |
    | `InvalidInputParameters`            | 400         | Invalid model parameter       | Model not supported for chat            |
    | `InvalidContentType`                | 400         | Invalid tool configuration    | Malformed tools or `tool_choice`        |
    | `BadRequest`                        | 400         | Invalid streaming parameters  | Invalid stream or `stream_options`      |
    | `CompletionModelUnsafeRequestError` | 400         | Content policy violation      | Request contains prohibited content     |
    | `BadCredentials`                    | 401         | Authentication failed         | Invalid or missing API key              |
    | `BadToken`                          | 401         | Authentication failed         | Invalid or missing API key              |
    | `InsufficientAccessRights`          | 403         | Model access denied           | Account lacks access to requested model |
    | `QuotaExceeded`                     | 429         | Rate limit exceeded           | Too many requests per minute            |
    | `CompletionModelQuotaError`         | 429         | Model quota exceeded          | Model-specific usage limit reached      |
    | `CompletionModelInternalError`      | 500         | Model processing error        | Internal error in model inference       |
    | `CompletionModelUnavailableError`   | 503         | Model temporarily unavailable | Model service is down for maintenance   |
  </Accordion>

  <Accordion title="Files API" icon="file">
    ### Upload files

    **Endpoint:** `POST /v1/files`

    | Error Type                 | HTTP Status | Description                | Possible Causes                       |
    | -------------------------- | ----------- | -------------------------- | ------------------------------------- |
    | `BadRequest`               | 400         | Invalid file format        | Unsupported file type                 |
    | `InvalidInputParameters`   | 400         | File too large             | File exceeds size limit               |
    | `InvalidContentType`       | 400         | Invalid file content       | Corrupted or malformed file           |
    | `BadCredentials`           | 401         | Authentication required    | Missing or invalid API key            |
    | `BadToken`                 | 401         | Authentication required    | Missing or invalid API key            |
    | `InsufficientAccessRights` | 403         | Upload permission denied   | Account lacks file upload permissions |
    | `BadRequest`               | 413         | Payload too large          | Request body exceeds size limit       |
    | `QuotaExceeded`            | 429         | Upload rate limit exceeded | Too many file uploads per minute      |
    | `InternalError`            | 500         | File processing error      | Error processing uploaded file        |
    | `QuotaExceeded`            | 507         | Storage quota exceeded     | Account storage limit reached         |

    ### Get file

    **Endpoint:** `GET /v1/files/{file_id}`

    | Error Type                 | HTTP Status | Description             | Possible Causes                   |
    | -------------------------- | ----------- | ----------------------- | --------------------------------- |
    | `BadCredentials`           | 401         | Authentication required | Missing or invalid API key        |
    | `BadToken`                 | 401         | Authentication required | Missing or invalid API key        |
    | `InsufficientAccessRights` | 403         | Access denied           | No permission to access this file |
    | `ResourceNotFound`         | 404         | File not found          | File ID doesn't exist             |
    | `ResourceNotFound`         | 410         | File gone               | File has been deleted or expired  |
  </Accordion>

  <Accordion title="Knowledge Graphs API" icon="brain">
    ### Create graph

    **Endpoint:** `POST /v1/knowledge-graphs`

    | Error Type                 | HTTP Status | Description                 | Possible Causes                          |
    | -------------------------- | ----------- | --------------------------- | ---------------------------------------- |
    | `BadRequest`               | 400         | Invalid graph configuration | Malformed graph parameters               |
    | `InvalidInputParameters`   | 400         | Invalid graph name          | Name contains invalid characters         |
    | `BadRequest`               | 400         | Duplicate graph name        | Graph with this name already exists      |
    | `BadCredentials`           | 401         | Authentication required     | Missing or invalid API key               |
    | `BadToken`                 | 401         | Authentication required     | Missing or invalid API key               |
    | `InsufficientAccessRights` | 403         | Graph creation denied       | Account lacks graph creation permissions |
    | `QuotaExceeded`            | 429         | Graph creation rate limit   | Too many graphs created per hour         |
    | `InternalError`            | 500         | Graph creation failed       | Internal error creating graph            |

    ### Add file to graph

    **Endpoint:** `POST /v1/knowledge-graphs/{graph_id}/files`

    | Error Type                 | HTTP Status | Description                | Possible Causes                       |
    | -------------------------- | ----------- | -------------------------- | ------------------------------------- |
    | `BadRequest`               | 400         | Invalid file format        | File type not supported for graphs    |
    | `InvalidInputParameters`   | 400         | File processing failed     | Error parsing file content            |
    | `BadCredentials`           | 401         | Authentication required    | Missing or invalid API key            |
    | `BadToken`                 | 401         | Authentication required    | Missing or invalid API key            |
    | `InsufficientAccessRights` | 403         | Graph access denied        | No permission to modify this graph    |
    | `ResourceNotFound`         | 404         | Graph not found            | Graph ID does not exist               |
    | `BadRequest`               | 409         | File already in graph      | File is already associated with graph |
    | `QuotaExceeded`            | 429         | File processing rate limit | Too many files processed per minute   |

    ### Query graph

    **Endpoint:** `POST /v1/knowledge-graphs/{graph_id}/query`

    | Error Type                 | HTTP Status | Description               | Possible Causes                   |
    | -------------------------- | ----------- | ------------------------- | --------------------------------- |
    | `BadRequest`               | 400         | Invalid query format      | Malformed query parameters        |
    | `InvalidInputParameters`   | 400         | Query too complex         | Query exceeds complexity limits   |
    | `BadCredentials`           | 401         | Authentication required   | Missing or invalid API key        |
    | `BadToken`                 | 401         | Authentication required   | Missing or invalid API key        |
    | `InsufficientAccessRights` | 403         | Query permission denied   | No permission to query this graph |
    | `ResourceNotFound`         | 404         | Graph not found           | Graph ID doesn't exist            |
    | `QuotaExceeded`            | 429         | Query rate limit exceeded | Too many queries per minute       |
    | `InternalError`            | 500         | Query processing error    | Internal error processing query   |
  </Accordion>

  <Accordion title="Applications API" icon="gear">
    ### Create application

    **Endpoint:** `POST /v1/applications`

    | Error Type                 | HTTP Status | Description                       | Possible Causes                                |
    | -------------------------- | ----------- | --------------------------------- | ---------------------------------------------- |
    | `BadRequest`               | 400         | Invalid application configuration | Malformed application parameters               |
    | `InvalidInputParameters`   | 400         | Invalid blueprint configuration   | Blueprint syntax or configuration error        |
    | `BadRequest`               | 400         | Duplicate application name        | Application with this name already exists      |
    | `BadCredentials`           | 401         | Authentication required           | Missing or invalid API key                     |
    | `BadToken`                 | 401         | Authentication required           | Missing or invalid API key                     |
    | `InsufficientAccessRights` | 403         | Application creation denied       | Account lacks application creation permissions |
    | `QuotaExceeded`            | 429         | Application creation rate limit   | Too many applications created per hour         |
    | `InternalError`            | 500         | Application creation failed       | Internal error creating application            |

    ### Generate application job

    **Endpoint:** `POST /v1/applications/{app_id}/jobs`

    | Error Type                 | HTTP Status | Description              | Possible Causes                            |
    | -------------------------- | ----------- | ------------------------ | ------------------------------------------ |
    | `BadRequest`               | 400         | Invalid job parameters   | Malformed job request                      |
    | `InvalidInputParameters`   | 400         | Missing required inputs  | Required input parameters not provided     |
    | `BadCredentials`           | 401         | Authentication required  | Missing or invalid API key                 |
    | `BadToken`                 | 401         | Authentication required  | Missing or invalid API key                 |
    | `InsufficientAccessRights` | 403         | Job execution denied     | No permission to execute jobs for this app |
    | `ResourceNotFound`         | 404         | Application not found    | Application ID doesn't exist               |
    | `BadRequest`               | 409         | Job already running      | Application has a job already in progress  |
    | `QuotaExceeded`            | 429         | Job execution rate limit | Too many jobs executed per minute          |
    | `InternalError`            | 500         | Job execution failed     | Internal error executing job               |
  </Accordion>

  <Accordion title="Tools API" icon="wrench">
    ### AI detect

    **Endpoint:** `POST /v1/tools/ai-detect`

    | Error Type                 | HTTP Status | Description                | Possible Causes                        |
    | -------------------------- | ----------- | -------------------------- | -------------------------------------- |
    | `BadRequest`               | 400         | Invalid text input         | Empty or malformed text input          |
    | `InvalidInputParameters`   | 400         | Text too long              | Input exceeds maximum length           |
    | `BadCredentials`           | 401         | Authentication required    | Missing or invalid API key             |
    | `BadToken`                 | 401         | Authentication required    | Missing or invalid API key             |
    | `InsufficientAccessRights` | 403         | Tool access denied         | Account lacks AI detect permissions    |
    | `QuotaExceeded`            | 429         | Detection rate limit       | Too many detection requests per minute |
    | `InternalError`            | 500         | Detection processing error | Internal error in AI detection         |

    ### PDF parser

    **Endpoint:** `POST /v1/tools/pdf-parser`

    | Error Type                 | HTTP Status | Description             | Possible Causes                      |
    | -------------------------- | ----------- | ----------------------- | ------------------------------------ |
    | `BadRequest`               | 400         | Invalid PDF file        | Corrupted or unsupported PDF         |
    | `InvalidInputParameters`   | 400         | PDF too large           | PDF exceeds size limits              |
    | `BadRequest`               | 400         | PDF password protected  | PDF requires password to access      |
    | `BadCredentials`           | 401         | Authentication required | Missing or invalid API key           |
    | `BadToken`                 | 401         | Authentication required | Missing or invalid API key           |
    | `InsufficientAccessRights` | 403         | Parser access denied    | Account lacks PDF parser permissions |
    | `QuotaExceeded`            | 429         | Parser rate limit       | Too many parsing requests per minute |
    | `InternalError`            | 500         | PDF parsing error       | Internal error parsing PDF           |

    ### Web search

    **Endpoint:** `POST /v1/tools/web-search`

    | Error Type                 | HTTP Status | Description                | Possible Causes                      |
    | -------------------------- | ----------- | -------------------------- | ------------------------------------ |
    | `BadRequest`               | 400         | Invalid search query       | Empty or malformed search query      |
    | `InvalidInputParameters`   | 400         | Search query too long      | Query exceeds maximum length         |
    | `BadCredentials`           | 401         | Authentication required    | Missing or invalid API key           |
    | `BadToken`                 | 401         | Authentication required    | Missing or invalid API key           |
    | `InsufficientAccessRights` | 403         | Search access denied       | Account lacks web search permissions |
    | `QuotaExceeded`            | 429         | Search rate limit          | Too many search requests per minute  |
    | `InternalError`            | 500         | Search processing error    | Internal error in web search         |
    | `InternalError`            | 503         | Search service unavailable | External search service is down      |
  </Accordion>

  <Accordion title="Translation API" icon="language">
    ### Translate text

    **Endpoint:** `POST /v1/translate`

    | Error Type                 | HTTP Status | Description                     | Possible Causes                          |
    | -------------------------- | ----------- | ------------------------------- | ---------------------------------------- |
    | `BadRequest`               | 400         | Invalid language codes          | Unsupported source or target language    |
    | `InvalidInputParameters`   | 400         | Invalid text input              | Empty or malformed text input            |
    | `InvalidInputParameters`   | 400         | Text too long                   | Input exceeds maximum length             |
    | `BadCredentials`           | 401         | Authentication required         | Missing or invalid API key               |
    | `BadToken`                 | 401         | Authentication required         | Missing or invalid API key               |
    | `InsufficientAccessRights` | 403         | Translation access denied       | Account lacks translation permissions    |
    | `QuotaExceeded`            | 429         | Translation rate limit          | Too many translation requests per minute |
    | `InternalError`            | 500         | Translation processing error    | Internal error in translation            |
    | `InternalError`            | 503         | Translation service unavailable | Translation service is down              |
  </Accordion>

  <Accordion title="Vision API" icon="eye">
    ### Analyze images

    **Endpoint:** `POST /v1/vision/analyze`

    | Error Type                 | HTTP Status | Description                | Possible Causes                           |
    | -------------------------- | ----------- | -------------------------- | ----------------------------------------- |
    | `BadRequest`               | 400         | Invalid image format       | Unsupported image type                    |
    | `InvalidInputParameters`   | 400         | Image too large            | Image exceeds size limits                 |
    | `InvalidContentType`       | 400         | Invalid image content      | Corrupted or malformed image              |
    | `BadCredentials`           | 401         | Authentication required    | Missing or invalid API key                |
    | `BadToken`                 | 401         | Authentication required    | Missing or invalid API key                |
    | `InsufficientAccessRights` | 403         | Vision access denied       | Account lacks vision analysis permissions |
    | `QuotaExceeded`            | 429         | Vision rate limit          | Too many analysis requests per minute     |
    | `InternalError`            | 500         | Image processing error     | Internal error processing image           |
    | `InternalError`            | 503         | Vision service unavailable | Vision service is down for maintenance    |
  </Accordion>

  <Accordion title="Guardrails" icon="shield-halved">
    Guardrail errors occur when content is blocked by configured safety controls. For more information, see [Configure guardrails](/home/guardrails).

    ### Content blocked by guardrail

    | Error Type                 | HTTP Status | Description                     | Possible Causes                                                                     |
    | -------------------------- | ----------- | ------------------------------- | ----------------------------------------------------------------------------------- |
    | `GuardrailBlockedError`    | 400         | Content blocked by guardrail    | Input or output violated guardrail policy                                           |
    | `BadRequest`               | 400         | Bedrock guardrail violation     | Content blocked by AWS Bedrock guardrail policy (PII, content filter, denied topic) |
    | `BadCredentials`           | 401         | Guardrail authentication failed | Invalid AWS credentials for Bedrock guardrail                                       |
    | `InsufficientAccessRights` | 403         | Guardrail access denied         | Missing permissions for guardrail provider                                          |
    | `ResourceNotFound`         | 404         | Guardrail not found             | Invalid guardrail ID or version                                                     |
    | `InternalError`            | 500         | Guardrail processing error      | Error communicating with guardrail provider                                         |
    | `InternalError`            | 503         | Guardrail service unavailable   | Guardrail provider service is down                                                  |

    **Example guardrail error:**

    ```json  theme={null}
    {
      "tpe": "BadRequest",
      "errors": [
        {
          "description": "Content blocked by guardrail: PII detected",
          "key": "fail.guardrail.blocked",
          "extras": {
            "guardrail_name": "pii-filter",
            "entity_type": "CREDIT_CARD"
          }
        }
      ],
      "extras": {}
    }
    ```

    **How to Fix:**

    * Review the blocked entity type or violation reason in the error response
    * Remove or mask sensitive content before retrying
    * Check guardrail configuration if blocks are unexpected
    * See [Guardrails documentation](/home/guardrails) for configuration options
  </Accordion>
</AccordionGroup>

## Error categories

### Authentication and authorization errors

#### 401 Unauthorized

| Status | Error code       | Type           | Description     | Common causes                                        |
| ------ | ---------------- | -------------- | --------------- | ---------------------------------------------------- |
| 401    | `BadCredentials` | Authentication | Invalid API key | Missing Authorization header, invalid API key format |
| 401    | `BadToken`       | Authentication | API key expired | API key has expired                                  |

**Example Response:**

```json  theme={null}
{
  "tpe": "Unauthorized",
  "errors": [
    {
      "description": "Invalid token",
      "key": "fail.unauthorized.badToken",
      "extras": {}
    }
  ],
  "extras": {}
}
```

**How to Fix:**

* Verify your API key is correct
* Ensure you've included the `Authorization: Bearer <your_api_key>` header
* Check that your API key hasn't expired
* See [API Keys documentation](/api-reference/api-keys) for more details

#### 403 Forbidden

| Status | Error code                 | Type          | Description                        | Common causes                                |
| ------ | -------------------------- | ------------- | ---------------------------------- | -------------------------------------------- |
| 403    | `InsufficientAccessRights` | Authorization | API key lacks required permissions | Insufficient permissions, wrong API key type |

**Example Response:**

```json  theme={null}
{
  "tpe": "Forbidden",
  "errors": [
    {
      "description": "Insufficient access rights",
      "key": "fail.forbidden.insufficientAccessRights",
      "extras": {}
    }
  ],
  "extras": {}
}
```

**How to Fix:**

* Verify your API key has the required permissions
* Check if you're using the correct API key type
* Contact support if permissions seem incorrect

### Request validation errors

#### 400 Bad Request

| Status | Error code               | Type       | Description                | Common causes                             |
| ------ | ------------------------ | ---------- | -------------------------- | ----------------------------------------- |
| 400    | `BadRequest`             | Validation | Invalid request parameters | Missing required fields, invalid format   |
| 400    | `InvalidInputParameters` | Validation | Invalid parameter values   | Out of range values, unsupported options  |
| 400    | `InvalidContentType`     | Validation | Invalid content type       | Malformed JSON, wrong content-type header |

**Example Response:**

```json  theme={null}
{
  "tpe": "BadRequest",
  "errors": [
    {
      "description": "Invalid input parameters",
      "key": "fail.badRequest.invalidParameters",
      "extras": {}
    }
  ],
  "extras": {}
}
```

**How to Fix:**

* Check required fields and data formats
* Validate parameter values against API documentation
* Ensure request body is valid JSON
* See specific endpoint documentation for required parameters

#### 404 Not Found

| Status | Error code         | Type       | Description                      | Common causes                         |
| ------ | ------------------ | ---------- | -------------------------------- | ------------------------------------- |
| 404    | `ResourceNotFound` | Validation | Requested resource doesn't exist | Invalid resource ID, deleted resource |

**Example Response:**

```json  theme={null}
{
  "tpe": "NotFound",
  "errors": [
    {
      "description": "Resource is not found",
      "key": "fail.notFound.resource",
      "extras": {}
    }
  ],
  "extras": {}
}
```

**How to Fix:**

* Verify the resource ID is correct
* Check if the resource has been deleted
* Ensure the endpoint URL is correct

### Rate limiting and quota errors

#### 429 Too Many Requests

| Status | Error code                  | Type          | Description                      | Common causes                          |
| ------ | --------------------------- | ------------- | -------------------------------- | -------------------------------------- |
| 429    | `QuotaExceeded`             | Rate Limiting | Too many requests in time period | Exceeding per-minute or per-day limits |
| 429    | `CompletionModelQuotaError` | Rate Limiting | Model quota exceeded             | Monthly usage limit reached            |

**Example Response:**

```json  theme={null}
{
  "tpe": "TooManyRequests",
  "errors": [
    {
      "description": "Quota exceeded",
      "key": "fail.tooManyRequests.quotaExceeded",
      "extras": {}
    }
  ],
  "extras": {}
}
```

**How to Fix:**

* Implement exponential backoff
* Check your rate limits in the dashboard
* Consider upgrading your plan for higher limits
* See [Rate Limits documentation](/api-reference/rate-limits) for details

### Server and processing errors

#### 500 Internal Server Error

| Status | Error code                     | Type   | Description             | Common causes                     |
| ------ | ------------------------------ | ------ | ----------------------- | --------------------------------- |
| 500    | `InternalError`                | Server | Unexpected server error | Server-side processing issue      |
| 500    | `CompletionModelInternalError` | Server | Model processing error  | Internal error in model inference |

**Example Response:**

```json  theme={null}
{
  "tpe": "InternalServerError",
  "errors": [
    {
      "description": "Internal server error",
      "key": "fail.internalServerError.generic",
      "extras": {}
    }
  ],
  "extras": {}
}
```

**How to Fix:**

* Retry the request after a short delay
* Check if the issue persists
* Contact support if the error continues

#### 503 Service Unavailable

| Status | Error code                        | Type   | Description                   | Common causes                         |
| ------ | --------------------------------- | ------ | ----------------------------- | ------------------------------------- |
| 503    | `CompletionModelUnavailableError` | Server | Model temporarily unavailable | Model service is down for maintenance |

**Example Response:**

```json  theme={null}
{
  "tpe": "ServiceUnavailable",
  "errors": [
    {
      "description": "Service temporarily unavailable",
      "key": "fail.serviceUnavailable.temporary",
      "extras": {}
    }
  ],
  "extras": {}
}
```

**How to Fix:**

* Wait and retry after some time
* Check service status page
* Implement retry logic with exponential backoff

## AI model-specific errors

For AI content generation endpoints, the API may return additional error types:

### Model errors

| Error Type                              | Description                          |
| --------------------------------------- | ------------------------------------ |
| `CompletionModelUnavailableError`       | AI model is temporarily unavailable  |
| `CompletionModelInternalError`          | Internal error in model processing   |
| `CompletionModelQuotaError`             | Model usage quota exceeded           |
| `CompletionModelUnauthorizedError`      | Invalid model access credentials     |
| `CompletionModelUnderlyingRequestError` | Error in underlying model request    |
| `CompletionModelUnsafeRequestError`     | Request contains unsafe content      |
| `CompletionModelNoPredictionError`      | Model couldn't generate a prediction |

**Example model error:**

```json  theme={null}
{
  "tpe": "CompletionModelQuotaError",
  "errors": [
    {
      "description": "Model usage quota exceeded",
      "key": "fail.model.quotaExceeded",
      "extras": {}
    }
  ],
  "extras": {}
}
```

## SDK error types

The official Writer SDKs provide structured error handling with specific exception types:

### Python SDK errors

| Error Type                 | HTTP Status | Description                                          |
| -------------------------- | ----------- | ---------------------------------------------------- |
| `APIConnectionError`       | N/A         | Network connectivity issues, timeouts, DNS failures  |
| `APITimeoutError`          | N/A         | Request timeout exceeded                             |
| `BadRequestError`          | 400         | Invalid request parameters or malformed request body |
| `AuthenticationError`      | 401         | Missing or invalid API key                           |
| `PermissionDeniedError`    | 403         | Valid API key but insufficient permissions           |
| `NotFoundError`            | 404         | Requested resource doesn't exist                     |
| `UnprocessableEntityError` | 422         | Request is well-formed but contains semantic errors  |
| `RateLimitError`           | 429         | Rate limit or quota exceeded                         |
| `InternalServerError`      | ≥500        | Internal server error                                |

### JavaScript/Node.js SDK errors

| Error Type              | HTTP Status | Description                                          |
| ----------------------- | ----------- | ---------------------------------------------------- |
| `connection_error`      | N/A         | Network connectivity issues, timeouts, DNS failures  |
| `timeout_error`         | N/A         | Request timeout exceeded                             |
| `bad_request`           | 400         | Invalid request parameters or malformed request body |
| `authentication_error`  | 401         | Missing or invalid API key                           |
| `permission_denied`     | 403         | Valid API key but insufficient permissions           |
| `not_found`             | 404         | Requested resource doesn't exist                     |
| `unprocessable_entity`  | 422         | Request is well-formed but contains semantic errors  |
| `rate_limit_error`      | 429         | Rate limit or quota exceeded                         |
| `internal_server_error` | ≥500        | Internal server error                                |

### Error handling example

This example shows how to handle common error cases when making API requests using the Writer SDKs.

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer
  import writerai

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  try:
      response = client.chat.chat(
          messages=[
              {
                  "role": "user",
                  "content": "Write a haiku about programming"
              }
          ],
          model="palmyra-x5"
      )
      print("Success:", response.choices[0].message.content)
      
  except writerai.APIConnectionError as e:
      print("Network error:", e)
      print("Cause:", e.__cause__)
      
  except writerai.RateLimitError as e:
      print("Rate limited:", e)
      print("Status code:", e.status_code)
      # SDK automatically handles retries with exponential backoff
      
  except writerai.AuthenticationError as e:
      print("Authentication failed:", e)
      print("Status code:", e.status_code)
      # Refresh API key or redirect to login
      
  except writerai.BadRequestError as e:
      print("Invalid request:", e)
      print("Status code:", e.status_code)
      
  except writerai.InternalServerError as e:
      print("Server error:", e)
      print("Status code:", e.status_code)
      # SDK automatically retries 5xx errors
      
  except writerai.APIStatusError as e:
      print("API error:", e)
      print("Status code:", e.status_code)
      print("Response:", e.response)
  ```

  ```javascript JavaScript theme={null}
  import Writer from '@writer/writer-node';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer({});

  try {
    const response = await client.chat.chat({
      messages: [
        {
          role: 'user',
          content: 'Write a haiku about programming'
        }
      ],
      model: 'palmyra-x5'
    });
    
    console.log('Success:', response.choices[0].message.content);
  } catch (error) {
    if (error.code === 'bad_request') {
      console.error('Invalid request:', error.message);
    } else if (error.code === 'authentication_error') {
      console.error('Authentication failed:', error.message);
      // Refresh API key or redirect to login
    } else if (error.code === 'rate_limit_error') {
      console.error('Rate limited:', error.message);
      // SDK automatically handles retries with exponential backoff
    } else if (error.code === 'internal_server_error') {
      console.error('Server error:', error.message);
      // SDK automatically retries 5xx errors
    } else if (error.code === 'connection_error') {
      console.error('Network error:', error.message);
    } else {
      console.error('Unexpected error:', error.message);
    }
  }
  ```
</CodeGroup>

## Troubleshooting common errors

### 400 Bad request

* Verify all required parameters are included
* Check parameter value formats and constraints
* Ensure request body is valid JSON

### 401 Unauthorized

* Verify API key is correct and not expired
* Check that the API key has the required permissions
* Ensure the Authorization header is properly formatted

### 403 Forbidden

* Check if your organization/team has access to the requested resource
* Verify that the feature is enabled for your plan
* Contact support if you believe this is an error

### 429 Too many requests

* Implement exponential backoff retry logic
* Check your current usage against rate limits
* Consider upgrading your plan for higher limits

### 500 Internal server error

* Retry the request after a short delay
* Check the [Writer status page](https://status.writer.com/) for known issues
* Contact support if the error persists

## Next steps

* [API keys](/api-reference/api-keys): learn how to authenticate with Writer APIs
* [Rate limits](/api-reference/rate-limits): understand API rate limiting and quotas
* [Python SDK](https://github.com/writer/writer-python): official Python library with built-in error handling
* [Node.js SDK](https://github.com/writer/writer-node): official JavaScript/Node.js library with built-in error handling
