# Source: https://virustotal.readme.io/reference/get-retrohunt-job-relationships.md

# Retrieve matches for a Retrohunt job

Retrohunt jobs are related to other objects. As mentioned in the [Relationships](https://virustotal.readme.io/reference/relationships) section, those related objects can be retrieved by sending `GET` requests to the relationships URL.

The supported relationships for Retrohunt jobs are described in the [Retrohunt Jobs](https://virustotal.readme.io/reference/retrohunt-job-object) API object page.

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
    "/intelligence/retrohunt_jobs/{id}/matching_files": {
      "get": {
        "summary": "Retrieve matches for a Retrohunt job",
        "description": "",
        "operationId": "get-retrohunt-job-relationships",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Job identifier",
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
            "name": "limit",
            "in": "query",
            "description": "Maximum number of matching files to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
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