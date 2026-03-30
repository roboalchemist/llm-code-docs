# Source: https://developers.smtp2go.com/reference/add-allowed-senders.md

# Add allowed senders

Add one or more email addresses and domain names to your Allowed or Restricted Senders List. How this list of email addresses and domain names are used is shown by the current 'mode' value; if the Restrict Senders setting is on, they will form either a whitelist or blacklist. If the setting is off, the list will be disabled. Further details of the associated setting are found in the SMTP2GO Guides. Details of how this mode can be set via the update end-point, are given further in the documentation. A post to this endpoint will return a success, even if the Restrict Senders setting is not in use.

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
      "name": "ALLOWED SENDERS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/allowed_senders/add": {
      "post": {
        "tags": [
          "ALLOWED SENDERS"
        ],
        "summary": "Add allowed senders",
        "description": "Add one or more email addresses and domain names to your Allowed or Restricted Senders List. How this list of email addresses and domain names are used is shown by the current 'mode' value; if the Restrict Senders setting is on, they will form either a whitelist or blacklist. If the setting is off, the list will be disabled. Further details of the associated setting are found in the SMTP2GO Guides. Details of how this mode can be set via the update end-point, are given further in the documentation. A post to this endpoint will return a success, even if the Restrict Senders setting is not in use.",
        "operationId": "add-allowed-senders",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "allowed_senders"
                ],
                "properties": {
                  "allowed_senders": {
                    "type": "array",
                    "description": "Array of email addresses and domain names.",
                    "default": [
                      "test-person@example.com",
                      "other@example.com"
                    ],
                    "items": {
                      "type": "string"
                    }
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
            "description": "Allowed Senders list updated",
            "content": {
              "application/json": {
                "examples": {
                  "Example": {
                    "value": {
                      "request_id": "b8f3c2b4-63ca-11ed-b66a-f23c9216ce11",
                      "data": {
                        "allowed_senders": [
                          "test@test.com"
                        ],
                        "mode": "disabled"
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
                        "allowed_senders",
                        "mode"
                      ],
                      "properties": {
                        "allowed_senders": {
                          "type": "array",
                          "description": "A list of email addresses and domain names",
                          "items": {
                            "type": "string",
                            "example": "test-person@example.com"
                          }
                        },
                        "mode": {
                          "type": "string",
                          "description": "A string indicating how the list of email address and domain names is interpreted.",
                          "example": "whitelist",
                          "enum": [
                            "whitelist",
                            "blacklist",
                            "disabled"
                          ]
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