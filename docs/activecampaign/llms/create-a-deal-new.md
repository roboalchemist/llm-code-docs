# Source: https://developers.activecampaign.com/reference/create-a-deal-new.md

# Create a deal

Create a new deal

To create a deal, following permissions are required.

* Deal permission: the user should have a permission to manage deals.
* Pipeline-specific permission: the user should have a permission to manage the pipeline a new deal belongs to.

By default, primary contact and deal stage are also returned in the response.

```json POST /deals (Example REQUEST)
{
  "deal": {
    "contact": "51",
    "account": "45",
    "description": "This deal is an important deal",
    "currency": "usd",
    "group": "1",
    "owner": "1",
    "percent": null,
    "stage": "1",
    "status": 0,
    "title": "AC Deal",
    "value": 45600,
    "fields": [
      {
        "customFieldId": 1,
        "fieldValue": "First field value"
      },
      {
        "customFieldId": 2,
        "fieldValue": "2008-01-20"
      },
      {
        "customFieldId": 3,
        "fieldValue": 5500,
        "fieldCurrency": "EUR"
      }
    ]
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
    "/deals": {
      "post": {
        "summary": "Create a deal",
        "description": "Create a new deal",
        "operationId": "create-a-deal-new",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "deal": {
                    "properties": {
                      "title": {
                        "type": "string",
                        "description": "Deal's title."
                      },
                      "description": {
                        "type": "string",
                        "description": "Deal's description"
                      },
                      "account": {
                        "type": "string",
                        "description": "Deal’s account id. Required if `deal.contact` is not provided."
                      },
                      "contact": {
                        "type": "string",
                        "description": "Deal's primary contact's id. Required if `deal.account` is not provided."
                      },
                      "value": {
                        "type": "integer",
                        "description": "Deal's value in cents. (i.e. $456.78 => 45678). Must be greater than or equal to zero.",
                        "format": "int32"
                      },
                      "currency": {
                        "type": "string",
                        "description": "Deal's currency in 3-digit ISO format, lowercased."
                      },
                      "group": {
                        "type": "string",
                        "description": "Deal's pipeline id. Required if `deal.stage` is not provided. If `deal.group` is not provided, the stage's pipeline will be assigned to the deal automatically."
                      },
                      "stage": {
                        "type": "string",
                        "description": "Deal's stage id. Required if `deal.group` is not provided. If `deal.stage` is not provided, the deal will be assigned with the first stage in the pipeline provided in `deal.group`."
                      },
                      "owner": {
                        "type": "string",
                        "description": "Deal's owner id. Required if pipeline's auto-assign option is disabled."
                      },
                      "percent": {
                        "type": "integer",
                        "description": "Deal's percentage.",
                        "format": "int32"
                      },
                      "status": {
                        "type": "integer",
                        "description": "Deal's status. See [available values](https://developers.activecampaign.com/reference/deal).",
                        "default": 0,
                        "format": "int32"
                      },
                      "fields": {
                        "type": "array",
                        "description": "Deal's custom field values `{customFieldId: string, fieldValue: string, fieldCurrency?:string}[]`",
                        "items": {
                          "properties": {
                            "customFieldId": {
                              "type": "integer",
                              "description": "Field ID, ID of the Custom Field Meta Data",
                              "format": "int32"
                            },
                            "fieldValue": {
                              "type": "string",
                              "description": "Updated field value. For `currency` field, this needs to be in cents not dollars (or 100 x Base Unit)."
                            },
                            "fieldCurrency": {
                              "type": "string",
                              "description": "Required only for the `currency` field type. The three letter currency code for the currency value"
                            }
                          },
                          "required": [
                            "customFieldId",
                            "fieldValue"
                          ],
                          "type": "object"
                        }
                      }
                    },
                    "required": [
                      "title",
                      "account",
                      "contact",
                      "value",
                      "currency",
                      "group",
                      "stage",
                      "owner"
                    ],
                    "type": "object"
                  }
                },
                "required": [
                  "deal"
                ]
              },
              "examples": {
                "POST /deals (Example REQUEST)": {
                  "value": {
                    "deal": {
                      "contact": "51",
                      "account": "45",
                      "description": "This deal is an important deal",
                      "currency": "usd",
                      "group": "1",
                      "owner": "1",
                      "percent": null,
                      "stage": "1",
                      "status": 0,
                      "title": "AC Deal",
                      "value": 45600,
                      "fields": [
                        {
                          "customFieldId": 1,
                          "fieldValue": "First field value"
                        },
                        {
                          "customFieldId": 2,
                          "fieldValue": "2008-01-20"
                        },
                        {
                          "customFieldId": 3,
                          "fieldValue": 5500,
                          "fieldCurrency": "EUR"
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
                    "value": {
                      "contacts": [
                        {
                          "adate": "2017-02-06 15:50:11",
                          "bounced_date": "0000-00-00",
                          "bounced_hard": "0",
                          "bounced_soft": "0",
                          "cdate": "2017-02-03T11:26:41-06:00",
                          "deleted": "0",
                          "edate": "0000-00-00 00:00:00",
                          "email": "johndoe@example.com",
                          "email_domain": "",
                          "email_local": "",
                          "firstName": "",
                          "gravatar": "1",
                          "hash": "e1705a92f24edf5313ed21df44d6ff5f",
                          "id": "51",
                          "ip": "0",
                          "lastName": "",
                          "links": {
                            "bounceLogs": "/api/3/contacts/51/bounceLogs",
                            "contactAutomations": "/api/3/contacts/51/contactAutomations",
                            "contactData": "/api/3/contacts/51/contactData",
                            "contactDeals": "/api/3/contacts/51/contactDeals",
                            "contactGoals": "/api/3/contacts/51/contactGoals",
                            "contactLists": "/api/3/contacts/51/contactLists",
                            "contactLogs": "/api/3/contacts/51/contactLogs",
                            "contactTags": "/api/3/contacts/51/contactTags",
                            "deals": "/api/3/contacts/51/deals",
                            "fieldValues": "/api/3/contacts/51/fieldValues",
                            "geoIps": "/api/3/contacts/51/geoIps",
                            "notes": "/api/3/contacts/51/notes",
                            "organization": "/api/3/contacts/51/organization",
                            "plusAppend": "/api/3/contacts/51/plusAppend",
                            "scoreValues": "/api/3/contacts/51/scoreValues",
                            "trackingLogs": "/api/3/contacts/51/trackingLogs"
                          },
                          "organization": null,
                          "orgid": "0",
                          "phone": "",
                          "rating_tstamp": "0000-00-00",
                          "segmentio_id": "",
                          "sentcnt": "0",
                          "socialdata_lastcheck": "0000-00-00 00:00:00",
                          "ua": "",
                          "udate": "2017-02-03T11:26:41-06:00"
                        }
                      ],
                      "deal": {
                        "description": "This deal is an important deal",
                        "currency": "usd",
                        "percent": null,
                        "status": 0,
                        "title": "AC Deal",
                        "value": 45600,
                        "organization": 45,
                        "contact": 1,
                        "group": "1",
                        "owner": "1",
                        "stage": "1",
                        "cdate": "2019-12-09T12:29:33-06:00",
                        "mdate": "2019-12-09T12:29:33-06:00",
                        "nextdate": null,
                        "hash": "c3a5497c",
                        "winProbability": null,
                        "winProbabilityMdate": null,
                        "links": {
                          "dealActivities": "/api/3/deals/51/dealActivities",
                          "contact": "/api/3/deals/51/contact",
                          "contactDeals": "/api/3/deals/51/contactDeals",
                          "group": "/api/3/deals/51/group",
                          "nextTask": "/api/3/deals/51/nextTask",
                          "notes": "/api/3/deals/51/notes",
                          "account": "/api/3/deals/51/account",
                          "customerAccount": "/api/3/deals/51/customerAccount",
                          "organization": "/api/3/deals/51/organization",
                          "owner": "/api/3/deals/51/owner",
                          "scoreValues": "/api/3/deals/51/scoreValues",
                          "stage": "/api/3/deals/51/stage",
                          "tasks": "/api/3/deals/51/tasks",
                          "dealCustomFieldData": "/api/3/deals/51/dealCustomFieldData"
                        },
                        "fields": [
                          {
                            "customFieldId": 1,
                            "fieldValue": "First field value",
                            "dealId": "51"
                          },
                          {
                            "customFieldId": 2,
                            "fieldValue": "2008-01-20",
                            "dealId": "51"
                          },
                          {
                            "customFieldId": 3,
                            "fieldValue": 5500,
                            "fieldCurrency": "EUR",
                            "dealId": "51"
                          }
                        ],
                        "id": "51",
                        "isDisabled": false,
                        "account": 45,
                        "customerAccount": 45
                      },
                      "dealStages": [
                        {
                          "cardRegion1": "title",
                          "cardRegion2": "next-action",
                          "cardRegion3": "show-avatar",
                          "cardRegion4": "contact-fullname-orgname",
                          "cardRegion5": "value",
                          "cdate": "2017-01-20T09:27:32-06:00",
                          "color": "C481DF",
                          "dealOrder": "next-action DESC",
                          "group": "1",
                          "id": "1",
                          "links": {
                            "group": "/api/3/dealStages/1/group"
                          },
                          "order": "1",
                          "title": "To Contact",
                          "udate": "2017-01-20T09:27:32-06:00",
                          "width": "280"
                        }
                      ]
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