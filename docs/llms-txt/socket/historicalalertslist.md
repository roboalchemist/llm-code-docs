# Source: https://docs.socket.dev/reference/historicalalertslist.md

# List historical alerts (Beta)

List historical alerts.

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- historical:alerts-list

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
      "name": "alerts"
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
    "schemas": {
      "Capabilities": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "env": {
            "type": "boolean",
            "default": false,
            "description": "Package can read or modify environment variables"
          },
          "eval": {
            "type": "boolean",
            "default": false,
            "description": "Package uses dynamic code evaluation (eval, Function constructor, etc.)"
          },
          "fs": {
            "type": "boolean",
            "default": false,
            "description": "Package can read or write to the file system"
          },
          "net": {
            "type": "boolean",
            "default": false,
            "description": "Package can make network requests or create servers"
          },
          "shell": {
            "type": "boolean",
            "default": false,
            "description": "Package can execute shell commands or spawn processes"
          },
          "unsafe": {
            "type": "boolean",
            "default": false,
            "description": "Package uses unsafe or dangerous operations that could compromise security"
          },
          "url": {
            "type": "boolean",
            "default": false,
            "description": "Package contains remote URL(s) in the source code"
          }
        },
        "required": [
          "env",
          "eval",
          "fs",
          "net",
          "shell",
          "unsafe",
          "url"
        ]
      },
      "Qualifiers": {},
      "SocketScore": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "license": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 evaluating license permissiveness and compatibility",
            "default": 0
          },
          "maintenance": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 evaluating project maintenance health and activity",
            "default": 0
          },
          "overall": {
            "type": "number",
            "description": "Combined score from 0.0 to 1.0 representing overall package health and safety",
            "default": 0
          },
          "quality": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 evaluating code quality, testing, and documentation",
            "default": 0
          },
          "supplyChain": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 evaluating supply chain security and provenance",
            "default": 0
          },
          "vulnerability": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 based on known vulnerabilities and their severity",
            "default": 0
          }
        },
        "required": [
          "license",
          "maintenance",
          "overall",
          "quality",
          "supplyChain",
          "vulnerability"
        ]
      },
      "SocketManifestReference": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "file": {
            "type": "string",
            "description": "Path to the manifest file (e.g., package.json, pom.xml)",
            "default": ""
          },
          "start": {
            "type": "integer",
            "description": "Starting line or position in the manifest file",
            "default": 0
          },
          "end": {
            "type": "integer",
            "description": "Ending line or position in the manifest file",
            "default": 0
          }
        },
        "required": [
          "file"
        ]
      },
      "SocketId": {
        "type": "string",
        "description": "",
        "default": ""
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
    "/orgs/{org_slug}/historical/alerts": {
      "get": {
        "tags": [
          "alerts"
        ],
        "summary": "List historical alerts (Beta)",
        "operationId": "historicalAlertsList",
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
            "name": "date",
            "in": "query",
            "required": false,
            "description": "The UTC date in YYYY-MM-DD format for which to fetch alerts",
            "schema": {
              "type": "string",
              "default": "CURRENT_DATE"
            }
          },
          {
            "name": "range",
            "in": "query",
            "required": false,
            "description": "The number of days of data to fetch as an offset from input date (e.g. \"-7d\" or \"7d\") or use \"latest\" to query for latest alerts for each repo",
            "schema": {
              "type": "string",
              "default": "-7d"
            }
          },
          {
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Specify the maximum number of results to return per page (intermediate pages may have fewer than this limit and callers should always check \"endCursor\" in response body to know if there are more pages)",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 10000,
              "default": 10000
            }
          },
          {
            "name": "startAfterCursor",
            "in": "query",
            "required": false,
            "description": "The pagination cursor that was returned as the \"endCursor\" property in previous request",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "filters.alertAction",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert actions (\"error\", \"warn\", \"monitor\", or \"ignore) that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertAction.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert actions (\"error\", \"warn\", \"monitor\", or \"ignore) that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertActionSourceType",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert action source types (\"fallback\", \"injected-alert\", \"org-policy\", \"reachability\", \"repo-label-policy\", \"socket-yml\", or \"triage\") that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertActionSourceType.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert action source types (\"fallback\", \"injected-alert\", \"org-policy\", \"reachability\", \"repo-label-policy\", \"socket-yml\", or \"triage\") that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCategory",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert categories (\"supplyChainRisk\", \"maintenance\", \"quality\", \"license\", or \"vulnerability\") that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCategory.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert categories (\"supplyChainRisk\", \"maintenance\", \"quality\", \"license\", or \"vulnerability\") that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCveId",
            "in": "query",
            "required": false,
            "description": "CVE ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCveId.notIn",
            "in": "query",
            "required": false,
            "description": "CVE ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCveTitle",
            "in": "query",
            "required": false,
            "description": "CVE title",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCveTitle.notIn",
            "in": "query",
            "required": false,
            "description": "CVE title",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCweId",
            "in": "query",
            "required": false,
            "description": "CWE ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCweId.notIn",
            "in": "query",
            "required": false,
            "description": "CWE ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCweName",
            "in": "query",
            "required": false,
            "description": "CWE name",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCweName.notIn",
            "in": "query",
            "required": false,
            "description": "CWE name",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertEPSS",
            "in": "query",
            "required": false,
            "description": "Alert EPSS (\"low\", \"medium\", \"high\", \"critical\")",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertEPSS.notIn",
            "in": "query",
            "required": false,
            "description": "Alert EPSS (\"low\", \"medium\", \"high\", \"critical\")",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertFixType",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert fix types (\"upgrade\", \"cve\", or \"remove\") that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertFixType.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert fix types (\"upgrade\", \"cve\", or \"remove\") that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertKEV",
            "in": "query",
            "required": false,
            "description": "Alert KEV (Known Exploited Vulnerability) filter flag",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filters.alertKEV.notIn",
            "in": "query",
            "required": false,
            "description": "Alert KEV (Known Exploited Vulnerability) filter flag",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filters.alertPriority",
            "in": "query",
            "required": false,
            "description": "Alert priority (\"low\", \"medium\", \"high\", or \"critical\")",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertPriority.notIn",
            "in": "query",
            "required": false,
            "description": "Alert priority (\"low\", \"medium\", \"high\", or \"critical\")",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertReachabilityAnalysisType",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert CVE reachability analysis types (\"full-scan\" or \"precomputed\") that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertReachabilityAnalysisType.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert CVE reachability analysis types (\"full-scan\" or \"precomputed\") that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertReachabilityType",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert CVE reachability types (\"direct_dependency\", \"error\", \"maybe_reachable\", \"missing_support\", \"pending\", \"reachable\", \"undeterminable_reachability\", \"unknown\", or \"unreachable\") that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertReachabilityType.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert CVE reachability types (\"direct_dependency\", \"error\", \"maybe_reachable\", \"missing_support\", \"pending\", \"reachable\", \"undeterminable_reachability\", \"unknown\", or \"unreachable\") that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertSeverity",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert severities (\"low\", \"medium\", \"high\", or \"critical\") that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertSeverity.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert severities (\"low\", \"medium\", \"high\", or \"critical\") that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertType",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert types (e.g. \"usesEval\", \"unmaintained\", etc.) that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertType.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of alert types (e.g. \"usesEval\", \"unmaintained\", etc.) that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.artifactName",
            "in": "query",
            "required": false,
            "description": "Name of artifact",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.artifactName.notIn",
            "in": "query",
            "required": false,
            "description": "Name of artifact",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.artifactType",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of artifact types (e.g. \"npm\", \"pypi\", \"gem\", \"maven\", \"golang\", etc.) that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.artifactType.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of artifact types (e.g. \"npm\", \"pypi\", \"gem\", \"maven\", \"golang\", etc.) that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.branch",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of branch names that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.branch.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of branch names that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.cvePatchStatus",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of patch statuses (\"patch_unavailable\", \"patch_available\", or \"patch_applied\") that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.cvePatchStatus.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of patch statuses (\"patch_unavailable\", \"patch_available\", or \"patch_applied\") that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.dependencyDead",
            "in": "query",
            "required": false,
            "description": "Dead/reachable dependency filter flag",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filters.dependencyDead.notIn",
            "in": "query",
            "required": false,
            "description": "Dead/reachable dependency filter flag",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filters.dependencyDev",
            "in": "query",
            "required": false,
            "description": "Development/production dependency filter flag",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filters.dependencyDev.notIn",
            "in": "query",
            "required": false,
            "description": "Development/production dependency filter flag",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filters.dependencyDirect",
            "in": "query",
            "required": false,
            "description": "Direct/transitive dependency filter flag",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filters.dependencyDirect.notIn",
            "in": "query",
            "required": false,
            "description": "Direct/transitive dependency filter flag",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filters.repoFullName",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of repo full names that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.repoFullName.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of repo full names that should be excluded",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.repoLabels",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of repo labels that should be included. Use \"\" to filter for repositories with no labels.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.repoLabels.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of repo labels that should be excluded. Use \"\" to filter for repositories with no labels.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.repoSlug",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of repo slugs that should be included",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.repoSlug.notIn",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of repo slugs that should be excluded",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "historical:alerts-list"
            ]
          },
          {
            "basicAuth": [
              "historical:alerts-list"
            ]
          }
        ],
        "description": "List historical alerts.\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- historical:alerts-list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "endCursor": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "items": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "repoFullName": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "repoId": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "repoSlug": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "repoLabels": {
                            "type": "array",
                            "items": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            },
                            "description": ""
                          },
                          "repoLabelIds": {
                            "type": "array",
                            "items": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            },
                            "description": ""
                          },
                          "branch": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "defaultBranch": {
                            "type": "boolean",
                            "default": false,
                            "description": ""
                          },
                          "fullScanId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "scannedAt": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "artifact": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                              "id": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "license": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "name": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "namespace": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "type": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "version": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "artifact_id": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "artifactId": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "author": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "capabilities": {
                                "$ref": "#/components/schemas/Capabilities"
                              },
                              "qualifiers": {
                                "$ref": "#/components/schemas/Qualifiers"
                              },
                              "scores": {
                                "$ref": "#/components/schemas/SocketScore"
                              },
                              "size": {
                                "type": "integer",
                                "description": "",
                                "default": 0
                              },
                              "subpath": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              }
                            },
                            "required": [
                              "id",
                              "license",
                              "name",
                              "namespace",
                              "type",
                              "version"
                            ]
                          },
                          "alert": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                              "key": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "type": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "severity": {
                                "type": "integer",
                                "description": "",
                                "default": 0
                              },
                              "severityName": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "action": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "category": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "file": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "props": {
                                "type": "object",
                                "description": "",
                                "default": null,
                                "nullable": true
                              },
                              "start": {
                                "type": "integer",
                                "description": "",
                                "default": 0,
                                "nullable": true
                              },
                              "end": {
                                "type": "integer",
                                "description": "",
                                "default": 0,
                                "nullable": true
                              },
                              "fix": {
                                "type": "object",
                                "additionalProperties": false,
                                "description": "",
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "description": "",
                                    "default": ""
                                  },
                                  "description": {
                                    "type": "string",
                                    "description": "",
                                    "default": ""
                                  }
                                },
                                "required": [
                                  "description",
                                  "type"
                                ],
                                "nullable": true
                              }
                            },
                            "required": [
                              "action",
                              "category",
                              "key",
                              "severity",
                              "severityName",
                              "type"
                            ]
                          },
                          "dependency": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                              "direct": {
                                "type": "boolean",
                                "default": false,
                                "description": ""
                              },
                              "dev": {
                                "type": "boolean",
                                "default": false,
                                "description": ""
                              },
                              "dead": {
                                "type": "boolean",
                                "default": false,
                                "description": ""
                              },
                              "manifestFiles": {
                                "type": "array",
                                "items": {
                                  "$ref": "#/components/schemas/SocketManifestReference"
                                },
                                "description": ""
                              },
                              "topLevelAncestors": {
                                "type": "array",
                                "items": {
                                  "$ref": "#/components/schemas/SocketId"
                                },
                                "description": ""
                              },
                              "dependencies": {
                                "type": "array",
                                "items": {
                                  "$ref": "#/components/schemas/SocketId"
                                },
                                "description": ""
                              }
                            },
                            "required": [
                              "dead",
                              "dev",
                              "direct"
                            ]
                          }
                        },
                        "required": [
                          "alert",
                          "artifact",
                          "branch",
                          "defaultBranch",
                          "dependency",
                          "fullScanId",
                          "repoFullName",
                          "repoId",
                          "repoLabelIds",
                          "repoLabels",
                          "repoSlug",
                          "scannedAt"
                        ]
                      },
                      "description": ""
                    },
                    "meta": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "organizationId": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "queryStartTimestamp": {
                          "type": "number",
                          "description": "",
                          "default": 0
                        },
                        "startDateInclusive": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "endDateInclusive": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "includeLatestAlertsOnly": {
                          "type": "boolean",
                          "default": false,
                          "description": ""
                        },
                        "filters": {
                          "type": "object",
                          "additionalProperties": false,
                          "properties": {
                            "alertAction": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert actions (\"error\", \"warn\", \"monitor\", or \"ignore) that should be included"
                            },
                            "alertAction.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert actions (\"error\", \"warn\", \"monitor\", or \"ignore) that should be excluded"
                            },
                            "alertActionSourceType": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert action source types (\"fallback\", \"injected-alert\", \"org-policy\", \"reachability\", \"repo-label-policy\", \"socket-yml\", or \"triage\") that should be included"
                            },
                            "alertActionSourceType.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert action source types (\"fallback\", \"injected-alert\", \"org-policy\", \"reachability\", \"repo-label-policy\", \"socket-yml\", or \"triage\") that should be excluded"
                            },
                            "alertCategory": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert categories (\"supplyChainRisk\", \"maintenance\", \"quality\", \"license\", or \"vulnerability\") that should be included"
                            },
                            "alertCategory.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert categories (\"supplyChainRisk\", \"maintenance\", \"quality\", \"license\", or \"vulnerability\") that should be excluded"
                            },
                            "alertCveId": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "CVE ID"
                            },
                            "alertCveId.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "CVE ID"
                            },
                            "alertCveTitle": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "CVE title"
                            },
                            "alertCveTitle.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "CVE title"
                            },
                            "alertCweId": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "CWE ID"
                            },
                            "alertCweId.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "CWE ID"
                            },
                            "alertCweName": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "CWE name"
                            },
                            "alertCweName.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "CWE name"
                            },
                            "alertEPSS": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert EPSS (\"low\", \"medium\", \"high\", \"critical\")"
                            },
                            "alertEPSS.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert EPSS (\"low\", \"medium\", \"high\", \"critical\")"
                            },
                            "alertFixType": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert fix types (\"upgrade\", \"cve\", or \"remove\") that should be included"
                            },
                            "alertFixType.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert fix types (\"upgrade\", \"cve\", or \"remove\") that should be excluded"
                            },
                            "alertKEV": {
                              "type": "array",
                              "items": {
                                "type": "boolean",
                                "default": false,
                                "description": ""
                              },
                              "description": "Alert KEV (Known Exploited Vulnerability) filter flag"
                            },
                            "alertPriority": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert priority (\"low\", \"medium\", \"high\", or \"critical\")"
                            },
                            "alertPriority.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert priority (\"low\", \"medium\", \"high\", or \"critical\")"
                            },
                            "alertReachabilityAnalysisType": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert CVE reachability analysis types (\"full-scan\" or \"precomputed\") that should be included"
                            },
                            "alertReachabilityAnalysisType.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert CVE reachability analysis types (\"full-scan\" or \"precomputed\") that should be excluded"
                            },
                            "alertReachabilityType": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert CVE reachability types (\"direct_dependency\", \"error\", \"maybe_reachable\", \"missing_support\", \"pending\", \"reachable\", \"undeterminable_reachability\", \"unknown\", or \"unreachable\") that should be included"
                            },
                            "alertReachabilityType.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert CVE reachability types (\"direct_dependency\", \"error\", \"maybe_reachable\", \"missing_support\", \"pending\", \"reachable\", \"undeterminable_reachability\", \"unknown\", or \"unreachable\") that should be excluded"
                            },
                            "alertSeverity": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert severities (\"low\", \"medium\", \"high\", or \"critical\") that should be included"
                            },
                            "alertSeverity.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert severities (\"low\", \"medium\", \"high\", or \"critical\") that should be excluded"
                            },
                            "alertType": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert types (e.g. \"usesEval\", \"unmaintained\", etc.) that should be included"
                            },
                            "alertType.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of alert types (e.g. \"usesEval\", \"unmaintained\", etc.) that should be excluded"
                            },
                            "artifactName": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Name of artifact"
                            },
                            "artifactName.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Name of artifact"
                            },
                            "artifactType": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of artifact types (e.g. \"npm\", \"pypi\", \"gem\", \"maven\", \"golang\", etc.) that should be included"
                            },
                            "artifactType.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of artifact types (e.g. \"npm\", \"pypi\", \"gem\", \"maven\", \"golang\", etc.) that should be excluded"
                            },
                            "branch": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of branch names that should be included"
                            },
                            "branch.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of branch names that should be excluded"
                            },
                            "cvePatchStatus": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of patch statuses (\"patch_unavailable\", \"patch_available\", or \"patch_applied\") that should be included"
                            },
                            "cvePatchStatus.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of patch statuses (\"patch_unavailable\", \"patch_available\", or \"patch_applied\") that should be excluded"
                            },
                            "dependencyDead": {
                              "type": "array",
                              "items": {
                                "type": "boolean",
                                "default": false,
                                "description": ""
                              },
                              "description": "Dead/reachable dependency filter flag"
                            },
                            "dependencyDev": {
                              "type": "array",
                              "items": {
                                "type": "boolean",
                                "default": false,
                                "description": ""
                              },
                              "description": "Development/production dependency filter flag"
                            },
                            "dependencyDirect": {
                              "type": "array",
                              "items": {
                                "type": "boolean",
                                "default": false,
                                "description": ""
                              },
                              "description": "Direct/transitive dependency filter flag"
                            },
                            "repoFullName": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of repo full names that should be included"
                            },
                            "repoFullName.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of repo full names that should be excluded"
                            },
                            "repoLabels": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of repo labels that should be included. Use \"\" to filter for repositories with no labels."
                            },
                            "repoLabels.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of repo labels that should be excluded. Use \"\" to filter for repositories with no labels."
                            },
                            "repoSlug": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of repo slugs that should be included"
                            },
                            "repoSlug.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Comma-separated list of repo slugs that should be excluded"
                            }
                          },
                          "description": ""
                        }
                      },
                      "required": [
                        "endDateInclusive",
                        "filters",
                        "includeLatestAlertsOnly",
                        "organizationId",
                        "queryStartTimestamp",
                        "startDateInclusive"
                      ]
                    }
                  },
                  "required": [
                    "endCursor",
                    "items",
                    "meta"
                  ]
                }
              }
            },
            "description": "The paginated array of API tokens for the organization, and related metadata."
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