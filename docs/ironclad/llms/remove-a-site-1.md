# Source: https://clickwrap-developer.ironcladapp.com/reference/remove-a-site-1.md

# Remove a Site

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "contact": {
      "email": "support@ironcladapp.com",
      "name": "Ironclad Support"
    },
    "title": "REST API",
    "version": "v1.1"
  },
  "security": [
    {
      "Bearer": []
    }
  ],
  "servers": [
    {
      "description": "Ironclad Clickwrap REST API",
      "url": "https://api.pactsafe.com/v1.1"
    }
  ],
  "components": {
    "securitySchemes": {
      "Bearer": {
        "scheme": "bearer",
        "type": "http"
      }
    }
  },
  "paths": {
    "/sites/{site_id}": {
      "delete": {
        "summary": "Remove a Site",
        "tags": [
          "Sites"
        ],
        "operationId": "remove-a-site",
        "parameters": [
          {
            "name": "site_id",
            "in": "path",
            "description": "The ID of the Ironclad Clickwrap Site.",
            "schema": {
              "type": "integer",
              "format": "integer"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "A site",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "properties": {
                        "acceptance_language": {
                          "type": "string"
                        },
                        "access_id": {
                          "example": "f9a33f92-0c74-4803-abb5-bf7159da7a13",
                          "readOnly": true,
                          "type": "string"
                        },
                        "account": {
                          "example": 1,
                          "readOnly": true,
                          "type": "integer"
                        },
                        "adoption_level": {
                          "readOnly": true,
                          "enum": [
                            "laggard",
                            "majority",
                            "early_adopter",
                            "innovator",
                            "ironclad_clickwrap",
                            "ironclad_clickwrap_v2",
                            "internal_sandbox",
                            "growth",
                            "professional",
                            "enterprise",
                            "legal_centers"
                          ],
                          "title": "Adoption Level",
                          "type": "string"
                        },
                        "approval_order": {
                          "example": false,
                          "type": "boolean"
                        },
                        "base_publish_url": {
                          "readOnly": true,
                          "type": "string"
                        },
                        "company_information": {
                          "properties": {
                            "city": {
                              "example": "Indianapolis",
                              "type": "string"
                            },
                            "country": {
                              "example": "United States",
                              "type": "string"
                            },
                            "name": {
                              "example": "New Website, LLC",
                              "type": "string"
                            },
                            "postal_code": {
                              "example": 46205,
                              "type": "integer"
                            },
                            "state": {
                              "example": "IN",
                              "type": "string"
                            },
                            "street": {
                              "example": "6311 Westfield Blvd.",
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "created_by": {
                          "example": 1,
                          "readOnly": true,
                          "type": "integer"
                        },
                        "created_time": {
                          "description": "ISO 8601 formatted.",
                          "example": "2023-11-02T15:23:51.007+00:00",
                          "readOnly": true,
                          "type": "string"
                        },
                        "deleted": {
                          "example": false,
                          "readOnly": true,
                          "type": "boolean"
                        },
                        "deleted_by": {
                          "example": 1,
                          "readOnly": true,
                          "type": "integer"
                        },
                        "deleted_time": {
                          "description": "ISO 8601 formatted.",
                          "example": "2023-11-02T15:23:51.007+00:00",
                          "readOnly": true,
                          "type": "string"
                        },
                        "disabled": {
                          "example": false,
                          "readOnly": true,
                          "type": "boolean"
                        },
                        "email_allow_override": {
                          "example": false,
                          "type": "boolean"
                        },
                        "email_display_name": {
                          "example": "New Website",
                          "type": "string"
                        },
                        "email_reply_address": {
                          "example": "team@pactsafe.com",
                          "type": "string"
                        },
                        "enable_allowed_domains": {
                          "example": false,
                          "type": "boolean"
                        },
                        "enforce_limits": {
                          "example": true,
                          "readOnly": true,
                          "type": "boolean"
                        },
                        "first_acceptance_time": {
                          "description": "ISO 8601 formatted.",
                          "example": "2023-11-02T15:23:51.007+00:00",
                          "readOnly": true,
                          "type": "string"
                        },
                        "id": {
                          "example": 1,
                          "readOnly": true,
                          "type": "integer"
                        },
                        "key": {
                          "example": "new-website",
                          "type": "string"
                        },
                        "legal_center_url": {
                          "readOnly": true,
                          "type": "string"
                        },
                        "locale": {
                          "example": "en-US",
                          "type": "string"
                        },
                        "mobile_acceptance_language": {
                          "default": "Agree",
                          "example": "Agree",
                          "type": "string"
                        },
                        "mobile_friendly": {
                          "example": true,
                          "type": "boolean"
                        },
                        "name": {
                          "example": "New Website",
                          "type": "string"
                        },
                        "primary": {
                          "example": false,
                          "readOnly": true,
                          "type": "boolean"
                        },
                        "require_signer_verification": {
                          "example": false,
                          "type": "boolean"
                        },
                        "sandbox": {
                          "example": false,
                          "readOnly": true,
                          "type": "boolean"
                        },
                        "time_zone": {
                          "example": "America/New_York",
                          "type": "string"
                        },
                        "updated_by": {
                          "example": 1,
                          "readOnly": true,
                          "type": "integer"
                        },
                        "updated_time": {
                          "description": "ISO 8601 formatted.",
                          "example": "2023-11-02T15:23:51.007+00:00",
                          "readOnly": true,
                          "type": "string"
                        },
                        "url": {
                          "example": "http://wwww.newwebsite.com",
                          "type": "string"
                        },
                        "verified": {
                          "example": true,
                          "readOnly": true,
                          "type": "boolean"
                        },
                        "verified_time": {
                          "description": "ISO 8601 formatted.",
                          "example": "2023-11-02T15:23:51.007+00:00",
                          "readOnly": true,
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad request."
          },
          "404": {
            "description": "Not found."
          }
        },
        "deprecated": false
      }
    }
  }
}
```