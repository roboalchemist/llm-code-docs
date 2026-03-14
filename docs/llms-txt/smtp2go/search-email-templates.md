# Source: https://developers.smtp2go.com/reference/search-email-templates.md

# View email templates

Search your collection of email templates. Returns any templates that match your search criteria.

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
      "name": "TEMPLATES"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/template/search": {
      "post": {
        "tags": [
          "TEMPLATES"
        ],
        "summary": "View email templates",
        "description": "Search your collection of email templates. Returns any templates that match your search criteria.",
        "operationId": "search-email-templates",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "fuzzy_search": {
                    "type": "boolean",
                    "description": "If provided, will determine whether search terms are matched exactly or using wildcards.  Default: false"
                  },
                  "search_terms": {
                    "type": "array",
                    "description": "If provided, will return email templates containing any of the strings provided in name, tag, id or subject fields.",
                    "items": {
                      "type": "string"
                    }
                  },
                  "tags": {
                    "type": "array",
                    "description": "If provided, will return email templates containing any of the tags provided",
                    "items": {
                      "type": "string"
                    }
                  },
                  "sort_direction": {
                    "type": "string",
                    "description": "If provided, will sort the returned email templates in ascending or descending order.  Default: asc<br><br><strong>Values:</strong> asc or desc"
                  },
                  "page_size": {
                    "type": "integer",
                    "description": "If provided, will limit the number of email templates returned. Default 100",
                    "format": "int32"
                  },
                  "continue_token": {
                    "type": "string",
                    "description": "If provided, will fetch the next page of results, following on from the previous page of results from which this continue token was returned"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Matching templates",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "13ab6f3a-ddea-11eb-b4ce-1002b51e60a4",
                      "data": {
                        "continue_token": null,
                        "templates": [
                          {
                            "name": "Order receipt",
                            "id": "5355878",
                            "subject": "Order receipt for {{ product_name }}",
                            "tags": [
                              "one",
                              "two",
                              "five",
                              "four"
                            ],
                            "last_updated": "2024-01-01 12:00:00"
                          }
                        ],
                        "total_count": 1
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "13ab6f3a-ddea-11eb-b4ce-1002b51e60a4"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "continue_token": {},
                        "templates": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "required": [
                              "id",
                              "subject",
                              "tags"
                            ],
                            "properties": {
                              "id": {
                                "type": "string",
                                "example": "5355878"
                              },
                              "name": {
                                "type": "string",
                                "example": "Order receipt",
                                "description": "This parameter is only returned in 'search' response"
                              },
                              "template_name": {
                                "type": "string",
                                "example": "Order receipt",
                                "description": "This parameter is not present in 'search' response"
                              },
                              "subject": {
                                "type": "string",
                                "example": "Order receipt for {{ product_name }}"
                              },
                              "tags": {
                                "type": "array",
                                "required": [
                                  "types",
                                  "example"
                                ],
                                "items": {
                                  "type": "string",
                                  "example": "one"
                                }
                              },
                              "last_updated": {
                                "type": "string",
                                "example": "2024-01-01 12:00:00",
                                "description": "A timestamp indicating when this template was last updated"
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