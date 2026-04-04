# Source: https://docs.jfrog.com/security/reference/update-policy.md

# Update Policy

Updates an existing policy. The policy name in the URL path is authoritative — it overrides any `name` field in the request body. The full policy definition must be provided (this is a full replacement, not a partial update).

Requires the "Manage Policies" role to be set on the User or Group level. For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can update a policy in the scope of a project by using the additional query parameter `projectKey`.


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
      "put": {
        "operationId": "update-policy",
        "summary": "Update Policy",
        "description": "Updates an existing policy. The policy name in the URL path is authoritative — it overrides any `name` field in the request body. The full policy definition must be provided (this is a full replacement, not a partial update).\n\nRequires the \"Manage Policies\" role to be set on the User or Group level. For Xray version 3.21.2 and above with Projects, a Project Admin with Manage Security Assets privilege can update a policy in the scope of a project by using the additional query parameter `projectKey`.\n",
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
            "description": "The name of the policy to update. This value takes precedence over any name in the request body.\n",
            "example": "sec-policy"
          },
          {
            "name": "projectKey",
            "in": "query",
            "required": false,
            "description": "When provided, the update is scoped to the specified project. Requires Xray 3.21.2+ with Projects enabled.\n",
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
                "$ref": "#/components/schemas/PoliciesPolicyMutationRequest"
              },
              "examples": {
                "updateSeverity": {
                  "summary": "Update minimum severity to medium",
                  "value": {
                    "name": "sec-policy",
                    "type": "security",
                    "description": "Updated security policy",
                    "rules": [
                      {
                        "name": "sec_rule",
                        "priority": 1,
                        "criteria": {
                          "min_severity": "medium"
                        },
                        "actions": {
                          "webhooks": [
                            "sec_webhook"
                          ],
                          "fail_build": true,
                          "block_download": {
                            "active": true,
                            "unscanned": true
                          }
                        }
                      }
                    ]
                  }
                },
                "updateCveList": {
                  "summary": "Target specific CVEs",
                  "value": {
                    "name": "sec-policy",
                    "type": "security",
                    "description": "Block specific CVEs",
                    "rules": [
                      {
                        "name": "cve_rule",
                        "priority": 1,
                        "criteria": {
                          "vulnerability_ids": [
                            "CVE-2022-23307",
                            "CVE-2022-23305",
                            "XRAY-23432"
                          ]
                        },
                        "actions": {
                          "fail_build": true,
                          "notify_deployer": true,
                          "notify_watch_recipients": true
                        }
                      }
                    ]
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Policy updated successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string",
                      "description": "Success message."
                    }
                  }
                },
                "example": {
                  "info": "Policy edited successfully"
                }
              }
            }
          },
          "400": {
            "description": "Policy name is empty or the policy is not valid.\n",
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
                  "error": "Found Invalid Policy: Mandatory fields are missing"
                }
              }
            }
          },
          "403": {
            "description": "Permission denied, or attempting to use a license-type policy without the required license entitlement.\n",
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
                  "error": "cannot create license policy with existing jfrog license"
                }
              }
            }
          },
          "404": {
            "description": "Policy not found.",
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
          "415": {
            "description": "Failed to parse the request body.",
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
                  "error": "Failed to parse request"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error while updating the policy.",
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
                  "error": "Failed to edit Policy"
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
      "PoliciesPolicyMutationRequest": {
        "type": "object",
        "description": "Request body for creating or updating a policy. A policy defines rules that determine how Xray identifies and acts on issues found during scanning. Each policy has a type (security, license, or operational_risk) and contains one or more rules. Each rule has criteria (what to match) and actions (what to do when matched).\n",
        "required": [
          "name",
          "type",
          "rules"
        ],
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the policy. Must be unique across the system (or within a project when using projectKey).\n",
            "example": "my-security-policy"
          },
          "description": {
            "type": "string",
            "description": "Optional free-text description of the policy.",
            "example": "Block critical vulnerabilities in production repos"
          },
          "type": {
            "type": "string",
            "description": "The policy type. Determines which criteria fields are available in the rules.\n",
            "enum": [
              "security",
              "license",
              "operational_risk"
            ],
            "example": "security"
          },
          "rules": {
            "type": "array",
            "description": "One or more rules that define the policy behavior. Each rule specifies criteria to match and actions to take when matched.\n",
            "items": {
              "$ref": "#/components/schemas/PolicyRule"
            }
          }
        }
      },
      "PolicyRule": {
        "type": "object",
        "description": "A single rule within a policy. Contains criteria for matching issues and actions to execute when criteria are met.\n",
        "required": [
          "name",
          "criteria",
          "actions"
        ],
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the rule.",
            "example": "critical-vuln-rule"
          },
          "priority": {
            "type": "integer",
            "description": "Priority for ordering between rules. Lower numbers indicate higher priority.\n",
            "example": 1
          },
          "criteria": {
            "$ref": "#/components/schemas/PolicyCriteria"
          },
          "actions": {
            "$ref": "#/components/schemas/PolicyActions"
          }
        }
      },
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
      "PolicyActions": {
        "type": "object",
        "description": "Actions to execute when a rule's criteria are matched. Multiple actions can be combined.\n",
        "properties": {
          "custom_severity": {
            "type": "string",
            "description": "Override the severity of the generated violation. Applies only to Operational Risk and License type policies.\n",
            "enum": [
              "critical",
              "high",
              "medium",
              "low"
            ],
            "example": "high"
          },
          "webhooks": {
            "type": "array",
            "description": "Webhook names to invoke when the rule is triggered.",
            "items": {
              "type": "string"
            },
            "example": [
              "sec_webhook"
            ]
          },
          "notify_watch_recipients": {
            "type": "boolean",
            "description": "Notify users subscribed to the watch.",
            "example": true
          },
          "notify_deployer": {
            "type": "boolean",
            "description": "Notify the user who deployed the artifact.",
            "example": true
          },
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
          "create_ticket_enabled": {
            "type": "boolean",
            "description": "Automatically create a Jira ticket for the violation. Requires a configured Jira integration.\n"
          },
          "block_download": {
            "$ref": "#/components/schemas/PolicyBlockDownload"
          },
          "block_release_bundle_distribution": {
            "type": "boolean",
            "description": "Block distribution of release bundles that match the rule."
          },
          "block_release_bundle_promotion": {
            "type": "boolean",
            "description": "Block promotion of release bundles that match the rule."
          },
          "fail_build": {
            "type": "boolean",
            "description": "Fail the build if the rule is triggered.",
            "example": true
          },
          "build_failure_grace_period_in_days": {
            "type": "integer",
            "description": "Grace period in days before the build is failed. Allows time to address the issue without immediately blocking CI/CD.\n",
            "example": 5
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