# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/get-replica.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Replica

> This endpoint returns a single Replica by its unique identifier. 

Included in the response body is a `training_progress` string that represents the progress of the Replica training. If there are any errors during training, the `status` will be `error` and the `error_message` will be populated.




## OpenAPI

````yaml get /v2/replicas/{replica_id}
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
  /v2/replicas/{replica_id}:
    get:
      tags:
        - Replicas
      summary: Get Replica
      description: >
        This endpoint returns a single Replica by its unique identifier. 


        Included in the response body is a `training_progress` string that
        represents the progress of the Replica training. If there are any errors
        during training, the `status` will be `error` and the `error_message`
        will be populated.
      operationId: getReplica
      parameters:
        - in: path
          name: replica_id
          required: true
          schema:
            type: string
          description: A unique identifier for the replica.
        - in: query
          name: verbose
          schema:
            type: boolean
          description: >-
            If set to true, the response will include additional replica data
            such as replica_type.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
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
                    example: '2024-01-24T07:14:03.327Z'
                    description: The date and time the replica was created.
                  updated_at:
                    type: string
                    example: '2024-01-24T07:14:03.327Z'
                    description: The date and time of when the replica was last updated.
                  error_message:
                    type: string
                    nullable: true
                    description: >-
                      If the replica has an error, this will contain the error
                      message.
                  replica_type:
                    type: string
                    example: user'
                    description: >-
                      If `verbose` query paramter is set to true. The type of
                      replica. Possible values: user, system. User replicas are
                      replicas that have been created by users. System replicas
                      are stock Tavus replicas that anyone may use
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Invalid replica_id
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