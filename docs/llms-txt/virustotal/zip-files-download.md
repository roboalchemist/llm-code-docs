# Source: https://virustotal.readme.io/reference/zip-files-download.md

# Download a ZIP file

This endpoint is similar to [GET /zip\_files/{id}/download\_url](https://virustotal.readme.io/reference/zip-files-download-url), but it redirects you to the download URL. The download URL you are redirected to can be reused as many times as you want for a period of 1 hour. After that period the URL expires and can't be used anymore.

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
    "/intelligence/zip_files/{id}/download": {
      "get": {
        "summary": "Download a ZIP file",
        "description": "",
        "operationId": "zip-files-download",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "id",
            "in": "path",
            "description": "ZIP file identifier",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "responses": {
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