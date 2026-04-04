# Source: https://docs.jfrog.com/security/reference/get-policy-by-name.md

# Get Policy

Returns the details of a specific policy by name, including its rules, criteria, actions, and metadata (author, created/modified timestamps, assigned watches).

Requires the Read Policies role to be set on the User or Group level. For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can get a policy by using the additional query parameter `projectKey`. When `projectKey` is provided, the policy is looked up in both the project scope and globally.


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
    "/api/v1/policies/{name}": {
      "get": {
        "operationId": "get-policy-by-name",
        "summary": "Get Policy",
        "description": "Returns the details of a specific policy by name, including its rules, criteria, actions, and metadata (author, created/modified timestamps, assigned watches).\n\nRequires the Read Policies role to be set on the User or Group level. For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can get a policy by using the additional query parameter `projectKey`. When `projectKey` is provided, the policy is looked up in both the project scope and globally.\n",
        "tags": [
          "Policies V1"
        ],
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The name of the policy to retrieve.",
            "example": "sec-policy"
          },
          {
            "name": "projectKey",
            "in": "query",
            "required": false,
            "description": "When provided, looks up the policy in the scope of the specified project as well as globally. Requires Xray 3.21.2+ with Projects enabled.\n",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "include_notify",
            "in": "query",
            "required": false,
            "description": "When set to true, includes notification-related action fields in the response.\n",
            "schema": {
              "type": "string",
              "enum": [
                "true",
                "false"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved the policy.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PolicyApiResponse"
                },
                "example": {
                  "name": "sec-policy",
                  "type": "security",
                  "description": "Block critical vulnerabilities",
                  "author": "admin",
                  "rules": [
                    {
                      "name": "sec_rule",
                      "priority": 1,
                      "criteria": {
                        "min_severity": "all severities"
                      },
                      "actions": {
                        "webhooks": [
                          "sec_webhook"
                        ],
                        "fail_build": true,
                        "block_download": {
                          "unscanned": true,
                          "active": true,
                          "grace_period_days": 0
                        }
                      }
                    }
                  ],
                  "created": "2019-12-19T09:17:09.562Z",
                  "modified": "2024-01-15T10:30:00.000Z",
                  "watches": [
                    "prod-watch"
                  ],
                  "project_key": ""
                }
              }
            }
          },
          "400": {
            "description": "Empty policy name.",
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
                  "error": "Empty policy name"
                }
              }
            }
          },
          "404": {
            "description": "Policy not found or not accessible in the current scope.",
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
                  "error": "Failed to get policy by name sec-policy : Policy was not found"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error while retrieving the policy.",
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
                  "error": "Failed to get policy by name sec-policy"
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
      "PolicyCriteria": {
        "type": "object",
        "description": "Criteria that determine which issues trigger the rule. The available fields depend on the policy type. For security policies use min_severity, cvss_range, vulnerability_ids, etc. For license policies use allow_licenses, banned_licenses, etc. For operational_risk policies use op_risk_min_risk, op_risk_custom, etc.\n",
        "properties": {
          "min_severity": {
            "type": "string",
            "description": "Minimum severity of vulnerabilities to match. Applies to security and exposures policy types.\n",
            "enum": [
              "critical",
              "high",
              "medium",
              "low",
              "all severities"
            ],
            "example": "High"
          },
          "cvss_range": {
            "$ref": "#/components/schemas/PolicyCvssRange"
          },
          "vulnerability_ids": {
            "type": "array",
            "description": "Match specific CVEs and/or XRAY IDs. A CVE identifier has the format CVE-YYYY-NNNNN, an XRAY ID has the format XRAY-NNNNNN.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "CVE-2022-23307",
              "XRAY-23432"
            ]
          },
          "fix_version_dependant": {
            "type": "boolean",
            "description": "Only match when a fixed version is available."
          },
          "applicable_cves_only": {
            "type": "boolean",
            "description": "Only match CVEs determined to be applicable by contextual analysis."
          },
          "malicious_package": {
            "type": "boolean",
            "description": "Match packages identified as malicious."
          },
          "exposures": {
            "$ref": "#/components/schemas/PolicyExposures"
          },
          "package_name": {
            "type": "string",
            "description": "Filter by specific package name. The name format varies between package types.\n",
            "example": "log4j-core"
          },
          "package_type": {
            "type": "string",
            "description": "Filter by package type.",
            "enum": [
              "maven",
              "docker",
              "npm",
              "pypi",
              "nuget",
              "rpm",
              "conan",
              "debian",
              "rubygems",
              "generic",
              "golang",
              "conda",
              "composer",
              "alpine",
              "cargo",
              "cran",
              "terraformbe",
              "bower",
              "huggingface",
              "oci"
            ],
            "example": "maven"
          },
          "package_versions": {
            "type": "array",
            "description": "Filter by specific package versions. Supports exact versions and ranges. Any version: (,). Specific version: [v1]. Ranges: (v1,v2) open interval, [v1,v2] closed interval, (v1,v2] and [v1,v2) half-open intervals.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "[1.1,1.3]"
            ]
          },
          "allow_licenses": {
            "type": "array",
            "description": "List of allowed licenses for license-type policies. Components with licenses not in this list will trigger the rule.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "GPL-3.0",
              "MIT"
            ]
          },
          "allowed_licenses": {
            "type": "array",
            "description": "List of allowed licenses (alias for allow_licenses).\n",
            "items": {
              "type": "string"
            },
            "example": [
              "BSD",
              "AAL"
            ]
          },
          "allow_unknown": {
            "type": "boolean",
            "description": "Whether to allow components with unknown licenses.",
            "example": true
          },
          "banned_licenses": {
            "type": "array",
            "description": "List of banned licenses. Components with these licenses will trigger the rule.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "GPL-3.0"
            ]
          },
          "multi_license_permissive": {
            "type": "boolean",
            "description": "Use permissive approach for components with multiple licenses.\n"
          },
          "op_risk_min_risk": {
            "type": "string",
            "description": "Minimum operational risk level to match.",
            "enum": [
              "high",
              "medium",
              "low"
            ],
            "example": "medium"
          },
          "op_risk_custom": {
            "$ref": "#/components/schemas/PolicyOpRiskCustom"
          }
        }
      },
      "PolicyCvssRange": {
        "type": "object",
        "description": "CVSS score range for filtering vulnerabilities.",
        "properties": {
          "from": {
            "type": "string",
            "description": "Start of CVSS score range (0.0 - 10.0).",
            "example": "6.3"
          },
          "to": {
            "type": "string",
            "description": "End of CVSS score range (0.0 - 10.0).",
            "example": "9.0"
          }
        }
      },
      "PolicyExposures": {
        "type": "object",
        "description": "Criteria for matching exposures (contextual analysis findings). Enable specific categories to scope which exposure types trigger the rule.\n",
        "properties": {
          "min_severity": {
            "type": "string",
            "description": "Minimum severity of exposures to match.",
            "enum": [
              "critical",
              "high",
              "medium",
              "low",
              "all severities"
            ],
            "example": "high"
          },
          "applications": {
            "type": "boolean",
            "description": "Apply criteria to the applications exposure category."
          },
          "iac": {
            "type": "boolean",
            "description": "Apply criteria to the Infrastructure as Code (IaC) exposure category."
          },
          "malicious_code": {
            "type": "boolean",
            "description": "Apply criteria to the malicious code exposure category."
          },
          "secrets": {
            "type": "boolean",
            "description": "Apply criteria to the secrets exposure category."
          },
          "services": {
            "type": "boolean",
            "description": "Apply criteria to the services exposure category."
          }
        }
      },
      "PolicyOpRiskCustom": {
        "type": "object",
        "description": "Custom operational risk criteria. Use use_and_condition or use_or_condition to combine multiple conditions.\n",
        "properties": {
          "op_risk_min_risk": {
            "type": "string",
            "description": "Minimum operational risk level.",
            "enum": [
              "high",
              "medium",
              "low"
            ]
          },
          "use_and_condition": {
            "type": "boolean",
            "description": "When true, all custom conditions must be met (AND logic). When false, any single condition triggers the rule (OR logic).\n"
          },
          "is_eol": {
            "type": "boolean",
            "description": "Match packages that have reached end of life."
          },
          "commits_less_than": {
            "type": "integer",
            "description": "Match packages with fewer commits per year than this value.",
            "enum": [
              10,
              25,
              50,
              100
            ]
          },
          "newer_versions_greater_than": {
            "type": "integer",
            "description": "Match packages where newer versions exceed this count.",
            "enum": [
              1,
              2,
              3,
              4,
              5
            ]
          },
          "committers_less_than": {
            "type": "integer",
            "description": "Match packages with fewer committers per year than this value.",
            "enum": [
              1,
              2,
              3,
              4,
              5
            ]
          },
          "release_date_greater_than_months": {
            "type": "integer",
            "description": "Match packages with a release date older than this many months.",
            "enum": [
              6,
              12,
              18,
              24,
              30,
              36
            ]
          },
          "release_cadence_per_year_less_than": {
            "type": "integer",
            "description": "Match packages with fewer releases per year than this value.",
            "enum": [
              1,
              2,
              3,
              4,
              5
            ]
          },
          "risk": {
            "type": "string",
            "description": "Minimum operational risk level.",
            "enum": [
              "high",
              "medium",
              "low"
            ]
          }
        }
      },
      "PolicyBlockDownload": {
        "type": "object",
        "description": "Controls whether artifact downloads are blocked.",
        "properties": {
          "active": {
            "type": "boolean",
            "description": "Block download of artifacts that match the rule.",
            "example": true
          },
          "unscanned": {
            "type": "boolean",
            "description": "Block download of artifacts that have not been scanned.",
            "example": true
          },
          "grace_period_days": {
            "type": "integer",
            "description": "Grace period in days before blocking takes effect. Allows time to address the issue.\n",
            "example": 5
          }
        }
      },
      "PolicyApiResponse": {
        "type": "object",
        "description": "A policy object as returned by the v1 GET endpoints. Includes read-only fields (author, created, modified) in addition to the fields used for creation.\n",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the policy.",
            "example": "sec-policy"
          },
          "type": {
            "type": "string",
            "description": "The policy type.",
            "enum": [
              "security",
              "license",
              "operational_risk"
            ],
            "example": "security"
          },
          "description": {
            "type": "string",
            "description": "Description of the policy.",
            "example": "Block critical vulnerabilities"
          },
          "author": {
            "type": "string",
            "description": "The user who created the policy.",
            "example": "admin"
          },
          "rules": {
            "type": "array",
            "description": "The rules defined in this policy.",
            "items": {
              "$ref": "#/components/schemas/PolicyApiRuleResponse"
            }
          },
          "created": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp when the policy was created. RFC 3339 format.\n",
            "example": "2019-12-19T09:17:09.562Z"
          },
          "modified": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp when the policy was last modified. RFC 3339 format.\n",
            "example": "2024-01-15T10:30:00.000Z"
          },
          "watches": {
            "type": "array",
            "description": "Names of watches this policy is assigned to.",
            "items": {
              "type": "string"
            },
            "example": [
              "prod-watch",
              "staging-watch"
            ]
          },
          "project_key": {
            "type": "string",
            "description": "The project key if this is a project-scoped policy. Empty for global policies.\n",
            "example": "myproj"
          }
        }
      },
      "PolicyApiRuleResponse": {
        "type": "object",
        "description": "A rule within a policy (v1 response format).",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the rule.",
            "example": "sec_rule"
          },
          "priority": {
            "type": "integer",
            "description": "Priority for ordering between rules.",
            "example": 1
          },
          "criteria": {
            "$ref": "#/components/schemas/PolicyCriteria"
          },
          "actions": {
            "$ref": "#/components/schemas/PolicyApiActionsResponse"
          }
        }
      },
      "PolicyApiActionsResponse": {
        "type": "object",
        "description": "Actions configured for a v1 policy rule. Note: v1 actions do not include block_release_bundle_distribution, block_release_bundle_promotion, create_ticket_enabled, or build_failure_grace_period_in_days — those are available in v2 only.\n",
        "properties": {
          "mails": {
            "type": "array",
            "description": "Email addresses to notify.",
            "items": {
              "type": "string"
            },
            "example": [
              "security-team@example.com"
            ]
          },
          "webhooks": {
            "type": "array",
            "description": "Webhook names to invoke.",
            "items": {
              "type": "string"
            },
            "example": [
              "sec_webhook"
            ]
          },
          "fail_build": {
            "type": "boolean",
            "description": "Whether builds are failed when this rule triggers.",
            "example": true
          },
          "block_download": {
            "$ref": "#/components/schemas/PolicyBlockDownload"
          },
          "custom_severity": {
            "type": "string",
            "description": "Overridden severity for the generated violation.\n",
            "enum": [
              "critical",
              "high",
              "medium",
              "low"
            ]
          },
          "notify_watch_recipients": {
            "type": "boolean",
            "description": "Whether watch subscribers are notified."
          },
          "notify_deployer": {
            "type": "boolean",
            "description": "Whether the deployer is notified."
          }
        }
      }
    }
  },
  "tags": [
    {
      "name": "Policies V1",
      "description": "APIs from Policies V1"
    }
  ]
}
```