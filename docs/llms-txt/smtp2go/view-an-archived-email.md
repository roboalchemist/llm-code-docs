# Source: https://developers.smtp2go.com/reference/view-an-archived-email.md

# View an archived email

Fetch an archived email using the email_id

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
    "/archive/email": {
      "post": {
        "tags": [
          "EMAIL ARCHIVE"
        ],
        "summary": "View an archived email",
        "description": "Fetch an archived email using the email_id",
        "operationId": "view-an-archived-email",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "email_id"
                ],
                "properties": {
                  "email_id": {
                    "type": "string",
                    "description": "The unique email_id of the archived email you wish to retrieve",
                    "example": "1u0SwL-B9zBpi9ffUq-JAB2"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Archived email",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "13dd3376-40fa-11ec-9fc6-f23c9216bf47",
                      "data": {
                        "attachment_count": 0,
                        "attachments": [],
                        "byte_count": 1428,
                        "email_id": "1u0SwL-B9zBpi9ffUq-JAB2",
                        "envelope_from": "test@test.com",
                        "headers": "...",
                        "recipient": "test@test.com",
                        "sender": "test@test.com",
                        "sent": "2021-10-19T21:35:40Z",
                        "subject": "test",
                        "to": "test@test.com",
                        "url": "...",
                        "username": "api-12345678"
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
                      "example": "13dd3376-40fa-11ec-9fc6-f23c9216bf47"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "attachment_count": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        },
                        "attachments": {
                          "type": "array"
                        },
                        "byte_count": {
                          "type": "integer",
                          "example": 1428,
                          "default": 0
                        },
                        "email_id": {
                          "type": "string",
                          "example": "1u0SwL-B9zBpi9ffUq-JAB2"
                        },
                        "envelope_from": {
                          "type": "string",
                          "example": "test@test.com"
                        },
                        "headers": {
                          "type": "string",
                          "example": "..."
                        },
                        "recipient": {
                          "type": "string",
                          "example": "test@test.com"
                        },
                        "sender": {
                          "type": "string",
                          "example": "test@test.com"
                        },
                        "sent": {
                          "type": "string",
                          "example": "2021-10-19T21:35:40Z"
                        },
                        "subject": {
                          "type": "string",
                          "example": "test"
                        },
                        "to": {
                          "type": "string",
                          "example": "test@test.com"
                        },
                        "url": {
                          "type": "string",
                          "example": "..."
                        },
                        "username": {
                          "type": "string",
                          "example": "api-12345678"
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