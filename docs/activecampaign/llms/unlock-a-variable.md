# Source: https://developers.activecampaign.com/reference/unlock-a-variable.md

# Unlock a Variable

Lock a personalization variable

You can unlock previously locked Variables to allow editing. Only admin users can lock or unlock a message variable.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/personalizations/{variableID}/unlock": {
      "patch": {
        "description": "",
        "operationId": "patch_new-endpoint",
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    },
                    "message": {
                      "type": "string"
                    }
                  }
                },
                "examples": {
                  "New Example 1": {
                    "summary": "New Example 1",
                    "value": {
                      "success": false,
                      "message": "Only admin can lock/unlock personalizations"
                    }
                  },
                  "No rights to unlock (not an admin)": {
                    "summary": "No rights to unlock (not an admin)",
                    "value": {
                      "success": true,
                      "message": "Personalization updated successfully"
                    }
                  }
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "path",
            "name": "variableID",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ]
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```