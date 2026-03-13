# Source: https://developers-classic.mailerlite.com/reference/add-single-subscriber.md

# /groups/:id/subscribers

Add new single subscriber to specified group [Rate limited]

[block:api-header]
{
  "type": "basic",
  "title": "Response Body Parameters"
}
[/block]

Response contains [Single Subscriber](https://developers-classic.mailerlite.com/docs/single-subscriber) object.

[block:api-header]
{
  "type": "basic",
  "title": "Double opt-in for API"
}
[/block]

Find out how to enable it [in our help center](https://help.mailerlite.com/article/show/29273-double-opt-in-for-api).

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "V2 production",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api.mailerlite.com/api/v2"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "X-MailerLite-ApiKey",
        "in": "header",
        "x-default": "your api key"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/groups/{id}/subscribers": {
      "post": {
        "summary": "/groups/:id/subscribers",
        "description": "Add new single subscriber to specified group [Rate limited]",
        "operationId": "add-single-subscriber",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of group",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "email": {
                    "type": "string",
                    "description": "email of new subscriber",
                    "default": "null"
                  },
                  "name": {
                    "type": "string"
                  },
                  "fields": {
                    "type": "object",
                    "description": "object that contains your custom fields. i.e. company, city, state, etc.",
                    "properties": {
                      "company": {
                        "type": "string"
                      },
                      "city": {
                        "type": "string"
                      }
                    }
                  },
                  "resubscribe": {
                    "type": "boolean",
                    "description": "reactivate subscriber if value is true",
                    "default": false
                  },
                  "autoresponders": {
                    "type": "boolean",
                    "description": "autoresponders will be sent if value is true",
                    "default": true
                  },
                  "type": {
                    "type": "string",
                    "description": "available values: unsubscribed, active, unconfirmed",
                    "default": "null"
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
                    "value": "{\n  \"id\": 1343965485,\n  \"name\": \"John\",\n  \"email\": \"demo@mailerlite.com\",\n  \"sent\": 0,\n  \"opened\": 0,\n  \"clicked\": 0,\n  \"type\": \"active\",\n  \"fields\": [\n    {\n      \"key\": \"email\",\n      \"value\": \"demo@mailerlite.com\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"name\",\n      \"value\": \"John\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"last_name\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"company\",\n      \"value\": \"MailerLite\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"country\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"city\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"phone\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"state\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"zip\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    }\n  ],\n  \"date_subscribe\": null,\n  \"date_unsubscribe\": null,\n  \"date_created\": \"2016-04-04\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "example": 1343965485,
                      "default": 0
                    },
                    "name": {
                      "type": "string",
                      "example": "John"
                    },
                    "email": {
                      "type": "string",
                      "example": "demo@mailerlite.com"
                    },
                    "sent": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "opened": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "clicked": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "type": {
                      "type": "string",
                      "example": "active"
                    },
                    "fields": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "key": {
                            "type": "string",
                            "example": "email"
                          },
                          "value": {
                            "type": "string",
                            "example": "demo@mailerlite.com"
                          },
                          "type": {
                            "type": "string",
                            "example": "TEXT"
                          }
                        }
                      }
                    },
                    "date_subscribe": {},
                    "date_unsubscribe": {},
                    "date_created": {
                      "type": "string",
                      "example": "2016-04-04"
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
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Group Not Found": {
                    "value": "{\n  \"error\": {\n    \"code\": 123,\n    \"message\": \"Group not found\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "object",
                      "properties": {
                        "code": {
                          "type": "integer",
                          "example": 123,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "Group not found"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl -X POST https://api.mailerlite.com/api/v2/groups/3640549/subscribers \\\n-d '{\"email\":\"demo@mailerlite.com\", \"name\": \"John\", \"fields\": {\"company\": \"MailerLite\"}}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            },
            {
              "language": "php",
              "code": "<?php\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$groupId = 123;\n\n$subscriber = [\n  'email' => 'johndoe@mailerlite.com',\n  'name' => 'John',\n  'fields' => [\n    'surname' => 'Doe',\n    'company' => 'MailerLite'\n  ]\n];\n\n$addedSubscriber = $groupsApi->addSubscriber($groupId, $subscriber); // returns added subscriber",
              "name": "PHP (SDK)"
            },
            {
              "language": "csharp",
              "code": "var client = new RestClient(\"https://api.mailerlite.com/api/v2/groups/3640549/subscribers\");\nvar request = new RestRequest(Method.POST);\nrequest.AddHeader(\"x-mailerlite-apikey\", \"fc7b8c5b32067bcd47cafb5f475d2fe9\");\nrequest.AddHeader(\"content-type\", \"application/json\");\nrequest.AddParameter(\"application/json\", \"{\\\"email\\\":\\\"demo@mailerlite.com\\\", \\\"name\\\": \\\"John\\\", \\\"fields\\\": {\\\"company\\\": \\\"MailerLite\\\"}}\", ParameterType.RequestBody);\nIRestResponse response = client.Execute(request);",
              "name": "C# (.NET RestSharp)"
            },
            {
              "language": "java",
              "code": "HttpResponse<String> response = Unirest.post(\"https://api.mailerlite.com/api/v2/groups/3640549/subscribers\")\n  .header(\"content-type\", \"application/json\")\n  .header(\"x-mailerlite-apikey\", \"fc7b8c5b32067bcd47cafb5f475d2fe9\")\n  .body(\"{\\\"email\\\":\\\"demo@mailerlite.com\\\", \\\"name\\\": \\\"John\\\",  \\\"fields\\\": {\\\"company\\\": \\\"MailerLite\\\"}}\")\n  .asString();",
              "name": "Java (Unirest)"
            },
            {
              "language": "php",
              "code": "<?php\n\n$curl = curl_init();\n\ncurl_setopt_array($curl, array(\n  CURLOPT_URL => \"https://api.mailerlite.com/api/v2/groups/3640549/subscribers\",\n  CURLOPT_RETURNTRANSFER => true,\n  CURLOPT_ENCODING => \"\",\n  CURLOPT_MAXREDIRS => 10,\n  CURLOPT_TIMEOUT => 30,\n  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,\n  CURLOPT_CUSTOMREQUEST => \"POST\",\n  CURLOPT_POSTFIELDS => \"{\\\"email\\\":\\\"demo@mailerlite.com\\\", \\\"name\\\": \\\"John\\\", \\\"fields\\\": {\\\"company\\\": \\\"MailerLite\\\"}}\",\n  CURLOPT_HTTPHEADER => array(\n    \"content-type: application/json\",\n    \"x-mailerlite-apikey: fc7b8c5b32067bcd47cafb5f475d2fe9\"\n  ),\n));\n\n$response = curl_exec($curl);\n$err = curl_error($curl);\n\ncurl_close($curl);\n\nif ($err) {\n  echo \"cURL Error #:\" . $err;\n} else {\n  echo $response;\n}",
              "name": "PHP (cURL)"
            },
            {
              "language": "python",
              "code": "import requests, json\n\nurl = \"https://api.mailerlite.com/api/v2/groups/3640549/subscribers\"\n\ndata = {\n    'name'   : 'John',\n    'email'  : 'demo@mailerlite.com',\n    'fields' : {'company': 'MailerLite'}\n}\n\npayload = json.dumps(data)\n\nheaders = {\n    'content-type': \"application/json\",\n    'x-mailerlite-apikey': \"fc7b8c5b32067bcd47cafb5f475d2fe9\"\n}\n\nresponse = requests.request(\"POST\", url, data=payload, headers=headers)\n\nprint(response.text)"
            },
            {
              "language": "http",
              "code": "POST /api/v2/groups/3640549/subscribers HTTP/1.1\nHost: api.mailerlite.com\nContent-Type: application/json\nX-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\n\n{\"email\":\"demo@mailerlite.com\", \"name\":\"John\", \"fields\": {\"company\": \"MailerLite\"}}"
            }
          ],
          "samples-languages": [
            "curl",
            "php",
            "csharp",
            "java",
            "python",
            "http"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [
      {
        "key": "X-MailerLite-ApiDocs",
        "value": "true"
      }
    ],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true,
  "_id": "58b53b141065f9c438aa1afe:56e5b06f9191742000ef207c"
}
```