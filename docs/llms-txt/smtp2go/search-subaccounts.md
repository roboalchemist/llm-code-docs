# Source: https://developers.smtp2go.com/reference/search-subaccounts.md

# View subaccounts

Returns any subaccounts that match search criteria

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
    "/subaccounts/search": {
      "post": {
        "tags": [
          "SUBACCOUNTS"
        ],
        "summary": "View subaccounts",
        "description": "Returns any subaccounts that match search criteria",
        "operationId": "search-subaccounts",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "fuzzy_search": {
                    "type": "boolean",
                    "description": "Determines if search terms match complete field values and are case sensitive (false) or partial fields and are case insensitive (true).  Default: true",
                    "default": true
                  },
                  "search_terms": {
                    "type": "array",
                    "description": "Return subaccounts with one or more of the strings in the following array.<br><br><strong>Note:</strong> See 'fuzzy_search' for impact on case sensitivity",
                    "items": {
                      "type": "string"
                    }
                  },
                  "states": {
                    "type": "string",
                    "description": "Controls which states you will be searched <br><br><strong>Valid values:</strong><br> all, active, closed,  suspended",
                    "default": "all"
                  },
                  "sort_direction": {
                    "type": "string",
                    "description": "Sort direction, sorts either asc or desc by subaccount name",
                    "default": "asc"
                  },
                  "page_size": {
                    "type": "integer",
                    "description": "Number of subaccounts to retrieve per call",
                    "default": 100,
                    "format": "int32"
                  },
                  "continue_token": {
                    "type": "string",
                    "description": "A token provided by a prior call to this endpoint, passing this will cause it to fetch the next page of results"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "List of subaccounts",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "169e0780-63fd-11ed-860d-f23c92160e3c",
                      "data": {
                        "continue_token": "",
                        "subaccounts": [
                          {
                            "name": "10000",
                            "email": "matthew.juanita@gmail.com",
                            "id": "GnlKn5",
                            "plan_size": 10000,
                            "plan_used": 0,
                            "plan_remaining": 10000,
                            "state": "Active",
                            "dedicated_ip": false
                          }
                        ],
                        "total_count": 1
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
                        "continue_token",
                        "total_count",
                        "subaccounts"
                      ],
                      "properties": {
                        "continue_token": {},
                        "total_count": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "subaccounts": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "required": [
                              "email",
                              "state",
                              "plan_size",
                              "plan_remaining",
                              "plan_used",
                              "name"
                            ],
                            "properties": {
                              "email": {
                                "type": "string",
                                "example": "matthew.juanita@gmail.com"
                              },
                              "state": {
                                "type": "string",
                                "example": "Active"
                              },
                              "plan_size": {
                                "type": "integer",
                                "example": 10000,
                                "default": 0
                              },
                              "plan_remaining": {
                                "type": "integer",
                                "example": 10000,
                                "default": 0
                              },
                              "plan_used": {
                                "type": "integer",
                                "example": 0,
                                "default": 0
                              },
                              "name": {
                                "type": "string",
                                "example": "Matt & Juanita"
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