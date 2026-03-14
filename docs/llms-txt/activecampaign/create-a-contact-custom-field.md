# Source: https://developers.activecampaign.com/reference/create-a-contact-custom-field.md

# Create a custom field

* When the `field_type` is `dropdown`, `radio`, `checkbox` or `listbox`, you need to add field options using `fieldOption/bulk` endpoint.
* A User can only see a custom field if the contact is part of a list that this custom field is related to. Use [`fieldRel` endpoint](https://developers.activecampaign.com/reference/create-a-custom-field-relationship-to-lists) to specify which list gets to see the custom field.
* > 📘 This endpoint *creates* a custom field, but does not populate it with options, if it requires them.
  >
  > The **dropdown**, **multiselect**, **radio**, and **checkbox** custom fields need to be supplied with options. To learn more, see our [Custom Objets Api Guide](https://developers.activecampaign.com/reference/contact-custom-fields-api-guide)

#### Example `POST` Body

```json textarea
{
	"field": {
		"type": "textarea",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"defval": "Default Value",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json text
{
	"field": {
		"type": "text",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"defval": "Default Value",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json date
{
	"field": {
		"type": "date",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"defval": "2025-01-01",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json dropdown
{
	"field": {
		"type": "dropdown",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json multiselect
{
	"field": {
		"type": "listbox",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json radio
{
	"field": {
		"type": "radio",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json checkbox
{
	"field": {
		"type": "checkbox",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json hidden
{
	"field": {
		"type": "hidden",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"defval": "Default Value",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json datetime (ISO)
{
	"field": {
		"type": "datetime",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"defval": "2025-05-19T02:45:00-05:00",
		"visible": 1,
		"ordernum": 1
    }
}
```

```json number
{
	"field": {
		"type": "number",
		"title": "Field Title",
		"descript": "Field description",
		"perstag": "Personalized Tag",
		"defval": "1234",
		"visible": 1,
		"ordernum": 1
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
    "/fields": {
      "post": {
        "summary": "Create a custom field",
        "description": "",
        "operationId": "create-a-contact-custom-field",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "field": {
                    "properties": {
                      "title": {
                        "type": "string",
                        "description": "Title of the field being created"
                      },
                      "type": {
                        "type": "string",
                        "description": "Possible Values: dropdown, hidden, checkbox, date, text, datetime, textarea, NULL, listbox, radio"
                      },
                      "descript": {
                        "type": "string",
                        "description": "Description of field being created"
                      },
                      "perstag": {
                        "type": "string",
                        "description": "The perstag that represents the field being created"
                      },
                      "defval": {
                        "type": "string",
                        "description": "Default value of the field being created"
                      },
                      "show_in_list": {
                        "type": "boolean",
                        "description": "Show this field in the contact list view (Deprecated - no longer used)"
                      },
                      "rows": {
                        "type": "integer",
                        "description": "Num of rows for a textarea (Deprecated - no longer used)",
                        "format": "int32"
                      },
                      "cols": {
                        "type": "integer",
                        "description": "Num of columns for a textarea (Deprecated - no longer used)",
                        "format": "int32"
                      },
                      "visible": {
                        "type": "boolean",
                        "description": "Show or hide this field when using the Form Builder"
                      },
                      "service": {
                        "type": "string",
                        "description": "Possible Vales: nimble, contactually, mindbody, salesforce, highrise, google_spreadsheets, pipedrive, onepage, google_contacts, freshbooks, shopify, zendesk, etsy, NULL, bigcommerce, capsule, bigcommerce_oauth, sugarcrm, zohocrm, batchbook"
                      },
                      "ordernum": {
                        "type": "integer",
                        "description": "Order of appearance in ‘My Fields’ tab.",
                        "format": "int32"
                      }
                    },
                    "required": [
                      "title",
                      "type"
                    ],
                    "type": "object"
                  }
                }
              },
              "examples": {
                "textarea": {
                  "value": {
                    "field": {
                      "type": "textarea",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "defval": "Default Value",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "text": {
                  "value": {
                    "field": {
                      "type": "text",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "defval": "Default Value",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "date": {
                  "value": {
                    "field": {
                      "type": "date",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "defval": "2025-01-01",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "dropdown": {
                  "value": {
                    "field": {
                      "type": "dropdown",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "multiselect": {
                  "value": {
                    "field": {
                      "type": "listbox",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "radio": {
                  "value": {
                    "field": {
                      "type": "radio",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "checkbox": {
                  "value": {
                    "field": {
                      "type": "checkbox",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "hidden": {
                  "value": {
                    "field": {
                      "type": "hidden",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "defval": "Default Value",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "datetime (ISO)": {
                  "value": {
                    "field": {
                      "type": "datetime",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "defval": "2025-05-19T02:45:00-05:00",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                },
                "number": {
                  "value": {
                    "field": {
                      "type": "number",
                      "title": "Field Title",
                      "descript": "Field description",
                      "perstag": "Personalized Tag",
                      "defval": "1234",
                      "visible": 1,
                      "ordernum": 1
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "201",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"fieldOptions\": [],\n    \"fieldRels\": [],\n    \"fields\": [\n        {\n            \"title\": \"Another Test Title\",\n            \"descript\": null,\n            \"type\": \"\",\n            \"isrequired\": \"0\",\n            \"perstag\": \"ANOTHER_TEST_TITLE\",\n            \"defval\": null,\n            \"show_in_list\": \"0\",\n            \"rows\": \"0\",\n            \"cols\": \"0\",\n            \"visible\": \"1\",\n            \"service\": \"\",\n            \"ordernum\": \"2\",\n            \"cdate\": \"2018-11-15T21:43:38-06:00\",\n            \"udate\": \"2018-11-15T21:43:38-06:00\",\n            \"options\": [],\n            \"relations\": [],\n            \"links\": {\n                \"options\": \"https://:account.api-us1.com/api/:version/fields/2/options\",\n                \"relations\": \"https://:account.api-us1.com/api/:version/fields/2/relations\"\n            },\n            \"id\": \"2\"\n        },\n        {\n            \"title\": \"Title\",\n            \"descript\": \"Field  description\",\n            \"type\": \"textarea\",\n            \"isrequired\": \"1\",\n            \"perstag\": \"PERSONALIZEDTAG\",\n            \"defval\": \"Defaut Value\",\n            \"show_in_list\": \"1\",\n            \"rows\": \"2\",\n            \"cols\": \"2\",\n            \"visible\": \"1\",\n            \"service\": \"google\",\n            \"ordernum\": \"3\",\n            \"cdate\": \"2018-11-15T21:42:40-06:00\",\n            \"udate\": \"2018-11-15T21:49:52-06:00\",\n            \"options\": [],\n            \"relations\": [],\n            \"links\": {\n                \"options\": \"https://:account.api-us1.com/api/:version/fields/1/options\",\n                \"relations\": \"https://:account.api-us1.com/api/:version/fields/1/relations\"\n            },\n            \"id\": \"1\"\n        }\n    ],\n    \"meta\": {\n        \"total\": \"2\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "fieldOptions": {
                      "type": "array"
                    },
                    "fieldRels": {
                      "type": "array"
                    },
                    "fields": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "title": {
                            "type": "string",
                            "example": "Another Test Title"
                          },
                          "descript": {},
                          "type": {
                            "type": "string",
                            "example": ""
                          },
                          "isrequired": {
                            "type": "string",
                            "example": "0"
                          },
                          "perstag": {
                            "type": "string",
                            "example": "ANOTHER_TEST_TITLE"
                          },
                          "defval": {},
                          "show_in_list": {
                            "type": "string",
                            "example": "0"
                          },
                          "rows": {
                            "type": "string",
                            "example": "0"
                          },
                          "cols": {
                            "type": "string",
                            "example": "0"
                          },
                          "visible": {
                            "type": "string",
                            "example": "1"
                          },
                          "service": {
                            "type": "string",
                            "example": ""
                          },
                          "ordernum": {
                            "type": "string",
                            "example": "2"
                          },
                          "cdate": {
                            "type": "string",
                            "example": "2018-11-15T21:43:38-06:00"
                          },
                          "udate": {
                            "type": "string",
                            "example": "2018-11-15T21:43:38-06:00"
                          },
                          "options": {
                            "type": "array"
                          },
                          "relations": {
                            "type": "array"
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "options": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/fields/2/options"
                              },
                              "relations": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/fields/2/relations"
                              }
                            }
                          },
                          "id": {
                            "type": "string",
                            "example": "2"
                          }
                        }
                      }
                    },
                    "meta": {
                      "type": "object",
                      "properties": {
                        "total": {
                          "type": "string",
                          "example": "2"
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
                  "Result": {
                    "value": "{\n    \"message\": \"Forbidden\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Forbidden"
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
                    "value": "{\n    \"errors\": [\n        {\n            \"title\": \"There is already a field with this title\",\n            \"detail\": \"There is already a field named 'Test Title' -- choose another name\",\n            \"code\": \"duplicate\"\n        }\n    ]\n}"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
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
                    },
                    {
                      "type": "object",
                      "properties": {
                        "errors": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "title": {
                                "type": "string",
                                "example": "There is already a field with this personalization tag"
                              },
                              "detail": {
                                "type": "string",
                                "example": "There is already a personalization tag named 'Perstag' -- choose another name"
                              },
                              "code": {
                                "type": "string",
                                "example": "field_invalid"
                              }
                            }
                          }
                        }
                      }
                    },
                    {
                      "type": "object",
                      "properties": {
                        "errors": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "title": {
                                "type": "string",
                                "example": "There is already a field with this title"
                              },
                              "detail": {
                                "type": "string",
                                "example": "There is already a field named 'Test Title' -- choose another name"
                              },
                              "code": {
                                "type": "string",
                                "example": "duplicate"
                              }
                            }
                          }
                        }
                      }
                    }
                  ]
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