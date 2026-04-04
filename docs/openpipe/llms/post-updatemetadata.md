# Source: https://docs.openpipe.ai/api-reference/post-updatemetadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Metadata

> Update tags metadata for logged calls matching the provided filters.



## OpenAPI

````yaml post /logs/update-metadata
openapi: 3.0.3
info:
  title: OpenPipe API
  description: The public API for reporting API calls to OpenPipe
  version: 0.1.1
servers:
  - url: https://api.openpipe.ai/api/v1
security: []
paths:
  /logs/update-metadata:
    post:
      description: Update tags metadata for logged calls matching the provided filters.
      operationId: updateLogMetadata
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                filters:
                  type: array
                  items:
                    type: object
                    properties:
                      field:
                        type: string
                        description: >-
                          The field to filter on. Possible fields include:
                          `model`, `completionId`, and `metadata.your_tag_name`.
                      equals:
                        anyOf:
                          - type: string
                          - type: number
                          - type: boolean
                    required:
                      - field
                      - equals
                    additionalProperties: false
                metadata:
                  type: object
                  additionalProperties:
                    anyOf:
                      - type: string
                      - enum:
                          - 'null'
                        nullable: true
                  description: >-
                    Extra metadata to attach to the call for filtering. Eg {
                    "userId": "123", "prompt_id": "populate-title" }
              required:
                - filters
                - metadata
              additionalProperties: false
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  matchedLogs:
                    type: number
                required:
                  - matchedLogs
                additionalProperties: false
        default:
          $ref: '#/components/responses/error'
      security:
        - Authorization: []
components:
  responses:
    error:
      description: Error response
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
              code:
                type: string
              issues:
                type: array
                items:
                  type: object
                  properties:
                    message:
                      type: string
                  required:
                    - message
                  additionalProperties: false
            required:
              - message
              - code
            additionalProperties: false
  securitySchemes:
    Authorization:
      type: http
      scheme: bearer

````