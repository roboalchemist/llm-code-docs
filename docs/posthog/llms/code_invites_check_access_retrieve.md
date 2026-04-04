# Source: https://posthog.com/docs/open-api-spec/code_invites_check_access_retrieve.md

# code_invites_check_access_retrieve

## OpenAPI

```json GET /api/code/invites/check-access/
{
  "paths": {
    "/api/code/invites/check-access/": {
      "get": {
        "operationId": "code_invites_check_access_retrieve",
        "description": "Check whether the authenticated user has access to PostHog Code.",
        "summary": "Check access",
        "tags": [
          "code-invites",
          "code"
        ],
        "responses": {
          "200": {
            "description": "Access check result"
          }
        },
        "x-explicit-tags": [
          "code-invites",
          "tasks"
        ]
      }
    }
  }
}
```
