# Source: https://docs.socket.dev/reference/fetch-fixes.md

# Fetch fixes for vulnerabilities in a repository or scan

Fetches available fixes for vulnerabilities in a repository or scan.
Requires either repo_slug or full_scan_id as well as vulnerability_ids to be provided.
vulnerability_ids can be a comma-separated list of GHSA or CVE IDs, or "*" for all vulnerabilities.

## Response Structure

The response contains a `fixDetails` object where each key is a vulnerability ID (GHSA or CVE) and the value is a discriminated union based on the `type` field.

### Common Fields

All response variants include:
- `type`: Discriminator field (one of: "fixFound", "partialFixFound", "noFixAvailable", "fixNotApplicable", "errorComputingFix")
- `value`: Object containing the variant-specific data

The `value` object always contains:
- `ghsa`: string | null - The GHSA ID
- `cve`: string | null - The CVE ID (if available)
- `advisoryDetails`: object | null - Advisory details (only if include_details=true)

### Response Variants

**fixFound**: A complete fix is available for all vulnerable packages
- `value.fixDetails.fixes`: Array of fix objects, each containing:
  - `purl`: Package URL to upgrade
  - `fixedVersion`: Version to upgrade to
  - `manifestFiles`: Array of manifest files containing the package
  - `updateType`: "patch" | "minor" | "major" | "unknown"
- `value.fixDetails.responsibleDirectDependencies`: (optional) Map of direct dependencies responsible for the vulnerability

**partialFixFound**: Fixes available for some but not all vulnerable packages
- Same as fixFound, plus:
- `value.fixDetails.unfixablePurls`: Array of packages that cannot be fixed, each containing:
  - `purl`: Package URL
  - `manifestFiles`: Array of manifest files

**noFixAvailable**: No fix exists for this vulnerability (no patched version published)

**fixNotApplicable**: A fix exists but cannot be applied due to version constraints
- `value.vulnerableArtifacts`: Array of vulnerable packages with their manifest files

**errorComputingFix**: An error occurred while computing fixes
- `value.message`: Error description

### Advisory Details (when include_details=true)

- `title`: string | null
- `description`: string | null
- `cwes`: string[] - CWE identifiers
- `severity`: "LOW" | "MODERATE" | "HIGH" | "CRITICAL"
- `cvssVector`: string | null
- `publishedAt`: string (ISO date)
- `kev`: boolean - Whether it's a Known Exploited Vulnerability
- `epss`: number | null - Exploit Prediction Scoring System score
- `affectedPurls`: Array of affected packages with version ranges

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- fixes:list

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
      "name": "fixes"
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
      "SocketNotFoundResponse": {
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
        "description": "Resource not found"
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
    "/orgs/{org_slug}/fixes": {
      "get": {
        "tags": [
          "fixes"
        ],
        "summary": "Fetch fixes for vulnerabilities in a repository or scan",
        "operationId": "fetch-fixes",
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
            "name": "repo_slug",
            "in": "query",
            "required": false,
            "description": "The slug of the repository to fetch fixes for. Computes fixes based on the latest scan on the default branch",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "full_scan_id",
            "in": "query",
            "required": false,
            "description": "The ID of the scan to fetch fixes for",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "vulnerability_ids",
            "in": "query",
            "required": true,
            "description": "Comma-separated list of GHSA or CVE IDs, or \"*\" for all vulnerabilities",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "allow_major_updates",
            "in": "query",
            "required": true,
            "description": "Whether to allow major version updates in fixes",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "minimum_release_age",
            "in": "query",
            "required": false,
            "description": "Minimum release age for fixes packages (e.g., \"1h\", \"2d\", \"1w\"). Higher values reduces risk of installing recently released untested package versions.",
            "schema": {
              "type": "string",
              "default": "0d"
            }
          },
          {
            "name": "include_details",
            "in": "query",
            "required": false,
            "description": "Whether to include advisory details in the response",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "include_responsible_direct_dependencies",
            "in": "query",
            "required": false,
            "description": "Set to include the direct dependencies responsible for introducing the dependency or dependencies with the vulnerability in the response",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "fixes:list"
            ]
          },
          {
            "basicAuth": [
              "fixes:list"
            ]
          }
        ],
        "description": "Fetches available fixes for vulnerabilities in a repository or scan.\nRequires either repo_slug or full_scan_id as well as vulnerability_ids to be provided.\nvulnerability_ids can be a comma-separated list of GHSA or CVE IDs, or \"*\" for all vulnerabilities.\n\n## Response Structure\n\nThe response contains a `fixDetails` object where each key is a vulnerability ID (GHSA or CVE) and the value is a discriminated union based on the `type` field.\n\n### Common Fields\n\nAll response variants include:\n- `type`: Discriminator field (one of: \"fixFound\", \"partialFixFound\", \"noFixAvailable\", \"fixNotApplicable\", \"errorComputingFix\")\n- `value`: Object containing the variant-specific data\n\nThe `value` object always contains:\n- `ghsa`: string | null - The GHSA ID\n- `cve`: string | null - The CVE ID (if available)\n- `advisoryDetails`: object | null - Advisory details (only if include_details=true)\n\n### Response Variants\n\n**fixFound**: A complete fix is available for all vulnerable packages\n- `value.fixDetails.fixes`: Array of fix objects, each containing:\n  - `purl`: Package URL to upgrade\n  - `fixedVersion`: Version to upgrade to\n  - `manifestFiles`: Array of manifest files containing the package\n  - `updateType`: \"patch\" | \"minor\" | \"major\" | \"unknown\"\n- `value.fixDetails.responsibleDirectDependencies`: (optional) Map of direct dependencies responsible for the vulnerability\n\n**partialFixFound**: Fixes available for some but not all vulnerable packages\n- Same as fixFound, plus:\n- `value.fixDetails.unfixablePurls`: Array of packages that cannot be fixed, each containing:\n  - `purl`: Package URL\n  - `manifestFiles`: Array of manifest files\n\n**noFixAvailable**: No fix exists for this vulnerability (no patched version published)\n\n**fixNotApplicable**: A fix exists but cannot be applied due to version constraints\n- `value.vulnerableArtifacts`: Array of vulnerable packages with their manifest files\n\n**errorComputingFix**: An error occurred while computing fixes\n- `value.message`: Error description\n\n### Advisory Details (when include_details=true)\n\n- `title`: string | null\n- `description`: string | null\n- `cwes`: string[] - CWE identifiers\n- `severity`: \"LOW\" | \"MODERATE\" | \"HIGH\" | \"CRITICAL\"\n- `cvssVector`: string | null\n- `publishedAt`: string (ISO date)\n- `kev`: boolean - Whether it's a Known Exploited Vulnerability\n- `epss`: number | null - Exploit Prediction Scoring System score\n- `affectedPurls`: Array of affected packages with version ranges\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- fixes:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "fixDetails": {
                      "type": "object",
                      "additionalProperties": {
                        "type": "object",
                        "description": "",
                        "default": null
                      },
                      "properties": {},
                      "description": ""
                    }
                  },
                  "required": [
                    "fixDetails"
                  ]
                }
              }
            },
            "description": "Fix details for requested vulnerabilities"
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
          "404": {
            "$ref": "#/components/responses/SocketNotFoundResponse"
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