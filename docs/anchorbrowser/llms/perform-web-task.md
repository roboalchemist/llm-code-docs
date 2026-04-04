# Source: https://docs.anchorbrowser.io/api-reference/ai-tools/perform-web-task.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Perform Web Task

> Start from a URL and perform the given task.



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/tools/perform-web-task
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/tools/perform-web-task:
    post:
      tags:
        - AI Tools
      summary: Perform Web Task
      description: Start from a URL and perform the given task.
      parameters:
        - in: query
          name: sessionId
          schema:
            type: string
            title: Browser Session
          description: >-
            An optional browser session identifier to reference an existing
            running browser sessions. When passed, the tool will be executed on
            the provided browser session.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PerformWebTaskRequestSchema'
      responses:
        '200':
          description: The result of the autonomous task.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PerformWebTaskResponseSchema'
              examples:
                sync:
                  summary: Synchronous response
                  value:
                    data:
                      result:
                        result:
                          nodes_cpu_usage:
                            - node: pool-e1ro5g0nq-559g5
                              cluster: do-nyc1-demo-infra
                              cpu_avg_percentage: 8.29
                            - node: pool-e1ro5g0nq-559gk
                              cluster: do-nyc1-demo-infra
                              cpu_avg_percentage: 24.8
                async:
                  summary: Asynchronous response
                  value:
                    data:
                      status: running
                      workflow_id: >-
                        perform-web-task-execution-123e4567-e89b-12d3-a456-426614174000-550e8400-e29b-41d4-a716-446655440000
        '400':
          description: Invalid request.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    PerformWebTaskRequestSchema:
      type: object
      required:
        - prompt
      properties:
        url:
          type: string
          description: >-
            The URL of the webpage. If not provided, the tool will use the
            current page in the session.
        prompt:
          type: string
          description: The task to be autonomously completed.
        agent:
          type: string
          description: The AI agent to use for task completion. Defaults to browser-use.
          enum:
            - browser-use
            - openai-cua
            - gemini-computer-use
            - anthropic-cua
        provider:
          type: string
          description: The AI provider to use for task completion.
          enum:
            - openai
            - gemini
            - groq
            - azure
            - xai
        model:
          type: string
          description: >-
            The specific model to use for task completion. see our
            [models](/agentic-browser-control/ai-task-completion#available-models)
            page for more information.
        detect_elements:
          type: boolean
          description: >-
            Enable element detection for better interaction accuracy. Improves
            the agent's ability to identify and interact with UI elements.
        human_intervention:
          type: boolean
          description: >-
            Allow human intervention during task execution. When enabled, the
            agent can request human input for ambiguous situations.
        max_steps:
          type: integer
          description: >-
            Maximum number of steps the agent can take to complete the task.
            Defaults to 200.
        secret_values:
          type: object
          additionalProperties:
            type: string
          description: >-
            Secret values to pass to the agent for secure credential handling.
            Keys and values are passed as environment variables to the agent.
        highlight_elements:
          type: boolean
          description: >-
            Whether to highlight elements during task execution for better
            visibility.
        output_schema:
          type: object
          description: JSON Schema defining the expected structure of the output data.
        async:
          type: boolean
          description: >-
            Whether to run the task asynchronously. If true, the task will be
            run asynchronously and the response will include a workflow ID.
          default: false
    PerformWebTaskResponseSchema:
      type: object
      properties:
        data:
          oneOf:
            - $ref: '#/components/schemas/PerformWebTaskSyncResponseData'
            - $ref: '#/components/schemas/PerformWebTaskAsyncResponseData'
          x-oneOf-labels:
            - sync
            - async
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
    PerformWebTaskSyncResponseData:
      type: object
      title: sync
      properties:
        result:
          type: object
          description: The outcome or answer produced by the autonomous task.
      required:
        - result
    PerformWebTaskAsyncResponseData:
      type: object
      title: async
      properties:
        status:
          type: string
          enum:
            - running
          description: The status of the asynchronous task execution.
        workflow_id:
          type: string
          description: The workflow ID for tracking the asynchronous task execution.
      required:
        - status
        - workflow_id
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````