# Source: https://pipedream.com/docs/connect/api-reference/create-project.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create project

> Create a new project for the authenticated workspace

## OpenAPI

````yaml post /v1/connect/projects
openapi: 3.0.4
info:
  version: 2.0.0
  title: Pipedream REST API
servers:
  - url: https://api.pipedream.com
security: []
paths:
  /v1/connect/projects:
    post:
      summary: Create project
      description: Create a new project for the authenticated workspace
      operationId: createProject
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateProjectOpts'
      responses:
        '201':
          description: project created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Project'
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
            await client.projects.create({
              name: "name"
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
            client.projects.create(
              name="name",
            )
components:
  schemas:
    CreateProjectOpts:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: Name of the project
        app_name:
          type: string
          description: Display name for the Connect application
        support_email:
          type: string
          format: email
          description: Support email displayed to end users
        connect_require_key_auth_test:
          type: boolean
          description: >-
            Send a test request to the upstream API when adding Connect accounts
            for key-based apps
    Project:
      type: object
      description: Project that can be accessed via the Connect API
      required:
        - id
        - name
      properties:
        id:
          type: string
          pattern: ^proj_[0-9A-Za-z]+$
          description: Hash ID for the project
        name:
          type: string
          description: Display name of the project
        app_name:
          type: string
          nullable: true
          description: App name shown to Connect users
        support_email:
          type: string
          format: email
          nullable: true
          description: Support email configured for the project
        connect_require_key_auth_test:
          type: boolean
          description: >-
            Send a test request to the upstream API when adding Connect accounts
            for key-based apps
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
