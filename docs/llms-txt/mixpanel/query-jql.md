# Source: https://developer.mixpanel.com/reference/query-jql.md

# Custom JQL Query

> ❗️JQL is currently in maintenance mode. We recommend discontinuing use of JQL and using an [alternate method](https://docs.mixpanel.com/docs/export-methods) to get the data you need. Below are alternatives for common use cases and you need help deciding the best method for you, reach out to [support](mixpanel.com/get-support).
>
> * Raw Event export: [Export API](https://developer.mixpanel.com/reference/raw-data-export-api) or [Data Pipelines](https://docs.mixpanel.com/docs/data-pipelines)
> * User Profile export: [Engage Query API](https://developer.mixpanel.com/reference/engage-query) or [Data Pipelines](https://docs.mixpanel.com/docs/data-pipelines)
> * Other reporting: [Query API](https://developer.mixpanel.com/reference/query-api) or in-app [Core Reports](https://docs.mixpanel.com/docs/reports)

The HTTP API is the lowest-level way to use JQL. At its core, the API is very simple: you write a script, and you post it to an API endpoint with some authentication parameters.

For longer scripts, you will likely want to keep the code in a file. If you had your script in a file called my\_query.js, you could run it using the following cURL command:

```sh
curl https://mixpanel.com/api/query/jql \
     -u YOUR_API_SECRET: \
     --data-urlencode script@my_query.js
```

Example curl with the script directly inside of the curl:

```sh
curl --request POST \
     --url https://mixpanel.com/api/query/jql \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data 'script=function main(){
  return Events(params)
    .groupBy(
      ["name"],
      mixpanel.reducer.count()
    )
}
' \
     --data 'params={
  "scriptParam": "paramValue"
}
'
```

Note

* The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.
* Queries will timeout after 2 minutes of run-time.
* You cannot make remote network requests (using XMLHttpRequest) from JavaScript.
* Queries to the JQL endpoint contribute to Query API rate limit and have their own individual limit as well. There is a maximum of 5 concurrent queries and of 60 queries per hour. There is also a 5 GB limit on data that can be processed in a single query, and a 2 GB limit on the resulting output data.

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
      "name": "JQL",
      "description": "Write a custom query on your data"
    }
  ],
  "paths": {
    "/jql": {
      "post": {
        "operationId": "query-jql",
        "summary": "Custom JQL Query",
        "tags": [
          "JQL"
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
                "required": [
                  "script"
                ],
                "example": {
                  "script": "function main(){\n  return Events(params)\n    .groupBy(\n      [\"name\"],\n      mixpanel.reducer.count()\n    )\n}\n",
                  "params": "{\n  \"from_date\": 2016-01-01T00:00:00.000Z,\n  \"to_date\": 2016-01-07T00:00:00.000Z\n}\n"
                },
                "properties": {
                  "script": {
                    "type": "string",
                    "default": "function main(){\n  return Events(params)\n    .groupBy(\n      [\"name\"],\n      mixpanel.reducer.count()\n    )\n}\n",
                    "description": "The script to run."
                  },
                  "params": {
                    "type": "string",
                    "format": "blob",
                    "default": "{\n  \"scriptParam\": \"paramValue\"\n}\n",
                    "description": "A JSON-encoded object that will be made available to the script as the params global variable."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object"
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