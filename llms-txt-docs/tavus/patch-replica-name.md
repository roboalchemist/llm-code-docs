# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/patch-replica-name.md

# Rename Replica

> This endpoint renames a single Replica by its unique identifier.


## OpenAPI

````yaml patch /v2/replicas/{replica_id}/name
paths:
  path: /v2/replicas/{replica_id}/name
  method: patch
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path:
        replica_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the persona.
              example: rf3073f2dcc1
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              replica_name:
                allOf:
                  - type: string
                    example: Rio
            requiredProperties:
              - replica_name
        examples:
          Rename Replica:
            value:
              replica_name: Rio
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: OK
        examples: {}
        description: OK
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid replica_id
        examples:
          example:
            value:
              error: Invalid replica_id
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
  deprecated: false
  type: path
components:
  schemas: {}

````