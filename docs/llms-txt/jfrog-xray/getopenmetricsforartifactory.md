# Source: https://docs.jfrog.com/artifactory/reference/getopenmetricsforartifactory.md

# Get the Open Metrics for Artifactory

Returns all open metrics collected for Artifactory in OpenMetrics/Prometheus exposition text format (`text/plain`). This feature is supported on the Self-Hosted platform, with a Pro, Pro X, Enterprise X, or Enterprise+ license.

**Security**: Requires a valid admin user.

Use `Accept: text/plain` or `Accept: */*` in the request header.


<br />

<Callout icon="📘" theme="info">
  Supported on Self-managed JPD sites only.
</Callout>

<br />

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Artifactory Artifacts & Storage API",
    "description": "REST API for managing artifacts, storage, and related operations in JFrog Artifactory",
    "version": "1.0.0",
    "contact": {
      "name": "JFrog Support"
    }
  },
  "servers": [
    {
      "url": "https://{jfrog_url}/artifactory/api",
      "description": "JFrog Platform",
      "variables": {
        "jfrog_url": {
          "default": "myserver.jfrog.io",
          "description": "Your JFrog Platform hostname (e.g., mycompany.jfrog.io)"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Metrics",
      "description": "Metrics and monitoring operations"
    }
  ],
  "paths": {
    "/v1/metrics": {
      "get": {
        "tags": [
          "Metrics"
        ],
        "summary": "Get the Open Metrics for Artifactory",
        "description": "Returns all open metrics collected for Artifactory in OpenMetrics/Prometheus exposition text format (`text/plain`). This feature is supported on the Self-Hosted platform, with a Pro, Pro X, Enterprise X, or Enterprise+ license.\n\n**Security**: Requires a valid admin user.\n\nUse `Accept: text/plain` or `Accept: */*` in the request header.\n",
        "operationId": "getOpenMetricsForArtifactory",
        "parameters": [
          {
            "name": "Accept",
            "in": "header",
            "required": true,
            "description": "Must be `text/plain; version=0.0.4` (Prometheus exposition format).",
            "schema": {
              "type": "string",
              "enum": [
                "text/plain; version=0.0.4"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved open metrics in OpenMetrics text format.",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string",
                  "description": "Metrics in OpenMetrics/Prometheus exposition text format.",
                  "example": "# HELP jfrt_runtime_heap_freememory_bytes Free heap memory in bytes\n# TYPE jfrt_runtime_heap_freememory_bytes gauge\njfrt_runtime_heap_freememory_bytes 5.36870912e+08\n"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required."
          },
          "403": {
            "description": "Permission Denied - The user does not have admin permissions."
          },
          "406": {
            "description": "Not Acceptable - The server cannot produce a response matching the Accept header. This endpoint only serves text/plain. Ensure your request uses `Accept: text/plain` or `Accept: */*`."
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "JWT token authentication"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication"
      }
    }
  },
  "security": [
    {
      "bearerAuth": []
    },
    {
      "basicAuth": []
    }
  ]
}
```