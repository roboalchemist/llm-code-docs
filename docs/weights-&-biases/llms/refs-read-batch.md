# Source: https://docs.wandb.ai/weave/reference/service-api/refs/refs-read-batch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Refs Read Batch



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /refs/read_batch
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /refs/read_batch:
    post:
      tags:
        - Refs
      summary: Refs Read Batch
      operationId: refs_read_batch_refs_read_batch_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RefsReadBatchReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RefsReadBatchRes'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBasic: []
components:
  schemas:
    RefsReadBatchReq:
      properties:
        refs:
          items:
            type: string
          type: array
          title: Refs
      additionalProperties: false
      type: object
      required:
        - refs
      title: RefsReadBatchReq
    RefsReadBatchRes:
      properties:
        vals:
          items: {}
          type: array
          title: Vals
      type: object
      required:
        - vals
      title: RefsReadBatchRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````