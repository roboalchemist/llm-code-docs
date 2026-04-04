# Source: https://docs.jfrog.com/security/reference/listconditions.md

# List conditions

Get both built-in and custom conditions with pagination and filtering.

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
    "/api/v1/curation/conditions": {
      "get": {
        "operationId": "listConditions",
        "tags": [
          "Conditions"
        ],
        "summary": "List conditions",
        "description": "Get both built-in and custom conditions with pagination and filtering.",
        "parameters": [
          {
            "$ref": "#/components/parameters/OrderBy"
          },
          {
            "$ref": "#/components/parameters/Direction"
          },
          {
            "$ref": "#/components/parameters/NumOfRows"
          },
          {
            "$ref": "#/components/parameters/PageNum"
          },
          {
            "$ref": "#/components/parameters/Offset"
          },
          {
            "name": "name",
            "in": "query",
            "description": "Filter by condition name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "is_custom",
            "in": "query",
            "description": "Filter by built-in (`false`) or custom (`true`) conditions.",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "condition_template_id",
            "in": "query",
            "description": "Filter by the template used to create the condition.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "risk_type",
            "in": "query",
            "description": "Filter by risk type. One of: `security`, `legal`, `operational`.",
            "schema": {
              "$ref": "#/components/schemas/RiskType"
            }
          },
          {
            "name": "supported_pkg_types",
            "in": "query",
            "description": "Filter by supported package type.",
            "schema": {
              "$ref": "#/components/schemas/PackageType"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "data",
                    "meta"
                  ],
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Condition"
                      }
                    },
                    "meta": {
                      "$ref": "#/components/schemas/PaginationMeta"
                    }
                  }
                },
                "example": {
                  "data": [
                    {
                      "id": "14",
                      "is_custom": false,
                      "created_at": "2023-08-01T03:00:00+03:00",
                      "updated_at": "2023-08-01T03:00:00+03:00",
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
                      "on_demand": false,
                      "condition_template_id": "isImmature",
                      "name": "Package version is immature (permissive)",
                      "param_values": [
                        {
                          "param_id": "package_age_days",
                          "value": 2
                        }
                      ]
                    }
                  ],
                  "meta": {
                    "total_count": 1,
                    "result_count": 1,
                    "order_by": "updated_at",
                    "direction": "desc",
                    "num_of_rows": 15,
                    "page_num": 1
                  }
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
    "parameters": {
      "OrderBy": {
        "name": "order_by",
        "in": "query",
        "description": "Field used for sorting. Supported values depend on the endpoint; common values are `id` and `updated_at`.",
        "schema": {
          "type": "string",
          "default": "updated_at"
        }
      },
      "Direction": {
        "name": "direction",
        "in": "query",
        "description": "Sorting direction: `asc` or `desc`.",
        "schema": {
          "type": "string",
          "enum": [
            "asc",
            "desc"
          ],
          "default": "desc"
        }
      },
      "NumOfRows": {
        "name": "num_of_rows",
        "in": "query",
        "description": "Number of rows per page.",
        "schema": {
          "type": "integer",
          "default": 15
        }
      },
      "PageNum": {
        "name": "page_num",
        "in": "query",
        "description": "Page number (1-based).",
        "schema": {
          "type": "integer",
          "default": 1
        }
      },
      "Offset": {
        "name": "offset",
        "in": "query",
        "description": "Alternative to `page_num` — pagination offset (0-based).",
        "schema": {
          "type": "integer",
          "default": 0
        }
      }
    },
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
      "EditableCondition": {
        "type": "object",
        "required": [
          "name"
        ],
        "description": "Mutable fields for creating or updating a custom condition. `condition_template_id` is required when creating a new condition but absent on built-in conditions.",
        "properties": {
          "condition_template_id": {
            "type": "string",
            "description": "Template ID from the List Condition Templates endpoint."
          },
          "name": {
            "type": "string",
            "description": "Display name for the condition."
          },
          "param_values": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ParamValue"
            },
            "description": "Parameter values required by the condition template."
          }
        }
      },
      "Condition": {
        "description": "A condition (built-in or custom).",
        "allOf": [
          {
            "type": "object",
            "required": [
              "id",
              "is_custom",
              "risk_type",
              "supported_pkg_types"
            ],
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique condition identifier."
              },
              "is_custom": {
                "type": "boolean",
                "description": "`false` for built-in immutable conditions, `true` for user-created custom conditions."
              },
              "created_by": {
                "type": "string",
                "description": "Username of the creator (custom conditions only)."
              },
              "created_at": {
                "type": "string",
                "format": "date-time"
              },
              "updated_by": {
                "type": "string",
                "description": "Username of the last updater (custom conditions only)."
              },
              "updated_at": {
                "type": "string",
                "format": "date-time"
              },
              "risk_type": {
                "$ref": "#/components/schemas/RiskType"
              },
              "supported_pkg_types": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/PackageType"
                }
              },
              "on_demand": {
                "type": "boolean",
                "description": "Whether the condition is evaluated on-demand rather than proactively."
              }
            }
          },
          {
            "$ref": "#/components/schemas/EditableCondition"
          }
        ]
      },
      "ParamValue": {
        "type": "object",
        "required": [
          "param_id",
          "value"
        ],
        "properties": {
          "param_id": {
            "type": "string",
            "description": "A `param_id` that is valid for the condition's `condition_template_id`."
          },
          "value": {
            "$ref": "#/components/schemas/ParamValueVariant"
          }
        }
      },
      "ParamValueVariant": {
        "description": "The value type depends on the `param_id`:\n\n| param_id | Type | Example |\n|----------|------|---------|\n| `vulnerability_cvss_score_range` | array of 2 numbers (0–10) | `[7.0, 10]` |\n| `vulnerability_cvss_score` | number (0–10) | `7.0` |\n| `package_age_days` | integer (0–100) | `14` |\n| `cve_name` | string | `\"CVE-2025-12345\"` |\n| `apply_only_if_fix_is_available` | boolean | `true` |\n| `do_not_apply_for_already_existing_vulnerabilities` | boolean | `false` |\n| `block_in_case_check_value_is_missing` | boolean | `true` |\n| `multiple_license_permissive_approach` | boolean | `true` |\n| `list_of_package_licenses` | array of strings | `[\"MIT\", \"Apache-2.0\"]` |\n| `list_of_labels` | array of strings | `[\"Manual\", \"Approved\"]` |\n| `list_of_scorecard_checks` | array of objects | `[{\"checkName\": \"Maintained\", \"checkValue\": 5}]` |\n| `epss` | object | `{\"field_name\": \"score\", \"value\": 0.5}` |\n| `package_versions` | object (version range) | `{\"gte\": \"3.6.1\", \"lt\": \"3.7.1\"}` |\n| `package_type` | string | `\"npm\"` |\n| `package_name` | string | `\"lodash\"` |\n",
        "oneOf": [
          {
            "type": "number",
            "title": "NumericValue",
            "description": "Used for `vulnerability_cvss_score`, `package_age_days`, `vulnerability_cvss_score_range` element."
          },
          {
            "type": "boolean",
            "title": "BooleanValue",
            "description": "Used for `apply_only_if_fix_is_available`, `do_not_apply_for_already_existing_vulnerabilities`, `block_in_case_check_value_is_missing`, `multiple_license_permissive_approach`."
          },
          {
            "type": "string",
            "title": "StringValue",
            "description": "Used for `cve_name`, `package_type`, `package_name`."
          },
          {
            "type": "array",
            "title": "NumberArrayValue",
            "description": "Used for `vulnerability_cvss_score_range`. Array of exactly two numbers, each between 0 and 10.",
            "items": {
              "type": "number"
            }
          },
          {
            "type": "array",
            "title": "StringArrayValue",
            "description": "Used for `list_of_package_licenses`, `list_of_labels`.",
            "items": {
              "type": "string"
            }
          },
          {
            "type": "array",
            "title": "ScorecardChecksArray",
            "description": "Used for `list_of_scorecard_checks`.",
            "items": {
              "$ref": "#/components/schemas/ScorecardCheck"
            }
          },
          {
            "$ref": "#/components/schemas/EpssValue"
          },
          {
            "$ref": "#/components/schemas/PackageVersionRange"
          }
        ]
      },
      "ScorecardCheck": {
        "type": "object",
        "required": [
          "checkName",
          "checkValue"
        ],
        "properties": {
          "checkName": {
            "type": "string",
            "description": "One of the OpenSSF scorecard checks: `Aggregated score`, `Binary-Artifacts`, `Branch-Protection`, `CII-Best-Practices`, `Code-Review`, `Dangerous-Workflow`, `Fuzzing`, `License`, `Maintained`, `Packaging`, `Pinned-Dependencies`, `SAST`, `Security-Policy`, `Signed-Releases`, `Token-Permissions`, `Vulnerabilities`.",
            "enum": [
              "Aggregated score",
              "Binary-Artifacts",
              "Branch-Protection",
              "CII-Best-Practices",
              "Code-Review",
              "Dangerous-Workflow",
              "Fuzzing",
              "License",
              "Maintained",
              "Packaging",
              "Pinned-Dependencies",
              "SAST",
              "Security-Policy",
              "Signed-Releases",
              "Token-Permissions",
              "Vulnerabilities"
            ]
          },
          "checkValue": {
            "type": "number",
            "description": "Score threshold (0–10, exclusive). Integer for individual checks; one decimal place allowed for `Aggregated score`."
          }
        }
      },
      "EpssValue": {
        "type": "object",
        "title": "EpssValue",
        "description": "Used for the `epss` parameter. Filters by EPSS score or percentile.",
        "required": [
          "field_name",
          "value"
        ],
        "properties": {
          "field_name": {
            "type": "string",
            "enum": [
              "score",
              "percentile"
            ],
            "description": "`score` (0–1, exclusive) or `percentile` (0–100, exclusive)."
          },
          "value": {
            "type": "number",
            "description": "Threshold value. Range depends on `field_name`."
          }
        }
      },
      "PackageVersionRange": {
        "type": "object",
        "title": "PackageVersionRange",
        "description": "Used for the `package_versions` parameter. Specifies which versions\nto match. Exactly one of the following patterns:\n- `{\"in\": [\"3.6.1\", \"3.7.1\"]}` — exact list\n- `{\"gt\": \"3.6.1\"}` or `{\"gte\": \"3.6.1\"}` — greater than\n- `{\"lt\": \"3.7.1\"}` or `{\"lte\": \"3.7.1\"}` — less than\n- Combinations of `gt`/`gte` with `lt`/`lte` — range\n- `{\"any\": \"\"}` — all versions\n",
        "properties": {
          "in": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Exact list of versions."
          },
          "gt": {
            "type": "string",
            "description": "Greater than (exclusive)."
          },
          "gte": {
            "type": "string",
            "description": "Greater than or equal."
          },
          "lt": {
            "type": "string",
            "description": "Less than (exclusive)."
          },
          "lte": {
            "type": "string",
            "description": "Less than or equal."
          },
          "any": {
            "type": "string",
            "description": "Set to empty string `\"\"` to match all versions."
          }
        }
      },
      "PaginationMeta": {
        "type": "object",
        "properties": {
          "total_count": {
            "type": "integer",
            "description": "Total objects matching the filter. May be absent if not requested."
          },
          "result_count": {
            "type": "integer",
            "description": "Number of objects in this page."
          },
          "order_by": {
            "type": "string"
          },
          "direction": {
            "type": "string",
            "enum": [
              "asc",
              "desc"
            ]
          },
          "num_of_rows": {
            "type": "integer"
          },
          "page_num": {
            "type": "integer"
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