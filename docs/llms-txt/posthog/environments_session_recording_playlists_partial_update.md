# Source: https://posthog.com/docs/open-api-spec/environments_session_recording_playlists_partial_update.md

# environments_session_recording_playlists_partial_update

## OpenAPI

```json PATCH /api/environments/{environment_id}/session_recording_playlists/{short_id}/
{
  "paths": {
    "/api/environments/{environment_id}/session_recording_playlists/{short_id}/": {
      "patch": {
        "operationId": "environments_session_recording_playlists_partial_update",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "short_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "replay",
          "session_recording_playlists"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedSessionRecordingPlaylist"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedSessionRecordingPlaylist"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedSessionRecordingPlaylist"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "session_recording_playlist:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SessionRecordingPlaylist"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "replay"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PatchedSessionRecordingPlaylist": {
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
