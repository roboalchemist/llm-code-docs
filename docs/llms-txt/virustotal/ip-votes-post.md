# Source: https://virustotal.readme.io/reference/ip-votes-post.md

# Add a vote to an IP address

With this endpoint you can post a vote for a given file. The body for the POST request must be the JSON representation of a [vote object](https://virustotal.readme.io/reference/vote-object). Note however that you don't need to provide an ID for the object, as they are automatically generated for new votes.
The verdict attribute must have be either harmless or malicious.

```json
{
  "data": {
    "type": "vote",
    "attributes": {
    	"verdict": "harmless"
    }
  }
}
```

Returns a [Vote](https://virustotal.readme.io/reference/vote-object) object.

````

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/ip_addresses/{ip}/votes": {
      "post": {
        "summary": "Add a vote to an IP address",
        "description": "",
        "operationId": "ip-votes-post",
        "parameters": [
          {
            "name": "ip",
            "in": "path",
            "description": "IP Address",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "x-apikey",
            "in": "header",
            "required": true,
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
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "Vote object",
                    "default": "{\"type\": \"vote\", \"attributes\": {\"verdict\": \"malicious\"}}",
                    "format": "json"
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
                    "value": "{\n    \"data\": {\n        \"attributes\": {\n            \"date\": 1574246672,\n            \"value\": 1,\n            \"verdict\": \"harmless\"\n        },\n        \"id\": \"i-IP-a68784ad\",\n        \"links\": {\n            \"self\": null\n        },\n        \"type\": \"vote\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "attributes": {
                          "type": "object",
                          "properties": {
                            "date": {
                              "type": "integer",
                              "example": 1574246672,
                              "default": 0
                            },
                            "value": {
                              "type": "integer",
                              "example": 1,
                              "default": 0
                            },
                            "verdict": {
                              "type": "string",
                              "example": "harmless"
                            }
                          }
                        },
                        "id": {
                          "type": "string",
                          "example": "i-IP-a68784ad"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "self": {}
                          }
                        },
                        "type": {
                          "type": "string",
                          "example": "vote"
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
          "409": {
            "description": "409",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": {\n        \"code\": \"AlreadyExistsError\",\n        \"message\": \"User \\\"UserName\\\" already voted \\\"harmless\\\" for this ip_address\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "object",
                      "properties": {
                        "code": {
                          "type": "string",
                          "example": "AlreadyExistsError"
                        },
                        "message": {
                          "type": "string",
                          "example": "User \"UserName\" already voted \"harmless\" for this ip_address"
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
        "security": []
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```
````