# Source: https://developers.smtp2go.com/reference/email-history.md

# Email history

Retrieve a summary of activity from a specified date range (defaults to last 30 days), per sender email address, SMTP username, domain or subaccount.

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
      "name": "STATISTICS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/stats/email_history": {
      "post": {
        "tags": [
          "STATISTICS"
        ],
        "summary": "Email history",
        "description": "Retrieve a summary of activity from a specified date range (defaults to last 30 days), per sender email address, SMTP username, domain or subaccount.",
        "operationId": "email-history",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "group_by": {
                    "type": "string",
                    "description": "One of [<code>email_address</code>, <code>username</code>, <code>domain</code>, <code>subaccount</code>] - controls the grouping of results. Defaults to <code>email_address</code>"
                  },
                  "start_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime which defaults to 30 days prior to the current date at midnight. Timezone is UTC"
                  },
                  "end_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime which defaults the current time. Timezone is UTC"
                  },
                  "subaccounts": {
                    "type": "array",
                    "description": "Pass an optional list of subaccount ids to fetch a summary of only particular subaccounts, ID's can be found by querying <code>/subaccounts/search</code>"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Summary of Account",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "f3898083-f5d5-4512-86bd-e02bd1685840",
                      "data": {
                        "count": 1,
                        "history": [
                          {
                            "used": 1,
                            "bytecount": 1022,
                            "avgsize": 1022,
                            "email_address": "test3@example.com",
                            "lastip": "82.1.149.48",
                            "bounces": 0,
                            "clicks": 0,
                            "opens": 0,
                            "rejects": 0,
                            "spam": 0,
                            "unsubscribes": 0
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
                      "example": "f3898083-f5d5-4512-86bd-e02bd1685840"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "count",
                        "history"
                      ],
                      "properties": {
                        "count": {
                          "type": "integer",
                          "example": 159,
                          "default": 0
                        },
                        "history": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "required": [
                              "lastip",
                              "used",
                              "bytecount",
                              "avgsize"
                            ],
                            "properties": {
                              "subaccount": {
                                "type": "string",
                                "example": "My Subaccount Name",
                                "description": "Only returned if <code>group_by</code> is set to <code>subaccount</code>"
                              },
                              "domain": {
                                "type": "string",
                                "example": "test.com",
                                "description": "Only returned if <code>group_by</code> is set to <code>domain</code>"
                              },
                              "domain_verified": {
                                "type": "boolean",
                                "example": true,
                                "description": "Only returned if <code>group_by</code> is set to <code>domain</code>"
                              },
                              "lastip": {
                                "type": "string",
                                "example": "55.67.22.12"
                              },
                              "used": {
                                "type": "integer",
                                "example": 123,
                                "default": 0
                              },
                              "email_address": {
                                "type": "string",
                                "example": "test3@example.com",
                                "description": "Only returned if <code>group_by</code> is set to <code>email_address</code>"
                              },
                              "username": {
                                "type": "string",
                                "example": "my_user",
                                "description": "Only returned if <code>group_by</code> is set to <code>username</code>"
                              },
                              "description": {
                                "type": "string",
                                "description": "A comment or description of the user, Only returned if <code>group_by</code> is set to <code>username</code>"
                              },
                              "bytecount": {
                                "type": "integer",
                                "example": 148113,
                                "default": 0
                              },
                              "avgsize": {
                                "type": "number",
                                "example": 1204.1707317073171,
                                "default": 0
                              },
                              "bounces": {
                                "type": "integer",
                                "example": 123,
                                "default": 0
                              },
                              "clicks": {
                                "type": "integer",
                                "example": 123,
                                "default": 0
                              },
                              "opens": {
                                "type": "integer",
                                "example": 123,
                                "default": 0
                              },
                              "rejects": {
                                "type": "integer",
                                "example": 123,
                                "default": 0
                              },
                              "spam": {
                                "type": "integer",
                                "example": 123,
                                "default": 0
                              },
                              "unsubscribes": {
                                "type": "integer",
                                "example": 123,
                                "default": 0
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