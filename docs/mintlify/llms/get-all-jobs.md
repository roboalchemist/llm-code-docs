# Source: https://www.mintlify.com/docs/api/agent/get-all-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all agent jobs

> Retrieves all agent jobs for the specified domain, including their status and details.

## Usage

This endpoint retrieves all agent jobs for the specified domain, providing an overview of all agent activities and their current status. This is useful for monitoring and managing multiple concurrent or historical agent jobs.

## Response

Use this endpoint to get a comprehensive view of all previous agent sessions.


## OpenAPI

````yaml admin-openapi.json get /agent/{projectId}/jobs
openapi: 3.0.1
info:
  title: Mintlify Admin API
  description: >-
    An API for administrative operations including documentation updates and
    agent management.
  version: 1.0.0
servers:
  - url: https://api.mintlify.com/v1
security:
  - bearerAuth: []
paths:
  /agent/{projectId}/jobs:
    get:
      summary: Get all agent jobs
      description: >-
        Retrieves all agent jobs for the specified domain, including their
        status and details.
      parameters:
        - name: projectId
          in: path
          required: true
          schema:
            type: string
          description: >-
            Your project ID. Can be copied from the [API
            keys](https://dashboard.mintlify.com/settings/organization/api-keys)
            page in your dashboard.
      responses:
        '200':
          description: All agent jobs retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  allSessions:
                    type: array
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
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        The Authorization header expects a Bearer token. Use an admin API key
        (prefixed with `mint_`). This is a server-side secret key. Generate one
        on the [API keys
        page](https://dashboard.mintlify.com/settings/organization/api-keys) in
        your dashboard.

````