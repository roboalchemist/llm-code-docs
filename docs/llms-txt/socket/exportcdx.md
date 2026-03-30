# Source: https://docs.socket.dev/reference/exportcdx.md

# Export CycloneDX SBOM (Beta)

Export a Socket SBOM as a CycloneDX SBOM

Supported ecosystems:

- crates
- go
- maven
- npm
- nuget
- pypi
- rubygems
- spdx
- cdx

Unsupported ecosystems are filtered from the export.

This endpoint consumes 1 unit of your quota.

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
      "name": "full-scans"
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
      "CDXManifestSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "bomFormat": {
            "type": "string",
            "description": "",
            "default": "CycloneDX"
          },
          "specVersion": {
            "type": "string",
            "description": "",
            "default": "1.5"
          },
          "serialNumber": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "version": {
            "type": "number",
            "description": "",
            "default": 0
          },
          "metadata": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "timestamp": {
                "type": "string",
                "description": "",
                "default": ""
              },
              "tools": {
                "type": "object",
                "additionalProperties": false,
                "description": "",
                "properties": {
                  "components": {
                    "type": "array",
                    "items": {
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/CDXComponentSchema"
                        },
                        {
                          "type": "object",
                          "additionalProperties": false,
                          "properties": {
                            "author": {
                              "type": "string",
                              "description": "",
                              "default": "Socket"
                            },
                            "authors": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": "Socket"
                              },
                              "description": ""
                            },
                            "publisher": {
                              "type": "string",
                              "description": "",
                              "default": "Socket"
                            }
                          }
                        }
                      ]
                    },
                    "description": ""
                  }
                },
                "required": [
                  "components"
                ]
              },
              "authors": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "name": {
                      "type": "string",
                      "description": "",
                      "default": "Socket"
                    }
                  },
                  "required": [
                    "name"
                  ]
                },
                "description": ""
              },
              "supplier": {
                "type": "string",
                "description": "",
                "default": ""
              },
              "lifecycles": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "phase": {
                      "type": "string",
                      "description": "",
                      "default": "build"
                    }
                  },
                  "required": [
                    "phase"
                  ]
                },
                "description": ""
              },
              "component": {
                "$ref": "#/components/schemas/CDXComponentSchema"
              },
              "properties": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "name": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "value": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "required": [
                    "name",
                    "value"
                  ]
                },
                "description": ""
              }
            },
            "required": [
              "authors",
              "component",
              "lifecycles",
              "timestamp",
              "tools"
            ]
          },
          "components": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CDXComponentSchema"
            },
            "description": ""
          },
          "dependencies": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "ref": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "dependsOn": {
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
                "ref"
              ]
            },
            "description": ""
          },
          "vulnerabilities": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "id": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "ref": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "source": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "name": {
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
                  "description": ""
                },
                "ratings": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "source": {
                        "type": "object",
                        "additionalProperties": false,
                        "properties": {
                          "name": {
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
                        "description": ""
                      },
                      "score": {
                        "type": "number",
                        "description": "",
                        "default": 0
                      },
                      "severity": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "method": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "vector": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      }
                    },
                    "description": ""
                  },
                  "description": ""
                },
                "cwes": {
                  "type": "array",
                  "items": {
                    "type": "number",
                    "description": "",
                    "default": 0
                  },
                  "description": ""
                },
                "description": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "detail": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "recommendation": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "advisories": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "url": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "title": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      }
                    },
                    "required": [
                      "url"
                    ]
                  },
                  "description": ""
                },
                "created": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "published": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "updated": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "affects": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "ref": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "versions": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "additionalProperties": false,
                          "properties": {
                            "version": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            },
                            "status": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            }
                          },
                          "description": ""
                        },
                        "description": ""
                      }
                    },
                    "required": [
                      "ref"
                    ]
                  },
                  "description": ""
                },
                "analysis": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "state": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "justification": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "response": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "description": ""
                    },
                    "detail": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "firstIssued": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "lastUpdated": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "description": ""
                }
              },
              "required": [
                "id"
              ]
            },
            "description": ""
          }
        },
        "required": [
          "bomFormat",
          "components",
          "dependencies",
          "metadata",
          "serialNumber",
          "specVersion",
          "version"
        ]
      },
      "CDXComponentSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "author": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "publisher": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "group": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "name": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "version": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "description": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "scope": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "hashes": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "alg": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "content": {
                  "type": "string",
                  "description": "",
                  "default": ""
                }
              },
              "required": [
                "alg",
                "content"
              ]
            },
            "description": ""
          },
          "licenses": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "expression": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "license": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "id": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "name": {
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
                  "description": ""
                }
              },
              "description": ""
            },
            "description": ""
          },
          "purl": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "externalReferences": {
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
                },
                "url": {
                  "type": "string",
                  "description": "",
                  "default": ""
                }
              },
              "required": [
                "type",
                "url"
              ]
            },
            "description": ""
          },
          "type": {
            "type": "string",
            "description": "",
            "default": "application"
          },
          "bom-ref": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "evidence": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "identity": {
                "type": "object",
                "additionalProperties": false,
                "description": "",
                "properties": {
                  "field": {
                    "type": "string",
                    "description": "",
                    "default": ""
                  },
                  "confidence": {
                    "type": "number",
                    "description": "",
                    "default": 0
                  },
                  "methods": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "technique": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "confidence": {
                          "type": "number",
                          "description": "",
                          "default": 0
                        },
                        "value": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        }
                      },
                      "required": [
                        "confidence",
                        "technique",
                        "value"
                      ]
                    },
                    "description": ""
                  }
                },
                "required": [
                  "confidence",
                  "field",
                  "methods"
                ]
              },
              "occurrences": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "location": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "required": [
                    "location"
                  ]
                },
                "description": ""
              }
            },
            "required": [
              "identity"
            ]
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "",
              "default": ""
            },
            "description": ""
          },
          "properties": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "value": {
                  "type": "string",
                  "description": "",
                  "default": ""
                }
              },
              "required": [
                "name",
                "value"
              ]
            },
            "description": ""
          },
          "cryptoProperties": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "assetType": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "algorithmProperties": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "executionEnvironment": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "implementationPlatform": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "required": [
                    "executionEnvironment",
                    "implementationPlatform"
                  ]
                }
              },
              "required": [
                "algorithmProperties",
                "assetType"
              ]
            },
            "description": ""
          },
          "components": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CDXComponentSchema"
            },
            "description": ""
          }
        },
        "required": [
          "bom-ref",
          "group",
          "name",
          "purl",
          "type",
          "version"
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
    "/orgs/{org_slug}/export/cdx/{id}": {
      "get": {
        "tags": [
          "full-scans"
        ],
        "summary": "Export CycloneDX SBOM (Beta)",
        "operationId": "exportCDX",
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
            "name": "id",
            "in": "path",
            "required": true,
            "description": "The full scan OR sbom report ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "author",
            "in": "query",
            "required": false,
            "description": "The person(s) who created the BOM.\nSet this value if you're intending the modify the BOM and claim authorship.",
            "schema": {
              "type": "string",
              "default": "OWASP Foundation"
            }
          },
          {
            "name": "project_group",
            "in": "query",
            "required": false,
            "description": "Dependency track project group",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "project_name",
            "in": "query",
            "required": false,
            "description": "Dependency track project name. Default use the directory name",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "project_version",
            "in": "query",
            "required": false,
            "description": "Dependency track project version",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "project_id",
            "in": "query",
            "required": false,
            "description": "Dependency track project id. Either provide the id or the project name and version together",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "include_vulnerabilities",
            "in": "query",
            "required": false,
            "description": "Include vulnerability information in the SBOM. Also includes reachability/VEX if available",
            "schema": {
              "type": "string",
              "default": "false"
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
        "description": "Export a Socket SBOM as a CycloneDX SBOM\n\nSupported ecosystems:\n\n- crates\n- go\n- maven\n- npm\n- nuget\n- pypi\n- rubygems\n- spdx\n- cdx\n\nUnsupported ecosystems are filtered from the export.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- report:read",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CDXManifestSchema"
                }
              }
            },
            "description": "CycloneDX SBOM"
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