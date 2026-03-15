# Source: https://posthog.com/docs/open-api-spec/notebooks_list.md

# notebooks_list

## OpenAPI

```json GET /api/projects/{project_id}/notebooks/
{
  "paths": {
    "/api/projects/{project_id}/notebooks/": {
      "get": {
        "operationId": "notebooks_list",
        "description": "The API for interacting with Notebooks. This feature is in early access and the API can have breaking changes without announcement.",
        "parameters": [
          {
            "in": "query",
            "name": "contains",
            "schema": {
              "type": "string"
            },
            "description": "Filter for notebooks that match a provided filter.\n                Each match pair is separated by a colon,\n                multiple match pairs can be sent separated by a space or a comma",
            "examples": {
              "FilterForNotebooksThatHaveAnyRecording": {
                "value": "recording:true",
                "summary": "Filter for notebooks that have any recording"
              },
              "FilterForNotebooksThatDoNotHaveAnyRecording": {
                "value": "recording:false",
                "summary": "Filter for notebooks that do not have any recording"
              },
              "FilterForNotebooksThatHaveASpecificRecording": {
                "value": "recording:the-session-recording-id",
                "summary": "Filter for notebooks that have a specific recording"
              }
            }
          },
          {
            "in": "query",
            "name": "created_by",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "The UUID of the Notebook's creator"
          },
          {
            "in": "query",
            "name": "date_from",
            "schema": {
              "type": "string",
              "format": "date-time"
            },
            "description": "Filter for notebooks created after this date & time"
          },
          {
            "in": "query",
            "name": "date_to",
            "schema": {
              "type": "string",
              "format": "date-time"
            },
            "description": "Filter for notebooks created before this date & time"
          },
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
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          },
          {
            "in": "query",
            "name": "user",
            "schema": {
              "type": "string"
            },
            "description": "If any value is provided for this parameter, return notebooks created by the logged in user."
          }
        ],
        "tags": [
          "notebooks"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "notebook:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedNotebookMinimalList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "notebooks"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedNotebookMinimalList": {
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
              "$ref": "#/components/schemas/NotebookMinimal"
            }
          }
        }
      },
      "NotebookMinimal": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "short_id": {
            "type": "string",
            "readOnly": true
          },
          "title": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "deleted": {
            "type": "boolean",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "last_modified_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "last_modified_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "user_access_level": {
            "type": "string",
            "nullable": true,
            "readOnly": true,
            "description": "The effective access level the user has for this object"
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          }
        },
        "required": [
          "created_at",
          "created_by",
          "deleted",
          "id",
          "last_modified_at",
          "last_modified_by",
          "short_id",
          "title",
          "user_access_level"
        ]
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      }
    }
  }
}
```
