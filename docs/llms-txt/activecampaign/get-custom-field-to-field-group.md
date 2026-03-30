# Source: https://developers.activecampaign.com/reference/get-custom-field-to-field-group.md

# Get Custom Field Group by ID

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
    "/groupMembers/{groupID}": {
      "get": {
        "summary": "Get Custom Field Group by ID",
        "description": "",
        "operationId": "get-custom-field-to-field-group",
        "parameters": [
          {
            "name": "groupID",
            "in": "path",
            "description": "Group ID",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"groupMember\": {\n        \"id\": 89,\n        \"group_id\": 1,\n        \"rel_id\": 5,\n        \"ordernum\": 20,\n        \"links\": {\n            \"groupDefinition\": \"https://:account.api-us1.com/api/3/groupDefinitions/1\"\n        }\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "groupMember": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "example": 89,
                          "default": 0
                        },
                        "group_id": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "rel_id": {
                          "type": "integer",
                          "example": 5,
                          "default": 0
                        },
                        "ordernum": {
                          "type": "integer",
                          "example": 20,
                          "default": 0
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "groupDefinition": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/groupDefinitions/1"
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
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"errors\": [\n        {\n            \"status\": 404,\n            \"title\": \"Not Found\"\n        }\n    ]\n}"
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
                            "example": 404,
                            "default": 0
                          },
                          "title": {
                            "type": "string",
                            "example": "Not Found"
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
        "deprecated": false,
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {},
              "examples": {
                "POST": {
                  "value": {
                    "groupMember": {
                      "rel_id": "10",
                      "ordernum": null,
                      "group_id": "1"
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
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```