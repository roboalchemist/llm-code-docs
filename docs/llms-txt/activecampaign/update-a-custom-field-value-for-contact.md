# Source: https://developers.activecampaign.com/reference/update-a-custom-field-value-for-contact.md

# Update a custom field value for contact

> 🚧 Datetime field values will be converted to your account's timezone when saved
>
> Example: If an account has a timezone setting of Central (America/Chicago):
>
> * Sending a datetime w/ timezone of `2024-11-01T13:05:00-06:00` will be saved in the account's preference of Chicago's (Central) timezone: `2024-11-01T14:05:00-05:00`

#### Example `PUT` Request

```json text/textarea/hidden
{
    "fieldValue": {
        "contact": 4,
        "field": 24,
        "value": "Blue"
    },
    "useDefaults": true
}
```

```json dropdown/radio
{
    "fieldValue": {
        "contact": 2,
        "field": 5,
        "value": "Option 1"
    }
}
```

```json date
{
    "fieldValue": {
        "contact": 2,
        "field": 7,
        "value": "2018-12-31"
    }
}
```

```json datetime ISO
{
    "fieldValue": {
        "contact": 2,
        "field": 7,
        "value": "2020-05-19T02:45:00-05:00"
    }
}
```

```json checkbox single
{
    "fieldValue": {
        "contact": 2,
        "field": 6,
        "value": "||Option 2||"
    }
}
```

```json checkbox multiple
{
    "fieldValue": {
        "contact": 2,
        "field": 6,
        "value": "||Option 1||Option 3||Option 4||"
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
    "/fieldValues/{id}": {
      "put": {
        "summary": "Update a custom field value for contact",
        "description": "",
        "operationId": "update-a-custom-field-value-for-contact",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of the fieldValue to update",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "fieldValue": {
                    "properties": {
                      "contact": {
                        "type": "string",
                        "description": "ID of the contact whose field value you're updating"
                      },
                      "field": {
                        "type": "string",
                        "description": "ID of the custom field whose value you're updating for the contact"
                      },
                      "value": {
                        "type": "string",
                        "description": "Value for the field that you're updating"
                      }
                    },
                    "required": [
                      "contact",
                      "field",
                      "value"
                    ],
                    "type": "object"
                  },
                  "useDefaults": {
                    "type": "boolean",
                    "description": "If true, this will populate the missing required fields for this contact with default values",
                    "default": false
                  }
                }
              },
              "examples": {
                "text/textarea/hidden value": {
                  "value": {
                    "fieldValue": {
                      "contact": 4,
                      "field": 24,
                      "value": "Blue"
                    },
                    "useDefaults": true
                  }
                },
                "dropdown/radio value": {
                  "value": {
                    "fieldValue": {
                      "contact": 2,
                      "field": 5,
                      "value": "Option 1"
                    }
                  }
                },
                "checkbox/listbox values (multiple)": {
                  "value": {
                    "fieldValue": {
                      "contact": 2,
                      "field": 6,
                      "value": "||Option 1||Option 3||Option 4||"
                    }
                  }
                },
                "date value": {
                  "value": {
                    "fieldValue": {
                      "contact": 2,
                      "field": 7,
                      "value": "2018-12-31"
                    }
                  }
                },
                "datetime value (ISO)": {
                  "value": {
                    "fieldValue": {
                      "contact": 2,
                      "field": 7,
                      "value": "2020-05-19T02:45:00-05:00"
                    }
                  }
                },
                "checkbox/listbox values (single)": {
                  "value": {
                    "fieldValue": {
                      "contact": 2,
                      "field": 6,
                      "value": "||Option 2||"
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
                    "value": "{\n    \"contacts\": [\n        {\n            \"cdate\": \"2018-08-06T16:56:43-05:00\",\n            \"email\": \"johndoe@example.com\",\n            \"phone\": \"\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"orgid\": \"0\",\n            \"segmentio_id\": \"\",\n            \"bounced_hard\": \"0\",\n            \"bounced_soft\": \"0\",\n            \"bounced_date\": \"0000-00-00\",\n            \"ip\": \"4\",\n            \"ua\": \"\",\n            \"hash\": \"867d56644591991f6b50e1cb913f038b\",\n            \"socialdata_lastcheck\": \"0000-00-00 00:00:00\",\n            \"email_local\": \"\",\n            \"email_domain\": \"\",\n            \"sentcnt\": \"0\",\n            \"rating_tstamp\": \"0000-00-00\",\n            \"gravatar\": \"0\",\n            \"deleted\": \"0\",\n            \"anonymized\": \"0\",\n            \"adate\": \"2018-10-24T13:33:06-05:00\",\n            \"udate\": \"2018-10-24T13:33:11-05:00\",\n            \"edate\": \"2018-10-24T13:33:07-05:00\",\n            \"deleted_at\": \"0000-00-00 00:00:00\",\n            \"created_utc_timestamp\": \"2018-09-21 12:04:48\",\n            \"updated_utc_timestamp\": \"2018-10-24 13:33:11\",\n            \"links\": {\n                \"bounceLogs\": \"https://:account.api-us1.com/api/:version/contacts/24/bounceLogs\",\n                \"contactAutomations\": \"https://:account.api-us1.com/api/:version/contacts/24/contactAutomations\",\n                \"contactData\": \"https://:account.api-us1.com/api/:version/contacts/24/contactData\",\n                \"contactGoals\": \"https://:account.api-us1.com/api/:version/contacts/24/contactGoals\",\n                \"contactLists\": \"https://:account.api-us1.com/api/:version/contacts/24/contactLists\",\n                \"contactLogs\": \"https://:account.api-us1.com/api/:version/contacts/24/contactLogs\",\n                \"contactTags\": \"https://:account.api-us1.com/api/:version/contacts/24/contactTags\",\n                \"contactDeals\": \"https://:account.api-us1.com/api/:version/contacts/24/contactDeals\",\n                \"deals\": \"https://:account.api-us1.com/api/:version/contacts/24/deals\",\n                \"fieldValues\": \"https://:account.api-us1.com/api/:version/contacts/24/fieldValues\",\n                \"geoIps\": \"https://:account.api-us1.com/api/:version/contacts/24/geoIps\",\n                \"notes\": \"https://:account.api-us1.com/api/:version/contacts/24/notes\",\n                \"organization\": \"https://:account.api-us1.com/api/:version/contacts/24/organization\",\n                \"plusAppend\": \"https://:account.api-us1.com/api/:version/contacts/24/plusAppend\",\n                \"trackingLogs\": \"https://:account.api-us1.com/api/:version/contacts/24/trackingLogs\",\n                \"scoreValues\": \"https://:account.api-us1.com/api/:version/contacts/24/scoreValues\"\n            },\n            \"id\": \"24\",\n            \"organization\": null\n        }\n    ],\n    \"fieldValue\": {\n        \"contact\": 4,\n        \"field\": 24,\n        \"value\": \"Blue\",\n        \"cdate\": \"2018-10-24T13:32:52-05:00\",\n        \"udate\": \"2018-10-24T13:33:11-05:00\",\n        \"links\": {\n            \"owner\": \"https://:account.api-us1.com/api/:version/fieldValues/15/owner\",\n            \"field\": \"https://:account.api-us1.com/api/:version/fieldValues/15/field\"\n        },\n        \"owner\": 4,\n        \"id\": \"15\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "contacts": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "cdate": {
                            "type": "string",
                            "example": "2018-08-06T16:56:43-05:00"
                          },
                          "email": {
                            "type": "string",
                            "example": "johndoe@example.com"
                          },
                          "phone": {
                            "type": "string",
                            "example": ""
                          },
                          "firstName": {
                            "type": "string",
                            "example": "John"
                          },
                          "lastName": {
                            "type": "string",
                            "example": "Doe"
                          },
                          "orgid": {
                            "type": "string",
                            "example": "0"
                          },
                          "segmentio_id": {
                            "type": "string",
                            "example": ""
                          },
                          "bounced_hard": {
                            "type": "string",
                            "example": "0"
                          },
                          "bounced_soft": {
                            "type": "string",
                            "example": "0"
                          },
                          "bounced_date": {
                            "type": "string",
                            "example": "0000-00-00"
                          },
                          "ip": {
                            "type": "string",
                            "example": "4"
                          },
                          "ua": {
                            "type": "string",
                            "example": ""
                          },
                          "hash": {
                            "type": "string",
                            "example": "867d56644591991f6b50e1cb913f038b"
                          },
                          "socialdata_lastcheck": {
                            "type": "string",
                            "example": "0000-00-00 00:00:00"
                          },
                          "email_local": {
                            "type": "string",
                            "example": ""
                          },
                          "email_domain": {
                            "type": "string",
                            "example": ""
                          },
                          "sentcnt": {
                            "type": "string",
                            "example": "0"
                          },
                          "rating_tstamp": {
                            "type": "string",
                            "example": "0000-00-00"
                          },
                          "gravatar": {
                            "type": "string",
                            "example": "0"
                          },
                          "deleted": {
                            "type": "string",
                            "example": "0"
                          },
                          "anonymized": {
                            "type": "string",
                            "example": "0"
                          },
                          "adate": {
                            "type": "string",
                            "example": "2018-10-24T13:33:06-05:00"
                          },
                          "udate": {
                            "type": "string",
                            "example": "2018-10-24T13:33:11-05:00"
                          },
                          "edate": {
                            "type": "string",
                            "example": "2018-10-24T13:33:07-05:00"
                          },
                          "deleted_at": {
                            "type": "string",
                            "example": "0000-00-00 00:00:00"
                          },
                          "created_utc_timestamp": {
                            "type": "string",
                            "example": "2018-09-21 12:04:48"
                          },
                          "updated_utc_timestamp": {
                            "type": "string",
                            "example": "2018-10-24 13:33:11"
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "bounceLogs": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/bounceLogs"
                              },
                              "contactAutomations": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/contactAutomations"
                              },
                              "contactData": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/contactData"
                              },
                              "contactGoals": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/contactGoals"
                              },
                              "contactLists": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/contactLists"
                              },
                              "contactLogs": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/contactLogs"
                              },
                              "contactTags": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/contactTags"
                              },
                              "contactDeals": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/contactDeals"
                              },
                              "deals": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/deals"
                              },
                              "fieldValues": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/fieldValues"
                              },
                              "geoIps": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/geoIps"
                              },
                              "notes": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/notes"
                              },
                              "organization": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/organization"
                              },
                              "plusAppend": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/plusAppend"
                              },
                              "trackingLogs": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/trackingLogs"
                              },
                              "scoreValues": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/24/scoreValues"
                              }
                            }
                          },
                          "id": {
                            "type": "string",
                            "example": "24"
                          },
                          "organization": {}
                        }
                      }
                    },
                    "fieldValue": {
                      "type": "object",
                      "properties": {
                        "contact": {
                          "type": "integer",
                          "example": 4,
                          "default": 0
                        },
                        "field": {
                          "type": "integer",
                          "example": 24,
                          "default": 0
                        },
                        "value": {
                          "type": "string",
                          "example": "Blue"
                        },
                        "cdate": {
                          "type": "string",
                          "example": "2018-10-24T13:32:52-05:00"
                        },
                        "udate": {
                          "type": "string",
                          "example": "2018-10-24T13:33:11-05:00"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "owner": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/:version/fieldValues/15/owner"
                            },
                            "field": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/:version/fieldValues/15/field"
                            }
                          }
                        },
                        "owner": {
                          "type": "integer",
                          "example": 4,
                          "default": 0
                        },
                        "id": {
                          "type": "string",
                          "example": "15"
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
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