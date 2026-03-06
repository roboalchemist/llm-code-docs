# Source: https://docs.vast.ai/api-reference/instances/cloud-copy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# cloud copy

> Starts a cloud copy operation by sending a command to the remote server. The operation can transfer data between an instance and a cloud service.

CLI Usage: `vastai cloud copy <instance_id> <src> <dst> [options]`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/commands/rclone/
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
  /api/v0/commands/rclone/:
    post:
      tags:
        - Instances
      summary: cloud copy
      description: >-
        Starts a cloud copy operation by sending a command to the remote server.
        The operation can transfer data between an instance and a cloud service.


        CLI Usage: `vastai cloud copy <instance_id> <src> <dst> [options]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                instance_id:
                  type: string
                  description: ID of the instance.
                src:
                  type: string
                  description: Source path for the copy operation.
                dst:
                  type: string
                  description: Destination path for the copy operation.
                selected:
                  type: string
                  description: ID of the cloud connection.
                transfer:
                  type: string
                  description: >-
                    Type of transfer (e.g., "Instance To Cloud" or "Cloud To
                    Instance").
                flags:
                  type: array
                  items:
                    type: string
                  description: Additional flags for the operation.
                api_key:
                  type: string
                  description: API key for authentication.
      responses:
        '200':
          description: Cloud copy operation initiated successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  msg:
                    type: string
                  result_url:
                    type: string
        '400':
          description: Bad request due to invalid parameters or cloud service.
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  msg:
                    type: string
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````