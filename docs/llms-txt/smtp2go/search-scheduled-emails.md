# Source: https://developers.smtp2go.com/reference/search-scheduled-emails.md

# Search schedule emails

Allows searching of scheduled emails

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
    "/email/scheduled/search": {
      "post": {
        "tags": [
          "EMAILS"
        ],
        "summary": "Search schedule emails",
        "description": "Allows searching of scheduled emails",
        "operationId": "search-scheduled-emails",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [],
                "example": {
                  "schedule_id": "8fb29ea3-286d-493e-83c5-401f76859bb1",
                  "search": "recipient@example.com",
                  "limit": 100,
                  "page": 2
                },
                "properties": {
                  "schedule_id": {
                    "type": "string",
                    "description": "The schedule_id returned from the `/email/send` endpoint"
                  },
                  "search_subject": {
                    "type": "string",
                    "description": "The subject of the email you want to search for"
                  },
                  "search_recipient": {
                    "type": "string",
                    "description": "The recipient of the email you want to search for"
                  },
                  "search_sender": {
                    "type": "string",
                    "description": "The sender of the email you want to search for"
                  },
                  "limit": {
                    "type": "integer",
                    "description": "If passed will limit the search results",
                    "default": 1000
                  },
                  "page": {
                    "type": "integer",
                    "description": "If passed will return the results of the specific page"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Scheduled email results",
            "content": {
              "application/json": {
                "examples": {
                  "Example": {
                    "value": {
                      "request_id": "c2dca1b4-89b9-4dc7-bd82-a86b83b29d84",
                      "data": [
                        {
                          "schedule_id": "4d3b03a7-8663-4592-899a-b479ba6fcba9",
                          "schedule": "2025-06-30T23:11:56Z",
                          "sender": "test@example.com",
                          "subject": "test 1",
                          "recipients": "test@example2.com",
                          "client_ip": "127.0.0.1"
                        },
                        {
                          "schedule_id": "188262b6-f6cc-4c98-bbe6-84c39d1c0ef4",
                          "schedule": "2025-06-30T23:11:56Z",
                          "sender": "test@example.com",
                          "subject": "test 2",
                          "recipients": "test@example2.com",
                          "client_ip": "127.0.0.1"
                        },
                        {
                          "schedule_id": "789db207-5aba-4895-801b-4ebf1843721e",
                          "schedule": "2025-06-30T23:11:56Z",
                          "sender": "test@example.com",
                          "subject": "test 3",
                          "recipients": "test@example2.com",
                          "client_ip": "127.0.0.1"
                        }
                      ]
                    }
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "description": "An array of emails scheduled to be sent",
                    "properties": {
                      "schedule_id": {
                        "type": "string",
                        "description": "A unique identifier for the scheduled_email"
                      },
                      "schedule": {
                        "type": "string",
                        "description": "A timestamp indicating when the email was scheduled"
                      },
                      "sender": {
                        "type": "string",
                        "description": "The sender of the scheduled email"
                      },
                      "subject": {
                        "type": "string",
                        "description": "The subject of the email"
                      },
                      "recipients": {
                        "type": "string",
                        "description": "The recipients the email is scheduled to send to"
                      },
                      "client_ip": {
                        "type": "string",
                        "description": "The IP address that scheduled the email."
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