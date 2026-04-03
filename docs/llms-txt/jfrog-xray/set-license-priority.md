# Source: https://docs.jfrog.com/security/reference/set-license-priority.md

# Set License Priority

Set License Priority.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Xray REST APIs",
    "description": "Combined JFrog Xray REST API specification (all endpoints).",
    "version": "3.140"
  },
  "servers": [
    {
      "url": "https://jf.example.com/xray",
      "description": "JFrog Platform (Xray)"
    }
  ],
  "security": [
    {
      "basicAuth": []
    }
  ],
  "paths": {
    "/api/v1/licensesNames/priorities": {
      "post": {
        "operationId": "set-license-priority",
        "summary": "Set License Priority",
        "description": "Set License Priority.",
        "tags": [
          "Legal V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "key": {
                    "type": "string"
                  },
                  "priority": {
                    "type": "integer"
                  }
                },
                "required": [
                  "key",
                  "priority"
                ]
              },
              "example": {
                "key": "Apache-2.0",
                "priority": 198
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success - Set license priority",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "info"
                  ]
                },
                "example": {
                  "info": "License priority have been set successfully to the license key 'Apache-2.0'. New priority:198."
                }
              }
            }
          },
          "400": {
            "description": "Failed to set priority to license",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "403": {
            "description": "Permission denied",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication using username/password or API key"
      }
    }
  },
  "tags": [
    {
      "name": "Legal V1",
      "description": "APIs from Legal V1"
    }
  ]
}
```