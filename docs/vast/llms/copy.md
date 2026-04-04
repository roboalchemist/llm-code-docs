# Source: https://docs.vast.ai/api-reference/instances/copy.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# copy

> Initiate a remote copy operation to transfer data from one instance to another or between an instance and the local machine.

CLI Usage: `vastai copy <src_id> <dst_id> <src_path> <dst_path>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/commands/copy_direct/
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
  /api/v0/commands/copy_direct/:
    put:
      tags:
        - Instances
      summary: copy
      description: >-
        Initiate a remote copy operation to transfer data from one instance to
        another or between an instance and the local machine.


        CLI Usage: `vastai copy <src_id> <dst_id> <src_path> <dst_path>`
      operationId: initiateRemoteRsync
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                src_id:
                  type: string
                  description: ID of the source instance.
                dst_id:
                  type: string
                  description: ID of the destination instance.
                src_path:
                  type: string
                  description: Path of the source data.
                dst_path:
                  type: string
                  description: Path of the destination data.
              required:
                - src_path
                - dst_path
      responses:
        '200':
          description: Remote copy initiated successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  msg:
                    type: string
                    example: >-
                      Remote to Remote copy initiated - check instance status
                      bar for progress updates (~30 seconds delayed).
        '400':
          description: Invalid arguments provided.
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
                    example: Invalid src_path.
        '404':
          description: Source or destination ID not found or access denied.
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
                    example: no_such_user
                  msg:
                    type: string
                    example: No such user.
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````