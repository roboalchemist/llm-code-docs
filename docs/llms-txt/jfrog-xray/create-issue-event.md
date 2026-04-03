# Source: https://docs.jfrog.com/security/reference/create-issue-event.md

# Create Issue Event

Creates a custom issue (vulnerability). The id parameter cannot have a prefix Xray, and provider parameter cannot be JFrog. Requires Manage Xray Metadata permission.

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
    "/api/v1/events": {
      "post": {
        "operationId": "create-issue-event",
        "summary": "Create Issue Event",
        "description": "Creates a custom issue (vulnerability). The id parameter cannot have a prefix Xray, and provider parameter cannot be JFrog. Requires Manage Xray Metadata permission.",
        "tags": [
          "Custom Issues V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CustomIssuesEventMutationRequest"
              },
              "example": {
                "id": "IMP-ISSUE-787",
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
                "summary": "A very important custom issue",
                "description": "A very important custom issue",
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
          "201": {
            "description": "Custom issue created successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "description": "Issue identifier."
                    },
                    "package_type": {
                      "type": "string",
                      "description": "Package technology."
                    },
                    "type": {
                      "type": "string",
                      "description": "Issue type."
                    },
                    "provider": {
                      "type": "string",
                      "description": "Vendor or provider identifier."
                    },
                    "summary": {
                      "type": "string",
                      "description": "Short summary."
                    },
                    "description": {
                      "type": "string",
                      "description": "Detailed description."
                    },
                    "severity": {
                      "type": "string",
                      "description": "Issue severity."
                    },
                    "created": {
                      "type": "string",
                      "description": "Creation timestamp."
                    },
                    "cves": {
                      "type": "array",
                      "description": "Associated CVEs.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "cve": {
                            "type": "string"
                          },
                          "cvss_v2": {
                            "type": "string"
                          }
                        }
                      }
                    },
                    "sources": {
                      "type": "array",
                      "description": "Issue sources.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "source_id": {
                            "type": "string"
                          }
                        }
                      }
                    },
                    "components": {
                      "type": "array",
                      "description": "Affected components.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "vulnerable_versions": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "fixed_versions": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    },
                    "modified": {
                      "type": "string",
                      "description": "Last modification timestamp."
                    },
                    "edited": {
                      "type": "string",
                      "description": "Last edit timestamp."
                    }
                  }
                },
                "example": {
                  "id": "IMP-ISSUE-787",
                  "package_type": "maven",
                  "type": "security",
                  "provider": "sec-dep",
                  "summary": "A very important custom issue",
                  "description": "A very important custom issue",
                  "severity": "High",
                  "created": "2019-12-17T15:29:31.958350982",
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
                  ],
                  "modified": "2019-12-17T15:29:31.958350982",
                  "edited": "2019-12-17T15:29:31.979204912"
                }
              }
            }
          },
          "400": {
            "description": "Bad request - issue already exists, or required fields are missing."
          },
          "415": {
            "description": "Unsupported media type."
          },
          "500": {
            "description": "Internal server error."
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