# Source: https://virustotal.readme.io/reference/private-files-upload-url.md

# Get a URL for uploading large files

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

For uploading files smaller than 32MB you can simply use the [POST /files](https://virustotal.readme.io/reference/upload-file-private-scanning) endpoint, but for larger files you need to obtain a special upload URL first, and then send the `POST` request to the upload URL instead of sending it to `/private/files`. The `POST` request should have the same format expected by the  [POST /files](https://virustotal.readme.io/reference/upload-file-private-scanning) endpoint. Each upload URL can be used only once.

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
    "/files/upload_url": {
      "get": {
        "summary": "Get a URL for uploading large files",
        "description": "",
        "operationId": "private-files-upload-url",
        "parameters": [
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