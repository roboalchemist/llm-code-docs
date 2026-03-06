# Source: https://docs.vast.ai/api-reference/instances/execute.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# execute

> Executes a constrained remote command on a specified instance.
The command output can be retrieved from the returned result URL.

CLI Usage: `vastai execute <instance_id> <command>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/instances/command/{id}/
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
  /api/v0/instances/command/{id}/:
    put:
      tags:
        - Instances
      summary: execute
      description: |-
        Executes a constrained remote command on a specified instance.
        The command output can be retrieved from the returned result URL.

        CLI Usage: `vastai execute <instance_id> <command>`
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the instance to execute command on
          schema:
            type: integer
            example: 12345
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - command
              properties:
                command:
                  type: string
                  description: Command to execute on the instance
                  example: ls -l
                  maxLength: 512
      responses:
        '200':
          description: Command queued successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  writeable_path:
                    type: string
                    description: Container writeable path
                    example: /workspace
                  result_url:
                    type: string
                    description: URL to fetch command execution results
                    example: https://s3.amazonaws.com/vast.ai/instance_logs/abc123.log
                  msg:
                    type: string
                    example: >-
                      Command is executing, wait a few seconds and then view the
                      result_url
        '400':
          description: Invalid request parameters
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
                      - invalid_args
                      - invalid_container_id
                      - invalid_container
                  msg:
                    type: string
                    example: Invalid command given.
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Forbidden - User is blacklisted
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
                    example: API requests too frequent endpoint threshold=1.5
        '483':
          description: Invalid JSON body
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
                    example: invalid_args
                  msg:
                    type: string
                    example: Invalid json_body
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