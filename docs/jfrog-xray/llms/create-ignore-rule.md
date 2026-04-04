# Source: https://docs.jfrog.com/security/reference/create-ignore-rule.md

# Create Ignore Rule

Creates an Ignore Rule that suppresses violations matching the specified filters. Ignore rules apply only to future scans. To apply to past scans, you must manually trigger Apply on Existing Content on the relevant watch or watches.

The `ignore_filters` object defines what to ignore. You must specify at least one objective filter (vulnerabilities, licenses, cves, operational_risk, or exposures) and can optionally scope it with source filters (components, artifacts, builds, etc.).

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
      "post": {
        "operationId": "create-ignore-rule",
        "summary": "Create Ignore Rule",
        "description": "Creates an Ignore Rule that suppresses violations matching the specified filters. Ignore rules apply only to future scans. To apply to past scans, you must manually trigger Apply on Existing Content on the relevant watch or watches.\n\nThe `ignore_filters` object defines what to ignore. You must specify at least one objective filter (vulnerabilities, licenses, cves, operational_risk, or exposures) and can optionally scope it with source filters (components, artifacts, builds, etc.).\n\nRequires the \"Manage Watches\" permission. Since Xray 3.11.\n",
        "tags": [
          "Ignore Rules V1"
        ],
        "parameters": [
          {
            "name": "projectKey",
            "in": "query",
            "required": false,
            "description": "When provided, the ignore rule is created in the scope of the specified project.\n",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/IgnoreRulesCreateRequest"
              },
              "examples": {
                "licenseBuildScope": {
                  "summary": "Ignore licenses for a build component",
                  "value": {
                    "notes": "ignore any license for any version of alpine for the base layer within all myApp builds",
                    "ignore_filters": {
                      "licenses": [
                        "any"
                      ],
                      "builds": [
                        {
                          "name": "myApp"
                        }
                      ],
                      "components": [
                        {
                          "name": "docker://alpine"
                        }
                      ],
                      "docker-layers": [
                        "0503825856099e6adb39c8297af09547f69684b7016b7f3680ed801aa310baaa"
                      ]
                    }
                  }
                },
                "cveWithExpiration": {
                  "summary": "Ignore a CVE until a specific date",
                  "value": {
                    "notes": "ignore CVE-2016-2168 until the expiration date set",
                    "expires_at": "2026-06-29T00:00:00Z",
                    "ignore_filters": {
                      "cves": [
                        "CVE-2016-2168"
                      ],
                      "watches": [
                        "tstWatch"
                      ]
                    }
                  }
                },
                "operationalRisk": {
                  "summary": "Ignore operational risk for an artifact",
                  "value": {
                    "notes": "ignore Operational Risk for artifact gav://org.jfrog.ignored:ignored-core v2.0.0",
                    "ignore_filters": {
                      "operational_risk": [
                        "any"
                      ],
                      "artifacts": [
                        {
                          "name": "gav://org.jfrog.ignored:ignored-core",
                          "version": "2.0.0"
                        }
                      ]
                    }
                  }
                },
                "exposuresByCategory": {
                  "summary": "Ignore exposures by category and file path",
                  "value": {
                    "notes": "path /etc/envoy/req.sw.envoy.admin-localhost.yaml",
                    "ignore_filters": {
                      "exposures": {
                        "categories": [
                          "secrets",
                          "services"
                        ],
                        "file_path": [
                          "/etc/envoy/req.sw.envoy.admin-localhost.yaml"
                        ]
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Ignore rule created successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string",
                      "description": "Success message including the new rule ID."
                    }
                  }
                },
                "example": {
                  "info": "Successfully added Ignore rule with id: 269c3072-4735-4244-4886-17ae1dc5fcd6"
                }
              }
            }
          },
          "400": {
            "description": "Parsing or validation error.",
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
                  "error": "Ignore rule validation failed"
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
                  "error": "Failed to add ignore rule"
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
      "IgnoreRulesCreateRequest": {
        "type": "object",
        "description": "Request body for creating an ignore rule. Must include notes and an ignore_filters object with at least one objective filter.\n",
        "required": [
          "notes",
          "ignore_filters"
        ],
        "properties": {
          "notes": {
            "type": "string",
            "description": "Free-text note explaining why this rule was created.",
            "example": "ignore CVE-2016-2168 when watch is tstWatch"
          },
          "expires_at": {
            "type": "string",
            "format": "date-time",
            "description": "Optional expiration date in RFC 3339 format. After this date the rule is marked as expired and stops suppressing violations.\n",
            "example": "2026-06-29T00:00:00Z"
          },
          "ignore_filters": {
            "$ref": "#/components/schemas/IgnoreRuleFilters"
          }
        }
      },
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