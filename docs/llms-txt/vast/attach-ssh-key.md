# Source: https://docs.vast.ai/api-reference/instances/attach-ssh-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# attach ssh-key

> Attaches an SSH key to the specified instance, allowing SSH access using the provided key.

CLI Usage: `vastai attach ssh <instance_id> <ssh_key>`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/instances/{id}/ssh/
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
  /api/v0/instances/{id}/ssh/:
    post:
      tags:
        - Instances
      summary: attach ssh-key
      description: >-
        Attaches an SSH key to the specified instance, allowing SSH access using
        the provided key.


        CLI Usage: `vastai attach ssh <instance_id> <ssh_key>`
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the instance to attach the SSH key to
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                ssh_key:
                  type: string
                  description: The SSH key to attach to the instance
                  example: ssh-rsa AAAAB3NzaC1yc2EAAA...
                  minLength: 1
      responses:
        '200':
          description: SSH key attached successfully
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
                    example: SSH key attached successfully
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
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