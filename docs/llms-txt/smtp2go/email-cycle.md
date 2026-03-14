# Source: https://developers.smtp2go.com/reference/email-cycle.md

# Email cycle

Retrieve a summary of your Account activity, including the start and end date of your monthly plan, the number of emails sent this cycle, the number of emails remaining and the number of emails in your monthly allowance.

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
    "/stats/email_cycle": {
      "post": {
        "tags": [
          "STATISTICS"
        ],
        "summary": "Email cycle",
        "description": "Retrieve a summary of your Account activity, including the start and end date of your monthly plan, the number of emails sent this cycle, the number of emails remaining and the number of emails in your monthly allowance.",
        "operationId": "email-cycle",
        "responses": {
          "200": {
            "description": "Summary of Account",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "4b84c952-9bca-432f-a68e-585e4c7a969c",
                      "data": {
                        "cycle_start": "2022-11-01 00:00:00+00:00",
                        "cycle_end": "2022-11-30 00:00:00+00:00",
                        "cycle_used": 1,
                        "cycle_remaining": 9999,
                        "cycle_max": 10000
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
                      "example": "4b84c952-9bca-432f-a68e-585e4c7a969c"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "cycle_end",
                        "cycle_used",
                        "cycle_start",
                        "cycle_max",
                        "cycle_remaining"
                      ],
                      "properties": {
                        "cycle_end": {
                          "type": "string",
                          "example": "2016-08-04 01:49:15.863998"
                        },
                        "cycle_used": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        },
                        "cycle_start": {
                          "type": "string",
                          "example": "2016-08-01 01:49:15.863998"
                        },
                        "cycle_max": {
                          "type": "integer",
                          "example": 1000,
                          "default": 0
                        },
                        "cycle_remaining": {
                          "type": "integer",
                          "example": 1000,
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