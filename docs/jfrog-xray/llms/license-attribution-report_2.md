# Source: https://docs.jfrog.com/security/reference/license-attribution-report.md

# License Attribution Report

Generates a license attribution report for a specific resource in the platform. The report can be output in PDF, JSON, CSV, or TXT format. Requires the Catalog service to be available.

Requires the "Manage Data" role. Supported from Xray Version 3.118.0 and above.


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
    "/api/v2/component/attribution": {
      "post": {
        "operationId": "license-attribution-report",
        "summary": "License Attribution Report",
        "description": "Generates a license attribution report for a specific resource in the platform. The report can be output in PDF, JSON, CSV, or TXT format. Requires the Catalog service to be available.\n\nRequires the \"Manage Data\" role. Supported from Xray Version 3.118.0 and above.\n",
        "tags": [
          "Legal V2"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "path": {
                    "type": "string",
                    "description": "Path of the requested resource in the platform."
                  },
                  "component_id": {
                    "type": "string",
                    "description": "Optional component identifier to scope the report."
                  },
                  "exclude_unknown_license": {
                    "type": "boolean",
                    "description": "If true, excludes components with unknown licenses."
                  },
                  "license_resolution": {
                    "type": "boolean",
                    "description": "If true, performs automatic license resolution for multi-license components."
                  },
                  "full_license_text": {
                    "type": "boolean",
                    "description": "If true, includes the full license text inside the report."
                  },
                  "include_package_versions": {
                    "type": "boolean",
                    "description": "If true, includes package versions as a column in the report."
                  },
                  "format": {
                    "type": "string",
                    "description": "Output format. Valid values are pdf, json, csv, txt."
                  }
                },
                "required": [
                  "path"
                ]
              },
              "example": {
                "path": "docker-test/juice-shop/v10.0.0/manifest.json",
                "license_resolution": false,
                "full_license_text": true,
                "include_package_versions": true,
                "format": "txt"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Attribution report generated successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "400": {
            "description": "Failed to parse input arguments or Catalog is not available.",
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
                  "error": "Invalid request payload"
                }
              }
            }
          },
          "403": {
            "description": "Permission denied.",
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
                  "error": "Permission denied"
                }
              }
            }
          },
          "500": {
            "description": "Failed to generate the attribution report.",
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
                  "error": "Failed to Export Attribution Report"
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
    }
  },
  "tags": [
    {
      "name": "Legal V2",
      "description": "APIs from Legal V2"
    }
  ]
}
```