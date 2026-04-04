# Source: https://docs.jfrog.com/security/reference/generate-due-diligence-report.md

# Generate Due Diligence Report

Generates a Due Diligence report with data defined by scope and filters. This request starts the report generation process which runs in the background. The returned report ID is used in other requests such as Get Report Content, Export, Delete Report, etc.

For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can generate a Due Diligence report in the scope of a project by using the additional query parameter `projectKey`.

Requires a user with the Manage Reports role. Since Xray 3.9.


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
    "/api/v1/reports/licenses": {
      "post": {
        "operationId": "generate-due-diligence-report",
        "summary": "Generate Due Diligence Report",
        "description": "Generates a Due Diligence report with data defined by scope and filters. This request starts the report generation process which runs in the background. The returned report ID is used in other requests such as Get Report Content, Export, Delete Report, etc.\n\nFor Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can generate a Due Diligence report in the scope of a project by using the additional query parameter `projectKey`.\n\nRequires a user with the Manage Reports role. Since Xray 3.9.\n",
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
                "$ref": "#/components/schemas/ReportsGenerateDueDiligenceRequest"
              },
              "example": {
                "name": "report1",
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
                  "component": "*gav:component*",
                  "artifact": "some://impacted*artifact",
                  "unknown": false,
                  "unrecognized": true,
                  "license_names": [
                    "Apache",
                    "MIT",
                    "AFL"
                  ],
                  "license_patterns": [
                    "*Apache*",
                    "The Apache*",
                    "AFL*"
                  ],
                  "scan_date": {
                    "start": "2020-06-29T12:22:16Z",
                    "end": "2020-06-29T12:22:16Z"
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
      "ReportsGenerateDueDiligenceRequest": {
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
            "description": "Optional filters to narrow the license report results.",
            "properties": {
              "component": {
                "type": "string",
                "description": "Wildcard pattern for filtering components."
              },
              "artifact": {
                "type": "string",
                "description": "Wildcard pattern for filtering artifacts."
              },
              "unknown": {
                "type": "boolean",
                "description": "Include components with unknown licenses."
              },
              "unrecognized": {
                "type": "boolean",
                "description": "Include components with unrecognized licenses."
              },
              "license_names": {
                "type": "array",
                "description": "Filter by specific license names.",
                "items": {
                  "type": "string"
                }
              },
              "license_patterns": {
                "type": "array",
                "description": "Wildcard patterns for license names.",
                "items": {
                  "type": "string"
                }
              },
              "scan_date": {
                "$ref": "#/components/schemas/ReportsDateRange"
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