# Source: https://developers.activecampaign.com/reference/create-campaign.md

# Create Campaign

```json Example REQUEST
{
    "canSplitContent": false,
    "type": "single",
    "name": "Campaign Name"
}
```

```Text Example RESPONSE
{
    "id": 149,
    "name": "Campaign Name",
    "type": "single",
    "canSplitContent": false
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
    "/campaign": {
      "post": {
        "summary": "Create Campaign",
        "description": "",
        "operationId": "create-campaign",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "name",
                  "type"
                ],
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string"
                  },
                  "canSplitContent": {
                    "type": "boolean",
                    "default": false
                  }
                }
              },
              "examples": {
                "Create Campaign": {
                  "value": {
                    "canSplitContent": false,
                    "type": "single",
                    "name": "Campaign Name"
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
                    "value": "{\n    \"id\": 149,\n    \"name\": \"Campaign Name\",\n    \"type\": \"single\",\n    \"canSplitContent\": false\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "example": 149,
                      "default": 0
                    },
                    "name": {
                      "type": "string",
                      "example": "Campaign Name"
                    },
                    "type": {
                      "type": "string",
                      "example": "single"
                    },
                    "canSplitContent": {
                      "type": "boolean",
                      "example": false,
                      "default": true
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
                    "value": "{\n    \"errors\": [\n        \"Field name is required\",\n        \"Field type must be of type string\"\n    ]\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "errors": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "Field name is required"
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