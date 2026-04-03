# Source: https://docs.jfrog.com/security/reference/get-issue-events-v2_custom-issues-v2-openapi.md

# Get Issue Events V2

Gets an issue created by a vendor.

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
    "/api/v2/events/{id}": {
      "get": {
        "operationId": "get-issue-events-v2_custom-issues-v2-openapi",
        "summary": "Get Issue Events V2",
        "description": "Gets an issue created by a vendor.",
        "tags": [
          "Custom Issues V2"
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
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "package_type": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    },
                    "provider": {
                      "type": "string"
                    },
                    "summary": {
                      "type": "string"
                    },
                    "malicious_package": {
                      "type": "boolean"
                    },
                    "description": {
                      "type": "string"
                    },
                    "severity": {
                      "type": "string"
                    },
                    "leading_severity": {
                      "type": "object",
                      "properties": {
                        "severity": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "severity"
                      ]
                    },
                    "created": {
                      "type": "string"
                    },
                    "sources": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "source_id": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "source_id"
                        ]
                      }
                    },
                    "components": {
                      "type": "array",
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
                            "type": "null"
                          },
                          "vulnerable_ranges": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "vulnerable_versions": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                },
                                "fixed_versions": {
                                  "type": "null"
                                },
                                "container_affected_cpes": {
                                  "type": "null"
                                }
                              },
                              "required": [
                                "vulnerable_versions"
                              ]
                            }
                          }
                        },
                        "required": [
                          "id",
                          "vulnerable_versions",
                          "vulnerable_ranges"
                        ]
                      }
                    },
                    "modified": {
                      "type": "string"
                    },
                    "modified_time": {
                      "type": "integer"
                    },
                    "edited": {
                      "type": "string"
                    },
                    "issue_kind": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "id",
                    "package_type",
                    "type",
                    "provider",
                    "summary",
                    "malicious_package",
                    "description",
                    "severity",
                    "leading_severity",
                    "created",
                    "sources",
                    "components",
                    "modified",
                    "modified_time",
                    "edited",
                    "issue_kind"
                  ]
                },
                "example": {
                  "id": "CustomIssue_IvPwvFGilq1w5t3s",
                  "package_type": "maven",
                  "type": "security",
                  "provider": "Custom",
                  "summary": "custom issue example",
                  "malicious_package": true,
                  "description": "Security issue in specific package and version\nCustom issue type: security\nSeverity: Critical\nPkg:  com.google.guava:guava \nAssigned versions:  specific version, version 16.0",
                  "severity": "Critical",
                  "leading_severity": {
                    "severity": "Critical"
                  },
                  "created": "2023-06-08T06:52:16.383Z",
                  "sources": [
                    {
                      "source_id": "CustomIssue_BClINuPvH9JmkVy4"
                    }
                  ],
                  "components": [
                    {
                      "id": "com.google.guava:guava",
                      "vulnerable_versions": [
                        "[16.0]"
                      ],
                      "fixed_versions": null,
                      "vulnerable_ranges": [
                        {
                          "vulnerable_versions": [
                            "[16.0]"
                          ],
                          "fixed_versions": null,
                          "container_affected_cpes": null
                        }
                      ]
                    }
                  ],
                  "modified": "2023-06-08T06:52:16.383Z",
                  "modified_time": 0,
                  "edited": "2023-06-08T06:52:16.507Z",
                  "issue_kind": 0
                }
              }
            }
          }
        },
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "additionalProperties": true
              },
              "example": {
                "id": "CustomIssue_IvPwvFGilq1w5t3s",
                "package_type": "maven",
                "type": "security",
                "provider": "Custom",
                "summary": "custom issue example",
                "malicious_package": true,
                "description": "Security issue in specific package and version\nCustom issue type: security\nSeverity: Critical\nPkg:  com.google.guava:guava \nAssigned versions:  specific version, version 16.0",
                "severity": "Critical",
                "leading_severity": {
                  "severity": "Critical"
                },
                "created": "2023-06-08T06:52:16.383Z",
                "sources": [
                  {
                    "source_id": "CustomIssue_BClINuPvH9JmkVy4"
                  }
                ],
                "components": [
                  {
                    "id": "com.google.guava:guava",
                    "vulnerable_versions": [
                      "[16.0]"
                    ],
                    "fixed_versions": null,
                    "vulnerable_ranges": [
                      {
                        "vulnerable_versions": [
                          "[16.0]"
                        ],
                        "fixed_versions": null,
                        "container_affected_cpes": null
                      }
                    ]
                  }
                ],
                "modified": "2023-06-08T06:52:16.383Z",
                "modified_time": 0,
                "edited": "2023-06-08T06:52:16.507Z",
                "issue_kind": 0
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
      "name": "Custom Issues V2",
      "description": "APIs from Custom Issues V2"
    }
  ]
}
```