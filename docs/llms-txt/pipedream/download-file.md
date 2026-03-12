# Source: https://pipedream.com/docs/connect/api-reference/download-file.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Download file

> Download a file from File Stash

## OpenAPI

````yaml get /v1/connect/{project_id}/file_stash/download
openapi: 3.0.4
info:
  version: 2.0.0
  title: Pipedream REST API
servers:
  - url: https://api.pipedream.com
security: []
paths:
  /v1/connect/{project_id}/file_stash/download:
    parameters:
      - name: project_id
        in: path
        required: true
        description: The project ID, which starts with `proj_`.
        schema:
          type: string
          pattern: ^proj_[a-zA-Z0-9]+$
        x-fern-sdk-variable: project_id
    get:
      summary: Download file
      description: Download a file from File Stash
      operationId: downloadFileStashFile
      parameters:
        - name: s3_key
          in: query
          schema:
            type: string
            pattern: ^1day\/[^\/]+\/[^\/]+\/[^\/]+\/u\/.*$
            description: The S3 key for the file to download
          required: true
      responses:
        '200':
          description: file contents
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '302':
          description: redirected to presigned URL
          headers:
            Location:
              schema:
                type: string
                format: uri
              description: The presigned URL
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
            application/octet-stream:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Throttled
      security:
        - ConnectToken: []
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
            await client.fileStash.downloadFile({
              s3Key: "s3_key"
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
            client.file_stash.download_file(
              s_3_key="s3_key",
            )
components:
  securitySchemes:
    ConnectToken:
      description: >-
        A short-lived Connect token for client-side requests on behalf of an end
        user. Generate one via the Create Connect token endpoint.
      type: http
      scheme: bearer
      bearerFormat: ^ctok_[0-9a-f]{32}$
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
