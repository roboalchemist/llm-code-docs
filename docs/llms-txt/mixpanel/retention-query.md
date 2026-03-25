# Source: https://developer.mixpanel.com/reference/retention-query.md

# Query Retention Report

Get cohort analysis.

If you specify neither an `interval` nor a `unit`, the `interval` is 1 day. This means that each user gets 24 hours in each interval to do the specified event.

An example response with a `born_event` of 'event integration' and `event` of 'viewed report' might look like this:

```json
{
  "2012-01-01": {
    "counts": [2, 1, 2],
    "first": 2
  },
  "2012-01-02": {
    "counts": [9, 7, 6],
    "first": 10
  },
  "2012-01-03": {
    "counts": [9, 6, 4],
    "first": 10
  }
}
```

These results indicate that on 2012-01-02, 10 users did the `born_event` ("event integration"), as indicated by the first field. If the `retention_type=compounded`, then first will instead indicate the number of users who did `event` ("viewed report") on the specified date. 9 of those users did `event` ("viewed report") within 24 hours (the "0th" interval) of doing the `born_event`. Seven of those did `event` between 24 and 48 hours (interval 1) of the `born_event`. These 7 are a subset of the initial 10, but not necessarily a subset of the 9 (retention is not a funnel; see the number increase between 72 and 96 hours). And finally, 6 users did `event` between 48 and 72 hours (interval 2) after the `born_event`.

In the Mixpanel retention UI, "First time" corresponds to `retention_type=birth`, and "Recurring" corresponds to `retention_type=compounded`.

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
    "/retention": {
      "get": {
        "operationId": "retention-query",
        "summary": "Query Retention Report",
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
            "name": "retention_type",
            "schema": {
              "type": "string",
              "enum": [
                "birth",
                "compounded"
              ],
              "example": "birth"
            },
            "description": "Must be either \"birth\" or \"compounded\". Defaults to \"birth\". The “birth” retention type corresponds to first time retention. The “compounded” retention type corresponds to recurring retention. See the [Types of Retention](https://help.mixpanel.com/hc/en-us/articles/360001370146) article for more information."
          },
          {
            "in": "query",
            "name": "born_event",
            "schema": {
              "type": "string",
              "example": "Added to cart"
            },
            "description": "The first event a user must do to be counted in a birth retention cohort. Required when retention_type is \"birth\"; ignored otherwise."
          },
          {
            "in": "query",
            "name": "event",
            "schema": {
              "type": "string",
              "example": "Viewed report"
            },
            "description": "The event to generate returning counts for. Applies to both birth and compounded retention. If not specified, we look across all events."
          },
          {
            "in": "query",
            "name": "born_where",
            "schema": {
              "type": "string",
              "example": "properties[\"$os\"]==\"Linux\""
            },
            "description": "An expression to filter born_events by. See the [expressions section](https://developer.mixpanel.com/reference/segmentation-expressions) above."
          },
          {
            "in": "query",
            "name": "where",
            "schema": {
              "type": "string",
              "example": "properties[\"$os\"]==\"Linux\""
            },
            "description": "An expression to filter born_events by. See the [expressions section](https://developer.mixpanel.com/reference/segmentation-expressions) above."
          },
          {
            "in": "query",
            "name": "interval",
            "schema": {
              "type": "integer",
              "example": 1
            },
            "description": "The number of units (can be specified in either days, weeks, or months) that you want per individual bucketed interval. May not be greater than 90 days if days is the specified unit. The default value is 1."
          },
          {
            "in": "query",
            "name": "interval_count",
            "schema": {
              "type": "integer",
              "example": 1
            },
            "description": "The number of individual buckets, or intervals, that are returned; defaults to 1. Note that we include a \"0th\" interval for events that take place less than one interval after the initial event."
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
              ],
              "example": "day"
            },
            "description": "The interval unit. It can be \"day\", \"week\", or \"month\". Default is \"day\"."
          },
          {
            "in": "query",
            "name": "unbounded_retention",
            "schema": {
              "type": "boolean",
              "default": false,
              "example": false
            },
            "description": "A counting method for retention queries where retention values accumulate from right to left, i.e. day N is equal to users who retained on day N and any day after. The default value of false does not perform this accumulation. [Learn more about Counting Method](https://help.mixpanel.com/hc/en-us/articles/360045484191)."
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
                      "2012-01-01": {
                        "counts": [
                          2,
                          1,
                          2
                        ],
                        "first": 2
                      },
                      "2012-01-02": {
                        "counts": [
                          9,
                          7,
                          6
                        ],
                        "first": 10
                      },
                      "2012-01-03": {
                        "counts": [
                          9,
                          6,
                          4
                        ],
                        "first": 10
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "additionalProperties": {
                    "type": "object",
                    "properties": {
                      "counts": {
                        "type": "array",
                        "items": {
                          "type": "integer"
                        }
                      },
                      "first": {
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