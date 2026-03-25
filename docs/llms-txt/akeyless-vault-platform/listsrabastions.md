# Source: https://docs.akeyless.io/reference/listsrabastions.md

# /list-sra-bastions

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
    "/list-sra-bastions": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "listSRABastions",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/listSRABastions"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/listSRABastionsResponse"
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
      "listSRABastionsResponse": {
        "description": "listSRABastionsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/BastionsList"
            }
          }
        }
      }
    },
    "schemas": {
      "BastionListEntry": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessID"
          },
          "allowed_access_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedAccessIDs"
          },
          "allowed_urls": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedUrls"
          },
          "allowed_urls_per_instance": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "AllowedUrlsPerInstance"
          },
          "bastion_ssh_port": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "BastionSSHPort"
          },
          "bastion_urls_per_type": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "BastionURLsPerType"
          },
          "cluster_name": {
            "type": "string",
            "x-go-name": "ClusterName"
          },
          "display_name": {
            "type": "string",
            "x-go-name": "DisplayName"
          },
          "has_gateway_identity": {
            "type": "boolean",
            "x-go-name": "HasGatewayIdentity"
          },
          "last_report": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "LastReport"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "BastionsList": {
        "type": "object",
        "properties": {
          "clusters": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BastionListEntry"
            },
            "x-go-name": "Clusters"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "listSRABastions": {
        "type": "object",
        "title": "listSRABastions is a command that returns a list of bastions.",
        "properties": {
          "allowed-urls-only": {
            "description": "Filter the response to show only bastions allowed URLs",
            "type": "boolean",
            "default": false,
            "x-go-name": "BastionsAllowedURLsOnly"
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