# Source: https://developers.activecampaign.com/reference/create-custom-deal-field-meta.md

# Create a custom field meta

> 🚧 You must call /groupMembers after creating the Custom Field
>
> After creating the custom field, you must call the [Add Custom Field to Field Group](https://developers.activecampaign.com/reference/add-custom-field-to-field-group) api to add the custom field to a field group. Failure to do so will result in fields that are not visible on record pages.

To create a custom deal field, the following permissions are required.

* Deal permission: the user should have permission to manage deals.
* Pipeline-specific permission: the user should have permission to manage the pipeline that the deal belongs to. If the user does not have the permission to manage the pipeline, limited deal data are returned with only `id`, `title`, and `isDisabled` set to `1`.

```json text
{	
	"dealCustomFieldMetum": {
		"fieldLabel": "sample text field2",
		"fieldType": "text",
		"fieldDefault": "Default Text",
		"isFormVisible": 1,
		"displayOrder": 1
	}
}
```

```json textarea
{	
	"dealCustomFieldMetum": {
		"fieldLabel": "sample textarea field",
		"fieldType": "textarea",
		"fieldDefault": "Default Text in Text Area",
		"isFormVisible": 1,
		"displayOrder": 2
	}
}
```

```json date
{	
	"dealCustomFieldMetum": {
		"fieldLabel": "sample date field",
		"fieldType": "date",
		"fieldDefault": "2018-12-31 00:00:00",
		"isFormVisible": 1,
		"displayOrder": 3
	}
}
```

```json dropdown
{	
	"dealCustomFieldMetum": {
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
```

```json multiselect
{	
	"dealCustomFieldMetum": {
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
```

```json radio
{	
	"dealCustomFieldMetum": {
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
```

```json checkbox
{	
	"dealCustomFieldMetum": {
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
```

```json hidden
{	
	"dealCustomFieldMetum": {
		"fieldLabel": "sample hidden field",
		"fieldType": "hidden",
		"fieldDefault": "Default Text in Hidden Field",
		"isFormVisible": 1,
		"displayOrder": 8
	}
}
```

```json number
{	
	"dealCustomFieldMetum": {
		"fieldLabel": "sample number field",
		"fieldType": "number",
		"fieldDefault": "100.99",
		"isFormVisible": 1,
		"displayOrder": 9
	}
}
```

```json currency
{	
	"dealCustomFieldMetum": {
		"fieldLabel": "sample money field",
		"fieldType": "currency",
		"fieldDefault": "10099",
		"fieldDefaultCurrency": "aud",
		"isFormVisible": 1,
		"displayOrder": 10
	}
}
```

```json datetime (ISO)
{	
	"dealCustomFieldMetum": {
		"fieldLabel": "sample datetime field",
		"fieldType": "datetime",
		"fieldDefault": "2020-05-16T03:15:00-05:00",
		"isFormVisible": 1,
		"displayOrder": 3
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
    "/dealCustomFieldMeta": {
      "post": {
        "summary": "Create a custom field meta",
        "description": "",
        "operationId": "create-custom-deal-field-meta",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "dealCustomFieldMetum": {
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
                    "dealCustomFieldMetum": {
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
                    "dealCustomFieldMetum": {
                      "fieldLabel": "sample textarea field",
                      "fieldType": "textarea",
                      "fieldDefault": "Default Text in Text Area",
                      "isFormVisible": 1,
                      "isRequired": 1,
                      "displayOrder": 2
                    }
                  }
                },
                "date": {
                  "value": {
                    "dealCustomFieldMetum": {
                      "fieldLabel": "sample date field",
                      "fieldType": "date",
                      "fieldDefault": "2018-12-31 00:00:00",
                      "isFormVisible": 1,
                      "isRequired": 1,
                      "displayOrder": 3
                    }
                  }
                },
                "dropdown": {
                  "value": {
                    "dealCustomFieldMetum": {
                      "fieldLabel": "sample dropdown field",
                      "fieldType": "dropdown",
                      "fieldDefault": "option 2",
                      "fieldOptions": [
                        "option 1",
                        "option 2",
                        "option 3"
                      ],
                      "isFormVisible": 1,
                      "isRequired": 1,
                      "displayOrder": 4
                    }
                  }
                },
                "multiselect": {
                  "value": {
                    "dealCustomFieldMetum": {
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
                      "isRequired": 1,
                      "displayOrder": 5
                    }
                  }
                },
                "radio": {
                  "value": {
                    "dealCustomFieldMetum": {
                      "fieldLabel": "sample radio field",
                      "fieldType": "radio",
                      "fieldDefault": "option 2",
                      "fieldOptions": [
                        "option 1",
                        "option 2",
                        "option 3"
                      ],
                      "isFormVisible": 1,
                      "isRequired": 1,
                      "displayOrder": 6
                    }
                  }
                },
                "checkbox": {
                  "value": {
                    "dealCustomFieldMetum": {
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
                      "isRequired": 1,
                      "displayOrder": 7
                    }
                  }
                },
                "hidden": {
                  "value": {
                    "dealCustomFieldMetum": {
                      "fieldLabel": "sample hidden field",
                      "fieldType": "hidden",
                      "fieldDefault": "Default Text in Hidden Field",
                      "isFormVisible": 1,
                      "isRequired": 1,
                      "displayOrder": 8
                    }
                  }
                },
                "number": {
                  "value": {
                    "dealCustomFieldMetum": {
                      "fieldLabel": "sample number field",
                      "fieldType": "number",
                      "fieldDefault": "100.99",
                      "isFormVisible": 1,
                      "isRequired": 1,
                      "displayOrder": 9
                    }
                  }
                },
                "currency": {
                  "value": {
                    "dealCustomFieldMetum": {
                      "fieldLabel": "sample money field",
                      "fieldType": "currency",
                      "fieldDefault": "10099",
                      "fieldDefaultCurrency": "aud",
                      "isFormVisible": 1,
                      "isRequired": 1,
                      "displayOrder": 10
                    }
                  }
                },
                "datetime (ISO)": {
                  "value": {
                    "dealCustomFieldMetum": {
                      "fieldLabel": "sample datetime field",
                      "fieldType": "datetime",
                      "fieldDefault": "2020-05-16T03:15:00-05:00",
                      "isFormVisible": 1,
                      "isRequired": 1,
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
                    "value": "{\n    \"dealCustomFieldMetum\": {\n        \"id\": \"1\",\n        \"fieldLabel\": \"title\",\n        \"fieldType\": \"text\",\n        \"fieldOptions\": null,\n        \"fieldDefault\": \"Default Text\",\n        \"isFormVisible\": 1,\n        \"isRequired\": 1,\n        \"displayOrder\": 1,\n        \"createdTimestamp\": \"2018-10-22 19:57:37\",\n        \"updatedTimestamp\": \"2018-10-22 19:57:37\",\n        \"links\": {\n            \"dealCustomFieldData\": \"https://:account.api-us1.com/api/:version/3/dealCustomFieldMeta/1/dealCustomFieldData\"\n        }\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "dealCustomFieldMetum": {
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
                          "example": "2018-10-22 19:57:37"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "dealCustomFieldData": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/:version/3/dealCustomFieldMeta/1/dealCustomFieldData"
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