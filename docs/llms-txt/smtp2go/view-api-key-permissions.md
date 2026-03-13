# Source: https://developers.smtp2go.com/reference/view-api-key-permissions.md

# View Permissions

Retrieve a list of endpoints this API Key can use

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "SMTP2GO API v3.0.3",
    "version": "3.0.3"
  },
  "servers": [
    {
      "url": "https://api.smtp2go.com/v3",
      "description": "Regionless"
    },
    {
      "url": "https://us-api.smtp2go.com/v3",
      "description": "US Region"
    },
    {
      "url": "https://eu-api.smtp2go.com/v3",
      "description": "EU Region"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "X-Smtp2go-Api-Key",
        "x-default": ""
      }
    }
  },
  "tags": [
    {
      "name": "API KEYS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/api_keys/permissions": {
      "post": {
        "tags": [
          "API KEYS"
        ],
        "summary": "View Permissions",
        "description": "Retrieve a list of endpoints this API Key can use",
        "operationId": "view-api-key-permissions",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {}
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successfully retrieved API key permissions",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "f3e50113-deb2-4e54-9675-2ea497c3732e",
                      "data": [
                        "/email/send",
                        "/api_keys/view"
                      ]
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "required": [
                    "data",
                    "request_id"
                  ],
                  "properties": {
                    "data": {
                      "type": "array",
                      "description": "An array of API key results",
                      "items": {
                        "type": "object",
                        "required": [
                          "request_id",
                          "data"
                        ],
                        "properties": {
                          "request_id": {
                            "type": "string",
                            "example": "aa253464-0bd0-467a-b24b-6159dcd7be60"
                          },
                          "data": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    },
                    "request_id": {
                      "type": "string",
                      "example": [
                        "/email/send",
                        "/api_keys/view"
                      ]
                    }
                  }
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
                    "value": {
                      "request_id": "22e5acba-43bf-11e6-ae42-408d5cce2644",
                      "data": {
                        "error": "You do not have permission to access this API endpoint",
                        "error_code": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "22e5acba-43bf-11e6-ae42-408d5cce2644"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "error": {
                          "type": "string",
                          "example": "You do not have permission to access this API endpoint"
                        },
                        "error_code": {
                          "type": "string",
                          "example": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
                        }
                      }
                    }
                  }
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
    "headers": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "explorer-enabled": true,
    "proxy-enabled": true,
    "samples-enabled": true
  }
}
```