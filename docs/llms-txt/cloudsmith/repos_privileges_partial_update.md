# Source: https://help.cloudsmith.io/reference/repos_privileges_partial_update.md

# Modify privileges for the repository.

Modify privileges for the repository.

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
    "/repos/{owner}/{identifier}/privileges": {
      "patch": {
        "operationId": "repos_privileges_partial_update",
        "summary": "Modify privileges for the repository.",
        "description": "Modify privileges for the repository.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RepositoryPrivilegeInputRequestPatch"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "Repository privileges updated"
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
          "404": {
            "description": "Owner namespace or repository not found",
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
          "repos"
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
        },
        {
          "name": "identifier",
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
      "RepositoryPrivilegeDict": {
        "required": [
          "privilege"
        ],
        "type": "object",
        "properties": {
          "privilege": {
            "title": "Privilege",
            "description": "The level of privilege that the user or team should be granted to the specified repository.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ]
          },
          "service": {
            "title": "Service",
            "description": "The service identifier (slug).",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "minLength": 1
          },
          "team": {
            "title": "Team",
            "description": "The team identifier (slug).",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "minLength": 1
          },
          "user": {
            "title": "User",
            "description": "The user identifier (slug).",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "minLength": 1
          }
        }
      },
      "RepositoryPrivilegeInputRequestPatch": {
        "type": "object",
        "properties": {
          "privileges": {
            "description": "List of objects with explicit privileges to the repository.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RepositoryPrivilegeDict"
            }
          }
        }
      }
    }
  }
}
```