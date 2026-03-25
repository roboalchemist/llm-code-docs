# Source: https://docs.akeyless.io/reference/usclist.md

# /usc-list

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
    "/usc-list": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "uscList",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/uscList"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/uscListResponse"
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
      "uscListResponse": {
        "description": "uscListResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/UscListSecretsOutput"
            }
          }
        }
      }
    },
    "schemas": {
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
      "ObjectType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/external-secrets-manager/base"
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
      "UscListSecretsOutput": {
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
      "uscList": {
        "description": "uscList is a command that lists the secrets of a Universal Secrets Connector",
        "type": "object",
        "required": [
          "usc-name"
        ],
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "object-type": {
            "$ref": "#/components/schemas/ObjectType"
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
          },
          "usc-name": {
            "description": "Name of the Universal Secrets Connector item",
            "type": "string",
            "x-go-name": "ExternalSecretManagerName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```