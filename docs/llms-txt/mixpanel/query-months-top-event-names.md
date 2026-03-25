# Source: https://developer.mixpanel.com/reference/query-months-top-event-names.md

# Top Events

Get a list of the most common events over the last 31 days. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Query API",
    "description": "query api",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://{regionAndDomain}.com/api/query",
      "description": "Mixpanel's calculated data API",
      "variables": {
        "regionAndDomain": {
          "default": "mixpanel",
          "enum": [
            "mixpanel",
            "eu.mixpanel",
            "in.mixpanel"
          ],
          "description": "The server location to be used:\n  * `mixpanel` - The default (US) servers used for most projects\n  * `eu.mixpanel` - EU servers if you are enrolled in EU Data Residency\n  * `in.mixpanel` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "security": [
    {
      "ServiceAccount": []
    },
    {
      "ProjectSecret": []
    }
  ],
  "tags": [
    {
      "name": "Event Breakdown",
      "description": "Breakdowns on the most common events in your project"
    }
  ],
  "paths": {
    "/events/names": {
      "get": {
        "operationId": "query-months-top-event-names",
        "summary": "Top Events",
        "tags": [
          "Event Breakdown"
        ],
        "description": "Get a list of the most common events over the last 31 days. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          },
          {
            "$ref": "#/components/parameters/type"
          },
          {
            "$ref": "#/components/parameters/limit255"
          }
        ],
        "responses": {
          "200": {
            "description": "Success.",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": [
                      "battle",
                      "click signup button",
                      "View homepage"
                    ]
                  }
                },
                "schema": {
                  "type": "array",
                  "description": "List of names in descending alphabetical order.",
                  "items": {
                    "type": "string",
                    "description": "Event name",
                    "example": "Viewed page"
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      },
      "ProjectSecret": {
        "type": "http",
        "scheme": "basic",
        "description": "Project Secret"
      }
    },
    "parameters": {
      "workspaceId": {
        "in": "query",
        "name": "workspace_id",
        "schema": {
          "type": "integer"
        },
        "description": "The id of the workspace if applicable."
      },
      "type": {
        "in": "query",
        "name": "type",
        "schema": {
          "type": "string",
          "enum": [
            "general",
            "unique",
            "average"
          ]
        },
        "description": "The analysis type you would like to get data for - such as general, unique, or average events. Valid values: \"general\", \"unique\", or \"average\".",
        "required": true
      },
      "limit255": {
        "in": "query",
        "name": "limit",
        "schema": {
          "type": "integer"
        },
        "description": "The maximum number of values to return. Defaults to 255."
      },
      "projectId": {
        "in": "query",
        "name": "project_id",
        "schema": {
          "type": "integer"
        },
        "description": "Required if using service account to authenticate request.",
        "required": true
      }
    }
  },
  "x-readme-deploy-id": "query"
}
```