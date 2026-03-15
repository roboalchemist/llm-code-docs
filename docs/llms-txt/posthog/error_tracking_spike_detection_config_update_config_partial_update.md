# Source: https://posthog.com/docs/open-api-spec/error_tracking_spike_detection_config_update_config_partial_update.md

# error_tracking_spike_detection_config_update_config_partial_update

## OpenAPI

```json PATCH /api/environments/{project_id}/error_tracking/spike_detection_config/update_config/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/spike_detection_config/update_config/": {
      "patch": {
        "operationId": "error_tracking_spike_detection_config_update_config_partial_update",
        "parameters": [
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
          "error_tracking",
          "error_tracking"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "error_tracking"
        ]
      }
    }
  }
}
```
