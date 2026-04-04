# Source: https://clickwrap-developer.ironcladapp.com/reference/get_contracts.md

# List all Contracts

List contracts in an Account

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
    "/contracts": {
      "get": {
        "summary": "List all Contracts",
        "tags": [
          "Contracts"
        ],
        "parameters": [
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
            "name": "fields",
            "schema": {
              "type": "string"
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
            "name": "includeArchived",
            "description": "Determine if archived contracts should be included in the result",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
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
                            "title": "Contract",
                            "type": "object",
                            "properties": {
                              "id": {
                                "readOnly": true,
                                "type": "integer",
                                "example": 2
                              },
                              "account": {
                                "readOnly": true,
                                "type": "integer",
                                "example": 2
                              },
                              "site": {
                                "readOnly": true,
                                "type": "integer",
                                "example": 2
                              },
                              "created_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 2
                              },
                              "created_time": {
                                "type": "string",
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted.",
                                "readOnly": true
                              },
                              "updated_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 2
                              },
                              "updated_time": {
                                "type": "string",
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted.",
                                "readOnly": true
                              },
                              "deleted": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "deleted_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 2
                              },
                              "deleted_time": {
                                "type": "string",
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted.",
                                "readOnly": true
                              },
                              "archived": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "archived_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 2
                              },
                              "archived_time": {
                                "type": "string",
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted.",
                                "readOnly": true
                              },
                              "published": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "published_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 2
                              },
                              "published_time": {
                                "type": "string",
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted.",
                                "readOnly": true
                              },
                              "protected": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "private": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "public": {
                                "type": "boolean",
                                "description": "The status of allowing the contract to be published to a legal center or be added to a Group.",
                                "default": false
                              },
                              "shared": {
                                "type": "boolean"
                              },
                              "title": {
                                "type": "string",
                                "description": "The title of the contract.",
                                "example": "Portal Terms of Use"
                              },
                              "key": {
                                "type": "string",
                                "example": "template-0rnbcrv3g"
                              },
                              "description": {
                                "type": "string",
                                "example": "This is a description of the Terms of Use"
                              },
                              "classification": {
                                "type": "string",
                                "example": "privacy_policy"
                              },
                              "clm_record_sync": {
                                "title": "CLMRecordSync",
                                "type": "object",
                                "properties": {
                                  "enabled": {
                                    "type": "boolean"
                                  },
                                  "record_type": {
                                    "type": "string",
                                    "example": "clickwrap"
                                  }
                                }
                              },
                              "countries": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                },
                                "example": [
                                  "RU"
                                ]
                              },
                              "locales": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                },
                                "example": [
                                  "ru-RU"
                                ]
                              },
                              "download_endpoint": {
                                "type": "string",
                                "example": "s/3652e4b9-a327-430c-8ceb-c8f68a2bbd24/contracts/491263.pdf",
                                "readOnly": true
                              },
                              "type": {
                                "allOf": [
                                  {
                                    "title": "ContractType",
                                    "type": "string",
                                    "enum": [
                                      "html",
                                      "pdf"
                                    ]
                                  }
                                ],
                                "readOnly": true
                              },
                              "tags": {
                                "type": "array",
                                "description": "The tags to uniquely identify or easily filter from other contracts.",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "latest_version": {
                                "type": "string",
                                "example": "55dccf164e10cbd8454d7951",
                                "readOnly": true
                              },
                              "published_version": {
                                "type": "string",
                                "example": "55dccf164e10cbd8454d7951",
                                "readOnly": true
                              },
                              "render_data": {
                                "type": "object"
                              },
                              "language_direction": {
                                "title": "ContractLanguageDirection",
                                "type": "string",
                                "enum": [
                                  "auto",
                                  "rtl"
                                ]
                              },
                              "used_in": {
                                "type": "array",
                                "items": {
                                  "title": "ContractUsedIn",
                                  "type": "string",
                                  "enum": [
                                    "embedded_contract",
                                    "standardized_contract",
                                    "personalized_contract",
                                    "legal_center"
                                  ]
                                }
                              }
                            },
                            "required": [
                              "title"
                            ]
                          }
                        }
                      }
                    }
                  ]
                }
              }
            },
            "description": "An array of Contracts"
          },
          "400": {
            "description": "Bad request."
          },
          "401": {
            "description": "The requester is unauthorized."
          }
        }
      }
    }
  }
}
```