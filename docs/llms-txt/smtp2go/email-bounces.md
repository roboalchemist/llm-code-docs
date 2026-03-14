# Source: https://developers.smtp2go.com/reference/email-bounces.md

# Email bounces

Retrieve a summary of bounces and rejects, for the last 30 days.

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
      "name": "STATISTICS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/stats/email_bounces": {
      "post": {
        "tags": [
          "STATISTICS"
        ],
        "summary": "Email bounces",
        "description": "Retrieve a summary of bounces and rejects, for the last 30 days.",
        "operationId": "email-bounces",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [],
                "properties": {
                  "username": {
                    "type": "string",
                    "description": "Allows statistics to be returned for a specific user."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Bounce report",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "ee9b9484-63eb-11ed-8da7-f23c9216ce11",
                      "data": {
                        "emails": 1,
                        "rejects": 0,
                        "softbounces": 0,
                        "hardbounces": 0,
                        "bounce_percent": "0.00"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "required": [
                    "request_id",
                    "data"
                  ],
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "2917fc07-d685-4fea-b49a-14087058461f"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "emails",
                        "hardbounces",
                        "bounce_percent",
                        "softbounces",
                        "rejects"
                      ],
                      "properties": {
                        "emails": {
                          "type": "integer",
                          "example": 159,
                          "default": 0
                        },
                        "hardbounces": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        },
                        "bounce_percent": {
                          "type": "string",
                          "example": "0.00"
                        },
                        "softbounces": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        },
                        "rejects": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        }
                      }
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