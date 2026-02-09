# Source: https://docs.infera.org/api-reference/endpoint/get-node-job-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Node Job History



## OpenAPI

````yaml post /node_job_history
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /node_job_history:
    post:
      summary: Get Node Job History
      operationId: get_node_job_history_node_job_history_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NodeRegistration'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - APIKeyHeader: []
components:
  schemas:
    NodeRegistration:
      properties:
        node_url:
          type: string
          title: Node Url
        node_version:
          anyOf:
            - type: string
            - type: 'null'
          title: Node Version
      type: object
      required:
        - node_url
      title: NodeRegistration
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````