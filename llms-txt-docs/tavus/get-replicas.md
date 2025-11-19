# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/get-replicas.md

# List Replicas

> This endpoint returns a list of all Replicas created by the account associated with the API Key in use. In the response, a root level `data` key will contain the list of Replicas.


## OpenAPI

````yaml get /v2/replicas
paths:
  path: /v2/replicas
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
      path: {}
      query:
        limit:
          schema:
            - type: integer
              description: The number of replicas to return per page.
        page:
          schema:
            - type: integer
              description: The page number to return
        verbose:
          schema:
            - type: boolean
              description: >-
                If set to true, the response will include additional replica
                data such as the replica type.
        replica_type:
          schema:
            - type: enum<string>
              enum:
                - user
                - system
              description: >-
                If set to user, the response will only include user replicas. If
                set to system, the response will only include stock replicas.
        replica_ids:
          schema:
            - type: string
              description: >-
                A comma separated list of replica ids to filter the response by.
                Example: `replica_ids=re1074c227,r243eed46c`
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        replica_id:
                          type: string
                          example: r783537ef5
                          description: A unique identifier for the replica.
                        replica_name:
                          type: string
                          example: My Replica
                          description: The name of the replica.
                        thumbnail_video_url:
                          type: string
                          description: >-
                            A direct link to the video that will be used as the
                            thumbnail for the replica.
                        training_progress:
                          type: string
                          example: 100/100
                          description: The progress of the replica training.
                        status:
                          type: string
                          example: completed
                          description: >-
                            The status of the replica. Possible values: started,
                            completed, error.
                        created_at:
                          type: string
                        replica_type:
                          type: string
                          example: user'
                          description: >-
                            If `verbose` query paramter is set to true. The type
                            of replica. Possible values: user, system. User
                            replicas are replicas that have been created by
                            users. System replicas are stock Tavus replicas that
                            anyone may use
              total_count:
                allOf:
                  - type: integer
                    description: The total number of replicas given the filters provided.
                    example: 42
        examples:
          example:
            value:
              data:
                - replica_id: r783537ef5
                  replica_name: My Replica
                  thumbnail_video_url: <string>
                  training_progress: 100/100
                  status: completed
                  created_at: <string>
                  replica_type: user'
              total_count: 42
        description: ''
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