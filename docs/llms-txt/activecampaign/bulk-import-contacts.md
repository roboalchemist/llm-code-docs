# Source: https://developers.activecampaign.com/reference/bulk-import-contacts.md

# Bulk import contacts

## Using the Bulk Contact Importer API

With ActiveCampaign, you can use the Bulk Contact Importer API to upload large numbers of contacts into your account with just one API call.

## Take Note:

* The Bulk Contact Importer API is available on all ActiveCampaign plans
* This feature is for advanced users who are familiar with the API and are comfortable using it to import contacts

> 📘 Use exclude\_automations to skip running automations on imports
>
> Using this parameter will improve the import time.
>
> If `exclude_automations: true` is included in the payload, automations will NOT run when bulk importing contacts.
>
> **By default, automations will run when doing a bulk import.**

## About the Bulk Contact Importer API

The bulk contact importer is designed to perform operations on large quantities of contacts at one time. These operations include:

* Creating new contacts
* Updating existing contacts
* Setting fields on contacts
* Tagging contacts
* Adding contacts to lists

> 🚧 Note for less than 10 contacts:
>
> The Bulk Contact Importer is not designed to support frequent operations involving a small number of contacts or to sync updates in real-time from an external database. Instead, contact updates should be collected into larger batches and imported as a group. Contacts can be imported in batches of up to 250 items.
>
> If you need to upload 10 or fewer contacts at a time, please use the Contacts functionality of our ActiveCampaign API V3.

## Rate limiting

The bulk importer process is optimized for the upload of larger lists of contacts. Running frequent requests that involve a small number of contacts requires significant overhead, and can affect the importer’s performance. As a result, we enforce the following rate limits on the Bulk Contact Importer API:

* For requests containing a single contact, there is a limit of 20 requests per minute
* For requests containing multiple contacts, there is a limit of 100 requests per minute

We recommend that all users attempt to batch updates into groups as large as possible before starting an import.

## Payload size limiting

The maximum payload size of a single bulk\_import request must be less than less than 400K bytes (399,999 bytes or less).

## "Excluded" Emails will be Skipped

Any emails emails contained in a bulk import will be compared against your "Email Exclusions" list.\
If an email is important that is in your exclusion list, the Bulk Import API response will be `200` "Success" but will contain:

```
{"success":5,"queued_contacts":2,"batchId":"59f14dbe-a54f-4d84-a3f6-a13849Aa3eb","message":"Contact import queued"}\`
```

A call to import status will show the skipped emails:

```
{"status":"completed","success":["5232"],"failure":["excluded_email1@example.com", "excluded_email2@example.com"]}
```

> 🚧 Why Bulk Imports Fail
>
> ### Examples of invalid formatting that will fail an import:
>
> * Username before `@` must have a length of at least 1 character.
> * Address does not contain special characters such as  " ( ) , : ; \< > @ \[ \ ]
> * An `@` symbol is required between the email username and domain url.
> * A `.` is required in the address's domain url, and there must be at least **two** letters after the `.` containing no special characters.
>
> ### Other reasons for failure:
>
> * The imported contacts may not exceed your account limit
> * The contact must have an email address
> * The contact’s email address must not be on an exclusion list
> * The contact’s email must not be on a list of bounced email addresses
> * The contact must not have unsubscribed to a list that the import would add them to

```json POST /import/bulk_import (Example REQUEST)
{
  "contacts": [
    {
      "email": "someone@somewhere.com",
      "first_name": "Jane",
      "last_name": "Doe",
      "phone": "123-456-7890",
      "customer_acct_name": "ActiveCampaign",
      "tags": [
        "dictumst", "aliquam", "augue quam", "sollicitudin rutrum"
      ],
      "fields": [
        { "id": 1, "value": "foo" },
        { "id": 2, "value": "||foo||bar||baz||" }
      ],
      "subscribe": [
        { "listid": 1 },
        { "listid": 2 }
      ],
      "unsubscribe": [
        { "listid": 3 }
      ]
    }
  ],
  "callback": {
    "url": "www.your_web_server.com",
    "requestType": "POST",
    "detailed_results": "true",
    "params": [
      { "key": "", "value": "" }
    ],
    "headers": [
      { "key": "", "value": "" }
    ]
  }
}
```

```json POST /import/bulk_import (Example RESPONSE)
{
   "Success":1,
   "queued_contacts":1,
   "batchId":"0641fbdd-f62f-4c2c-ba02-3a83d5d11ac9",
   "message":"Contact import queued"
}
```

> ❗️ 400 Errors can take two forms
>
> If the error occurs during contact creation,  the error will return `failureReasons` as a list of objects, and a nested `contact` indicating which Contact the failure occurred with.
>
> If the failure is more general (for example, rate limit exceeded), the error will return `failureReasons` as a list of strings.

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
    "/import/bulk_import": {
      "post": {
        "summary": "Bulk import contacts",
        "description": "",
        "operationId": "bulk-import-contacts",
        "parameters": [
          {
            "name": "Content-Type",
            "in": "header",
            "schema": {
              "type": "string",
              "default": "application/json"
            }
          },
          {
            "name": "Api-Token",
            "in": "header",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "contacts"
                ],
                "properties": {
                  "contacts": {
                    "type": "array",
                    "description": "An array of objects containing information about a single contact. Up to 250 contacts may be included in a single request. The suggested minimum number of contacts is 10. If less than that, then contact/sync api request should be used.",
                    "items": {
                      "properties": {
                        "email": {
                          "type": "string",
                          "description": "The contact's email."
                        },
                        "first_name": {
                          "type": "string",
                          "description": "The contact's first name"
                        },
                        "last_name": {
                          "type": "string",
                          "description": "The contact's last name."
                        },
                        "phone": {
                          "type": "string",
                          "description": "The contact’s phone number."
                        },
                        "customer_acct_name": {
                          "type": "string",
                          "description": "The name of the contact’s account."
                        },
                        "tags": {
                          "type": "array",
                          "description": "Each string in the array will be added as a single tag to the contact. New tags will be created if they do not already exist.",
                          "default": [],
                          "items": {
                            "type": "string"
                          }
                        },
                        "fields": {
                          "type": "array",
                          "description": "A list of custom fields to apply to the contact. Each field must contain two fields: Each contact may have up to N custom fields.",
                          "items": {
                            "properties": {
                              "id": {
                                "type": "integer",
                                "description": "The ID of the custom field. Custom fields must be referenced by the ID that ActiveCampaign assigns to them. You can retrieve the ID number for a custom field by using the \"List all custom fields\" API call.",
                                "format": "int32"
                              },
                              "value": {
                                "type": "string",
                                "description": "The value of the custom field. Multiple values may be populated for multi-value fields by separating the different values by the double-pipe delimiter (“||”)."
                              }
                            },
                            "required": [
                              "id",
                              "value"
                            ],
                            "type": "object"
                          }
                        },
                        "subscribe": {
                          "type": "array",
                          "description": "An array of lists to subscribe the contact to. Contacts may not be subscribed to lists which they have previously unsubscribed from. Each list object contains a single field.",
                          "items": {
                            "properties": {
                              "listid": {
                                "type": "string",
                                "description": "The ID of the list to subscribe the contact to or unsubscribe the contact from. Lists must be referenced by the ID that ActiveCampaign assigns to them.  You can find the list ID by clicking the list in your ActiveCampaign account then viewing the URL bar. It will look something like this: /app/contacts/?listid=19&status=1  You can also retrieve the ID number for a list by using the \"Retrieve all lists\" API call."
                              }
                            },
                            "type": "object"
                          }
                        },
                        "unsubscribe": {
                          "type": "array",
                          "description": "An array of lists to unsubscribe the contact to. Each list object contains a single field.",
                          "items": {
                            "properties": {
                              "listid": {
                                "type": "string",
                                "description": "The ID of the list to subscribe the contact to or unsubscribe the contact from. Lists must be referenced by the ID that ActiveCampaign assigns to them.  You can find the list ID by clicking the list in your ActiveCampaign account then viewing the URL bar. It will look something like this: /app/contacts/?listid=19&status=1  You can also retrieve the ID number for a list by using the \"Retrieve all lists\" API call."
                              }
                            },
                            "type": "object"
                          }
                        }
                      },
                      "required": [
                        "email"
                      ],
                      "type": "object"
                    }
                  },
                  "callback": {
                    "type": "object",
                    "description": "Callback function to notify users when an import is complete.",
                    "required": [
                      "url",
                      "requestType"
                    ],
                    "properties": {
                      "url": {
                        "type": "string",
                        "description": "The URL endpoint which the importer will make a request to once the import has completed."
                      },
                      "requestType": {
                        "type": "string",
                        "description": "Can be set to either “GET” or “POST”. Determines the type of HTTP request which will be sent to the specified endpoint.",
                        "default": "POST"
                      },
                      "detailed_results": {
                        "type": "string",
                        "description": "When set to “true” and the requestType parameter is set to “POST”, the callback will include the number of successes and failures in the originating request, as well as an array of error messages for each failed contact.",
                        "default": "true"
                      },
                      "params": {
                        "type": "array",
                        "description": "A list of parameters to include in the callback request. Add each parameter in the form of a key-value pair. For a GET request, each parameter will be appended to the end of the URL in a query string. For a POST request, parameters will be included in the body of the request.",
                        "items": {
                          "properties": {
                            "key": {
                              "type": "string"
                            },
                            "value": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        }
                      },
                      "headers": {
                        "type": "array",
                        "description": "A list of headers to include in the callback request. Add each header in the form of a key-value pair.",
                        "items": {
                          "properties": {
                            "key": {
                              "type": "string"
                            },
                            "value": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        }
                      }
                    }
                  }
                }
              },
              "examples": {
                "Request Example": {
                  "value": {
                    "contacts": [
                      {
                        "email": "someone@somewhere.com",
                        "first_name": "Jane",
                        "last_name": "Doe",
                        "phone": "123-456-7890",
                        "customer_acct_name": "ActiveCampaign",
                        "exclude_automations": false,
                        "tags": [
                          "dictumst",
                          "aliquam",
                          "augue quam",
                          "sollicitudin rutrum"
                        ],
                        "fields": [
                          {
                            "id": 1,
                            "value": "foo"
                          },
                          {
                            "id": 2,
                            "value": "||foo||bar||baz||"
                          }
                        ],
                        "subscribe": [
                          {
                            "listid": 1
                          },
                          {
                            "listid": 2
                          }
                        ],
                        "unsubscribe": [
                          {
                            "listid": 3
                          }
                        ]
                      }
                    ],
                    "callback": {
                      "url": "www.your_web_server.com",
                      "requestType": "POST",
                      "detailed_results": "true",
                      "params": [
                        {
                          "key": "",
                          "value": ""
                        }
                      ],
                      "headers": [
                        {
                          "key": "",
                          "value": ""
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
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n   \"Success\":1,\n   \"queued_contacts\":1,\n   \"batchId\":\"0641fbdd-f62f-4c2c-ba02-3a83d5d11ac9\",\n   \"message\":\"Contact import queued\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "Success": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "queued_contacts": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "batchId": {
                      "type": "string",
                      "example": "0641fbdd-f62f-4c2c-ba02-3a83d5d11ac9"
                    },
                    "message": {
                      "type": "string",
                      "example": "Contact import queued"
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
                  "Contact Create Fail": {
                    "value": "{\n\t\"success\": 0,\n\t\"message\": \"JSON payload did not pass validation. Please fix failure Reasons and retry. The import was not queued for processing.\",\n\t\"failureReasons\": [{\n\t\t\"contact\": 230,\n\t\t\"failureReason\": \"Field‘ email’ incorrect format\"\n\t}]\n}"
                  },
                  "Other Error": {
                    "value": "{\n\t\"success\": 0,\n\t\"message\": \"Rate limit exceeded.\",\n\t\"failureReasons\": [\"Up to 100 imports may be requested per minute.Please batch contacts into larger requests, or retry this request in a minute.\"]\n}"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "title": "Contact Create Fail",
                      "type": "object",
                      "properties": {
                        "success": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "JSON payload did not pass validation. Please fix failure Reasons and retry. The import was not queued for processing."
                        },
                        "failureReasons": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "contact": {
                                "type": "integer",
                                "example": 230,
                                "default": 0
                              },
                              "failureReason": {
                                "type": "string",
                                "example": "Field‘ email’ incorrect format"
                              }
                            }
                          }
                        }
                      }
                    },
                    {
                      "title": "Other Error",
                      "type": "object",
                      "properties": {
                        "success": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "Rate limit exceeded."
                        },
                        "failureReasons": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "Up to 100 imports may be requested per minute.Please batch contacts into larger requests, or retry this request in a minute."
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