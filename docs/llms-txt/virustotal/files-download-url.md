# Source: https://virustotal.readme.io/reference/files-download-url.md

# Get a file’s download URL

> 🚧 Special privileges required
>
> This endpoint is only available for users with special privileges.

This endpoint returns a signed URL from where you can download the specified file. Getting the URL counts as a file download in your quota, even if you don't actually download the file, but once you have the URL you can use it to download the file multiple times without consuming any quota at all. The URL expires after 1 hour.

```json
{
  "data": "https://vtsamples.commondatastorage.googleapis.com/275a..fd0f?GoogleAccessId=758681729565-rc7fcckv235v1@developer.gserviceaccount.com&Expires=1524733537&Signature=GRs9WLy...oHA%3D"
}
```

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
    "/files/{id}/download_url": {
      "get": {
        "summary": "Get a file’s download URL",
        "description": "",
        "operationId": "files-download-url",
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