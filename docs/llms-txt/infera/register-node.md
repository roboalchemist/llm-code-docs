# Source: https://docs.infera.org/api-reference/endpoint/register-node.md

# Register Node

## OpenAPI

````yaml post /register_node_secret
paths:
  path: /register_node_secret
  method: post
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              node_id:
                allOf:
                  - type: string
                    title: Node Id
              secret:
                allOf:
                  - type: string
                    title: Secret
            required: true
            title: NodeSecretRequest
            refIdentifier: '#/components/schemas/NodeSecretRequest'
            requiredProperties:
              - node_id
              - secret
        examples:
          example:
            value:
              node_id: <string>
              secret: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
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