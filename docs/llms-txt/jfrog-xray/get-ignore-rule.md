# Source: https://docs.jfrog.com/security/reference/get-ignore-rule.md

# Get Ignore Rule

Returns a single Ignore Rule by its ID, including its filters and metadata.

Requires the "Manage Watches" permission. Since Xray 3.11.


# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Xray REST APIs",
    "description": "Combined JFrog Xray REST API specification (all endpoints).",
    "version": "3.140"
  },
  "servers": [
    {
      "url": "https://jf.example.com/xray",
      "description": "JFrog Platform (Xray)"
    }
  ],
  "security": [
    {
      "basicAuth": []
    }
  ],
  "paths": {
    "/api/v1/ignore_rules/{id}": {
      "get": {
        "operationId": "get-ignore-rule",
        "summary": "Get Ignore Rule",
        "description": "Returns a single Ignore Rule by its ID, including its filters and metadata.\n\nRequires the \"Manage Watches\" permission. Since Xray 3.11.\n",
        "tags": [
          "Ignore Rules V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The external ID of the ignore rule.",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "269c3072-4735-4244-4886-17ae1dc5fcd6"
          },
          {
            "name": "projectKey",
            "in": "query",
            "required": false,
            "description": "Scope to the specified project.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved the ignore rule.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IgnoreRuleApiResponse"
                },
                "example": {
                  "id": "93989214-d2db-4692-6e3e-7dbc39f1bc17",
                  "author": "admin",
                  "created": "2024-01-15T10:30:00.000Z",
                  "notes": "ignore CVE-2016-2168 when watch is tstWatch",
                  "is_expired": false,
                  "expires_at": "2026-02-25T21:59:59Z",
                  "project_key": "myproj",
                  "ignore_filters": {
                    "vulnerabilities": [
                      "Vuln1",
                      "Vuln2"
                    ],
                    "licenses": [],
                    "watches": [
                      "Watch1",
                      "Watch2"
                    ],
                    "components": [
                      {
                        "name": "docker://redis"
                      },
                      {
                        "name": "Comp2",
                        "version": "2.6"
                      },
                      {
                        "name": "Comp3",
                        "version": "1.03"
                      }
                    ]
                  }
                }
              }
            }
          },
          "400": {
            "description": "Empty ignore rule ID.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Got an empty ignore rule id"
                }
              }
            }
          },
          "404": {
            "description": "Ignore rule not found.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Ignore rule '269c3072-4735-4244-4886-17ae1dc5fcd6' doesn't exist"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Failed to get ignore rule"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication using username/password or API key"
      }
    },
    "schemas": {
      "IgnoreRuleFilters": {
        "type": "object",
        "description": "Filters that define what to ignore. Combine objective filters (what issue type) with optional scope filters (where to apply). At least one objective filter is required.\n",
        "properties": {
          "vulnerabilities": {
            "type": "array",
            "description": "List of vulnerability IDs (XRAY-nnnnn) to ignore. Use [\"any\"] to ignore all vulnerabilities.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "XRAY-12345"
            ]
          },
          "cves": {
            "type": "array",
            "description": "List of CVE IDs to ignore. Use [\"any\"] to ignore all CVEs.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "CVE-2016-2168"
            ]
          },
          "licenses": {
            "type": "array",
            "description": "List of license names to ignore. Use [\"any\"] to ignore all licenses.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "any"
            ]
          },
          "operational_risk": {
            "type": "array",
            "description": "List of operational risk identifiers. Use [\"any\"] to ignore all.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "any"
            ]
          },
          "exposures": {
            "type": "object",
            "description": "Exposure-specific filters.",
            "properties": {
              "scanners": {
                "type": "array",
                "description": "List of exposure scanner IDs (e.g., EXP-12345).",
                "items": {
                  "type": "string"
                }
              },
              "categories": {
                "type": "array",
                "description": "Exposure categories (secrets, services, applications, iac, malicious_code).",
                "items": {
                  "type": "string"
                }
              },
              "file_path": {
                "type": "array",
                "description": "Specific file paths to ignore.",
                "items": {
                  "type": "string"
                }
              },
              "file_path_pattern": {
                "type": "array",
                "description": "File path patterns to ignore.",
                "items": {
                  "type": "string"
                }
              },
              "fingerprints": {
                "type": "array",
                "description": "Exposure fingerprints to ignore.",
                "items": {
                  "type": "string"
                }
              }
            }
          },
          "policies": {
            "type": "array",
            "description": "Scope filter - list of policy names.",
            "items": {
              "type": "string"
            }
          },
          "watches": {
            "type": "array",
            "description": "Scope filter - list of watch names.",
            "items": {
              "type": "string"
            },
            "example": [
              "tstWatch"
            ]
          },
          "projects": {
            "type": "array",
            "description": "Scope filter - list of project keys.",
            "items": {
              "type": "string"
            }
          },
          "components": {
            "type": "array",
            "description": "Scope filter - list of components (name required, version optional).",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Component identifier (e.g., docker://alpine, npm://lodash)."
                },
                "version": {
                  "type": "string",
                  "description": "Component version. Omit to match all versions."
                }
              }
            }
          },
          "artifacts": {
            "type": "array",
            "description": "Scope filter - list of artifacts (name required, version/path optional).",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "version": {
                  "type": "string"
                },
                "path": {
                  "type": "string"
                }
              }
            }
          },
          "builds": {
            "type": "array",
            "description": "Scope filter - list of builds (name required, version/project optional).",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "version": {
                  "type": "string"
                },
                "project": {
                  "type": "string"
                }
              }
            }
          },
          "release-bundles": {
            "type": "array",
            "description": "Scope filter - list of release bundles (name required, version optional).",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "version": {
                  "type": "string"
                }
              }
            }
          },
          "release_bundles_v2": {
            "type": "array",
            "description": "Scope filter - list of v2 release bundles.",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "version": {
                  "type": "string"
                }
              }
            }
          },
          "docker-layers": {
            "type": "array",
            "description": "Scope filter - list of Docker layer SHA256 hashes.",
            "items": {
              "type": "string"
            }
          },
          "git_repositories": {
            "type": "array",
            "description": "Scope filter - list of git repository names.",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "IgnoreRuleApiResponse": {
        "type": "object",
        "description": "An ignore rule as returned by the GET endpoints.",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique external identifier of the ignore rule.",
            "example": "269c3072-4735-4244-4886-17ae1dc5fcd6"
          },
          "author": {
            "type": "string",
            "description": "User who created the rule.",
            "example": "admin"
          },
          "created": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp when the rule was created (RFC 3339).",
            "example": "2024-01-15T10:30:00.000Z"
          },
          "notes": {
            "type": "string",
            "description": "Free-text note explaining the rule.",
            "example": "ignore CVE-2016-2168 when watch is tstWatch"
          },
          "is_expired": {
            "type": "boolean",
            "description": "Whether the rule has expired.",
            "example": false
          },
          "expires_at": {
            "type": "string",
            "format": "date-time",
            "description": "Expiration date, if set (RFC 3339)."
          },
          "project_key": {
            "type": "string",
            "description": "Project key if the rule is project-scoped."
          },
          "deleted_by": {
            "type": "string",
            "description": "User who deleted the rule (if soft-deleted)."
          },
          "deleted_at": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp when the rule was deleted (if soft-deleted)."
          },
          "ignore_filters": {
            "$ref": "#/components/schemas/IgnoreRuleFilters"
          }
        }
      }
    }
  },
  "tags": [
    {
      "name": "Ignore Rules V1",
      "description": "APIs from Ignore Rules V1"
    }
  ]
}
```