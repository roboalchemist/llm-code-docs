# Source: https://docs.socket.dev/reference/exportopenvex.md

# Export OpenVEX Document (Beta)

Export vulnerability exploitability data as an OpenVEX v0.2.0 document.

OpenVEX (Vulnerability Exploitability eXchange) documents communicate the
exploitability status of vulnerabilities in software products. This export
includes:

- **Patch data**: Vulnerabilities fixed by applied Socket patches are marked as "fixed"
- **Reachability analysis**: Code reachability determines if vulnerable code is exploitable:
- Unreachable code → "not_affected" with justification
- Reachable code → "affected"
- Unknown/pending → "under_investigation"

Each statement in the document represents a single artifact-vulnerability pair
for granular reachability information.

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
      "OpenVEXDocumentSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "@context": {
            "type": "string",
            "description": "",
            "default": "https://openvex.dev/ns/v0.2.0"
          },
          "@id": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "author": {
            "type": "string",
            "description": "",
            "default": "Socket Security"
          },
          "timestamp": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "version": {
            "type": "number",
            "description": "",
            "default": 1
          },
          "statements": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OpenVEXStatementSchema"
            },
            "description": ""
          },
          "role": {
            "type": "string",
            "description": "",
            "default": "VEX Generator"
          },
          "last_updated": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "tooling": {
            "type": "string",
            "description": "",
            "default": "Socket Security VEX Generator"
          }
        },
        "required": [
          "@context",
          "@id",
          "author",
          "statements",
          "timestamp",
          "version"
        ]
      },
      "OpenVEXStatementSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "vulnerability": {
            "$ref": "#/components/schemas/OpenVEXVulnerabilitySchema"
          },
          "products": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OpenVEXProductSchema"
            },
            "description": ""
          },
          "status": {
            "type": "string",
            "description": "",
            "default": "affected"
          },
          "@id": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "version": {
            "type": "number",
            "description": "",
            "default": 0
          },
          "timestamp": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "last_updated": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "supplier": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "status_notes": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "justification": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "impact_statement": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "action_statement": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "action_statement_timestamp": {
            "type": "string",
            "description": "",
            "default": ""
          }
        },
        "required": [
          "products",
          "status",
          "vulnerability"
        ]
      },
      "OpenVEXVulnerabilitySchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "@id": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "description": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "aliases": {
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
          "name"
        ]
      },
      "OpenVEXProductSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "@id": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "identifiers": {
            "$ref": "#/components/schemas/OpenVEXIdentifiersSchema"
          },
          "hashes": {
            "$ref": "#/components/schemas/OpenVEXHashesSchema"
          },
          "subcomponents": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OpenVEXComponentSchema"
            },
            "description": ""
          }
        },
        "required": [
          "@id"
        ]
      },
      "OpenVEXIdentifiersSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "purl": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "cpe23": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "cpe22": {
            "type": "string",
            "description": "",
            "default": ""
          }
        },
        "description": ""
      },
      "OpenVEXHashesSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "md5": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "sha1": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "sha-256": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "sha-384": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "sha-512": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "sha3-224": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "sha3-256": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "sha3-384": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "sha3-512": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "blake2s-256": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "blake2b-256": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "blake2b-512": {
            "type": "string",
            "description": "",
            "default": ""
          }
        },
        "description": ""
      },
      "OpenVEXComponentSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "@id": {
            "type": "string",
            "description": "",
            "default": ""
          },
          "identifiers": {
            "$ref": "#/components/schemas/OpenVEXIdentifiersSchema"
          },
          "hashes": {
            "$ref": "#/components/schemas/OpenVEXHashesSchema"
          }
        }
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
    "/orgs/{org_slug}/export/openvex/{id}": {
      "get": {
        "tags": [
          "full-scans"
        ],
        "summary": "Export OpenVEX Document (Beta)",
        "operationId": "exportOpenVEX",
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
            "description": "The author of the VEX document. Should be an individual or organization.",
            "schema": {
              "type": "string",
              "default": "Socket Security"
            }
          },
          {
            "name": "role",
            "in": "query",
            "required": false,
            "description": "The role of the document author (e.g., \"VEX Generator\", \"Security Team\").",
            "schema": {
              "type": "string",
              "default": "VEX Generator"
            }
          },
          {
            "name": "document_id",
            "in": "query",
            "required": false,
            "description": "Custom IRI for the VEX document. If not provided, a default IRI will be generated.",
            "schema": {
              "type": "string",
              "default": ""
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
        "description": "Export vulnerability exploitability data as an OpenVEX v0.2.0 document.\n\nOpenVEX (Vulnerability Exploitability eXchange) documents communicate the\nexploitability status of vulnerabilities in software products. This export\nincludes:\n\n- **Patch data**: Vulnerabilities fixed by applied Socket patches are marked as \"fixed\"\n- **Reachability analysis**: Code reachability determines if vulnerable code is exploitable:\n- Unreachable code → \"not_affected\" with justification\n- Reachable code → \"affected\"\n- Unknown/pending → \"under_investigation\"\n\nEach statement in the document represents a single artifact-vulnerability pair\nfor granular reachability information.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- report:read",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OpenVEXDocumentSchema"
                }
              }
            },
            "description": "OpenVEX v0.2.0 document"
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