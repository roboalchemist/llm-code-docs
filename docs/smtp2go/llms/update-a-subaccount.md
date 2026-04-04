# Source: https://developers.smtp2go.com/reference/update-a-subaccount.md

# Update a subaccount

Changes the details on an existing subaccount

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
      "name": "SUBACCOUNTS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/subaccount/edit": {
      "post": {
        "tags": [
          "SUBACCOUNTS"
        ],
        "summary": "Update a subaccount",
        "description": "Changes the details on an existing subaccount",
        "operationId": "update-a-subaccount",
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
                    "type": "string",
                    "description": "The id of an existing subaccount"
                  },
                  "fullname": {
                    "type": "string",
                    "description": "If provided, will set to the new full name for the subaccount"
                  },
                  "limit": {
                    "type": "integer",
                    "description": "If provided, will set to the new limit for the subaccount",
                    "format": "int32"
                  },
                  "dedicated_ip": {
                    "type": "boolean",
                    "description": "If provided, will set to the new dedicated IP address for the subaccount (If limit is greater than 100,000)",
                    "default": false
                  },
                  "archiving": {
                    "type": "boolean",
                    "description": "Choose whether the subaccount is allowed to enable archiving. You still need to turn on archiving for individual senders within the subaccount.",
                    "default": false
                  },
                  "enforce_2fa": {
                    "type": "boolean",
                    "description": "Enforce team members of this subaccount to use 2FA.",
                    "default": false
                  },
                  "enable_sms": {
                    "type": "boolean",
                    "description": "Enable SMS messaging for the subaccount. Additional charges apply.",
                    "default": false
                  },
                  "sms_limit": {
                    "type": "integer",
                    "description": "Your subaccount will be able to send up to this monthly limit of SMS messages. Their sending will also be limited by the master account's overall monthly limit.",
                    "default": 1000
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Subaccount updated",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "dc1b8a6a-63fc-11ed-b6de-f23c9216bfec",
                      "data": {
                        "name": "Test Person",
                        "id": "34l8oj",
                        "plan_size": 10000,
                        "plan_used": 0,
                        "plan_remaining": 10000,
                        "state": "Active",
                        "dedicated_ip": false,
                        "archiving": true,
                        "enforce_2fa": true,
                        "sms_enabled": true,
                        "sms_limit": 1000
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
                      "example": "0ef3f48a-2cfb-11eb-aee9-408d5cce2644"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "name",
                        "id",
                        "plan_size",
                        "plan_used",
                        "plan_remaining",
                        "state",
                        "dedicated_ip",
                        "archiving",
                        "enforce_2fa",
                        "sms_enabled",
                        "sms_limit"
                      ],
                      "properties": {
                        "name": {
                          "type": "string",
                          "example": "Test Person"
                        },
                        "id": {
                          "type": "string",
                          "example": "NDU5OTgw"
                        },
                        "plan_size": {
                          "type": "integer",
                          "example": 10000
                        },
                        "plan_used": {
                          "type": "integer",
                          "example": 0
                        },
                        "plan_remaining": {
                          "type": "integer",
                          "example": 10000
                        },
                        "state": {
                          "type": "string",
                          "example": "Active"
                        },
                        "dedicated_ip": {
                          "type": "boolean",
                          "example": false
                        },
                        "archiving": {
                          "type": "boolean",
                          "example": false
                        },
                        "enforce_2fa": {
                          "type": "boolean",
                          "example": false
                        },
                        "sms_enabled": {
                          "type": "boolean",
                          "example": false
                        },
                        "sms_limit": {
                          "type": "integer",
                          "example": 1000
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