# Source: https://docs.jfrog.com/artifactory/reference/replacesignedurlkey.md

# Replace Signed URL Key

Replaces the key for signing and validating signed URLs. This will invalidate any signed URLs previously created. Note - This feature is available only for Artifactory Cloud Enterprise and Enterprise+ users.

Note: This feature is available only for Artifactory Cloud Enterprise and Enterprise+ users.

Since: Artifactory 7.5.0

Security: Requires a privileged user (admin)


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
      "name": "Signed URLs",
      "description": "Signed URL operations"
    }
  ],
  "paths": {
    "/signed/url/key": {
      "post": {
        "tags": [
          "Signed URLs"
        ],
        "summary": "Replace Signed URL Key",
        "description": "Replaces the key for signing and validating signed URLs. This will invalidate any signed URLs previously created. Note - This feature is available only for Artifactory Cloud Enterprise and Enterprise+ users.\n\nNote: This feature is available only for Artifactory Cloud Enterprise and Enterprise+ users.\n\nSince: Artifactory 7.5.0\n\nSecurity: Requires a privileged user (admin)\n",
        "operationId": "replaceSignedUrlKey",
        "responses": {
          "201": {
            "description": "Signed URL key replaced successfully"
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Permission Denied - The user does not have admin permissions.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "status": {
                  "type": "integer",
                  "description": "HTTP status code"
                },
                "message": {
                  "type": "string",
                  "description": "Error message"
                }
              }
            }
          }
        }
      }
    },
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