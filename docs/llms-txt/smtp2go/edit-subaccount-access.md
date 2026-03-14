# Source: https://developers.smtp2go.com/reference/edit-subaccount-access.md

# Edit subaccount access

Allow subaccounts to send from verified sender domains on the master account.

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
    "/domain/subaccount_access": {
      "post": {
        "tags": [
          "SENDER DOMAINS"
        ],
        "summary": "Edit subaccount access",
        "description": "Allow subaccounts to send from verified sender domains on the master account.",
        "operationId": "edit-subaccount-access",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "domain",
                  "subaccounts"
                ],
                "properties": {
                  "domain": {
                    "type": "string",
                    "description": "The sender domain to edit subaccount access for"
                  },
                  "subaccounts": {
                    "type": "array",
                    "description": "A list of subaccount_ids to be given access. ID's can be found by querying <code>/subaccounts/search</code>"
                  },
                  "future_subaccounts": {
                    "type": "boolean",
                    "description": "If set to true, will automatically add any new subaccounts to the access list",
                    "default": false
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Subaccount access updated",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "domain": {
                      "type": "string",
                      "description": "The sender domain that was modified."
                    },
                    "subaccounts": {
                      "type": "array",
                      "description": "A list of subaccount IDs that were given access the sender domain."
                    },
                    "future_subaccounts": {
                      "type": "boolean",
                      "description": "If true, any new subaccounts added will automatically be given access."
                    }
                  }
                },
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "6d4706c4-54c9-483d-b141-4f16a9c26879",
                      "data": {
                        "domain": "my-verified-domain.com",
                        "subaccounts": [],
                        "future_subaccounts": false
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