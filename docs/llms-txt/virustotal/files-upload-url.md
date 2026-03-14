# Source: https://virustotal.readme.io/reference/files-upload-url.md

# Get a URL for uploading large files

Get a URL for uploading files larger than 32MB

For uploading files smaller than 32MB you can simply use the [POST /files](https://virustotal.readme.io/reference/files-scan) endpoint, but for larger files you need to obtain a special upload URL first, and then send the `POST` request to the upload URL instead of sending it to `/files`. The `POST` request should have the same format expected by the  [POST /files](https://virustotal.readme.io/reference/files-scan) endpoint. Each upload URL can be used only once.

> 📘 Files larger than 200MBs
>
> Notice that although the actual size limit is 650MBs, files larger than 200MBs tend to be bundles of some sort, (compressed files, ISO images, etc.) in these cases it makes sense to upload the inner individual files instead for several reasons, as an example:
>
> * Engines tend to have performance issues on big files (timeouts, some may not even scan them).
> * Some engines are not able to inspect certain file types whereas they will be able to inspect the inner files if submitted.
> * When scanning a big bundle you lose context on which specific inner file is causing the detection.

```json
{
  "data": "http://www.virustotal.com/_ah/upload/AMmfu6b-_DXUeFe36Sb3b0F4B8mH9Nb-CHbRoUNVOPwG/"
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
    "/files/upload_url": {
      "get": {
        "summary": "Get a URL for uploading large files",
        "description": "Get a URL for uploading files larger than 32MB",
        "operationId": "files-upload-url",
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