# Source: https://virustotal.readme.io/reference/delete-hunting-ruleset-editor.md

# Revoke Livehunt ruleset edit permission from a user or group

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
    "/intelligence/hunting_rulesets/{id}/relationships/editors/{user_or_group_id}": {
      "delete": {
        "summary": "Revoke Livehunt ruleset edit permission from a user or group",
        "description": "",
        "operationId": "delete-hunting-ruleset-editor",
        "parameters": [
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
            "name": "id",
            "in": "path",
            "description": "Ruleset identifier",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "user_or_group_id",
            "in": "path",
            "description": "User or group ID",
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
                    "value": ""
                  }
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