# Source: https://virustotal.readme.io/reference/monitor-item-comments.md

# Retrieve partner's comments on a file

```json
{
  "data": [
    {
      "type": "monitor_hash_comment",
      "id": "6620bdb508ab363eee95fd511ae88e2e38daf948b117bd49bcf8609f87cc86de-{engine name}",
      "attributes": {
        "comment": "This is an example comment.",
        "date": 1519222846,
        "detection": "confirmed",
        "engine": "{engine name}",
        "sha256": "6620bdb508ab363eee95fd511ae88e2e38daf948b117bd49bcf8609f87cc86de"
      }
    }
  ]
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
    "/monitor/items/{id}/comments": {
      "get": {
        "summary": "Retrieve partner's comments on a file",
        "description": "",
        "operationId": "monitor-item-comments",
        "parameters": [
          {
            "name": "cursor",
            "in": "query",
            "description": "Continue listing after this offset",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of analyses to retrieve",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "id",
            "in": "path",
            "description": "Monitor item identifier",
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