# Source: https://developers.activecampaign.com/reference/lock-a-variable.md

# Lock a Variable

Lock a personalization variable

You can lock Variables to prevent unauthorized editing or being overwritten by third-party integrations. Only admin users can lock or unlock a message variable.

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
    "/personalizations/{variableID}/lock": {
      "patch": {
        "description": "",
        "operationId": "get_{personalizationId}lock",
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "description": ""
                    },
                    "message": {
                      "type": "string"
                    }
                  }
                },
                "examples": {
                  "Success": {
                    "summary": "Success",
                    "value": {
                      "success": true,
                      "message": "Personalization updated successfully"
                    }
                  },
                  "No rights to lock (not an admin)": {
                    "summary": "No rights to lock (not an admin)",
                    "value": {
                      "success": false,
                      "message": "Only admin can lock/unlock personalizations"
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