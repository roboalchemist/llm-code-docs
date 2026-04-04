# Source: https://docs.jfrog.com/security/reference/export-component-details-v1-deprecated_components-v2-openapi.md

# Export Component Details V2

Export component security details (vulnerabilities, violations, licenses, operational risks) to various formats. Returns a ZIP file containing the exported data. Requires Read permission.

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
    "/api/v2/component/exportDetails": {
      "post": {
        "operationId": "export-component-details-v1-deprecated_components-v2-openapi",
        "summary": "Export Component Details V2",
        "description": "Export component security details (vulnerabilities, violations, licenses, operational risks) to various formats. Returns a ZIP file containing the exported data. Requires Read permission.",
        "tags": [
          "Components V2"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "package_type": {
                    "type": "string",
                    "description": "Package type of the component (e.g. docker, maven, npm)."
                  },
                  "component_name": {
                    "type": "string",
                    "description": "Name of the component to export details for."
                  },
                  "path": {
                    "type": "string",
                    "description": "Path to the component in the repository."
                  },
                  "output_format": {
                    "type": "string",
                    "description": "Output format for the export (e.g. pdf)."
                  },
                  "spdx": {
                    "type": "boolean",
                    "description": "Generate SPDX SBOM document."
                  },
                  "spdx_format": {
                    "type": "string",
                    "description": "SPDX output format (e.g. json, tag-value)."
                  },
                  "cyclonedx": {
                    "type": "boolean",
                    "description": "Generate CycloneDX SBOM document."
                  },
                  "cyclonedx_format": {
                    "type": "string",
                    "description": "CycloneDX output format (e.g. json, xml)."
                  },
                  "vex": {
                    "type": "boolean",
                    "description": "Generate VEX (Vulnerability Exploitability eXchange) document."
                  },
                  "violations": {
                    "type": "boolean",
                    "description": "Include violations in the export."
                  },
                  "include_ignored_violations": {
                    "type": "boolean",
                    "description": "Include ignored violations in the export."
                  },
                  "license": {
                    "type": "boolean",
                    "description": "Include license information in the export."
                  },
                  "exclude_unknown": {
                    "type": "boolean",
                    "description": "Exclude components with unknown licenses from the export."
                  },
                  "vulnerabilities": {
                    "type": "boolean",
                    "description": "Include security vulnerabilities information in the export."
                  },
                  "operational_risk": {
                    "type": "boolean",
                    "description": "Include operational risk information in the export."
                  },
                  "secrets": {
                    "type": "boolean",
                    "description": "Include information about secrets in the export."
                  },
                  "services": {
                    "type": "boolean",
                    "description": "Include information about services in the export."
                  },
                  "malicious_code": {
                    "type": "boolean",
                    "description": "Include malicious code findings in the export."
                  },
                  "applications": {
                    "type": "boolean",
                    "description": "Include information about applications in the export."
                  },
                  "iac": {
                    "type": "boolean",
                    "description": "Include Infrastructure as Code (IaC) findings in the export."
                  },
                  "sast": {
                    "type": "boolean",
                    "description": "Include Static Application Security Testing (SAST) findings in the export."
                  },
                  "license_resolution": {
                    "type": "boolean",
                    "description": "Include license conclusion/resolution in the export."
                  }
                },
                "required": [
                  "package_type",
                  "component_name"
                ]
              },
              "example": {
                "package_type": "docker",
                "component_name": "ics:latest",
                "path": "my-dockers/ics/latest/manifest.json",
                "violations": true,
                "include_ignored_violations": true,
                "license": true,
                "exclude_unknown": false,
                "operational_risk": true,
                "vulnerabilities": true,
                "secrets": true,
                "services": true,
                "applications": true,
                "output_format": "pdf"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "ZIP file containing the exported component details.",
            "content": {
              "application/zip": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          },
          "400": {
            "description": "Invalid request payload."
          },
          "500": {
            "description": "Failed to export component details."
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
      "name": "Components V2",
      "description": "APIs from Components V2"
    }
  ]
}
```