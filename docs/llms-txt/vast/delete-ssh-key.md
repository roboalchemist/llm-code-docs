# Source: https://docs.vast.ai/api-reference/accounts/delete-ssh-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# delete ssh key

> Removes an SSH key from the authenticated user's account

CLI Usage: `vastai delete ssh-key <id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/ssh/{id}/
openapi: 3.1.0
info:
  title: Vast.ai API
  description: >-
    Welcome to Vast.ai 's API documentation. Our API allows you to
    programmatically manage GPU instances, handle machine operations, and
    automate your AI/ML workflow. Whether you're running individual GPU
    instances or managing a fleet of machines, our API provides comprehensive
    control over all Vast.ai  platform features.
  version: 1.0.0
  contact:
    name: Vast.ai Support
    url: https://discord.gg/vast
servers:
  - url: https://console.vast.ai
    description: Production server
security:
  - BearerAuth: []
paths:
  /api/v0/ssh/{id}/:
    delete:
      tags:
        - Accounts
      summary: delete ssh key
      description: |-
        Removes an SSH key from the authenticated user's account

        CLI Usage: `vastai delete ssh-key <id>`
      operationId: deleteSshKey
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the SSH key to delete
          schema:
            type: integer
            format: int64
      responses:
        '200':
          description: SSH key successfully deleted
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                required:
                  - success
              example:
                success: true
        '400':
          description: Invalid request or SSH key not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  error:
                    type: string
                    example: no_ssh_key
                  msg:
                    type: string
                    example: No ssh key provided
                required:
                  - success
                  - error
                  - msg
              examples:
                not_found:
                  value:
                    success: false
                    error: no_ssh_key
                    msg: No ssh key provided
                invalid:
                  value:
                    success: false
                    error: invalid_request
                    msg: Invalid request parameters
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````