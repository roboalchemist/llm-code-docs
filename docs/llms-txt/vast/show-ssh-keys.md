# Source: https://docs.vast.ai/api-reference/instances/show-ssh-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show ssh-keys

> Retrieves the SSH keys associated with a specific instance.

CLI Usage: `vastai show ssh-keys <instance_id>`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/instances/{instance_id}/ssh/
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
  /api/v0/instances/{instance_id}/ssh/:
    get:
      tags:
        - Instances
      summary: show ssh-keys
      description: |-
        Retrieves the SSH keys associated with a specific instance.

        CLI Usage: `vastai show ssh-keys <instance_id>`
      parameters:
        - name: instance_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the instance to retrieve SSH keys for.
          example: 17816188
      responses:
        '200':
          description: Success response with SSH keys
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  ssh_keys:
                    type: string
                    description: JSON string containing array of SSH key objects
                    example: >-
                      [{"id": 1, "name": "my-key", "public_key": "ssh-rsa
                      AAAA..."}]
        '400':
          description: Bad Request - Invalid instance ID
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Unauthorized - Invalid or missing authentication
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Instance not found
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