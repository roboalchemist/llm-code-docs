# Source: https://virustotal.readme.io/reference/transfer-livehunt-ruleset-to-another-user.md

# Transfer Livehunt ruleset to another user

Note: The new owner must be a member of the same group the ruleset was created with.

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
    "/intelligence/hunting_rulesets/{id}/relationships/owner": {
      "post": {
        "summary": "Transfer Livehunt ruleset to another user",
        "description": "",
        "operationId": "transfer-livehunt-ruleset-to-another-user",
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "A user object descriptor",
                    "format": "json"
                  }
                }
              }
            }
          }
        },
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
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl --request POST \\\n  --url https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/{id}/relationships/owner \\\n  --header 'x-apikey: <your API key>'\n  --data='{\"data\": {\"type\": \"user\", \"id\": \"<user id>\"}}'"
            }
          ],
          "samples-languages": [
            "curl"
          ]
        }
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