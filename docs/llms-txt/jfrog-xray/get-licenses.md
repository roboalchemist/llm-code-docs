# Source: https://docs.jfrog.com/security/reference/get-licenses.md

# Get Licenses

Get Licenses.

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
    "/api/v1/licensesNames": {
      "get": {
        "operationId": "get-licenses",
        "summary": "Get Licenses",
        "description": "Get Licenses.",
        "tags": [
          "Legal V1"
        ],
        "responses": {
          "200": {
            "description": "Success - Licenses Data Returned",
            "content": {
              "application/json": {
                "schema": {
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
                      "references": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "category": {
                        "type": "string"
                      },
                      "priority": {
                        "type": "integer"
                      },
                      "default_priority": {
                        "type": "integer"
                      },
                      "isCustom": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "name",
                      "full_name",
                      "references",
                      "category",
                      "priority",
                      "default_priority",
                      "isCustom"
                    ]
                  }
                },
                "example": [
                  {
                    "name": "Afmparse",
                    "full_name": "Afmparse License",
                    "references": [
                      "https://fedoraproject.org/wiki/Licensing/Afmparse",
                      "https://spdx.org/licenses/Afmparse"
                    ],
                    "category": "Permissive",
                    "priority": -1,
                    "default_priority": 200,
                    "isCustom": false
                  },
                  {
                    "name": "AGPL-1.0",
                    "full_name": "Affero General Public License v1.0",
                    "references": [
                      "https://spdx.org/licenses/AGPL-1.0"
                    ],
                    "category": "Copyleft",
                    "priority": -1,
                    "default_priority": 500,
                    "isCustom": false
                  }
                ]
              }
            }
          },
          "400": {
            "description": "Failed to retrieve Licenses",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "403": {
            "description": "Permission denied",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
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
      "name": "Legal V1",
      "description": "APIs from Legal V1"
    }
  ]
}
```