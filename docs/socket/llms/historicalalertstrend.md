# Source: https://docs.socket.dev/reference/historicalalertstrend.md

# Trend of historical alerts (Beta)

Trend analytics of historical alerts.

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- historical:alerts-trend

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
    "/orgs/{org_slug}/historical/alerts/trend": {
      "get": {
        "tags": [
          "alerts"
        ],
        "summary": "Trend of historical alerts (Beta)",
        "operationId": "historicalAlertsTrend",
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
            "description": "The number of days of data to fetch as an offset from input date",
            "schema": {
              "type": "string",
              "default": "-7d"
            }
          },
          {
            "name": "aggregation.fields",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of fields that should be used for count aggregation (allowed: alertSeverity,repoSlug,repoFullName,branch,repoLabels,alertType,artifactType,alertAction,alertActionSourceType,alertFixType,alertCategory,alertCveId,alertCveTitle,alertCweId,alertCweName,alertReachabilityType,cvePatchStatus,alertReachabilityAnalysisType,alertPriority,alertKEV,alertEPSS,dependencyDirect,dependencyDev,dependencyDead)",
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
              "historical:alerts-trend"
            ]
          },
          {
            "basicAuth": [
              "historical:alerts-trend"
            ]
          }
        ],
        "description": "Trend analytics of historical alerts.\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- historical:alerts-trend",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
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
                        "interval": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "aggregation": {
                          "type": "object",
                          "additionalProperties": false,
                          "description": "",
                          "properties": {
                            "fields": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": ""
                            },
                            "groups": {
                              "type": "array",
                              "items": {
                                "type": "array",
                                "items": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "description": ""
                              },
                              "description": ""
                            }
                          },
                          "required": [
                            "fields",
                            "groups"
                          ]
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
                        "aggregation",
                        "endDateInclusive",
                        "filters",
                        "interval",
                        "organizationId",
                        "startDateInclusive"
                      ]
                    },
                    "items": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "date": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "startOfDayTimestamp": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "dataPoints": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "aggregationGroup": {
                                  "type": "array",
                                  "items": {
                                    "type": "string",
                                    "description": "",
                                    "default": ""
                                  },
                                  "description": ""
                                },
                                "count": {
                                  "type": "integer",
                                  "description": "",
                                  "default": 0
                                },
                                "countDelta": {
                                  "type": "integer",
                                  "description": "",
                                  "default": 0
                                }
                              },
                              "required": [
                                "aggregationGroup",
                                "count",
                                "countDelta"
                              ]
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "dataPoints",
                          "date",
                          "startOfDayTimestamp"
                        ]
                      },
                      "description": ""
                    }
                  },
                  "required": [
                    "items",
                    "meta"
                  ]
                }
              }
            },
            "description": "The trend data"
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