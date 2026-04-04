# Source: https://www.mintlify.com/docs/api/agent/get-agent-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get agent job by ID

> Retrieves the details and status of a specific agent job by its ID.

## Usage

This endpoint retrieves the details and status of a specific agent job by its unique identifier. Use this to check the progress, status, and results of a previously created agent job.

## Job details

The response includes information such as:

* Job execution status and completion state
* Branch information and pull request details
* Session metadata and timestamps


## OpenAPI

````yaml admin-openapi.json get /agent/{projectId}/job/{id}
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
  /agent/{projectId}/job/{id}:
    get:
      summary: Get agent job by ID
      description: Retrieves the details and status of a specific agent job by its ID.
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
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: The unique identifier of the agent job to retrieve.
      responses:
        '200':
          description: Agent job details retrieved successfully
          content:
            application/json:
              schema:
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