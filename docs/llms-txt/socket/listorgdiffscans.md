# Source: https://docs.socket.dev/reference/listorgdiffscans.md

# List diff scans

Returns a paginated list of all diff scans in an organization.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- diff-scans:list

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
      "name": "diff-scans"
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
    "/orgs/{org_slug}/diff-scans": {
      "get": {
        "tags": [
          "diff-scans"
        ],
        "summary": "List diff scans",
        "operationId": "listOrgDiffScans",
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
            "description": "Specify sort field.",
            "schema": {
              "type": "string",
              "enum": [
                "created_at",
                "updated_at"
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
              "default": 20
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "required": false,
            "description": "Cursor for pagination. Use the next_cursor or prev_cursor from previous responses.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "repository_id",
            "in": "query",
            "required": false,
            "description": "Filter by repository ID.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "before_full_scan_id",
            "in": "query",
            "required": false,
            "description": "Filter by before full scan ID.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "after_full_scan_id",
            "in": "query",
            "required": false,
            "description": "Filter by after full scan ID.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "diff-scans:list"
            ]
          },
          {
            "basicAuth": [
              "diff-scans:list"
            ]
          }
        ],
        "description": "Returns a paginated list of all diff scans in an organization.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- diff-scans:list",
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
                        "description": "",
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "organization_id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "repository_id": {
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
                          "before_full_scan_id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "after_full_scan_id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "external_href": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "merge": {
                            "type": "boolean",
                            "default": false,
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
                          }
                        },
                        "required": [
                          "after_full_scan_id",
                          "api_url",
                          "before_full_scan_id",
                          "created_at",
                          "description",
                          "external_href",
                          "html_url",
                          "id",
                          "merge",
                          "organization_id",
                          "repository_id",
                          "updated_at"
                        ]
                      },
                      "description": ""
                    },
                    "next_page_href": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "next_cursor": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    }
                  },
                  "required": [
                    "next_cursor",
                    "next_page_href",
                    "results"
                  ]
                }
              }
            },
            "description": "Lists diff scans for the specified organization."
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