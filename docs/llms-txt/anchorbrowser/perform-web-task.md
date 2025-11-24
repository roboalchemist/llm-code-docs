# Source: https://docs.anchorbrowser.io/api-reference/ai-tools/perform-web-task.md

# Perform Web Task

> Start from a URL and perform the given task.

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/tools/perform-web-task
paths:
  path: /v1/tools/perform-web-task
  method: post
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
          cookie: {}
    parameters:
      path: {}
      query:
        sessionId:
          schema:
            - type: string
              title: Browser Session
              description: >-
                An optional browser session identifier to reference an existing
                running browser sessions. When passed, the tool will be executed
                on the provided browser session.
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              url:
                allOf:
                  - type: string
                    description: >-
                      The URL of the webpage. If not provided, the tool will use
                      the current page in the session.
              prompt:
                allOf:
                  - type: string
                    description: The task to be autonomously completed.
              agent:
                allOf:
                  - type: string
                    description: >-
                      The AI agent to use for task completion. Defaults to
                      browser-use.
                    enum:
                      - browser-use
                      - openai-cua
              provider:
                allOf:
                  - type: string
                    description: The AI provider to use for task completion.
                    enum:
                      - openai
                      - gemini
                      - groq
                      - azure
                      - xai
              model:
                allOf:
                  - type: string
                    description: >-
                      The specific model to use for task completion. see our
                      [models](/agentic-browser-control/ai-task-completion#available-models)
                      page for more information.
              detect_elements:
                allOf:
                  - type: boolean
                    description: >-
                      Enable element detection for better interaction accuracy.
                      Improves the agent's ability to identify and interact with
                      UI elements.
              human_intervention:
                allOf:
                  - type: boolean
                    description: >-
                      Allow human intervention during task execution. When
                      enabled, the agent can request human input for ambiguous
                      situations.
              max_steps:
                allOf:
                  - type: integer
                    description: >-
                      Maximum number of steps the agent can take to complete the
                      task. Defaults to 200.
              secret_values:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                    description: >-
                      Secret values to pass to the agent for secure credential
                      handling. Keys and values are passed as environment
                      variables to the agent.
              highlight_elements:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to highlight elements during task execution for
                      better visibility.
              output_schema:
                allOf:
                  - type: object
                    description: >-
                      JSON Schema defining the expected structure of the output
                      data.
            required: true
            refIdentifier: '#/components/schemas/PerformWebTaskRequestSchema'
            requiredProperties:
              - prompt
        examples:
          example:
            value:
              url: <string>
              prompt: <string>
              agent: browser-use
              provider: openai
              model: <string>
              detect_elements: true
              human_intervention: true
              max_steps: 123
              secret_values: {}
              highlight_elements: true
              output_schema: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      result:
                        type: string
                        description: The outcome or answer produced by the autonomous task.
            refIdentifier: '#/components/schemas/PerformWebTaskResponseSchema'
        examples:
          example:
            value:
              data:
                result: <string>
        description: The result of the autonomous task.
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Invalid request.
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Internal server error.
  deprecated: false
  type: path
components:
  schemas: {}

````