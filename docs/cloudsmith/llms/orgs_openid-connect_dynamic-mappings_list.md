# Source: https://help.cloudsmith.io/reference/orgs_openid-connect_dynamic-mappings_list.md

# Retrieve the list of OpenID Connect dynamic mappings for the provider setting.

Retrieve the list of OpenID Connect dynamic mappings for the provider setting.

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
    "/orgs/{org}/openid-connect/{provider_setting}/dynamic-mappings/": {
      "get": {
        "operationId": "orgs_openid-connect_dynamic-mappings_list",
        "summary": "Retrieve the list of OpenID Connect dynamic mappings for the provider setting.",
        "description": "Retrieve the list of OpenID Connect dynamic mappings for the provider setting.",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "A page number within the paginated result set.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "description": "Number of results to return per page.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved the list of OpenID Connect dynamic mappings for the selected provider setting",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/DynamicMapping"
                  }
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
            "description": "Organization or Provider Setting not found (see detail)",
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
          "name": "provider_setting",
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
      "DynamicMapping": {
        "description": "The dynamic mappings of `mapping_claim` values to service accounts. Cannot be provided if `service_accounts` is also set.\n\nNote: This field and the dynamic mappings feature are still in early access. Breaking changes are possible as we receive feedback on this feature.",
        "required": [
          "claim_value",
          "service_account"
        ],
        "type": "object",
        "properties": {
          "claim_value": {
            "title": "Claim value",
            "description": "The OIDC token claim value that must be present in the token for it to successfully authenticate as the mapped `service_account`.\n\nNote: This field and the dynamic mappings feature are still in early access. Breaking changes are possible as we receive feedback on this feature.",
            "type": "string",
            "minLength": 1
          },
          "service_account": {
            "title": "Service account",
            "description": "The service account associated with the provider setting and `claim_value`\n\nNote: This field and the dynamic mappings feature are still in early access. Breaking changes are possible as we receive feedback on this feature.",
            "type": "string",
            "minLength": 1
          }
        }
      }
    }
  }
}
```