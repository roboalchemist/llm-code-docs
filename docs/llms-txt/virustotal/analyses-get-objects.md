# Source: https://virustotal.readme.io/reference/analyses-get-objects.md

# Get objects related to an analysis

As mentioned in the [Relationships](https://virustotal.readme.io/reference/relationships) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Available relationships are described in the [analysis](https://virustotal.readme.io/reference/analyses-object) object documentation.

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
    "/analyses/{id}/{relationship}": {
      "get": {
        "summary": "Get objects related to an analysis",
        "description": "",
        "operationId": "analyses-get-objects",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Analysis identifier",
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
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://virustotal.readme.io/reference/analyses-object#relationships))",
            "schema": {
              "type": "string"
            },
            "required": true
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