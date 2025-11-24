# Source: https://docs.infera.org/api-reference/endpoint/node-points-ep.md

# Node Points Ep

## OpenAPI

````yaml get /node_points/{node_id}
paths:
  path: /node_points/{node_id}
  method: get
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
  request:
    security:
      - title: APIKeyHeader
        parameters:
          query: {}
          header:
            api_key:
              type: apiKey
          cookie: {}
    parameters:
      path:
        node_id:
          schema:
            - type: string
              required: true
              title: Node Id
      query: {}
      header: {}
      cookie: {}
    body: {}
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