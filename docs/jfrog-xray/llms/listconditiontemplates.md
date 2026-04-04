# Source: https://docs.jfrog.com/security/reference/listconditiontemplates.md

# List condition templates

Get the available condition templates with their parameters. Every custom condition is built from a single template identified by `condition_template_id` and a set of parameter values.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Curation API",
    "description": "Public REST API for JFrog Curation — policy-based governance of open-source\npackages flowing through JFrog Artifactory remote repositories.\n\nCuration lets you define **conditions** (e.g. \"package has a critical CVE\")\nand attach them to **policies** that either block or audit (dry-run)\nnon-compliant packages. **Waiver requests** allow users to request\nunblocking of a package, and the **audit** endpoint provides full export of\nall approved/blocked events.\n",
    "version": "1.0.0",
    "license": {
      "name": "Proprietary"
    },
    "contact": {
      "name": "JFrog"
    }
  },
  "servers": [
    {
      "url": "{protocol}://{host}:{port}/xray",
      "description": "JFrog Platform (Xray service)",
      "variables": {
        "protocol": {
          "default": "https",
          "enum": [
            "http",
            "https"
          ]
        },
        "host": {
          "default": "localhost"
        },
        "port": {
          "default": "8046"
        }
      }
    }
  ],
  "security": [],
  "tags": [
    {
      "name": "Conditions",
      "description": "Condition templates and custom conditions used by policies."
    }
  ],
  "paths": {
    "/api/v1/curation/condition_templates": {
      "get": {
        "operationId": "listConditionTemplates",
        "tags": [
          "Conditions"
        ],
        "summary": "List condition templates",
        "description": "Get the available condition templates with their parameters. Every custom condition is built from a single template identified by `condition_template_id` and a set of parameter values.",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "data",
                    "total_count"
                  ],
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/ConditionTemplate"
                      }
                    },
                    "total_count": {
                      "type": "integer",
                      "description": "Total number of available templates."
                    }
                  }
                },
                "example": {
                  "data": [
                    {
                      "condition_template_id": "CVECVSSRange",
                      "name": "Package has vulnerability with CVSS score in range {range}",
                      "risk_type": "security",
                      "supported_pkg_types": [
                        "npm",
                        "PyPI",
                        "Maven",
                        "Go",
                        "NuGet",
                        "Conan",
                        "Gems",
                        "Gradle"
                      ],
                      "params": [
                        {
                          "param_id": "vulnerability_cvss_score_range"
                        },
                        {
                          "param_id": "epss",
                          "is_optional": true
                        },
                        {
                          "param_id": "apply_only_if_fix_is_available",
                          "is_optional": true
                        },
                        {
                          "param_id": "do_not_apply_for_already_existing_vulnerabilities",
                          "is_optional": true
                        }
                      ]
                    },
                    {
                      "condition_template_id": "isImmature",
                      "name": "Package version is immature",
                      "risk_type": "operational",
                      "supported_pkg_types": [
                        "npm",
                        "PyPI",
                        "Maven",
                        "Go",
                        "NuGet",
                        "Conan",
                        "Gems",
                        "Gradle"
                      ],
                      "params": [
                        {
                          "param_id": "package_age_days"
                        },
                        {
                          "param_id": "vulnerability_cvss_score",
                          "is_optional": true
                        }
                      ]
                    }
                  ],
                  "total_count": 2
                }
              }
            }
          },
          "400": {
            "$ref": "#/components/responses/BadRequest"
          }
        }
      }
    }
  },
  "components": {
    "responses": {
      "BadRequest": {
        "description": "Bad request — validation error or invalid parameters.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/Error"
            }
          }
        }
      }
    },
    "schemas": {
      "RiskType": {
        "type": "string",
        "enum": [
          "security",
          "legal",
          "operational"
        ]
      },
      "PackageType": {
        "type": "string",
        "enum": [
          "npm",
          "PyPI",
          "Maven",
          "Go",
          "NuGet",
          "Conan",
          "Gems",
          "Gradle",
          "HuggingFaceML",
          "Docker"
        ],
        "description": "Supported package types. Additional types may be added in the future."
      },
      "ConditionTemplate": {
        "type": "object",
        "required": [
          "condition_template_id",
          "name",
          "risk_type",
          "supported_pkg_types",
          "params"
        ],
        "properties": {
          "condition_template_id": {
            "type": "string",
            "description": "Unique template identifier (e.g. `CVECVSSRange`, `isImmature`)."
          },
          "name": {
            "type": "string",
            "description": "Human-readable template name."
          },
          "risk_type": {
            "$ref": "#/components/schemas/RiskType"
          },
          "supported_pkg_types": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PackageType"
            },
            "description": "Package types that conditions created from this template can support. A custom condition may use a subset."
          },
          "params": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ConditionTemplateParam"
            }
          }
        }
      },
      "ConditionTemplateParam": {
        "type": "object",
        "required": [
          "param_id"
        ],
        "properties": {
          "param_id": {
            "type": "string",
            "description": "Parameter identifier."
          },
          "is_optional": {
            "type": "boolean",
            "description": "If `true`, the parameter is optional when creating a condition from this template. If absent, the parameter is required."
          }
        }
      },
      "Error": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Error message."
          }
        }
      }
    }
  }
}
```