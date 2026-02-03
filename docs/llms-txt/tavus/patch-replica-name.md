# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/patch-replica-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Rename Replica

> This endpoint renames a single Replica by its unique identifier.




## OpenAPI

````yaml patch /v2/replicas/{replica_id}/name
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
  /v2/replicas/{replica_id}/name:
    parameters:
      - name: replica_id
        in: path
        required: true
        description: The unique identifier of the persona.
        schema:
          type: string
          example: rf3073f2dcc1
    patch:
      tags:
        - Replicas
      summary: Rename Replica
      description: |
        This endpoint renames a single Replica by its unique identifier.
      operationId: renameReplica
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                replica_name:
                  type: string
                  example: Rio
              required:
                - replica_name
            examples:
              Rename Replica:
                value:
                  replica_name: Rio
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