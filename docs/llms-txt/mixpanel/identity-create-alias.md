# Source: https://developer.mixpanel.com/reference/identity-create-alias.md

# Create Alias

<Callout icon="📘" theme="info">
  The `$create_alias` event payload is only useful for projects using the Original ID Merge system and the Legacy ID Management System; it has no functionality in the Simplified ID Merge system. Please review [this section of our documentation](https://docs.mixpanel.com/docs/tracking-methods/id-management#identity-merge-apis) for more information.
</Callout>

<Callout icon="📘" theme="info">
  You can also use the import endpoint: [https://api.mixpanel.com/import/](https://api.mixpanel.com/import/)
</Callout>

Mixpanel supports adding an alias to a distinct id. An alias is a new value that will be interpreted by Mixpanel as an existing value. That means that you can send messages to Mixpanel using the new value, and Mixpanel will continue to use the old value for calculating funnels and retention reports, or applying updates to user profiles.

**Alias Criteria:**

<Image alt="960" border={false} src="https://files.readme.io/d16f1d3-ID_management_alias_3-HTTP.png" title="Identity Management - Alias" />

**Required[Event Object](https://docs.mixpanel.com/docs/tracking/reference/data-model#anatomy-of-an-event) attributes**

<table>
  <thead>
    <tr>
      <th>Event Object property</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**event**</td>

      <td>
        <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "red" }}>required</span>
      </td>

      <td>value must be: <br />`$create_alias`</td>
    </tr>

    <tr>
      <td>**properties**</td>

      <td>
        <span style={{ fontFamily: "courier" }}>Object</span><br /><span style={{ color: "red" }}>required</span>
      </td>

      <td />
    </tr>

    <tr>
      <td>**properties.distinct\_id**</td>

      <td>
        <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "red" }}>required</span>
      </td>

      <td>A distinct\_id to be merged with the alias.</td>
    </tr>

    <tr>
      <td>**properties.alias**</td>

      <td>
        <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "red" }}>required</span>
      </td>

      <td>A new distinct\_id to be merged with the original distinct\_id. Each alias can only map to one distinct\_id.</td>
    </tr>

    <tr>
      <td>**properties.token**</td>

      <td>
        <span style={{ fontFamily: "courier" }}>String</span><br /><span style={{ color: "red" }}>required</span>
      </td>

      <td>The project token.</td>
    </tr>
  </tbody>
</table>

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
    "/track#identity-create-alias": {
      "post": {
        "tags": [
          "Identities"
        ],
        "summary": "Create Alias",
        "operationId": "identity-create-alias",
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
                        "default": "{\n    \"event\": \"$create_alias\",\n    \"properties\": {\n        \"distinct_id\": \"other_distinct_id\",\n        \"alias\": \"your_id\",\n        \"token\": \"YOUR_PROJECT_TOKEN\"\n    }\n}\n"
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