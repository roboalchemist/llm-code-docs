# Source: https://docs.jfrog.com/security/reference/createwaiverrequest.md

# Create a waiver request

Create a waiver request to unblock a package that was blocked by a curation policy. The policy must have `waiver_request_config` set to `manual` or `auto_approved`.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Curation API",
    "description": "Public REST API for JFrog Curation — policy-based governance of open-source\npackages flowing through JFrog Artifactory remote repositories.\n\nCuration lets you define **conditions** (e.g. \"package has a critical CVE\")\nand attach them to **policies** that either block or audit (dry-run)\nnon-compliant packages. **Waiver requests** allow users to request\nunblocking of a package, and the **audit** endpoint provides full export of\nall approved/blocked events.\n",
    "version": "1.0.0",
    "license": {
      "name": "Proprietary"
    },
    "contact": {
      "name": "JFrog"
    }
  },
  "servers": [
    {
      "url": "{protocol}://{host}:{port}/xray",
      "description": "JFrog Platform (Xray service)",
      "variables": {
        "protocol": {
          "default": "https",
          "enum": [
            "http",
            "https"
          ]
        },
        "host": {
          "default": "localhost"
        },
        "port": {
          "default": "8046"
        }
      }
    }
  ],
  "security": [],
  "tags": [
    {
      "name": "Waiver Requests",
      "description": "Request and list waivers for blocked packages."
    }
  ],
  "paths": {
    "/api/v1/curation/waiver_requests": {
      "post": {
        "operationId": "createWaiverRequest",
        "tags": [
          "Waiver Requests"
        ],
        "summary": "Create a waiver request",
        "description": "Create a waiver request to unblock a package that was blocked by a curation policy. The policy must have `waiver_request_config` set to `manual` or `auto_approved`.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WaiverRequestCreate"
              },
              "example": {
                "pkg_name": "lodash",
                "pkg_version": "4.17.21",
                "pkg_type": "npm",
                "repo_key": "remote-npm-repo",
                "reason": "Required for backward compatibility"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "message",
                    "id"
                  ],
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "Success message."
                    },
                    "id": {
                      "type": "integer",
                      "format": "int64",
                      "description": "Unique identifier of the newly created waiver request."
                    }
                  }
                },
                "example": {
                  "message": "Successfully created waiver request",
                  "id": 42
                }
              }
            }
          },
          "400": {
            "$ref": "#/components/responses/BadRequest"
          },
          "403": {
            "description": "Permission denied."
          }
        }
      }
    }
  },
  "components": {
    "responses": {
      "BadRequest": {
        "description": "Bad request — validation error or invalid parameters.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/Error"
            }
          }
        }
      }
    },
    "schemas": {
      "WaiverRequestCreate": {
        "type": "object",
        "required": [
          "pkg_type",
          "pkg_name",
          "pkg_version",
          "reason"
        ],
        "properties": {
          "pkg_type": {
            "type": "string",
            "description": "Package type (e.g. `npm`, `pypi`, `maven`)."
          },
          "pkg_name": {
            "type": "string",
            "description": "Name of the package."
          },
          "pkg_version": {
            "type": "string",
            "description": "Version of the package."
          },
          "repo_key": {
            "type": "string",
            "description": "Repository key where the package was blocked."
          },
          "reason": {
            "type": "string",
            "description": "Justification for the waiver request."
          }
        }
      },
      "Error": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Error message."
          }
        }
      }
    }
  }
}
```