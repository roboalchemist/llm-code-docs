# Source: https://docs.jfrog.com/artifactory/reference/createsignedurl.md

# Create Signed URL

Generates a signed url for the provided repository path, providing temporary access to download artifacts. User may provide expiry or valid_for_secs optional parameter. With a maximum timeframe of one year (365 days). Default expiry is 24 hours. Note - This API is available only to Artifactory Cloud Enterprise and Cloud Enterprise+ users. The JSON included in the request URL cannot include %20.

Since: Artifactory 7.5.0

Security: Requires a privileged user (admin or manage permission type)


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
    "/signed/url": {
      "post": {
        "tags": [
          "Signed URLs"
        ],
        "summary": "Create Signed URL",
        "description": "Generates a signed url for the provided repository path, providing temporary access to download artifacts. User may provide expiry or valid_for_secs optional parameter. With a maximum timeframe of one year (365 days). Default expiry is 24 hours. Note - This API is available only to Artifactory Cloud Enterprise and Cloud Enterprise+ users. The JSON included in the request URL cannot include %20.\n\nSince: Artifactory 7.5.0\n\nSecurity: Requires a privileged user (admin or manage permission type)\n",
        "operationId": "createSignedUrl",
        "requestBody": {
          "required": true,
          "description": "Signed URL request",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateSignedUrlRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Signed URL created successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - The request body is malformed or invalid.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
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
            "description": "Permission Denied - The user does not have admin or manage permission type.",
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
      },
      "CreateSignedUrlRequest": {
        "type": "object",
        "required": [
          "repo_path"
        ],
        "properties": {
          "repo_path": {
            "type": "string",
            "minLength": 1,
            "description": "Full path to the artifact"
          },
          "valid_for_secs": {
            "type": "integer",
            "format": "int32",
            "description": "Number of seconds since generation before the URL expires"
          },
          "expiry": {
            "type": "integer",
            "format": "int64",
            "description": "An expiry date for the URL after which the URL will be invalid, expiry value is in Unix epoch time in milliseconds"
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