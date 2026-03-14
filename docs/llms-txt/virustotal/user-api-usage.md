# Source: https://virustotal.readme.io/reference/user-api-usage.md

# Get a user’s API usage

This endpoint retrieves information about a the API usage, broken down by endpoint, of an user in a specific range of days (last 30 days by default).\
The period of time can be delimited by the two query parameters **start\_date** and **end\_date**, being the first and last day when API usage data will be retrieved, respectively.\
The data available includes only the last 60 natural days.

> 🚧 Time range restrictions
>
> The maximum range of time allowed by this endpoint is 30 days. If a greater range of time is specified, this endpoint will return an error message as response.

The user can be retrieved either by user ID or by API key, but the latter only works if the requester is the user himself or an administrator of a group the user belongs to.

```json Example response
{
    "daily": {
        "2019-10-23": {
            "/api/v3/(file_behaviours)": 1,
            "/api/v3/(file_graphs)": 1,
            "/api/v3/(file_relationships)": 20,
            "/api/v3/(intelligence_search)": 3
        },
        "2019-10-24": {
            "/api/v3/(intelligence_search)": 2
        },
        "2019-10-25": {
            "/api/v3/(intelligence_search)": 3
        },
        "2019-10-28": {
            "/api/v3/(intelligence_search)": 2
        },
        "2019-10-31": {
            "/api/v3/(domain_comments)": 9,
            "/api/v3/(domain_graphs)": 9,
            "/api/v3/(domain_relationships)": 90,
            "/api/v3/(intelligence_search)": 30,
            "/api/v3/(ip_addresses)": 2,
            "/api/v3/(ip_addresses_graphs)": 4,
            "/api/v3/(ip_addresses_relationships)": 28
        },
        "2019-11-04": {
            "/api/v3/(file_behaviours)": 2,
            "/api/v3/(file_graphs)": 2,
            "/api/v3/(file_relationships)": 40,
            "/api/v3/(intelligence_search)": 4
        },
        "2019-11-05": {
            "/api/v3/(graphs)": 1,
            "/api/v3/(intelligence_search)": 1
        },
        "2019-11-06": {
            "/api/v3/(domains)": 14,
            "/api/v3/(file_relationships)": 11,
            "/api/v3/(ip_addresses)": 10,
            "/api/v3/(urls)": 10
        },
        "2019-11-08": {
            "/api/v3/(intelligence_search)": 4,
            "/api/v3/(url_graphs)": 3,
            "/api/v3/(url_relationships)": 12,
            "/api/v3/(urls)": 9
        },
        "2019-11-09": {
            "/api/v3/(intelligence_search)": 13
        },
        "2019-11-12": {
            "/api/v3/(file_behaviours)": 16,
            "/api/v3/(file_graphs)": 15,
            "/api/v3/(file_relationships)": 314,
            "/api/v3/(intelligence_search)": 3,
            "/api/v3/(retrohunt_jobs)": 1
        },
        "2019-11-13": {
            "/api/v3/(file_behaviours)": 1,
            "/api/v3/(file_graphs)": 1,
            "/api/v3/(file_relationships)": 20,
            "/api/v3/(intelligence_search)": 1
        },
        "2019-11-18": {
            "/api/v3/(file_behaviours)": 10,
            "/api/v3/(file_graphs)": 10,
            "/api/v3/(file_relationships)": 215,
            "/api/v3/(intelligence_search)": 7
        },
        "2019-11-19": {
            "/api/v3/(domain_graphs)": 1,
            "/api/v3/(domain_relationships)": 10,
            "/api/v3/(file_behaviours)": 9,
            "/api/v3/(file_graphs)": 9,
            "/api/v3/(file_relationships)": 180,
            "/api/v3/(intelligence_search)": 11
        },
        "2019-11-20": {
            "/api/v3/(file_behaviours)": 5,
            "/api/v3/(file_graphs)": 5,
            "/api/v3/(file_relationships)": 100,
            "/api/v3/(intelligence_search)": 16
        },
        "2019-11-21": {
            "/api/v3/(intelligence_search)": 8,
            "/api/v3/(url_graphs)": 9,
            "/api/v3/(url_relationships)": 36,
            "/api/v3/(urls)": 24
        }
    },
    "daily_endpoints_not_consuming_quota": {
        "2019-10-22": {
            "/api/v3/(search)": 1
        },
        "2019-10-23": {
            "/api/v3/(file_comments)": 1,
            "/api/v3/(files)": 3,
            "/api/v3/(item_vote)": 1
        },
        "2019-10-25": {
            "/api/v3/(files)": 10
        },
        "2019-10-29": {
            "/api/v3/(url_submission)": 1
        },
        "2019-10-30": {
            "/api/v3/(url_submission)": 1
        },
        "2019-10-31": {
            "/api/v3/(domain_comments)": 9,
            "/api/v3/(file_upload_url)": 1,
            "/api/v3/(ip_addresses_comments)": 4,
            "/api/v3/(item_vote)": 13,
            "/api/v3/(url_submission)": 1
        },
        "2019-11-04": {
            "/api/v3/(file_comments)": 2,
            "/api/v3/(files)": 8,
            "/api/v3/(item_vote)": 2
        },
        "2019-11-06": {
            "/api/v3/(file_comments)": 1,
            "/api/v3/(files)": 34
        },
        "2019-11-08": {
            "/api/v3/(analyses)": 1,
            "/api/v3/(item_vote)": 3,
            "/api/v3/(url_comments)": 3,
            "/api/v3/(url_submission)": 2
        },
        "2019-11-09": {
            "/api/v3/(files)": 123
        },
        "2019-11-12": {
            "/api/v3/(file_comments)": 15,
            "/api/v3/(files)": 44,
            "/api/v3/(item_vote)": 15
        },
        "2019-11-13": {
            "/api/v3/(file_comments)": 1,
            "/api/v3/(files)": 2,
            "/api/v3/(item_vote)": 1
        },
        "2019-11-18": {
            "/api/v3/(analyses)": 12,
            "/api/v3/(file_comments)": 10,
            "/api/v3/(file_upload_url)": 1,
            "/api/v3/(files)": 51,
            "/api/v3/(item_vote)": 10
        },
        "2019-11-19": {
            "/api/v3/(domain_comments)": 1,
            "/api/v3/(file_comments)": 9,
            "/api/v3/(files)": 9,
            "/api/v3/(item_vote)": 10
        },
        "2019-11-20": {
            "/api/v3/(file_comments)": 5,
            "/api/v3/(files)": 21,
            "/api/v3/(item_vote)": 5
        },
        "2019-11-21": {
            "/api/v3/(item_vote)": 9,
            "/api/v3/(url_comments)": 9
        }
    },
    "total": {
        "/api/v3/(domain_graphs)": 10,
        "/api/v3/(domain_relationships)": 100,
        "/api/v3/(domains)": 54,
        "/api/v3/(file_behaviours)": 44,
        "/api/v3/(file_download)": 309,
        "/api/v3/(file_graphs)": 43,
        "/api/v3/(file_relationships)": 900,
        "/api/v3/(graphs)": 1,
        "/api/v3/(intelligence_search)": 189,
        "/api/v3/(ip_addresses)": 14,
        "/api/v3/(ip_addresses_graphs)": 4,
        "/api/v3/(ip_addresses_relationships)": 39,
        "/api/v3/(retrohunt_jobs)": 1,
        "/api/v3/(url_graphs)": 12,
        "/api/v3/(url_relationships)": 48,
        "/api/v3/(urls)": 53
    },
    "total_endpoints_not_consuming_quota": {
        "/api/v3/(analyses)": 13,
        "/api/v3/(domain_comments)": 10,
        "/api/v3/(file_comments)": 44,
        "/api/v3/(file_upload_url)": 2,
        "/api/v3/(files)": 551,
        "/api/v3/(ip_addresses_comments)": 6,
        "/api/v3/(item_vote)": 69,
        "/api/v3/(search)": 3,
        "/api/v3/(url_comments)": 12,
        "/api/v3/(url_submission)": 5
    }
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-enterprise",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [],
  "paths": {
    "/users/{id}/api_usage": {
      "get": {
        "summary": "Get a user’s API usage",
        "description": "",
        "operationId": "user-api-usage",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "User ID or API key",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "start_date",
            "in": "query",
            "description": "A string in format YYYYMMDD",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "end_date",
            "in": "query",
            "description": "A string in format YYYYMMDD",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```