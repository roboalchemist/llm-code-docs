# Source: https://docs.jfrog.com/security/reference/generate-exposures-report.md

# Generate Exposures Report

Generates an Exposures report with data defined by scope and filters. This request starts the report generation process which runs in the background. The returned report ID is used in other requests such as Get Report Content, Export, Delete Report, etc.

Requires a user with the Manage Reports role.


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
    "/api/v1/reports/exposures": {
      "post": {
        "operationId": "generate-exposures-report",
        "summary": "Generate Exposures Report",
        "description": "Generates an Exposures report with data defined by scope and filters. This request starts the report generation process which runs in the background. The returned report ID is used in other requests such as Get Report Content, Export, Delete Report, etc.\n\nRequires a user with the Manage Reports role.\n",
        "tags": [
          "Reports V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ReportsGenerateExposuresRequest"
              },
              "example": {
                "name": "exposures-report",
                "resources": {
                  "repositories": [
                    {
                      "name": "repository-name"
                    }
                  ]
                },
                "filters": {
                  "category": "secrets",
                  "impacted_artifact": "*bin*",
                  "scan_date": {
                    "start": "2023-01-05T08:00:00Z",
                    "end": "2026-01-22T20:00:00Z"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Report generation started. Use the returned report_id to check status, retrieve content, or export the report.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ReportsReportIdStatusResponse"
                },
                "example": {
                  "report_id": 22,
                  "status": "pending"
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
      "ReportsDateRange": {
        "type": "object",
        "description": "Time window (ISO-8601). From product documentation.",
        "properties": {
          "start": {
            "type": "string",
            "description": "Interval start, e.g. 2020-06-29T12:22:16Z"
          },
          "end": {
            "type": "string",
            "description": "Interval end, e.g. 2020-06-29T12:22:16Z"
          }
        }
      },
      "ReportsRepositoryEntry": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Repository name"
          },
          "include_path_patterns": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Optional path include globs"
          },
          "exclude_path_patterns": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Optional path exclude globs"
          }
        },
        "required": [
          "name"
        ]
      },
      "ReportsBuildsScope": {
        "type": "object",
        "properties": {
          "names": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "include_patterns": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "exclude_patterns": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "number_of_latest_versions": {
            "type": "integer"
          }
        }
      },
      "ReportsNamedScopeWithPatterns": {
        "type": "object",
        "properties": {
          "names": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "include_patterns": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "exclude_patterns": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "number_of_latest_versions": {
            "type": "integer"
          }
        }
      },
      "ReportsProjectsScope": {
        "type": "object",
        "properties": {
          "keys": {
            "type": "array",
            "description": "List of project keys.",
            "items": {
              "type": "string"
            }
          },
          "include_key_patterns": {
            "type": "array",
            "description": "Wildcard patterns for including project keys.",
            "items": {
              "type": "string"
            }
          },
          "exclude_key_patterns": {
            "type": "array",
            "description": "Wildcard patterns for excluding project keys.",
            "items": {
              "type": "string"
            }
          },
          "number_of_latest_versions": {
            "type": "integer"
          }
        }
      },
      "ReportsResourcesBlock": {
        "type": "object",
        "description": "Report scope; provide at least one resource category.",
        "properties": {
          "repositories": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ReportsRepositoryEntry"
            }
          },
          "builds": {
            "$ref": "#/components/schemas/ReportsBuildsScope"
          },
          "release_bundles": {
            "$ref": "#/components/schemas/ReportsNamedScopeWithPatterns"
          },
          "release_bundles_v2": {
            "$ref": "#/components/schemas/ReportsBuildsScope"
          },
          "projects": {
            "$ref": "#/components/schemas/ReportsProjectsScope"
          }
        }
      },
      "ReportsGenerateExposuresRequest": {
        "type": "object",
        "required": [
          "name",
          "resources",
          "filters"
        ],
        "properties": {
          "name": {
            "type": "string"
          },
          "resources": {
            "$ref": "#/components/schemas/ReportsResourcesBlock"
          },
          "filters": {
            "type": "object",
            "required": [
              "category"
            ],
            "properties": {
              "category": {
                "type": "string",
                "description": "One of: secrets, services, applications, iac"
              },
              "scan_date": {
                "$ref": "#/components/schemas/ReportsDateRange"
              },
              "impacted_artifact": {
                "type": "string"
              }
            }
          }
        }
      },
      "ReportsReportIdStatusResponse": {
        "type": "object",
        "required": [
          "report_id",
          "status"
        ],
        "properties": {
          "report_id": {
            "type": "integer",
            "description": "New report identifier"
          },
          "status": {
            "type": "string",
            "description": "e.g. pending, running, completed"
          }
        }
      }
    }
  },
  "tags": [
    {
      "name": "Reports V1",
      "description": "APIs from Reports V1"
    }
  ]
}
```