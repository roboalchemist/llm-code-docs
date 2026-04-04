# Source: https://docs.jfrog.com/artifactory/reference/getartifactoryapplicationmetrics.md

# Get Artifactory Application Metrics

Returns application-related metrics for Cloud (SaaS) users in OpenMetrics/Prometheus exposition text format (`text/plain`). This feature is supported on the Cloud (SaaS) platform for all licenses.

**Security**: Requires a valid admin user.

Use `Accept: text/plain` or `Accept: */*` in the request header.


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
    "/v1/metrics/application": {
      "get": {
        "tags": [
          "Metrics"
        ],
        "summary": "Get Artifactory Application Metrics",
        "description": "Returns application-related metrics for Cloud (SaaS) users in OpenMetrics/Prometheus exposition text format (`text/plain`). This feature is supported on the Cloud (SaaS) platform for all licenses.\n\n**Security**: Requires a valid admin user.\n\nUse `Accept: text/plain` or `Accept: */*` in the request header.\n",
        "operationId": "getArtifactoryApplicationMetrics",
        "responses": {
          "200": {
            "description": "Successfully retrieved application metrics in OpenMetrics text format.",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string",
                  "description": "Metrics in OpenMetrics/Prometheus exposition text format.",
                  "example": "# HELP app_disk_free_bytes Free disk space in bytes\n# TYPE app_disk_free_bytes gauge\napp_disk_free_bytes 1.073741824e+09\n"
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