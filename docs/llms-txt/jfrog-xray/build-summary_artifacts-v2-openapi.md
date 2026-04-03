# Source: https://docs.jfrog.com/security/reference/build-summary_artifacts-v2-openapi.md

# Build Summary

Provides a security, license, and operational risk summary for a build specified by name and number. Returns issues (vulnerabilities), licenses found, operational risks, and any scan errors.

The v2 endpoint includes component-level details within issues that are not available in v1.

Requires a user with Read permission.


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
    "/api/v2/summary/build": {
      "get": {
        "operationId": "build-summary_artifacts-v2-openapi",
        "summary": "Build Summary",
        "description": "Provides a security, license, and operational risk summary for a build specified by name and number. Returns issues (vulnerabilities), licenses found, operational risks, and any scan errors.\n\nThe v2 endpoint includes component-level details within issues that are not available in v1.\n\nRequires a user with Read permission.\n",
        "tags": [
          "Artifacts V2"
        ],
        "parameters": [
          {
            "name": "build_name",
            "in": "query",
            "description": "The name of the build.",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "my-build"
          },
          {
            "name": "build_number",
            "in": "query",
            "description": "The build number/version.",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "42"
          },
          {
            "name": "build_repo",
            "in": "query",
            "description": "Build repository name. If not specified, resolved from project_key or uses default.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "project_key",
            "in": "query",
            "description": "Project key. Used to resolve build_repo if not explicitly provided.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Build summary retrieved successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "build": {
                      "type": "object",
                      "description": "Build artifact details.",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "path": {
                          "type": "string"
                        },
                        "pkg_type": {
                          "type": "string"
                        },
                        "sha256": {
                          "type": "string"
                        },
                        "component_id": {
                          "type": "string"
                        },
                        "sha1": {
                          "type": "string"
                        },
                        "parent_sha256": {
                          "type": "string"
                        }
                      }
                    },
                    "issues": {
                      "type": "array",
                      "description": "Security vulnerabilities found in the build.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "issue_id": {
                            "type": "string"
                          },
                          "summary": {
                            "type": "string"
                          },
                          "description": {
                            "type": "string"
                          },
                          "issue_type": {
                            "type": "string"
                          },
                          "severity": {
                            "type": "string"
                          },
                          "provider": {
                            "type": "string"
                          },
                          "cves": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "cve": {
                                  "type": "string"
                                },
                                "cvss_v2": {
                                  "type": "string"
                                },
                                "cvss_v3": {
                                  "type": "string"
                                }
                              }
                            }
                          },
                          "created": {
                            "type": "string"
                          },
                          "impact_path": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "components": {
                            "type": "array",
                            "description": "Component-level details (v2 only).",
                            "items": {
                              "type": "object",
                              "properties": {
                                "component_id": {
                                  "type": "string"
                                },
                                "version": {
                                  "type": "string"
                                },
                                "pkg_type": {
                                  "type": "string"
                                },
                                "fixed_versions": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    },
                    "licenses": {
                      "type": "array",
                      "description": "Licenses found in the build components.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "string"
                          },
                          "full_name": {
                            "type": "string"
                          },
                          "more_info_url": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "components": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    },
                    "operational_risks": {
                      "type": "array",
                      "description": "Operational risk assessments for build components.",
                      "items": {
                        "type": "object"
                      }
                    },
                    "errors": {
                      "type": "array",
                      "description": "Any errors encountered during scan or retrieval.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "error": {
                            "type": "string"
                          }
                        }
                      }
                    }
                  }
                },
                "example": {
                  "build": {
                    "name": "example_build",
                    "component_id": "example_build:1.0.0",
                    "pkg_type": "Build",
                    "path": "default/builds/example_build",
                    "sha256": "ff55b68d5f587aeaa2253f9586fd9ea847cbb29e1858edfe67d91536586980l2"
                  },
                  "issues": [
                    {
                      "issue_id": "XRAY-95701",
                      "summary": "A vulnerability was discovered in the PyYAML library...",
                      "description": "A vulnerability was discovered in the PyYAML library...",
                      "issue_type": "security",
                      "severity": "Critical",
                      "provider": "JFrog",
                      "cves": [
                        {
                          "cve": "CVE-2020-1747",
                          "cwe": [
                            "CWE-20"
                          ],
                          "cvss_v2": "10.0/CVSS:2.0/AV:N/AC:L/Au:N/C:C/I:C/A:C",
                          "cvss_v3": "9.8/CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
                        }
                      ],
                      "created": "2020-03-25T00:00:00.669Z",
                      "impact_path": [
                        "default/builds/example_build/example/latest/PyYAML-3.10-cp36-cp36m-linux_x86_64.whl"
                      ],
                      "extended_information": {
                        "short_description": "Insufficient input validation in the PyYAML library allows unauthenticated network attacker...",
                        "jfrog_research_severity": "Critical",
                        "jfrog_research_severity_reasons": [
                          {
                            "name": "The CVE can be remotely exploited",
                            "is_positive": false
                          },
                          {
                            "name": "The CVE has an exploit published",
                            "is_positive": false
                          }
                        ],
                        "remediation": "#### Development upgrade\nUpgrade the component to any of the suggested fixed versions."
                      }
                    }
                  ],
                  "licenses": [
                    {
                      "name": "Unknown",
                      "full_name": "Unknown license",
                      "more_info_url": [
                        "Unknown link"
                      ],
                      "components": [
                        "deb://ubuntu:bionic:grep:3.1-2build1",
                        "deb://ubuntu:bionic:passwd:1:4.5-1ubuntu2"
                      ]
                    }
                  ],
                  "errors": []
                }
              }
            }
          },
          "400": {
            "description": "Missing build name or build number.",
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
                  "error": "Failed to get build summary"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
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
      "name": "Artifacts V2",
      "description": "APIs from Artifacts V2"
    }
  ]
}
```