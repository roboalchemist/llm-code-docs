# Source: https://posthog.com/docs/open-api-spec/surveys_partial_update.md

# surveys_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/surveys/{id}/
{
  "paths": {
    "/api/projects/{project_id}/surveys/{id}/": {
      "patch": {
        "operationId": "surveys_partial_update",
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
                "$ref": "#/components/schemas/PatchedSurveySerializerCreateUpdateOnlySchema"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedSurveySerializerCreateUpdateOnlySchema"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedSurveySerializerCreateUpdateOnlySchema"
              }
            }
          }
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
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SurveySerializerCreateUpdateOnly"
                }
              }
            },
            "description": ""
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
      "PatchedSurveySerializerCreateUpdateOnlySchema": {
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
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFiltersSchema"
              }
            ],
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
        }
      },
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
      "FeatureFlagFiltersSchema": {
        "type": "object",
        "properties": {
          "groups": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FeatureFlagConditionGroupSchema"
            },
            "description": "Release condition groups for the feature flag."
          },
          "multivariate": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagMultivariateSchema"
              }
            ],
            "nullable": true,
            "description": "Multivariate configuration for variant-based rollouts."
          },
          "aggregation_group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index for group-based feature flags."
          },
          "payloads": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "description": "Optional payload values keyed by variant key."
          },
          "super_groups": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "description": "Additional super condition groups used by experiments."
          }
        }
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
      "FeatureFlagConditionGroupSchema": {
        "type": "object",
        "properties": {
          "properties": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FeatureFlagFilterPropertySchema"
            },
            "description": "Property conditions for this release condition group."
          },
          "rollout_percentage": {
            "type": "number",
            "format": "double",
            "description": "Rollout percentage for this release condition group."
          },
          "variant": {
            "type": "string",
            "nullable": true,
            "description": "Variant key override for multivariate flags."
          }
        }
      },
      "FeatureFlagMultivariateSchema": {
        "type": "object",
        "properties": {
          "variants": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FeatureFlagMultivariateVariantSchema"
            },
            "description": "Variant definitions for multivariate feature flags."
          }
        },
        "required": [
          "variants"
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
      "FeatureFlagFilterPropertySchema": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyGenericSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyExistsSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyDateSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertySemverSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyMultiContainsSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyCohortInSchema"
          },
          {
            "$ref": "#/components/schemas/FeatureFlagFilterPropertyFlagEvaluatesSchema"
          }
        ]
      },
      "FeatureFlagMultivariateVariantSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Unique key for this variant."
          },
          "name": {
            "type": "string",
            "description": "Human-readable name for this variant."
          },
          "rollout_percentage": {
            "type": "number",
            "format": "double",
            "description": "Variant rollout percentage."
          }
        },
        "required": [
          "key",
          "rollout_percentage"
        ]
      },
      "FeatureFlagFilterPropertyGenericSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "value": {
            "description": "Comparison value for the property filter. Supports strings, numbers, booleans, and arrays."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyGenericSchemaOperatorEnum"
              }
            ],
            "description": "Operator used to compare the property value.\n\n* `exact` - exact\n* `is_not` - is_not\n* `icontains` - icontains\n* `not_icontains` - not_icontains\n* `regex` - regex\n* `not_regex` - not_regex\n* `gt` - gt\n* `gte` - gte\n* `lt` - lt\n* `lte` - lte"
          }
        },
        "required": [
          "key",
          "operator",
          "value"
        ]
      },
      "FeatureFlagFilterPropertyExistsSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Operator3e6Enum"
              }
            ],
            "description": "Existence operator.\n\n* `is_set` - is_set\n* `is_not_set` - is_not_set"
          },
          "value": {
            "description": "Optional value. Runtime behavior determines whether this is ignored."
          }
        },
        "required": [
          "key",
          "operator"
        ]
      },
      "FeatureFlagFilterPropertyDateSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyDateSchemaOperatorEnum"
              }
            ],
            "description": "Date comparison operator.\n\n* `is_date_exact` - is_date_exact\n* `is_date_after` - is_date_after\n* `is_date_before` - is_date_before"
          },
          "value": {
            "type": "string",
            "description": "Date value in ISO format or relative date expression."
          }
        },
        "required": [
          "key",
          "operator",
          "value"
        ]
      },
      "FeatureFlagFilterPropertySemverSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertySemverSchemaOperatorEnum"
              }
            ],
            "description": "Semantic version comparison operator.\n\n* `semver_gt` - semver_gt\n* `semver_gte` - semver_gte\n* `semver_lt` - semver_lt\n* `semver_lte` - semver_lte\n* `semver_eq` - semver_eq\n* `semver_neq` - semver_neq\n* `semver_tilde` - semver_tilde\n* `semver_caret` - semver_caret\n* `semver_wildcard` - semver_wildcard"
          },
          "value": {
            "type": "string",
            "description": "Semantic version string."
          }
        },
        "required": [
          "key",
          "operator",
          "value"
        ]
      },
      "FeatureFlagFilterPropertyMultiContainsSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Type380Enum"
              }
            ],
            "description": "Property filter type. Common values are 'person' and 'cohort'.\n\n* `cohort` - cohort\n* `person` - person\n* `group` - group"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyMultiContainsSchemaOperatorEnum"
              }
            ],
            "description": "Multi-contains operator.\n\n* `icontains_multi` - icontains_multi\n* `not_icontains_multi` - not_icontains_multi"
          },
          "value": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of strings to evaluate against."
          }
        },
        "required": [
          "key",
          "operator",
          "value"
        ]
      },
      "FeatureFlagFilterPropertyCohortInSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyCohortInSchemaTypeEnum"
              }
            ],
            "description": "Cohort property type required for in/not_in operators.\n\n* `cohort` - cohort"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyCohortInSchemaOperatorEnum"
              }
            ],
            "description": "Membership operator for cohort properties.\n\n* `in` - in\n* `not_in` - not_in"
          },
          "value": {
            "description": "Cohort comparison value (single or list, depending on usage)."
          }
        },
        "required": [
          "key",
          "operator",
          "type",
          "value"
        ]
      },
      "FeatureFlagFilterPropertyFlagEvaluatesSchema": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Property key used in this feature flag condition."
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyFlagEvaluatesSchemaTypeEnum"
              }
            ],
            "description": "Flag property type required for flag dependency checks.\n\n* `flag` - flag"
          },
          "cohort_name": {
            "type": "string",
            "nullable": true,
            "description": "Resolved cohort name for cohort-type filters."
          },
          "group_type_index": {
            "type": "integer",
            "nullable": true,
            "description": "Group type index when using group-based filters."
          },
          "operator": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FeatureFlagFilterPropertyFlagEvaluatesSchemaOperatorEnum"
              }
            ],
            "description": "Operator for feature flag dependency evaluation.\n\n* `flag_evaluates_to` - flag_evaluates_to"
          },
          "value": {
            "description": "Value to compare flag evaluation against."
          }
        },
        "required": [
          "key",
          "operator",
          "type",
          "value"
        ]
      },
      "Type380Enum": {
        "enum": [
          "cohort",
          "person",
          "group"
        ],
        "type": "string",
        "description": "* `cohort` - cohort\n* `person` - person\n* `group` - group"
      },
      "FeatureFlagFilterPropertyGenericSchemaOperatorEnum": {
        "enum": [
          "exact",
          "is_not",
          "icontains",
          "not_icontains",
          "regex",
          "not_regex",
          "gt",
          "gte",
          "lt",
          "lte"
        ],
        "type": "string",
        "description": "* `exact` - exact\n* `is_not` - is_not\n* `icontains` - icontains\n* `not_icontains` - not_icontains\n* `regex` - regex\n* `not_regex` - not_regex\n* `gt` - gt\n* `gte` - gte\n* `lt` - lt\n* `lte` - lte"
      },
      "Operator3e6Enum": {
        "enum": [
          "is_set",
          "is_not_set"
        ],
        "type": "string",
        "description": "* `is_set` - is_set\n* `is_not_set` - is_not_set"
      },
      "FeatureFlagFilterPropertyDateSchemaOperatorEnum": {
        "enum": [
          "is_date_exact",
          "is_date_after",
          "is_date_before"
        ],
        "type": "string",
        "description": "* `is_date_exact` - is_date_exact\n* `is_date_after` - is_date_after\n* `is_date_before` - is_date_before"
      },
      "FeatureFlagFilterPropertySemverSchemaOperatorEnum": {
        "enum": [
          "semver_gt",
          "semver_gte",
          "semver_lt",
          "semver_lte",
          "semver_eq",
          "semver_neq",
          "semver_tilde",
          "semver_caret",
          "semver_wildcard"
        ],
        "type": "string",
        "description": "* `semver_gt` - semver_gt\n* `semver_gte` - semver_gte\n* `semver_lt` - semver_lt\n* `semver_lte` - semver_lte\n* `semver_eq` - semver_eq\n* `semver_neq` - semver_neq\n* `semver_tilde` - semver_tilde\n* `semver_caret` - semver_caret\n* `semver_wildcard` - semver_wildcard"
      },
      "FeatureFlagFilterPropertyMultiContainsSchemaOperatorEnum": {
        "enum": [
          "icontains_multi",
          "not_icontains_multi"
        ],
        "type": "string",
        "description": "* `icontains_multi` - icontains_multi\n* `not_icontains_multi` - not_icontains_multi"
      },
      "FeatureFlagFilterPropertyCohortInSchemaTypeEnum": {
        "enum": [
          "cohort"
        ],
        "type": "string",
        "description": "* `cohort` - cohort"
      },
      "FeatureFlagFilterPropertyCohortInSchemaOperatorEnum": {
        "enum": [
          "in",
          "not_in"
        ],
        "type": "string",
        "description": "* `in` - in\n* `not_in` - not_in"
      },
      "FeatureFlagFilterPropertyFlagEvaluatesSchemaTypeEnum": {
        "enum": [
          "flag"
        ],
        "type": "string",
        "description": "* `flag` - flag"
      },
      "FeatureFlagFilterPropertyFlagEvaluatesSchemaOperatorEnum": {
        "enum": [
          "flag_evaluates_to"
        ],
        "type": "string",
        "description": "* `flag_evaluates_to` - flag_evaluates_to"
      }
    }
  }
}
```
