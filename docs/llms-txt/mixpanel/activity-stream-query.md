# Source: https://developer.mixpanel.com/reference/activity-stream-query.md

# Profile Event Activity

This endpoint returns the activity feed for specified users. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

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
      "name": "Activity Feed",
      "description": "See a profiles recent events history"
    }
  ],
  "paths": {
    "/stream/query": {
      "get": {
        "operationId": "activity-stream-query",
        "summary": "Profile Event Activity",
        "tags": [
          "Activity Feed"
        ],
        "description": "This endpoint returns the activity feed for specified users. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          },
          {
            "in": "query",
            "name": "distinct_ids",
            "schema": {
              "type": "string"
            },
            "description": "A JSON array as a string representing the `distinct_ids` to return activity feeds for. For example: `[\"12a34aa567eb8d-9ab1c26f345b67-89123c45-6aeaa7-89f12af345f678\"]`",
            "required": true
          },
          {
            "$ref": "#/components/parameters/fromDate"
          },
          {
            "$ref": "#/components/parameters/toDate"
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
                      "results": {
                        "events": [
                          {
                            "event": "Game Played",
                            "properties": {
                              "time": 1599589453,
                              "$distinct_id": "12a34aa567eb8d-9ab1c26f345b67-89123c45-6aeaa7-89f12af345f678",
                              "$browser": "Chrome",
                              "$city": "Austin",
                              "$region": "Texas",
                              "report_name": "insights"
                            }
                          },
                          {
                            "event": "Viewed Page",
                            "properties": {
                              "time": 1599589470,
                              "distinct_id": "12a34aa567eb8d-9ab1c26f345b67-89123c45-6aeaa7-89f12af345f678",
                              "$browser": "Chrome",
                              "$city": "Austin",
                              "$region": "Texas",
                              "report_name": "funnels"
                            }
                          }
                        ]
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
                    "results": {
                      "type": "object",
                      "properties": {
                        "events": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "event": {
                                "type": "string"
                              },
                              "properties": {
                                "type": "object"
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