# Source: https://docs.akeyless.io/reference/updatelinkedtarget.md

# /update-linked-target

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
    "/update-linked-target": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateLinkedTarget",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateLinkedTarget"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateLinkedTargetResponse"
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
      "updateLinkedTargetResponse": {
        "description": "updateLinkedTargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateLinkedTargetOutput"
            }
          }
        }
      }
    },
    "schemas": {
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
      "updateLinkedTarget": {
        "description": "updateLinkedTarget is a command that updates an existing target. [Deprecated: Use target-update-linked command]",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "add-hosts": {
            "description": "A comma seperated list of new server hosts and server descriptions joined by semicolon ';' that will be added to the Linked Target hosts.",
            "type": "string",
            "x-go-name": "AddHosts"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "hosts": {
            "description": "A comma seperated list of server hosts and server descriptions joined by semicolon ';' (i.e. 'server-dev.com;My Dev server,server-prod.com;My Prod server description')",
            "type": "string",
            "x-go-name": "Hosts"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "keep-prev-version": {
            "description": "Whether to keep previous version [true/false]. If not set, use default according to account settings",
            "type": "string",
            "x-go-name": "KeepPrevVersion"
          },
          "name": {
            "description": "Linked Target name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "new-name": {
            "description": "New Linked Target name",
            "type": "string",
            "x-go-name": "NewTargetName"
          },
          "parent-target-name": {
            "description": "The parent Target name",
            "type": "string",
            "x-go-name": "ParentTargetName"
          },
          "rm-hosts": {
            "description": "Comma separated list of existing hosts that will be removed from Linked Target hosts.",
            "type": "string",
            "x-go-name": "RemoveHosts"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "Specifies the hosts type, relevant only when working without parent target",
            "type": "string",
            "x-go-name": "HostType"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateLinkedTargetOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```