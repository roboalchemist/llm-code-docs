# Source: https://developers-classic.mailerlite.com/reference/add-many-subscribers.md

# /groups/:id/subscribers/import

Add many new subscribers to specified group at once [Rate limited]

[block:api-header]
{
  "type": "basic",
  "title": "Response Body Parameters"
}
[/block]

Response contains [Single Subscriber](https://developers-classic.mailerlite.com/docs/single-subscriber) object.

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
    "/groups/{id}/subscribers/import": {
      "post": {
        "summary": "/groups/:id/subscribers/import",
        "description": "Add many new subscribers to specified group at once [Rate limited]",
        "operationId": "add-many-subscribers",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "schema": {
              "type": "integer",
              "format": "int32"
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
                  "subscribers": {
                    "type": "array",
                    "items": {
                      "properties": {
                        "email": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "email"
                      ],
                      "type": "object"
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
                    "default": false
                  },
                  "return_status": {
                    "type": "boolean",
                    "description": "run import in the background",
                    "default": true
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
                  "OK": {
                    "value": "{\n  \"imported\": [\n    {\n      \"id\": 1343991205,\n      \"email\": \"another.demo@mailerlite.com\"\n    }\n  ],\n  \"updated\": [\n  ],\n  \"unchanged\": [\n    {\n      \"id\": 1343965485,\n      \"email\": \"demo@mailerlite.com\"\n    }\n  ],\n  \"errors\": []\n}"
                  },
                  "OK (return_status is set to false)": {
                    "value": "{\n  \"id\": 1234,\n  \"type\": \"import\",\n  \"stats\": {\n    \"imported\": 0,\n    \"duplicates\": 0,\n    \"invalid\": 0,\n    \"unchanged\": 0,\n    \"total\": 0\n  },\n  \"options\": {\n    \"resubscribe\": false,\n    \"autoresponders\": false\n  },\n  \"is_finished\": false,\n  \"is_importing\": true,\n  \"is_killed\": false,\n  \"created_at\": \"2017-04-10 15:47:47\"\n}"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "title": "OK",
                      "type": "object",
                      "properties": {
                        "imported": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "integer",
                                "example": 1343991205,
                                "default": 0
                              },
                              "email": {
                                "type": "string",
                                "example": "another.demo@mailerlite.com"
                              }
                            }
                          }
                        },
                        "updated": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {}
                          }
                        },
                        "unchanged": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "integer",
                                "example": 1343965485,
                                "default": 0
                              },
                              "email": {
                                "type": "string",
                                "example": "demo@mailerlite.com"
                              }
                            }
                          }
                        },
                        "errors": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {}
                          }
                        }
                      }
                    },
                    {
                      "title": "OK (return_status is set to false)",
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "example": 1234,
                          "default": 0
                        },
                        "type": {
                          "type": "string",
                          "example": "import"
                        },
                        "stats": {
                          "type": "object",
                          "properties": {
                            "imported": {
                              "type": "integer",
                              "example": 0,
                              "default": 0
                            },
                            "duplicates": {
                              "type": "integer",
                              "example": 0,
                              "default": 0
                            },
                            "invalid": {
                              "type": "integer",
                              "example": 0,
                              "default": 0
                            },
                            "unchanged": {
                              "type": "integer",
                              "example": 0,
                              "default": 0
                            },
                            "total": {
                              "type": "integer",
                              "example": 0,
                              "default": 0
                            }
                          }
                        },
                        "options": {
                          "type": "object",
                          "properties": {
                            "resubscribe": {
                              "type": "boolean",
                              "example": false,
                              "default": true
                            },
                            "autoresponders": {
                              "type": "boolean",
                              "example": false,
                              "default": true
                            }
                          }
                        },
                        "is_finished": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        },
                        "is_importing": {
                          "type": "boolean",
                          "example": true,
                          "default": true
                        },
                        "is_killed": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        },
                        "created_at": {
                          "type": "string",
                          "example": "2017-04-10 15:47:47"
                        }
                      }
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "No subscribers provided": {
                    "value": "{\n  \"error\": {\n    \"code\": 123,\n    \"message\": \"Wrong data provided\"\n  }\n}"
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
                          "example": "Wrong data provided"
                        }
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
              "code": "curl -X POST https://api.mailerlite.com/api/v2/groups/123456/subscribers/import \\\n-d '{\"subscribers\": [{\"email\": \"demo@mailerlite.com\"}, {\"email\": \"another.demo@mailerlite.com\", \"fields\": {\"name\": \"Another Demo\", \"company\": \"MailerLite\"}}]}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            },
            {
              "language": "php",
              "code": "<?php\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$groupId = 123;\n\n$subscribers = [\n  [\n    'email' => 'johndoe@mailerlite.com',\n  \t'fields' => [\n    \t'name' => 'John',\n    \t'surname' => 'Doe',\n    \t'company' => 'MailerLite'\n  \t],\n  ],\n  [\n    'email' => 'johndoejr@mailerlite.com',\n  \t'fields' => [\n    \t'name' => 'John Jr.',\n    \t'surname' => 'Doe',\n    \t'company' => 'MailerLite'\n  \t]\n  ]\n];\n\n$options = [\n  'resubscribe' => false,\n  'autoresponders' => true // send autoresponders for successfully imported subscribers \n];\n\n$addedSubscribers = $groupsApi->importSubscribers($groupId, $subscribers, $options); // returns imported subscribers divided into groups by import status"
            },
            {
              "language": "text",
              "code": "curl -X POST https://api.mailerlite.com/api/v2/groups/123456/subscribers/import \\\n-d '{\"subscribers\": [{\"email\": \"demo@mailerlite.com\"}, {\"email\": \"another.demo@mailerlite.com\", \"fields\": {\"name\": \"Another Demo\", \"company\": \"MailerLite\"}}], \"return_status\": false}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\"",
              "name": "cURL (run import in the background)"
            }
          ],
          "samples-languages": [
            "curl",
            "php",
            "text"
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
  "_id": "58b53b141065f9c438aa1afe:56fe249dd393740e0080f408"
}
```