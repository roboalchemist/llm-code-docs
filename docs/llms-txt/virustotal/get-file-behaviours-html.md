# Source: https://virustotal.readme.io/reference/get-file-behaviours-html.md

# Get a detailed HTML behaviour report

HTML sandbox report

Returns a [File behaviour](https://virustotal.readme.io/reference/file-behaviour-summary) object as an HTML report.

## Sandbox Report identifiers

A Sandbox report ID has two main components: the **analysed file's SHA256** and the **sandbox name**. These two components are joined by a `_` character. For example, ID `5353e23f3653402339c93a8565307c6308ff378e03fcf23a4378f31c434030b0_VirusTotal Jujubox` fetches the sandbox report for a file having a SHA256 `5353e23f3653402339c93a8565307c6308ff378e03fcf23a4378f31c434030b0` analysed in the `VirusTotal Jujubox` sandbox.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
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
        "operationId": "get-file-behaviours-html",
        "parameters": [
          {
            "name": "sandbox_id",
            "in": "path",
            "description": "Sandbox report ID.",
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
        "deprecated": false,
        "security": []
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