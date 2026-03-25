# Source: https://developers.activecampaign.com/reference/update-a-message.md

# Update a message

> 🚧 Messages edited through the API will not show updates in the UI preview window.
>
> When a message is edited through the API, the preview window and email builder will not show the updated contents, and will save over whatever updates were made with the API with what is shown in the email editor.
>
> To preview a message that was updated with the API, select "Test And Preview" in the campaign builder window, then select your preview option:
>
> ![](https://files.readme.io/985ffb1c7e643a2e484ec9b6864ff67ef372f0173c1ec1990a31c0f12a17b68c-image.png)

```json PUT /messages/:id (Example REQUEST)
{
	"message": {
	    "fromname": "AC Admin",
        "fromemail": "noreply@example.com",
        "reply2": "hello@example.com",
        "subject": "You are subscribing to %LISTNAME%",
        "preheader_text": "Pre-header Text",
        "text": "hello",
        "html": "<div>hello</div>"
	}
}
```

```json PUT /messages/:id (Example RESPONSE)
{
    "message": {
        "userid": "0",
        "ed_instanceid": "0",
        "ed_version": "1",
        "cdate": "2024-08-06T16:31:45-05:00",
        "mdate": "2024-08-06T16:33:23-05:00",
        "name": "",
        "fromname": "AC Admin",
        "fromemail": "noreply@example.com",
        "reply2": "hello@example.com",
        "priority": "3",
        "charset": "utf-8",
        "encoding": "8bit",
        "format": "mime",
        "subject": "You are subscribing to %LISTNAME%",
        "preheader_text": "Pre-header Text",
        "text": "hello",
        "html": "<div>hello</div>",
        "htmlfetch": "now",
        "textfetch": "now",
        "hidden": "0",
        "preview_mime": "",
        "preview_data": null,
        "has_predictive_content": "0",
        "links": {
            "user": "https://accountName.api-us1.com/api/3/messages/56/user",
            "hyperlinks": "https://accountName.api-us1.com/api/3/messages/56/hyperlinks"
        },
        "id": "56",
        "user": null
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
    "/messages/{id}": {
      "put": {
        "summary": "Update a message",
        "description": "",
        "operationId": "update-a-message",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of the message to update",
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
                  "message": {
                    "properties": {
                      "fromname": {
                        "type": "string",
                        "description": "Name of sender"
                      },
                      "fromemail": {
                        "type": "string",
                        "description": "Email of sender"
                      },
                      "reply2": {
                        "type": "string",
                        "description": "Reply email for the recipient to reply to"
                      },
                      "subject": {
                        "type": "string",
                        "description": "Subject of message"
                      },
                      "preheader_text": {
                        "type": "string",
                        "description": "Preheader Text"
                      },
                      "name": {
                        "type": "string",
                        "description": "Name of the message"
                      },
                      "text": {
                        "type": "string",
                        "description": "Text content"
                      },
                      "html": {
                        "type": "string",
                        "description": "HTML Content"
                      }
                    },
                    "required": [],
                    "type": "object"
                  }
                }
              },
              "examples": {
                "Request Example": {
                  "value": {
                    "message": {
                      "fromname": "John Doe",
                      "fromemail": "noreply@example.com",
                      "reply2": "hello@example.com",
                      "subject": "You are subscribing to %LISTNAME%",
                      "preheader_text": "Pre-header Text"
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
                    "value": "{\n    \"message\": {\n        \"userid\": \"0\",\n        \"ed_instanceid\": \"0\",\n        \"ed_version\": \"1\",\n        \"cdate\": \"2024-08-06T16:31:45-05:00\",\n        \"mdate\": \"2024-08-06T16:33:23-05:00\",\n        \"name\": \"\",\n        \"fromname\": \"AC Admin\",\n        \"fromemail\": \"noreply@example.com\",\n        \"reply2\": \"hello@example.com\",\n        \"priority\": \"3\",\n        \"charset\": \"utf-8\",\n        \"encoding\": \"8bit\",\n        \"format\": \"mime\",\n        \"subject\": \"You are subscribing to %LISTNAME%\",\n        \"preheader_text\": \"Pre-header Text\",\n        \"text\": \"hello\",\n        \"html\": \"<div>hello</div>\",\n        \"htmlfetch\": \"now\",\n        \"textfetch\": \"now\",\n        \"hidden\": \"0\",\n        \"preview_mime\": \"\",\n        \"preview_data\": null,\n        \"has_predictive_content\": \"0\",\n        \"links\": {\n            \"user\": \"https://accountName.api-us1.com/api/3/messages/56/user\",\n            \"hyperlinks\": \"https://accountName.api-us1.com/api/3/messages/56/hyperlinks\"\n        },\n        \"id\": \"56\",\n        \"user\": null\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "object",
                      "properties": {
                        "userid": {
                          "type": "string",
                          "example": "0"
                        },
                        "ed_instanceid": {
                          "type": "string",
                          "example": "0"
                        },
                        "ed_version": {
                          "type": "string",
                          "example": "1"
                        },
                        "cdate": {
                          "type": "string",
                          "example": "2024-08-06T16:31:45-05:00"
                        },
                        "mdate": {
                          "type": "string",
                          "example": "2024-08-06T16:33:23-05:00"
                        },
                        "name": {
                          "type": "string",
                          "example": ""
                        },
                        "fromname": {
                          "type": "string",
                          "example": "AC Admin"
                        },
                        "fromemail": {
                          "type": "string",
                          "example": "noreply@example.com"
                        },
                        "reply2": {
                          "type": "string",
                          "example": "hello@example.com"
                        },
                        "priority": {
                          "type": "string",
                          "example": "3"
                        },
                        "charset": {
                          "type": "string",
                          "example": "utf-8"
                        },
                        "encoding": {
                          "type": "string",
                          "example": "8bit"
                        },
                        "format": {
                          "type": "string",
                          "example": "mime"
                        },
                        "subject": {
                          "type": "string",
                          "example": "You are subscribing to %LISTNAME%"
                        },
                        "preheader_text": {
                          "type": "string",
                          "example": "Pre-header Text"
                        },
                        "text": {
                          "type": "string",
                          "example": "hello"
                        },
                        "html": {
                          "type": "string",
                          "example": "<div>hello</div>"
                        },
                        "htmlfetch": {
                          "type": "string",
                          "example": "now"
                        },
                        "textfetch": {
                          "type": "string",
                          "example": "now"
                        },
                        "hidden": {
                          "type": "string",
                          "example": "0"
                        },
                        "preview_mime": {
                          "type": "string",
                          "example": ""
                        },
                        "preview_data": {},
                        "has_predictive_content": {
                          "type": "string",
                          "example": "0"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "user": {
                              "type": "string",
                              "example": "https://accountName.api-us1.com/api/3/messages/56/user"
                            },
                            "hyperlinks": {
                              "type": "string",
                              "example": "https://accountName.api-us1.com/api/3/messages/56/hyperlinks"
                            }
                          }
                        },
                        "id": {
                          "type": "string",
                          "example": "56"
                        },
                        "user": {}
                      }
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"message\": \"No Result found for Message with id 543\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "No Result found for Message with id 543"
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