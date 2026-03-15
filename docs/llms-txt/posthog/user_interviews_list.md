# Source: https://posthog.com/docs/open-api-spec/user_interviews_list.md

# user_interviews_list

## OpenAPI

```json GET /api/environments/{project_id}/user_interviews/
{
  "paths": {
    "/api/environments/{project_id}/user_interviews/": {
      "get": {
        "operationId": "user_interviews_list",
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
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          }
        ],
        "tags": [
          "user_interviews",
          "user_interviews"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "user_interview_DO_NOT_USE:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedUserInterviewList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "user_interviews"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedUserInterviewList": {
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
              "$ref": "#/components/schemas/UserInterview"
            }
          }
        }
      },
      "UserInterview": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
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
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "interviewee_emails": {
            "type": "array",
            "items": {
              "type": "string",
              "maxLength": 254
            }
          },
          "transcript": {
            "type": "string",
            "readOnly": true
          },
          "summary": {
            "type": "string"
          },
          "audio": {
            "type": "string",
            "format": "uri",
            "writeOnly": true
          }
        },
        "required": [
          "audio",
          "created_at",
          "created_by",
          "id",
          "transcript"
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
