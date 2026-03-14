# Source: https://pipedream.com/docs/connect/api-reference/delete-deployed-trigger.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete deployed trigger

> Remove a deployed trigger and stop receiving events

## OpenAPI

````yaml delete /v1/connect/{project_id}/deployed-triggers/{trigger_id}
openapi: 3.0.4
info:
  version: 2.0.0
  title: Pipedream REST API
servers:
  - url: https://api.pipedream.com
security: []
paths:
  /v1/connect/{project_id}/deployed-triggers/{trigger_id}:
    parameters:
      - name: project_id
        in: path
        required: true
        description: The project ID, which starts with `proj_`.
        schema:
          type: string
          pattern: ^proj_[a-zA-Z0-9]+$
        x-fern-sdk-variable: project_id
      - name: trigger_id
        in: path
        required: true
        schema:
          type: string
    delete:
      summary: Delete deployed trigger
      description: Remove a deployed trigger and stop receiving events
      operationId: deleteDeployedTrigger
      parameters:
        - name: x-pd-environment
          in: header
          required: true
          description: The environment in which the server client is running
          schema:
            $ref: '#/components/schemas/ProjectEnvironment'
        - name: external_user_id
          in: query
          required: true
          description: The external user ID who owns the trigger
          schema:
            type: string
        - name: ignore_hook_errors
          in: query
          description: Whether to ignore errors during deactivation hook
          schema:
            type: boolean
      responses:
        '204':
          description: deployed trigger deleted
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
            await client.deployedTriggers.delete("trigger_id", {
              externalUserId: "external_user_id",
              ignoreHookErrors: true
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
            client.deployed_triggers.delete(
              trigger_id="trigger_id",
              external_user_id="external_user_id",
              ignore_hook_errors=True,
            )
        - lang: java
          label: Java SDK
          source: >
            package com.example.usage;


            import com.pipedream.api.BaseClient;

            import
            com.pipedream.api.resources.deployedtriggers.requests.DeployedTriggersDeleteRequest;


            public class Example {
              public static void main(String[] args) {
              BaseClient client = BaseClient
                .builder()
                .clientId("<clientId>")
                .clientSecret("<clientSecret>")
                .build();

              client.deployedTriggers().delete(
                "project_id",
                "trigger_id",
                DeployedTriggersDeleteRequest
                .builder()
                .externalUserId("external_user_id")
                .build()
              );
              }
            }
components:
  schemas:
    ProjectEnvironment:
      type: string
      description: The environment in which the server client is running
      enum:
        - development
        - production
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
