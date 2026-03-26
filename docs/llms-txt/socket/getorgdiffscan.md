# Source: https://docs.socket.dev/reference/getorgdiffscan.md

# Diff Full Scans

**This endpoint is deprecated.**

Get the difference between two existing Full Scans. The results are not persisted.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- full-scans:list

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
      }
    },
    "schemas": {
      "SocketDiffArtifact": {
        "allOf": [
          {
            "$ref": "#/components/schemas/SocketPURL"
          },
          {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "diffType": {
                "$ref": "#/components/schemas/SocketDiffArtifactType"
              },
              "id": {
                "$ref": "#/components/schemas/SocketId"
              },
              "author": {
                "type": "array",
                "items": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "description": "List of package authors or maintainers"
              },
              "base": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/SocketArtifactLink"
                },
                "description": "Artifact links from the base/before state"
              },
              "capabilities": {
                "$ref": "#/components/schemas/Capabilities"
              },
              "head": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/SocketArtifactLink"
                },
                "description": "Artifact links from the head/after state"
              },
              "qualifiers": {
                "$ref": "#/components/schemas/Qualifiers"
              },
              "size": {
                "type": "number",
                "description": "Total size of the package artifact in bytes",
                "default": 0
              },
              "license": {
                "type": "string",
                "description": "",
                "default": ""
              },
              "licenseDetails": {
                "$ref": "#/components/schemas/LicenseDetails"
              },
              "licenseAttrib": {
                "$ref": "#/components/schemas/SAttrib1_N"
              },
              "score": {
                "$ref": "#/components/schemas/SocketScore"
              },
              "alerts": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/SocketAlert"
                },
                "description": ""
              }
            },
            "required": [
              "diffType"
            ]
          }
        ]
      },
      "Capabilities": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "env": {
            "type": "boolean",
            "default": false,
            "description": "Package can read or modify environment variables"
          },
          "eval": {
            "type": "boolean",
            "default": false,
            "description": "Package uses dynamic code evaluation (eval, Function constructor, etc.)"
          },
          "fs": {
            "type": "boolean",
            "default": false,
            "description": "Package can read or write to the file system"
          },
          "net": {
            "type": "boolean",
            "default": false,
            "description": "Package can make network requests or create servers"
          },
          "shell": {
            "type": "boolean",
            "default": false,
            "description": "Package can execute shell commands or spawn processes"
          },
          "unsafe": {
            "type": "boolean",
            "default": false,
            "description": "Package uses unsafe or dangerous operations that could compromise security"
          },
          "url": {
            "type": "boolean",
            "default": false,
            "description": "Package contains remote URL(s) in the source code"
          }
        },
        "required": [
          "env",
          "eval",
          "fs",
          "net",
          "shell",
          "unsafe",
          "url"
        ]
      },
      "Qualifiers": {},
      "SocketScore": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "license": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 evaluating license permissiveness and compatibility",
            "default": 0
          },
          "maintenance": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 evaluating project maintenance health and activity",
            "default": 0
          },
          "overall": {
            "type": "number",
            "description": "Combined score from 0.0 to 1.0 representing overall package health and safety",
            "default": 0
          },
          "quality": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 evaluating code quality, testing, and documentation",
            "default": 0
          },
          "supplyChain": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 evaluating supply chain security and provenance",
            "default": 0
          },
          "vulnerability": {
            "type": "number",
            "description": "Score from 0.0 to 1.0 based on known vulnerabilities and their severity",
            "default": 0
          }
        },
        "required": [
          "license",
          "maintenance",
          "overall",
          "quality",
          "supplyChain",
          "vulnerability"
        ]
      },
      "SocketManifestReference": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "file": {
            "type": "string",
            "description": "Path to the manifest file (e.g., package.json, pom.xml)",
            "default": ""
          },
          "start": {
            "type": "integer",
            "description": "Starting line or position in the manifest file",
            "default": 0
          },
          "end": {
            "type": "integer",
            "description": "Ending line or position in the manifest file",
            "default": 0
          }
        },
        "required": [
          "file"
        ]
      },
      "SocketId": {
        "type": "string",
        "description": "",
        "default": ""
      },
      "SocketPURL": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "type": {
            "$ref": "#/components/schemas/SocketPURL_Type"
          },
          "namespace": {
            "type": "string",
            "description": "Package namespace or scope, such as npm organizations (@angular), Maven groupIds, or Docker image owners",
            "default": ""
          },
          "name": {
            "type": "string",
            "description": "Package name within its ecosystem",
            "default": ""
          },
          "version": {
            "type": "string",
            "description": "Package version string",
            "default": ""
          },
          "subpath": {
            "type": "string",
            "description": "Path within the package to a specific file or directory, used to reference nested components",
            "default": ""
          },
          "release": {
            "type": "string",
            "description": "Package-specific release identifier, such as PyPI's artifact ID or the specific build/release version",
            "default": ""
          }
        },
        "required": [
          "type"
        ]
      },
      "SocketAlert": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "key": {
            "type": "string",
            "description": "Unique identifier for this alert instance, used for deduplication and tracking across scans",
            "default": ""
          },
          "type": {
            "type": "string",
            "description": "Alert type identifier referencing the alert type definition",
            "default": ""
          },
          "severity": {
            "$ref": "#/components/schemas/SocketIssueSeverity"
          },
          "category": {
            "$ref": "#/components/schemas/SocketCategory"
          },
          "file": {
            "type": "string",
            "description": "File path where this alert was detected",
            "default": ""
          },
          "start": {
            "type": "integer",
            "description": "Starting position of the alert in the file",
            "default": 0
          },
          "end": {
            "type": "integer",
            "description": "Ending position of the alert in the file",
            "default": 0
          },
          "props": {
            "type": "object",
            "description": "Additional alert-specific properties and metadata that vary by alert type",
            "default": null
          },
          "action": {
            "type": "string",
            "description": "Action to take for this alert (e.g., error, warn, ignore)",
            "default": ""
          },
          "actionSource": {
            "type": "object",
            "additionalProperties": false,
            "description": "",
            "properties": {
              "type": {
                "type": "string",
                "description": "Type of action source (e.g., policy, override)",
                "default": ""
              },
              "candidates": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "type": {
                      "type": "string",
                      "description": "Type of action candidate",
                      "default": ""
                    },
                    "action": {
                      "type": "string",
                      "description": "Proposed action for this candidate",
                      "default": ""
                    },
                    "actionPolicyIndex": {
                      "type": "integer",
                      "description": "Index of the policy rule for this candidate",
                      "default": 0
                    },
                    "repoLabelId": {
                      "type": "string",
                      "description": "Repository label ID associated with this candidate",
                      "default": ""
                    }
                  },
                  "required": [
                    "action",
                    "actionPolicyIndex",
                    "repoLabelId",
                    "type"
                  ]
                },
                "description": ""
              }
            },
            "required": [
              "candidates",
              "type"
            ]
          },
          "actionPolicyIndex": {
            "type": "integer",
            "description": "Index of the policy rule that triggered this action, for traceability to security policies",
            "default": 0
          },
          "fix": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "type": {
                "type": "string",
                "description": "Type of fix available (e.g., upgrade, remove, cve)",
                "default": ""
              },
              "description": {
                "type": "string",
                "description": "Human-readable description of how to fix this issue",
                "default": ""
              },
              "patch": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "uuid": {
                      "type": "string",
                      "description": "Unique identifier for this patch",
                      "default": ""
                    },
                    "tier": {
                      "type": "string",
                      "enum": [
                        "free",
                        "paid"
                      ],
                      "description": "Access tier required for this patch (free or paid)",
                      "default": "free"
                    },
                    "deprecated": {
                      "type": "boolean",
                      "default": false,
                      "description": "Indicates if this patch is deprecated and should not be used"
                    }
                  },
                  "required": [
                    "tier",
                    "uuid"
                  ]
                },
                "description": "Patches available to fix this specific alert"
              }
            },
            "required": [
              "description",
              "type"
            ]
          },
          "patch": {
            "$ref": "#/components/schemas/SocketPatch"
          },
          "reachability": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "head": {
                "$ref": "#/components/schemas/ReachabilityResult"
              },
              "base": {
                "$ref": "#/components/schemas/ReachabilityResult"
              }
            },
            "description": ""
          },
          "subType": {
            "type": "string",
            "description": "Generic alert sub-type",
            "default": ""
          }
        },
        "required": [
          "key",
          "type"
        ]
      },
      "LicenseDetails": {
        "type": "array",
        "items": {
          "type": "object",
          "additionalProperties": false,
          "description": "",
          "properties": {
            "spdxDisj": {
              "type": "string",
              "description": "SPDX license expression in disjunctive normal form (e.g., '(MIT OR Apache-2.0)')",
              "default": ""
            },
            "authors": {
              "type": "array",
              "items": {
                "type": "string",
                "description": "",
                "default": ""
              },
              "description": "List of authors found in the license text"
            },
            "errorData": {
              "type": "string",
              "description": "Error details if license parsing failed",
              "default": ""
            },
            "provenance": {
              "type": "string",
              "description": "Source where this license information was detected (e.g., 'package.json', 'LICENSE file', 'README')",
              "default": ""
            },
            "filepath": {
              "type": "string",
              "description": "Path to the file containing this license information",
              "default": ""
            },
            "match_strength": {
              "type": "number",
              "description": "Confidence score from 0.0 to 1.0 indicating how well the detected license matches the source text",
              "default": 0
            }
          },
          "required": [
            "authors",
            "errorData",
            "filepath",
            "match_strength",
            "provenance",
            "spdxDisj"
          ]
        },
        "description": ""
      },
      "SAttrib1_N": {
        "type": "array",
        "items": {
          "type": "object",
          "additionalProperties": false,
          "description": "",
          "properties": {
            "attribText": {
              "type": "string",
              "description": "Full text of the license attribution or copyright notice found in the package",
              "default": ""
            },
            "attribData": {
              "type": "array",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "description": "",
                "properties": {
                  "purl": {
                    "type": "string",
                    "description": "Package URL this attribution applies to",
                    "default": ""
                  },
                  "foundInFilepath": {
                    "type": "string",
                    "description": "File path where this attribution was found",
                    "default": ""
                  },
                  "spdxExpr": {
                    "type": "string",
                    "description": "SPDX license expression parsed from the attribution text",
                    "default": ""
                  },
                  "foundAuthors": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "description": "Authors mentioned in this attribution"
                  }
                },
                "required": [
                  "foundAuthors",
                  "foundInFilepath",
                  "purl",
                  "spdxExpr"
                ]
              },
              "description": ""
            }
          },
          "required": [
            "attribData",
            "attribText"
          ]
        },
        "description": ""
      },
      "SocketArtifactLink": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "direct": {
            "type": "boolean",
            "default": false,
            "description": "Indicates if this is a direct dependency (not transitive)"
          },
          "dev": {
            "type": "boolean",
            "default": false,
            "description": "Indicates if this is a development-only dependency not used in production"
          },
          "dead": {
            "type": "boolean",
            "default": false,
            "description": "Indicates if this package is deprecated, abandoned, or no longer maintained"
          },
          "manifestFiles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SocketManifestReference"
            },
            "description": ""
          },
          "topLevelAncestors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SocketId"
            },
            "description": "IDs of the root-level packages in the dependency tree that depend on this package"
          },
          "dependencies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SocketId"
            },
            "description": "IDs of packages that this package directly depends on"
          },
          "alertPriorities": {
            "type": "object",
            "additionalProperties": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "result": {
                  "type": "integer",
                  "description": "Computed priority score for this alert",
                  "default": 0
                },
                "components": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "isFixable": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "result": {
                          "type": "number",
                          "description": "Contribution of fixability to the priority score",
                          "default": 0
                        },
                        "value": {
                          "type": "boolean",
                          "default": false,
                          "description": "Whether a fix is available for this alert"
                        }
                      },
                      "required": [
                        "result",
                        "value"
                      ]
                    },
                    "isReachable": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "result": {
                          "type": "number",
                          "description": "Contribution of reachability to the priority score",
                          "default": 0
                        },
                        "value": {
                          "type": "boolean",
                          "default": false,
                          "description": "Whether the vulnerable code is reachable"
                        },
                        "specificValue": {
                          "type": "string",
                          "description": "Specific reachability type value such as 'unreachable', 'maybe_reachable', or 'reachable'",
                          "default": ""
                        }
                      },
                      "required": [
                        "result",
                        "specificValue",
                        "value"
                      ]
                    },
                    "severity": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "result": {
                          "type": "number",
                          "description": "Contribution of severity to the priority score",
                          "default": 0
                        },
                        "value": {
                          "type": "integer",
                          "description": "Numeric severity level",
                          "default": 0
                        }
                      },
                      "required": [
                        "result",
                        "value"
                      ]
                    }
                  },
                  "required": [
                    "isFixable",
                    "isReachable",
                    "severity"
                  ]
                },
                "formula": {
                  "type": "string",
                  "description": "Formula used to calculate the priority score",
                  "default": ""
                }
              },
              "required": [
                "result"
              ]
            },
            "properties": {},
            "description": "Computed priority scores for each alert type based on severity, reachability, and fixability factors"
          },
          "artifact": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SocketPURL"
              },
              {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "id": {
                    "$ref": "#/components/schemas/SocketId"
                  }
                },
                "required": [
                  "id"
                ]
              }
            ]
          },
          "alertKeysToReachabilityTypes": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "description": "",
                "default": ""
              },
              "description": ""
            },
            "properties": {},
            "description": "Deprecated: mapping of alert keys to arrays of reachability types found across different manifest files or code locations. This field is derived from alertKeysToReachabilitySummaries for backward compatibility; use that property instead."
          },
          "alertKeysToReachabilitySummaries": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "description": "",
                "properties": {
                  "type": {
                    "type": "string",
                    "description": "",
                    "default": ""
                  }
                },
                "required": [
                  "type"
                ]
              },
              "description": ""
            },
            "properties": {},
            "description": "Mapping of alert keys to arrays of reachability summaries. Each summary contains a reachability type indicating the result of reachability analysis for the corresponding vulnerability alert."
          }
        },
        "description": ""
      },
      "SocketDiffArtifactType": {
        "type": "string",
        "enum": [
          "added",
          "removed",
          "updated",
          "replaced",
          "unchanged"
        ],
        "description": "Type of change detected for this artifact in the diff",
        "default": "unchanged"
      },
      "SocketPURL_Type": {
        "type": "string",
        "enum": [
          "alpm",
          "apk",
          "bitbucket",
          "cocoapods",
          "cargo",
          "chrome",
          "clawhub",
          "composer",
          "conan",
          "conda",
          "cran",
          "deb",
          "docker",
          "gem",
          "generic",
          "github",
          "golang",
          "hackage",
          "hex",
          "huggingface",
          "maven",
          "mlflow",
          "npm",
          "nuget",
          "qpkg",
          "oci",
          "pub",
          "pypi",
          "rpm",
          "socket",
          "swid",
          "swift",
          "vscode",
          "unknown"
        ],
        "description": "Package ecosystem type identifier based on the PURL specification",
        "default": "unknown"
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
      "SocketPatch": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "uuid": {
            "type": "string",
            "description": "Unique identifier for this patch",
            "default": ""
          },
          "tier": {
            "type": "string",
            "enum": [
              "free",
              "paid"
            ],
            "description": "Access tier required for this patch (free or paid)",
            "default": "free"
          },
          "deprecated": {
            "type": "boolean",
            "default": false,
            "description": "Indicates if this patch is deprecated and should not be used"
          }
        },
        "required": [
          "tier",
          "uuid"
        ]
      },
      "ReachabilityResult": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "precomputed",
              "full-scan"
            ],
            "description": "Type of reachability analysis performed",
            "default": "precomputed"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ReachabilityResultItem"
            },
            "description": "Reachability analysis results for each vulnerability"
          }
        },
        "required": [
          "results",
          "type"
        ]
      },
      "ReachabilityResultItem": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "type": {
            "$ref": "#/components/schemas/ReachabilityType"
          },
          "truncated": {
            "type": "boolean",
            "default": false,
            "description": "Indicates if the reachability analysis was stopped early due to depth or complexity limits"
          },
          "error": {
            "type": "string",
            "description": "Error message if reachability analysis failed",
            "default": ""
          },
          "matches": {
            "anyOf": [
              {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": [
                      "function-level"
                    ]
                  },
                  "value": {
                    "type": "array",
                    "items": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/CallStackItem"
                      },
                      "description": ""
                    },
                    "description": ""
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
                      "class-level"
                    ]
                  },
                  "value": {
                    "type": "array",
                    "items": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/ClassStackItem"
                      },
                      "description": ""
                    },
                    "description": ""
                  }
                }
              }
            ]
          },
          "workspacePath": {
            "type": "string",
            "description": "Path to the workspace root for multi-workspace projects",
            "default": ""
          },
          "subprojectPath": {
            "type": "string",
            "description": "Path to the subproject within the workspace",
            "default": ""
          }
        },
        "required": [
          "type"
        ]
      },
      "ReachabilityType": {
        "type": "string",
        "enum": [
          "missing_support",
          "undeterminable_reachability",
          "pending",
          "unreachable",
          "unknown",
          "direct_dependency",
          "error",
          "maybe_reachable",
          "reachable"
        ],
        "description": "Status of reachability analysis for vulnerable code paths",
        "default": "unknown"
      },
      "CallStackItem": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "purl": {
            "type": "string",
            "description": "Package URL (PURL) of the dependency containing this code",
            "default": ""
          },
          "sourceLocation": {
            "$ref": "#/components/schemas/SourceLocation"
          },
          "confidence": {
            "type": "number",
            "description": "Confidence score from 0.0 to 1.0 indicating how certain the reachability analysis is about this result",
            "default": 0
          }
        },
        "description": ""
      },
      "ClassStackItem": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "purl": {
            "type": "string",
            "description": "Package URL (PURL) of the dependency containing this class",
            "default": ""
          },
          "class": {
            "type": "string",
            "description": "Name of the class in the dependency",
            "default": ""
          },
          "confidence": {
            "type": "number",
            "description": "Confidence score from 0.0 to 1.0 indicating how certain the reachability analysis is about this result",
            "default": 0
          }
        },
        "description": ""
      },
      "SourceLocation": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "start": {
            "type": "object",
            "additionalProperties": false,
            "description": "",
            "properties": {
              "line": {
                "type": "integer",
                "description": "Line number in the source file",
                "default": 0
              },
              "column": {
                "type": "integer",
                "description": "Column number in the source file",
                "default": 0
              },
              "byteOffset": {
                "type": "integer",
                "description": "Absolute byte position from the beginning of the file, used for precise location tracking",
                "default": 0
              }
            },
            "required": [
              "byteOffset",
              "column",
              "line"
            ]
          },
          "end": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "line": {
                "type": "integer",
                "description": "Line number in the source file",
                "default": 0
              },
              "column": {
                "type": "integer",
                "description": "Column number in the source file",
                "default": 0
              },
              "byteOffset": {
                "type": "integer",
                "description": "Absolute byte position from the beginning of the file, used for precise location tracking",
                "default": 0
              }
            },
            "description": ""
          },
          "filename": {
            "type": "string",
            "description": "Path to the source file",
            "default": ""
          },
          "fileHash": {
            "type": "string",
            "description": "Hash of the source file for integrity verification",
            "default": ""
          }
        },
        "required": [
          "end",
          "fileHash",
          "filename",
          "start"
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
    "/orgs/{org_slug}/full-scans/diff": {
      "get": {
        "tags": [
          "deprecated"
        ],
        "summary": "Diff Full Scans",
        "deprecated": true,
        "operationId": "GetOrgDiffScan",
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
            "name": "after",
            "in": "query",
            "required": true,
            "description": "The full scan ID of the base/target of the diff (older)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "before",
            "in": "query",
            "required": true,
            "description": "The full scan ID of the head/changed side of the diff (newer)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "include_license_details",
            "in": "query",
            "required": false,
            "description": "Include license details in the response. This can increase the response size significantly.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "omit_unchanged",
            "in": "query",
            "required": false,
            "description": "Omit unchanged artifacts from the response. When set to true, the unchanged field will be set to null.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "full-scans:list"
            ]
          },
          {
            "basicAuth": [
              "full-scans:list"
            ]
          }
        ],
        "description": "**This endpoint is deprecated.**\n\nGet the difference between two existing Full Scans. The results are not persisted.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- full-scans:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "before": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "id": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "created_at": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "updated_at": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "organization_id": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "organization_slug": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "repository_id": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "repository_slug": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "branch": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        },
                        "commit_message": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        },
                        "commit_hash": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        },
                        "pull_request": {
                          "type": "integer",
                          "description": "",
                          "default": 0,
                          "nullable": true
                        },
                        "committers": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "description": ""
                        },
                        "html_url": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        },
                        "api_url": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        }
                      },
                      "required": [
                        "api_url",
                        "branch",
                        "commit_hash",
                        "commit_message",
                        "committers",
                        "created_at",
                        "html_url",
                        "id",
                        "organization_id",
                        "organization_slug",
                        "pull_request",
                        "repository_id",
                        "repository_slug",
                        "updated_at"
                      ]
                    },
                    "after": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "id": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "created_at": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "updated_at": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "organization_id": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "organization_slug": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "repository_id": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "repository_slug": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "branch": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        },
                        "commit_message": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        },
                        "commit_hash": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        },
                        "pull_request": {
                          "type": "integer",
                          "description": "",
                          "default": 0,
                          "nullable": true
                        },
                        "committers": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "description": ""
                        },
                        "html_url": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        },
                        "api_url": {
                          "type": "string",
                          "description": "",
                          "default": "",
                          "nullable": true
                        }
                      },
                      "required": [
                        "api_url",
                        "branch",
                        "commit_hash",
                        "commit_message",
                        "committers",
                        "created_at",
                        "html_url",
                        "id",
                        "organization_id",
                        "organization_slug",
                        "pull_request",
                        "repository_id",
                        "repository_slug",
                        "updated_at"
                      ]
                    },
                    "artifacts": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "added": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/SocketDiffArtifact"
                          },
                          "description": ""
                        },
                        "removed": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/SocketDiffArtifact"
                          },
                          "description": ""
                        },
                        "unchanged": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/SocketDiffArtifact"
                          },
                          "description": "",
                          "nullable": true
                        },
                        "replaced": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/SocketDiffArtifact"
                          },
                          "description": ""
                        },
                        "updated": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/SocketDiffArtifact"
                          },
                          "description": ""
                        }
                      },
                      "required": [
                        "added",
                        "removed",
                        "replaced",
                        "unchanged",
                        "updated"
                      ]
                    },
                    "directDependenciesChanged": {
                      "type": "boolean",
                      "default": false,
                      "description": ""
                    },
                    "diff_report_url": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    }
                  },
                  "required": [
                    "after",
                    "artifacts",
                    "before",
                    "diff_report_url",
                    "directDependenciesChanged"
                  ]
                }
              }
            },
            "description": "The difference between the two provided Full Scans."
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