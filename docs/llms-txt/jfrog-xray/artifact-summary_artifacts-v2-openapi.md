# Source: https://docs.jfrog.com/security/reference/artifact-summary_artifacts-v2-openapi.md

# Artifact Summary

Provides a security, license, and operational risk summary for artifacts specified by path identifiers or checksums (v2 API).

The v2 endpoint includes component-level vulnerability details within each issue, showing which specific components are affected and what fixed versions are available (via the components array containing component_id, version, pkg_type, and fixed_versions). This data is not available in the v1 endpoint.

Either paths or checksums must be provided. If both are provided, checksums are ignored.

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
    "/api/v2/summary/artifact": {
      "post": {
        "operationId": "artifact-summary_artifacts-v2-openapi",
        "summary": "Artifact Summary",
        "description": "Provides a security, license, and operational risk summary for artifacts specified by path identifiers or checksums (v2 API).\n\nThe v2 endpoint includes component-level vulnerability details within each issue, showing which specific components are affected and what fixed versions are available (via the components array containing component_id, version, pkg_type, and fixed_versions). This data is not available in the v1 endpoint.\n\nEither paths or checksums must be provided. If both are provided, checksums are ignored.\n\nRequires a user with Read permission.\n",
        "tags": [
          "Artifacts V2"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "paths": {
                    "type": "array",
                    "description": "Array of artifact paths. The path must start with the artifactory_id (default for Xray 3.x).\n",
                    "items": {
                      "type": "string"
                    }
                  },
                  "checksums": {
                    "type": "array",
                    "description": "Array of SHA-256 or SHA-1 checksums. Ignored if paths is provided.",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              },
              "examples": {
                "byPaths": {
                  "summary": "Search by artifact paths",
                  "value": {
                    "paths": [
                      "docker-local/nginx/latest/manifest.json",
                      "jfrog-npm-local/lodash/-/lodash-4.9.0.tgz"
                    ]
                  }
                },
                "byChecksums": {
                  "summary": "Search by checksum",
                  "value": {
                    "checksums": [
                      "d160c68ed8879ae42756e159daec1dd7ecfd53b6192321656b72715e28d46dd2"
                    ]
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Artifact summary retrieved successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "artifacts": {
                      "type": "array",
                      "description": "Array of artifact summaries.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "general": {
                            "type": "object",
                            "properties": {
                              "component_id": {
                                "type": "string"
                              },
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
                              }
                            }
                          },
                          "issues": {
                            "type": "array",
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
                                      "cwe": {
                                        "type": "array",
                                        "items": {
                                          "type": "string"
                                        }
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
                                  "description": "Vulnerable component details (v2 only). Shows which components are affected and available fixes.\n",
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
                                },
                                "extended_information": {
                                  "type": "object",
                                  "properties": {
                                    "short_description": {
                                      "type": "string"
                                    },
                                    "full_description": {
                                      "type": "string"
                                    },
                                    "jfrog_research_severity": {
                                      "type": "string"
                                    },
                                    "jfrog_research_severity_reasons": {
                                      "type": "array",
                                      "items": {
                                        "type": "object",
                                        "properties": {
                                          "name": {
                                            "type": "string"
                                          },
                                          "description": {
                                            "type": "string"
                                          },
                                          "is_positive": {
                                            "type": "boolean"
                                          }
                                        }
                                      }
                                    },
                                    "remediation": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "component_physical_paths": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              }
                            }
                          },
                          "licenses": {
                            "type": "array",
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
                            "items": {
                              "type": "object",
                              "properties": {
                                "component_id": {
                                  "type": "string"
                                },
                                "risk": {
                                  "type": "string"
                                },
                                "risk_reason": {
                                  "type": "string"
                                },
                                "is_eol": {
                                  "type": "boolean"
                                },
                                "eol_message": {
                                  "type": "string"
                                },
                                "latest_version": {
                                  "type": "string"
                                },
                                "newer_versions": {
                                  "type": "integer"
                                },
                                "cadence": {
                                  "type": "integer"
                                },
                                "commits": {
                                  "type": "string"
                                },
                                "committers": {
                                  "type": "string"
                                },
                                "released": {
                                  "type": "string"
                                }
                              }
                            }
                          }
                        }
                      }
                    },
                    "errors": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "identifier": {
                            "type": "string"
                          },
                          "error": {
                            "type": "string"
                          }
                        }
                      }
                    }
                  }
                },
                "example": {
                  "artifacts": [
                    {
                      "general": {
                        "name": "moment-2.29.3.tar.gz",
                        "component_id": "moment-2.29.3.tar.gz",
                        "pkg_type": "Generic",
                        "path": "default/npm-local/moment-2.29.3.tar.gz",
                        "sha256": "8240b88c4879b771bdc2ab571fe26d8c10dc92f0e1c130ae468a01ef0d57fe52"
                      },
                      "issues": [
                        {
                          "issue_id": "XRAY-230778",
                          "summary": "moment is a JavaScript date library for parsing...",
                          "issue_type": "security",
                          "severity": "High",
                          "provider": "JFrog",
                          "cves": [
                            {
                              "cve": "CVE-2022-31129",
                              "cwe": [
                                "CWE-1333",
                                "CWE-400"
                              ],
                              "cvss_v2": "5.0/CVSS:2.0/AV:N/C:N/I:N/A:P",
                              "cvss_v3": "7.5/CVSS:3.1/AV:N/PR:N/UI:N/S:U/C:N/I:N/A:H"
                            }
                          ],
                          "created": "2022-07-12T00:00:08.828Z",
                          "impact_path": [
                            "default/npm-local/moment-2.29.3.tar.gz/moment-2.29.3/Moment.js.nuspec"
                          ],
                          "components": [
                            {
                              "component_id": "npm://moment:2.29.3",
                              "version": "2.29.3",
                              "pkg_type": "npm",
                              "fixed_versions": [
                                "2.29.4"
                              ]
                            }
                          ],
                          "extended_information": {
                            "short_description": "ReDoS in moment.js could lead to denial of service.",
                            "jfrog_research_severity": "Medium",
                            "jfrog_research_severity_reasons": [
                              {
                                "name": "Exploitation requires specific usage pattern",
                                "is_positive": true
                              },
                              {
                                "name": "The issue has an exploit published",
                                "is_positive": false
                              }
                            ]
                          },
                          "component_physical_paths": [
                            "moment-2.29.3/package.json"
                          ]
                        }
                      ],
                      "licenses": [
                        {
                          "name": "MIT",
                          "full_name": "MIT License",
                          "more_info_url": [
                            "https://opensource.org/licenses/MIT"
                          ],
                          "components": [
                            "npm://moment:2.29.3"
                          ]
                        }
                      ],
                      "operational_risks": [
                        {
                          "component_id": "npm://moment:2.29.3",
                          "risk": "High",
                          "risk_reason": "Health",
                          "latest_version": "2.29.4",
                          "newer_versions": 1,
                          "cadence": 1,
                          "released": "2022-04-17T18:27:04Z"
                        }
                      ]
                    }
                  ],
                  "errors": []
                }
              }
            }
          },
          "415": {
            "description": "Failed to parse JSON request body.",
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
                  "error": "Failed to parse json."
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