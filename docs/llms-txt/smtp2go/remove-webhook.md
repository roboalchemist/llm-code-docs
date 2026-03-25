# Source: https://developers.smtp2go.com/reference/remove-webhook.md

# Remove a specified Webhook

Remove a specific webhook using its unique ID.

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
      "name": "WEBHOOKS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/webhook/remove": {
      "post": {
        "tags": [
          "WEBHOOKS"
        ],
        "summary": "Remove a specified Webhook",
        "description": "Remove a specific webhook using its unique ID.",
        "operationId": "remove-webhook",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "id"
                ],
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "The ID of an existing webhook you want to remove"
                  },
                  "subaccount_id": {
                    "type": "string",
                    "description": "If you wish to make this API call on behalf of a subaccount then include its unique ID here."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Webhook removed",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "f3e50113-deb2-4e54-9675-2ea497c3732e",
                      "data": {
                        "url": "https://example.com/webhook\"",
                        "id": 4317,
                        "events": [
                          "spam"
                        ],
                        "sms_events": [],
                        "headers": [],
                        "usernames": [],
                        "output_format": "json"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "required": [
                    "data",
                    "request_id"
                  ],
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "string",
                          "example": "https://example.com/test-webhook",
                          "description": "The URL of the webhook."
                        },
                        "id": {
                          "type": "integer",
                          "description": "The ID of the webhook."
                        },
                        "events": {
                          "type": "array",
                          "description": "A list of events the webhook will receive, from this list [<code>delivered</code>,<code>unsubscribe</code>,<code>spam</code>,<code>bounce</code>,<code>processed</code>,<code>reject</code>,<code>click</code>,<code>open</code>].",
                          "items": {
                            "type": "string"
                          }
                        },
                        "sms_events": {
                          "type": "array",
                          "description": "A list of SMS events the webhook will receive, from this list [<code>delivered</code>,<code>failed</code>,<code>rejected</code>,<code>sending</code>,<code>submitted</code>].",
                          "items": {
                            "type": "string"
                          }
                        },
                        "headers": {
                          "type": "array",
                          "description": "Custom headers you would specifically like sent in the event data. The headers must already exist in the emails. Subject and Message-id headers are sent by default.",
                          "items": {
                            "type": "string"
                          }
                        },
                        "usernames": {
                          "type": "array",
                          "description": "Usernames to be included in this webhook. All usernames will be included if none are specified.",
                          "items": {
                            "type": "string"
                          }
                        },
                        "output_format": {
                          "type": "string",
                          "description": "The format of the webhook data. Either <code>form</code> or <code>json</code>.",
                          "default": "form"
                        },
                        "auth_header_type": {
                          "type": "string",
                          "description": "The type of authentiction header, Either <code>bearer</code> or <code>basic</code>.",
                          "default": ""
                        },
                        "auth_header_value": {
                          "type": "string",
                          "description": "The value of authentiction header, Either <code>base64(user:pass)</code> or <code>a custom token</code>.",
                          "default": ""
                        }
                      }
                    },
                    "request_id": {
                      "type": "string",
                      "example": "4b661d88-6b2d-11eb-8bb3-f23c92bb31d2"
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