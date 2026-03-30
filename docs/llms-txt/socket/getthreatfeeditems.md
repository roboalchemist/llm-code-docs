# Source: https://docs.socket.dev/reference/getthreatfeeditems.md

# Get Threat Feed Items (Deprecated)

**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/getorgthreatfeeditems) instead.

Paginated list of threat feed items.

This endpoint requires an Enterprise Plan with Threat Feed add-on. [Contact](https://socket.dev/demo?utm_source=api-docs&utm_medium=referral&utm_campaign=tracking) our sales team for more details.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- threat-feed:list

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
    "/threat-feed": {
      "get": {
        "tags": [
          "deprecated"
        ],
        "summary": "Get Threat Feed Items (Deprecated)",
        "deprecated": true,
        "operationId": "getThreatFeedItems",
        "parameters": [
          {
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Number of threats per page",
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
            "description": "Page token",
            "schema": {
              "type": "string",
              "default": "1"
            }
          },
          {
            "name": "sort",
            "in": "query",
            "required": false,
            "description": "Sort sort the threat feed by ID or createdAt attribute.",
            "schema": {
              "type": "string",
              "enum": [
                "id",
                "created_at"
              ],
              "default": "id"
            }
          },
          {
            "name": "discovery_period",
            "in": "query",
            "required": false,
            "description": "Filter results by discovery period",
            "schema": {
              "type": "string",
              "enum": [
                "1h",
                "6h",
                "1d",
                "7d",
                "30d",
                "90d",
                "365d"
              ]
            }
          },
          {
            "name": "direction",
            "in": "query",
            "required": false,
            "description": "Ordering direction of the sort attribute",
            "schema": {
              "type": "string",
              "enum": [
                "desc",
                "asc"
              ],
              "default": "desc"
            }
          },
          {
            "name": "filter",
            "in": "query",
            "required": false,
            "description": "Filter by threat classification. Supported values: `mal` (malware, including possible malware), `vuln` (vulnerability), `typo` (typosquat, including possible typosquat), `anom` (anomaly), `spy` (telemetry), `obf` (obfuscated code), `dual` (dual-use tool), `joke` (protestware or joke package), `tp` (all confirmed true positives), `fp` (false positive), `u` (unreviewed), `c` (classified, i.e. anything except unreviewed).",
            "schema": {
              "type": "string",
              "enum": [
                "u",
                "c",
                "fp",
                "tp",
                "mal",
                "vuln",
                "anom",
                "joke",
                "spy",
                "typo",
                "obf",
                "dual"
              ],
              "default": "mal"
            }
          },
          {
            "name": "name",
            "in": "query",
            "required": false,
            "description": "Filter threats by package name",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "version",
            "in": "query",
            "required": false,
            "description": "Filter threats by package version",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "is_human_reviewed",
            "in": "query",
            "required": false,
            "description": "Only return threats which have been human-reviewed",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "ecosystem",
            "in": "query",
            "required": false,
            "description": "Filter threats by package ecosystem.",
            "schema": {
              "type": "string",
              "enum": [
                "github",
                "cargo",
                "clawhub",
                "composer",
                "chrome",
                "golang",
                "huggingface",
                "maven",
                "npm",
                "nuget",
                "vscode",
                "pypi",
                "gem",
                "swift"
              ]
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "threat-feed:list"
            ]
          },
          {
            "basicAuth": [
              "threat-feed:list"
            ]
          }
        ],
        "description": "**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/getorgthreatfeeditems) instead.\n\nPaginated list of threat feed items.\n\nThis endpoint requires an Enterprise Plan with Threat Feed add-on. [Contact](https://socket.dev/demo?utm_source=api-docs&utm_medium=referral&utm_campaign=tracking) our sales team for more details.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- threat-feed:list",
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
                          "createdAt": {
                            "type": "string",
                            "description": "ISO 8601 timestamp of when the threat in the package artifact was first discovered",
                            "default": "",
                            "format": "date-time"
                          },
                          "updatedAt": {
                            "type": "string",
                            "description": "ISO 8601 timestamp of when the threat record for the package artifact was last updated (e.g., classification changed, package removed from registry, etc.)",
                            "default": "",
                            "format": "date-time"
                          },
                          "publishedAt": {
                            "type": "string",
                            "description": "ISO 8601 timestamp of when the package artifact was published to the respective registry",
                            "default": "",
                            "format": "date-time",
                            "nullable": true
                          },
                          "description": {
                            "type": "string",
                            "description": "Detailed description of the underlying threat",
                            "default": ""
                          },
                          "id": {
                            "type": "integer",
                            "description": "Unique identifier of the threat feed entry",
                            "default": 0
                          },
                          "locationHtmlUrl": {
                            "type": "string",
                            "description": "URL to the threat details page on Socket",
                            "default": "",
                            "format": "uri"
                          },
                          "packageHtmlUrl": {
                            "type": "string",
                            "description": "URL to the affected package page on Socket",
                            "default": "",
                            "format": "uri"
                          },
                          "purl": {
                            "type": "string",
                            "description": "Package URL (PURL) of the affected package artifact",
                            "default": ""
                          },
                          "removedAt": {
                            "type": "string",
                            "description": "ISO 8601 timestamp of when the package artifact was removed from the respective registry, or null if the package is still available on the registry",
                            "default": "",
                            "format": "date-time",
                            "nullable": true
                          },
                          "threatType": {
                            "type": "string",
                            "description": "Threat classification. Possible values: `malware` (known malware), `possible_malware` (AI-detected potential malware), `vulnerability` (potential vulnerability), `typosquat` (human-reviewed typosquat), `possible_typosquat` (AI-detected potential typosquat), `anomaly` (anomalous behavior), `telemetry` (telemetry), `obfuscated` (obfuscated code), `dual_use` (dual-use tool), `troll` (protestware or joke package), `unreviewed` (not yet reviewed), `false_positive` (confirmed false positive).",
                            "default": ""
                          },
                          "needsHumanReview": {
                            "type": "boolean",
                            "default": false,
                            "description": "Whether the threat still is in need of human review by the threat research team"
                          },
                          "threatInstanceId": {
                            "type": "integer",
                            "description": "Unique threat instance identifier across artifacts",
                            "default": 0
                          }
                        },
                        "description": ""
                      },
                      "description": ""
                    },
                    "nextPage": {
                      "type": "string",
                      "description": "",
                      "default": "",
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
            "description": "The paginated list of threats in the feed and the next page querystring token."
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