# Source: https://virustotal.readme.io/reference/files-download.md

# Download a file

> 🚧 Special privileges required
>
> This endpoint is only available for users with premium privileges.

This endpoint is similar to [GET /files/{id}/download\_url](https://virustotal.readme.io/reference/files-download-url), but it redirects you to the download URL. The download URL you are redirected to can be reused as many times as you want for a period of 1 hour. After that period the URL expires and can't be used anymore.

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
    "/files/{id}/download": {
      "get": {
        "summary": "Download a file",
        "description": "",
        "operationId": "files-download",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "SHA-256, SHA-1 or MD5 identifying the file",
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