# Source: https://virustotal.readme.io/reference/get-private-files-behaviours-html.md

# Get a detailed HTML behaviour report

HTML sandbox report

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Returns a [Private File Behaviour](https://virustotal.readme.io/reference/private-file-behaviours) object as an HTML report. It expects the sandbox ID returned by the [GET /private/files/{id}/behaviours](https://virustotal.readme.io/reference/get-all-behaviour-reports-from-a-private-file) endpoint.

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
    "/file_behaviours/{sandbox_id}/html": {
      "get": {
        "summary": "Get a detailed HTML behaviour report",
        "description": "HTML sandbox report",
        "operationId": "get-private-files-behaviours-html",
        "parameters": [
          {
            "name": "sandbox_id",
            "in": "path",
            "description": "Sandbox report ID",
            "schema": {
              "type": "string"
            },
            "required": true
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
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": "<!DOCTYPE html>\n<html lang=\"en\">\n  ..."
                  }
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