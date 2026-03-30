# Source: https://posthog.com/docs/open-api-spec/proxy_records_destroy.md

# proxy_records_destroy

## OpenAPI

```json DELETE /api/organizations/{organization_id}/proxy_records/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/proxy_records/{id}/": {
      "delete": {
        "operationId": "proxy_records_destroy",
        "description": "Delete a reverse proxy. For proxies in 'waiting', 'erroring', or 'timed_out' status, the record is deleted immediately. For active proxies, a deletion workflow is started to clean up the provisioned infrastructure.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this proxy record.",
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
          "reverse_proxy",
          "proxy_records"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "reverse_proxy"
        ]
      }
    }
  }
}
```
