# Source: https://developers.smtp2go.com/reference/email-summary.md

# Email summary

Retrieve a combination of the email_bounces, email_cycle, email_spam, and email_unsubs calls in one report. Note this call may take longer to complete.

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
    "/stats/email_summary": {
      "post": {
        "tags": [
          "STATISTICS"
        ],
        "summary": "Email summary",
        "description": "Retrieve a combination of the email_bounces, email_cycle, email_spam, and email_unsubs calls in one report. Note this call may take longer to complete.",
        "operationId": "email-summary",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "username": {
                    "type": "string",
                    "description": "Allows statistics to be returned for a specific user"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Account Statistics",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "72f48187-64d9-4a2f-ba9c-527a2a7911f7",
                      "data": {
                        "spam_emails": 0,
                        "cycle_start": "2022-11-01 00:00:00+00:00",
                        "cycle_end": "2022-11-30 00:00:00+00:00",
                        "cycle_used": 1,
                        "cycle_remaining": 9999,
                        "cycle_max": 10000,
                        "email_count": 1,
                        "bounce_rejects": 0,
                        "softbounces": 0,
                        "hardbounces": 0,
                        "bounce_percent": "0.00",
                        "spam_rejects": 0,
                        "spam_percent": "0.00",
                        "unsubscribes": 0,
                        "unsubscribe_percent": "0.0",
                        "opens": 0,
                        "clicks": 0,
                        "rejects": 0
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
                      "example": "72f48187-64d9-4a2f-ba9c-527a2a7911f7"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "cycle_end",
                        "spam_rejects",
                        "bounce_percent",
                        "unsubscribes",
                        "bounce_rejects",
                        "spam_percent",
                        "softbounces",
                        "cycle_max",
                        "spam_emails",
                        "cycle_remaining",
                        "cycle_start",
                        "unsubscribe_percent",
                        "cycle_used",
                        "hardbounces",
                        "email_count",
                        "opens",
                        "clicks",
                        "rejects"
                      ],
                      "properties": {
                        "cycle_end": {
                          "type": "string",
                          "example": "2016-08-04 01:49:15.863998"
                        },
                        "spam_rejects": {
                          "type": "integer",
                          "example": 1,
                          "default": 0,
                          "deprecated": true
                        },
                        "bounce_percent": {
                          "type": "string",
                          "example": "7.33"
                        },
                        "unsubscribes": {
                          "type": "integer",
                          "example": 32,
                          "default": 0
                        },
                        "bounce_rejects": {
                          "type": "integer",
                          "example": 11,
                          "default": 0,
                          "deprecated": true
                        },
                        "spam_percent": {
                          "type": "string",
                          "example": "1.33"
                        },
                        "softbounces": {
                          "type": "integer",
                          "example": 6,
                          "default": 0
                        },
                        "cycle_max": {
                          "type": "integer",
                          "example": 1000,
                          "default": 0
                        },
                        "spam_emails": {
                          "type": "integer",
                          "example": 2,
                          "default": 0
                        },
                        "cycle_remaining": {
                          "type": "integer",
                          "example": 850,
                          "default": 0
                        },
                        "cycle_start": {
                          "type": "string",
                          "example": "2016-08-01 01:49:15.863998"
                        },
                        "unsubscribe_percent": {
                          "type": "string",
                          "example": "21.33"
                        },
                        "cycle_used": {
                          "type": "integer",
                          "example": 150,
                          "default": 0
                        },
                        "hardbounces": {
                          "type": "integer",
                          "example": 5,
                          "default": 0
                        },
                        "email_count": {
                          "type": "integer",
                          "example": 150,
                          "default": 0
                        },
                        "opens": {
                          "type": "integer",
                          "example": 123,
                          "default": 0
                        },
                        "clicks": {
                          "type": "integer",
                          "example": 321,
                          "default": 0
                        },
                        "rejects": {
                          "type": "integer",
                          "example": 11,
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