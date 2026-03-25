# Source: https://help.cloudsmith.io/reference/orgs_openid-connect_create.md

# Create the OpenID Connect provider settings for the org.

Create the OpenID Connect provider settings for the org.

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
    "/orgs/{org}/openid-connect/": {
      "post": {
        "operationId": "orgs_openid-connect_create",
        "summary": "Create the OpenID Connect provider settings for the org.",
        "description": "Create the OpenID Connect provider settings for the org.",
        "requestBody": {
          "$ref": "#/components/requestBodies/ProviderSettingsWriteRequest"
        },
        "responses": {
          "201": {
            "description": "Created the OpenID Connect provider settings for the org",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProviderSettingsWrite"
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
            "description": "Organization not found",
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
    "requestBodies": {
      "ProviderSettingsWriteRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ProviderSettingsWriteRequest"
            }
          }
        }
      }
    },
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
      },
      "ProviderSettingsWriteRequest": {
        "required": [
          "claims",
          "enabled",
          "name",
          "provider_url"
        ],
        "type": "object",
        "properties": {
          "claims": {
            "title": "Claims",
            "description": "The set of claims that any received tokens from the provider must contain to authenticate as the configured service account.",
            "type": "object"
          },
          "dynamic_mappings": {
            "description": "The dynamic mappings of `mapping_claim` values to service accounts. Cannot be provided if `service_accounts` is also set.\n\nNote: This field and the dynamic mappings feature are still in early access. Breaking changes are possible as we receive feedback on this feature.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DynamicMapping"
            }
          },
          "enabled": {
            "title": "Enabled",
            "description": "Whether the provider settings should be used for incoming OIDC requests.",
            "type": "boolean"
          },
          "mapping_claim": {
            "title": "Mapping claim",
            "description": "The OIDC claim to use for mapping to service accounts in dynamic_mappings. Cannot be provided if `service_accounts` is also set.\n\nNote: This field and the dynamic mappings feature are still in early access. Breaking changes are possible as we receive feedback on this feature.",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "The name of the provider settings are being configured for",
            "type": "string",
            "minLength": 1
          },
          "provider_url": {
            "title": "Provider url",
            "description": "The URL from the provider that serves as the base for the OpenID configuration.\nFor example, if the OpenID configuration is available at https://token.actions.githubusercontent.com/.well-known/openid-configuration, the provider URL would be https://token.actions.githubusercontent.com/",
            "type": "string",
            "format": "uri",
            "minLength": 1
          },
          "service_accounts": {
            "description": "The service accounts associated with these provider settings. Cannot be provided if `mapping_claim` or `dynamic_mappings` are specified.",
            "type": "array",
            "items": {
              "description": "The service accounts associated with these provider settings. Cannot be provided if `mapping_claim` or `dynamic_mappings` are specified.",
              "type": "string"
            },
            "uniqueItems": true
          }
        }
      },
      "ProviderSettingsWrite": {
        "required": [
          "claims",
          "enabled",
          "name",
          "provider_url"
        ],
        "type": "object",
        "properties": {
          "claims": {
            "title": "Claims",
            "description": "The set of claims that any received tokens from the provider must contain to authenticate as the configured service account.",
            "type": "object"
          },
          "dynamic_mappings": {
            "description": "The dynamic mappings of `mapping_claim` values to service accounts. Cannot be provided if `service_accounts` is also set.\n\nNote: This field and the dynamic mappings feature are still in early access. Breaking changes are possible as we receive feedback on this feature.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DynamicMapping"
            }
          },
          "enabled": {
            "title": "Enabled",
            "description": "Whether the provider settings should be used for incoming OIDC requests.",
            "type": "boolean"
          },
          "mapping_claim": {
            "title": "Mapping claim",
            "description": "The OIDC claim to use for mapping to service accounts in dynamic_mappings. Cannot be provided if `service_accounts` is also set.\n\nNote: This field and the dynamic mappings feature are still in early access. Breaking changes are possible as we receive feedback on this feature.",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "The name of the provider settings are being configured for",
            "type": "string",
            "minLength": 1
          },
          "provider_url": {
            "title": "Provider url",
            "description": "The URL from the provider that serves as the base for the OpenID configuration.\nFor example, if the OpenID configuration is available at https://token.actions.githubusercontent.com/.well-known/openid-configuration, the provider URL would be https://token.actions.githubusercontent.com/",
            "type": "string",
            "format": "uri",
            "minLength": 1
          },
          "service_accounts": {
            "description": "The service accounts associated with these provider settings. Cannot be provided if `mapping_claim` or `dynamic_mappings` are specified.",
            "type": "array",
            "items": {
              "description": "The service accounts associated with these provider settings. Cannot be provided if `mapping_claim` or `dynamic_mappings` are specified.",
              "type": "string"
            },
            "uniqueItems": true
          },
          "slug": {
            "title": "Slug",
            "description": "The slug of the provider settings",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "slug_perm": {
            "title": "Slug perm",
            "description": "The unique, immutable identifier of the provider settings.",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          }
        }
      }
    }
  }
}
```