# Source: https://developer.mixpanel.com/reference/get-annotation-1.md

# Get Annotation

Get an Annotation

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
      "name": "Retrieve Annotations",
      "description": "List all annotations for the project"
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
      "get": {
        "operationId": "get-annotation",
        "tags": [
          "Retrieve Annotations"
        ],
        "summary": "Get Annotation",
        "description": "Get an Annotation",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetAnnotationsResponse"
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
      "GetAnnotationsResponse": {
        "title": "GetAnnotationsResponse",
        "description": "A JSON response object containing an annotation'",
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
            "$ref": "#/components/schemas/AnnotationsEntry"
          }
        }
      },
      "AnnotationsEntry": {
        "title": "AnnotationsEntry",
        "description": "Representation of a single annotation",
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "date": {
            "$ref": "#/components/schemas/InputDate"
          },
          "description": {
            "$ref": "#/components/schemas/InputDescription"
          },
          "id": {
            "type": "number"
          },
          "user": {
            "$ref": "#/components/schemas/UserInfo"
          },
          "tags": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SimpleTag"
            }
          }
        }
      },
      "SimpleTag": {
        "title": "SimpleTag",
        "description": "Basic info about an Annotation Tag",
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "name": {
            "type": "string"
          }
        }
      },
      "UserInfo": {
        "title": "UserInfo",
        "description": "Info about the creator of the annotation",
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "first_name": {
            "example": "John",
            "type": "string"
          },
          "last_name": {
            "example": "Smith",
            "type": "string"
          }
        }
      },
      "InputDate": {
        "type": "string",
        "description": "A string representation of a date in \"YYYY-MM-DD HH:mm:ss\" format",
        "example": "2022-02-15 12:00:00"
      },
      "InputDescription": {
        "type": "string",
        "description": "The text that will be shown when looking at the annotation",
        "example": "Something interesting happened!"
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