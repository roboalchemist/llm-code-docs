# Source: https://help.cloudsmith.io/reference/orgs_services_partial_update.md

# Update a service within an organization.

Update a service within an organization.

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
    "/orgs/{org}/services/{service}/": {
      "patch": {
        "operationId": "orgs_services_partial_update",
        "summary": "Update a service within an organization.",
        "description": "Update a service within an organization.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ServiceRequestPatch"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Updated the service within the org",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Service"
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
            "description": "Org namespace not found",
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
        },
        {
          "name": "service",
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
      "ServiceTeams": {
        "required": [
          "slug"
        ],
        "type": "object",
        "properties": {
          "role": {
            "title": "Role",
            "description": "The team role associated with the service",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ],
            "default": "Manager"
          },
          "slug": {
            "title": "Slug",
            "description": "The teams associated with the service",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "minLength": 1
          }
        }
      },
      "Service": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "title": "Created by",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "created_by_url": {
            "title": "Created by url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "description": {
            "title": "Description",
            "description": "The description of the service",
            "type": "string",
            "maxLength": 1024,
            "minLength": 1
          },
          "key": {
            "title": "Key",
            "description": "The API key of the service",
            "type": "string",
            "readOnly": true
          },
          "key_expires_at": {
            "title": "Key expires at",
            "description": "The time at which the API key will expire. This will only be populated if the Organization has an active API Key Policy.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "The name of the service",
            "type": "string",
            "maxLength": 120,
            "minLength": 1
          },
          "role": {
            "title": "Role",
            "description": "The role of the service.",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ],
            "default": "Member"
          },
          "slug": {
            "title": "Slug",
            "description": "The slug of the service",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "teams": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ServiceTeams"
            }
          }
        }
      },
      "ServiceRequestPatch": {
        "type": "object",
        "properties": {
          "description": {
            "title": "Description",
            "description": "The description of the service",
            "type": "string",
            "maxLength": 1024,
            "minLength": 1
          },
          "name": {
            "title": "Name",
            "description": "The name of the service",
            "type": "string",
            "maxLength": 120,
            "minLength": 1
          },
          "role": {
            "title": "Role",
            "description": "The role of the service.",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ],
            "default": "Member"
          },
          "teams": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ServiceTeams"
            }
          }
        }
      }
    }
  }
}
```