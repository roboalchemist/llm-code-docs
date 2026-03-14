# Source: https://developers.smtp2go.com/reference/remove-allowed-recipients.md

# Remove allowed recipients

Remove one or more emails addresses or domain names stored in your Allowed Recipients List. <strong>Note: In the event that any of the email addresses or domains do not feature in the list, no error will be raised.</strong>

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
      "name": "ALLOWED RECIPIENTS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/allowed_recipients/remove": {
      "post": {
        "tags": [
          "ALLOWED RECIPIENTS"
        ],
        "summary": "Remove allowed recipients",
        "description": "Remove one or more emails addresses or domain names stored in your Allowed Recipients List. <strong>Note: In the event that any of the email addresses or domains do not feature in the list, no error will be raised.</strong>",
        "operationId": "remove-allowed-recipients",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "allowed_recipients"
                ],
                "properties": {
                  "allowed_recipients": {
                    "type": "array",
                    "description": "Array of email addresses and domain names to remove.",
                    "default": [
                      "test-person@example.com"
                    ],
                    "items": {
                      "type": "string"
                    }
                  },
                  "enabled": {
                    "type": "boolean",
                    "description": "A flag indicating if this list is taken into account when sending",
                    "example": true
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
            "description": "Allowed Recipients Removed",
            "content": {
              "application/json": {
                "examples": {
                  "Example": {
                    "value": {
                      "request_id": "40cbb6f2-935f-11e7-b5be-480fcf01a6f2",
                      "data": {
                        "allowed_recipients": [
                          "test-person@example.com"
                        ],
                        "enabled": true
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
                      "example": "40cbb6f2-935f-11e7-b5be-480fcf01a6f2"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "allowed_recipients",
                        "enabled"
                      ],
                      "properties": {
                        "allowed_recipients": {
                          "type": "array",
                          "description": "A list of email addresses and domain names",
                          "items": {
                            "type": "string",
                            "example": "test-person@example.com"
                          }
                        },
                        "enabled": {
                          "type": "boolean",
                          "description": "A flag indicating if this list is taken into account when sending",
                          "example": true
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