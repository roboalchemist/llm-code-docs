# Source: https://virustotal.readme.io/reference/crowdsourced-yara-rule-relationship-endpoint.md

# Get objects related to a Crowdsourced YARA rule

YARA rule objects have relationships to other objects. As mentioned in the [Relationships](https://virustotal.readme.io/reference/relationships) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

The relationships supported by YARA rule objects are documented in the [YARA Rules](https://virustotal.readme.io/reference/yara-rule#relationships) API object page.

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
    "/yara_rules/{id}/{relationship}": {
      "get": {
        "summary": "Get objects related to a Crowdsourced YARA rule",
        "description": "",
        "operationId": "crowdsourced-yara-rule-relationship-endpoint",
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