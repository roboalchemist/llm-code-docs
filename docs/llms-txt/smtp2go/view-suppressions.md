# Source: https://developers.smtp2go.com/reference/view-suppressions.md

# View suppressions

Returns your suppressed email addresses and domains

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
    "/suppression/view": {
      "post": {
        "tags": [
          "SUPPRESSIONS"
        ],
        "summary": "View suppressions",
        "description": "Returns your suppressed email addresses and domains",
        "operationId": "view-suppressions",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "continue_token": {
                    "type": "string",
                    "description": "If returned from a request this can be passed to continue paging through the result of the results"
                  },
                  "email_address": {
                    "type": "string",
                    "description": "If provided, checks if a specific email address or domain is in the block list"
                  },
                  "end_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime which defaults to 30 days prior to the current date at midnight. Timezone is UTC"
                  },
                  "fuzzy": {
                    "type": "boolean",
                    "description": "Indicates if the search should use fuzzy matching on recipients & reasons"
                  },
                  "reason": {
                    "type": "string",
                    "description": "A reason string to search for"
                  },
                  "reasons": {
                    "type": "array",
                    "description": "An array of reason strings to search for",
                    "items": {
                      "type": "string"
                    }
                  },
                  "recipient": {
                    "type": "string",
                    "description": "A recipient string to search for"
                  },
                  "recipients": {
                    "type": "array",
                    "description": "An array of recipient strings to search for",
                    "items": {
                      "type": "string"
                    }
                  },
                  "sort": {
                    "type": "string",
                    "description": "The direction to sort the results, either <code>asc</code> or <code>desc</code>"
                  },
                  "start_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime which defaults to the current date at midnight. Timezone is UTC"
                  },
                  "suppression_type": {
                    "type": "string",
                    "description": "If passed restricts the search to a single suppression type <code>manual</code>, <code>spam</code>, <code>unsubscribe</code>, <code>bounce</code> or <code>compliance</code>"
                  },
                  "suppression_types": {
                    "type": "array",
                    "description": "If passed restricts the search to multiple suppression types <code>manual</code>, <code>spam</code>, <code>unsubscribe</code>, <code>bounce</code> or <code>compliance</code>",
                    "items": {
                      "type": "string"
                    }
                  },
                  "wildcard": {
                    "type": "string",
                    "description": "If provided, only suppressions with this wildcard string in name, domain, or email address fields, will be returned"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "List of suppressions",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "0d782ff6-63f2-11ed-9e11-f23c92160e3c",
                      "data": {
                        "continue_token": null,
                        "results": [
                          {
                            "block_description": "",
                            "complaint": "",
                            "email_address": "temp@example.com",
                            "reason": "manual",
                            "subject": null,
                            "timestamp": "2022-11-14 07:54:45"
                          }
                        ],
                        "total_results": 1
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
                      "example": "e61431d0-a532-11e8-a307-f23c91285f72"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "continue_token",
                        "results",
                        "total_results"
                      ],
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "required": [
                              "complaint",
                              "reason",
                              "block_description",
                              "timestamp",
                              "email_address"
                            ],
                            "properties": {
                              "complaint": {
                                "type": "string",
                                "example": ""
                              },
                              "reason": {
                                "type": "string",
                                "example": "manual"
                              },
                              "block_description": {
                                "type": "string",
                                "example": "no longer a customer"
                              },
                              "timestamp": {
                                "type": "string",
                                "example": "2018-08-21 11:10:55.457489+00:00"
                              },
                              "email_address": {
                                "type": "string",
                                "example": "test@example.com"
                              }
                            }
                          }
                        },
                        "continue_token": {
                          "type": "string",
                          "nullable": true
                        },
                        "total_results": {
                          "type": "integer"
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