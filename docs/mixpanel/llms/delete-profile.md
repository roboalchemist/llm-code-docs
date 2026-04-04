# Source: https://developer.mixpanel.com/reference/delete-profile.md

# Delete Profile

Permanently delete the profile from Mixpanel, along with all of its properties. The $delete object value is ignored - the profile is determined by the $distinct_id from the request itself.

If you have duplicate profiles, use property $ignore_alias set to true so that you don't delete the original profile when trying to delete the duplicate (as they pass in the alias as the distinct_id).


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
      "name": "User Profiles",
      "description": "Manage profiles and their properties"
    }
  ],
  "paths": {
    "/engage#profile-delete": {
      "post": {
        "operationId": "delete-profile",
        "tags": [
          "User Profiles"
        ],
        "summary": "Delete Profile",
        "description": "Permanently delete the profile from Mixpanel, along with all of its properties. The $delete object value is ignored - the profile is determined by the $distinct_id from the request itself.\n\nIf you have duplicate profiles, use property $ignore_alias set to true so that you don't delete the original profile when trying to delete the duplicate (as they pass in the alias as the distinct_id).\n",
        "security": [
          {}
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/Strict"
          },
          {
            "$ref": "#/components/parameters/Verbose"
          },
          {
            "$ref": "#/components/parameters/JavascriptWithCallback"
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
                  "description": "A JSON update object, with a $token, $distinct_id, $ignore_alias and a $delete operation object.",
                  "required": [
                    "$token",
                    "$distinct_id",
                    "$delete"
                  ],
                  "properties": {
                    "$token": {
                      "type": "string",
                      "default": "YOUR_PROJECT_TOKEN"
                    },
                    "$distinct_id": {
                      "type": "string",
                      "default": "13793"
                    },
                    "$delete": {
                      "type": "string",
                      "nullable": true,
                      "default": "null"
                    },
                    "$ignore_alias": {
                      "type": "boolean",
                      "default": false
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
      },
      "JavascriptWithCallback": {
        "in": "query",
        "name": "callback",
        "required": false,
        "schema": {
          "type": "string"
        },
        "description": "If present, Mixpanel will return a `content-type: text/javascript` with a body that calls a function by value provided. This is useful for creating local callbacks to a successful track call in JavaScript."
      },
      "Strict": {
        "in": "query",
        "name": "strict",
        "required": false,
        "schema": {
          "$ref": "#/components/schemas/IntegerPropertyAsBooleanFlag",
          "description": "If present and equal to 1, Mixpanel will validate the provided records and return a JSON object with per-record error messages for records that fail validation."
        }
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