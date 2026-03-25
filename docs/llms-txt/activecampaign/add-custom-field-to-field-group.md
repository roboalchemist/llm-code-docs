# Source: https://developers.activecampaign.com/reference/add-custom-field-to-field-group.md

# Add Custom Field to Field Group

> 🚧 This call should be used after creating any deal custom field or account custom field.
>
> The default group for contact custom fields is `1`, for deal custom fields is `2`, and for account custom fields is `3`.
>
> *Failing to make this call could leave fields not visible on the deal or account record page.*

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
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
    "/groupMembers": {
      "post": {
        "summary": "Add Custom Field to Field Group",
        "description": "",
        "operationId": "add-custom-field-to-field-group",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "groupMember": {
                    "properties": {
                      "rel_id": {
                        "type": "integer",
                        "description": "Custom field ID",
                        "format": "int32"
                      },
                      "ordernum": {
                        "type": "integer",
                        "description": "Order within the field group, use null to append",
                        "format": "int32"
                      },
                      "group_id": {
                        "type": "integer",
                        "default": null,
                        "format": "int32"
                      }
                    },
                    "required": [],
                    "type": "object"
                  }
                }
              },
              "examples": {
                "POST": {
                  "value": {
                    "groupMember": {
                      "rel_id": "10",
                      "ordernum": null,
                      "group_id": "1"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"groupMember\": {\n        \"id\": 87,\n        \"group_id\": 1,\n        \"rel_id\": 10,\n        \"ordernum\": 18,\n        \"created_by\": 1,\n        \"updated_by\": 1,\n        \"links\": {\n            \"groupDefinition\": \"https://yourAccounut.api-us1.com/api/3/groupDefinitions/1\"\n        }\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "groupMember": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "example": 87,
                          "default": 0
                        },
                        "group_id": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "rel_id": {
                          "type": "integer",
                          "example": 10,
                          "default": 0
                        },
                        "ordernum": {
                          "type": "integer",
                          "example": 18,
                          "default": 0
                        },
                        "created_by": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "updated_by": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "groupDefinition": {
                              "type": "string",
                              "example": "https://yourAccounut.api-us1.com/api/3/groupDefinitions/1"
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
          "403": {
            "description": "403",
            "content": {
              "application/json": {
                "examples": {
                  "rel_id left blank": {
                    "value": "{\n    \"message\": \"Client error: `POST https://escape-velocity-grouper.cluster-private.app-us1.com/member` resulted in a `400 Bad Request` response:\\n{\\\"message\\\": {\\\"rel_id\\\": \\\"rel_id is required\\\"}}\\n\\n\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Client error: `POST https://escape-velocity-grouper.cluster-private.app-us1.com/member` resulted in a `400 Bad Request` response:\n{\"message\": {\"rel_id\": \"rel_id is required\"}}\n\n"
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"message\": \"No Result found for GroupDefinition with id 94\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "No Result found for GroupDefinition with id 94"
                    }
                  }
                }
              }
            }
          },
          "422": {
            "description": "422",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"errors\": [\n        {\n            \"title\": \"The field title was not provided.\",\n            \"detail\": \"\",\n            \"code\": \"field_missing\"\n        }\n    ]\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "errors": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "title": {
                            "type": "string",
                            "example": "The field title was not provided."
                          },
                          "detail": {
                            "type": "string",
                            "example": ""
                          },
                          "code": {
                            "type": "string",
                            "example": "field_missing"
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
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```