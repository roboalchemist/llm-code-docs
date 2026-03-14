# Source: https://developers.smtp2go.com/reference/send-sms.md

# Send SMS

Send an SMS message to one or more numbers, up to a maximum of 100 numbers.

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
    "/sms/send": {
      "post": {
        "tags": [
          "SMS"
        ],
        "summary": "Send SMS",
        "description": "Send an SMS message to one or more numbers, up to a maximum of 100 numbers.",
        "operationId": "send-sms",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "destination",
                  "content"
                ],
                "properties": {
                  "destination": {
                    "type": "array",
                    "description": "An array of SMS numbers to send the message to (Maximum: 100 numbers). Numbers should include the country code of the recipient, and can optionally start with a plus symbol (+).",
                    "items": {
                      "type": "string",
                      "example": "+12025550959"
                    }
                  },
                  "sender": {
                    "type": "string",
                    "description": "The message will be sent from this number (must be in e.164 format). Leave empty to use the default sender number. If the source and destination are located in different countries, a shared number in the recipient's country will be used for sending."
                  },
                  "content": {
                    "type": "string",
                    "description": "The content of the SMS. If more than 160 characters, will be sent as multiple units."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "SMS Sent",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "13ab6f3a-ddea-11eb-b4ce-1002b51e60a4",
                      "data": {
                        "statuses": {
                          "queued": 1
                        },
                        "total_sent": 1
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
                    "data": {
                      "type": "object",
                      "required": [
                        "statuses",
                        "total_sent"
                      ],
                      "properties": {
                        "statuses": {
                          "type": "object",
                          "required": [
                            "queued"
                          ],
                          "properties": {
                            "queued": {
                              "type": "integer",
                              "example": 1,
                              "default": 0
                            }
                          }
                        },
                        "total_sent": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "messages": {
                          "type": "array",
                          "description": "An array of objects containing the object of each message sent",
                          "items": {
                            "type": "object",
                            "required": [
                              "destination",
                              "message_id",
                              "status"
                            ],
                            "properties": {
                              "destination": {
                                "type": "string",
                                "example": "+12025550959"
                              },
                              "message_id": {
                                "type": "string",
                                "example": "d6b0e06d-f031-4485-8e92-8141816b3a22"
                              },
                              "status": {
                                "type": "string",
                                "enum": [
                                  "processing",
                                  "enroute",
                                  "queued",
                                  "submitted",
                                  "processed",
                                  "delivered",
                                  "held",
                                  "expired",
                                  "cancelled",
                                  "failed",
                                  "rejected"
                                ],
                                "example": "queued"
                              }
                            }
                          },
                          "example": [
                            {
                              "destination": "+12025550959",
                              "message_id": "d6b0e06d-f031-4485-8e92-8141816b3a22",
                              "status": "queued"
                            }
                          ]
                        }
                      }
                    },
                    "request_id": {
                      "type": "string",
                      "example": "13ab6f3a-ddea-11eb-b4ce-1002b51e60a4"
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