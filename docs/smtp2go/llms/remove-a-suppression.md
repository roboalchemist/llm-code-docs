# Source: https://developers.smtp2go.com/reference/remove-a-suppression.md

# Remove a suppression

Removes the suppression on the specified email address or domain

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
      "name": "SUPPRESSIONS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/suppression/remove": {
      "post": {
        "tags": [
          "SUPPRESSIONS"
        ],
        "summary": "Remove a suppression",
        "description": "Removes the suppression on the specified email address or domain",
        "operationId": "remove-a-suppression",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "email_address",
                  "reasons"
                ],
                "properties": {
                  "email_address": {
                    "type": "string",
                    "description": "The email address or domain you would like to remove from your suppression list",
                    "default": "test@example.com"
                  },
                  "reasons": {
                    "type": "array",
                    "description": "A list of block types you would like to remove for the given email or domain",
                    "default": [
                      "manual",
                      "spam"
                    ],
                    "items": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Suppression removed",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "be4811ac-63f2-11ed-ab1c-f23c9216bfec",
                      "data": {
                        "suppressions": [
                          {
                            "email_address": "temp@test.com",
                            "reason": "manual",
                            "removed": true
                          },
                          {
                            "email_address": "temp@test.com",
                            "reason": "spam",
                            "removed": false
                          }
                        ]
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
                      "example": "aa253464-0bd0-467a-b24b-6159dcd7be60"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "suppressions"
                      ],
                      "properties": {
                        "suppressions": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "required": [
                              "reason",
                              "email_address",
                              "removed"
                            ],
                            "properties": {
                              "reason": {
                                "type": "string",
                                "example": "manual"
                              },
                              "email_address": {
                                "type": "string",
                                "example": "test@example.com"
                              },
                              "removed": {
                                "type": "boolean",
                                "example": true,
                                "default": true
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