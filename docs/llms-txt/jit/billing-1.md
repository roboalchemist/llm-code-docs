# Source: https://docs.jit.io/reference/billing-1.md

# Retrieve SCM Billable Minutes Statistics.

Fetch detailed statistics on SCM **billable** minutes consumed by Jit scanners.

This endpoint allows you to access the billable minutes used by various scanning jobs. You can group the results by different categories such as job names, developers, or assets.

**Important:** Data availability starts from **August 18, 2024**, and is available up to **1 year** in the past, even if the provided start date is more than a year ago.

- For `Github` - the billable minutes are always rounded up to the nearest minute (e.g. 20 seconds scan will be considered as 1 minute).

- For `Gitlab` - the billable minutes are calculated based on the actual time spent on the scan.

When grouping by developers (`by_developer=true`), you can also count the number of unique developers who have interacted with the platform through Pull Requests (PRs) or Merge Requests (MRs).

**Requires the following permission:**
`jit.generalMetrics.read`

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Jit Public APIs",
    "description": "Jit Public APIs.\n\nThe API requires that you log in first and obtain a JWT authentication bearer token:\n\nJIT Platform generates CLIENT_ID and SECRET under `Settings -> Users & Permissions -> API Tokens`\n\n For more information, refer to [Users and Permissions](https://docs.jit.io/docs/managing-users#generating-api-tokens)",
    "version": "1",
    "termsOfService": "https://www.jit.io/legal/terms"
  },
  "servers": [
    {
      "url": "https://api.jit.io",
      "description": "Jit API domain"
    }
  ],
  "externalDocs": {
    "url": "https://docs.jit.io/docs",
    "description": "Jit docs"
  },
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "tags": [
    {
      "name": "Billing",
      "description": "Provides details about billing",
      "externalDocs": {
        "url": "https://docs.jit.io/docs/about-jit",
        "description": "Learn about managing this service at Jit."
      }
    }
  ],
  "paths": {
    "/metrics/billing": {
      "get": {
        "summary": "Retrieve SCM Billable Minutes Statistics.",
        "description": "Fetch detailed statistics on SCM **billable** minutes consumed by Jit scanners.\n\nThis endpoint allows you to access the billable minutes used by various scanning jobs. You can group the results by different categories such as job names, developers, or assets.\n\n**Important:** Data availability starts from **August 18, 2024**, and is available up to **1 year** in the past, even if the provided start date is more than a year ago.\n\n- For `Github` - the billable minutes are always rounded up to the nearest minute (e.g. 20 seconds scan will be considered as 1 minute).\n\n- For `Gitlab` - the billable minutes are calculated based on the actual time spent on the scan.\n\nWhen grouping by developers (`by_developer=true`), you can also count the number of unique developers who have interacted with the platform through Pull Requests (PRs) or Merge Requests (MRs).\n\n**Requires the following permission:**\n`jit.generalMetrics.read`",
        "operationId": "billing",
        "parameters": [
          {
            "name": "start_date",
            "in": "query",
            "description": "The start date for the query, in the format `YYYY-MM-DD`, Defaults to 1 month ago if not specified, You can query up to 1 year in the past.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/start_date"
            }
          },
          {
            "name": "end_date",
            "in": "query",
            "description": "The end date for the query, in the format `YYYY-MM-DD`, Defaults to `Now` if not specified.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/end_date"
            }
          },
          {
            "name": "categories",
            "in": "query",
            "description": "Comma separated list of group categories to filter by, e.g., `first_scan, pr`.\n\nAll groups are returned if not specified.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/categories"
            }
          },
          {
            "name": "by_job_name",
            "in": "query",
            "description": "Whether to further group by the name of the job, e.g., `secret-detection`, `software-bill-of-materials`, etc.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/by_job_name"
            }
          },
          {
            "name": "by_developer",
            "in": "query",
            "description": "Whether to further group by the developer name. `N/A` if not applicable (e.g., for scheduled jobs).",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/by_developer"
            }
          },
          {
            "name": "by_asset",
            "in": "query",
            "description": "Whether to further group by asset. It will be grouped by `asset_id`.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/by_asset"
            }
          },
          {
            "name": "exclude_bots",
            "in": "query",
            "description": "Whether to exclude users with names containing [bot], -bot, or _bot_.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/exclude_bots"
            }
          }
        ],
        "tags": [
          "Billing"
        ],
        "responses": {
          "200": {
            "description": "A list of SCM billable minutes statistics, grouped according to your specified filters.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Success"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "400": {
            "description": "Invalid Query Params",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InvalidQueryParams"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UnauthorizedAuthorizerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "403": {
            "description": "Forbidden",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ForbiddenError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InternalServerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ForbiddenError": {
        "title": "ForbiddenErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "FORBIDDEN",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Request is missing the required permissions.",
            "type": "string"
          },
          "missing_permissions": {
            "title": "Missing permissions",
            "description": "List of missing permissions.",
            "nullable": true,
            "example": [
              "jit.category.write",
              "jit.category.read"
            ],
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "InternalServerError": {
        "title": "InternalErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INTERNAL_SERVER_ERROR",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Some error message indicating the issue that occurred",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "UnauthorizedAuthorizerError": {
        "title": "UnauthorizedAuthorizerErrorResponse",
        "type": "object",
        "properties": {
          "Message": {
            "title": "Error message",
            "description": "Human readable error message.\n\n**Important**: This schema does not contain `error` field.",
            "example": "Unauthorized",
            "type": "string"
          }
        },
        "required": [
          "Message"
        ]
      },
      "Access-Control-Allow-Origin": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Credentials": {
        "type": "boolean",
        "default": true
      },
      "InvalidQueryParams": {
        "title": "InvalidQueryParamsExceptionErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "BAD_REQUEST",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error description.",
            "example": "xxx is not a valid date format",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "Success": {
        "title": "BillingResults",
        "type": "object",
        "properties": {
          "start_date": {
            "title": "Start Date",
            "description": "The start date for the query, in the format `YYYY-MM-DD`, Defaults to 1 month ago if not specified, You can query up to 1 year in the past.",
            "example": "2024-03-22",
            "type": "string"
          },
          "end_date": {
            "title": "End Date",
            "description": "The end date for the query, in the format `YYYY-MM-DD`, Defaults to `Now` if not specified.",
            "example": "2024-05-10",
            "type": "string"
          },
          "results": {
            "title": "Billing Results",
            "description": "A list of billing results, each containing detailed statistics on the billable minutes consumed.",
            "example": [
              {
                "total_minutes": 2,
                "category": "pr",
                "job_name": "secret-detection"
              },
              {
                "total_minutes": 1,
                "category": "scheduled",
                "job_name": "enrich"
              }
            ],
            "type": "array",
            "items": {
              "title": "BillingResult",
              "type": "object",
              "properties": {
                "total_minutes": {
                  "title": "Total Minutes",
                  "description": "The total billable minutes consumed.",
                  "example": 2,
                  "type": "number"
                },
                "category": {
                  "title": "Category",
                  "description": "The category of the billing summary, e.g., `pr`, `first_scan`, etc.",
                  "example": "pr",
                  "allOf": [
                    {
                      "title": "JitEventGroups",
                      "description": "An enumeration.",
                      "enum": [
                        "first_scan",
                        "pr",
                        "manual",
                        "scheduled",
                        "deployment"
                      ],
                      "type": "string"
                    }
                  ]
                },
                "job_name": {
                  "title": "Job Name",
                  "description": "The name of the specific job that consumed the billable minutes. This field is optional and is included only if `by_job_name` is `True`.",
                  "example": "secret-detection",
                  "type": "string"
                },
                "developer": {
                  "title": "Developer",
                  "description": "The name of the developer associated with the job. `N/A` if not applicable (e.g., for scheduled jobs).",
                  "example": "johndoe",
                  "type": "string"
                },
                "asset_id": {
                  "title": "Asset ID",
                  "description": "The ID of the asset associated with the job. This field is optional and is included only if `by_asset` is `True`.",
                  "example": "3a85d9e9-715d-43c3-9e20-a91339c233f0",
                  "type": "string"
                }
              },
              "required": [
                "total_minutes",
                "category"
              ]
            }
          }
        },
        "required": [
          "results"
        ]
      },
      "start_date": {
        "example": "2024-03-22",
        "title": "Start Date",
        "type": "string"
      },
      "end_date": {
        "example": "2024-05-10",
        "title": "End Date",
        "type": "string"
      },
      "categories": {
        "example": "first_scan,pr",
        "title": "JitEventGroups",
        "description": "An enumeration.",
        "enum": [
          "first_scan",
          "pr",
          "manual",
          "scheduled",
          "deployment"
        ],
        "type": "string"
      },
      "by_job_name": {
        "default": false,
        "example": false,
        "title": "Group by Job Name",
        "type": "boolean"
      },
      "by_developer": {
        "default": false,
        "example": false,
        "title": "Group by Developer",
        "type": "boolean"
      },
      "by_asset": {
        "default": false,
        "example": false,
        "title": "Group by Asset",
        "type": "boolean"
      },
      "exclude_bots": {
        "default": false,
        "example": false,
        "title": "Exclude Bots",
        "type": "boolean"
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 103,
      "1": 96,
      "2": 119,
      "3": 178,
      "4": 114,
      "5": 109,
      "6": 158,
      "7": 128,
      "8": 238,
      "9": 252,
      "10": 241,
      "11": 194
    }
  }
}
```