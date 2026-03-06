# Source: https://docs.vast.ai/api-reference/accounts/update-ssh-key.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# update ssh key

> Updates the specified SSH key with the provided value.

CLI Usage: `vastai update ssh-key <id> <ssh_key>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/ssh/{id}/
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
    put:
      tags:
        - Accounts
      summary: update ssh key
      description: |-
        Updates the specified SSH key with the provided value.

        CLI Usage: `vastai update ssh-key <id> <ssh_key>`
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the SSH key to update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - ssh_key
              properties:
                ssh_key:
                  type: string
                  description: The new value for the SSH key
                  example: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3...
      responses:
        '200':
          description: SSH key updated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  key:
                    type: object
                    description: The updated SSH key data
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=1.0
      security:
        - BearerAuth: []
components:
  schemas:
    Error:
      type: object
      properties:
        success:
          type: boolean
          example: false
        error:
          type: string
        msg:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````