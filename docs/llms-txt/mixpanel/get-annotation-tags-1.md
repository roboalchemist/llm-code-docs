# Source: https://developer.mixpanel.com/reference/get-annotation-tags-1.md

# Get Annotation Tags

Get all tags that have been added to at least one annotation. Requires a role of at least Analyst

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
  "paths": {
    "/projects/{projectId}/annotations/tags": {
      "parameters": [
        {
          "$ref": "#/components/parameters/projectId"
        }
      ],
      "get": {
        "operationId": "get-annotation-tags",
        "tags": [
          "Get Annotation tags"
        ],
        "description": "Get all tags that have been added to at least one annotation. Requires a role of at least Analyst",
        "summary": "Get Annotation Tags",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetAnnotationTagsResponse"
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
      "GetAnnotationTagsResponse": {
        "title": "GetAnnotationTagsResponse",
        "description": "The list of annotation tags that have been created",
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/AnnotationTag"
        }
      },
      "AnnotationTag": {
        "title": "AnnotationTag",
        "description": "An annotation tag",
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "name": {
            "type": "string"
          },
          "project_id": {
            "type": "number"
          },
          "has_annotations": {
            "type": "boolean",
            "description": "whether the tag is currently attached to any annotations"
          }
        }
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