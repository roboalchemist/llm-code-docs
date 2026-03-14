# Source: https://virustotal.readme.io/reference/file-feed-download.md

# Download a file published in the file feed

> 🚧 Special privileges required
>
> File feeds endpoints are only available to users with a File feeds license. For this particular endpoint, download file privilege is also required. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

Each JSON object contained in the file feed packages include a URL to this API endpoint to download the corresponding file. The link only works during the feed's lifetime, which is 7 days. Check [/feeds/files/{time}](https://virustotal.readme.io/reference/feeds-file) for more information.

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
    "/feeds/files/{token}/download": {
      "get": {
        "summary": "Download a file published in the file feed",
        "description": "",
        "operationId": "file-feed-download",
        "parameters": [
          {
            "name": "token",
            "in": "path",
            "description": "Download token. It can be found inside the file's properties in the file feed.",
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