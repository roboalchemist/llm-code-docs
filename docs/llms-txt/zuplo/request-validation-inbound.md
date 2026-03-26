# Source: https://www.zuplo.com/docs/policies/request-validation-inbound.md

# Request Validation Policy

The Request Validation policy validates incoming requests against your OpenAPI
schema definitions, ensuring that all requests conform to your API's expected
structure and data types before they reach your backend services.

With this policy, you'll benefit from:

- **Data Integrity Protection**: Prevent malformed or invalid data from reaching
  your backend systems
- **Automatic Schema Enforcement**: Leverage your existing OpenAPI definitions
  for validation without additional code
- **Comprehensive Validation**: Validate request bodies, query parameters, path
  parameters, and headers
- **Detailed Error Responses**: Return clear, actionable error messages that
  help API consumers fix invalid requests
- **Developer-Friendly Experience**: Improve the developer experience by
  providing immediate feedback on request issues
- **Reduced Backend Errors**: Minimize crashes and unexpected behavior caused by
  invalid input data
- **API Contract Enforcement**: Ensure all API consumers adhere to your
  documented API contract

When configured, any requests that do not conform to your OpenAPI schema will be
rejected with a `400: Bad Request` response containing a detailed error message
(in JSON) explaining why the request was not accepted.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-request-validation-inbound-policy",
  "policyType": "request-validation-inbound",
  "handler": {
    "export": "RequestValidationInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "includeRequestInLogs": false,
      "logLevel": "info",
      "validateBody": "reject-and-log",
      "validateHeaders": "none",
      "validatePathParameters": "log-only",
      "validateQueryParameters": "log-only"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `request-validation-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `RequestValidationInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `logLevel` <code className="text-green-600">&lt;string&gt;</code> - The log level to use when logging validation errors. Allowed values are `error`, `warn`, `info`, `debug`. Defaults to `"info"`.
- `validateBody` <code className="text-green-600">&lt;string&gt;</code> - The action to perform when validation fails. Allowed values are `none`, `log-only`, `reject-and-log`, `reject-only`. Defaults to `"none"`.
- `validateQueryParameters` <code className="text-green-600">&lt;string&gt;</code> - The action to perform when validation fails. Allowed values are `none`, `log-only`, `reject-and-log`, `reject-only`. Defaults to `"none"`.
- `validatePathParameters` <code className="text-green-600">&lt;string&gt;</code> - The action to perform when validation fails. Allowed values are `none`, `log-only`, `reject-and-log`, `reject-only`. Defaults to `"none"`.
- `validateHeaders` <code className="text-green-600">&lt;string&gt;</code> - The action to perform when validation fails. Allowed values are `none`, `log-only`, `reject-and-log`, `reject-only`. Defaults to `"none"`.
- `includeRequestInLogs` <code className="text-green-600">&lt;boolean&gt;</code> - Whether to include the request in the logs. Defaults to `false`.

## Using the Policy

The Request Validation Inbound policy validates incoming requests against your
OpenAPI schema definitions. This ensures that all requests to your API conform
to your specified data structure and types before they reach your backend
services.

## How It Works

This policy automatically validates incoming requests based on the OpenAPI
schemas defined in your API specification. It checks:

- **Request Bodies**: Validates JSON/XML payloads against your schema
  definitions
- **Query Parameters**: Ensures query parameters match expected types and
  constraints
- **Path Parameters**: Validates URL path parameters against defined patterns
- **Headers**: Verifies required headers are present and conform to
  specifications

When a request fails validation, the policy returns a detailed 400 Bad Request
response with specific information about which part of the request failed
validation and why.

## Configuration

The policy requires minimal configuration as it automatically uses your existing
OpenAPI schemas. You can enable or disable validation for specific parts of the
request (body, query parameters, headers) through the policy options.

## OpenAPI Schema Example

Here's an example of how to specify a schema for validation in a request body in
your OpenAPI specification:

```json
  "requestBody": {
    "description": "user to add to the system",
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "age": {
              "type": "integer"
            }
          },
          "required": [
            "name",
            "age"
          ]
        }
      }
    }
  }
```

## Advanced Validation

The policy supports the full range of OpenAPI schema validation features,
including:

- Type validation (string, number, boolean, array, object)
- Format validation (date, date-time, email, etc.)
- Pattern matching with regular expressions
- Numeric constraints (minimum, maximum, multipleOf)
- String constraints (minLength, maxLength)
- Array constraints (minItems, maxItems, uniqueItems)
- Required properties
- Enum values
- Complex schemas with allOf, anyOf, oneOf, and not

Read more about [how policies work](/articles/policies)
