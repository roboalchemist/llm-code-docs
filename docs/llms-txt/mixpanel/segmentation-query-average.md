# Source: https://developer.mixpanel.com/reference/segmentation-query-average.md

# Numerically Average

Averages an expression for events per unit time. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

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
    "/segmentation/average": {
      "get": {
        "operationId": "segmentation-query-average",
        "summary": "Numerically Average",
        "tags": [
          "Segmentation"
        ],
        "description": "Averages an expression for events per unit time. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
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
            "description": "Success",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": {
                      "results": {
                        "2011-08-06": 8.64705882352939,
                        "2011-08-07": 4.640625,
                        "2011-08-08": 3.6230899830221,
                        "2011-08-09": 7.3353658536585
                      },
                      "status": "ok"
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "results": {
                      "type": "object",
                      "additionalProperties": {
                        "type": "number",
                        "format": "float"
                      }
                    },
                    "status": {
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