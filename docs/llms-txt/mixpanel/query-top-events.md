# Source: https://developer.mixpanel.com/reference/query-top-events.md

# Today's Top Events

Get the top events for today, with their counts and the normalized percent change from yesterday.
The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

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
    "/events/top": {
      "get": {
        "operationId": "query-top-events",
        "summary": "Today's Top Events",
        "tags": [
          "Event Breakdown"
        ],
        "description": "Get the top events for today, with their counts and the normalized percent change from yesterday.\nThe Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
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
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer"
            },
            "description": "The maximum number of events to return. Defaults to 100."
          }
        ],
        "responses": {
          "200": {
            "description": "Success.",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": {
                      "events": [
                        {
                          "amount": 2,
                          "event": "funnel",
                          "percent_change": -0.35635745999582824
                        },
                        {
                          "amount": 75,
                          "event": "pages",
                          "percent_change": -0.20209602478821687
                        },
                        {
                          "amount": 2,
                          "event": "projects",
                          "percent_change": 1
                        }
                      ],
                      "type": "unique"
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "events": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "amount": {
                            "type": "integer",
                            "description": "Number of events"
                          },
                          "event": {
                            "type": "string",
                            "description": "The name of the event"
                          },
                          "percent_change": {
                            "type": "number",
                            "format": "float",
                            "description": "The percent change from yesterday"
                          }
                        }
                      }
                    },
                    "type": {
                      "type": "string"
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