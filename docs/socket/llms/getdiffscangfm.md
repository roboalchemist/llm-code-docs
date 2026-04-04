# Source: https://docs.socket.dev/reference/getdiffscangfm.md

# SCM Comment for Diff Scan

Get the dependency overview and dependency alert comments in GitHub flavored markdown for an existing diff scan.

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
    "/orgs/{org_slug}/diff-scans/{diff_scan_id}/gfm": {
      "get": {
        "tags": [
          "diff-scans"
        ],
        "summary": "SCM Comment for Diff Scan",
        "operationId": "GetDiffScanGfm",
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
            "name": "diff_scan_id",
            "in": "path",
            "required": true,
            "description": "The ID of the diff scan",
            "schema": {
              "type": "string",
              "format": "uuid"
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
              "diff-scans:list"
            ]
          },
          {
            "basicAuth": [
              "diff-scans:list"
            ]
          }
        ],
        "description": "Get the dependency overview and dependency alert comments in GitHub flavored markdown for an existing diff scan.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- diff-scans:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "diff_scan": {
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
                        "before_full_scan": {
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
                        "after_full_scan": {
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
                        },
                        "gfm": {
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
                        }
                      },
                      "required": [
                        "after_full_scan",
                        "api_url",
                        "before_full_scan",
                        "created_at",
                        "description",
                        "external_href",
                        "gfm",
                        "html_url",
                        "id",
                        "merge",
                        "organization_id",
                        "repository_id",
                        "updated_at"
                      ]
                    }
                  },
                  "required": [
                    "diff_scan"
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