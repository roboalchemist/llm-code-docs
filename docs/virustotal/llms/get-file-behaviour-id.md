# Source: https://virustotal.readme.io/reference/get-file-behaviour-id.md

# Get a file behavior report from a sandbox

Fetches a [File behaviour](https://virustotal.readme.io/reference/file-behaviour-summary) object by ID.

[block:callout]
{
  "type": "info",
  "body": "This API call only fetches the behaviour report for a single behavioural analysis you can fetch all of them with https://developers.virustotal.com/reference/file-all-behaviours-summary"
}
[/block]

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
    "/file_behaviours/{sandbox_id}": {
      "get": {
        "summary": "Get a file behavior report from a sandbox",
        "description": "",
        "operationId": "get-file-behaviour-id",
        "parameters": [
          {
            "name": "sandbox_id",
            "in": "path",
            "description": "Sandbox report ID. See \"Sandbox Report identifiers\" section below for more info.",
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