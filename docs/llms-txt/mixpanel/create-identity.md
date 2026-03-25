# Source: https://developer.mixpanel.com/reference/create-identity.md

# Create Identity

<Callout icon="📘" theme="info">
  The `$identify` event payload is only useful for projects using the Original ID Merge system; it has no functionality in other ID management systems. Please review [this section of our documentation](https://docs.mixpanel.com/docs/tracking-methods/id-management#identity-merge-apis) for more information.
</Callout>

<Callout icon="📘" theme="info">
  You can also use the import endpoint: [https://api.mixpanel.com/import/](https://api.mixpanel.com/import/)
</Callout>

```sh
curl --request POST \
     --url 'https://api.mixpanel.com/track#create-identity' \
     --header 'accept: text/plain' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data 'data={
      "event": "$identify",
      "properties": {
          "$identified_id": "YOUR_CHOSEN_USER_ID",
          "$anon_id": "ORIGINAL_ANON_ID",
          "token": "YOUR_PROJECT_TOKEN"
      }
}
'
```

**Identify Criteria:**
![](https://files.readme.io/d0066f0-ID_management_identify_3-HTTP.png)

**Required[Event Object](https://docs.mixpanel.com/docs/tracking/reference/data-model#anatomy-of-an-event) attributes**

| Event Object property          | Type                                                                                                        | Description                                                                                                                                                                                         |
| :----------------------------- | :---------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **event**                      | <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "red" }}>required</span>   | value must be: `$identify`                                                                                                                                                                          |
| **properties**                 | <span style={{ fontFamily: "courier" }}>Object</span><br /><span style={{ color: "red" }}>required</span>   |                                                                                                                                                                                                     |
| **properties.distinct\_id**    | <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "green" }}>optional</span> | The distinct ID post-identification (same as $identified\_id - it will be inferred from $identified\_id if not included)                                                                            |
| **properties.$identified\_id** | <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "red" }}>required</span>   | A distinct\_id to merge with the $anon\_id.                                                                                                                                                         |
| **properties.$anon\_id**       | <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "red" }}>required</span>   | A distinct\_id to merge with the $identified\_id. The $anon\_id must be [UUID v4](https://en.wikipedia.org/wiki/Universally_unique_identifier) format and not already merged to an $identified\_id. |
| **properties.token**           | <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "red" }}>required</span>   | The project token.                                                                                                                                                                                  |

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Identity API",
    "description": "APIs to identify anonymous user IDs to their canonical user ID.",
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
      "name": "Identities",
      "description": "Register or merge users with a new identity."
    }
  ],
  "paths": {
    "/track#create-identity": {
      "post": {
        "tags": [
          "Identities"
        ],
        "summary": "Create Identity",
        "operationId": "create-identity",
        "description": "",
        "security": [
          {}
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "allOf": [
                  {
                    "type": "object",
                    "required": [
                      "data"
                    ],
                    "properties": {
                      "data": {
                        "type": "string",
                        "format": "blob",
                        "description": "A JSON object with the required Event Object fields and any additional event properties.",
                        "default": "{\n      \"event\": \"$identify\",\n      \"properties\": {\n          \"$identified_id\": \"ORIGINAL_ID\",\n          \"$anon_id\": \"NEW_ID\",\n          \"token\": \"YOUR_PROJECT_TOKEN\"\n      }\n}\n"
                      }
                    }
                  },
                  {
                    "$ref": "#/components/schemas/ImportRequestParameters"
                  }
                ]
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
      "ImportRequestParameters": {
        "allOf": [
          {
            "$ref": "#/components/schemas/Strict"
          }
        ]
      },
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
      },
      "Strict": {
        "type": "object",
        "properties": {
          "strict": {
            "allOf": [
              {
                "$ref": "#/components/schemas/IntegerPropertyAsBooleanFlag"
              },
              {
                "description": "If present and equal to 1, Mixpanel will validate the provided records and return a JSON object with per-record error messages for records that fail validation."
              }
            ]
          }
        }
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
        "description": "\n* `1` - All data objects provided are valid. This does not signify a valid project token or secret.\n* `0` - One or more data objects in the body are invalid.\n"
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
    }
  },
  "x-readme-deploy-id": "identity",
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