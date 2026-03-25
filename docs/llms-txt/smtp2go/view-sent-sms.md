# Source: https://developers.smtp2go.com/reference/view-sent-sms.md

# View sent SMS

View sent SMS messages.

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
      "name": "SMS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/sms/view-sent": {
      "post": {
        "tags": [
          "SMS"
        ],
        "summary": "View sent SMS",
        "description": "View sent SMS messages.",
        "operationId": "view-sent-sms",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime which defaults to 7 days ago at midnight. The range will be inclusive of start_date and exclusive of end_date. Timezone is UTC.",
                    "format": "date"
                  },
                  "end_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime which defaults to now. Timezone is UTC.",
                    "format": "date"
                  },
                  "username": {
                    "type": "string",
                    "description": "If passed will filter the results based on the username information on the message"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "SMS Messages",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "data": {
                        "request_id": "99b91538-53e4-4e97-8700-4284dcba148d",
                        "messages": [
                          {
                            "id": "11170632-25c9-4fbd-85b3-7491fa506d74",
                            "timestamp": "2025-06-08T19:05:25.830Z",
                            "username": "username",
                            "sender": "shared",
                            "sender_email": "test@example.com",
                            "destination_address": "+123456789",
                            "destination_address_country": "US",
                            "format": "SMS",
                            "status": "Message discarded",
                            "content": "Example content",
                            "units": 1
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
                        "messages"
                      ],
                      "properties": {
                        "request_id": {
                          "type": "string",
                          "example": "e023461c-8c86-11e9-b984-408d5cce2644"
                        },
                        "messages": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "example": "a9d6d238-900c-4b9a-9e42-2d55c48785ab",
                                "description": "A unique ID associated with the message"
                              },
                              "timestamp": {
                                "type": "string",
                                "example": "2025-06-08T19:05:25.830Z",
                                "description": "A timestamp indicating when the message was sent"
                              },
                              "username": {
                                "type": "string",
                                "example": "username",
                                "description": "The username used to send the message"
                              },
                              "sender": {
                                "type": "string",
                                "example": "shared",
                                "descriptions": "The sender used to send the message"
                              },
                              "sender_email": {
                                "type": "string",
                                "example": "test@example.com",
                                "description": "If sent via email this is the sender email"
                              },
                              "destination_address": {
                                "type": "string",
                                "example": "+123456789",
                                "description": "The number the message was sent to"
                              },
                              "destination_address_county": {
                                "type": "string",
                                "example": "US",
                                "description": "The country the destination address resides in"
                              },
                              "format": {
                                "type": "string",
                                "example": "SMS",
                                "description": "The format of the sent message"
                              },
                              "status": {
                                "type": "string",
                                "example": "Message sent",
                                "description": "The status of the sent message"
                              },
                              "content": {
                                "type": "string",
                                "example": "test message",
                                "description": "The content of the sent message"
                              },
                              "units": {
                                "type": "integer",
                                "example": "The number of units used to send the mssage"
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