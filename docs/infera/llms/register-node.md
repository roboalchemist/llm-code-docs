# Source: https://docs.infera.org/api-reference/endpoint/register-node.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Register Node



## OpenAPI

````yaml post /register_node_secret
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /register_node_secret:
    post:
      summary: Register Node
      operationId: register_node_register_node_secret_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NodeSecretRequest'
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
    NodeSecretRequest:
      properties:
        node_id:
          type: string
          title: Node Id
        secret:
          type: string
          title: Secret
      type: object
      required:
        - node_id
        - secret
      title: NodeSecretRequest
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