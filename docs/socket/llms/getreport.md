# Source: https://docs.socket.dev/reference/getreport.md

# View a report

**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/getorgfullscan) instead.

Deprecated: Use `/orgs/{org_slug}/full-scans` instead. Get all the issues, packages, and scores related to an specific project report.

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- report:read

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
      "name": "deprecated"
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
      },
      "SocketGone": {
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
        "description": "Gone"
      }
    },
    "schemas": {
      "SocketReport": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "id": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "healthy": {
            "type": "boolean",
            "default": false,
            "description": ""
          },
          "issues": {
            "$ref": "#/components/schemas/SocketIssueList"
          },
          "score": {
            "type": "object",
            "additionalProperties": false,
            "description": "",
            "properties": {
              "avgSupplyChainRisk": {
                "type": "number",
                "description": "",
                "default": 0
              },
              "avgQuality": {
                "type": "number",
                "description": "",
                "default": 0
              },
              "avgMaintenance": {
                "type": "number",
                "description": "",
                "default": 0
              },
              "avgVulnerability": {
                "type": "number",
                "description": "",
                "default": 0
              },
              "avgLicense": {
                "type": "number",
                "description": "",
                "default": 0
              }
            },
            "required": [
              "avgLicense",
              "avgMaintenance",
              "avgQuality",
              "avgSupplyChainRisk",
              "avgVulnerability"
            ]
          },
          "url": {
            "type": "string",
            "description": "",
            "default": ""
          }
        },
        "required": [
          "healthy",
          "id",
          "issues",
          "score",
          "url"
        ]
      },
      "SocketIssueList": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/SocketIssue"
        },
        "description": ""
      },
      "SocketIssue": {
        "anyOf": [
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "gptSecurity"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "gptAnomaly"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "risk": {
                            "type": "string",
                            "enum": [
                              "low",
                              "medium",
                              "high"
                            ],
                            "description": "",
                            "default": "medium"
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "risk",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "gptMalware"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "filesystemAccess"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "module": {
                            "type": "string",
                            "description": "",
                            "default": "fs"
                          }
                        },
                        "required": [
                          "module"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "networkAccess"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "module": {
                            "type": "string",
                            "description": "",
                            "default": "net"
                          }
                        },
                        "required": [
                          "module"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "shellAccess"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "module": {
                            "type": "string",
                            "description": "",
                            "default": "child_process"
                          }
                        },
                        "required": [
                          "module"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "debugAccess"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "module": {
                            "type": "string",
                            "description": "",
                            "default": "vm"
                          }
                        },
                        "required": [
                          "module"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "chromePermission"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "permission": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "permissionType": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "permission",
                          "permissionType"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "chromeHostPermission"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "host": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "permissionType": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "host",
                          "permissionType"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "chromeWildcardHostPermission"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "host": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "permissionType": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "host",
                          "permissionType"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "chromeContentScript"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "scriptFile": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "matches": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "runAt": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "matches",
                          "runAt",
                          "scriptFile"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "criticalCVE"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "cveId": {
                            "type": "string",
                            "description": "Common Vulnerabilities and Exposures identifier (e.g., CVE-2021-44228)",
                            "default": ""
                          },
                          "cwes": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "description": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "id": {
                                  "type": "string",
                                  "description": "Common Weakness Enumeration identifier (e.g., CWE-79)",
                                  "default": ""
                                },
                                "name": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                }
                              },
                              "required": [
                                "description",
                                "id",
                                "name"
                              ]
                            },
                            "description": ""
                          },
                          "cvss": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "Common Vulnerability Scoring System metrics",
                            "properties": {
                              "score": {
                                "type": "number",
                                "description": "CVSS base score ranging from 0.0 to 10.0",
                                "default": 0
                              },
                              "vectorString": {
                                "type": "string",
                                "description": "CVSS vector string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)",
                                "default": ""
                              }
                            },
                            "required": [
                              "score",
                              "vectorString"
                            ]
                          },
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "firstPatchedVersionIdentifier": {
                            "type": "string",
                            "description": "The first version that includes a patch for this vulnerability",
                            "default": ""
                          },
                          "ghsaId": {
                            "type": "string",
                            "description": "GitHub Security Advisory identifier (e.g., GHSA-1234-5678-9abc)",
                            "default": ""
                          },
                          "severity": {
                            "type": "string",
                            "description": "",
                            "default": "critical"
                          },
                          "title": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "url": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "vulnerableVersionRange": {
                            "type": "string",
                            "description": "Version range affected by this vulnerability (e.g., >= 2.0.0, < 2.17.1)",
                            "default": ""
                          },
                          "kevs": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "vulnerabilityName": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "shortDescription": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "requiredAction": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "dateAdded": {
                                  "type": "string",
                                  "description": "Date when added to CISA KEV catalog (ISO 8601 format)",
                                  "default": ""
                                },
                                "dueDate": {
                                  "type": "string",
                                  "description": "Remediation deadline for federal agencies (ISO 8601 format)",
                                  "default": "",
                                  "nullable": true
                                },
                                "knownRansomwareCampaignUse": {
                                  "type": "string",
                                  "description": "Known, Unknown, or specific ransomware campaign names",
                                  "default": "",
                                  "nullable": true
                                },
                                "notes": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "vendorProject": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "product": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                }
                              },
                              "required": [
                                "dateAdded",
                                "dueDate",
                                "knownRansomwareCampaignUse",
                                "notes",
                                "product",
                                "requiredAction",
                                "shortDescription",
                                "vendorProject",
                                "vulnerabilityName"
                              ]
                            },
                            "description": "",
                            "nullable": true
                          },
                          "epss": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "Exploit Prediction Scoring System https://www.first.org/epss/",
                            "properties": {
                              "score": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              },
                              "percentile": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              }
                            },
                            "required": [
                              "percentile",
                              "score"
                            ],
                            "nullable": true
                          }
                        },
                        "required": [
                          "cveId",
                          "cvss",
                          "cwes",
                          "description",
                          "epss",
                          "firstPatchedVersionIdentifier",
                          "ghsaId",
                          "kevs",
                          "severity",
                          "title",
                          "url",
                          "vulnerableVersionRange"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "cve"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "cveId": {
                            "type": "string",
                            "description": "Common Vulnerabilities and Exposures identifier (e.g., CVE-2021-44228)",
                            "default": ""
                          },
                          "cwes": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "description": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "id": {
                                  "type": "string",
                                  "description": "Common Weakness Enumeration identifier (e.g., CWE-79)",
                                  "default": ""
                                },
                                "name": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                }
                              },
                              "required": [
                                "description",
                                "id",
                                "name"
                              ]
                            },
                            "description": ""
                          },
                          "cvss": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "Common Vulnerability Scoring System metrics",
                            "properties": {
                              "score": {
                                "type": "number",
                                "description": "CVSS base score ranging from 0.0 to 10.0",
                                "default": 0
                              },
                              "vectorString": {
                                "type": "string",
                                "description": "CVSS vector string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)",
                                "default": ""
                              }
                            },
                            "required": [
                              "score",
                              "vectorString"
                            ]
                          },
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "firstPatchedVersionIdentifier": {
                            "type": "string",
                            "description": "The first version that includes a patch for this vulnerability",
                            "default": ""
                          },
                          "ghsaId": {
                            "type": "string",
                            "description": "GitHub Security Advisory identifier (e.g., GHSA-1234-5678-9abc)",
                            "default": ""
                          },
                          "severity": {
                            "type": "string",
                            "description": "",
                            "default": "critical"
                          },
                          "title": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "url": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "vulnerableVersionRange": {
                            "type": "string",
                            "description": "Version range affected by this vulnerability (e.g., >= 2.0.0, < 2.17.1)",
                            "default": ""
                          },
                          "kevs": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "vulnerabilityName": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "shortDescription": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "requiredAction": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "dateAdded": {
                                  "type": "string",
                                  "description": "Date when added to CISA KEV catalog (ISO 8601 format)",
                                  "default": ""
                                },
                                "dueDate": {
                                  "type": "string",
                                  "description": "Remediation deadline for federal agencies (ISO 8601 format)",
                                  "default": "",
                                  "nullable": true
                                },
                                "knownRansomwareCampaignUse": {
                                  "type": "string",
                                  "description": "Known, Unknown, or specific ransomware campaign names",
                                  "default": "",
                                  "nullable": true
                                },
                                "notes": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "vendorProject": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "product": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                }
                              },
                              "required": [
                                "dateAdded",
                                "dueDate",
                                "knownRansomwareCampaignUse",
                                "notes",
                                "product",
                                "requiredAction",
                                "shortDescription",
                                "vendorProject",
                                "vulnerabilityName"
                              ]
                            },
                            "description": "",
                            "nullable": true
                          },
                          "epss": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "Exploit Prediction Scoring System https://www.first.org/epss/",
                            "properties": {
                              "score": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              },
                              "percentile": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              }
                            },
                            "required": [
                              "percentile",
                              "score"
                            ],
                            "nullable": true
                          }
                        },
                        "required": [
                          "cveId",
                          "cvss",
                          "cwes",
                          "description",
                          "epss",
                          "firstPatchedVersionIdentifier",
                          "ghsaId",
                          "kevs",
                          "severity",
                          "title",
                          "url",
                          "vulnerableVersionRange"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "mediumCVE"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "cveId": {
                            "type": "string",
                            "description": "Common Vulnerabilities and Exposures identifier (e.g., CVE-2021-44228)",
                            "default": ""
                          },
                          "cwes": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "description": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "id": {
                                  "type": "string",
                                  "description": "Common Weakness Enumeration identifier (e.g., CWE-79)",
                                  "default": ""
                                },
                                "name": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                }
                              },
                              "required": [
                                "description",
                                "id",
                                "name"
                              ]
                            },
                            "description": ""
                          },
                          "cvss": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "Common Vulnerability Scoring System metrics",
                            "properties": {
                              "score": {
                                "type": "number",
                                "description": "CVSS base score ranging from 0.0 to 10.0",
                                "default": 0
                              },
                              "vectorString": {
                                "type": "string",
                                "description": "CVSS vector string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)",
                                "default": ""
                              }
                            },
                            "required": [
                              "score",
                              "vectorString"
                            ]
                          },
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "firstPatchedVersionIdentifier": {
                            "type": "string",
                            "description": "The first version that includes a patch for this vulnerability",
                            "default": ""
                          },
                          "ghsaId": {
                            "type": "string",
                            "description": "GitHub Security Advisory identifier (e.g., GHSA-1234-5678-9abc)",
                            "default": ""
                          },
                          "severity": {
                            "type": "string",
                            "description": "",
                            "default": "critical"
                          },
                          "title": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "url": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "vulnerableVersionRange": {
                            "type": "string",
                            "description": "Version range affected by this vulnerability (e.g., >= 2.0.0, < 2.17.1)",
                            "default": ""
                          },
                          "kevs": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "vulnerabilityName": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "shortDescription": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "requiredAction": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "dateAdded": {
                                  "type": "string",
                                  "description": "Date when added to CISA KEV catalog (ISO 8601 format)",
                                  "default": ""
                                },
                                "dueDate": {
                                  "type": "string",
                                  "description": "Remediation deadline for federal agencies (ISO 8601 format)",
                                  "default": "",
                                  "nullable": true
                                },
                                "knownRansomwareCampaignUse": {
                                  "type": "string",
                                  "description": "Known, Unknown, or specific ransomware campaign names",
                                  "default": "",
                                  "nullable": true
                                },
                                "notes": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "vendorProject": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "product": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                }
                              },
                              "required": [
                                "dateAdded",
                                "dueDate",
                                "knownRansomwareCampaignUse",
                                "notes",
                                "product",
                                "requiredAction",
                                "shortDescription",
                                "vendorProject",
                                "vulnerabilityName"
                              ]
                            },
                            "description": "",
                            "nullable": true
                          },
                          "epss": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "Exploit Prediction Scoring System https://www.first.org/epss/",
                            "properties": {
                              "score": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              },
                              "percentile": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              }
                            },
                            "required": [
                              "percentile",
                              "score"
                            ],
                            "nullable": true
                          }
                        },
                        "required": [
                          "cveId",
                          "cvss",
                          "cwes",
                          "description",
                          "epss",
                          "firstPatchedVersionIdentifier",
                          "ghsaId",
                          "kevs",
                          "severity",
                          "title",
                          "url",
                          "vulnerableVersionRange"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "mildCVE"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "cveId": {
                            "type": "string",
                            "description": "Common Vulnerabilities and Exposures identifier (e.g., CVE-2021-44228)",
                            "default": ""
                          },
                          "cwes": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "description": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "id": {
                                  "type": "string",
                                  "description": "Common Weakness Enumeration identifier (e.g., CWE-79)",
                                  "default": ""
                                },
                                "name": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                }
                              },
                              "required": [
                                "description",
                                "id",
                                "name"
                              ]
                            },
                            "description": ""
                          },
                          "cvss": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "Common Vulnerability Scoring System metrics",
                            "properties": {
                              "score": {
                                "type": "number",
                                "description": "CVSS base score ranging from 0.0 to 10.0",
                                "default": 0
                              },
                              "vectorString": {
                                "type": "string",
                                "description": "CVSS vector string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)",
                                "default": ""
                              }
                            },
                            "required": [
                              "score",
                              "vectorString"
                            ]
                          },
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "firstPatchedVersionIdentifier": {
                            "type": "string",
                            "description": "The first version that includes a patch for this vulnerability",
                            "default": ""
                          },
                          "ghsaId": {
                            "type": "string",
                            "description": "GitHub Security Advisory identifier (e.g., GHSA-1234-5678-9abc)",
                            "default": ""
                          },
                          "severity": {
                            "type": "string",
                            "description": "",
                            "default": "critical"
                          },
                          "title": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "url": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "vulnerableVersionRange": {
                            "type": "string",
                            "description": "Version range affected by this vulnerability (e.g., >= 2.0.0, < 2.17.1)",
                            "default": ""
                          },
                          "kevs": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "additionalProperties": false,
                              "description": "",
                              "properties": {
                                "vulnerabilityName": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "shortDescription": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "requiredAction": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "dateAdded": {
                                  "type": "string",
                                  "description": "Date when added to CISA KEV catalog (ISO 8601 format)",
                                  "default": ""
                                },
                                "dueDate": {
                                  "type": "string",
                                  "description": "Remediation deadline for federal agencies (ISO 8601 format)",
                                  "default": "",
                                  "nullable": true
                                },
                                "knownRansomwareCampaignUse": {
                                  "type": "string",
                                  "description": "Known, Unknown, or specific ransomware campaign names",
                                  "default": "",
                                  "nullable": true
                                },
                                "notes": {
                                  "type": "string",
                                  "description": "",
                                  "default": "",
                                  "nullable": true
                                },
                                "vendorProject": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                },
                                "product": {
                                  "type": "string",
                                  "description": "",
                                  "default": ""
                                }
                              },
                              "required": [
                                "dateAdded",
                                "dueDate",
                                "knownRansomwareCampaignUse",
                                "notes",
                                "product",
                                "requiredAction",
                                "shortDescription",
                                "vendorProject",
                                "vulnerabilityName"
                              ]
                            },
                            "description": "",
                            "nullable": true
                          },
                          "epss": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "Exploit Prediction Scoring System https://www.first.org/epss/",
                            "properties": {
                              "score": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              },
                              "percentile": {
                                "type": "number",
                                "description": "",
                                "default": 0
                              }
                            },
                            "required": [
                              "percentile",
                              "score"
                            ],
                            "nullable": true
                          }
                        },
                        "required": [
                          "cveId",
                          "cvss",
                          "cwes",
                          "description",
                          "epss",
                          "firstPatchedVersionIdentifier",
                          "ghsaId",
                          "kevs",
                          "severity",
                          "title",
                          "url",
                          "vulnerableVersionRange"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "emptyPackage"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "trivialPackage"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "linesOfCode": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "linesOfCode"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "noREADME"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "shrinkwrap"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "tooManyFiles"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "fileCount": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "fileCount"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "generic"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "title": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "description",
                          "title"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "ghaArgToSink"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "message": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "sourceLocation": {
                            "type": "object",
                            "description": "",
                            "default": null
                          },
                          "sinkLocations": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "message",
                          "sinkLocations",
                          "sourceLocation"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "ghaEnvToSink"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "message": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "sourceLocation": {
                            "type": "object",
                            "description": "",
                            "default": null
                          },
                          "sinkLocations": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "message",
                          "sinkLocations",
                          "sourceLocation"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "ghaContextToSink"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "message": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "sourceLocation": {
                            "type": "object",
                            "description": "",
                            "default": null
                          },
                          "sinkLocations": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "message",
                          "sinkLocations",
                          "sourceLocation"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "ghaArgToOutput"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "message": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "sourceLocation": {
                            "type": "object",
                            "description": "",
                            "default": null
                          },
                          "sinkLocations": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "message",
                          "sinkLocations",
                          "sourceLocation"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "ghaArgToEnv"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "message": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "sourceLocation": {
                            "type": "object",
                            "description": "",
                            "default": null
                          },
                          "sinkLocations": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "message",
                          "sinkLocations",
                          "sourceLocation"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "ghaContextToOutput"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "message": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "sourceLocation": {
                            "type": "object",
                            "description": "",
                            "default": null
                          },
                          "sinkLocations": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "message",
                          "sinkLocations",
                          "sourceLocation"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "ghaContextToEnv"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "message": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "sourceLocation": {
                            "type": "object",
                            "description": "",
                            "default": null
                          },
                          "sinkLocations": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "message",
                          "sinkLocations",
                          "sourceLocation"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "recentlyPublished"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "publishedAt": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "checkedAt": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "checkedAt",
                          "publishedAt"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "licenseSpdxDisj"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "spdxDisj": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "licenseScanResult": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "violationData": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          },
                          "warnData": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          },
                          "monitorData": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "description": "",
                              "default": null
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "licenseScanResult",
                          "monitorData",
                          "spdxDisj",
                          "violationData",
                          "warnData"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unsafeCopyright"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "licenseChange"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "prevLicenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "newLicenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "newLicenseId",
                          "prevLicenseId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "nonOSILicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "licenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "licenseId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "deprecatedLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "licenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "licenseId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "missingLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "nonSPDXLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unclearLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "possibleLicenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "possibleLicenseId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "mixedLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "licenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "licenseId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "notice"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "modifiedLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "licenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "similarity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "licenseId",
                          "similarity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "modifiedException"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "exceptionId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "similarity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "comments": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "comments",
                          "exceptionId",
                          "similarity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "licenseException"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "exceptionId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "comments": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "comments",
                          "exceptionId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "deprecatedException"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "exceptionId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "comments": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "comments",
                          "exceptionId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "miscLicenseIssues"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "location": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "description",
                          "location"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unidentifiedLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "location": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "maybeByteSpan": {
                            "type": "object",
                            "description": "",
                            "default": {}
                          },
                          "maybeTruncatedSource": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "match_strength": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "location",
                          "match_strength",
                          "maybeByteSpan",
                          "maybeTruncatedSource"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "noLicenseFound"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "explicitlyUnlicensedItem"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "location": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "maybeByteSpan": {
                            "type": "object",
                            "description": "",
                            "default": {}
                          },
                          "maybeTruncatedSource": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "location",
                          "maybeByteSpan",
                          "maybeTruncatedSource"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "copyleftLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "licenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "licenseId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "nonpermissiveLicense"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "licenseId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "licenseId"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "ambiguousClassifier"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "classifier": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "filepathOrProvenance": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "maybeByteSpan": {
                            "type": "object",
                            "description": "",
                            "default": {}
                          }
                        },
                        "required": [
                          "classifier",
                          "filepathOrProvenance",
                          "maybeByteSpan"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "invalidPackageJSON"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "httpDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "packageName": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "url": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "packageName",
                          "url"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "gitDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "packageName": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "url": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "packageName",
                          "url"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "gitHubDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "packageName": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "githubUser": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "githubRepo": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "commitsh": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "commitsh",
                          "githubRepo",
                          "githubUser",
                          "packageName"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "fileDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "packageName": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "filePath": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "filePath",
                          "packageName"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "noTests"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "noRepository"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "badSemver"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "badSemverDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "packageName": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "packageVersion": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "packageName",
                          "packageVersion"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "noV1"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "noWebsite"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "noBugTracker"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "noAuthorData"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "typeModuleCompatibility"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "floatingDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "dependency": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "dependency"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "manifestConfusion"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "key": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "description": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "description",
                          "key"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "malware"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "note": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "id",
                          "note"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "telemetry"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "note": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "id",
                          "note"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "troll"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "note": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "id",
                          "note"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "deprecated"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "reason": {
                            "type": "string",
                            "description": "",
                            "default": "This package is deprecated"
                          }
                        },
                        "required": [
                          "reason"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "chronoAnomaly"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "prevChronoDate": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "prevChronoVersion": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "prevSemverDate": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "prevSemverVersion": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "prevChronoDate",
                          "prevChronoVersion",
                          "prevSemverDate",
                          "prevSemverVersion"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "compromisedSSHKey"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "fingerprint": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "sshKey": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "username": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "fingerprint",
                          "sshKey",
                          "username"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "semverAnomaly"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "prevVersion": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "newVersion": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "newVersion",
                          "prevVersion"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "newAuthor"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "prevAuthor": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "newAuthor": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "newAuthor",
                          "prevAuthor"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unstableOwnership"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "author": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "author"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "missingAuthor"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unmaintained"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "lastPublish": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "lastPublish"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unpublished"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "version": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "version"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "majorRefactor"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "linesChanged": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "prevSize": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "curSize": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "changedPercent": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "changedPercent",
                          "curSize",
                          "linesChanged",
                          "prevSize"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "missingTarball"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "suspiciousStarActivity"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "percentageSuspiciousStars": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "repository": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "percentageSuspiciousStars",
                          "repository"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unpopularPackage"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillAutonomyAbuse"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillCommandInjection"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillDataExfiltration"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillDiscoveryAbuse"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillHardcodedSecrets"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillObfuscation"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillPromptInjection"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillResourceAbuse"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillSupplyChain"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillToolAbuse"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillToolChaining"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "skillTransitiveTrust"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "severity": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence",
                          "notes",
                          "severity"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "socketUpgradeAvailable"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "categories": {
                            "type": "array",
                            "items": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            },
                            "description": ""
                          },
                          "deprecated": {
                            "type": "boolean",
                            "default": false,
                            "description": ""
                          },
                          "interop": {
                            "type": "array",
                            "items": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            },
                            "description": ""
                          },
                          "replacementPURL": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "version": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "categories",
                          "deprecated",
                          "interop",
                          "replacementPURL",
                          "version"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "longStrings"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "highEntropyStrings"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "urlStrings"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "urls": {
                            "type": "array",
                            "items": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "urls"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "usesEval"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "evalType": {
                            "type": "string",
                            "description": "",
                            "default": "eval"
                          }
                        },
                        "required": [
                          "evalType"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "dynamicRequire"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "envVars"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "envVars": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "envVars"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "missingDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "name": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "name"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unusedDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "name": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "version": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "name",
                          "version"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "peerDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "name": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "name"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "uncaughtOptionalDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "name": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "name"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unresolvedRequire"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "extraneousDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "obfuscatedRequire"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "obfuscatedFile"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          },
                          "notes": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "confidence",
                          "notes"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "minifiedFile"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "confidence": {
                            "type": "number",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "confidence"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "installScripts"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "script": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "source": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "script",
                          "source"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "hasNativeCode"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "binScriptConfusion"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "binScript": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "binScript"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "shellScriptOverride"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "binScript": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "binScript"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "didYouMean"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "alternatePackage": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "alternatePackage"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "gptDidYouMean"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "alternatePackage": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "alternatePackage"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "bidi"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "zeroWidth"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "badEncoding"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "encoding": {
                            "type": "string",
                            "description": "",
                            "default": "utf8"
                          }
                        },
                        "required": [
                          "encoding"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "homoglyphs"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "invisibleChars"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "suspiciousString"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "pattern": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "explanation": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "explanation",
                          "pattern"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "potentialVulnerability"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "note": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "risk": {
                            "type": "string",
                            "enum": [
                              "low",
                              "medium",
                              "high"
                            ],
                            "description": "",
                            "default": "medium"
                          }
                        },
                        "required": [
                          "note",
                          "risk"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxProposedApiUsage"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "proposals": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "proposals"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxActivationWildcard"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "event": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "event"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxWorkspaceContainsActivation"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "pattern": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "pattern"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxUntrustedWorkspaceSupported"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "supported": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "supported"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxVirtualWorkspaceSupported"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "supported": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "supported"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxWebviewContribution"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxDebuggerContribution"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxExtensionDependency"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "extension": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "extension"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "vsxExtensionPack"
                ]
              },
              "value": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SocketIssueBasics"
                  },
                  {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "count": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "count"
                        ]
                      },
                      "usage": {
                        "$ref": "#/components/schemas/SocketUsageRef"
                      }
                    },
                    "required": [
                      "description",
                      "props"
                    ]
                  }
                ]
              }
            }
          }
        ]
      },
      "SocketIssueSeverity": {
        "type": "string",
        "enum": [
          "low",
          "middle",
          "high",
          "critical"
        ],
        "description": "",
        "default": "low"
      },
      "SocketCategory": {
        "type": "string",
        "enum": [
          "supplyChainRisk",
          "quality",
          "maintenance",
          "vulnerability",
          "license",
          "other"
        ],
        "description": "",
        "default": "other"
      },
      "SocketIssueBasics": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "severity": {
            "$ref": "#/components/schemas/SocketIssueSeverity"
          },
          "category": {
            "$ref": "#/components/schemas/SocketCategory"
          },
          "locations": {
            "$ref": "#/components/schemas/SocketRefList"
          },
          "label": {
            "type": "string",
            "description": "",
            "default": ""
          }
        },
        "required": [
          "category",
          "label",
          "locations",
          "severity"
        ]
      },
      "SocketUsageRef": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "file": {
            "$ref": "#/components/schemas/SocketRefFile"
          },
          "dependencies": {
            "$ref": "#/components/schemas/SocketRefList"
          }
        },
        "required": [
          "dependencies",
          "file"
        ]
      },
      "SocketRefList": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/SocketRef"
        },
        "description": ""
      },
      "SocketRefFile": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "path": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "range": {
            "$ref": "#/components/schemas/SocketRefTextRange"
          },
          "bytes": {
            "$ref": "#/components/schemas/SocketRefByteRange"
          }
        },
        "required": [
          "path"
        ]
      },
      "SocketRef": {
        "anyOf": [
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "unknown"
                ]
              },
              "value": {
                "type": "object",
                "additionalProperties": false,
                "description": "",
                "properties": {}
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "npm"
                ]
              },
              "value": {
                "$ref": "#/components/schemas/SocketRefNPM"
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "git"
                ]
              },
              "value": {
                "$ref": "#/components/schemas/SocketRefGit"
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "web"
                ]
              },
              "value": {
                "$ref": "#/components/schemas/SocketRefWeb"
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "pypi"
                ]
              },
              "value": {
                "$ref": "#/components/schemas/SocketRefPyPI"
              }
            }
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "go"
                ]
              },
              "value": {
                "$ref": "#/components/schemas/SocketRefGo"
              }
            }
          }
        ]
      },
      "SocketRefTextRange": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "startLine": {
            "type": "integer",
            "description": "",
            "default": 0
          },
          "startColumn": {
            "type": "integer",
            "description": "",
            "default": 0
          },
          "endLine": {
            "type": "integer",
            "description": "",
            "default": 0
          },
          "endColumn": {
            "type": "integer",
            "description": "",
            "default": 0
          }
        },
        "required": [
          "endColumn",
          "endLine",
          "startColumn",
          "startLine"
        ]
      },
      "SocketRefByteRange": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "start": {
            "type": "integer",
            "description": "",
            "default": 0
          },
          "end": {
            "type": "integer",
            "description": "",
            "default": 0
          }
        },
        "required": [
          "end",
          "start"
        ]
      },
      "SocketRefNPM": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "package": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "version": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "file": {
            "$ref": "#/components/schemas/SocketRefFile"
          }
        },
        "required": [
          "package"
        ]
      },
      "SocketRefGit": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "url": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "commit": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "tag": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "file": {
            "$ref": "#/components/schemas/SocketRefFile"
          }
        },
        "required": [
          "url"
        ]
      },
      "SocketRefWeb": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "url": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "file": {
            "$ref": "#/components/schemas/SocketRefFile"
          }
        },
        "required": [
          "url"
        ]
      },
      "SocketRefPyPI": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "package": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "version": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "artifact": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "file": {
            "$ref": "#/components/schemas/SocketRefFile"
          }
        },
        "required": [
          "package"
        ]
      },
      "SocketRefGo": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "package": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "version": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "file": {
            "$ref": "#/components/schemas/SocketRefFile"
          }
        },
        "required": [
          "package"
        ]
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
    "/report/view/{id}": {
      "get": {
        "tags": [
          "deprecated"
        ],
        "summary": "View a report",
        "deprecated": true,
        "operationId": "getReport",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "description": "",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "report:read"
            ]
          },
          {
            "basicAuth": [
              "report:read"
            ]
          }
        ],
        "description": "**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/getorgfullscan) instead.\n\nDeprecated: Use `/orgs/{org_slug}/full-scans` instead. Get all the issues, packages, and scores related to an specific project report.\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- report:read",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SocketReport"
                }
              }
            },
            "description": "Socket report"
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
          "410": {
            "$ref": "#/components/responses/SocketGone"
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