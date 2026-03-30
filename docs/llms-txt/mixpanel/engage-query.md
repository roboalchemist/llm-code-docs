# Source: https://developer.mixpanel.com/reference/engage-query.md

# Query Profiles

Query user (or group) profile data and return list of users (or groups) that fit specified parameters.

API responses will return at most `page_size` records for each request. To request additional records, callers should repeat their call to the API using the same `where` param, but provide a `session_id` parameter with a value taken from the first response, and include a `page` parameter with a value one greater than the value of page in the response.

A caller trying to retrieve all of the records for a particular query might use an algorithm something like this:

```javascript
// Get the first page of data associated with our selector expression
this_page = query_api(where=YOUR_SELECTOR_EXPRESSION)
do_something_with_response(this_page)

// If we get fewer records than the page_size returned with our results,
// then there are no more records to get. Otherwise, keep querying for additional pages.
while (length of this_page.results) >= this_page.page_size:
    next_page_number = this_page.page + 1
    this_page = query_api(where=YOUR_SELECTOR_EXPRESSION, session_id=this_page.session_id, page=next_page_number)
    do_something_with_response(this_page)
```

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
      "name": "Engage",
      "description": "Query for profile information"
    }
  ],
  "paths": {
    "/engage": {
      "post": {
        "operationId": "engage-query",
        "summary": "Query Profiles",
        "tags": [
          "Engage"
        ],
        "description": "",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          }
        ],
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "properties": {
                  "distinct_id": {
                    "type": "string",
                    "description": "A unique identifier used to distinguish an individual profile."
                  },
                  "distinct_ids": {
                    "type": "string",
                    "description": "A JSON array of distinct_ids to retrieve profiles for.\nExample: `distinct_ids=[\"id1\", \"id2\"]`\n"
                  },
                  "data_group_id": {
                    "type": "string",
                    "description": "The ID of the group key, used when querying group profiles, click [here](https://docs.mixpanel.com/docs/data-structure/group-analytics#exporting-group-profiles-via-api) for more info."
                  },
                  "where": {
                    "type": "string",
                    "description": "An expression to filter users (or groups) by. See the [expressions section](https://developer.mixpanel.com/reference/segmentation-expressions) above."
                  },
                  "output_properties": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "A JSON array of names of properties you want returned.\nExample: `output_properties=[\"$last_name\", \"$email\", \"Total Spent\"]`\n\nThis parameter can drastically reduce the amount of data returned by the API when you're not interested in all properties and can speed up queries significantly.\n"
                  },
                  "session_id": {
                    "type": "string",
                    "description": "A string id provided in the results of a previous query. Using a session_id speeds up api response, and allows paging through results."
                  },
                  "page": {
                    "type": "integer",
                    "description": "Which page of the results to retrieve. Pages start at zero. If the \"page\" parameter is provided and above 0, the session_id parameter must also be provided."
                  },
                  "behaviors": {
                    "type": "integer",
                    "description": "If you are exporting user profiles using an event selector, you use a `behaviors` parameter in your request. `behaviors` and `filter_by_cohort` are mutually exclusive."
                  },
                  "as_of_timestamp": {
                    "type": "integer",
                    "description": "This parameter is only useful when also using `behaviors`.\nIf you try to export more than 1k profiles using a `behaviors` parameter and you don't included the parameter `as_of_timestamp`, you'll see the following error:\n\n`request for page in uncached query for params`\n"
                  },
                  "filter_by_cohort": {
                    "type": "string",
                    "description": "Takes a JSON object with a single key called `id` whose value is the cohort ID. `behaviors` and `filter_by_cohort` are mutually exclusive.\n\nExample: `filter_by_cohort='{\"id\":12345}'`\n"
                  },
                  "include_all_users": {
                    "type": "boolean",
                    "description": "*\\*only applicable with `filter_by_cohort` parameter*\n\n`include_all_users=true` (default) include all distinct_ids even if they don’t have a user (or group) profile.\n\n`include_all_users=false` include only distinct_ids with user (or group) profile.\n"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success.",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": {
                      "page": 0,
                      "page_size": 1000,
                      "results": [
                        {
                          "$distinct_id": 4,
                          "$properties": {
                            "$created": "2008-12-12T11:20:47",
                            "$email": "example@mixpanel.com",
                            "$first_name": "Example",
                            "$last_name": "Name",
                            "$last_seen": "2008-06-09T23:08:40"
                          }
                        }
                      ],
                      "session_id": "1234567890-EXAMPL",
                      "status": "ok",
                      "total": 1
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "page": {
                      "type": "integer",
                      "description": "The page number of the results"
                    },
                    "page_size": {
                      "type": "integer",
                      "description": "The max number of results in a single page."
                    },
                    "session_id": {
                      "type": "string"
                    },
                    "status": {
                      "type": "string",
                      "description": "Indicates whether the request was successful"
                    },
                    "total": {
                      "type": "integer",
                      "description": "The number of users in the results payload."
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "$distinct_id": {
                            "type": "integer",
                            "description": "The ID of the user"
                          },
                          "$properties": {
                            "type": "object",
                            "description": "The properties associated with the user"
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
      }
    }
  },
  "x-readme-deploy-id": "query"
}
```