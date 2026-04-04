# Source: https://developers.activecampaign.com/reference/create-new-list.md

# Create a list

> ❗️ Adding new lists may be subject to limits based on your account's tier.
>
> For more information about tiers, see [https://www.activecampaign.com/pricing](https://www.activecampaign.com/pricing)

> 📘 For a list to visible in the "accounts" ui, a user group needs to be assigned to the list.
>
> If your newly-created Lists are not showing in the "accounts" user interface, it may be because a user group has not been to assigned to this List.

```json POST /lists (Example REQUEST)
{
	"list": {
		"name": "Name of List",
		"stringid": "Name-of-list",
		"channel": "email",
		"sender_url": "http://activecampaign.com",
		"sender_reminder": "You are receiving this email as you subscribed to a newsletter when making an order on our site.",
		"send_last_broadcast": 0,
		"carboncopy": "",
		"subscription_notify": "",
		"unsubscription_notify": "",
		"user": 1
	}
}
```

```json POST /lists (Example RESPONSE)
{
    "list": {
        "name": "Name of List",
        "stringid": "Name-of-list",
        "channel": "email",
        "cdate": "2019-02-27T19:06:23-05:00",
        "udate": "2019-02-27T19:06:23-05:00",
        "links": {
            "contactGoalLists": "https://:account.api-us1.com/api/:version/lists/6/contactGoalLists",
            "user": "https://:account.api-us1.com/api/:version/lists/6/user",
            "addressLists": "https://:account.api-us1.com/api/:version/lists/6/addressLists"
        },
        "id": "6"
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
    "/lists": {
      "post": {
        "summary": "Create a list",
        "description": "",
        "operationId": "create-new-list",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "list": {
                    "properties": {
                      "name": {
                        "type": "string",
                        "description": "Name of the list to create"
                      },
                      "stringid": {
                        "type": "string",
                        "description": "URL-safe list name. Example: 'list-name-sample'"
                      },
                      "sender_url": {
                        "type": "string",
                        "description": "The website URL this list is for."
                      },
                      "sender_reminder": {
                        "type": "string",
                        "description": "A reminder for your contacts as to why they are on this list and you are messaging them."
                      },
                      "send_last_broadcast": {
                        "type": "boolean",
                        "description": "Boolean value indicating whether or not to send the last sent campaign to this list to a new subscriber upon subscribing. 1 = yes, 0 = no",
                        "default": false
                      },
                      "carboncopy": {
                        "type": "string",
                        "description": "Comma-separated list of email addresses to send a copy of all mailings to upon send"
                      },
                      "subscription_notify": {
                        "type": "string",
                        "description": "Comma-separated list of email addresses to notify when a new subscriber joins this list."
                      },
                      "unsubscription_notify": {
                        "type": "string",
                        "description": "Comma-separated list of email addresses to notify when a subscriber unsubscribes from this list."
                      },
                      "user": {
                        "type": "integer",
                        "description": "User Id of the list owner.  A list owner is able to control campaign branding.  A property of list.userid also exists on this object; both properties map to the same list owner field and are being maintained in the response object for backward compatibility.  If you post values for both list.user and list.userid, the value of list.user will be used.",
                        "format": "int32"
                      },
                      "channel": {
                        "type": "string",
                        "description": "Type of channel for the list. Possible values are `email` or `sms`.",
                        "default": "email"
                      }
                    },
                    "required": [
                      "name",
                      "stringid",
                      "sender_url",
                      "sender_reminder"
                    ],
                    "type": "object"
                  }
                }
              },
              "examples": {
                "Request Example": {
                  "value": {
                    "list": {
                      "name": "Name of List",
                      "stringid": "Name-of-list",
                      "sender_url": "http://activecampaign.com",
                      "sender_reminder": "You are receiving this email as you subscribed to a newsletter when making an order on our site.",
                      "send_last_broadcast": 0,
                      "carboncopy": "",
                      "subscription_notify": "",
                      "unsubscription_notify": "",
                      "user": 1
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
                    "value": "{\n    \"list\": {\n        \"name\": \"Name of List\",\n        \"stringid\": \"Name-of-list\",\n        \"cdate\": \"2019-02-27T19:06:23-05:00\",\n        \"udate\": \"2019-02-27T19:06:23-05:00\",\n        \"links\": {\n            \"contactGoalLists\": \"https://:account.api-us1.com/api/:version/lists/6/contactGoalLists\",\n            \"user\": \"https://:account.api-us1.com/api/:version/lists/6/user\",\n            \"addressLists\": \"https://:account.api-us1.com/api/:version/lists/6/addressLists\"\n        },\n        \"id\": \"6\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "list": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string",
                          "example": "Name of List"
                        },
                        "stringid": {
                          "type": "string",
                          "example": "Name-of-list"
                        },
                        "cdate": {
                          "type": "string",
                          "example": "2019-02-27T19:06:23-05:00"
                        },
                        "udate": {
                          "type": "string",
                          "example": "2019-02-27T19:06:23-05:00"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "contactGoalLists": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/:version/lists/6/contactGoalLists"
                            },
                            "user": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/:version/lists/6/user"
                            },
                            "addressLists": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/:version/lists/6/addressLists"
                            }
                          }
                        },
                        "id": {
                          "type": "string",
                          "example": "6"
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
          },
          "403": {
            "description": "403",
            "content": {
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"errors\": [\n        {\n            \"status\": 403,\n            \"title\": \"Forbidden\",\n            \"detail\": \"You do not have permission to create lists.\"\n        }\n    ]\n}"
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
                            "example": 403,
                            "default": 0
                          },
                          "title": {
                            "type": "string",
                            "example": "Forbidden"
                          },
                          "detail": {
                            "type": "string",
                            "example": "You do not have permission to create lists."
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