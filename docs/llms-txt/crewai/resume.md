# Source: https://docs.crewai.com/en/api-reference/resume.md

# POST /resume

> Resume crew execution with human feedback

## OpenAPI

````yaml enterprise-api.en.yaml post /resume
paths:
  path: /resume
  method: post
  servers:
    - url: https://your-actual-crew-name.crewai.com
      description: Replace with your actual deployed crew URL from the CrewAI AMP dashboard
    - url: https://my-travel-crew.crewai.com
      description: Example travel planning crew (replace with your URL)
    - url: https://content-creation-crew.crewai.com
      description: Example content creation crew (replace with your URL)
    - url: https://research-assistant-crew.crewai.com
      description: Example research assistant crew (replace with your URL)
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >
                **📋 Reference Documentation** - *The tokens shown in examples
                are placeholders for reference only.*


                Use your actual Bearer Token or User Bearer Token from the
                CrewAI AMP dashboard for real API calls.


                **Bearer Token**: Organization-level access for full crew
                operations

                **User Bearer Token**: User-scoped access with limited
                permissions
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
              execution_id:
                allOf:
                  - type: string
                    format: uuid
                    description: >-
                      The unique identifier for the crew execution (from
                      kickoff)
                    example: abcd1234-5678-90ef-ghij-klmnopqrstuv
              task_id:
                allOf:
                  - type: string
                    description: The ID of the task that requires human feedback
                    example: research_task
              human_feedback:
                allOf:
                  - type: string
                    description: >-
                      Your feedback on the task output. This will be
                      incorporated as additional context for subsequent task
                      executions.
                    example: >-
                      Great research! Please add more details about recent
                      developments in the field.
              is_approve:
                allOf:
                  - type: boolean
                    description: >-
                      Whether you approve the task output: true = positive
                      feedback (continue), false = negative feedback (retry
                      task)
                    example: true
              taskWebhookUrl:
                allOf:
                  - type: string
                    format: uri
                    description: >-
                      Callback URL executed after each task completion. MUST be
                      provided to continue receiving task notifications.
                    example: https://your-server.com/webhooks/task
              stepWebhookUrl:
                allOf:
                  - type: string
                    format: uri
                    description: >-
                      Callback URL executed after each agent thought/action.
                      MUST be provided to continue receiving step notifications.
                    example: https://your-server.com/webhooks/step
              crewWebhookUrl:
                allOf:
                  - type: string
                    format: uri
                    description: >-
                      Callback URL executed when the crew execution completes.
                      MUST be provided to receive completion notification.
                    example: https://your-server.com/webhooks/crew
            required: true
            requiredProperties:
              - execution_id
              - task_id
              - human_feedback
              - is_approve
        examples:
          approve_and_continue:
            summary: Approve task and continue execution
            value:
              execution_id: abcd1234-5678-90ef-ghij-klmnopqrstuv
              task_id: research_task
              human_feedback: Excellent research! Proceed to the next task.
              is_approve: true
              taskWebhookUrl: https://api.example.com/webhooks/task
              stepWebhookUrl: https://api.example.com/webhooks/step
              crewWebhookUrl: https://api.example.com/webhooks/crew
          request_revision:
            summary: Request task revision with feedback
            value:
              execution_id: abcd1234-5678-90ef-ghij-klmnopqrstuv
              task_id: analysis_task
              human_feedback: Please include more quantitative data and cite your sources.
              is_approve: false
              taskWebhookUrl: https://api.example.com/webhooks/task
              crewWebhookUrl: https://api.example.com/webhooks/crew
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: string
                    enum:
                      - resumed
                      - retrying
                      - completed
                    description: Status of the resumed execution
                    example: resumed
              message:
                allOf:
                  - type: string
                    description: Human-readable message about the resume operation
                    example: Execution resumed successfully
        examples:
          resumed:
            summary: Execution resumed with positive feedback
            value:
              status: resumed
              message: Execution resumed successfully
          retrying:
            summary: Task will be retried with negative feedback
            value:
              status: retrying
              message: Task will be retried with your feedback
        description: Execution resumed successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    description: Error type or title
                    example: Authentication Error
              message:
                allOf:
                  - &ref_1
                    type: string
                    description: Detailed error message
                    example: Invalid bearer token provided
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error: Invalid Request
              message: Execution is not in pending human input state
        description: Invalid request body or execution not in pending state
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error: Unauthorized
              message: Invalid or missing bearer token
        description: Authentication failed - check your bearer token
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error: Not Found
              message: Execution ID not found
        description: Execution ID or Task ID not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              error: Internal Server Error
              message: An unexpected error occurred
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas: {}

````