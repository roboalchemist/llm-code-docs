# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/get-replicas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Replicas

> This endpoint returns a list of all Replicas created by the account associated with the API Key in use. In the response, a root level `data` key will contain the list of Replicas.




## OpenAPI

````yaml get /v2/replicas
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/replicas:
    get:
      tags:
        - Replicas
      summary: List Replicas
      description: >
        This endpoint returns a list of all Replicas created by the account
        associated with the API Key in use. In the response, a root level `data`
        key will contain the list of Replicas.
      operationId: listReplicas
      parameters:
        - in: query
          name: limit
          schema:
            type: integer
          description: The number of replicas to return per page.
        - in: query
          name: page
          schema:
            type: integer
          description: The page number to return
        - in: query
          name: verbose
          schema:
            type: boolean
          description: >-
            If set to true, the response will include additional replica data
            such as the replica type.
        - in: query
          name: replica_type
          schema:
            type: string
            enum:
              - user
              - system
          description: >-
            If set to user, the response will only include user replicas. If set
            to system, the response will only include stock replicas.
        - in: query
          name: replica_ids
          schema:
            type: string
          description: >-
            A comma separated list of replica ids to filter the response by.
            Example: `replica_ids=re1074c227,r243eed46c`
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
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
                    type: integer
                    description: The total number of replicas given the filters provided.
                    example: 42
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid access token
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````