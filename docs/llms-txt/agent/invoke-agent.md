# Source: https://docs.agent.ai/api-reference/advanced/invoke-agent.md

# Invoke Agent

> Trigger another agent to perform additional processing or data handling within workflows.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/invoke_agent
paths:
  path: /action/invoke_agent
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: >-
                      Enter the ID of the agent you want to invoke, such as
                      'agent_123' or 'data_processor'
                    example: deepseek-r1
              input:
                allOf:
                  - type: string
                    description: Top-level key value pairs for inputs and their values.
                    example: value
            required: true
            requiredProperties:
              - id
              - input
        examples:
          example:
            value:
              id: deepseek-r1
              input: value
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              response: >-
                <think>


                </think>


                AI agents are autonomous entities that use artificial
                intelligence to perceive their environment, make decisions, and
                take actions to achieve specific goals. They operate with
                varying levels of autonomy, ranging from simple rule-based
                systems to complex, adaptive, and learning-based models. AI
                agents can be deployed across diverse applications, including
                software applications, robotics, and IoT devices, to perform
                tasks such as data analysis, decision-making, and interaction
                with humans.
              status: 200
        description: API response
  deprecated: false
  type: path
components:
  schemas: {}

````