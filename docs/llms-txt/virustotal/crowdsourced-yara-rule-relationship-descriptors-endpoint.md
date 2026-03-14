# Source: https://virustotal.readme.io/reference/crowdsourced-yara-rule-relationship-descriptors-endpoint.md

# Get objects descriptors related to a Crowdsourced YARA rule

Same as [/yara\_rules/{id}/{relationships}](https://virustotal.readme.io/reference/crowdsourced-yara-rule-relationship-endpoint) except it returns just the related object's descriptor (and context attributes, if any) instead of returning all attributes.

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
    "/yara_rules/{id}/relationships/{relationship}": {
      "get": {
        "summary": "Get objects descriptors related to a Crowdsourced YARA rule",
        "description": "",
        "operationId": "crowdsourced-yara-rule-relationship-descriptors-endpoint",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Rule identifier",
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
            "description": "Relationship name",
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