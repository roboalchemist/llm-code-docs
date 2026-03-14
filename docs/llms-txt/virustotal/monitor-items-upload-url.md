# Source: https://virustotal.readme.io/reference/monitor-items-upload-url.md

# Get a URL for uploading files larger than 32MB

For uploading files smaller than 32MB you can simply send a POST request to the [/items](https://virustotal.readme.io/reference/monitor-items-create) endpoint, but for larger files you need to get a special upload URL first. This endpoint returns one of those URLs. The returned URL can be used as a drop-in replacement for the  [/items](https://virustotal.readme.io/reference/monitor-items-create) endpoint. A new upload URL should be generated each big file upload.

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
    "/monitor/items/upload_url": {
      "get": {
        "summary": "Get a URL for uploading files larger than 32MB",
        "description": "",
        "operationId": "monitor-items-upload-url",
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
              "text/plain": {
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