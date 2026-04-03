# Source: https://docs.jfrog.com/security/reference/generate-violations-report.md

# Generate Violations Report

Generates a Violations report with data defined by scope and filters. This request starts the report generation process which runs in the background. The returned report ID is used in other requests such as Get Report Content, Export, Delete Report, etc.

For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can generate a Violations report in the scope of a project by using the additional query parameter `projectKey`.

Requires a user with the Manage Reports role. Since Xray 3.11.


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
    "/api/v1/reports/violations": {
      "post": {
        "operationId": "generate-violations-report",
        "summary": "Generate Violations Report",
        "description": "Generates a Violations report with data defined by scope and filters. This request starts the report generation process which runs in the background. The returned report ID is used in other requests such as Get Report Content, Export, Delete Report, etc.\n\nFor Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can generate a Violations report in the scope of a project by using the additional query parameter `projectKey`.\n\nRequires a user with the Manage Reports role. Since Xray 3.11.\n",
        "tags": [
          "Reports V1"
        ],
        "parameters": [
          {
            "name": "projectKey",
            "in": "query",
            "required": false,
            "description": "Generate the report in the scope of the specified project.",
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
                "$ref": "#/components/schemas/ReportsGenerateViolationsRequest"
              },
              "example": {
                "name": "violationsReport",
                "resources": {
                  "repositories": [
                    {
                      "name": "libs-release-local"
                    },
                    {
                      "name": "plugins-release-local",
                      "include_path_patterns": [
                        "*folder1/*path"
                      ]
                    },
                    {
                      "name": "ext-release-local",
                      "include_path_patterns": [
                        "folder1/path/*",
                        "folder2/path*"
                      ],
                      "exclude_path_patterns": [
                        "folder1/path2/*",
                        "folder2/path2*"
                      ]
                    }
                  ],
                  "builds": {
                    "names": [
                      "art-docker-test",
                      "art-docker-prod"
                    ],
                    "include_patterns": [
                      "release*",
                      "feature"
                    ],
                    "exclude_patterns": [
                      "snapshots*",
                      "test*"
                    ],
                    "number_of_latest_versions": 5
                  },
                  "release_bundles": {
                    "names": [
                      "art-pkg",
                      "xray_pkg"
                    ],
                    "include_patterns": [
                      "release*",
                      "feature"
                    ],
                    "exclude_patterns": [
                      "snapshots*",
                      "test*"
                    ],
                    "number_of_latest_versions": 5
                  },
                  "projects": {
                    "keys": [
                      "test1",
                      "test2"
                    ],
                    "include_key_patterns": [
                      "test*"
                    ],
                    "number_of_latest_versions": 5
                  }
                },
                "filters": {
                  "type": "security",
                  "watch_names": [
                    "NameOfWatch1",
                    "NameOfWatch2"
                  ],
                  "watch_patterns": [
                    "WildcardWatch*"
                  ],
                  "component": "*vulnerable:component*",
                  "artifact": "some://impacted*artifact",
                  "policy_names": [
                    "NameOfPolicy"
                  ],
                  "severities": [
                    "High",
                    "Medium"
                  ],
                  "updated": {
                    "start": "2020-01-02T15:00:00Z",
                    "end": "2020-12-15T00:00:00Z"
                  },
                  "security_filters": {
                    "cve": "CVE-2020-10693",
                    "issue_id": "XRAY-87343",
                    "cvss_score": {
                      "min_score": 6.3,
                      "max_score": 9
                    },
                    "summary_contains": "kernel",
                    "has_remediation": false
                  },
                  "license_filters": {
                    "unknown": false,
                    "unrecognized": true,
                    "license_names": [
                      "Apache",
                      "MIT",
                      "AFL"
                    ],
                    "license_patterns": [
                      "*Apache*",
                      "AFL*"
                    ]
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
                  "report_id": 43,
                  "status": "pending"
                }
              }
            }
          },
          "400": {
            "description": "Bad request.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "Not found.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "412": {
            "description": "Report feature is disabled.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "429": {
            "description": "Too many reports.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
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
      "ReportsCvssScoreRange": {
        "type": "object",
        "properties": {
          "min_score": {
            "type": "number",
            "description": "Minimum CVSS score"
          },
          "max_score": {
            "type": "number",
            "description": "Maximum CVSS score"
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
      "ReportsGenerateViolationsRequest": {
        "type": "object",
        "required": [
          "name",
          "resources"
        ],
        "properties": {
          "name": {
            "type": "string",
            "description": "Display name for the report."
          },
          "resources": {
            "$ref": "#/components/schemas/ReportsResourcesBlock"
          },
          "filters": {
            "type": "object",
            "description": "Optional filters to narrow the violations report results.",
            "properties": {
              "type": {
                "type": "string",
                "description": "Violation type filter: security|license|operational_risk."
              },
              "watch_names": {
                "type": "array",
                "description": "Filter by watch names.",
                "items": {
                  "type": "string"
                }
              },
              "watch_patterns": {
                "type": "array",
                "description": "Wildcard patterns for watch names.",
                "items": {
                  "type": "string"
                }
              },
              "component": {
                "type": "string",
                "description": "Wildcard pattern for filtering components."
              },
              "artifact": {
                "type": "string",
                "description": "Wildcard pattern for filtering artifacts."
              },
              "policy_names": {
                "type": "array",
                "description": "Filter by policy names.",
                "items": {
                  "type": "string"
                }
              },
              "severities": {
                "type": "array",
                "description": "Filter by severity levels.",
                "items": {
                  "type": "string"
                }
              },
              "updated": {
                "$ref": "#/components/schemas/ReportsDateRange"
              },
              "security_filters": {
                "type": "object",
                "description": "Additional security-specific filters.",
                "properties": {
                  "cve": {
                    "type": "string"
                  },
                  "issue_id": {
                    "type": "string"
                  },
                  "summary_contains": {
                    "type": "string"
                  },
                  "has_remediation": {
                    "type": "boolean"
                  },
                  "cvss_score": {
                    "$ref": "#/components/schemas/ReportsCvssScoreRange"
                  },
                  "published": {
                    "$ref": "#/components/schemas/ReportsDateRange"
                  }
                }
              },
              "license_filters": {
                "type": "object",
                "description": "Additional license-specific filters.",
                "properties": {
                  "unknown": {
                    "type": "boolean"
                  },
                  "unrecognized": {
                    "type": "boolean"
                  },
                  "license_names": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "license_patterns": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              },
              "scan_date": {
                "$ref": "#/components/schemas/ReportsDateRange"
              },
              "violation_status": {
                "type": "string",
                "description": "Filter by violation status."
              },
              "runtime_filter": {
                "type": "boolean",
                "description": "Filter by runtime context."
              },
              "ca_filter": {
                "type": "boolean",
                "description": "Filter by contextual analysis results."
              }
            }
          },
          "notify": {
            "type": "object",
            "description": "Notification settings for the report.",
            "properties": {
              "emails": {
                "type": "array",
                "description": "Email addresses to notify when the report completes.",
                "items": {
                  "type": "string"
                }
              }
            }
          },
          "cron_schedule": {
            "type": "string",
            "description": "Cron expression for scheduling recurring report generation."
          },
          "cron_schedule_timezone": {
            "type": "string",
            "description": "Timezone for the cron schedule (e.g., UTC, America/New_York)."
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