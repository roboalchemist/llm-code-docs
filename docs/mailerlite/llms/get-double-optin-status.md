# Source: https://developers-classic.mailerlite.com/reference/get-double-optin-status.md

# /settings/double_optin

Retrieve the status if double opt-in for API and integrations is enabled

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "V2 production",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api.mailerlite.com/api/v2"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "X-MailerLite-ApiKey",
        "in": "header",
        "x-default": "your api key"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/settings/double_optin": {
      "get": {
        "summary": "/settings/double_optin",
        "description": "Retrieve the status if double opt-in for API and integrations is enabled",
        "operationId": "get-double-optin-status",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"enabled\": true,\n  \"previewPaths\": {\n    \"pagePath\": \"/data/a/0/1/confirmation_thank_you.html\",\n    \"emailPath\": \"/data/a/0/1/mails/0/1/mail.html\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "enabled": {
                      "type": "boolean",
                      "example": true,
                      "default": true
                    },
                    "previewPaths": {
                      "type": "object",
                      "properties": {
                        "pagePath": {
                          "type": "string",
                          "example": "/data/a/0/1/confirmation_thank_you.html"
                        },
                        "emailPath": {
                          "type": "string",
                          "example": "/data/a/0/1/mails/0/1/mail.html"
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
                    "value": "{\n    \"error\": {\n        \"code\": 400,\n        \"message\": \"You must provide \\\"enable\\\" body parameter with a boolean value.\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "object",
                      "properties": {
                        "code": {
                          "type": "integer",
                          "example": 400,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "You must provide \"enable\" body parameter with a boolean value."
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "403",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": {\n        \"code\": 403,\n        \"message\": \"Account is not approved so it is impossible to enable double opt-in.\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "object",
                      "properties": {
                        "code": {
                          "type": "integer",
                          "example": 403,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "Account is not approved so it is impossible to enable double opt-in."
                        }
                      }
                    }
                  }
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
              "code": "curl -v https://api.mailerlite.com/api/v2/settings/double_optin \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
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
    "headers": [
      {
        "key": "X-MailerLite-ApiDocs",
        "value": "true"
      }
    ],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true,
  "_id": "58b53b141065f9c438aa1afe:5a0329d5d46da20032a46135"
}
```