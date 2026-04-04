# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/delete-replica.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Replica

> This endpoint deletes a Replica by its unique ID. Deleted Replicas cannot be used in a conversation.




## OpenAPI

````yaml delete /v2/replicas/{replica_id}
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
    delete:
      tags:
        - Replicas
      summary: Delete Replica
      description: >
        This endpoint deletes a Replica by its unique ID. Deleted Replicas
        cannot be used in a conversation.
      operationId: deleteReplica
      parameters:
        - name: replica_id
          in: path
          required: true
          description: The unique identifier of the persona.
          schema:
            type: string
            example: rf3073f2dcc1
        - name: hard
          in: query
          schema:
            type: boolean
            example: false
          description: >-
            If set to true, the replica and associated assets (such as training
            footage) will be hard deleted. CAUTION: This action is irrevocable.
            Note that a hard delete of a replica does *not* delete the
            conversation created using said replica. See [Delete
            Video](https://docs.tavus.io/api-reference/video-request/delete-video)
            for more info.
      responses:
        '200':
          description: OK
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