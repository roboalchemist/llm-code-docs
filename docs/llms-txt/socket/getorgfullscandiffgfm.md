# Source: https://docs.socket.dev/reference/getorgfullscandiffgfm.md

# SCM Comment for Scan Diff

**This endpoint is deprecated.**

Get the dependency overview and dependency alert comments in GitHub flavored markdown between the diff between two existing full scans.

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
      "name": "deprecated"
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
    "/orgs/{org_slug}/full-scans/diff/gfm": {
      "get": {
        "tags": [
          "deprecated"
        ],
        "summary": "SCM Comment for Scan Diff",
        "deprecated": true,
        "operationId": "GetOrgFullScanDiffGfm",
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
            "name": "after",
            "in": "query",
            "required": true,
            "description": "The head full scan ID (newer)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "before",
            "in": "query",
            "required": true,
            "description": "The base full scan ID (older)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "github_installation_id",
            "in": "query",
            "required": false,
            "description": "The ID of the GitHub installation. This will be used to get the GitHub installation settings. If not provided, the default GitHub installation settings will be used.",
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
        "description": "**This endpoint is deprecated.**\n\nGet the dependency overview and dependency alert comments in GitHub flavored markdown between the diff between two existing full scans.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- full-scans:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "before": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
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
                        }
                      },
                      "required": [
                        "api_url",
                        "branch",
                        "commit_hash",
                        "commit_message",
                        "committers",
                        "created_at",
                        "html_url",
                        "id",
                        "organization_id",
                        "organization_slug",
                        "pull_request",
                        "repository_id",
                        "repository_slug",
                        "updated_at"
                      ]
                    },
                    "after": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
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
                        }
                      },
                      "required": [
                        "api_url",
                        "branch",
                        "commit_hash",
                        "commit_message",
                        "committers",
                        "created_at",
                        "html_url",
                        "id",
                        "organization_id",
                        "organization_slug",
                        "pull_request",
                        "repository_id",
                        "repository_slug",
                        "updated_at"
                      ]
                    },
                    "comments": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "overview": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "alerts": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        }
                      },
                      "required": [
                        "alerts",
                        "overview"
                      ]
                    },
                    "directDependenciesChanged": {
                      "type": "boolean",
                      "default": false,
                      "description": ""
                    },
                    "diff_report_url": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    }
                  },
                  "required": [
                    "after",
                    "before",
                    "comments",
                    "diff_report_url",
                    "directDependenciesChanged"
                  ]
                }
              }
            },
            "description": "Metadata about the full scans and the dependency overview and dependency alert comment. Can be used in a pull request context."
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