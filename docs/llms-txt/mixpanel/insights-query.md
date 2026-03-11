# Source: https://developer.mixpanel.com/reference/insights-query.md

# Query Saved Report

Get data from your Insights reports. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

# OpenAPI definition

````json
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
      "name": "Insights",
      "description": "Query data shown in your Insights reports"
    }
  ],
  "paths": {
    "/insights": {
      "get": {
        "operationId": "insights-query",
        "summary": "Query Saved Report",
        "tags": [
          "Insights"
        ],
        "description": "Get data from your Insights reports. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          },
          {
            "in": "query",
            "name": "bookmark_id",
            "schema": {
              "type": "integer"
            },
            "description": "The ID of your Insights report can be found from the url: `https://mixpanel.com/project/<YOUR_PROJECT_ID>/view/<YOUR_WORKSPACE_ID>/app/boards#id=12345&editor-card-id=%22report-<YOUR_BOOKMARK_ID>%22`",
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": {
                      "computed_at": "2020-09-21T16:35:41.252314+00:00",
                      "date_range": {
                        "from_date": "2020-08-31T00:00:00-07:00",
                        "to_date": "2020-09-12T23:59:59.999000-07:00"
                      },
                      "headers": [
                        "$event"
                      ],
                      "series": {
                        "Logged in": {
                          "2020-08-31T00:00:00-07:00": 9852,
                          "2020-09-07T00:00:00-07:00": 4325
                        },
                        "Viewed page": {
                          "2020-08-31T00:00:00-07:00": 10246,
                          "2020-09-07T00:00:00-07:00": 11432
                        }
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "computed_at": {
                      "type": "string"
                    },
                    "date_range": {
                      "type": "object",
                      "properties": {
                        "from_date": {
                          "type": "string"
                        },
                        "to_date": {
                          "type": "string"
                        }
                      }
                    },
                    "headers": {
                      "type": "array",
                      "description": "Explanation of what the nested keys mean in `series`.",
                      "items": {
                        "type": "string"
                      }
                    },
                    "series": {
                      "type": "object",
                      "description": "Maps event name of event to an object with dates as keys and number of instances as values. For example:\n\n```json\n{\n  'Viewed page': {\n    '2020-08-17T00:00:00-07:00': 7832,\n    '2020-08-24T00:00:00-07:00': 6234,\n  }\n}\n```\n"
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
````