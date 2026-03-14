# Source: https://developers.smtp2go.com/reference/add-a-single-sender-email.md

# Add a single sender email

Use the API to add a single sender email address to your account, to use from which to send mail. If the email address has previously been added and not yet verified, this action will simply resend the verification email.

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
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/single_sender_emails/add": {
      "post": {
        "tags": [
          "SINGLE SENDER EMAILS"
        ],
        "summary": "Add a single sender email",
        "description": "Use the API to add a single sender email address to your account, to use from which to send mail. If the email address has previously been added and not yet verified, this action will simply resend the verification email.",
        "operationId": "add-a-single-sender-email",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "email_address"
                ],
                "properties": {
                  "email_address": {
                    "type": "string",
                    "description": "The email address that you wish to send emails from",
                    "default": "send@example.com"
                  },
                  "message": {
                    "type": "string",
                    "description": "(Optional) If provided, will add a text only message to the email."
                  },
                  "subaccount_id": {
                    "type": "string",
                    "description": "If you wish to make this API call on behalf of a subaccount then include its unique ID here"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Single sender email added",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "just_returns_this": "ok"
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "required": [
                    "request_id"
                  ],
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "e023461c-8c86-11e9-b984-408d5cce2644"
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