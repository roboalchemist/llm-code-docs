# Source: https://developers.activecampaign.com/reference/sync-a-contacts-data.md

# Sync a contact's data

> 🚧 Organization-Related Nodes Have Been Deprecated
>
> Contact-Organization relationships are now managed through [Account-Contact end points](reference#account-contacts)

> 📘 /sync "upserts" Contact data
>
> The Contact record to be updated is identified by the `email` you provide in the JSON body. If that email address matches an existing Contact's address, that Contact's record will be updated with the JSON body provided.
>
> If the `email` does not match any existing Contact's email address, a new Contact will be created with the provided JSON data.

```json POST /contact/sync (Example REQUEST)
{
	"contact": {
		"email": "jondoe@example.com",
		"firstName": "John",
		"lastName": "Doe",
		"phone": "7223224241",
		"fieldValues": [{
				"field": "1",
				"value": "The Value for First Field"
			},
			{
				"field": "6",
				"value": "2008-01-20"
			}
		]
	}
}
```

```json POST /contact/sync (Example RESPONSE)
{
   "fieldValues": [
     {
       "contact": "113",
       "field": "1",
            "value": "The Value for First Field",
            "cdate": "2020-08-01T10:54:59-05:00",
            "udate": "2020-08-01T14:13:34-05:00",
            "links": {
                "owner": "https://:account.api-us1.com/api/3/fieldValues/11797/owner",
                "field": "https://:account.api-us1.com/api/3/fieldValues/11797/field"
            },
            "id": "11797",
            "owner": "115"
      },
      {
            "contact": "113",
            "field": "6",
            "value": "2008-01-20",
            "cdate": "2020-08-01T10:54:59-05:00",
            "udate": "2020-08-01T14:13:34-05:00",
            "links": {
                "owner": "https://:account.api-us1.com/api/3/fieldValues/11798/owner",
                "field": "https://:account.api-us1.com/api/3/fieldValues/11798/field"
            },
            "id": "11798",
            "owner": "115"
      }
    ],
    "contact": {
        "cdate": "2018-09-28T17:27:21-05:00",
        "email": "jondoe@example.com",
        "phone": "7223224241",
        "firstName": "John",
        "lastName": "Doe",
        "orgid": "0",
        "segmentio_id": "",
        "bounced_hard": "0",
        "bounced_soft": "0",
        "bounced_date": "0000-00-00",
        "ip": "0",
        "ua": "",
        "hash": "",
        "socialdata_lastcheck": "0000-00-00 00:00:00",
        "email_local": "",
        "email_domain": "",
        "sentcnt": "0",
        "rating_tstamp": "0000-00-00",
        "gravatar": "0",
        "deleted": "0",
        "anonymized": "0",
        "udate": "2018-09-28T17:30:52-05:00",
        "deleted_at": "0000-00-00 00:00:00",
        "created_utc_timestamp": "2018-09-28 17:27:21",
        "updated_utc_timestamp": "2018-09-28 17:27:21",
        "links": {
            "bounceLogs": "https://:account.api-us1.com/api/3/contacts/115/bounceLogs",
            "contactAutomations": "https://:account.api-us1.com/api/3/contacts/115/contactAutomations",
            "contactData": "https://:account.api-us1.com/api/3/contacts/115/contactData",
            "contactGoals": "https://:account.api-us1.com/api/3/contacts/115/contactGoals",
            "contactLists": "https://:account.api-us1.com/api/3/contacts/115/contactLists",
            "contactLogs": "https://:account.api-us1.com/api/3/contacts/115/contactLogs",
            "contactTags": "https://:account.api-us1.com/api/3/contacts/115/contactTags",
            "contactDeals": "https://:account.api-us1.com/api/3/contacts/115/contactDeals",
            "deals": "https://:account.api-us1.com/api/3/contacts/115/deals",
            "fieldValues": "https://:account.api-us1.com/api/3/contacts/115/fieldValues",
            "geoIps": "https://:account.api-us1.com/api/3/contacts/115/geoIps",
            "notes": "https://:account.api-us1.com/api/3/contacts/115/notes",
            "organization": "https://:account.api-us1.com/api/3/contacts/115/organization",
            "plusAppend": "https://:account.api-us1.com/api/3/contacts/115/plusAppend",
            "trackingLogs": "https://:account.api-us1.com/api/3/contacts/115/trackingLogs",
            "scoreValues": "https://:account.api-us1.com/api/3/contacts/115/scoreValues"
        },
        "id": "115",
        "organization": null
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
    "/contact/sync": {
      "post": {
        "summary": "Sync a contact's data",
        "description": "",
        "operationId": "sync-a-contacts-data",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "contact": {
                    "properties": {
                      "email": {
                        "type": "string",
                        "description": "Email address of the contact to sync"
                      },
                      "firstName": {
                        "type": "string"
                      },
                      "lastName": {
                        "type": "string"
                      },
                      "phone": {
                        "type": "string"
                      },
                      "fieldValues": {
                        "type": "array",
                        "description": "Contact's custom field values [{field, value}]"
                      },
                      "orgid": {
                        "type": "integer",
                        "description": "(Deprecated) Please use Account-Contact end points",
                        "format": "int32"
                      },
                      "deleted": {
                        "type": "boolean",
                        "description": "(Deprecated) Please use the DELETE endpoint"
                      }
                    },
                    "required": [
                      "email"
                    ],
                    "type": "object"
                  }
                }
              },
              "examples": {
                "Request Example": {
                  "value": {
                    "contact": {
                      "email": "jondoe@example.com",
                      "firstName": "John",
                      "lastName": "Doe",
                      "phone": "7223224241",
                      "fieldValues": [
                        {
                          "field": "1",
                          "value": "The Value for First Field"
                        },
                        {
                          "field": "6",
                          "value": "2008-01-20"
                        }
                      ]
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
                    "value": "{\n    \"fieldValues\": [\n        {\n            \"contact\": \"10\",\n            \"field\": \"2\",\n            \"value\": \"Albany\",\n            \"cdate\": \"2022-04-14T10:03:23-05:00\",\n            \"udate\": \"2022-04-14T10:03:23-05:00\",\n            \"created_by\": null,\n            \"updated_by\": null,\n            \"links\": {\n                \"owner\": \"https://:account.api-us1.com/api/3/fieldValues/14/owner\",\n                \"field\": \"https://:account.api-us1.com/api/3/fieldValues/14/field\"\n            },\n            \"id\": \"14\",\n            \"owner\": \"10\"\n        },\n        {\n            \"contact\": \"10\",\n            \"field\": \"3\",\n            \"value\": \"Georgia\",\n            \"cdate\": \"2022-04-14T10:03:23-05:00\",\n            \"udate\": \"2022-04-14T10:03:23-05:00\",\n            \"created_by\": null,\n            \"updated_by\": null,\n            \"links\": {\n                \"owner\": \"https://:account.api-us1.com/api/3/fieldValues/15/owner\",\n                \"field\": \"https://:account.api-us1.com/api/3/fieldValues/15/field\"\n            },\n            \"id\": \"15\",\n            \"owner\": \"10\"\n        }\n    ],\n    \"contact\": {\n        \"email\": \"johndoe@example.com\",\n        \"phone\": \"7223224241\",\n        \"firstName\": \"John\",\n        \"lastName\": \"Doe\",\n        \"email_empty\": false,\n        \"cdate\": \"2022-04-14T10:03:23-05:00\",\n        \"udate\": \"2022-04-14T10:03:23-05:00\",\n        \"orgid\": \"\",\n        \"orgname\": \"\",\n        \"links\": {\n            \"bounceLogs\": \"https://:account.api-us1.com/api/3/contacts/10/bounceLogs\",\n            \"contactAutomations\": \"https://:account.api-us1.com/api/3/contacts/10/contactAutomations?limit=1000&orders%5Blastdate%5D=DESC\",\n            \"contactData\": \"https://:account.api-us1.com/api/3/contacts/10/contactData\",\n            \"contactGoals\": \"https://:account.api-us1.com/api/3/contacts/10/contactGoals\",\n            \"contactLists\": \"https://:account.api-us1.com/api/3/contacts/10/contactLists\",\n            \"contactLogs\": \"https://:account.api-us1.com/api/3/contacts/10/contactLogs\",\n            \"contactTags\": \"https://:account.api-us1.com/api/3/contacts/10/contactTags\",\n            \"contactDeals\": \"https://:account.api-us1.com/api/3/contacts/10/contactDeals\",\n            \"deals\": \"https://:account.api-us1.com/api/3/contacts/10/deals\",\n            \"fieldValues\": \"https://:account.api-us1.com/api/3/contacts/10/fieldValues\",\n            \"geoIps\": \"https://:account.api-us1.com/api/3/contacts/10/geoIps\",\n            \"notes\": \"https://:account.api-us1.com/api/3/contacts/10/notes\",\n            \"organization\": \"https://:account.api-us1.com/api/3/contacts/10/organization\",\n            \"plusAppend\": \"https://:account.api-us1.com/api/3/contacts/10/plusAppend\",\n            \"trackingLogs\": \"https://:account.api-us1.com/api/3/contacts/10/trackingLogs\",\n            \"scoreValues\": \"https://:account.api-us1.com/api/3/contacts/10/scoreValues\",\n            \"accountContacts\": \"https://:account.api-us1.com/api/3/contacts/10/accountContacts\",\n            \"automationEntryCounts\": \"https://:account.api-us1.com/api/3/contacts/10/automationEntryCounts\"\n        },\n        \"hash\": \"75b8163f768dff1f0f7b5f69476b986a\",\n        \"fieldValues\": [\n            \"14\",\n            \"15\"\n        ],\n        \"id\": \"10\",\n        \"organization\": \"\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "fieldValues": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "contact": {
                            "type": "string",
                            "example": "10"
                          },
                          "field": {
                            "type": "string",
                            "example": "2"
                          },
                          "value": {
                            "type": "string",
                            "example": "Albany"
                          },
                          "cdate": {
                            "type": "string",
                            "example": "2022-04-14T10:03:23-05:00"
                          },
                          "udate": {
                            "type": "string",
                            "example": "2022-04-14T10:03:23-05:00"
                          },
                          "created_by": {},
                          "updated_by": {},
                          "links": {
                            "type": "object",
                            "properties": {
                              "owner": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/3/fieldValues/14/owner"
                              },
                              "field": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/3/fieldValues/14/field"
                              }
                            }
                          },
                          "id": {
                            "type": "string",
                            "example": "14"
                          },
                          "owner": {
                            "type": "string",
                            "example": "10"
                          }
                        }
                      }
                    },
                    "contact": {
                      "type": "object",
                      "properties": {
                        "email": {
                          "type": "string",
                          "example": "johndoe@example.com"
                        },
                        "phone": {
                          "type": "string",
                          "example": "7223224241"
                        },
                        "firstName": {
                          "type": "string",
                          "example": "John"
                        },
                        "lastName": {
                          "type": "string",
                          "example": "Doe"
                        },
                        "email_empty": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        },
                        "cdate": {
                          "type": "string",
                          "example": "2022-04-14T10:03:23-05:00"
                        },
                        "udate": {
                          "type": "string",
                          "example": "2022-04-14T10:03:23-05:00"
                        },
                        "orgid": {
                          "type": "string",
                          "example": ""
                        },
                        "orgname": {
                          "type": "string",
                          "example": ""
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "bounceLogs": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/bounceLogs"
                            },
                            "contactAutomations": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/contactAutomations?limit=1000&orders%5Blastdate%5D=DESC"
                            },
                            "contactData": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/contactData"
                            },
                            "contactGoals": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/contactGoals"
                            },
                            "contactLists": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/contactLists"
                            },
                            "contactLogs": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/contactLogs"
                            },
                            "contactTags": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/contactTags"
                            },
                            "contactDeals": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/contactDeals"
                            },
                            "deals": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/deals"
                            },
                            "fieldValues": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/fieldValues"
                            },
                            "geoIps": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/geoIps"
                            },
                            "notes": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/notes"
                            },
                            "organization": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/organization"
                            },
                            "plusAppend": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/plusAppend"
                            },
                            "trackingLogs": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/trackingLogs"
                            },
                            "scoreValues": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/scoreValues"
                            },
                            "accountContacts": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/accountContacts"
                            },
                            "automationEntryCounts": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/contacts/10/automationEntryCounts"
                            }
                          }
                        },
                        "hash": {
                          "type": "string",
                          "example": "75b8163f768dff1f0f7b5f69476b986a"
                        },
                        "fieldValues": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "14"
                          }
                        },
                        "id": {
                          "type": "string",
                          "example": "10"
                        },
                        "organization": {
                          "type": "string",
                          "example": ""
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