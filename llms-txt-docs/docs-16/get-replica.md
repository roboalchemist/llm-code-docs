# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/get-replica.md

# Get Replica

> This endpoint returns a single Replica by its unique identifier. 

Included in the response body is a `training_progress` string that represents the progress of the Replica training. If there are any errors during training, the `status` will be `error` and the `error_message` will be populated.


## OpenAPI

````yaml get /v2/replicas/{replica_id}
paths:
  path: /v2/replicas/{replica_id}
  method: get
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
              description: A unique identifier for the replica.
      query:
        verbose:
          schema:
            - type: boolean
              description: >-
                If set to true, the response will include additional replica
                data such as replica_type.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              replica_id:
                allOf:
                  - type: string
                    example: r783537ef5
                    description: A unique identifier for the replica.
              replica_name:
                allOf:
                  - type: string
                    example: My Replica
                    description: The name of the replica.
              thumbnail_video_url:
                allOf:
                  - type: string
                    description: >-
                      A direct link to the video that will be used as the
                      thumbnail for the replica.
              training_progress:
                allOf:
                  - type: string
                    example: 100/100
                    description: The progress of the replica training.
              status:
                allOf:
                  - type: string
                    example: completed
                    description: >-
                      The status of the replica. Possible values: started,
                      completed, error.
              created_at:
                allOf:
                  - type: string
                    example: '2024-01-24T07:14:03.327Z'
                    description: The date and time the replica was created.
              updated_at:
                allOf:
                  - type: string
                    example: '2024-01-24T07:14:03.327Z'
                    description: The date and time of when the replica was last updated.
              error_message:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      If the replica has an error, this will contain the error
                      message.
              replica_type:
                allOf:
                  - type: string
                    example: user'
                    description: >-
                      If `verbose` query paramter is set to true. The type of
                      replica. Possible values: user, system. User replicas are
                      replicas that have been created by users. System replicas
                      are stock Tavus replicas that anyone may use
        examples:
          example:
            value:
              replica_id: r783537ef5
              replica_name: My Replica
              thumbnail_video_url: <string>
              training_progress: 100/100
              status: completed
              created_at: '2024-01-24T07:14:03.327Z'
              updated_at: '2024-01-24T07:14:03.327Z'
              error_message: <string>
              replica_type: user'
        description: ''
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