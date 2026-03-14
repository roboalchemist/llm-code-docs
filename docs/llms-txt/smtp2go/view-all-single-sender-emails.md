# Source: https://developers.smtp2go.com/reference/view-all-single-sender-emails.md

# View single sender emails

Returns a list of single sender email addresses on your account, along with their verification status. If you include a email_address, the response will only include items matching this search.

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
    "/single_sender_emails/view": {
      "post": {
        "tags": [
          "SINGLE SENDER EMAILS"
        ],
        "summary": "View single sender emails",
        "description": "Returns a list of single sender email addresses on your account, along with their verification status. If you include a email_address, the response will only include items matching this search.",
        "operationId": "view-all-single-sender-emails",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "email_address": {
                    "type": "string",
                    "description": "(Optional) If provided, only return email addresses that match value"
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
            "description": "List of single sender emails",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "data": {
                        "request_id": "e023461c-8c86-11e9-b984-408d5cce2644",
                        "senders": [
                          {
                            "email_address": "test@test.com",
                            "verified": true
                          }
                        ]
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "required": [
                        "request_id",
                        "senders"
                      ],
                      "properties": {
                        "request_id": {
                          "type": "string",
                          "example": "e023461c-8c86-11e9-b984-408d5cce2644"
                        },
                        "senders": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "required": [
                              "email_address",
                              "verified"
                            ],
                            "properties": {
                              "email_address": {
                                "type": "string",
                                "example": "test@test.com"
                              },
                              "verified": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              }
                            }
                          }
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