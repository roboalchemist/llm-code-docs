# Source: https://virustotal.readme.io/reference/get-hunting-ruleset-relationship.md

# Get object descriptors related to a Livehunt ruleset

Same as [/hunting\_rulesets/{id}/{relationships}](https://virustotal.readme.io/reference/get-hunting-ruleset-full-relationships) except it returns just the related object's descriptor (and context attributes, if any) instead of returning all attributes.

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
    "/intelligence/hunting_rulesets/{id}/relationships/{relationship}": {
      "get": {
        "summary": "Get object descriptors related to a Livehunt ruleset",
        "description": "",
        "operationId": "get-hunting-ruleset-relationship",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Ruleset identifier",
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
            "description": "Relationship name (see [table](https://virustotal.readme.io/reference/hunting-ruleset-object#relationships))",
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