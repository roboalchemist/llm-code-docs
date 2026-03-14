# Source: https://pipedream.com/docs/connect/api-reference/list-usage-records.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List usage records

> Retrieve Connect usage records for a time window

## OpenAPI

````yaml get /v1/connect/usage
openapi: 3.0.4
info:
  version: 2.0.0
  title: Pipedream REST API
servers:
  - url: https://api.pipedream.com
security: []
paths:
  /v1/connect/usage:
    get:
      summary: List usage records
      description: Retrieve Connect usage records for a time window
      operationId: listUsages
      parameters:
        - name: start_ts
          in: query
          required: true
          description: Usage window start timestamp (seconds)
          schema:
            type: integer
        - name: end_ts
          in: query
          required: true
          description: Usage window end timestamp (seconds)
          schema:
            type: integer
      responses:
        '200':
          description: usage records listed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConnectUsageResponse'
        '400':
          description: invalid timestamps
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '429':
          description: too many requests
          headers:
            Retry-After:
              description: Number of seconds until the rate limit resets
              schema:
                type: integer
            X-RateLimit-Limit:
              schema:
                type: integer
              description: The rate limit threshold
            X-RateLimit-Remaining:
              schema:
                type: integer
              description: Number of requests remaining (always 0 when throttled)
            X-RateLimit-Reset:
              schema:
                type: integer
              description: Unix timestamp when the rate limit resets
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Throttled
      security:
        - OAuth2: []
      x-codeSamples:
        - lang: typescript
          label: TypeScript SDK
          source: |
            import { PipedreamClient } from "@pipedream/sdk";

            const client = new PipedreamClient({
              clientId: "YOUR_CLIENT_ID",
              clientSecret: "YOUR_CLIENT_SECRET",
              projectEnvironment: "YOUR_PROJECT_ENVIRONMENT",
              projectId: "YOUR_PROJECT_ID"
            });
            await client.usage.list({
              startTs: 1,
              endTs: 1
            });
        - lang: python
          label: Python SDK
          source: |
            from pipedream import Pipedream

            client = Pipedream(
              project_id="YOUR_PROJECT_ID",
              project_environment="YOUR_PROJECT_ENVIRONMENT",
              client_id="YOUR_CLIENT_ID",
              client_secret="YOUR_CLIENT_SECRET",
            )
            client.usage.list(
              start_ts=1,
              end_ts=1,
            )
components:
  schemas:
    ConnectUsageResponse:
      type: object
      description: Connect usage records for a time window
      required:
        - data
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/ConnectUsage'
    ErrorResponse:
      type: object
      description: Error response returned by the API in case of an error
      required:
        - error
      properties:
        error:
          type: string
          description: The error message
        code:
          type: string
          description: The error code
        details:
          type: object
          description: Additional error details
    ConnectUsage:
      type: object
      description: Connect usage record
      required:
        - credits_used
        - usage_start_ts
        - usage_end_ts
      properties:
        credits_used:
          type: integer
          description: Total Connect credits used
        action_run_credits_used:
          type: integer
          description: Credits used when running Connect actions
          nullable: true
        proxy_credits_used:
          type: integer
          description: Credits used by Connect proxy requests
          nullable: true
        source_emit_credits_used:
          type: integer
          description: Credits used by Connect source event emissions
          nullable: true
        usage_start_ts:
          type: integer
          description: Usage window start timestamp (seconds)
        usage_end_ts:
          type: integer
          description: Usage window end timestamp (seconds)
  securitySchemes:
    OAuth2:
      description: >-
        A short-lived OAuth access token for server-side requests. Generate one
        via the Generate OAuth Token flow or automatically when initializing the
        SDK client.
      type: oauth2
      flows:
        clientCredentials:
          tokenUrl: https://api.pipedream.com/v1/oauth/token
          scopes:
            '*': Full access to every OAuth-protected endpoint.
            connect:*: >-
              Full access to all Connect API endpoints (components, projects,
              triggers, accounts, etc.).
            connect:actions:*: Full access to Connect actions.
            connect:triggers:*: Full access to Connect triggers.
            connect:accounts:read: List and fetch Connect accounts for an external user.
            connect:accounts:write: Create or remove Connect accounts.
            connect:deployed_triggers:read: >-
              Read deployed triggers and related data like events, pipelines and
              webhooks.
            connect:deployed_triggers:write: Modify or delete deployed triggers.
            connect:users:read: List and fetch external users
            connect:users:write: Delete external users.
            connect:projects:read: List and fetch projects owned by the workspace.
            connect:projects:write: Create, update, or delete projects owned by the workspace.
            connect:usage:read: List Connect usage records for a time window.
            connect:tokens:create: Create Connect session tokens.
            connect:proxy: Invoke the Connect proxy.
            connect:workflow:invoke: Invoke Connect workflows on behalf of a user.

````

Built with [Mintlify](https://mintlify.com).
