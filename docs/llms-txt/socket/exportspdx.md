# Source: https://docs.socket.dev/reference/exportspdx.md

# Export SPDX SBOM (Beta)

Export a Socket SBOM as a SPDX SBOM

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
      "SPDXManifestSchema": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "spdxVersion": {
            "type": "string",
            "description": "",
            "default": "SPDX-2.3"
          },
          "dataLicense": {
            "type": "string",
            "description": "",
            "default": "CC0-1.0"
          },
          "SPDXID": {
            "type": "string",
            "description": "",
            "default": "SPDXRef-DOCUMENT"
          },
          "name": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "documentNamespace": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "creationInfo": {
            "type": "object",
            "additionalProperties": false,
            "description": "",
            "properties": {
              "created": {
                "type": "string",
                "description": "",
                "default": ""
              },
              "creators": {
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
              "created",
              "creators"
            ]
          },
          "documentDescribes": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "",
              "default": ""
            },
            "description": ""
          },
          "packages": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "name": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "SPDXID": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "versionInfo": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "packageFileName": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "description": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "primaryPackagePurpose": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "downloadLocation": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "filesAnalyzed": {
                  "type": "boolean",
                  "default": false,
                  "description": ""
                },
                "homepage": {
                  "type": "string",
                  "description": "",
                  "default": "NOASSERTION"
                },
                "licenseDeclared": {
                  "type": "string",
                  "description": "",
                  "default": "NOASSERTION"
                },
                "externalRefs": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "description": "",
                    "properties": {
                      "referenceCategory": {
                        "type": "string",
                        "description": "",
                        "default": "PACKAGE-MANAGER"
                      },
                      "referenceType": {
                        "type": "string",
                        "description": "",
                        "default": "purl"
                      },
                      "referenceLocator": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      }
                    },
                    "required": [
                      "referenceCategory",
                      "referenceLocator",
                      "referenceType"
                    ]
                  },
                  "description": ""
                },
                "checksums": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "description": "",
                    "properties": {
                      "algorithm": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "checksumValue": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      }
                    },
                    "required": [
                      "algorithm",
                      "checksumValue"
                    ]
                  },
                  "description": ""
                }
              },
              "required": [
                "SPDXID",
                "externalRefs",
                "filesAnalyzed",
                "homepage",
                "licenseDeclared",
                "name",
                "packageFileName",
                "versionInfo"
              ]
            },
            "description": ""
          },
          "relationships": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "spdxElementId": {
                  "type": "string",
                  "description": "",
                  "default": "SPDXRef-DOCUMENT"
                },
                "relatedSpdxElement": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "relationshipType": {
                  "type": "string",
                  "description": "",
                  "default": "DESCRIBES"
                }
              },
              "required": [
                "relatedSpdxElement",
                "relationshipType",
                "spdxElementId"
              ]
            },
            "description": ""
          }
        },
        "required": [
          "SPDXID",
          "creationInfo",
          "dataLicense",
          "documentDescribes",
          "documentNamespace",
          "name",
          "packages",
          "relationships",
          "spdxVersion"
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
    "/orgs/{org_slug}/export/spdx/{id}": {
      "get": {
        "tags": [
          "full-scans"
        ],
        "summary": "Export SPDX SBOM (Beta)",
        "operationId": "exportSPDX",
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
        "description": "Export a Socket SBOM as a SPDX SBOM\n\nSupported ecosystems:\n\n- crates\n- go\n- maven\n- npm\n- nuget\n- pypi\n- rubygems\n- spdx\n- cdx\n\nUnsupported ecosystems are filtered from the export.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- report:read",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SPDXManifestSchema"
                }
              }
            },
            "description": "SPDX SBOM"
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