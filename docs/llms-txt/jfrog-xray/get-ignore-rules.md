# Source: https://docs.jfrog.com/security/reference/get-ignore-rules.md

# Get Ignore Rules

Returns all Ignore Rules matching the specified query filters. All filter parameters are optional. Use pagination parameters to control result size.

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
    "/api/v1/ignore_rules": {
      "get": {
        "operationId": "get-ignore-rules",
        "summary": "Get Ignore Rules",
        "description": "Returns all Ignore Rules matching the specified query filters. All filter parameters are optional. Use pagination parameters to control result size.\n\nRequires the \"Manage Watches\" permission. Since Xray 3.11.\n",
        "tags": [
          "Ignore Rules V1"
        ],
        "parameters": [
          {
            "name": "vulnerability",
            "in": "query",
            "required": false,
            "description": "Filter by vulnerability ID (XRAY-nnnnn).",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cve",
            "in": "query",
            "required": false,
            "description": "Filter by CVE ID.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "license",
            "in": "query",
            "required": false,
            "description": "Filter by license name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "policy",
            "in": "query",
            "required": false,
            "description": "Filter by policy name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "watch",
            "in": "query",
            "required": false,
            "description": "Filter by watch name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "component_name",
            "in": "query",
            "required": false,
            "description": "Filter by component name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "component_version",
            "in": "query",
            "required": false,
            "description": "Filter by component version.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "artifact_name",
            "in": "query",
            "required": false,
            "description": "Filter by artifact name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "artifact_version",
            "in": "query",
            "required": false,
            "description": "Filter by artifact version.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "artifact_path",
            "in": "query",
            "required": false,
            "description": "Filter by artifact path.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "build_name",
            "in": "query",
            "required": false,
            "description": "Filter by build name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "build_version",
            "in": "query",
            "required": false,
            "description": "Filter by build version.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "release_bundle_name",
            "in": "query",
            "required": false,
            "description": "Filter by release bundle name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "release_bundle_version",
            "in": "query",
            "required": false,
            "description": "Filter by release bundle version.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "docker_layer",
            "in": "query",
            "required": false,
            "description": "Filter by Docker layer SHA.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "exposures_scanner",
            "in": "query",
            "required": false,
            "description": "Filter by exposure scanner ID.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "exposures_category",
            "in": "query",
            "required": false,
            "description": "Filter by exposure category.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "exposures_file_path",
            "in": "query",
            "required": false,
            "description": "Filter by exposure file path.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "exposures_fingerprint",
            "in": "query",
            "required": false,
            "description": "Filter by exposure fingerprint.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "git_repository",
            "in": "query",
            "required": false,
            "description": "Filter by git repository name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "expires_before",
            "in": "query",
            "required": false,
            "description": "Filter rules expiring before this date (RFC 3339).",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "expires_after",
            "in": "query",
            "required": false,
            "description": "Filter rules expiring after this date (RFC 3339).",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "order_by",
            "in": "query",
            "required": false,
            "description": "Sort field. Valid values: external_id, author, created, expires_at, project_key. Default: created.\n",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "direction",
            "in": "query",
            "required": false,
            "description": "Sort direction. Default: asc.",
            "schema": {
              "type": "string",
              "enum": [
                "asc",
                "desc"
              ]
            }
          },
          {
            "name": "page_num",
            "in": "query",
            "required": false,
            "description": "Page number (1-based).",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "num_of_rows",
            "in": "query",
            "required": false,
            "description": "Number of rows per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "projectKey",
            "in": "query",
            "required": false,
            "description": "Scope results to the specified project.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved ignore rules.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/IgnoreRuleApiResponse"
                      }
                    },
                    "total_count": {
                      "type": "integer",
                      "description": "Total number of matching ignore rules."
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid query parameters.",
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
                  "error": "invalid params"
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
                  "error": "Failed to get ignore rules"
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