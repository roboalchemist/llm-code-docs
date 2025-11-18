# Source: https://docs.crewai.com/en/api-reference/status.md

# GET /status/{kickoff_id}

> Get execution status

## OpenAPI

````yaml enterprise-api.en.yaml get /status/{kickoff_id}
paths:
  path: /status/{kickoff_id}
  method: get
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
      path:
        kickoff_id:
          schema:
            - type: string
              required: true
              description: The kickoff ID returned from the /kickoff endpoint
              format: uuid
              example: abcd1234-5678-90ef-ghij-klmnopqrstuv
      query: {}
      header: {}
      cookie: {}
    body: {}
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
                      - running
                    example: running
              current_task:
                allOf:
                  - type: string
                    description: Name of the currently executing task
                    example: research_task
              progress:
                allOf:
                  - type: object
                    properties:
                      completed_tasks:
                        type: integer
                        description: Number of completed tasks
                        example: 1
                      total_tasks:
                        type: integer
                        description: Total number of tasks in the crew
                        example: 3
            refIdentifier: '#/components/schemas/ExecutionRunning'
          - type: object
            properties:
              status:
                allOf:
                  - type: string
                    enum:
                      - completed
                    example: completed
              result:
                allOf:
                  - type: object
                    properties:
                      output:
                        type: string
                        description: Final output from the crew execution
                        example: Comprehensive travel itinerary...
                      tasks:
                        type: array
                        items:
                          $ref: '#/components/schemas/TaskResult'
              execution_time:
                allOf:
                  - type: number
                    description: Total execution time in seconds
                    example: 108.5
            refIdentifier: '#/components/schemas/ExecutionCompleted'
          - type: object
            properties:
              status:
                allOf:
                  - type: string
                    enum:
                      - error
                    example: error
              error:
                allOf:
                  - type: string
                    description: Error message describing what went wrong
                    example: 'Task execution failed: Invalid API key'
              execution_time:
                allOf:
                  - type: number
                    description: Time until error occurred in seconds
                    example: 23.1
            refIdentifier: '#/components/schemas/ExecutionError'
        examples:
          running:
            summary: Execution in progress
            value:
              status: running
              current_task: research_task
              progress:
                completed_tasks: 1
                total_tasks: 3
          completed:
            summary: Execution completed successfully
            value:
              status: completed
              result:
                output: >-
                  Comprehensive travel itinerary for 7 days in Japan focusing on
                  tech culture...
                tasks:
                  - task_id: research_task
                    output: Research findings on tech destinations in Japan...
                    agent: Travel Researcher
                    execution_time: 45.2
                  - task_id: planning_task
                    output: >-
                      7-day detailed itinerary with activities and
                      recommendations...
                    agent: Trip Planner
                    execution_time: 62.8
              execution_time: 108.5
          error:
            summary: Execution failed
            value:
              status: error
              error: 'Task execution failed: Invalid API key for external service'
              execution_time: 23.1
        description: Successfully retrieved execution status
    '401':
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
              error: Execution not found
              message: 'No execution found with ID: abcd1234-5678-90ef-ghij-klmnopqrstuv'
        description: Kickoff ID not found
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
  schemas:
    TaskResult:
      type: object
      properties:
        task_id:
          type: string
          description: Unique identifier for the task
          example: research_task
        output:
          type: string
          description: Output generated by this task
          example: Research findings...
        agent:
          type: string
          description: Name of the agent that executed this task
          example: Travel Researcher
        execution_time:
          type: number
          description: Time taken to execute this task in seconds
          example: 45.2

````