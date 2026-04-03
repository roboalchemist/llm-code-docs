# Source: https://docs.jfrog.com/security/reference/add-custom-license.md

# Add Custom License

Assigns a license to a single component in Xray. The license must be a known license (already existing in the system). The request body contains a `component` object identifying the target and a `license` object specifying which license to assign.

Requires a valid user with MANAGE_DATA permission.


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
    "/api/v1/licenses/assign": {
      "post": {
        "operationId": "add-custom-license",
        "summary": "Add Custom License",
        "description": "Assigns a license to a single component in Xray. The license must be a known license (already existing in the system). The request body contains a `component` object identifying the target and a `license` object specifying which license to assign.\n\nRequires a valid user with MANAGE_DATA permission.\n",
        "tags": [
          "Legal V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/LegalAssignCustomLicenseRequest"
              },
              "example": {
                "component": {
                  "package_id": "npm://lodash",
                  "component_name": "lodash",
                  "pkg_type": "npm",
                  "version": "4.17.21"
                },
                "license": {
                  "name": "MIT",
                  "aliases": [
                    "MIT License"
                  ]
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "License successfully added to the component.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string",
                      "description": "Success message."
                    }
                  }
                },
                "example": {
                  "info": "license 'MIT' has been successfully added to component 'npm://lodash'"
                }
              }
            }
          },
          "415": {
            "description": "Failed to parse request, or the license name is not a known license.\n",
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
                  "error": "License name is not valid"
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
                },
                "example": {
                  "error": "Failed to add license to component"
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
    },
    "schemas": {
      "LegalAssignCustomLicenseRequest": {
        "type": "object",
        "description": "Request body for assigning a license to a component.",
        "required": [
          "component",
          "license"
        ],
        "properties": {
          "component": {
            "type": "object",
            "description": "Identifies the component to assign the license to.",
            "required": [
              "package_id"
            ],
            "properties": {
              "package_id": {
                "type": "string",
                "description": "Package identifier (e.g., npm://lodash, build://my-build).",
                "example": "npm://lodash"
              },
              "component_name": {
                "type": "string",
                "description": "Component name.",
                "example": "lodash"
              },
              "pkg_type": {
                "type": "string",
                "description": "Package type (e.g., npm, maven, pypi).",
                "example": "npm"
              },
              "version": {
                "type": "string",
                "description": "Component version.",
                "example": "4.17.21"
              },
              "distribution": {
                "type": "string",
                "description": "Distribution identifier for remote repositories."
              },
              "build_repo": {
                "type": "string",
                "description": "Build repository name. Required for build:// components."
              }
            }
          },
          "license": {
            "type": "object",
            "description": "Specifies the license to assign. Must be a known license.",
            "required": [
              "name"
            ],
            "properties": {
              "name": {
                "type": "string",
                "description": "License identifier. Must be a known license in the system.",
                "example": "MIT"
              },
              "full_name": {
                "type": "string",
                "description": "Full display name of the license.",
                "example": "The MIT License"
              },
              "references": {
                "type": "array",
                "description": "Array of reference URLs for the license.",
                "items": {
                  "type": "string"
                }
              },
              "aliases": {
                "type": "array",
                "description": "Array of alternative names for the license.",
                "items": {
                  "type": "string"
                },
                "example": [
                  "MIT License"
                ]
              }
            }
          }
        }
      }
    }
  },
  "tags": [
    {
      "name": "Legal V1",
      "description": "APIs from Legal V1"
    }
  ]
}
```