# Source: https://docs.jfrog.com/security/reference/create-custom-license.md

# Create Custom License

Creates a custom license for license compliance management. Custom licenses are user-defined and can be assigned to components for tracking and compliance purposes. The license name must be unique and cannot exceed 128 characters. Aliases also have a 128 character limit each.

Requires Admin permission. Since Xray 3.132.0.


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
    "/api/v1/licensesNames/customLicense": {
      "post": {
        "operationId": "create-custom-license",
        "summary": "Create Custom License",
        "description": "Creates a custom license for license compliance management. Custom licenses are user-defined and can be assigned to components for tracking and compliance purposes. The license name must be unique and cannot exceed 128 characters. Aliases also have a 128 character limit each.\n\nRequires Admin permission. Since Xray 3.132.0.\n",
        "tags": [
          "Legal V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/LegalCreateCustomLicenseRequest"
              },
              "example": {
                "name": "MyCustomLicense",
                "full_name": "My Custom License Full Name",
                "text": "This is a custom license description",
                "references": [
                  "https://example.com/license",
                  "https://example.com/legal"
                ],
                "aliases": [
                  "MCL",
                  "MyLicense"
                ],
                "category": "Permissive"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Custom license created successfully. Returns the created license.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "example": "MyCustomLicense"
                    },
                    "full_name": {
                      "type": "string",
                      "example": "My Custom License Full Name"
                    },
                    "text": {
                      "type": "string"
                    },
                    "references": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    },
                    "aliases": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    },
                    "category": {
                      "type": "string",
                      "example": "Permissive"
                    },
                    "priority": {
                      "type": "integer"
                    },
                    "default_priority": {
                      "type": "integer"
                    },
                    "isCustom": {
                      "type": "boolean",
                      "description": "Always true for custom licenses.",
                      "example": true
                    }
                  }
                },
                "example": {
                  "name": "MyCustomLicense",
                  "full_name": "My Custom License Full Name",
                  "text": "This is a custom license description",
                  "references": [
                    "https://example.com/license",
                    "https://example.com/legal"
                  ],
                  "aliases": [
                    "MCL",
                    "MyLicense"
                  ],
                  "category": "Permissive",
                  "isCustom": true
                }
              }
            }
          },
          "400": {
            "description": "License name already exists, or validation failed (name or alias exceeds 128 characters).\n",
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
                  "error": "License name already exists"
                }
              }
            }
          },
          "415": {
            "description": "Failed to parse the request body.",
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
                  "error": "Failed to parse message"
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
                  "error": "Failed to set custom license"
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
      "LegalCreateCustomLicenseRequest": {
        "type": "object",
        "description": "Request body for creating a custom license. The name must be unique and cannot exceed 128 characters.\n",
        "required": [
          "name"
        ],
        "properties": {
          "name": {
            "type": "string",
            "description": "License key/identifier. Must be unique. Maximum 128 characters.",
            "example": "MyCustomLicense"
          },
          "full_name": {
            "type": "string",
            "description": "Full display name of the license.",
            "example": "My Custom License Full Name"
          },
          "text": {
            "type": "string",
            "description": "Description or full text of the license.",
            "example": "This is a custom license description"
          },
          "references": {
            "type": "array",
            "description": "Array of URLs or references related to the license.",
            "items": {
              "type": "string"
            },
            "example": [
              "https://example.com/license"
            ]
          },
          "aliases": {
            "type": "array",
            "description": "Array of alternative names. Each alias max 128 characters.",
            "items": {
              "type": "string"
            },
            "example": [
              "MCL",
              "MyLicense"
            ]
          },
          "category": {
            "type": "string",
            "description": "License category. Defaults to Uncategorized if not specified.",
            "example": "Permissive"
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