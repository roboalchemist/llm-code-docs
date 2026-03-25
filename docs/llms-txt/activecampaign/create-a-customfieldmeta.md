# Source: https://developers.activecampaign.com/reference/create-a-customfieldmeta.md

# Create a custom field

> 🚧 You must call /groupMembers after creating the Custom Field
>
> After creating the custom field, you must call the [Add Custom Field to Field Group](https://developers.activecampaign.com/reference/add-custom-field-to-field-group) api to add the custom field to a field group. Failure to do so will result in fields that are not visible on record pages.

To create a custom account field, the following permissions are required.

* Account permission: the user should have permission to manage account.

> 📘 datetime field format
>
> The datetime field default must be in ISO format

```json POST /accountCustomFieldMeta (Example REQUEST)
{	
	"accountCustomFieldMetum": {
		"fieldLabel": "sample text field2",
		"fieldType": "text",
		"fieldDefault": "Default Text",
		"isFormVisible": 1,
		"displayOrder": 1
	}
}
```

```json POST /accountCustomFieldMeta (Example RESPONSE)
{
    "accountCustomFieldMetum": {
        "id": "1",
        "fieldLabel": "title",
        "fieldType": "text",
        "fieldOptions": null,
        "fieldDefault": "Default Text",
        "isFormVisible": 1,
        "displayOrder": 1,
        "createdTimestamp": "2018-10-22 19:57:37",
        "updatedTimestamp": "2018-10-22 19:57:37",
        "links": {
            "accountCustomFieldData": "https://:account.api-us1.com/api/:version/3/accountCustomFieldMeta/1/accountCustomFieldData"
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
    "/accountCustomFieldMeta": {
      "post": {
        "summary": "Create a custom field",
        "description": "",
        "operationId": "create-a-customfieldmeta",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "accountCustomFieldMetum": {
                    "properties": {
                      "fieldLabel": {
                        "type": "string",
                        "description": "Name of the field"
                      },
                      "fieldType": {
                        "type": "string",
                        "description": "Type of field. Possible values are: `text`, `textarea`, `date`, `datetime`, `dropdown`, `multiselect`, `radio`, `checkbox`, `hidden`, `currency`, or `number`."
                      },
                      "fieldOptions": {
                        "type": "array",
                        "description": "Options for the field. Only necessary if `field_type` is `dropdown`, `multiselect`, `radio`, or `checkbox`.",
                        "items": {
                          "type": "string"
                        }
                      },
                      "fieldDefault": {
                        "type": "string",
                        "description": "Default value of the field"
                      },
                      "fieldDefaultCurrency": {
                        "type": "string",
                        "description": "The 3-letter currency code of the default currency for the field. Only necessary if `field_type` is `currency`."
                      },
                      "isFormVisible": {
                        "type": "boolean",
                        "description": "Whether or not the field is visible on forms"
                      },
                      "displayOrder": {
                        "type": "integer",
                        "description": "Order for displaying the field on Manage Fields page and deal profiles",
                        "format": "int32"
                      }
                    },
                    "required": [
                      "fieldLabel",
                      "fieldType"
                    ],
                    "type": "object"
                  }
                }
              },
              "examples": {
                "text": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample text field2",
                      "fieldType": "text",
                      "fieldDefault": "Default Text",
                      "isFormVisible": 1,
                      "displayOrder": 1
                    }
                  }
                },
                "textarea": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample textarea field",
                      "fieldType": "textarea",
                      "fieldDefault": "Default Text in Text Area",
                      "isFormVisible": 1,
                      "displayOrder": 2
                    }
                  }
                },
                "date (ISO ONLY)": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample date field",
                      "fieldType": "date",
                      "fieldDefault": "2018-12-31 00:00:00",
                      "isFormVisible": 1,
                      "displayOrder": 3
                    }
                  }
                },
                "dropdown": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample dropdown field",
                      "fieldType": "dropdown",
                      "fieldDefault": "option 2",
                      "fieldOptions": [
                        "option 1",
                        "option 2",
                        "option 3"
                      ],
                      "isFormVisible": 1,
                      "displayOrder": 4
                    }
                  }
                },
                "multiselect": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample multiselect field",
                      "fieldType": "multiselect",
                      "fieldDefault": [
                        "option 2",
                        "option 3"
                      ],
                      "fieldOptions": [
                        "option 1",
                        "option 2",
                        "option 3"
                      ],
                      "isFormVisible": 1,
                      "displayOrder": 5
                    }
                  }
                },
                "radio": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample radio field",
                      "fieldType": "radio",
                      "fieldDefault": "option 2",
                      "fieldOptions": [
                        "option 1",
                        "option 2",
                        "option 3"
                      ],
                      "isFormVisible": 1,
                      "displayOrder": 6
                    }
                  }
                },
                "checkbox": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample checkbox field",
                      "fieldType": "checkbox",
                      "fieldDefault": [
                        "option 2",
                        "option 3"
                      ],
                      "fieldOptions": [
                        "option 1",
                        "option 2",
                        "option 3"
                      ],
                      "isFormVisible": 1,
                      "displayOrder": 7
                    }
                  }
                },
                "hidden": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample hidden field",
                      "fieldType": "hidden",
                      "fieldDefault": "Default Text in Hidden Field",
                      "isFormVisible": 1,
                      "displayOrder": 8
                    }
                  }
                },
                "number": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample number field",
                      "fieldType": "number",
                      "fieldDefault": "100.99",
                      "isFormVisible": 1,
                      "displayOrder": 9
                    }
                  }
                },
                "currency": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample money field",
                      "fieldType": "currency",
                      "fieldDefault": "10099",
                      "fieldDefaultCurrency": "aud",
                      "isFormVisible": 1,
                      "displayOrder": 10
                    }
                  }
                },
                "datetime": {
                  "value": {
                    "accountCustomFieldMetum": {
                      "fieldLabel": "sample datetime field",
                      "fieldType": "datetime",
                      "fieldDefault": "2020-05-16T03:15:00-05:00",
                      "isFormVisible": 1,
                      "displayOrder": 3
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
                    "value": "{\n    \"accountCustomFieldMetum\": {\n        \"id\": \"1\",\n        \"fieldLabel\": \"title\",\n        \"fieldType\": \"text\",\n        \"fieldOptions\": null,\n        \"fieldDefault\": \"Default Text\",\n        \"isFormVisible\": 1,\n        \"isRequired\": 0,\n        \"displayOrder\": 1,\n        \"createdTimestamp\": \"2018-10-22 19:57:37\",\n        \"updatedTimestamp\": \"2018-10-22 19:57:37\",\n        \"links\": {\n            \"accountCustomFieldData\": \"https://:account.api-us1.com/api/:version/3/accountCustomFieldMeta/1/accountCustomFieldData\"\n        }\n    }\n}"
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
                          "example": "title"
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
                          "example": 0,
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
                          "example": "2018-10-22 19:57:37"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "accountCustomFieldData": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/:version/3/accountCustomFieldMeta/1/accountCustomFieldData"
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
          "422": {
            "description": "422",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n\t\"errors\": [\n  \t\"title\": \"The field type field is required.\",\n    \"detail\": \"\",\n    \"code\": 422\n  ]\n}"
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