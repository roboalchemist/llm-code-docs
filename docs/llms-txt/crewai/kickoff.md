# Source: https://docs.crewai.com/en/api-reference/kickoff.md

# POST /kickoff

> Start a crew execution

## OpenAPI

````yaml enterprise-api.en.yaml post /kickoff
paths:
  path: /kickoff
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
              inputs:
                allOf:
                  - type: object
                    description: Key-value pairs of all required inputs for your crew
                    additionalProperties:
                      type: string
                    example:
                      budget: 1000 USD
                      interests: games, tech, ai, relaxing hikes, amazing food
                      duration: 7 days
                      age: '35'
              meta:
                allOf:
                  - type: object
                    description: Additional metadata to pass to the crew
                    additionalProperties: true
                    example:
                      requestId: user-request-12345
                      source: mobile-app
              taskWebhookUrl:
                allOf:
                  - type: string
                    format: uri
                    description: Callback URL executed after each task completion
                    example: https://your-server.com/webhooks/task
              stepWebhookUrl:
                allOf:
                  - type: string
                    format: uri
                    description: Callback URL executed after each agent thought/action
                    example: https://your-server.com/webhooks/step
              crewWebhookUrl:
                allOf:
                  - type: string
                    format: uri
                    description: Callback URL executed when the crew execution completes
                    example: https://your-server.com/webhooks/crew
            required: true
            requiredProperties:
              - inputs
        examples:
          travel_planning:
            summary: Travel planning crew
            value:
              inputs:
                budget: 1000 USD
                interests: games, tech, ai, relaxing hikes, amazing food
                duration: 7 days
                age: '35'
              meta:
                requestId: travel-req-123
                source: web-app
          outreach_campaign:
            summary: Outreach crew with webhooks
            value:
              inputs:
                name: John Smith
                title: CTO
                company: TechCorp
                industry: Software
                our_product: AI Development Platform
                linkedin_url: https://linkedin.com/in/johnsmith
              taskWebhookUrl: https://api.example.com/webhooks/task
              crewWebhookUrl: https://api.example.com/webhooks/crew
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              kickoff_id:
                allOf:
                  - type: string
                    format: uuid
                    description: Unique identifier for tracking this execution
                    example: abcd1234-5678-90ef-ghij-klmnopqrstuv
        examples:
          example:
            value:
              kickoff_id: abcd1234-5678-90ef-ghij-klmnopqrstuv
        description: Crew execution started successfully
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
              error: Authentication Error
              message: Invalid bearer token provided
        description: Invalid request body or missing required inputs
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
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: Validation Error
              message:
                allOf:
                  - type: string
                    example: Missing required inputs
              details:
                allOf:
                  - type: object
                    properties:
                      missing_inputs:
                        type: array
                        items:
                          type: string
                        example:
                          - budget
                          - interests
            refIdentifier: '#/components/schemas/ValidationError'
        examples:
          example:
            value:
              error: Validation Error
              message: Missing required inputs
              details:
                missing_inputs:
                  - budget
                  - interests
        description: Validation error - ensure all required inputs are provided
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