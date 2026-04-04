# Source: https://docs.socket.dev/reference/getorgtriage.md

# List Org Alert Triage

List triage actions for an organization. Results are paginated and can be sorted by created_at or updated_at.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- triage:alerts-list

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
      "name": "triage"
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
    "/orgs/{org_slug}/triage/alerts": {
      "get": {
        "tags": [
          "triage"
        ],
        "summary": "List Org Alert Triage",
        "operationId": "getOrgTriage",
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
            "description": "Field to sort by. One of: created_at, updated_at.",
            "schema": {
              "type": "string",
              "default": "created_at"
            }
          },
          {
            "name": "direction",
            "in": "query",
            "required": false,
            "description": "Sort direction. One of: asc, desc.",
            "schema": {
              "type": "string",
              "default": "desc"
            }
          },
          {
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Number of results per page (1–100, default 30).",
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
            "description": "Page number (1-based).",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 1
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "triage:alerts-list"
            ]
          },
          {
            "basicAuth": [
              "triage:alerts-list"
            ]
          }
        ],
        "description": "List triage actions for an organization. Results are paginated and can be sorted by created_at or updated_at.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- triage:alerts-list",
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
                          "uuid": {
                            "type": "string",
                            "description": "The uuid of the triage action",
                            "default": "",
                            "nullable": true
                          },
                          "package_type": {
                            "type": "string",
                            "description": "The package type associated with the triage state",
                            "default": "",
                            "nullable": true
                          },
                          "package_namespace": {
                            "type": "string",
                            "description": "The package namespace associated with the triage state",
                            "default": "",
                            "nullable": true
                          },
                          "package_name": {
                            "type": "string",
                            "description": "The package name associated with the triage state",
                            "default": "",
                            "nullable": true
                          },
                          "package_version": {
                            "type": "string",
                            "description": "The package version associated with the triage state, it can contain a * suffix for wildcard matching",
                            "default": "",
                            "nullable": true
                          },
                          "alert_key": {
                            "type": "string",
                            "description": "The alert_key associated with the triage state",
                            "default": "",
                            "nullable": true
                          },
                          "alert_type": {
                            "type": "string",
                            "description": "The alert type (e.g., criticalCVE, highCVE) associated with the triage state",
                            "default": "",
                            "nullable": true
                          },
                          "fix_available": {
                            "type": "string",
                            "enum": [
                              "available",
                              "unavailable",
                              "*"
                            ],
                            "description": "Whether a fix must be available, unavailable, or * for any",
                            "default": "*",
                            "nullable": true
                          },
                          "patch_available": {
                            "type": "string",
                            "enum": [
                              "available",
                              "unavailable",
                              "*"
                            ],
                            "description": "Whether a patch must be available, unavailable, or * for any",
                            "default": "*",
                            "nullable": true
                          },
                          "cvss_score_cmp": {
                            "type": "string",
                            "description": "CVSS score comparison (e.g., >=7.5, >5.0, ==8.0)",
                            "default": "",
                            "nullable": true
                          },
                          "created_at": {
                            "type": "string",
                            "description": "The creation date of the triage action",
                            "default": ""
                          },
                          "updated_at": {
                            "type": "string",
                            "description": "The last update date of the triage action",
                            "default": ""
                          },
                          "note": {
                            "type": "string",
                            "description": "The note associated with the triage action",
                            "default": ""
                          },
                          "organization_id": {
                            "type": "string",
                            "description": "The organization id associated with the triage action",
                            "default": ""
                          },
                          "state": {
                            "type": "string",
                            "enum": [
                              "block",
                              "ignore",
                              "inherit",
                              "monitor",
                              "warn"
                            ],
                            "description": "The triage state of the alert",
                            "default": "inherit"
                          },
                          "cve_or_ghsa_id": {
                            "type": "string",
                            "description": "CVE or GHSA ID associated with the triage state",
                            "default": "",
                            "nullable": true
                          },
                          "reachability": {
                            "type": "string",
                            "enum": [
                              "reachable",
                              "unreachable",
                              "other",
                              "*"
                            ],
                            "description": "The reachability of the alert, can be reachable, unreachable, other, or * for any",
                            "default": "*",
                            "nullable": true
                          },
                          "kevs": {
                            "type": "string",
                            "enum": [
                              "exist",
                              "none",
                              "*"
                            ],
                            "description": "Whether the alert has a CISA KEV (Known Exploited Vulnerability), can be exist, none, or * for any",
                            "default": "*",
                            "nullable": true
                          }
                        },
                        "description": ""
                      },
                      "description": ""
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
                    "results"
                  ]
                }
              }
            },
            "description": "Lists triage actions for the specified organization."
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