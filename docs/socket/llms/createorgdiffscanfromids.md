# Source: https://docs.socket.dev/reference/createorgdiffscanfromids.md

# Create diff scan from full scan IDs

Create a diff scan from two existing full scan IDs. The full scans must be in the same repository.
Returns metadata about the diff scan. Once the diff scan is created, fetch the diff scan from
the [api_url](/reference/getDiffScanById) URL to get the contents of the diff.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
      - diff-scans:create
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
      },
      "SocketConflict": {
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
        "description": "Resource already exists"
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
    "/orgs/{org_slug}/diff-scans/from-ids": {
      "post": {
        "tags": [
          "diff-scans"
        ],
        "summary": "Create diff scan from full scan IDs",
        "operationId": "createOrgDiffScanFromIds",
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
            "name": "before",
            "in": "query",
            "required": true,
            "description": "The ID of the before/base full scan (older)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "after",
            "in": "query",
            "required": true,
            "description": "The ID of the after/head full scan (newer)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "description",
            "in": "query",
            "required": false,
            "description": "A description of the diff scan. This will be used in the diff report and can be used to provide context for the changes made.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "external_href",
            "in": "query",
            "required": false,
            "description": "An external URL to associate with the diff scan. This can be a link to a pull request, issue, or any other relevant resource.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "merge",
            "in": "query",
            "required": false,
            "description": "Set to true when running a diff between a merged commit and its parent commit in the same branch. Set to false when running diffs in an open PR between unmerged commits.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "diff-scans:create",
              "full-scans:list"
            ]
          },
          {
            "basicAuth": [
              "diff-scans:create",
              "full-scans:list"
            ]
          }
        ],
        "description": "Create a diff scan from two existing full scan IDs. The full scans must be in the same repository.\nReturns metadata about the diff scan. Once the diff scan is created, fetch the diff scan from\nthe [api_url](/reference/getDiffScanById) URL to get the contents of the diff.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n      - diff-scans:create\n- full-scans:list",
        "responses": {
          "201": {
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
                        }
                      },
                      "required": [
                        "after_full_scan",
                        "api_url",
                        "before_full_scan",
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
                    }
                  },
                  "required": [
                    "diff_scan"
                  ]
                }
              }
            },
            "description": "The details of the created diff scan."
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
          "409": {
            "$ref": "#/components/responses/SocketConflict"
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