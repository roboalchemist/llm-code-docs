# Source: https://developer.mixpanel.com/reference/delete-annotation-1.md

# Delete Annotation

Delete an Annotation. Requires a role of at least Analyst.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Annotations API",
    "description": "Use annotations to label specific points in time in your charts with a description.",
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "1.0.0"
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
      "ServiceAccount": []
    }
  ],
  "tags": [
    {
      "name": "Delete Annotation",
      "description": "Delete annotation for a project"
    }
  ],
  "paths": {
    "/projects/{projectId}/annotations/{annotationId}": {
      "parameters": [
        {
          "$ref": "#/components/parameters/projectId"
        },
        {
          "name": "annotationId",
          "in": "path",
          "description": "The id of the annotation",
          "required": true,
          "schema": {
            "type": "number"
          }
        }
      ],
      "delete": {
        "operationId": "delete-annotation",
        "tags": [
          "Delete Annotation"
        ],
        "summary": "Delete Annotation",
        "description": "Delete an Annotation. Requires a role of at least Analyst.",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DeleteAnnotationsResponse"
                }
              }
            }
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
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      }
    },
    "schemas": {
      "DeleteAnnotationsResponse": {
        "title": "DeleteAnnotationsResponse",
        "description": "A JSON response object containing the id of the deleted annotation'",
        "type": "object",
        "additionalProperties": false,
        "required": [
          "status",
          "results"
        ],
        "properties": {
          "status": {
            "$ref": "#/components/schemas/ResponseStatus"
          },
          "results": {
            "type": "object",
            "properties": {
              "id": {
                "type": "number",
                "description": "The id of the deleted annotation"
              }
            }
          }
        }
      },
      "ResponseStatus": {
        "type": "string",
        "description": "The status of the response",
        "example": "ok"
      },
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