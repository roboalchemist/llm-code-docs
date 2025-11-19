# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/delete-replica.md

# Delete Replica

> This endpoint deletes a Replica by its unique ID. Deleted Replicas cannot be used in a conversation.


## OpenAPI

````yaml delete /v2/replicas/{replica_id}
paths:
  path: /v2/replicas/{replica_id}
  method: delete
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
      query:
        hard:
          schema:
            - type: boolean
              description: >-
                If set to true, the replica and associated assets (such as
                training footage) will be hard deleted. CAUTION: This action is
                irrevocable. Note that a hard delete of a replica does *not*
                delete the conversation created using said replica. See [Delete
                Video](https://docs.tavus.io/api-reference/video-request/delete-video)
                for more info.
              example: false
      header: {}
      cookie: {}
    body: {}
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