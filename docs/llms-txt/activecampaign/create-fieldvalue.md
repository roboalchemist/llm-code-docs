# Source: https://developers.activecampaign.com/reference/create-fieldvalue.md

# Create a custom field value

> 🚧 Datetime field values will be converted to your account's timezone when saved
>
> Example: If an account has a timezone setting of Central (America/Chicago):
>
> * Sending a datetime w/ timezone of `2024-11-01T13:05:00-06:00` will be saved in the account's preference of Chicago's (Central) timezone: `2024-11-01T14:05:00-05:00`

#### Example `POST` Body

```json text/textarea/hidden
{
    "fieldValue": {
        "contact": 2,
        "field": 3,
        "value": "Blue"
    },
    "useDefaults": true
}
```

```json dropdown/radio
{
    "fieldValue": {
        "contact": 2,
        "field": 4,
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

```json checkbox multiple
{
    "fieldValue": {
        "contact": 2,
        "field": 6,
        "value": "||Option 1||Option 3||Option 4||"
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
    "/fieldValues": {
      "post": {
        "summary": "Create a custom field value",
        "description": "",
        "operationId": "create-fieldvalue",
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
                        "description": "Value for the field that you're updating. For multi-select options this needs to be in the format of ||option1||option2||"
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
                      "contact": 2,
                      "field": 3,
                      "value": "Blue"
                    },
                    "useDefaults": true
                  }
                },
                "dropdown/radio value": {
                  "value": {
                    "fieldValue": {
                      "contact": 2,
                      "field": 4,
                      "value": "||option 1||option 2||option 3||"
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
                "datetime value ISO format": {
                  "value": {
                    "fieldValue": {
                      "contact": 2,
                      "field": 7,
                      "value": "2020-05-19T02:45:00-05:00"
                    }
                  }
                },
                "multiselect with multiple options": {
                  "value": {
                    "fieldValue": {
                      "contact": 2,
                      "field": 6,
                      "value": "||Option 1||Option 3||Option 4||"
                    }
                  }
                },
                "multiselect with single option": {
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
                    "value": "{\n    \"contacts\": [\n        {\n            \"cdate\": \"2018-08-06T16:26:04-05:00\",\n            \"email\": \"ikreimont+2@activecampaign.com\",\n            \"phone\": \"\",\n            \"firstName\": \"\",\n            \"lastName\": \"\",\n            \"orgid\": \"0\",\n            \"segmentio_id\": \"\",\n            \"bounced_hard\": \"0\",\n            \"bounced_soft\": \"0\",\n            \"bounced_date\": null,\n            \"ip\": \"0\",\n            \"ua\": null,\n            \"hash\": \"14d8c4418ae944c68e9dde4a975854cc\",\n            \"socialdata_lastcheck\": null,\n            \"email_local\": \"\",\n            \"email_domain\": \"\",\n            \"sentcnt\": \"0\",\n            \"rating_tstamp\": null,\n            \"gravatar\": \"0\",\n            \"deleted\": \"0\",\n            \"anonymized\": \"0\",\n            \"adate\": null,\n            \"udate\": \"2018-10-01T17:18:40-05:00\",\n            \"edate\": null,\n            \"deleted_at\": null,\n            \"created_utc_timestamp\": \"2018-09-21 12:04:40\",\n            \"updated_utc_timestamp\": \"2018-10-01 17:18:40\",\n            \"links\": {\n                \"bounceLogs\": \"https://:account.api-us1.com/api/:version/contacts/2/bounceLogs\",\n                \"contactAutomations\": \"https://:account.api-us1.com/api/:version/contacts/2/contactAutomations\",\n                \"contactData\": \"https://:account.api-us1.com/api/:version/contacts/2/contactData\",\n                \"contactGoals\": \"https://:account.api-us1.com/api/:version/contacts/2/contactGoals\",\n                \"contactLists\": \"https://:account.api-us1.com/api/:version/contacts/2/contactLists\",\n                \"contactLogs\": \"https://:account.api-us1.com/api/:version/contacts/2/contactLogs\",\n                \"contactTags\": \"https://:account.api-us1.com/api/:version/contacts/2/contactTags\",\n                \"contactDeals\": \"https://:account.api-us1.com/api/:version/contacts/2/contactDeals\",\n                \"deals\": \"https://:account.api-us1.com/api/:version/contacts/2/deals\",\n                \"fieldValues\": \"https://:account.api-us1.com/api/:version/contacts/2/fieldValues\",\n                \"geoIps\": \"https://:account.api-us1.com/api/:version/contacts/2/geoIps\",\n                \"notes\": \"https://:account.api-us1.com/api/:version/contacts/2/notes\",\n                \"organization\": \"https://:account.api-us1.com/api/:version/contacts/2/organization\",\n                \"plusAppend\": \"https://:account.api-us1.com/api/:version/contacts/2/plusAppend\",\n                \"trackingLogs\": \"https://:account.api-us1.com/api/:version/contacts/2/trackingLogs\",\n                \"scoreValues\": \"https://:account.api-us1.com/api/:version/contacts/2/scoreValues\"\n            },\n            \"id\": \"2\",\n            \"organization\": null\n        }\n    ],\n    \"fieldValue\": {\n        \"contact\": 2,\n        \"field\": 3,\n        \"value\": \"Blue\",\n        \"cdate\": \"2018-10-01T17:18:40-05:00\",\n        \"udate\": \"2018-10-01T17:18:40-05:00\",\n        \"links\": {\n            \"owner\": \"https://:account.api-us1.com/api/:version/fieldValues/15/owner\",\n            \"field\": \"https://:account.api-us1.com/api/:version/fieldValues/15/field\"\n        },\n        \"owner\": 2,\n        \"id\": \"15\"\n    }\n}"
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
                            "example": "2018-08-06T16:26:04-05:00"
                          },
                          "email": {
                            "type": "string",
                            "example": "ikreimont+2@activecampaign.com"
                          },
                          "phone": {
                            "type": "string",
                            "example": ""
                          },
                          "firstName": {
                            "type": "string",
                            "example": ""
                          },
                          "lastName": {
                            "type": "string",
                            "example": ""
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
                          "bounced_date": {},
                          "ip": {
                            "type": "string",
                            "example": "0"
                          },
                          "ua": {},
                          "hash": {
                            "type": "string",
                            "example": "14d8c4418ae944c68e9dde4a975854cc"
                          },
                          "socialdata_lastcheck": {},
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
                          "rating_tstamp": {},
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
                          "adate": {},
                          "udate": {
                            "type": "string",
                            "example": "2018-10-01T17:18:40-05:00"
                          },
                          "edate": {},
                          "deleted_at": {},
                          "created_utc_timestamp": {
                            "type": "string",
                            "example": "2018-09-21 12:04:40"
                          },
                          "updated_utc_timestamp": {
                            "type": "string",
                            "example": "2018-10-01 17:18:40"
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "bounceLogs": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/bounceLogs"
                              },
                              "contactAutomations": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/contactAutomations"
                              },
                              "contactData": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/contactData"
                              },
                              "contactGoals": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/contactGoals"
                              },
                              "contactLists": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/contactLists"
                              },
                              "contactLogs": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/contactLogs"
                              },
                              "contactTags": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/contactTags"
                              },
                              "contactDeals": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/contactDeals"
                              },
                              "deals": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/deals"
                              },
                              "fieldValues": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/fieldValues"
                              },
                              "geoIps": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/geoIps"
                              },
                              "notes": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/notes"
                              },
                              "organization": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/organization"
                              },
                              "plusAppend": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/plusAppend"
                              },
                              "trackingLogs": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/trackingLogs"
                              },
                              "scoreValues": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/contacts/2/scoreValues"
                              }
                            }
                          },
                          "id": {
                            "type": "string",
                            "example": "2"
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
                          "example": 2,
                          "default": 0
                        },
                        "field": {
                          "type": "integer",
                          "example": 3,
                          "default": 0
                        },
                        "value": {
                          "type": "string",
                          "example": "Blue"
                        },
                        "cdate": {
                          "type": "string",
                          "example": "2018-10-01T17:18:40-05:00"
                        },
                        "udate": {
                          "type": "string",
                          "example": "2018-10-01T17:18:40-05:00"
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
                          "example": 2,
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