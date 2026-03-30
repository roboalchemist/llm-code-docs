# Source: https://developer.mixpanel.com/reference/segmentation-sum-query.md

# Numerically Sum

Sums an expression for events per unit time. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

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
    "/segmentation/sum": {
      "get": {
        "operationId": "segmentation-sum-query",
        "summary": "Numerically Sum",
        "tags": [
          "Segmentation"
        ],
        "description": "Sums an expression for events per unit time. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
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
            "description": "The expression to sum per unit time. The result of the expression should be a numeric value. If the expression is not numeric, a value of 0.0 is assumed. See the [expressions section](https://developer.mixpanel.com/reference/segmentation-expressions) below.",
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
                      "status": "ok",
                      "computed_at": "2019-10-07T23:02:11.666218+00:00",
                      "results": {
                        "2019-10-07": 4,
                        "2019-10-06": 7
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string"
                    },
                    "computed_at": {
                      "type": "string"
                    },
                    "results": {
                      "type": "object",
                      "additionalProperties": {
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
    }
  },
  "x-readme-deploy-id": "query"
}
```