# Source: https://developer.mixpanel.com/reference/profile-set.md

# Set Property

Takes a JSON object containing names and values of profile properties. If the profile does not exist, it creates it with these properties. If it does exist, it sets the properties to these values, overwriting existing values.

<Callout icon="📘" theme="info">
  This API will return a `200 OK` even if there are data validation issues. To ensure the request actually succeeded, you need to check the response body.
</Callout>

<Callout icon="📘" theme="info">
  This API does not support gzip encoding.
</Callout>

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
    "/engage#profile-set": {
      "post": {
        "operationId": "profile-set",
        "tags": [
          "User Profiles"
        ],
        "summary": "Set Property",
        "description": "Takes a JSON object containing names and values of profile properties. If the profile does not exist, it creates it with these properties. If it does exist, it sets the properties to these values, overwriting existing values.",
        "security": [
          {}
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/IP"
          },
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
                  "description": "A JSON update object, with a $token, $distinct_id, and $set operation object.",
                  "required": [
                    "$token",
                    "$distinct_id",
                    "$set"
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
                    "$set": {
                      "type": "object"
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
      "IP": {
        "in": "query",
        "name": "ip",
        "required": false,
        "schema": {
          "$ref": "#/components/schemas/IntegerPropertyAsBooleanFlag",
          "default": 0,
          "description": "If present and equal to 0, Mixpanel will not perform geolocation parsing using the IP address of the request. We recommend setting the ip to \"0\" when making requests from the server-side to prevent the unintentional effect of overwriting your profile's geolocation with your server location. Defaults to 1 which would use the IP address of the request to update profile geolocation."
        }
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