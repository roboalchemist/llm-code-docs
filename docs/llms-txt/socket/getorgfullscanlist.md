# Source: https://docs.socket.dev/reference/getorgfullscanlist.md

# List full scans

Returns a paginated list of all full scans in an org, excluding SBOM artifacts.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- full-scans:list

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "Specification of the Socket API endpoints",
    "title": "API Endpoints",
    "version": "0"
  },
  "servers": [
    {
      "url": "https://api.socket.dev/v0"
    }
  ],
  "tags": [
    {
      "name": "full-scans"
    }
  ],
  "components": {
    "responses": {
      "SocketBadRequest": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Bad request"
      },
      "SocketUnauthorized": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Unauthorized"
      },
      "SocketForbidden": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Insufficient max_quota for API method"
      },
      "SocketNotFoundResponse": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Resource not found"
      },
      "SocketTooManyRequestsResponse": {
        "description": "Insufficient quota for API route",
        "headers": {
          "Retry-After": {
            "description": "Retry contacting the endpoint *at least* after seconds.\nSee https://tools.ietf.org/html/rfc7231#section-7.1.3",
            "schema": {
              "format": "int32",
              "type": "integer"
            }
          }
        },
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        }
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "description": "Organization Tokens can be passed as a Bearer token"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Organization Tokens can be passed as the user field in basic auth"
      }
    }
  },
  "paths": {
    "/orgs/{org_slug}/full-scans": {
      "get": {
        "tags": [
          "full-scans"
        ],
        "summary": "List full scans",
        "operationId": "getOrgFullScanList",
        "parameters": [
          {
            "name": "org_slug",
            "in": "path",
            "required": true,
            "description": "The slug of the organization",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "sort",
            "in": "query",
            "required": false,
            "description": "Specify Sort order.",
            "schema": {
              "type": "string",
              "enum": [
                "name",
                "created_at"
              ],
              "default": "created_at"
            }
          },
          {
            "name": "direction",
            "in": "query",
            "required": false,
            "description": "Specify sort direction.",
            "schema": {
              "type": "string",
              "enum": [
                "asc",
                "desc"
              ],
              "default": "desc"
            }
          },
          {
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Specify the maximum number of results to return per page.",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 30
            }
          },
          {
            "name": "page",
            "in": "query",
            "required": false,
            "description": "The page number to return when using offset-style pagination. Ignored when cursor pagination is used.",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 1
            }
          },
          {
            "name": "startAfterCursor",
            "in": "query",
            "required": false,
            "description": "Cursor token for pagination. Pass the returned nextPageCursor from previous responses to fetch the next set of results.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "use_cursor",
            "in": "query",
            "required": false,
            "description": "Set to true on the first request to opt into cursor-based pagination.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "from",
            "in": "query",
            "required": false,
            "description": "A Unix timestamp in seconds that filters full-scans prior to the date.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "workspace",
            "in": "query",
            "required": false,
            "description": "A repository workspace to filter full-scans by.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "repo",
            "in": "query",
            "required": false,
            "description": "A repository slug to filter full-scans by.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "branch",
            "in": "query",
            "required": false,
            "description": "A branch name to filter full-scans by.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "pull_request",
            "in": "query",
            "required": false,
            "description": "A PR number to filter full-scans by.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "commit_hash",
            "in": "query",
            "required": false,
            "description": "A commit hash to filter full-scans by.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "scan_type",
            "in": "query",
            "required": false,
            "description": "A scan type to filter full-scans by (e.g. socket, socket_tier1, socket_basics).",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "full-scans:list"
            ]
          },
          {
            "basicAuth": [
              "full-scans:list"
            ]
          }
        ],
        "description": "Returns a paginated list of all full scans in an org, excluding SBOM artifacts.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- full-scans:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "created_at": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "updated_at": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "organization_id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "organization_slug": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "repository_id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "repository_slug": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "branch": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "commit_message": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "commit_hash": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "pull_request": {
                            "type": "integer",
                            "description": "",
                            "default": 0,
                            "nullable": true
                          },
                          "committers": {
                            "type": "array",
                            "items": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            },
                            "description": ""
                          },
                          "html_url": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "api_url": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "workspace": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "repo": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "html_report_url": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "integration_type": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "integration_repo_url": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "integration_branch_url": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "integration_commit_url": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "integration_pull_request_url": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "scan_type": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "scan_state": {
                            "type": "string",
                            "enum": [
                              "pending",
                              "precrawl",
                              "resolve",
                              "scan"
                            ],
                            "description": "The current processing status of the SBOM",
                            "default": "pending",
                            "nullable": true
                          }
                        },
                        "description": ""
                      },
                      "description": ""
                    },
                    "nextPageCursor": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "nextPage": {
                      "type": "integer",
                      "description": "",
                      "default": 0,
                      "nullable": true
                    }
                  },
                  "required": [
                    "nextPage",
                    "nextPageCursor",
                    "results"
                  ]
                }
              }
            },
            "description": "Lists repositories for the specified organization. The authenticated user must be a member of the organization."
          },
          "400": {
            "$ref": "#/components/responses/SocketBadRequest"
          },
          "401": {
            "$ref": "#/components/responses/SocketUnauthorized"
          },
          "403": {
            "$ref": "#/components/responses/SocketForbidden"
          },
          "404": {
            "$ref": "#/components/responses/SocketNotFoundResponse"
          },
          "429": {
            "$ref": "#/components/responses/SocketTooManyRequestsResponse"
          }
        },
        "x-readme": {}
      }
    }
  }
}
```