# Source: https://docs.infera.org/api-reference/endpoint/node-jobs-stats.md

# Node Jobs Stats

## OpenAPI

````yaml post /node_jobs_stats
paths:
  path: /node_jobs_stats
  method: post
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              node_url:
                allOf:
                  - type: string
                    title: Node Url
              node_version:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Node Version
            required: true
            title: NodeRegistration
            refIdentifier: '#/components/schemas/NodeRegistration'
            requiredProperties:
              - node_url
        examples:
          example:
            value:
              node_url: <string>
              node_version: <string>
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