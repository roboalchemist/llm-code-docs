# Source: https://docs.akeyless.io/reference/esmlist.md

# /esm-list

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "The purpose of this application is to provide access to Akeyless API.",
    "title": "Akeyless API",
    "contact": {
      "name": "Akeyless",
      "url": "http://akeyless.io",
      "email": "support@akeyless.io"
    },
    "version": "3.0"
  },
  "paths": {
    "/esm-list": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "esmList",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/esmList"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/esmListResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://api.akeyless.io"
    }
  ],
  "components": {
    "responses": {
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      },
      "esmListResponse": {
        "description": "esmListResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/EsmListSecretsOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "EsmListSecretsOutput": {
        "type": "object",
        "properties": {
          "secrets_list": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SecretInfo"
            },
            "x-go-name": "SecretsList"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "GithubMetadata": {
        "type": "object",
        "properties": {
          "environment_name": {
            "type": "string",
            "x-go-name": "EnvironmentName"
          },
          "organization_name": {
            "type": "string",
            "x-go-name": "OrganizationName"
          },
          "repository": {
            "type": "string",
            "x-go-name": "Repository"
          },
          "repository_access": {
            "type": "string",
            "x-go-name": "RepositoryAccess"
          },
          "scope": {
            "type": "string",
            "x-go-name": "Scope"
          },
          "selected_repositories": {
            "type": "string",
            "x-go-name": "SelectedRepositories"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/external-secrets-manager/base"
      },
      "JSONError": {
        "type": "object",
        "title": "JSONError wraps an error with JSON object.",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Err"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client"
      },
      "SecretInfo": {
        "type": "object",
        "properties": {
          "created": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "Created"
          },
          "description": {
            "type": "string",
            "x-go-name": "Description"
          },
          "expiration": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "Expiration"
          },
          "github": {
            "$ref": "#/components/schemas/GithubMetadata"
          },
          "key_id": {
            "type": "string",
            "x-go-name": "KeyId"
          },
          "last_retrieved": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "LastRetrieved"
          },
          "location": {
            "x-go-name": "Location"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "region": {
            "type": "string",
            "x-go-name": "Region"
          },
          "secret_id": {
            "type": "string",
            "x-go-name": "SecretId"
          },
          "status": {
            "type": "boolean",
            "x-go-name": "Status"
          },
          "tags": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "thumbprint": {
            "type": "string",
            "x-go-name": "Thumbprint"
          },
          "type": {
            "type": "string",
            "x-go-name": "Type"
          },
          "version": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/external-secrets-manager/base"
      },
      "esmList": {
        "description": "esmList is a command that lists the secrets of an External Secrets Manager",
        "type": "object",
        "required": [
          "esm-name"
        ],
        "properties": {
          "esm-name": {
            "description": "Name of the External Secrets Manager item",
            "type": "string",
            "x-go-name": "ExternalSecretManagerName"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```