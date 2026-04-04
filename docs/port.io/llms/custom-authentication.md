# Source: https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/custom-authentication.md

# Custom authentication

Self-hosted only

Custom authentication is only available for self-hosted installations. It is not supported for integrations hosted by Port.

The custom authentication feature enables you to configure OAuth2, JWT, and other dynamic token-based authentication flows beyond the standard authentication types (`bearer_token`, `basic`, `api_key`, `none`).

## How it works[â](#how-it-works "Direct link to How it works")

When `authType` is set to `"custom"`, you configure two parts:

1. **How to authenticate** (`customAuthRequest`) - defines the authentication endpoint, HTTP method, headers, and body.
2. **How to use the token** (`customAuthRequestTemplate`) - defines where to inject authentication values in subsequent requests using template syntax.

The integration automatically:

* Authenticates on startup
* Caches evaluated templates for performance
* Refreshes tokens proactively (if `reauthenticateIntervalSeconds` is configured) or reactively on 401 errors
* Handles concurrent requests safely with locking

## Configuration[â](#configuration "Direct link to Configuration")

### customAuthRequest[â](#customauthrequest "Direct link to customAuthRequest")

Defines how to make the authentication request. This is configured as a JSON object.

| Field                           | Type    | Description                                                                                                                                                    | Required |
| ------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `endpoint`                      | string  | Authentication endpoint. Can be a relative path (e.g., `/oauth/token`) appended to your base URL, or a full URL (e.g., `https://auth.example.com/token`)       | â       |
| `method`                        | string  | HTTP method for the authentication request. Allowed values: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`. Default: `POST`                                           | â       |
| `headers`                       | object  | HTTP headers to send with the authentication request (key-value pairs)                                                                                         | â       |
| `body`                          | object  | JSON request body for the authentication request. Mutually exclusive with `bodyForm`                                                                           | â       |
| `bodyForm`                      | string  | Form-encoded request body (e.g., `grant_type=client_credentials&client_id=...`). Mutually exclusive with `body`                                                | â       |
| `queryParams`                   | object  | Query parameters to send with the authentication request (key-value pairs)                                                                                     | â       |
| `reauthenticateIntervalSeconds` | integer | Token validity duration in seconds. If provided, tokens refresh 60 seconds before expiration. If not provided, tokens only refresh on 401 errors. Must be >= 1 | â       |

Body configuration

You cannot specify both `body` and `bodyForm` in `customAuthRequest`. Use `body` for JSON payloads and `bodyForm` for form-encoded payloads.

### customAuthRequestTemplate[â](#customauthrequesttemplate "Direct link to customAuthRequestTemplate")

Defines how to use the authentication response in subsequent API requests. Use template syntax `{{.jq_path}}` to extract values from the auth response. At least one field must be provided.

| Field         | Type   | Description                                                                                                                                                                          | Required |
| ------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `headers`     | object | HTTP headers to add or override in subsequent API requests. Use template syntax to inject values (e.g., `{"Authorization": "Bearer {{.access_token}}"}`)                             | â       |
| `queryParams` | object | Query parameters to add or override in subsequent API requests. Use template syntax to inject values (e.g., `{"api_key": "{{.access_token}}"}`)                                      | â       |
| `body`        | object | Request body fields to add or override in subsequent API requests. Merged with request body if present. Use template syntax to inject values (e.g., `{"token": "{{.accessToken}}"}`) | â       |

#### Template syntax[â](#template-syntax "Direct link to Template syntax")

Use `{{.jq_path}}` to extract values from the authentication response JSON. The path uses dot notation to access nested fields:

* `{{.access_token}}` - Extracts the `access_token` field from the root
* `{{.data.token}}` - Extracts the `token` field from a nested `data` object
* `{{.nested.field.value}}` - Extracts deeply nested values

The template syntax is validated at configuration time, so errors fail fast before runtime.

## Installation examples[â](#installation-examples "Direct link to Installation examples")

### Using Helm[â](#using-helm "Direct link to Using Helm")

When using Helm, pass the custom authentication configuration as a JSON string in the `integration.config.customAuthRequest` and `integration.config.customAuthRequestTemplate` parameters:

```
helm install ocean-custom port-labs/port-ocean \
  --set port.clientId="<PORT_CLIENT_ID>" \
  --set port.clientSecret="<PORT_CLIENT_SECRET>" \
  --set port.baseUrl="https://api.port.io" \
  --set integration.identifier="ocean-custom" \
  --set integration.type="custom" \
  --set integration.eventListener.type="POLLING" \
  --set integration.config.baseUrl="https://api.yourcompany.com" \
  --set integration.config.authType="custom" \
  --set-json integration.config.customAuthRequest='{"endpoint":"/oauth/token","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded"},"bodyForm":"grant_type=client_credentials&client_id=<CLIENT_ID>&client_secret=<CLIENT_SECRET>","reauthenticateIntervalSeconds":3600}' \
  --set-json integration.config.customAuthRequestTemplate='{"headers":{"Authorization":"Bearer {{.access_token}}"}}'
```

### Using Docker[â](#using-docker "Direct link to Using Docker")

When using Docker, pass the configuration as JSON strings in environment variables:

```
docker run -i --rm \
  -e OCEAN__PORT__CLIENT_ID="<PORT_CLIENT_ID>" \
  -e OCEAN__PORT__CLIENT_SECRET="<PORT_CLIENT_SECRET>" \
  -e OCEAN__PORT__BASE_URL="https://api.port.io" \
  -e OCEAN__INTEGRATION__IDENTIFIER="ocean-custom" \
  -e OCEAN__INTEGRATION__TYPE="custom" \
  -e OCEAN__EVENT_LISTENER='{"type":"POLLING"}' \
  -e OCEAN__INTEGRATION__CONFIG__BASE_URL="https://api.yourcompany.com" \
  -e OCEAN__INTEGRATION__CONFIG__AUTH_TYPE="custom" \
  -e OCEAN__INTEGRATION__CONFIG__CUSTOM_AUTH_REQUEST='{"endpoint":"/oauth/token","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded"},"bodyForm":"grant_type=client_credentials&client_id=<CLIENT_ID>&client_secret=<CLIENT_SECRET>","reauthenticateIntervalSeconds":3600}' \
  -e OCEAN__INTEGRATION__CONFIG__CUSTOM_AUTH_REQUEST_TEMPLATE='{"headers":{"Authorization":"Bearer {{.access_token}}"}}'
  ghcr.io/port-labs/port-ocean-custom:latest
```

## Common examples[â](#common-examples "Direct link to Common examples")

### OAuth2 client credentials flow[â](#oauth2-client-credentials-flow "Direct link to OAuth2 client credentials flow")

Use this pattern for OAuth2 client credentials grants:

```
{
  "customAuthRequest": {
    "endpoint": "/oauth/token",
    "method": "POST",
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    "bodyForm": "grant_type=client_credentials&client_id=<CLIENT_ID>&client_secret=<CLIENT_SECRET>",
    "reauthenticateIntervalSeconds": 3600
  },
  "customAuthRequestTemplate": {
    "headers": {
      "Authorization": "Bearer {{.access_token}}"
    }
  }
}
```

**Expected auth response:**

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### API key in query parameter[â](#api-key-in-query-parameter "Direct link to API key in query parameter")

For APIs that return an API key to use in query parameters:

```
{
  "customAuthRequest": {
    "endpoint": "/api/auth/login",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "username": "<USERNAME>",
      "password": "<PASSWORD>"
    }
  },
  "customAuthRequestTemplate": {
    "queryParams": {
      "api_key": "{{.apiKey}}"
    }
  }
}
```

**Expected auth response:**

```
{
  "apiKey": "abc123xyz789",
  "userId": "12345"
}
```

### JWT token authentication[â](#jwt-token-authentication "Direct link to JWT token authentication")

For JWT-based authentication systems:

```
{
  "customAuthRequest": {
    "endpoint": "/v1/auth/token",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "clientId": "<CLIENT_ID>",
      "clientSecret": "<CLIENT_SECRET>"
    }
  },
  "customAuthRequestTemplate": {
    "headers": {
      "Authorization": "Bearer {{.jwt}}",
      "X-API-Version": "{{.version}}"
    }
  }
}
```

**Expected auth response:**

```
{
  "jwt": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "version": "2.0",
  "expiresAt": "2024-12-31T23:59:59Z"
}
```

### Nested response structure[â](#nested-response-structure "Direct link to Nested response structure")

If your authentication service returns nested data, use dot notation:

```
{
  "customAuthRequest": {
    "endpoint": "/auth/login",
    "method": "POST",
    "body": {
      "credentials": {
        "username": "<USERNAME>",
        "password": "<PASSWORD>"
      }
    }
  },
  "customAuthRequestTemplate": {
    "headers": {
      "Authorization": "Bearer {{.data.token}}",
      "X-Session-ID": "{{.data.sessionId}}"
    }
  }
}
```

**Expected auth response:**

```
{
  "status": "success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "sessionId": "sess_abc123"
  }
}
```

### Token in multiple places[â](#token-in-multiple-places "Direct link to Token in multiple places")

You can inject the same token into headers, query params, and body simultaneously:

```
{
  "customAuthRequest": {
    "endpoint": "/v1/auth/token",
    "method": "POST",
    "body": {
      "clientId": "<CLIENT_ID>",
      "clientSecret": "<CLIENT_SECRET>"
    }
  },
  "customAuthRequestTemplate": {
    "headers": {
      "Authorization": "Bearer {{.access_token}}"
    },
    "queryParams": {
      "token": "{{.access_token}}"
    },
    "body": {
      "auth_token": "{{.access_token}}"
    }
  }
}
```

## Token refresh behavior[â](#token-refresh-behavior "Direct link to Token refresh behavior")

The integration handles token refresh in two ways:

### Proactive refresh[â](#proactive-refresh "Direct link to Proactive refresh")

If `reauthenticateIntervalSeconds` is configured, tokens refresh automatically 60 seconds before expiration. For example, if you set `reauthenticateIntervalSeconds: 3600`, the integration will refresh the token after 3540 seconds (59 minutes).

### Reactive refresh[â](#reactive-refresh "Direct link to Reactive refresh")

If `reauthenticateIntervalSeconds` is not configured, tokens only refresh when the integration receives a 401 (Unauthorized) response. The integration will:

1. Attempt to reauthenticate once
2. Retry the failed request with the new token
3. If reauthentication fails, throw an error visible in the logs

## Error handling[â](#error-handling "Direct link to Error handling")

If authentication fails, errors are visible in the integration logs. Common failure scenarios:

* **Auth endpoint returns error**: The integration fails to start and logs the error
* **Missing token field**: If the expected field (e.g., `{{.access_token}}`) is not in the response, an error is thrown
* **Reauthentication fails**: If refresh fails after a 401 error, the integration logs the error and stops processing requests

### Verify configuration[â](#verify-configuration "Direct link to Verify configuration")

Ensure your configuration follows these rules:

* At least one of `headers`, `queryParams`, or `body` must be provided in `customAuthRequestTemplate`
* `body` and `bodyForm` cannot both be specified in `customAuthRequest`
* Template paths (e.g., `{{.access_token}}`) must match fields in your auth response
* Replace placeholders (e.g., `<CLIENT_ID>`, `<CLIENT_SECRET>`) with your actual values

### Test the authentication endpoint[â](#test-the-authentication-endpoint "Direct link to Test the authentication endpoint")

Before configuring the integration, test your authentication endpoint directly:

```
curl -X POST https://api.yourcompany.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=YOUR_ID&client_secret=YOUR_SECRET"
```

Verify that the response contains the fields you're trying to extract with template syntax.
