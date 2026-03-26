# Source: https://docs.socket.dev/reference/alertslist.md

# List latest alerts (Beta)

List latest alerts.

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- alerts:list

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
    "/orgs/{org_slug}/alerts": {
      "get": {
        "tags": [
          "alerts"
        ],
        "summary": "List latest alerts (Beta)",
        "operationId": "alertsList",
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
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Specify the maximum number of results to return per page (intermediate pages may have fewer than this limit and callers should always check \"endCursor\" in response body to know if there are more pages)",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 5000,
              "default": 1000
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
            "name": "filters.alertClearedAt.eq",
            "in": "query",
            "required": false,
            "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertClearedAt.lt",
            "in": "query",
            "required": false,
            "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertClearedAt.lte",
            "in": "query",
            "required": false,
            "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertClearedAt.gt",
            "in": "query",
            "required": false,
            "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertClearedAt.gte",
            "in": "query",
            "required": false,
            "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCreatedAt.eq",
            "in": "query",
            "required": false,
            "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCreatedAt.lt",
            "in": "query",
            "required": false,
            "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCreatedAt.lte",
            "in": "query",
            "required": false,
            "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCreatedAt.gt",
            "in": "query",
            "required": false,
            "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertCreatedAt.gte",
            "in": "query",
            "required": false,
            "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
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
            "name": "filters.alertStatus",
            "in": "query",
            "required": false,
            "description": "A single alert status (\"open\" or \"cleared\")",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertStatus.notIn",
            "in": "query",
            "required": false,
            "description": "A single alert status (\"open\" or \"cleared\")",
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
            "name": "filters.alertUpdatedAt.eq",
            "in": "query",
            "required": false,
            "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertUpdatedAt.lt",
            "in": "query",
            "required": false,
            "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertUpdatedAt.lte",
            "in": "query",
            "required": false,
            "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertUpdatedAt.gt",
            "in": "query",
            "required": false,
            "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters.alertUpdatedAt.gte",
            "in": "query",
            "required": false,
            "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)",
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
              "alerts:list"
            ]
          },
          {
            "basicAuth": [
              "alerts:list"
            ]
          }
        ],
        "description": "List latest alerts.\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- alerts:list",
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
                          "category": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": "",
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
                                "default": "",
                                "nullable": true
                              }
                            },
                            "required": [
                              "description",
                              "type"
                            ],
                            "nullable": true
                          },
                          "vulnerability": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "",
                            "properties": {
                              "cveId": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "cveTitle": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "cveDescription": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "cvssScore": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              },
                              "cvssVectorString": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "cweIds": {
                                "type": "array",
                                "items": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "description": "",
                                "nullable": true
                              },
                              "cweNames": {
                                "type": "array",
                                "items": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "description": "",
                                "nullable": true
                              },
                              "ghsaIds": {
                                "type": "array",
                                "items": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "description": "",
                                "nullable": true
                              },
                              "epssScore": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              },
                              "epssPercentile": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              },
                              "isKev": {
                                "type": "boolean",
                                "default": false,
                                "description": ""
                              },
                              "firstPatchedVersionIdentifier": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              },
                              "url": {
                                "type": "string",
                                "description": "",
                                "default": "",
                                "nullable": true
                              }
                            },
                            "required": [
                              "cveDescription",
                              "cveId",
                              "cveTitle",
                              "cvssScore",
                              "cvssVectorString",
                              "cweIds",
                              "cweNames",
                              "epssPercentile",
                              "epssScore",
                              "firstPatchedVersionIdentifier",
                              "ghsaIds",
                              "isKev",
                              "url"
                            ],
                            "nullable": true
                          },
                          "id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "version": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "status": {
                            "type": "string",
                            "enum": [
                              "open",
                              "cleared"
                            ],
                            "description": "",
                            "default": "open"
                          },
                          "createdAt": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "updatedAt": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "clearedAt": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "dashboardUrl": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "title": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "severity": {
                            "type": "string",
                            "enum": [
                              "low",
                              "medium",
                              "high",
                              "critical"
                            ],
                            "description": "",
                            "default": "low"
                          },
                          "locations": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "action": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "actionSourceType": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "reachability": {
                                  "type": "object",
                                  "additionalProperties": false,
                                  "description": "",
                                  "properties": {
                                    "type": {
                                      "type": "string",
                                      "description": "",
                                      "default": ""
                                    },
                                    "analysisType": {
                                      "type": "string",
                                      "description": "",
                                      "default": "",
                                      "nullable": true
                                    }
                                  },
                                  "required": [
                                    "analysisType",
                                    "type"
                                  ]
                                },
                                "licenseViolation": {
                                  "type": "object",
                                  "additionalProperties": false,
                                  "description": "",
                                  "properties": {
                                    "violationData": {
                                      "type": "array",
                                      "items": {
                                        "type": "object",
                                        "additionalProperties": false,
                                        "description": "",
                                        "properties": {
                                          "purl": {
                                            "type": "string",
                                            "description": "",
                                            "default": "",
                                            "nullable": true
                                          },
                                          "spdxAtomOrExtraData": {
                                            "type": "string",
                                            "description": "",
                                            "default": ""
                                          }
                                        },
                                        "required": [
                                          "purl",
                                          "spdxAtomOrExtraData"
                                        ]
                                      },
                                      "description": ""
                                    }
                                  },
                                  "required": [
                                    "violationData"
                                  ],
                                  "nullable": true
                                },
                                "prioritization": {
                                  "type": "object",
                                  "additionalProperties": false,
                                  "description": "",
                                  "properties": {
                                    "overallScore": {
                                      "type": "number",
                                      "description": "",
                                      "default": 0
                                    },
                                    "fixableScore": {
                                      "type": "number",
                                      "description": "",
                                      "default": 0
                                    },
                                    "reachableScore": {
                                      "type": "number",
                                      "description": "",
                                      "default": 0
                                    },
                                    "severityScore": {
                                      "type": "number",
                                      "description": "",
                                      "default": 0
                                    }
                                  },
                                  "required": [
                                    "fixableScore",
                                    "overallScore",
                                    "reachableScore",
                                    "severityScore"
                                  ]
                                },
                                "repository": {
                                  "type": "object",
                                  "additionalProperties": false,
                                  "description": "",
                                  "properties": {
                                    "fullName": {
                                      "type": "string",
                                      "description": "",
                                      "default": "",
                                      "nullable": true
                                    },
                                    "id": {
                                      "type": "string",
                                      "description": "",
                                      "default": "",
                                      "nullable": true
                                    },
                                    "slug": {
                                      "type": "string",
                                      "description": "",
                                      "default": "",
                                      "nullable": true
                                    },
                                    "workspace": {
                                      "type": "string",
                                      "description": "",
                                      "default": "",
                                      "nullable": true
                                    },
                                    "labels": {
                                      "type": "array",
                                      "items": {
                                        "type": "string",
                                        "description": "",
                                        "default": ""
                                      },
                                      "description": ""
                                    },
                                    "labelIds": {
                                      "type": "array",
                                      "items": {
                                        "type": "string",
                                        "description": "",
                                        "default": ""
                                      },
                                      "description": ""
                                    }
                                  },
                                  "required": [
                                    "fullName",
                                    "id",
                                    "labelIds",
                                    "labels",
                                    "slug",
                                    "workspace"
                                  ],
                                  "nullable": true
                                },
                                "branch": {
                                  "type": "object",
                                  "additionalProperties": false,
                                  "description": "",
                                  "properties": {
                                    "name": {
                                      "type": "string",
                                      "description": "",
                                      "default": ""
                                    },
                                    "type": {
                                      "type": "string",
                                      "description": "",
                                      "default": "",
                                      "nullable": true
                                    }
                                  },
                                  "required": [
                                    "name",
                                    "type"
                                  ],
                                  "nullable": true
                                },
                                "patch": {
                                  "type": "object",
                                  "additionalProperties": false,
                                  "description": "",
                                  "properties": {
                                    "uuid": {
                                      "type": "string",
                                      "description": "",
                                      "default": "",
                                      "nullable": true
                                    },
                                    "status": {
                                      "type": "string",
                                      "enum": [
                                        "patch_unavailable",
                                        "patch_available",
                                        "patch_applied"
                                      ],
                                      "description": "",
                                      "default": "patch_unavailable"
                                    },
                                    "deprecated": {
                                      "type": "boolean",
                                      "default": false,
                                      "description": ""
                                    }
                                  },
                                  "required": [
                                    "deprecated",
                                    "status",
                                    "uuid"
                                  ]
                                },
                                "dependency": {
                                  "type": "object",
                                  "additionalProperties": false,
                                  "description": "",
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
                                    }
                                  },
                                  "required": [
                                    "dead",
                                    "dev",
                                    "direct",
                                    "manifestFiles"
                                  ]
                                },
                                "artifact": {
                                  "type": "object",
                                  "additionalProperties": false,
                                  "description": "",
                                  "properties": {
                                    "type": {
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
                                    "name": {
                                      "type": "string",
                                      "description": "",
                                      "default": ""
                                    },
                                    "id": {
                                      "type": "string",
                                      "description": "",
                                      "default": ""
                                    },
                                    "version": {
                                      "type": "string",
                                      "description": "",
                                      "default": ""
                                    },
                                    "author": {
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
                                    "scores": {
                                      "$ref": "#/components/schemas/SocketScore"
                                    },
                                    "artifactId": {
                                      "type": "string",
                                      "description": "",
                                      "default": "",
                                      "nullable": true
                                    },
                                    "capabilities": {
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
                                      ],
                                      "nullable": true
                                    }
                                  },
                                  "required": [
                                    "artifactId",
                                    "author",
                                    "capabilities",
                                    "id",
                                    "license",
                                    "name",
                                    "namespace",
                                    "scores",
                                    "type",
                                    "version"
                                  ]
                                }
                              },
                              "required": [
                                "action",
                                "actionSourceType",
                                "artifact",
                                "branch",
                                "dependency",
                                "licenseViolation",
                                "patch",
                                "prioritization",
                                "reachability",
                                "repository"
                              ]
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "category",
                          "clearedAt",
                          "createdAt",
                          "dashboardUrl",
                          "description",
                          "fix",
                          "id",
                          "key",
                          "locations",
                          "severity",
                          "status",
                          "title",
                          "type",
                          "updatedAt",
                          "version",
                          "vulnerability"
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
                            "alertClearedAt.eq": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertClearedAt.lt": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertClearedAt.lte": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertClearedAt.gt": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertClearedAt.gte": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert cleared at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertCreatedAt.eq": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertCreatedAt.lt": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertCreatedAt.lte": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertCreatedAt.gt": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertCreatedAt.gte": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert created at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
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
                            "alertStatus": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "A single alert status (\"open\" or \"cleared\")"
                            },
                            "alertStatus.notIn": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "A single alert status (\"open\" or \"cleared\")"
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
                            "alertUpdatedAt.eq": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertUpdatedAt.lt": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertUpdatedAt.lte": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertUpdatedAt.gt": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
                            },
                            "alertUpdatedAt.gte": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": "Alert updated at (YYYY-MM-DD HH:MM:SS in UTC time zone)"
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
                        "filters",
                        "organizationId",
                        "queryStartTimestamp"
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
            "description": "The paginated array of alert items for the organization and related metadata."
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