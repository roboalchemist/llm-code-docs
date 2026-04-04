# Source: https://developers.activecampaign.com/reference/list-all-custom-fields-meta.md

# List all custom fields

To create a custom account field, the following permissions are required.

* Account permission: the user should have permission to manage account.

```json GET /accountCustomFieldMeta (Example RESPONSE)
{
    "accountCustomFieldMeta": [
        {
            "id": "1",
            "fieldLabel": "Text Example",
            "fieldType": "text",
            "fieldOptions": null,
            "fieldDefault": 1,
            "fieldDefaultCurrency": null,
            "isFormVisible": 0,
            "displayOrder": 1,
            "personalization": "",
            "knownFieldId": null,
            "hideFieldFlag": 0,
            "createdTimestamp": "2019-04-23 15:34:00",
            "updatedTimestamp": "2019-05-03 15:16:51",
            "links": {
                "accountCustomFieldData": "https://:account.api-us1.com/api/:version/accountCustomFieldMeta/1/accountCustomFieldData"
            }
        },
        {
            "id": "2",
            "fieldLabel": "Multiple Choice Example",
            "fieldType": "multiselect",
            "fieldOptions": [
            	"Option 1",
            	"Option 2",
            	"Option 3"
            ],
            "fieldDefault": 1,
            "fieldDefaultCurrency": null,
            "isFormVisible": 0,
            "displayOrder": 2,
            "personalization": "",
            "knownFieldId": null,
            "hideFieldFlag": 0,
            "createdTimestamp": "2019-04-23 15:34:00",
            "updatedTimestamp": "2019-05-03 15:16:51",
            "links": {
                "accountCustomFieldData": "https://:account.api-us1.com/api/:version/accountCustomFieldMeta/1/accountCustomFieldData"
            }
        }
    ]
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
    "/accountCustomFieldMeta": {
      "get": {
        "summary": "List all custom fields",
        "description": "",
        "operationId": "list-all-custom-fields-meta",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "The number of fields returned per request.",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 100
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"accountCustomFieldMeta\": [\n        {\n            \"id\": \"1\",\n            \"fieldLabel\": \"Text Example\",\n            \"fieldType\": \"text\",\n            \"fieldOptions\": null,\n            \"fieldDefault\": 1,\n            \"fieldDefaultCurrency\": null,\n            \"isFormVisible\": 0,\n            \"isRequired\": 0,\n            \"displayOrder\": 1,\n            \"personalization\": \"\",\n            \"knownFieldId\": null,\n            \"hideFieldFlag\": 0,\n            \"createdTimestamp\": \"2019-04-23 15:34:00\",\n            \"updatedTimestamp\": \"2019-05-03 15:16:51\",\n            \"links\": {\n                \"accountCustomFieldData\": \"https://:account.api-us1.com/api/:version/accountCustomFieldMeta/1/accountCustomFieldData\"\n            }\n        },\n        {\n            \"id\": \"2\",\n            \"fieldLabel\": \"Multiple Choice Example\",\n            \"fieldType\": \"multiselect\",\n            \"fieldOptions\": [\n            \t\"Option 1\",\n            \t\"Option 2\",\n            \t\"Option 3\"\n            ],\n            \"fieldDefault\": 1,\n            \"fieldDefaultCurrency\": null,\n            \"isFormVisible\": 0,\n            \"isRequired\": 0,\n            \"displayOrder\": 2,\n            \"personalization\": \"\",\n            \"knownFieldId\": null,\n            \"hideFieldFlag\": 0,\n            \"createdTimestamp\": \"2019-04-23 15:34:00\",\n            \"updatedTimestamp\": \"2019-05-03 15:16:51\",\n            \"links\": {\n                \"accountCustomFieldData\": \"https://:account.api-us1.com/api/:version/accountCustomFieldMeta/1/accountCustomFieldData\"\n            }\n        }\n    ]\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "accountCustomFieldMeta": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "example": "1"
                          },
                          "fieldLabel": {
                            "type": "string",
                            "example": "Text Example"
                          },
                          "fieldType": {
                            "type": "string",
                            "example": "text"
                          },
                          "fieldOptions": {},
                          "fieldDefault": {
                            "type": "integer",
                            "example": 1,
                            "default": 0
                          },
                          "fieldDefaultCurrency": {},
                          "isFormVisible": {
                            "type": "integer",
                            "example": 0,
                            "default": 0
                          },
                          "isRequired": {
                            "type": "integer",
                            "example": 0,
                            "default": 0
                          },
                          "displayOrder": {
                            "type": "integer",
                            "example": 1,
                            "default": 0
                          },
                          "personalization": {
                            "type": "string",
                            "example": ""
                          },
                          "knownFieldId": {},
                          "hideFieldFlag": {
                            "type": "integer",
                            "example": 0,
                            "default": 0
                          },
                          "createdTimestamp": {
                            "type": "string",
                            "example": "2019-04-23 15:34:00"
                          },
                          "updatedTimestamp": {
                            "type": "string",
                            "example": "2019-05-03 15:16:51"
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