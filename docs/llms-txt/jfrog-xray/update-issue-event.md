# Source: https://docs.jfrog.com/security/reference/update-issue-event.md

# Update Issue Event

Allows an issue vendor to update a custom issue

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
    "/api/v1/events/{id}": {
      "put": {
        "operationId": "update-issue-event",
        "summary": "Update Issue Event",
        "description": "Allows an issue vendor to update a custom issue",
        "tags": [
          "Custom Issues V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Resource identifier",
            "required": true,
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
                "$ref": "#/components/schemas/CustomIssuesEventMutationRequest"
              },
              "example": {
                "type": "Security",
                "provider": "sec-dep",
                "package_type": "maven",
                "severity": "High",
                "components": [
                  {
                    "id": "aero:aero",
                    "vulnerable_versions": [
                      "[0.2.3]"
                    ]
                  }
                ],
                "cves": [
                  {
                    "cve": "CVE-2017-1000386",
                    "cvss_v2": "2.4"
                  }
                ],
                "summary": "new summary",
                "description": "updated description",
                "sources": [
                  {
                    "source_id": "CVE-2017-1000386"
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": null
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
      "CustomIssuesEventMutationRequest": {
        "type": "object",
        "description": "JSON body for creating or updating a vendor issue event (Custom Issues API).",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique issue identifier. Cannot have an 'Xray' prefix."
          },
          "package_type": {
            "type": "string",
            "description": "Package technology (e.g. maven, npm)."
          },
          "type": {
            "type": "string",
            "description": "Issue type (e.g. Security)."
          },
          "provider": {
            "type": "string",
            "description": "Vendor or provider identifier. Cannot be 'JFrog'."
          },
          "summary": {
            "type": "string",
            "description": "Short summary of the issue."
          },
          "description": {
            "type": "string",
            "description": "Detailed description of the issue."
          },
          "severity": {
            "type": "string",
            "description": "Issue severity (e.g. High, Medium, Low, Critical)."
          },
          "cves": {
            "type": "array",
            "description": "List of associated CVEs.",
            "items": {
              "type": "object",
              "properties": {
                "cve": {
                  "type": "string",
                  "description": "CVE identifier."
                },
                "cvss_v2": {
                  "type": "string",
                  "description": "CVSS v2 score."
                }
              }
            }
          },
          "sources": {
            "type": "array",
            "description": "List of sources for this issue.",
            "items": {
              "type": "object",
              "properties": {
                "source_id": {
                  "type": "string",
                  "description": "Source identifier (e.g. CVE ID)."
                }
              }
            }
          },
          "components": {
            "type": "array",
            "description": "List of affected components.",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string",
                  "description": "Component identifier."
                },
                "vulnerable_versions": {
                  "type": "array",
                  "description": "List of vulnerable version ranges.",
                  "items": {
                    "type": "string"
                  }
                },
                "fixed_versions": {
                  "type": "array",
                  "description": "List of fixed version ranges (null if none).",
                  "items": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "required": [
          "id",
          "package_type",
          "type",
          "provider",
          "severity",
          "components"
        ],
        "example": {
          "id": "IMP-ISSUE-787",
          "package_type": "maven",
          "type": "Security",
          "provider": "sec-dep",
          "severity": "High",
          "summary": "A very important custom issue",
          "description": "A very important custom issue",
          "cves": [
            {
              "cve": "CVE-2017-1000386",
              "cvss_v2": "2.4"
            }
          ],
          "sources": [
            {
              "source_id": "CVE-2017-1000386"
            }
          ],
          "components": [
            {
              "id": "aero:aero",
              "vulnerable_versions": [
                "[0.2.3]"
              ],
              "fixed_versions": null
            }
          ]
        }
      }
    }
  },
  "tags": [
    {
      "name": "Custom Issues V1",
      "description": "APIs from Custom Issues V1"
    }
  ]
}
```