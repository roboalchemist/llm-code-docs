# Source: https://developer.mixpanel.com/reference/segmentation-numeric-query.md

# Numerically Bucket

Get data for an event, segmented and filtered by properties, with values placed into numeric buckets.
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
      "name": "Segmentation",
      "description": "Query data shown in your Segmenation reports"
    }
  ],
  "paths": {
    "/segmentation/numeric": {
      "get": {
        "operationId": "segmentation-numeric-query",
        "summary": "Numerically Bucket",
        "tags": [
          "Segmentation"
        ],
        "description": "Get data for an event, segmented and filtered by properties, with values placed into numeric buckets.\nThe Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
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
            "in": "query",
            "name": "on",
            "schema": {
              "type": "string"
            },
            "description": "The property expression to segment the event on. This expression must be a numeric property. See the [expressions section](https://developer.mixpanel.com/reference/segmentation-expressions) below.",
            "required": true
          },
          {
            "in": "query",
            "name": "unit",
            "schema": {
              "type": "string",
              "enum": [
                "hour",
                "day"
              ]
            },
            "description": "This can be \"hour\" or \"day\". This determines the buckets into which the property values that you segment on are placed. The default value is \"day\"."
          },
          {
            "$ref": "#/components/parameters/where"
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
            "description": "This can be \"hour\" or \"day\". This determines the buckets into which the property values that you segment on are placed. The default value is \"day\"."
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
                      "data": {
                        "series": [
                          "2011-08-08",
                          "2011-08-09",
                          "2011-08-06",
                          "2011-08-07"
                        ],
                        "values": {
                          "2,000 - 2,100": {
                            "2011-08-06": 1,
                            "2011-08-07": 5,
                            "2011-08-08": 4,
                            "2011-08-09": 15
                          },
                          "2,100 - 2,200": {
                            "2011-08-07": 2,
                            "2011-08-08": 7,
                            "2011-08-09": 15
                          },
                          "2,200 - 2,300": {
                            "2011-08-06": 1,
                            "2011-08-08": 6,
                            "2011-08-09": 5
                          },
                          "2,300 - 2,400": {
                            "2011-08-06": 4,
                            "2011-08-08": 1,
                            "2011-08-09": 12
                          },
                          "2,400 - 2,500": {
                            "2011-08-08": 2,
                            "2011-08-09": 5
                          }
                        }
                      },
                      "legend_size": 5
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
                            "type": "object",
                            "description": "The range of the bucket",
                            "additionalProperties": {
                              "type": "integer",
                              "description": "A mapping of the date of each unit to the number of specified events that took place. (ex. {\"2010-05-30\": 6})"
                            }
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