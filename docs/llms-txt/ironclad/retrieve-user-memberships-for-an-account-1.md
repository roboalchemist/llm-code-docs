# Source: https://clickwrap-developer.ironcladapp.com/reference/retrieve-user-memberships-for-an-account-1.md

# List all User Memberships

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "contact": {
      "email": "support@ironcladapp.com",
      "name": "Ironclad Support"
    },
    "title": "REST API",
    "version": "v1.1"
  },
  "security": [
    {
      "Bearer": []
    }
  ],
  "servers": [
    {
      "description": "Ironclad Clickwrap REST API",
      "url": "https://api.pactsafe.com/v1.1"
    }
  ],
  "components": {
    "securitySchemes": {
      "Bearer": {
        "scheme": "bearer",
        "type": "http"
      }
    }
  },
  "paths": {
    "/accounts/{account_id}/members": {
      "get": {
        "summary": "List all User Memberships",
        "description": "",
        "operationId": "retrieve-user-memberships-for-an-account",
        "tags": [
          "Accounts"
        ],
        "parameters": [
          {
            "name": "account_id",
            "in": "path",
            "description": "The ID of the PactSafe Account.",
            "schema": {
              "type": "integer",
              "format": "integer"
            },
            "required": true
          },
          {
            "in": "query",
            "name": "page",
            "description": "Page number to offset results for pagination. Defaults to 1.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "per_page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "expand",
            "description": "Expands objects that only return an ID. Works up to 2 levels deep.",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "filter",
            "description": "Filter activities by the various fields. Note the use of 'and' between the fields. Example: `event_type==agreed and signer_id==claddy@ironcladapp.com`.\n",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "sort",
            "description": "Sort the results of your call by a field in the Request.",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "no_count",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "fields",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "lean",
            "schema": {
              "type": "boolean"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "allOf": [
                    {
                      "properties": {
                        "count": {
                          "type": "integer"
                        },
                        "has_more": {
                          "type": "boolean"
                        },
                        "page": {
                          "type": "integer"
                        },
                        "per_page": {
                          "type": "integer"
                        },
                        "total_count": {
                          "type": "integer"
                        }
                      },
                      "title": "Collection",
                      "type": "object"
                    },
                    {
                      "properties": {
                        "data": {
                          "type": "array",
                          "items": {
                            "properties": {
                              "email": {
                                "example": "eric@pactsafe.com",
                                "type": "string"
                              },
                              "id": {
                                "default": 0,
                                "example": 1,
                                "type": "integer"
                              },
                              "locale": {
                                "example": "en-US",
                                "type": "string"
                              },
                              "name": {
                                "example": "Eric",
                                "type": "string"
                              },
                              "profiles": {
                                "items": {
                                  "properties": {
                                    "created_time": {
                                      "example": "2015-06-12T21:28:14.680Z",
                                      "type": "string"
                                    },
                                    "displayName": {
                                      "example": "Eric",
                                      "type": "string"
                                    },
                                    "emails": {
                                      "items": {
                                        "example": "foo",
                                        "type": "string"
                                      },
                                      "type": "array"
                                    },
                                    "id": {
                                      "example": "eric@pactsafe.com",
                                      "type": "string"
                                    },
                                    "photos": {
                                      "items": {
                                        "example": "foo",
                                        "type": "string"
                                      },
                                      "type": "array"
                                    },
                                    "provider": {
                                      "example": "local",
                                      "type": "string"
                                    },
                                    "updated_time": {
                                      "example": "2015-06-12T21:28:14.680Z",
                                      "type": "string"
                                    }
                                  },
                                  "type": "object"
                                },
                                "type": "array"
                              },
                              "time_zone": {
                                "example": "EDT",
                                "type": "string"
                              },
                              "verified": {
                                "default": true,
                                "example": true,
                                "type": "boolean"
                              },
                              "verified_time": {
                                "example": "2015-06-12T21:29:46.955Z",
                                "type": "string"
                              }
                            },
                            "type": "object"
                          }
                        }
                      }
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Bad request."
          }
        },
        "deprecated": false
      }
    }
  }
}
```