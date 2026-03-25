# Source: https://help.cloudsmith.io/reference/orgs_saml-group-sync_create.md

# Create a new SAML Group Sync mapping within an organization.

Create a new SAML Group Sync mapping within an organization.

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
    "/orgs/{org}/saml-group-sync/": {
      "post": {
        "operationId": "orgs_saml-group-sync_create",
        "summary": "Create a new SAML Group Sync mapping within an organization.",
        "description": "Create a new SAML Group Sync mapping within an organization.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrganizationGroupSyncRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "The SAML Group Sync mapping was created.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationGroupSync"
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
          "404": {
            "description": "Org namespace not found.",
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
      "OrganizationGroupSync": {
        "required": [
          "idp_key",
          "idp_value",
          "team"
        ],
        "type": "object",
        "properties": {
          "idp_key": {
            "title": "Idp key",
            "type": "string",
            "maxLength": 100,
            "minLength": 1
          },
          "idp_value": {
            "title": "Idp value",
            "type": "string",
            "maxLength": 100,
            "minLength": 1
          },
          "role": {
            "title": "Role",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ],
            "default": "Member"
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "team": {
            "title": "Team",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$"
          }
        }
      },
      "OrganizationGroupSyncRequest": {
        "required": [
          "idp_key",
          "idp_value",
          "organization",
          "team"
        ],
        "type": "object",
        "properties": {
          "idp_key": {
            "title": "Idp key",
            "type": "string",
            "maxLength": 100,
            "minLength": 1
          },
          "idp_value": {
            "title": "Idp value",
            "type": "string",
            "maxLength": 100,
            "minLength": 1
          },
          "organization": {
            "title": "Organization",
            "type": "string"
          },
          "role": {
            "title": "Role",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ],
            "default": "Member"
          },
          "team": {
            "title": "Team",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$"
          }
        }
      }
    }
  }
}
```