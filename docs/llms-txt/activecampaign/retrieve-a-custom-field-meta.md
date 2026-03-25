# Source: https://developers.activecampaign.com/reference/retrieve-a-custom-field-meta.md

# Retrieve a custom field

To retrieve a custom deal field, the following permissions are required.

* Deal permission: the user should have permission to manage deals.
* Pipeline-specific permission: the user should have permission to manage the pipeline that the deal belongs to. If the user does not have the permission to manage the pipeline, limited deal data are returned with only `id`, `title`, and `isDisabled` set to `1`.

```json GET /accountCustomFieldMeta/:id (Example RESPONSE)
{
    "accountCustomFieldMetum": {
        "id": "1",
        "fieldLabel": "New Title",
        "fieldType": "text",
        "fieldOptions": null,
        "fieldDefault": "Default Text",
        "isFormVisible": 1,
        "displayOrder": 1,
        "createdTimestamp": "2018-10-22 19:57:37",
        "updatedTimestamp": "2018-10-22 20:04:21",
        "links": {
            "accountCustomFieldData": "https://:account.api-us1.com/api/:version/accountCustomFieldMeta/1/accountCustomFieldData"
        }
    }
}
```

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
    "/accountCustomFieldMeta/{id}": {
      "get": {
        "summary": "Retrieve a custom field",
        "description": "",
        "operationId": "retrieve-a-custom-field-meta",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of the field to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"accountCustomFieldMetum\": {\n        \"id\": \"1\",\n        \"fieldLabel\": \"New Title\",\n        \"fieldType\": \"text\",\n        \"fieldOptions\": null,\n        \"fieldDefault\": \"Default Text\",\n        \"isFormVisible\": 1,\n        \"isRequired\": 1,\n        \"displayOrder\": 1,\n        \"createdTimestamp\": \"2018-10-22 19:57:37\",\n        \"updatedTimestamp\": \"2018-10-22 20:04:21\",\n        \"links\": {\n            \"accountCustomFieldData\": \"https://:account.api-us1.com/api/:version/accountCustomFieldMeta/1/accountCustomFieldData\"\n        }\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "accountCustomFieldMetum": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "1"
                        },
                        "fieldLabel": {
                          "type": "string",
                          "example": "New Title"
                        },
                        "fieldType": {
                          "type": "string",
                          "example": "text"
                        },
                        "fieldOptions": {},
                        "fieldDefault": {
                          "type": "string",
                          "example": "Default Text"
                        },
                        "isFormVisible": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "isRequired": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "displayOrder": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "createdTimestamp": {
                          "type": "string",
                          "example": "2018-10-22 19:57:37"
                        },
                        "updatedTimestamp": {
                          "type": "string",
                          "example": "2018-10-22 20:04:21"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "accountCustomFieldData": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/:version/accountCustomFieldMeta/1/accountCustomFieldData"
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
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"errors\": [\n        {\n            \"status\": 404,\n            \"title\": \"Not Found\"\n        }\n    ]\n}"
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
                          "status": {
                            "type": "integer",
                            "example": 404,
                            "default": 0
                          },
                          "title": {
                            "type": "string",
                            "example": "Not Found"
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