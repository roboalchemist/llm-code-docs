# Source: https://developer.mixpanel.com/reference/list-recent-events.md

# Aggregate Event Counts

Get unique, total, or average data for a set of events over N days, weeks, or months.
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
    "/events": {
      "get": {
        "operationId": "list-recent-events",
        "summary": "Aggregate Event Counts",
        "tags": [
          "Event Breakdown"
        ],
        "description": "Get unique, total, or average data for a set of events over N days, weeks, or months.\nThe Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          },
          {
            "in": "query",
            "name": "event",
            "schema": {
              "type": "string"
            },
            "description": "The event or events that you wish to get data for, encoded as a JSON array. Example format: \"[\"play song\", \"log in\", \"add playlist\"]\".",
            "required": true
          },
          {
            "$ref": "#/components/parameters/type"
          },
          {
            "$ref": "#/components/parameters/unit"
          },
          {
            "$ref": "#/components/parameters/interval"
          },
          {
            "$ref": "#/components/parameters/fromDate"
          },
          {
            "$ref": "#/components/parameters/toDate"
          },
          {
            "$ref": "#/components/parameters/format"
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
                          "2010-05-29",
                          "2010-05-30",
                          "2010-05-31"
                        ],
                        "values": {
                          "account-page": {
                            "2010-05-30": 1
                          },
                          "splash features": {
                            "2010-05-29": 6,
                            "2010-05-30": 4,
                            "2010-05-31": 5
                          }
                        }
                      },
                      "legend_size": 2
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
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "All dates included in `values`"
                          }
                        },
                        "values": {
                          "type": "object",
                          "additionalProperties": {
                            "type": "object",
                            "description": "A mapping of the date of each unit to the number of events. (ex. {\"2010-05-30\": 6})"
                          },
                          "description": "Keys are the names of events"
                        }
                      }
                    },
                    "legend_size": {
                      "type": "integer",
                      "description": "The number of events defined in `values`"
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
      "unit": {
        "in": "query",
        "name": "unit",
        "schema": {
          "type": "string",
          "enum": [
            "minute",
            "hour",
            "day",
            "week",
            "month"
          ]
        },
        "description": "This can be \"minute\", \"hour\", \"day\", \"week\", or \"month\". It determines the level of granularity of the data you get back. Note that you cannot get hourly uniques.",
        "required": true
      },
      "interval": {
        "in": "query",
        "name": "interval",
        "schema": {
          "type": "integer"
        },
        "description": "The number of \"units\" to return data for - minutes, hours, days, weeks, or months. 1 will return data for the current unit (minute, hour, day, week or month). 2 will return the current and previous units, and so on. Specify either interval or from_date and to_date."
      },
      "format": {
        "in": "query",
        "name": "format",
        "schema": {
          "type": "string",
          "enum": [
            "json",
            "csv"
          ]
        },
        "description": "The data return format, such as JSON or CSV. Options: \"json\" (default), \"csv\"."
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