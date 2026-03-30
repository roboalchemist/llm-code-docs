# Source: https://posthog.com/docs/open-api-spec/oauth_applications_list.md

# oauth_applications_list

## OpenAPI

```json GET /api/organizations/{organization_id}/oauth_applications/
{
  "paths": {
    "/api/organizations/{organization_id}/oauth_applications/": {
      "get": {
        "operationId": "oauth_applications_list",
        "description": "ViewSet for listing OAuth applications at the organization level (read-only).",
        "parameters": [
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
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
          "oauth_applications"
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
                  "$ref": "#/components/schemas/PaginatedOrganizationOAuthApplicationList"
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
      "PaginatedOrganizationOAuthApplicationList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OrganizationOAuthApplication"
            }
          }
        }
      },
      "OrganizationOAuthApplication": {
        "type": "object",
        "description": "Serializer for organization-scoped OAuth applications (read-only).",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 255
          },
          "client_id": {
            "type": "string",
            "maxLength": 100
          },
          "redirect_uris_list": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "is_verified": {
            "type": "boolean",
            "description": "True if this application has been verified by PostHog"
          },
          "created": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "created",
          "id",
          "redirect_uris_list",
          "updated"
        ]
      }
    }
  }
}
```
