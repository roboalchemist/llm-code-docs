# Source: https://developer.mixpanel.com/reference/retention-frequency-query.md

# Query Frequency Report

Get data about how frequently users are performing events.

Let's breakdown an example response. If you specify `day` as "unit" and `hour` as "addiction\_unit", you will get a response that looks like this:

```json
{
  "2012-01-01": [
    305, 107, 60, 41, 32, 20, 12, 7, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1,
    1, 1
  ],
  "2012-01-02": [
    495, 204, 117, 77, 53, 36, 26, 20, 12, 7, 4, 3, 3, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0
  ],
  "2012-01-03": [
    671, 324, 176, 122, 81, 63, 48, 31, 21, 14, 9, 5, 3, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 0, 0
  ]
}
```

One day's worth of data is shown for each date, split into hours. On 2012-01-02, 495 users did the event `Viewed report` during at least 1 hour out of the next 24 hour period (the period specified by `unit`). 204 users did the event during at least 2 hours. 117 users did the event during at least 3 hours.

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
      "name": "Retention",
      "description": "Query data shown in your Retention reports"
    }
  ],
  "paths": {
    "/retention/addiction": {
      "get": {
        "operationId": "retention-frequency-query",
        "summary": "Query Frequency Report",
        "tags": [
          "Retention"
        ],
        "description": "",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          },
          {
            "$ref": "#/components/parameters/fromDate"
          },
          {
            "$ref": "#/components/parameters/toDate"
          },
          {
            "in": "query",
            "name": "unit",
            "schema": {
              "type": "string",
              "enum": [
                "day",
                "week",
                "month"
              ]
            },
            "description": "The overall time period to return frequency of actions for can be \"day\", \"week\", or \"month\".",
            "required": true
          },
          {
            "in": "query",
            "name": "addiction_unit",
            "schema": {
              "type": "string",
              "enum": [
                "hour",
                "day"
              ]
            },
            "description": "The granularity to return frequency of actions at can be \"hour\" or \"day\".",
            "required": true
          },
          {
            "in": "query",
            "name": "event",
            "schema": {
              "type": "string"
            },
            "description": "The event to generate returning counts for."
          },
          {
            "in": "query",
            "name": "where",
            "schema": {
              "type": "string"
            },
            "description": "An expression to filter the returning events by. See the [expressions section](https://developer.mixpanel.com/reference/segmentation-expressions) above."
          },
          {
            "$ref": "#/components/parameters/retentionOn"
          },
          {
            "$ref": "#/components/parameters/retentionLimit"
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
                      "data": {
                        "2012-01-01": [
                          305,
                          107,
                          60,
                          41,
                          32,
                          20,
                          12,
                          7,
                          4,
                          3,
                          3,
                          3,
                          2,
                          2,
                          2,
                          1,
                          1,
                          1,
                          1,
                          1,
                          1,
                          1,
                          1,
                          1
                        ],
                        "2012-01-02": [
                          495,
                          204,
                          117,
                          77,
                          53,
                          36,
                          26,
                          20,
                          12,
                          7,
                          4,
                          3,
                          3,
                          1,
                          1,
                          1,
                          1,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0
                        ]
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "additionalProperties": {
                        "type": "array",
                        "items": {
                          "type": "integer"
                        }
                      }
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
      "retentionOn": {
        "in": "query",
        "name": "on",
        "schema": {
          "type": "string"
        },
        "description": "The property expression to segment the second event on. See the [expressions section](https://developer.mixpanel.com/reference/segmentation-expressions) above."
      },
      "retentionLimit": {
        "in": "query",
        "name": "limit",
        "schema": {
          "type": "integer"
        },
        "description": "Return the top limit segmentation values. This parameter does nothing if \"on\" is not specified."
      },
      "projectId": {
        "in": "query",
        "name": "project_id",
        "schema": {
          "type": "integer"
        },
        "description": "Required if using service account to authenticate request.",
        "required": true
      },
      "fromDate": {
        "in": "query",
        "name": "from_date",
        "schema": {
          "type": "string"
        },
        "description": "The date in yyyy-mm-dd format to begin querying from. This date is inclusive.",
        "required": true
      },
      "toDate": {
        "in": "query",
        "name": "to_date",
        "schema": {
          "type": "string"
        },
        "description": "The date in yyyy-mm-dd format to query to. This date is inclusive.",
        "required": true
      }
    }
  },
  "x-readme-deploy-id": "query"
}
```