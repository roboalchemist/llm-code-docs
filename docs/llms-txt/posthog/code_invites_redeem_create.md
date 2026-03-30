# Source: https://posthog.com/docs/open-api-spec/code_invites_redeem_create.md

# code_invites_redeem_create

## OpenAPI

```json POST /api/code/invites/redeem/
{
  "paths": {
    "/api/code/invites/redeem/": {
      "post": {
        "operationId": "code_invites_redeem_create",
        "description": "Redeem a PostHog Code invite code to enable access.",
        "summary": "Redeem invite code",
        "tags": [
          "code-invites",
          "code"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CodeInviteRedeemRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/CodeInviteRedeemRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/CodeInviteRedeemRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Invite code redeemed successfully"
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            },
            "description": "Invalid or expired invite code"
          }
        },
        "x-explicit-tags": [
          "code-invites",
          "tasks"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "CodeInviteRedeemRequest": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "maxLength": 50
          }
        },
        "required": [
          "code"
        ]
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Error message"
          }
        },
        "required": [
          "error"
        ]
      }
    }
  }
}
```
