# Source: https://virustotal.readme.io/reference/delete-file-private-scanning.md

# Delete a private file report

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

This endpoint deletes a private file from storage, as well as all the PrivateFile and PrivateAnalysis associated with it (unless `only_from_storage=true` is used.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-private-scanning",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/files/{id}": {
      "delete": {
        "summary": "Delete a private file report",
        "description": "",
        "operationId": "delete-file-private-scanning",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "File's SHA-256",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "only_from_storage",
            "in": "query",
            "description": "If true, only the file will be deleted from storage, but the generated reports and analyses won't.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```