# Source: https://docs.infera.org/api-reference/endpoint/worker-register.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Worker Register



## OpenAPI

````yaml post /worker/register_node
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /worker/register_node:
    post:
      summary: Worker Register
      operationId: worker_register_worker_register_node_post
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

````