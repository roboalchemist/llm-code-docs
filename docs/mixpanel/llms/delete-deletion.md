# Source: https://developer.mixpanel.com/reference/delete-deletion.md

# Cancel a Deletion

Cancel a deletion task that is still in progress

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "GDPR API",
    "description": "The following retrieval and deletion API is made for GDPR and CCPA compliance.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "version": "3.0.0"
  },
  "servers": [
    {
      "url": "https://{regionAndDomain}.com/api/app",
      "description": "Mixpanel's application API server.",
      "variables": {
        "regionAndDomain": {
          "default": "mixpanel",
          "enum": [
            "mixpanel",
            "eu.mixpanel",
            "in.mixpanel"
          ],
          "description": "The server location to be used:\n  * `mixpanel` - The default (US) servers used for most projects\n  * `eu.mixpanel` - EU servers if you are enrolled in EU Data Residency\n  * `in.mixpanel` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "security": [
    {
      "OAuthToken": []
    }
  ],
  "tags": [
    {
      "name": "Cancel a Deletion",
      "description": "Cancels an existing deletion task"
    }
  ],
  "paths": {
    "/data-deletions/v3.0/{tracking_id}": {
      "parameters": [
        {
          "$ref": "#/components/parameters/TrackingId"
        },
        {
          "$ref": "#/components/parameters/ProjectToken"
        }
      ],
      "delete": {
        "operationId": "delete-deletion",
        "tags": [
          "Cancel a Deletion"
        ],
        "summary": "Cancel a Deletion",
        "description": "Cancel a deletion task that is still in progress",
        "responses": {
          "204": {
            "description": "Success"
          },
          "401": {
            "$ref": "#/components/responses/401Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/403Forbidden"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "OAuthToken": {
        "type": "http",
        "scheme": "bearer",
        "description": "OAuth Token"
      }
    },
    "schemas": {
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Details about the error that occurred"
          },
          "status": {
            "type": "string",
            "enum": [
              "error"
            ]
          }
        }
      }
    },
    "responses": {
      "401Unauthorized": {
        "description": "Unauthorized",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "403Forbidden": {
        "description": "Forbidden",
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
```