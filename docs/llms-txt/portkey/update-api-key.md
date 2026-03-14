# Source: https://docs.portkey.ai/docs/api-reference/admin-api/control-plane/api-keys/update-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.portkey.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update API Key

> Updates an existing API key. The API key type (user vs service) and associated user_id cannot be changed after creation.




## OpenAPI

````yaml put /api-keys/{id}
openapi: 3.0.0
info:
  title: Portkey API
  description: >-
    The Portkey REST API. Please see https://portkey.ai/docs/api-reference for
    more details.
  version: 2.0.0
  termsOfService: https://portkey.ai/terms
  contact:
    name: Portkey Developer Forum
    url: https://portkey.wiki/community
  license:
    name: MIT
    url: https://github.com/Portkey-AI/portkey-openapi/blob/master/LICENSE
servers:
  - url: https://api.portkey.ai/v1
    description: Portkey API Public Endpoint
security:
  - Portkey-Key: []
tags:
  - name: Assistants
    description: Build Assistants that can call models and use tools.
  - name: Audio
    description: Turn audio into text or text into audio.
  - name: Chat
    description: >-
      Given a list of messages comprising a conversation, the model will return
      a response.
  - name: Collections
    description: Create, List, Retrieve, Update, and Delete collections of prompts.
  - name: Labels
    description: Create, List, Retrieve, Update, and Delete labels.
  - name: Prompt Collections
    description: Create, List, Retrieve, Update, and Delete prompt collections.
  - name: PromptPartials
    description: Create, List, Retrieve, Update, and Delete prompt partials.
  - name: Prompts
    description: >-
      Given a prompt template ID and variables, will run the saved prompt
      template and return a response.
  - name: Guardrails
    description: Create, List, Retrieve, Update, and Delete prompt Guardrails.
  - name: Completions
    description: >-
      Given a prompt, the model will return one or more predicted completions,
      and can also return the probabilities of alternative tokens at each
      position.
  - name: Embeddings
    description: >-
      Get a vector representation of a given input that can be easily consumed
      by machine learning models and algorithms.
  - name: Fine-tuning
    description: Manage fine-tuning jobs to tailor a model to your specific training data.
  - name: Batch
    description: Create large batches of API requests to run asynchronously.
  - name: Files
    description: >-
      Files are used to upload documents that can be used with features like
      Assistants and Fine-tuning.
  - name: Images
    description: Given a prompt and/or an input image, the model will generate a new image.
  - name: Models
    description: List and describe the various models available in the API.
  - name: Moderations
    description: >-
      Given a input text, outputs if the model classifies it as potentially
      harmful.
  - name: Configs
    description: Create, List, Retrieve, and Update your Portkey Configs.
  - name: Feedback
    description: Send and Update any feedback.
  - name: Logs
    description: Custom Logger to add external logs to Portkey.
  - name: Integrations
    description: Create, List, Retrieve, Update, and Delete your Portkey Integrations.
  - name: Integrations > Workspaces
    description: Manage workspace access for your Portkey Integrations.
  - name: Integrations > Models
    description: Manage model access for your Portkey Integrations.
  - name: Providers
    description: Create, List, Retrieve, Update, and Delete your Portkey Providers.
  - name: Virtual-keys
    description: Create, List, Retrieve, Update, and Delete your Portkey Virtual keys.
  - name: Users
    description: Create and manage users.
  - name: User-invites
    description: Create and manage user invites.
  - name: Workspaces
    description: Create and manage workspaces.
  - name: Workspaces > Members
    description: Create and manage workspace members.
  - name: MCP Integrations
    description: Create, List, Retrieve, Update, and Delete MCP Integrations.
  - name: MCP Integrations > Workspaces
    description: Manage workspace access for MCP Integrations.
  - name: MCP Integrations > Capabilities
    description: List and manage capabilities for MCP Integrations.
  - name: MCP Integrations > Metadata
    description: Get MCP Integration metadata and sync info.
  - name: MCP Servers
    description: >-
      Create, List, Retrieve, Update, and Delete MCP Servers (workspace
      instances of MCP Integrations).
  - name: MCP Servers > Capabilities
    description: List and manage capabilities for MCP Servers.
  - name: MCP Servers > User Access
    description: List and manage user access for MCP Servers.
  - name: Api-Keys
    description: Create, List, Retrieve, Update, and Delete your Portkey API keys.
  - name: Logs Export
    description: Exports logs service.
  - name: Audit Logs
    description: Get audit logs for your Portkey account.
  - name: Analytics
    description: >-
      Get analytics over different data points like requests, costs, tokens,
      etc.
  - name: Analytics > Graphs
    description: Get data points for graphical representation.
  - name: Analytics > Summary
    description: Get overall summary for the selected time bucket.
  - name: Analytics > Groups
    description: Get grouped metrics for the selected time bucket.
  - name: Usage Limits Policies
    description: Manage usage limits policies to control total usage over time
  - name: Rate Limits Policies
    description: Manage rate limits policies to control request or token rates
  - name: Model Pricing
    description: Model pricing configurations for 2300+ LLMs across 40+ providers
  - name: Secret-References
    description: >-
      Create, List, Retrieve, Update, and Delete secret references to external
      secret managers.
paths:
  /api-keys/{id}:
    servers:
      - url: https://api.portkey.ai/v1
        description: Portkey API Public Endpoint
      - url: SELF_HOSTED_CONTROL_PLANE_URL
        description: Self-Hosted Control Plane URL
    put:
      tags:
        - Api-Keys
      summary: Update API Keys
      description: >
        Updates an existing API key. The API key type (user vs service) and
        associated user_id cannot be changed after creation.
      parameters:
        - name: id
          in: path
          schema:
            type: string
            format: uuid
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateApiKeyObject'
      responses:
        '200':
          description: OK
          headers:
            Content-Type:
              schema:
                type: string
                example: application/json
          content:
            application/json:
              schema:
                type: object
              example: {}
      x-code-samples:
        - lang: python
          label: Default
          source: |
            from portkey_ai import Portkey

            # Initialize the Portkey client
            portkey = Portkey(
                api_key="PORTKEY_API_KEY",
            )

            # Update the API key
            updated_api_key = portkey.api_keys.update(
                id="API_KEY_ID",
                name="API_KEY_NAME_0909",
                rate_limits=[
                    {
                        "type": "requests",
                        "unit": "rpm",
                        "value": 100
                    }
                ],
                scopes=[
                    "organisation_users.create", "organisation_users.read", "organisation_users.update",
                    "organisation_users.delete", "organisation_users.list",
                    "organisation_service_api_keys.create", "organisation_service_api_keys.update",
                    "organisation_service_api_keys.read", "organisation_service_api_keys.delete",
                    "organisation_service_api_keys.list", "workspaces.delete", "workspaces.create",
                    "workspaces.read", "workspaces.update", "workspaces.list", "logs.export",
                    "logs.list", "logs.view", "configs.create", "configs.update", "configs.delete",
                    "configs.read", "configs.list", "virtual_keys.create", "virtual_keys.update",
                    "virtual_keys.delete", "virtual_keys.duplicate", "virtual_keys.read",
                    "virtual_keys.list", "virtual_keys.copy", "workspace_service_api_keys.create",
                    "workspace_service_api_keys.delete", "workspace_service_api_keys.update",
                    "workspace_service_api_keys.read", "workspace_service_api_keys.list",
                    "workspace_user_api_keys.create", "workspace_user_api_keys.delete",
                    "workspace_user_api_keys.update", "workspace_user_api_keys.read",
                    "workspace_user_api_keys.list", "workspace_users.create", "workspace_users.read",
                    "workspace_users.update", "workspace_users.delete", "workspace_users.list",
                    "analytics.view"
                ]
            )

            print(updated_api_key)
        - lang: javascript
          label: Default
          source: |
            import { Portkey } from "portkey-ai";

            const portkey = new Portkey({
                apiKey: "PORTKEY_API_KEY",
            })

            const apiKey=await portkey.apiKeys.update({
                id:"API_KEY_ID",
                name:"API_KEY_NAME_0909",
                rate_limits:[        {
                    "type": "requests",
                    "unit": "rpm",
                    "value": 100
                }],
                "scopes": [
                            "organisation_users.create",
                            "organisation_users.read",
                            "organisation_users.update",
                            "organisation_users.delete",
                            "organisation_users.list",
                            "organisation_service_api_keys.create",
                            "organisation_service_api_keys.update",
                            "organisation_service_api_keys.read",
                            "organisation_service_api_keys.delete",
                            "organisation_service_api_keys.list",
                            "workspaces.delete",
                            "workspaces.create",
                            "workspaces.read",
                            "workspaces.update",
                            "workspaces.list",
                            "logs.export",
                            "logs.list",
                            "logs.view",
                            "configs.create",
                            "configs.update",
                            "configs.delete",
                            "configs.read",
                            "configs.list",
                            "virtual_keys.create",
                            "virtual_keys.update",
                            "virtual_keys.delete",
                            "virtual_keys.duplicate",
                            "virtual_keys.read",
                            "virtual_keys.list",
                            "virtual_keys.copy",
                            "workspace_service_api_keys.create",
                            "workspace_service_api_keys.delete",
                            "workspace_service_api_keys.update",
                            "workspace_service_api_keys.read",
                            "workspace_service_api_keys.list",
                            "workspace_user_api_keys.create",
                            "workspace_user_api_keys.delete",
                            "workspace_user_api_keys.update",
                            "workspace_user_api_keys.read",
                            "workspace_user_api_keys.list",
                            "workspace_users.create",
                            "workspace_users.read",
                            "workspace_users.update",
                            "workspace_users.delete",
                            "workspace_users.list",
                            "analytics.view"
                        ],

            })
            console.log(apiKey);
        - lang: curl
          label: Default
          source: |
            curl -X GET "https://api.portkey.ai/v1/api-keys/{id}"
              -H "x-portkey-api-key: PORTKEY_API_KEY" \
              -H "Content-Type: application/json" \
              -d '{
                "name":"API_KEY_NAME_0909",
                "rate_limits":[
                    {
                        "type": "requests",
                        "unit": "rpm",
                        "value": 100
                    }
                ],
                "scopes": [
                  "organisation_users.create",
                  "organisation_users.read",
                  "organisation_users.update",
                  "organisation_users.delete",
                  "organisation_users.list",
                  "organisation_service_api_keys.create",
                  "organisation_service_api_keys.update",
                  "organisation_service_api_keys.read",
                  "organisation_service_api_keys.delete",
                  "organisation_service_api_keys.list",
                  "workspaces.delete",
                  "workspaces.create",
                  "workspaces.read",
                  "workspaces.update",
                  "workspaces.list",
                  "logs.export",
                  "logs.list",
                  "logs.view",
                  "configs.create",
                  "configs.update",
                  "configs.delete",
                  "configs.read",
                  "configs.list",
                  "virtual_keys.create",
                  "virtual_keys.update",
                  "virtual_keys.delete",
                  "virtual_keys.duplicate",
                  "virtual_keys.read",
                  "virtual_keys.list",
                  "virtual_keys.copy",
                  "workspace_service_api_keys.create",
                  "workspace_service_api_keys.delete",
                  "workspace_service_api_keys.update",
                  "workspace_service_api_keys.read",
                  "workspace_service_api_keys.list",
                  "workspace_user_api_keys.create",
                  "workspace_user_api_keys.delete",
                  "workspace_user_api_keys.update",
                  "workspace_user_api_keys.read",
                  "workspace_user_api_keys.list",
                  "workspace_users.create",
                  "workspace_users.read",
                  "workspace_users.update",
                  "workspace_users.delete",
                  "workspace_users.list",
                  "analytics.view"
                ]
            }'
        - lang: curl
          label: Self-Hosted
          source: |
            curl -X GET "SELF_HOSTED_CONTROL_PLANE_URL/api-keys/{id}" \
            -H "x-portkey-api-key: PORTKEY_API_KEY" \
            -H "Content-Type: application/json" \
            -d '{
                "name":"API_KEY_NAME_0909",
                "rate_limits":[
                    {
                        "type": "requests",
                        "unit": "rpm",
                        "value": 100
                    }
                ],
                "scopes":[
                  "organisation_users.create",
                  "organisation_users.read",
                  "organisation_users.update",
                  "organisation_users.delete",
                  "organisation_users.list",
                  "organisation_service_api_keys.create",
                  "organisation_service_api_keys.update",
                  "organisation_service_api_keys.read",
                  "organisation_service_api_keys.delete",
                  "organisation_service_api_keys.list",
                  "workspaces.delete",
                  "workspaces.create",
                  "workspaces.read",
                  "workspaces.update",
                  "workspaces.list",
                  "logs.export",
                  "logs.list",
                  "logs.view",
                  "configs.create",
                  "configs.update",
                  "configs.delete",
                  "configs.read",
                  "configs.list",
                  "virtual_keys.create",
                  "virtual_keys.update",
                  "virtual_keys.delete",
                  "virtual_keys.duplicate",
                  "virtual_keys.read",
                  "virtual_keys.list",
                  "virtual_keys.copy",
                  "workspace_service_api_keys.create",
                  "workspace_service_api_keys.delete",
                  "workspace_service_api_keys.update",
                  "workspace_service_api_keys.read",
                  "workspace_service_api_keys.list",
                  "workspace_user_api_keys.create",
                  "workspace_user_api_keys.delete",
                  "workspace_user_api_keys.update",
                  "workspace_user_api_keys.read",
                  "workspace_user_api_keys.list",
                  "workspace_users.create",
                  "workspace_users.read",
                  "workspace_users.update",
                  "workspace_users.delete",
                  "workspace_users.list",
                  "analytics.view"
                ]
            }'
        - lang: python
          label: Self-Hosted
          source: |
            from portkey_ai import Portkey

            # Initialize the Portkey client
            portkey = Portkey(
                api_key="PORTKEY_API_KEY",
                base_url="SELF_HOSTED_CONTROL_PLANE_URL"
            )

            # Update the API key
            updated_api_key = portkey.api_keys.update(
                id="API_KEY_ID",
                name="API_KEY_NAME_0909",
                rate_limits=[
                    {
                        "type": "requests",
                        "unit": "rpm",
                        "value": 100
                    }
                ],
                scopes=[
                    "organisation_users.create", "organisation_users.read", "organisation_users.update",
                    "organisation_users.delete", "organisation_users.list",
                    "organisation_service_api_keys.create", "organisation_service_api_keys.update",
                    "organisation_service_api_keys.read", "organisation_service_api_keys.delete",
                    "organisation_service_api_keys.list", "workspaces.delete", "workspaces.create",
                    "workspaces.read", "workspaces.update", "workspaces.list", "logs.export",
                    "logs.list", "logs.view", "configs.create", "configs.update", "configs.delete",
                    "configs.read", "configs.list", "virtual_keys.create", "virtual_keys.update",
                    "virtual_keys.delete", "virtual_keys.duplicate", "virtual_keys.read",
                    "virtual_keys.list", "virtual_keys.copy", "workspace_service_api_keys.create",
                    "workspace_service_api_keys.delete", "workspace_service_api_keys.update",
                    "workspace_service_api_keys.read", "workspace_service_api_keys.list",
                    "workspace_user_api_keys.create", "workspace_user_api_keys.delete",
                    "workspace_user_api_keys.update", "workspace_user_api_keys.read",
                    "workspace_user_api_keys.list", "workspace_users.create", "workspace_users.read",
                    "workspace_users.update", "workspace_users.delete", "workspace_users.list",
                    "analytics.view"
                ]
            )

            print(updated_api_key)
        - lang: javascript
          label: Self-Hosted
          source: |
            import { Portkey } from "portkey-ai";

            const portkey = new Portkey({
                apiKey: "PORTKEY_API_KEY",
                baseUrl: "SELF_HOSTED_CONTROL_PLANE_URL"
            })

            const apiKey=await portkey.apiKeys.update({
                id:"API_KEY_ID",
                name:"API_KEY_NAME_0909",
                rate_limits:[        {
                    "type": "requests",
                    "unit": "rpm",
                    "value": 100
                }],
                "scopes": [
                            "organisation_users.create",
                            "organisation_users.read",
                            "organisation_users.update",
                            "organisation_users.delete",
                            "organisation_users.list",
                            "organisation_service_api_keys.create",
                            "organisation_service_api_keys.update",
                            "organisation_service_api_keys.read",
                            "organisation_service_api_keys.delete",
                            "organisation_service_api_keys.list",
                            "workspaces.delete",
                            "workspaces.create",
                            "workspaces.read",
                            "workspaces.update",
                            "workspaces.list",
                            "logs.export",
                            "logs.list",
                            "logs.view",
                            "configs.create",
                            "configs.update",
                            "configs.delete",
                            "configs.read",
                            "configs.list",
                            "virtual_keys.create",
                            "virtual_keys.update",
                            "virtual_keys.delete",
                            "virtual_keys.duplicate",
                            "virtual_keys.read",
                            "virtual_keys.list",
                            "virtual_keys.copy",
                            "workspace_service_api_keys.create",
                            "workspace_service_api_keys.delete",
                            "workspace_service_api_keys.update",
                            "workspace_service_api_keys.read",
                            "workspace_service_api_keys.list",
                            "workspace_user_api_keys.create",
                            "workspace_user_api_keys.delete",
                            "workspace_user_api_keys.update",
                            "workspace_user_api_keys.read",
                            "workspace_user_api_keys.list",
                            "workspace_users.create",
                            "workspace_users.read",
                            "workspace_users.update",
                            "workspace_users.delete",
                            "workspace_users.list",
                            "analytics.view"
                        ],

            })
            console.log(apiKey);
components:
  schemas:
    UpdateApiKeyObject:
      type: object
      properties:
        name:
          type: string
          example: Development API Key
        description:
          type: string
          example: API key for development environment
        rate_limits:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
                example: requests
              unit:
                type: string
                example: rpm
              value:
                type: integer
                example: 100
        usage_limits:
          $ref: '#/components/schemas/UsageLimits'
        scopes:
          type: array
          items:
            type: string
          example:
            - completions.write
        defaults:
          type: object
          properties:
            metadata:
              type: object
              additionalProperties: true
              example:
                environment: development
                team: backend
            config_id:
              type: string
              example: config-abc
        alert_emails:
          type: array
          items:
            type: string
            format: email
            example: foo@bar.com
    UsageLimits:
      type: object
      properties:
        credit_limit:
          type: integer
          description: Credit Limit. Used for tracking usage
          minimum: 1
          default: null
        type:
          type: string
          description: Type of credit limit
          enum:
            - cost
            - tokens
        alert_threshold:
          type: integer
          description: Alert Threshold. Used for alerting when usage reaches more than this
          minimum: 1
          default: null
        periodic_reset:
          type: string
          description: Reset the usage periodically.
          enum:
            - monthly
            - weekly
      example:
        credit_limit: 10
        periodic_reset: monthly
        alert_threshold: 8
  securitySchemes:
    Portkey-Key:
      type: apiKey
      in: header
      name: x-portkey-api-key

````

Built with [Mintlify](https://mintlify.com).