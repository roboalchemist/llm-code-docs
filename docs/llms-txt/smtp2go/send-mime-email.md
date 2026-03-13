# Source: https://developers.smtp2go.com/reference/send-mime-email.md

# Send a MIME email

Send an email by supplying a pre-encoded MIME string

We recommend setting the parameter `fastaccept` to "true", as this is a much faster sending method, and will become the default method in the near future.

*Note - when using the `schedule` or `fastaccept` properties the email is queued, a total of 50,000 queued emails can be queued at any one time.*

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
    "/email/mime": {
      "post": {
        "tags": [
          "EMAILS"
        ],
        "summary": "Send a MIME email",
        "description": "Send an email by supplying a pre-encoded MIME string",
        "operationId": "send-mime-email",
        "requestBody": {
          "content": {
            "application/json": {
              "example": {
                "mime_email": "VG86IHRlc3RAZXhhbXBsZS5jb20KU3ViamVjdDogdGVzdApGcm9tOiBvdGhlckBleGFtcGxlLmNvbQoKdGVzdCBlbWFpbA=="
              },
              "schema": {
                "type": "object",
                "required": [
                  "mime_email"
                ],
                "properties": {
                  "mime_email": {
                    "type": "string",
                    "description": "A valid MIME-encoded string that has been Base64 encoded"
                  },
                  "schedule": {
                    "type": "string",
                    "description": "A timestamp that when passed allows you to schedule an email for sending. Must be in the future and within the next 3 days.<br />The api response will include a `schedule_id` property which can then be used alongside webhooks (An `X-Smtp2go-Schedule-Id` header is added to the sent email corresponds to this id)"
                  },
                  "fastaccept": {
                    "type": "boolean",
                    "default": false,
                    "description": "If true, the email will be accepted immediately and sent in a background process. Use webhooks if you need information about final delivery to the recipient. This will soon become the default method of sending via API."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Mime email sent",
            "content": {
              "application/json": {
                "examples": {
                  "Example": {
                    "value": {
                      "request_id": "aa253464-0bd0-467a-b24b-6159dcd7be60",
                      "data": {
                        "failed": 0,
                        "failures": [],
                        "succeeded": 1
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
                        "email_id"
                      ],
                      "properties": {
                        "failed": {
                          "type": "integer",
                          "example": 0,
                          "default": 0,
                          "description": "The number of emails that failed to send.<br><br>Note: An email with multiple recipients is classed as 1 email. Only returned if 'fastaccept' is false."
                        },
                        "failures": {
                          "type": "array",
                          "description": "An array containing any error messages encountered during sending. Only returned if 'fastaccept' is false."
                        },
                        "succeeded": {
                          "type": "integer",
                          "example": 1,
                          "default": 0,
                          "description": "The number of emails that were successfully sent.<br><br>Note: An email with multiple recipients is classed as 1 email. Only returned if 'fastaccept' is false."
                        },
                        "email_id": {
                          "type": "string",
                          "example": "1u0SwL-B9zBpi9ffUq-JAB2",
                          "description": "The email ID generated if successfully sent"
                        },
                        "schedule_id": {
                          "type": "string",
                          "example": "caa928f4-24ec-4a68-bcfc-1fd2596342f0",
                          "description": "The schedule ID generated if queued for sending. Only returned if 'schedule' is passed."
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
                  "Example": {
                    "value": {
                      "request_id": "22e5acba-43bf-11e6-ae42-408d5cce2644",
                      "data": {
                        "error_code": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED",
                        "error": "You do not have permission to access this API endpoint"
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
                        "error_code": {
                          "type": "string",
                          "example": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
                        },
                        "error": {
                          "type": "string",
                          "example": "You do not have permission to access this API endpoint"
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