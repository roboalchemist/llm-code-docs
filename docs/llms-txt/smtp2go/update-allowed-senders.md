# Source: https://developers.smtp2go.com/reference/update-allowed-senders.md

# Update allowed senders

Replace the email addresses and domain names on your Allowed or Restricted Senders List using this endpoint. How the email addresses and domain names are used is defined in the current 'mode' value - further details of these modes are found in the SMPT2GO Guides. Note that a post to this endpoint will return a success, even if the setting is not in use.

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
    "/allowed_senders/update": {
      "post": {
        "tags": [
          "ALLOWED SENDERS"
        ],
        "summary": "Update allowed senders",
        "description": "Replace the email addresses and domain names on your Allowed or Restricted Senders List using this endpoint. How the email addresses and domain names are used is defined in the current 'mode' value - further details of these modes are found in the SMPT2GO Guides. Note that a post to this endpoint will return a success, even if the setting is not in use.",
        "operationId": "update-allowed-senders",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "allowed_senders",
                  "mode"
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
                  "mode": {
                    "type": "string",
                    "description": "A string indicating how the list of email address and domain names is interpreted. and should be one of 'whitelist', 'blacklist' or 'disabled'.<br><strong>Warning:</strong> Changing the mode to 'whitelist' or 'blacklist' disables the 'Sender Domains' and 'Single Sender Emails' features.<br>",
                    "default": "whitelist",
                    "enum": [
                      "whitelist",
                      "blacklist",
                      "disabled"
                    ]
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
                      "request_id": "40cbb6f2-935f-11e7-b5be-480fcf01a6f2",
                      "data": {
                        "allowed_senders": [
                          "test-person@example.com",
                          "otherexample.com"
                        ],
                        "mode": "whitelist"
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