# Source: https://posthog.com/docs/open-api-spec/domains_retrieve.md

# domains_retrieve

## OpenAPI

```json GET /api/organizations/{organization_id}/domains/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/domains/{id}/": {
      "get": {
        "operationId": "domains_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this domain.",
            "required": true
          },
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "domains"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationDomain"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "OrganizationDomain": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "domain": {
            "type": "string",
            "maxLength": 128
          },
          "is_verified": {
            "type": "boolean",
            "description": "Determines whether a domain is verified or not.",
            "readOnly": true
          },
          "verified_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "verification_challenge": {
            "type": "string",
            "readOnly": true
          },
          "jit_provisioning_enabled": {
            "type": "boolean"
          },
          "sso_enforcement": {
            "type": "string",
            "maxLength": 28
          },
          "has_saml": {
            "type": "boolean",
            "description": "Returns whether SAML is configured for the instance. Does not validate the user has the required license (that check is performed in other places).",
            "readOnly": true
          },
          "saml_entity_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 512
          },
          "saml_acs_url": {
            "type": "string",
            "nullable": true,
            "maxLength": 512
          },
          "saml_x509_cert": {
            "type": "string",
            "nullable": true
          },
          "has_scim": {
            "type": "boolean",
            "description": "Returns whether SCIM is configured and enabled for this domain.",
            "readOnly": true
          },
          "scim_enabled": {
            "type": "boolean"
          },
          "scim_base_url": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "scim_bearer_token": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "required": [
          "domain",
          "has_saml",
          "has_scim",
          "id",
          "is_verified",
          "scim_base_url",
          "scim_bearer_token",
          "verification_challenge",
          "verified_at"
        ]
      }
    }
  }
}
```
