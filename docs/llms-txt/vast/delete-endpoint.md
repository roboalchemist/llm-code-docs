# Source: https://docs.vast.ai/api-reference/serverless/delete-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# delete endpoint

> Deletes an endpoint group by ID. Associated workergroups will also be deleted.

CLI Usage: `vastai delete endpoint <id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/endptjobs/{id}/
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
  /api/v0/endptjobs/{id}/:
    delete:
      tags:
        - Serverless
      summary: delete endpoint
      description: >-
        Deletes an endpoint group by ID. Associated workergroups will also be
        deleted.


        CLI Usage: `vastai delete endpoint <id>`
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the endpoint group to delete
          schema:
            type: integer
            example: 4242
      responses:
        '200':
          description: Endpoint group successfully deleted
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  deleted_workers:
                    type: array
                    description: List of worker instances that were deleted (if any)
                    items:
                      type: integer
                    example:
                      - 1001
                      - 1002
                  failed_workers:
                    type: array
                    description: List of worker instances that failed to delete (if any)
                    items:
                      type: integer
                    example: []
                  msg:
                    type: string
                    description: Additional information about the deletion
                    example: Deleted endpoint job and 2 workers
        '400':
          description: Bad request
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
                    example: Routegroup not found for user
        '401':
          description: Unauthorized
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
                  msg:
                    type: string
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=3.0
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````