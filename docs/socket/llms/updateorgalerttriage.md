# Source: https://docs.socket.dev/reference/updateorgalerttriage.md

# Update Org Alert Triage

Create or update triage actions on organization alerts. Accepts a batch of triage entries. Omit `uuid` to create a new entry; provide an existing `uuid` to update it. Use `?force=true` for broad triages that lack a specific `alertKey` or granular package information.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- triage:alerts-update

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
      "post": {
        "tags": [
          "triage"
        ],
        "summary": "Create/Update Org Alert Triage",
        "operationId": "updateOrgAlertTriage",
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
            "name": "force",
            "in": "query",
            "required": false,
            "description": "Set to true to force broad triage updates, these are triages lacking a specific alertKey or granular artifact information which may have limited introspection to see what they apply to.",
            "schema": {
              "type": "string",
              "default": "false"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "additionalProperties": false,
                "description": "",
                "properties": {
                  "alertTriage": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "additionalProperties": false,
                      "properties": {
                        "uuid": {
                          "type": "string",
                          "description": "The UUID of the triage entry. Omit to create a new entry; provide to update an existing one.",
                          "default": "",
                          "nullable": true
                        },
                        "packageType": {
                          "type": "string",
                          "description": "The package ecosystem type (e.g., npm, pypi). Use null or \"*\" for wildcard.",
                          "default": "",
                          "nullable": true
                        },
                        "packageNamespace": {
                          "type": "string",
                          "description": "The package namespace or scope. Use null or \"*\" for wildcard.",
                          "default": "",
                          "nullable": true
                        },
                        "packageName": {
                          "type": "string",
                          "description": "The package name. Use null or \"*\" for wildcard.",
                          "default": "",
                          "nullable": true
                        },
                        "packageVersion": {
                          "type": "string",
                          "description": "The package version. Supports a \"*\" suffix for wildcard prefix matching. Use null for any version.",
                          "default": "",
                          "nullable": true
                        },
                        "alertKey": {
                          "type": "string",
                          "description": "The specific alert key to target.",
                          "default": "",
                          "nullable": true
                        },
                        "alertType": {
                          "type": "string",
                          "description": "The alert type (e.g., criticalCVE, highCVE).",
                          "default": "",
                          "nullable": true
                        },
                        "fixAvailable": {
                          "type": "string",
                          "enum": [
                            "available",
                            "unavailable",
                            "*"
                          ],
                          "description": "Whether a fix is available, unavailable, or * for any"
                        },
                        "patchAvailable": {
                          "type": "string",
                          "enum": [
                            "available",
                            "unavailable",
                            "*"
                          ],
                          "description": "Whether a patch is available, unavailable, or * for any"
                        },
                        "kevs": {
                          "type": "string",
                          "enum": [
                            "exist",
                            "none",
                            "*"
                          ],
                          "description": "Whether the alert has a CISA KEV, can be exist, none, or * for any"
                        },
                        "cveOrGhsaId": {
                          "type": "string",
                          "description": "CVE or GHSA ID to match against.",
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
                          "description": "The reachability of the alert, can be reachable, unreachable, other, or * for any"
                        },
                        "cvssScoreCmp": {
                          "type": "string",
                          "description": "CVSS score comparison operator and value (e.g., >=7.5, >5.0, ==8.0).",
                          "default": "",
                          "nullable": true
                        },
                        "note": {
                          "type": "string",
                          "description": "A note or comment for the triage action.",
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
                          "description": "The triage state of the alert"
                        }
                      },
                      "description": ""
                    },
                    "description": ""
                  }
                },
                "required": [
                  "alertTriage"
                ]
              }
            }
          },
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "triage:alerts-update"
            ]
          },
          {
            "basicAuth": [
              "triage:alerts-update"
            ]
          }
        ],
        "description": "Create or update triage actions on organization alerts. Accepts a batch of triage entries. Omit `uuid` to create a new entry; provide an existing `uuid` to update it. Use `?force=true` for broad triages that lack a specific `alertKey` or granular package information.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- triage:alerts-update",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "result": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "required": [
                    "result"
                  ]
                }
              }
            },
            "description": "Updated Alert Triage"
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