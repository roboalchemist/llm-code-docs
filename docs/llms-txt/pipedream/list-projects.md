# Source: https://pipedream.com/docs/connect/api-reference/list-projects.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List projects

> List the projects that are available to the authenticated Connect client

## OpenAPI

````yaml get /v1/connect/projects
openapi: 3.0.4
info:
  version: 2.0.0
  title: Pipedream REST API
servers:
  - url: https://api.pipedream.com
security: []
paths:
  /v1/connect/projects:
    get:
      summary: List projects
      description: List the projects that are available to the authenticated Connect client
      operationId: listProjects
      parameters:
        - name: after
          in: query
          required: false
          description: The cursor to start from for pagination
          schema:
            type: string
        - name: before
          in: query
          required: false
          description: The cursor to end before for pagination
          schema:
            type: string
        - name: limit
          in: query
          required: false
          description: The maximum number of results to return
          schema:
            type: integer
        - name: q
          in: query
          required: false
          description: A search query to filter the projects
          schema:
            type: string
      responses:
        '200':
          description: projects listed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListProjectsResponse'
        '404':
          description: missing OAuth token
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
            const response = await client.projects.list({
              after: "after",
              before: "before",
              limit: 1,
              q: "q"
            });
            for await (const item of response) {
              console.log(item);
            }

            // Or you can manually iterate page-by-page
            let page = await client.projects.list({
              after: "after",
              before: "before",
              limit: 1,
              q: "q"
            });
            while (page.hasNextPage()) {
              page = page.getNextPage();
            }
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
            response = client.projects.list(
              after="after",
              before="before",
              limit=1,
              q="q",
            )
            for item in response:
              yield item
            # alternatively, you can paginate page-by-page
            for page in response.iter_pages():
              yield page
components:
  schemas:
    ListProjectsResponse:
      type: object
      description: Response received when listing Connect projects
      required:
        - data
        - page_info
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/Project'
        page_info:
          $ref: '#/components/schemas/PageInfo'
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
    PageInfo:
      type: object
      properties:
        count:
          type: integer
          description: Number of items returned
          example: 10
        total_count:
          type: integer
          description: Total number of items
          example: 120
        start_cursor:
          type: string
          description: Used to fetch the previous page of items
          nullable: true
        end_cursor:
          type: string
          description: Used to fetch the next page of items
          nullable: true
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
