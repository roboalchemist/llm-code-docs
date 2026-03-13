# Source: https://developers.smtp2go.com/reference/add-a-suppression.md

# Add a suppression

Suppresses the specified email address or domain

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
      "name": "SUPPRESSIONS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/suppression/add": {
      "post": {
        "tags": [
          "SUPPRESSIONS"
        ],
        "summary": "Add a suppression",
        "description": "Suppresses the specified email address or domain",
        "operationId": "add-a-suppression",
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
                    "description": "The email address or domain you would like to suppress from deliveries"
                  },
                  "block_description": {
                    "type": "string",
                    "description": "The description given for suppressing the email or domain from deliveries"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Suppression successful",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "aa253464-0bd0-467a-b24b-6159dcd7be60",
                      "data": {
                        "added": true,
                        "block_description": "",
                        "email_address": "temp@example.com"
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
                      "example": "aa253464-0bd0-467a-b24b-6159dcd7be60"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "block_description",
                        "added",
                        "email_address"
                      ],
                      "properties": {
                        "block_description": {
                          "type": "string",
                          "example": "No longer a customer."
                        },
                        "added": {
                          "type": "boolean",
                          "example": true,
                          "default": true
                        },
                        "email_address": {
                          "type": "string",
                          "example": "test@example.com"
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