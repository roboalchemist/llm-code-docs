# Source: https://virustotal.readme.io/reference/ip-votes.md

# Get votes on an IP address

Returns a list of [Vote](https://virustotal.readme.io/reference/vote-object) objects.

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
      "get": {
        "summary": "Get votes on an IP address",
        "description": "",
        "operationId": "ip-votes",
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
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"data\": [\n        {\n            \"attributes\": {\n                \"date\": 1574246328,\n                \"value\": 47,\n                \"verdict\": \"harmless\"\n            },\n            \"id\": \"i-1.1.1.1-a68784ad\",\n            \"links\": {\n                \"self\": \"https://www.virustotal.com/api/v3/votes/i-1.1.1.1-a68784ad\"\n            },\n            \"type\": \"vote\"\n        },\n        {\n            \"attributes\": {\n                \"date\": 1569486791,\n                \"value\": -1,\n                \"verdict\": \"malicious\"\n            },\n            \"id\": \"i-1.1.1.1-e15e57e9\",\n            \"links\": {\n                \"self\": \"https://www.virustotal.com/api/v3/votes/i-1.1.1.1-e15e57e9\"\n            },\n            \"type\": \"vote\"\n        }\n    ],\n    \"links\": {\n        \"self\": \"https://www.virustotal.com/api/v3/ip_addresses/1.1.1.1/votes?limit=10\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "attributes": {
                            "type": "object",
                            "properties": {
                              "date": {
                                "type": "integer",
                                "example": 1574246328,
                                "default": 0
                              },
                              "value": {
                                "type": "integer",
                                "example": 47,
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
                            "example": "i-1.1.1.1-a68784ad"
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "self": {
                                "type": "string",
                                "example": "https://www.virustotal.com/api/v3/votes/i-1.1.1.1-a68784ad"
                              }
                            }
                          },
                          "type": {
                            "type": "string",
                            "example": "vote"
                          }
                        }
                      }
                    },
                    "links": {
                      "type": "object",
                      "properties": {
                        "self": {
                          "type": "string",
                          "example": "https://www.virustotal.com/api/v3/ip_addresses/1.1.1.1/votes?limit=10"
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