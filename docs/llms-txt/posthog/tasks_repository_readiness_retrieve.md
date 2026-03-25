# Source: https://posthog.com/docs/open-api-spec/tasks_repository_readiness_retrieve.md

# tasks_repository_readiness_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/tasks/repository_readiness/
{
  "paths": {
    "/api/projects/{project_id}/tasks/repository_readiness/": {
      "get": {
        "operationId": "tasks_repository_readiness_retrieve",
        "description": "Get autonomy readiness details for a specific repository in the current project.",
        "summary": "Get repository readiness",
        "parameters": [
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
            "name": "refresh",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "in": "query",
            "name": "repository",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Repository in org/repo format",
            "required": true
          },
          {
            "in": "query",
            "name": "window_days",
            "schema": {
              "type": "integer",
              "maximum": 30,
              "minimum": 1,
              "default": 7
            }
          }
        ],
        "tags": [
          "tasks",
          "tasks"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "task:read"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "task:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryReadinessResponse"
                }
              }
            },
            "description": "Repository readiness status"
          }
        },
        "x-explicit-tags": [
          "tasks"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "RepositoryReadinessResponse": {
        "type": "object",
        "properties": {
          "repository": {
            "type": "string",
            "description": "Normalized repository identifier"
          },
          "classification": {
            "type": "string",
            "description": "Repository classification"
          },
          "excluded": {
            "type": "boolean",
            "description": "Whether the repository is excluded from readiness checks"
          },
          "coreSuggestions": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CapabilityState"
              }
            ],
            "description": "Tracking capability state"
          },
          "replayInsights": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CapabilityState"
              }
            ],
            "description": "Computer vision capability state"
          },
          "errorInsights": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CapabilityState"
              }
            ],
            "description": "Error tracking capability state"
          },
          "overall": {
            "type": "string",
            "description": "Overall readiness state"
          },
          "evidenceTaskCount": {
            "type": "integer",
            "description": "Count of replay-derived evidence tasks"
          },
          "windowDays": {
            "type": "integer",
            "description": "Lookback window in days"
          },
          "generatedAt": {
            "type": "string",
            "description": "ISO timestamp when the response was generated"
          },
          "cacheAgeSeconds": {
            "type": "integer",
            "description": "Age of cached response in seconds"
          },
          "scan": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ScanEvidence"
              }
            ],
            "description": "Scan evidence details"
          }
        },
        "required": [
          "cacheAgeSeconds",
          "classification",
          "coreSuggestions",
          "errorInsights",
          "evidenceTaskCount",
          "excluded",
          "generatedAt",
          "overall",
          "replayInsights",
          "repository",
          "windowDays"
        ]
      },
      "CapabilityState": {
        "type": "object",
        "properties": {
          "state": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CapabilityStateStateEnum"
              }
            ],
            "description": "Current state of the capability\n\n* `needs_setup` - needs_setup\n* `detected` - detected\n* `waiting_for_data` - waiting_for_data\n* `ready` - ready\n* `not_applicable` - not_applicable\n* `unknown` - unknown"
          },
          "estimated": {
            "type": "boolean",
            "description": "Whether the state is estimated from static analysis"
          },
          "reason": {
            "type": "string",
            "description": "Human-readable explanation"
          },
          "evidence": {
            "type": "object",
            "additionalProperties": {},
            "description": "Supporting evidence"
          }
        },
        "required": [
          "estimated",
          "reason",
          "state"
        ]
      },
      "ScanEvidence": {
        "type": "object",
        "properties": {
          "filesScanned": {
            "type": "integer",
            "description": "Number of files scanned"
          },
          "detectedFilesCount": {
            "type": "integer",
            "description": "Total candidate files detected"
          },
          "eventNameCount": {
            "type": "integer",
            "description": "Number of distinct event names found"
          },
          "foundPosthogInit": {
            "type": "boolean",
            "description": "Whether posthog.init() was found in scanned files"
          },
          "foundPosthogCapture": {
            "type": "boolean",
            "description": "Whether posthog.capture() was found in scanned files"
          },
          "foundErrorSignal": {
            "type": "boolean",
            "description": "Whether error tracking signals were found in scanned files"
          }
        },
        "required": [
          "detectedFilesCount",
          "eventNameCount",
          "filesScanned",
          "foundErrorSignal",
          "foundPosthogCapture",
          "foundPosthogInit"
        ]
      },
      "CapabilityStateStateEnum": {
        "enum": [
          "needs_setup",
          "detected",
          "waiting_for_data",
          "ready",
          "not_applicable",
          "unknown"
        ],
        "type": "string",
        "description": "* `needs_setup` - needs_setup\n* `detected` - detected\n* `waiting_for_data` - waiting_for_data\n* `ready` - ready\n* `not_applicable` - not_applicable\n* `unknown` - unknown"
      }
    }
  }
}
```
