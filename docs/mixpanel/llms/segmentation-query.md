# Source: https://developer.mixpanel.com/reference/segmentation-query.md

# Query Segmentation Report

Get data for an event, segmented and filtered by properties. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

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
      "name": "Segmentation",
      "description": "Query data shown in your Segmenation reports"
    }
  ],
  "paths": {
    "/segmentation": {
      "get": {
        "operationId": "segmentation-query",
        "summary": "Query Segmentation Report",
        "tags": [
          "Segmentation"
        ],
        "description": "Get data for an event, segmented and filtered by properties. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          },
          {
            "$ref": "#/components/parameters/eventName"
          },
          {
            "$ref": "#/components/parameters/fromDate"
          },
          {
            "$ref": "#/components/parameters/toDate"
          },
          {
            "$ref": "#/components/parameters/on"
          },
          {
            "in": "query",
            "name": "unit",
            "schema": {
              "type": "string",
              "enum": [
                "minute",
                "hour",
                "day",
                "month"
              ]
            },
            "description": "This can be \"minute\", \"hour\", \"day\", or \"month\". This determines the buckets into which the property values that you segment on are placed. The default value is \"day\"."
          },
          {
            "in": "query",
            "name": "interval",
            "schema": {
              "type": "integer"
            },
            "description": "Optional parameter in lieu of 'unit' when 'type' is not 'general'. Determines the number of days your results are bucketed into can be used with or without 'from_date' and 'to_date' parameters."
          },
          {
            "$ref": "#/components/parameters/where"
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer"
            },
            "description": "Return the top property values. Defaults to 60. Maximum value 10,000. This parameter does nothing if \"on\" is not specified."
          },
          {
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
            "description": "This can be \"general\", \"unique\", or \"average\". If this is set to \"unique\", we return the unique count of events or property values. If set to \"general\", we return the total, including repeats. If set to \"average\", we return the average count. The default value is \"general\"."
          },
          {
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "csv"
              ],
              "description": "Can be set to \"csv\"."
            }
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
                        "series": [
                          "2011-08-08",
                          "2011-08-09",
                          "2011-08-06",
                          "2011-08-07"
                        ],
                        "values": {
                          "Signed up": {
                            "2011-08-06": 147,
                            "2011-08-07": 146,
                            "2011-08-08": 776,
                            "2011-08-09": 1376
                          }
                        }
                      },
                      "legend_size": 1
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "series": {
                          "$ref": "#/components/schemas/series"
                        },
                        "values": {
                          "type": "object",
                          "additionalProperties": {
                            "description": "A mapping of the date to the number of specified events that took place. (ex. {\"2010-05-30\": 6})"
                          }
                        }
                      }
                    },
                    "legend_size": {
                      "type": "integer",
                      "description": "List of all dates."
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
      "on": {
        "in": "query",
        "name": "on",
        "schema": {
          "type": "string"
        },
        "description": "The property expression to segment the event on. See the [expression to segment](https://developer.mixpanel.com/reference/segmentation-expressions) below."
      },
      "where": {
        "in": "query",
        "name": "where",
        "schema": {
          "type": "string"
        },
        "description": "An expression to filter events by. See the [expression to segment](https://developer.mixpanel.com/reference/segmentation-expressions) below."
      },
      "eventName": {
        "in": "query",
        "name": "event",
        "schema": {
          "type": "string"
        },
        "description": "The event that you wish to get data for. Note: this is a single event name, not an array.",
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
    },
    "schemas": {
      "series": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "All dates we have data for in the response."
        }
      }
    }
  },
  "x-readme-deploy-id": "query"
}
```