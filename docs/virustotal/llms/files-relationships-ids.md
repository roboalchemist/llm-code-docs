# Source: https://virustotal.readme.io/reference/files-relationships-ids.md

# Get object descriptors related to a file

This endpoint is the same as [/files/{id}/{relationship}](https://virustotal.readme.io/reference/files-relationships) except it returns just the related object's IDs (and context attributes, if any) instead of returning all attributes.

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
    "/files/{id}/relationships/{relationship}": {
      "get": {
        "summary": "Get object descriptors related to a file",
        "description": "",
        "operationId": "files-relationships-ids",
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
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://virustotal.readme.io/reference/files#relationships))",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of related objects to retrieve",
            "schema": {
              "type": "string",
              "default": "10"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
            "schema": {
              "type": "string"
            }
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