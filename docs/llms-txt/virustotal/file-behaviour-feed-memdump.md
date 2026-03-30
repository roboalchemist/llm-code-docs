# Source: https://virustotal.readme.io/reference/file-behaviour-feed-memdump.md

# Get the memdump file generated during a file’s behavior analysis

> 🚧 Special privileges required
>
> Sandbox analyses feeds endpoints are only available to users with a Sandbox feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

Each JSON object contained in the file behaviour feed packages include a URL to this API endpoint to download the extracted memdump from the file's sandbox execution. The available in the feed link already includes the download token required by this endpoint. The following snippet represents the JSON structure in the file behaviour feed that takes to the link:

```json JSON structure
{
  "context_attributes": {
    "memdump": "https://www.virustotal.com/api/v3/feeds/file_behaviours/<TOKEN>/memdump"
  }
}
```

The link only works during the feed's lifetime. Check [/feeds/file\_behaviours/{time}](https://virustotal.readme.io/reference/feeds-file-behaviour) for more information.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-enterprise",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [],
  "paths": {
    "/feeds/file_behaviours/{token}/memdump": {
      "get": {
        "summary": "Get the memdump file generated during a file’s behavior analysis",
        "description": "",
        "operationId": "file-behaviour-feed-memdump",
        "parameters": [
          {
            "name": "token",
            "in": "path",
            "description": "Download token. It can be found inside the behaviour object's properties in the behaviour feed.",
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