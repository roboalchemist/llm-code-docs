# Source: https://posthog.com/docs/open-api-spec/surveys_responses_unarchive_create.md

# surveys_responses_unarchive_create

## OpenAPI

```json POST /api/projects/{project_id}/surveys/{id}/responses/{response_uuid}/unarchive/
{
  "paths": {
    "/api/projects/{project_id}/surveys/{id}/responses/{response_uuid}/unarchive/": {
      "post": {
        "operationId": "surveys_responses_unarchive_create",
        "description": "Unarchive a single survey response.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this survey.",
            "required": true
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
            "in": "path",
            "name": "response_uuid",
            "schema": {
              "type": "string",
              "pattern": "^[^/]+$"
            },
            "required": true
          }
        ],
        "tags": [
          "surveys",
          "surveys"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SurveySerializerCreateUpdateOnly"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/SurveySerializerCreateUpdateOnly"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/SurveySerializerCreateUpdateOnly"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "survey:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "surveys"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "SurveySerializerCreateUpdateOnly": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "description": {
            "type": "string"
          },
          "type": {
            "$ref": "#/components/schemas/SurveyType"
          },
          "schedule": {
            "type": "string",
            "nullable": true
          },
          "linked_flag": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MinimalFeatureFlag"
              }
            ],
            "readOnly": true
          },
          "linked_flag_id": {
            "type": "integer",
            "writeOnly": true,
            "nullable": true
          },
          "linked_insight_id": {
            "type": "integer",
            "writeOnly": true,
            "nullable": true
          },
          "targeting_flag_id": {
            "type": "integer",
            "writeOnly": true
          },
          "targeting_flag": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MinimalFeatureFlag"
              }
            ],
            "readOnly": true
          },
          "internal_targeting_flag": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MinimalFeatureFlag"
              }
            ],
            "readOnly": true
          },
          "targeting_flag_filters": {
            "writeOnly": true,
            "nullable": true
          },
          "remove_targeting_flag": {
            "type": "boolean",
            "writeOnly": true,
            "nullable": true
          },
          "questions": {
            "nullable": true,
            "description": "\n        The `array` of questions included in the survey. Each question must conform to one of the defined question types: Basic, Link, Rating, or Multiple Choice.\n\n        Basic (open-ended question)\n        - `id`: The question ID\n        - `type`: `open`\n        - `question`: The text of the question.\n        - `description`: Optional description of the question.\n        - `descriptionContentType`: Content type of the description (`html` or `text`).\n        - `optional`: Whether the question is optional (`boolean`).\n        - `buttonText`: Text displayed on the submit button.\n        - `branching`: Branching logic for the question. See branching types below for details.\n\n        Link (a question with a link)\n        - `id`: The question ID\n        - `type`: `link`\n        - `question`: The text of the question.\n        - `description`: Optional description of the question.\n        - `descriptionContentType`: Content type of the description (`html` or `text`).\n        - `optional`: Whether the question is optional (`boolean`).\n        - `buttonText`: Text displayed on the submit button.\n        - `link`: The URL associated with the question.\n        - `branching`: Branching logic for the question. See branching types below for details.\n\n        Rating (a question with a rating scale)\n        - `id`: The question ID\n        - `type`: `rating`\n        - `question`: The text of the question.\n        - `description`: Optional description of the question.\n        - `descriptionContentType`: Content type of the description (`html` or `text`).\n        - `optional`: Whether the question is optional (`boolean`).\n        - `buttonText`: Text displayed on the submit button.\n        - `display`: Display style of the rating (`number` or `emoji`).\n        - `scale`: The scale of the rating (`number`).\n        - `lowerBoundLabel`: Label for the lower bound of the scale.\n        - `upperBoundLabel`: Label for the upper bound of the scale.\n        - `isNpsQuestion`: Whether the question is an NPS rating.\n        - `branching`: Branching logic for the question. See branching types below for details.\n\n        Multiple choice\n        - `id`: The question ID\n        - `type`: `single_choice` or `multiple_choice`\n        - `question`: The text of the question.\n        - `description`: Optional description of the question.\n        - `descriptionContentType`: Content type of the description (`html` or `text`).\n        - `optional`: Whether the question is optional (`boolean`).\n        - `buttonText`: Text displayed on the submit button.\n        - `choices`: An array of choices for the question.\n        - `shuffleOptions`: Whether to shuffle the order of the choices (`boolean`).\n        - `hasOpenChoice`: Whether the question allows an open-ended response (`boolean`).\n        - `branching`: Branching logic for the question. See branching types below for details.\n\n        Branching logic can be one of the following types:\n\n        Next question: Proceeds to the next question\n        ```json\n        {\n            \"type\": \"next_question\"\n        }\n        ```\n\n        End: Ends the survey, optionally displaying a confirmation message.\n        ```json\n        {\n            \"type\": \"end\"\n        }\n        ```\n\n        Response-based: Branches based on the response values. Available for the `rating` and `single_choice` question types.\n        ```json\n        {\n            \"type\": \"response_based\",\n            \"responseValues\": {\n                \"responseKey\": \"value\"\n            }\n        }\n        ```\n\n        Specific question: Proceeds to a specific question by index.\n        ```json\n        {\n            \"type\": \"specific_question\",\n            \"index\": 2\n        }\n        ```\n\n        Translations: Each question can include inline translations.\n        - `translations`: Object mapping language codes to translated fields.\n        - Language codes: Any string - allows customers to use their own language keys (e.g., \"es\", \"es-MX\", \"english\", \"french\")\n        - Translatable fields: `question`, `description`, `buttonText`, `choices`, `lowerBoundLabel`, `upperBoundLabel`, `link`\n\n        Example with translations:\n        ```json\n        {\n            \"id\": \"uuid\",\n            \"type\": \"rating\",\n            \"question\": \"How satisfied are you?\",\n            \"lowerBoundLabel\": \"Not satisfied\",\n            \"upperBoundLabel\": \"Very satisfied\",\n            \"translations\": {\n                \"es\": {\n                    \"question\": \"¿Qué tan satisfecho estás?\",\n                    \"lowerBoundLabel\": \"No satisfecho\",\n                    \"upperBoundLabel\": \"Muy satisfecho\"\n                },\n                \"fr\": {\n                    \"question\": \"Dans quelle mesure êtes-vous satisfait?\"\n                }\n            }\n        }\n        ```\n        "
          },
          "conditions": {
            "nullable": true
          },
          "appearance": {
            "nullable": true
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
          "start_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "end_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "archived": {
            "type": "boolean"
          },
          "responses_limit": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0,
            "nullable": true
          },
          "iteration_count": {
            "type": "integer",
            "maximum": 500,
            "minimum": 0,
            "nullable": true
          },
          "iteration_frequency_days": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0,
            "nullable": true
          },
          "iteration_start_dates": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "date-time",
              "nullable": true
            },
            "nullable": true
          },
          "current_iteration": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0,
            "nullable": true
          },
          "current_iteration_start_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "response_sampling_start_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "response_sampling_interval_type": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/ResponseSamplingIntervalTypeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "response_sampling_interval": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0,
            "nullable": true
          },
          "response_sampling_limit": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0,
            "nullable": true
          },
          "response_sampling_daily_limits": {
            "nullable": true
          },
          "enable_partial_responses": {
            "type": "boolean",
            "nullable": true
          },
          "enable_iframe_embedding": {
            "type": "boolean",
            "nullable": true
          },
          "translations": {
            "nullable": true
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          },
          "form_content": {
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "id",
          "internal_targeting_flag",
          "linked_flag",
          "name",
          "targeting_flag",
          "type"
        ]
      },
      "SurveyType": {
        "enum": [
          "popover",
          "widget",
          "external_survey",
          "api"
        ],
        "type": "string",
        "description": "* `popover` - popover\n* `widget` - widget\n* `external_survey` - external survey\n* `api` - api"
      },
      "MinimalFeatureFlag": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "team_id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string"
          },
          "key": {
            "type": "string",
            "maxLength": 400
          },
          "filters": {
            "type": "object",
            "additionalProperties": {}
          },
          "deleted": {
            "type": "boolean"
          },
          "active": {
            "type": "boolean"
          },
          "ensure_experience_continuity": {
            "type": "boolean",
            "nullable": true
          },
          "has_encrypted_payloads": {
            "type": "boolean",
            "nullable": true
          },
          "version": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "nullable": true
          },
          "evaluation_runtime": {
            "nullable": true,
            "description": "Specifies where this feature flag should be evaluated\n\n* `server` - Server\n* `client` - Client\n* `all` - All",
            "oneOf": [
              {
                "$ref": "#/components/schemas/EvaluationRuntimeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "bucketing_identifier": {
            "nullable": true,
            "description": "Identifier used for bucketing users into rollout and variants\n\n* `distinct_id` - User ID (default)\n* `device_id` - Device ID",
            "oneOf": [
              {
                "$ref": "#/components/schemas/BucketingIdentifierEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "evaluation_tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "evaluation_contexts": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          }
        },
        "required": [
          "evaluation_contexts",
          "evaluation_tags",
          "id",
          "key",
          "team_id"
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
      "ResponseSamplingIntervalTypeEnum": {
        "enum": [
          "day",
          "week",
          "month"
        ],
        "type": "string",
        "description": "* `day` - day\n* `week` - week\n* `month` - month"
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
      },
      "EvaluationRuntimeEnum": {
        "enum": [
          "server",
          "client",
          "all"
        ],
        "type": "string",
        "description": "* `server` - Server\n* `client` - Client\n* `all` - All"
      },
      "BucketingIdentifierEnum": {
        "enum": [
          "distinct_id",
          "device_id"
        ],
        "type": "string",
        "description": "* `distinct_id` - User ID (default)\n* `device_id` - Device ID"
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
      }
    }
  }
}
```
