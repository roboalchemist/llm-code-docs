# Source: https://virustotal.readme.io/reference/get-private-files-behaviours-memdump.md

# Get the memdump file generated during a private file’s behavior analysis

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Fetch the PCAP file associated with the sandbox execution.

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
    "/file_behaviours/{sandbox_id}/memdump": {
      "get": {
        "summary": "Get the memdump file generated during a private file’s behavior analysis",
        "description": "",
        "operationId": "get-private-files-behaviours-memdump",
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