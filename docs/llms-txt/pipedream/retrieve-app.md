# Source: https://pipedream.com/docs/connect/api-reference/retrieve-app.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve app

> Get detailed information about a specific app by ID or name slug

## OpenAPI

````yaml get /v1/connect/apps/{app_id}
openapi: 3.0.4
info:
  version: 2.0.0
  title: Pipedream REST API
servers:
  - url: https://api.pipedream.com
security: []
paths:
  /v1/connect/apps/{app_id}:
    get:
      summary: Retrieve app
      description: Get detailed information about a specific app by ID or name slug
      operationId: retrieveApp
      parameters:
        - name: app_id
          in: path
          required: true
          description: The name slug or ID of the app (e.g., 'slack', 'github')
          schema:
            type: string
      responses:
        '200':
          description: app retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAppResponse'
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
            await client.apps.retrieve("app_id");
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
            client.apps.retrieve(
              app_id="app_id",
            )
        - lang: java
          label: Java SDK
          source: |
            package com.example.usage;

            import com.pipedream.api.BaseClient;

            public class Example {
              public static void main(String[] args) {
              BaseClient client = BaseClient
                .builder()
                .clientId("<clientId>")
                .clientSecret("<clientSecret>")
                .build();

              client.apps().retrieve("app_id");
              }
            }
components:
  schemas:
    GetAppResponse:
      type: object
      description: Response received when retrieving a single app
      required:
        - data
      properties:
        data:
          $ref: '#/components/schemas/App'
    App:
      type: object
      description: Response object for a Pipedream app's metadata
      required:
        - name_slug
        - name
        - img_src
        - custom_fields_json
        - categories
        - featured_weight
      properties:
        id:
          type: string
          description: ID of the app. Only applies for OAuth apps.
          nullable: true
        name_slug:
          type: string
          description: >-
            The name slug of the target app (see
            https://pipedream.com/docs/connect/quickstart#find-your-apps-name-slug)
        name:
          type: string
          description: The human-readable name of the app
        auth_type:
          $ref: '#/components/schemas/AppAuthType'
        description:
          type: string
          description: A short description of the app
          nullable: true
        img_src:
          type: string
          description: The URL to the app's logo
        custom_fields_json:
          type: string
          description: A JSON string representing the custom fields for the app
          nullable: true
        categories:
          type: array
          items:
            type: string
          description: Categories associated with the app
        featured_weight:
          type: number
          description: >-
            A rough directional ordering of app popularity, subject to changes
            by Pipedream
    AppAuthType:
      type: string
      enum:
        - keys
        - oauth
        - none
      description: The authentication type used by the app
      nullable: true
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
