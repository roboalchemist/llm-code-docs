# Source: https://mintlify.com/docs/api/agent/create-agent-job.md

# Create agent job

> Creates a new agent job that can generate and edit documentation based on provided messages and branch information.

## OpenAPI

````yaml POST /agent/{projectId}/job
paths:
  path: /agent/{projectId}/job
  method: post
  servers:
    - url: https://api.mintlify.com/v1
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
                The Authorization header expects a Bearer token. Create an
                [Admin API
                Key](https://dashboard.mintlify.com/settings/organization/api-keys)
                here.
          cookie: {}
    parameters:
      path:
        projectId:
          schema:
            - type: string
              required: true
              description: >-
                Your project ID. Can be copied from the [API
                keys](https://dashboard.mintlify.com/settings/organization/api-keys)
                page in your dashboard.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              branch:
                allOf:
                  - type: string
                    description: >-
                      The name of the Git branch that the agent should work on,
                      will be automatically created if it doesn't exist
              messages:
                allOf:
                  - type: array
                    description: A list of previous messages to provide to the agent.
                    items:
                      type: object
                      required:
                        - role
                        - content
                      properties:
                        role:
                          type: string
                          enum:
                            - system
                            - user
                          description: The role of the message sender.
                        content:
                          type: string
                          description: The content of the message.
            required: true
            requiredProperties:
              - branch
              - messages
        examples:
          example:
            value:
              branch: <string>
              messages:
                - role: system
                  content: <string>
  response:
    '200':
      text/plain:
        schemaArray:
          - type: string
            description: >-
              Streaming response containing the agent job execution details and
              results.
        examples:
          example:
            value: <string>
        description: >-
          Agent job created successfully (streaming response). X-Session-Id
          Header is sent back in the response
  deprecated: false
  type: path
components:
  schemas: {}

````