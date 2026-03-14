# Source: https://developers.smtp2go.com/reference/resend-subaccount-invitation.md

# Resend subaccount invitation

In the event that a subaccount didn't receive the invite you can resend it

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
      "name": "SUBACCOUNTS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/subaccount/reinvite": {
      "post": {
        "tags": [
          "SUBACCOUNTS"
        ],
        "summary": "Resend subaccount invitation",
        "description": "In the event that a subaccount didn't receive the invite you can resend it",
        "operationId": "resend-subaccount-invitation",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "email"
                ],
                "properties": {
                  "email": {
                    "type": "string",
                    "description": "The email address of the subaccount you want to resend the invitation email to"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Invitation sent",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "d02ce100-2cfd-11eb-ab52-408d5cce2644",
                      "data": "Successfully resent invite email to subaccount test@example.com"
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
                      "example": "0ef3f48a-2cfb-11eb-aee9-408d5cce2644"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "id"
                      ],
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "NDU5OTgw"
                        },
                        "email": {
                          "type": "string",
                          "example": "test@example.com"
                        },
                        "name": {
                          "type": "string",
                          "example": "Test Person"
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