# Source: https://virustotal.readme.io/reference/private-scanning-download-zip-file.md

# Download a ZIP file

This endpoint is similar to [GET /private/zip\_files/{id}/download\_url](https://virustotal.readme.io/reference/private-scanning-get-zip-download-url), but it redirects you to the download URL. The download URL you are redirected to can be reused as many times as you want for a period of 1 hour. After that period the URL expires and can't be used anymore.

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
    "/zip_files/{id}/download": {
      "get": {
        "summary": "Download a ZIP file",
        "description": "",
        "operationId": "private-scanning-download-zip-file",
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