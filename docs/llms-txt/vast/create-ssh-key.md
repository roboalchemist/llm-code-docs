# Source: https://docs.vast.ai/api-reference/accounts/create-ssh-key.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# create ssh-key

> Creates a new SSH key and associates it with your account.
The key will be automatically added to all your current instances.

CLI Usage: `vastai create ssh-key <ssh_key>`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/ssh/
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
  /api/v0/ssh/:
    post:
      tags:
        - Accounts
      summary: create ssh-key
      description: |-
        Creates a new SSH key and associates it with your account.
        The key will be automatically added to all your current instances.

        CLI Usage: `vastai create ssh-key <ssh_key>`
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
                  description: The public SSH key to add (from .pub file)
                  example: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...
      responses:
        '200':
          description: SSH key created successfully
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
                    properties:
                      id:
                        type: integer
                        description: The ID of the created SSH key
                        example: 123
                      user_id:
                        type: integer
                        description: The user ID who owns the key
                        example: 456
                      public_key:
                        type: string
                        description: The public SSH key content
                        example: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...
                      created_at:
                        type: string
                        format: date-time
                        example: '2023-01-01T12:00:00Z'
                      deleted_at:
                        type: string
                        format: date-time
                        nullable: true
                        example: null
        '400':
          description: Bad Request
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
                    enum:
                      - no_ssh_key
                  msg:
                    type: string
                    example: No ssh key provided
        '401':
          description: Unauthorized
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