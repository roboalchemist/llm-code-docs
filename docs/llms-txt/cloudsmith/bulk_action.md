# Source: https://help.cloudsmith.io/reference/bulk_action.md

# /bulk-action/{owner}/

Perform bulk operations on multiple packages within a repository or across all accessible repositories. If 'repository' is provided, actions are limited to that repository. If 'repository' is omitted, actions are performed across all repositories the user has access to within the workspace. Returns a list of successfully actioned packages and any packages that failed with error details. 

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/bulk-action/{owner}/": {
      "post": {
        "operationId": "bulk_action",
        "description": "Perform bulk operations on multiple packages within a repository or across all accessible repositories. If 'repository' is provided, actions are limited to that repository. If 'repository' is omitted, actions are performed across all repositories the user has access to within the workspace. Returns a list of successfully actioned packages and any packages that failed with error details. ",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PackageBulkAction"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PackageBulkActionResponse"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "bulk-action"
        ]
      },
      "parameters": [
        {
          "name": "owner",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "PackageBulkAction": {
        "required": [
          "action",
          "identifiers"
        ],
        "type": "object",
        "properties": {
          "action": {
            "title": "Action",
            "description": "The action to perform on the packages.",
            "type": "string",
            "enum": [
              "Delete",
              "Resync",
              "Quarantine",
              "Unquarantine",
              "Move",
              "Copy",
              "Rescan"
            ]
          },
          "identifiers": {
            "description": "A list of package identifiers to apply the action to.",
            "type": "array",
            "items": {
              "type": "string",
              "maxLength": 255,
              "minLength": 1
            },
            "maxItems": 100,
            "minItems": 1
          },
          "repository": {
            "title": "Repository",
            "description": "The repository name to filter packages to. If not provided, the action will be performed across all accessible repositories in the workspace.",
            "type": "string",
            "maxLength": 255,
            "minLength": 1
          },
          "target_repository": {
            "title": "Target repository",
            "description": "The slug of the target repository",
            "type": "string",
            "minLength": 1
          }
        }
      },
      "PackageBulkActionResponse": {
        "type": "object",
        "properties": {
          "action": {
            "title": "Action",
            "description": "The action that was performed.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "packages_actioned": {
            "description": "List of package identifiers that were successfully actioned.",
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            },
            "readOnly": true
          },
          "packages_failed_to_action": {
            "title": "Packages failed to action",
            "description": "Dictionary of package identifiers that failed with their error details.",
            "type": "object",
            "additionalProperties": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "nullable": true
              }
            },
            "readOnly": true
          }
        }
      }
    }
  }
}
```