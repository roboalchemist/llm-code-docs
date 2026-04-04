# Source: https://developer.mixpanel.com/reference/cohorts-list.md

# List Saved Cohorts

The list endpoint returns all of the cohorts in a given project. The JSON formatted return contains the cohort name, id, count, description, creation date, and visibility for every cohort in the project.

If you're trying to get a list of users in a cohort, you can use the [`/engage` endpoint with the `filter_by_cohort` parameter](ref:engage#engage-query).
The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.


The list endpoint returns all of the cohorts in a given project. The JSON formatted return contains the cohort name, id, count, description, creation date, and visibility for every cohort in the project.

If you're trying to get a list of users in a cohort, you can use the [`/engage` endpoint with the `filter_by_cohort` parameter](https://developer.mixpanel.com/reference/engage#engage-query).

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
      "name": "Cohorts",
      "description": "Understand what defines a cohort and how many profiles qualify"
    }
  ],
  "paths": {
    "/cohorts/list": {
      "post": {
        "operationId": "cohorts-list",
        "summary": "List Saved Cohorts",
        "tags": [
          "Cohorts"
        ],
        "description": "The list endpoint returns all of the cohorts in a given project. The JSON formatted return contains the cohort name, id, count, description, creation date, and visibility for every cohort in the project.\n\nIf you're trying to get a list of users in a cohort, you can use the [`/engage` endpoint with the `filter_by_cohort` parameter](https://developer.mixpanel.com/reference/engage#engage-query).\nThe Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.\n",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          }
        ],
        "responses": {
          "200": {
            "description": "Success.",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": [
                      {
                        "count": 150,
                        "is_visible": 1,
                        "description": "This cohort is visible, has an id = 1000, and currently has 150 users.",
                        "created": "2019-03-19 23:49:51",
                        "project_id": 1,
                        "id": 1000,
                        "name": "Cohort One"
                      },
                      {
                        "count": 25,
                        "is_visible": 0,
                        "description": "This cohort isn't visible, has an id = 2000, and currently has 25 users.",
                        "created": "2019-04-02 23:22:01",
                        "project_id": 1,
                        "id": 2000,
                        "name": "Cohort Two"
                      }
                    ]
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "count": {
                        "type": "integer"
                      },
                      "is_visible": {
                        "type": "integer",
                        "description": "0 if not visible. 1 if visible"
                      },
                      "description": {
                        "type": "string"
                      },
                      "created": {
                        "type": "string"
                      },
                      "project_id": {
                        "type": "integer"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "name": {
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
```