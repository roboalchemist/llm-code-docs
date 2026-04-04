# Source: https://posthog.com/docs/open-api-spec/session_recording_playlists_list.md

# session_recording_playlists_list

## OpenAPI

```json GET /api/projects/{project_id}/session_recording_playlists/
{
  "paths": {
    "/api/projects/{project_id}/session_recording_playlists/": {
      "get": {
        "operationId": "session_recording_playlists_list",
        "description": "Override list to include synthetic playlists",
        "parameters": [
          {
            "in": "query",
            "name": "created_by",
            "schema": {
              "type": "integer"
            }
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
            "name": "short_id",
            "schema": {
              "type": "string"
            }
          }
        ],
        "tags": [
          "replay",
          "session_recording_playlists"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "session_recording_playlist:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedSessionRecordingPlaylistList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "replay"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedSessionRecordingPlaylistList": {
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
              "$ref": "#/components/schemas/SessionRecordingPlaylist"
            }
          }
        }
      },
      "SessionRecordingPlaylist": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "short_id": {
            "type": "string",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "derived_name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "description": {
            "type": "string"
          },
          "pinned": {
            "type": "boolean"
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
          "deleted": {
            "type": "boolean"
          },
          "filters": {},
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
          "recordings_counts": {
            "type": "object",
            "additionalProperties": {
              "type": "object",
              "additionalProperties": {
                "oneOf": [
                  {
                    "type": "integer"
                  },
                  {
                    "type": "boolean"
                  }
                ],
                "nullable": true
              }
            },
            "readOnly": true
          },
          "type": {
            "readOnly": true,
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/SessionRecordingPlaylistTypeEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "is_synthetic": {
            "type": "boolean",
            "description": "Return whether this is a synthetic playlist",
            "readOnly": true
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
          "id",
          "is_synthetic",
          "last_modified_at",
          "last_modified_by",
          "recordings_counts",
          "short_id",
          "type"
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
      "SessionRecordingPlaylistTypeEnum": {
        "enum": [
          "collection",
          "filters"
        ],
        "type": "string",
        "description": "* `collection` - Collection\n* `filters` - Filters"
      },
      "NullEnum": {
        "enum": [
          null
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
      }
    }
  }
}
```
