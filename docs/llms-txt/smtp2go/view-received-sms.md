# Source: https://developers.smtp2go.com/reference/view-received-sms.md

# View received SMS

View received SMS messages.

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
    "/sms/view-received": {
      "post": {
        "tags": [
          "SMS"
        ],
        "summary": "View received SMS",
        "description": "View received SMS messages.",
        "operationId": "view-received-sms",
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
                  "unix_start": {
                    "type": "integer",
                    "description": "Deprecated: this is a legacy method of selecting the start of the search period as a unix timestamp. This can be left empty to use the start_date."
                  },
                  "unix_end": {
                    "type": "integer",
                    "description": "Deprecated: this is a legacy method of selecting the end of the search period as a unix timestamp. This can be left empty to use the end_date."
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
                            "source_address": 15185550120,
                            "destination_address": 15185550141,
                            "timestamp": "2022-09-30T02:02:41.000Z",
                            "content": "Example content",
                            "message_id": "4c1d0952-1c91-48ab-9a72-5221281c0c95",
                            "username": "api-12345678"
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
                            "required": [
                              "source_address",
                              "destination_address",
                              "timestamp",
                              "content",
                              "message_id",
                              "username"
                            ],
                            "properties": {
                              "source_address": {
                                "type": "string",
                                "example": 15185550120
                              },
                              "destination_address": {
                                "type": "string",
                                "example": 15185550141
                              },
                              "timestamp": {
                                "type": "string",
                                "example": "2022-09-30T02:02:41Z"
                              },
                              "content": {
                                "type": "string",
                                "example": "Example content"
                              },
                              "message_id": {
                                "type": "string",
                                "example": "2434321b-566d-40cf-a16b-34570931c205"
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