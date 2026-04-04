# Source: https://docs.jfrog.com/security/reference/listwaiverrequests.md

# List waiver requests

Get waiver requests for packages that were requested to be unblocked.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Curation API",
    "description": "Public REST API for JFrog Curation — policy-based governance of open-source\npackages flowing through JFrog Artifactory remote repositories.\n\nCuration lets you define **conditions** (e.g. \"package has a critical CVE\")\nand attach them to **policies** that either block or audit (dry-run)\nnon-compliant packages. **Waiver requests** allow users to request\nunblocking of a package, and the **audit** endpoint provides full export of\nall approved/blocked events.\n",
    "version": "1.0.0",
    "license": {
      "name": "Proprietary"
    },
    "contact": {
      "name": "JFrog"
    }
  },
  "servers": [
    {
      "url": "{protocol}://{host}:{port}/xray",
      "description": "JFrog Platform (Xray service)",
      "variables": {
        "protocol": {
          "default": "https",
          "enum": [
            "http",
            "https"
          ]
        },
        "host": {
          "default": "localhost"
        },
        "port": {
          "default": "8046"
        }
      }
    }
  ],
  "security": [],
  "tags": [
    {
      "name": "Waiver Requests",
      "description": "Request and list waivers for blocked packages."
    }
  ],
  "paths": {
    "/api/v1/curation/waiver_requests": {
      "get": {
        "operationId": "listWaiverRequests",
        "tags": [
          "Waiver Requests"
        ],
        "summary": "List waiver requests",
        "description": "Get waiver requests for packages that were requested to be unblocked.",
        "parameters": [
          {
            "name": "status",
            "in": "query",
            "description": "Filter by status. One of: `approved`, `rejected`, `pending`.",
            "schema": {
              "type": "string",
              "enum": [
                "approved",
                "rejected",
                "pending"
              ],
              "default": "pending"
            }
          },
          {
            "name": "pkg_type",
            "in": "query",
            "description": "Filter by package type (e.g. `npm`, `pypi`).",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "pkg_name",
            "in": "query",
            "description": "Filter by package name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "pkg_version",
            "in": "query",
            "description": "Filter by package version.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "can_approve",
            "in": "query",
            "description": "When `true`, returns only waiver requests that the current user has permission to approve.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "decision_owners",
            "in": "query",
            "description": "Comma-separated list of owner groups.",
            "schema": {
              "type": "string"
            }
          },
          {
            "$ref": "#/components/parameters/OrderBy"
          },
          {
            "$ref": "#/components/parameters/Direction"
          },
          {
            "$ref": "#/components/parameters/NumOfRows"
          },
          {
            "$ref": "#/components/parameters/PageNum"
          },
          {
            "$ref": "#/components/parameters/Offset"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "data",
                    "meta"
                  ],
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/WaiverResponse"
                      }
                    },
                    "meta": {
                      "$ref": "#/components/schemas/PaginationMeta"
                    }
                  }
                },
                "example": {
                  "data": [
                    {
                      "id": 23,
                      "status": "approved",
                      "created_at": "2025-12-26T14:05:57+05:30",
                      "closed_at": "2025-12-26T17:55:38+05:30",
                      "requesters": [
                        {
                          "user": "admin",
                          "email": "admin@example.com",
                          "requested_at": "2025-12-26T14:05:57+05:30",
                          "justification": "needed for RND"
                        }
                      ]
                    }
                  ],
                  "meta": {
                    "total_count": 1,
                    "result_count": 1,
                    "num_of_rows": 25,
                    "page_num": 1
                  }
                }
              }
            }
          },
          "403": {
            "description": "Permission denied."
          },
          "500": {
            "description": "Internal server error."
          }
        }
      }
    }
  },
  "components": {
    "parameters": {
      "OrderBy": {
        "name": "order_by",
        "in": "query",
        "description": "Field used for sorting. Supported values depend on the endpoint; common values are `id` and `updated_at`.",
        "schema": {
          "type": "string",
          "default": "updated_at"
        }
      },
      "Direction": {
        "name": "direction",
        "in": "query",
        "description": "Sorting direction: `asc` or `desc`.",
        "schema": {
          "type": "string",
          "enum": [
            "asc",
            "desc"
          ],
          "default": "desc"
        }
      },
      "NumOfRows": {
        "name": "num_of_rows",
        "in": "query",
        "description": "Number of rows per page.",
        "schema": {
          "type": "integer",
          "default": 15
        }
      },
      "PageNum": {
        "name": "page_num",
        "in": "query",
        "description": "Page number (1-based).",
        "schema": {
          "type": "integer",
          "default": 1
        }
      },
      "Offset": {
        "name": "offset",
        "in": "query",
        "description": "Alternative to `page_num` — pagination offset (0-based).",
        "schema": {
          "type": "integer",
          "default": 0
        }
      }
    },
    "schemas": {
      "WaiverResponse": {
        "type": "object",
        "required": [
          "id",
          "status",
          "created_at",
          "requesters"
        ],
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64",
            "description": "Unique waiver request identifier."
          },
          "status": {
            "type": "string",
            "enum": [
              "pending",
              "approved",
              "rejected"
            ],
            "description": "Current status of the waiver request."
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          },
          "closed_at": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp when the request was approved or rejected. Absent while pending."
          },
          "requesters": {
            "type": "array",
            "description": "Users who requested this waiver.",
            "items": {
              "$ref": "#/components/schemas/WaiverRequester"
            }
          }
        }
      },
      "WaiverRequester": {
        "type": "object",
        "required": [
          "user",
          "requested_at",
          "justification"
        ],
        "properties": {
          "user": {
            "type": "string",
            "description": "Username."
          },
          "email": {
            "type": "string",
            "format": "email"
          },
          "requested_at": {
            "type": "string",
            "format": "date-time"
          },
          "justification": {
            "type": "string"
          }
        }
      },
      "PaginationMeta": {
        "type": "object",
        "properties": {
          "total_count": {
            "type": "integer",
            "description": "Total objects matching the filter. May be absent if not requested."
          },
          "result_count": {
            "type": "integer",
            "description": "Number of objects in this page."
          },
          "order_by": {
            "type": "string"
          },
          "direction": {
            "type": "string",
            "enum": [
              "asc",
              "desc"
            ]
          },
          "num_of_rows": {
            "type": "integer"
          },
          "page_num": {
            "type": "integer"
          }
        }
      }
    }
  }
}
```