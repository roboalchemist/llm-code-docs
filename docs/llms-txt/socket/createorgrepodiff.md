# Source: https://docs.socket.dev/reference/createorgrepodiff.md

# Create diff scan from repository HEAD full-scan

Create a diff scan between the repository's current HEAD full scan and a new full scan from uploaded manifest files.
Returns metadata about the diff scan. Once the diff scan is created, fetch the diff scan from
the [api_url](/reference/getDiffScanById) URL to get the contents of the diff.

The maximum number of files you can upload at a time is 5000 and each file can be no bigger than 268 MB.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
      - repo:list
- diff-scans:create
- full-scans:create

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
    "/orgs/{org_slug}/diff-scans/from-repo/{repo_slug}": {
      "post": {
        "tags": [
          "diff-scans"
        ],
        "summary": "Create diff scan from repository HEAD full-scan",
        "operationId": "createOrgRepoDiff",
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
            "name": "repo_slug",
            "in": "path",
            "required": true,
            "description": "The slug of the repository",
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
            "name": "branch",
            "in": "query",
            "required": false,
            "description": "The branch name to associate the new full-scan with. Branch names must follow Git branch name rules: be 1–255 characters long; cannot be exactly @;  cannot begin or end with /, ., or .lock; cannot contain \"//\", \"..\", or \"@{\"; and cannot include control characters, spaces, or any of ~^:?*[.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "commit_message",
            "in": "query",
            "required": false,
            "description": "The commit message to associate the new full-scan with.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "commit_hash",
            "in": "query",
            "required": false,
            "description": "The commit hash to associate the full-scan with.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "pull_request",
            "in": "query",
            "required": false,
            "description": "The pull request number to associate the new full-scan with.",
            "schema": {
              "type": "integer",
              "minimum": 1
            }
          },
          {
            "name": "committers",
            "in": "query",
            "required": false,
            "description": "The committers to associate the new full-scan with. Set query more than once to set multiple committers.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "integration_type",
            "in": "query",
            "required": false,
            "description": "The integration type to associate the new full-scan with. Defaults to \"api\" if omitted.",
            "schema": {
              "type": "string",
              "enum": [
                "api",
                "github",
                "gitlab",
                "bitbucket",
                "azure",
                "web"
              ]
            }
          },
          {
            "name": "integration_org_slug",
            "in": "query",
            "required": false,
            "description": "The integration org slug to associate the new full-scan with. If omitted, the Socket org name will be used. This is used to generate links and badges.",
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
          },
          {
            "name": "workspace",
            "in": "query",
            "required": false,
            "description": "The workspace of the repository.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "additionalProperties": {
                  "type": "string",
                  "default": {
                    "type": "Buffer",
                    "data": []
                  },
                  "format": "binary",
                  "description": ""
                },
                "properties": {},
                "description": ""
              }
            }
          },
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "repo:list",
              "diff-scans:create",
              "full-scans:create"
            ]
          },
          {
            "basicAuth": [
              "repo:list",
              "diff-scans:create",
              "full-scans:create"
            ]
          }
        ],
        "description": "Create a diff scan between the repository's current HEAD full scan and a new full scan from uploaded manifest files.\nReturns metadata about the diff scan. Once the diff scan is created, fetch the diff scan from\nthe [api_url](/reference/getDiffScanById) URL to get the contents of the diff.\n\nThe maximum number of files you can upload at a time is 5000 and each file can be no bigger than 268 MB.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n      - repo:list\n- diff-scans:create\n- full-scans:create",
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
                    },
                    "unmatchedAfterFiles": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "description": ""
                    }
                  },
                  "required": [
                    "diff_scan",
                    "unmatchedAfterFiles"
                  ]
                }
              }
            },
            "description": "The details of the new full scan and diff scan between the two scans."
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