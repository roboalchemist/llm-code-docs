# Source: https://mintlify.com/docs/api/agent/get-all-jobs.md

# Get all agent jobs

> Retrieves all agent jobs for the specified domain, including their status and details.

## OpenAPI

````yaml GET /agent/{projectId}/jobs
paths:
  path: /agent/{projectId}/jobs
  method: get
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
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              allSessions:
                allOf:
                  - type: array
                    description: Array of all agent sessions for the domain.
                    items:
                      type: object
                      properties:
                        sessionId:
                          type: string
                          description: The subdomain this session belongs to.
                        subdomain:
                          type: string
                          description: The subdomain this session belongs to.
                        branch:
                          type: string
                          description: Git branch name where changes were made.
                          nullable: true
                        haulted:
                          type: boolean
                          description: Whether the session execution was halted.
                        haultReason:
                          type: string
                          enum:
                            - completed
                            - github_missconfigured
                            - error
                          description: Reason for session halt.
                        pullRequestLink:
                          type: string
                          description: Link to the created pull request.
                        messageToUser:
                          type: string
                          description: Message for the user about the session outcome.
                        todos:
                          type: array
                          description: List of todo items from the session.
                          items:
                            type: object
                            properties:
                              content:
                                type: string
                                description: Brief description of the task.
                              status:
                                type: string
                                enum:
                                  - pending
                                  - in_progress
                                  - completed
                                  - cancelled
                                description: Current status of the task.
                              priority:
                                type: string
                                enum:
                                  - high
                                  - medium
                                  - low
                                description: Priority level of the task.
                              id:
                                type: string
                                description: Unique identifier for the todo item.
                        createdAt:
                          type: string
                          format: date-time
                          description: Timestamp when the session was created.
        examples:
          example:
            value:
              allSessions:
                - sessionId: <string>
                  subdomain: <string>
                  branch: <string>
                  haulted: true
                  haultReason: completed
                  pullRequestLink: <string>
                  messageToUser: <string>
                  todos:
                    - content: <string>
                      status: pending
                      priority: high
                      id: <string>
                  createdAt: '2023-11-07T05:31:56Z'
        description: All agent jobs retrieved successfully
  deprecated: false
  type: path
components:
  schemas: {}

````