# Source: https://docs.agent.ai/api-reference/advanced/invoke-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Invoke Agent

> Trigger another agent to perform additional processing or data handling within workflows.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/invoke_agent
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/invoke_agent:
    post:
      tags:
        - Advanced
      summary: Invoke Agent
      description: >-
        Trigger another agent to perform additional processing or data handling
        within workflows.
      operationId: invokeAgent
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: >-
                    Enter the ID of the agent you want to invoke, such as
                    'agent_123' or 'data_processor'
                  example: deepseek-r1
                input:
                  type: string
                  description: Top-level key value pairs for inputs and their values.
                  example: value
              required:
                - id
                - input
      responses:
        '200':
          description: API response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                response: >-
                  <think>


                  </think>


                  AI agents are autonomous entities that use artificial
                  intelligence to perceive their environment, make decisions,
                  and take actions to achieve specific goals. They operate with
                  varying levels of autonomy, ranging from simple rule-based
                  systems to complex, adaptive, and learning-based models. AI
                  agents can be deployed across diverse applications, including
                  software applications, robotics, and IoT devices, to perform
                  tasks such as data analysis, decision-making, and interaction
                  with humans.
                status: 200
components:
  schemas:
    ActionResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        response:
          type: object
          description: Response data from the action
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````