# Source: https://developer.mixpanel.com/reference/delete-group.md

# Delete Group

Deletes a group profile from Mixpanel.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Ingestion API",
    "description": "APIs allowing for event-based tracking and user profile handling.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "1.0.0",
    "contact": {
      "url": "https://mixpanel.com/get-support"
    }
  },
  "servers": [
    {
      "url": "https://{region}.mixpanel.com",
      "description": "Mixpanel's data collection server.",
      "variables": {
        "region": {
          "default": "api",
          "enum": [
            "api",
            "api-eu",
            "api-in"
          ],
          "description": "The server location to be used:\n  * `api` - The default (US) servers used for most projects\n  * `api-eu` - EU servers if you are enrolled in EU Data Residency\n  * `api-in` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Group Profiles",
      "description": "Manage groups and their properties"
    }
  ],
  "paths": {
    "/groups#group-delete": {
      "post": {
        "operationId": "delete-group",
        "tags": [
          "Group Profiles"
        ],
        "summary": "Delete Group",
        "description": "Deletes a group profile from Mixpanel.",
        "security": [
          {}
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/Verbose"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "object",
                  "description": "A JSON update object, with $token, $group_key, and $group_id values and a $delete key.",
                  "required": [
                    "$token",
                    "$group_key",
                    "$group_id",
                    "$set"
                  ],
                  "properties": {
                    "$token": {
                      "type": "string",
                      "default": "YOUR_PROJECT_TOKEN"
                    },
                    "$group_key": {
                      "type": "string",
                      "default": "Company"
                    },
                    "$group_id": {
                      "type": "string",
                      "default": "Mixpanel"
                    },
                    "$delete": {
                      "type": "string",
                      "nullable": true,
                      "default": "null"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/Received"
          },
          "401": {
            "$ref": "#/components/responses/Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/Forbidden"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": [
              "error"
            ]
          }
        }
      },
      "IntegerPropertyAsBooleanFlag": {
        "type": "integer",
        "minimum": 0,
        "maximum": 1
      }
    },
    "responses": {
      "Received": {
        "content": {
          "text/plain": {
            "schema": {
              "type": "integer",
              "enum": [
                1,
                0
              ]
            },
            "examples": {
              "Valid Data": {
                "value": 1
              },
              "Invalid Data": {
                "value": 0
              }
            }
          }
        },
        "description": "\n* `1` - One or more objects provided are valid. This does not signify a valid project token or secret.\n* `0` - No data objects in the body are valid.\n"
      },
      "Unauthorized": {
        "description": "Unauthorized",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "Forbidden": {
        "description": "Forbidden",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      }
    },
    "parameters": {
      "Verbose": {
        "in": "query",
        "name": "verbose",
        "required": false,
        "schema": {
          "$ref": "#/components/schemas/IntegerPropertyAsBooleanFlag"
        },
        "description": "If present and equal to 1, Mixpanel will respond with a JSON Object describing the success or failure of the tracking call. The returned object will have two keys: `status`, with the value 1 on success and 0 on failure, and `error`, with a string-valued error message if the request wasn't successful. This is useful for debugging during implementation."
      }
    }
  },
  "x-readme-deploy-id": "ingestion",
  "x-explorer-enabled": true,
  "x-proxy-enabled": true,
  "x-samples-enabled": true,
  "x-samples-languages": [
    "curl",
    "node",
    "ruby",
    "javascript",
    "python"
  ]
}
```