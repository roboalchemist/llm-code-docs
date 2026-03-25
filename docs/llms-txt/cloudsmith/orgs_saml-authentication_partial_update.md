# Source: https://help.cloudsmith.io/reference/orgs_saml-authentication_partial_update.md

# Update the SAML Authentication settings for this Organization.

Update the SAML Authentication settings for this Organization.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/orgs/{org}/saml-authentication": {
      "patch": {
        "operationId": "orgs_saml-authentication_partial_update",
        "summary": "Update the SAML Authentication settings for this Organization.",
        "description": "Update the SAML Authentication settings for this Organization.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrganizationSAMLAuthRequestPatch"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Updated the SAML Authentication settings.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationSAMLAuth"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "402": {
            "description": "SAML Authentication is not available; please upgrade your account!",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "404": {
            "description": "Organization not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "orgs"
        ]
      },
      "parameters": [
        {
          "name": "org",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "OrganizationSAMLAuth": {
        "required": [
          "saml_auth_enabled",
          "saml_auth_enforced"
        ],
        "type": "object",
        "properties": {
          "saml_auth_enabled": {
            "title": "Saml auth enabled",
            "type": "boolean"
          },
          "saml_auth_enforced": {
            "title": "Saml auth enforced",
            "type": "boolean"
          },
          "saml_metadata_inline": {
            "title": "Inline SAML metadata",
            "description": "If configured, SAML metadata will be used as entered instead of retrieved from a remote URL.",
            "type": "string",
            "maxLength": 32000
          },
          "saml_metadata_url": {
            "title": "Saml metadata url",
            "description": "If configured, SAML metadata be retrieved from a remote URL.",
            "type": "string",
            "format": "uri",
            "maxLength": 254,
            "nullable": true
          }
        }
      },
      "OrganizationSAMLAuthRequestPatch": {
        "type": "object",
        "properties": {
          "saml_auth_enabled": {
            "title": "Saml auth enabled",
            "type": "boolean"
          },
          "saml_auth_enforced": {
            "title": "Saml auth enforced",
            "type": "boolean"
          },
          "saml_metadata_inline": {
            "title": "Inline SAML metadata",
            "description": "If configured, SAML metadata will be used as entered instead of retrieved from a remote URL.",
            "type": "string",
            "maxLength": 32000
          },
          "saml_metadata_url": {
            "title": "Saml metadata url",
            "description": "If configured, SAML metadata be retrieved from a remote URL.",
            "type": "string",
            "format": "uri",
            "maxLength": 254,
            "nullable": true
          }
        }
      }
    }
  }
}
```