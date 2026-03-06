# Source: https://docs.vast.ai/api-reference/instances/detach-ssh-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# detach ssh-key

> Detaches an SSH key from a specified instance, removing SSH access for that key.

CLI Usage: `vastai detach <instance_id> <ssh_key_id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/instances/{id}/ssh/{ssh_key_id}/
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
  /api/v0/instances/{id}/ssh/{ssh_key_id}/:
    delete:
      tags:
        - Instances
      summary: detach ssh-key
      description: >-
        Detaches an SSH key from a specified instance, removing SSH access for
        that key.


        CLI Usage: `vastai detach <instance_id> <ssh_key_id>`
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the instance to detach the SSH key from
          schema:
            type: integer
            example: 99999
        - name: ssh_key_id
          in: path
          required: true
          description: >
            Numeric ID of the SSH key to detach. Obtainable via `show ssh-keys`
            command
          schema:
            type: integer
            example: 12345
      responses:
        '200':
          description: SSH key successfully detached
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
                    example: SSH key removed from instance.
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
                      - invalid_request
                  msg:
                    type: string
                    example: Invalid request parameters
        '404':
          description: Instance or SSH key not found
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
                      - no_such_instance
                      - no_such_ssh_key
                  msg:
                    type: string
                    example: Instance not found.
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=2.0
        '500':
          description: Internal Server Error
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
                    example: delete_ssh_from_instance
                  msg:
                    type: string
                    example: Error deleting SSH key from instance
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````