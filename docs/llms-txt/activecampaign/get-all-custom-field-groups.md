# Source: https://developers.activecampaign.com/reference/get-all-custom-field-groups.md

# Get All Custom Field Groups

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
    "/groupMembers": {
      "get": {
        "summary": "Get All Custom Field Groups",
        "description": "",
        "operationId": "get-all-custom-field-groups",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"groupDefinitions\": [\n        {\n            \"id\": 1,\n            \"type_id\": 1,\n            \"label\": \"{**DEFAULT**}\",\n            \"ordernum\": 1,\n            \"links\": {\n                \"groupMembers\": \"https://account.api-us1.com/api/3/groupMembers?group_id=1\",\n                \"groupType\": \"https://account.api-us1.com/api/3/groupTypes/1\"\n            }\n        },\n        {\n            \"id\": 2,\n            \"type_id\": 2,\n            \"label\": \"{**DEAL_DEFAULT**}\",\n            \"ordernum\": 2,\n            \"links\": {\n                \"groupMembers\": \"https://account.api-us1.com/api/3/groupMembers?group_id=2\",\n                \"groupType\": \"https://account.api-us1.com/api/3/groupTypes/2\"\n            }\n        },\n        {\n            \"id\": 3,\n            \"type_id\": 3,\n            \"label\": \"{**ACCOUNT_DEFAULT**}\",\n            \"ordernum\": 3,\n            \"links\": {\n                \"groupMembers\": \"https://account.api-us1.com/api/3/groupMembers?group_id=3\",\n                \"groupType\": \"https://account.api-us1.com/api/3/groupTypes/3\"\n            }\n        },\n        {\n            \"id\": 21,\n            \"type_id\": 1,\n            \"label\": \"CustomName\",\n            \"ordernum\": 3,\n            \"links\": {\n                \"groupMembers\": \"https://account.api-us1.com/api/3/groupMembers?group_id=21\",\n                \"groupType\": \"https://account.api-us1.com/api/3/groupTypes/1\"\n            }\n        }\n    ]\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "groupDefinitions": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "example": 1,
                            "default": 0
                          },
                          "type_id": {
                            "type": "integer",
                            "example": 1,
                            "default": 0
                          },
                          "label": {
                            "type": "string",
                            "example": "{**DEFAULT**}"
                          },
                          "ordernum": {
                            "type": "integer",
                            "example": 1,
                            "default": 0
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "groupMembers": {
                                "type": "string",
                                "example": "https://account.api-us1.com/api/3/groupMembers?group_id=1"
                              },
                              "groupType": {
                                "type": "string",
                                "example": "https://account.api-us1.com/api/3/groupTypes/1"
                              }
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