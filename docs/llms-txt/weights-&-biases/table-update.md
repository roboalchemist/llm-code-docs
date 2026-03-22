# Source: https://docs.wandb.ai/weave/reference/service-api/tables/table-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Table Update



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /table/update
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /table/update:
    post:
      tags:
        - Tables
      summary: Table Update
      operationId: table_update_table_update_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TableUpdateReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TableUpdateRes'
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
    TableUpdateReq:
      properties:
        project_id:
          type: string
          title: Project Id
        base_digest:
          type: string
          title: Base Digest
        updates:
          items:
            anyOf:
              - $ref: '#/components/schemas/TableAppendSpec'
              - $ref: '#/components/schemas/TablePopSpec'
              - $ref: '#/components/schemas/TableInsertSpec'
          type: array
          title: Updates
      additionalProperties: false
      type: object
      required:
        - project_id
        - base_digest
        - updates
      title: TableUpdateReq
    TableUpdateRes:
      properties:
        digest:
          type: string
          title: Digest
        updated_row_digests:
          items:
            type: string
          type: array
          title: Updated Row Digests
          description: The digests of the rows that were updated
      type: object
      required:
        - digest
      title: TableUpdateRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    TableAppendSpec:
      properties:
        append:
          $ref: '#/components/schemas/TableAppendSpecPayload'
      type: object
      required:
        - append
      title: TableAppendSpec
    TablePopSpec:
      properties:
        pop:
          $ref: '#/components/schemas/TablePopSpecPayload'
      type: object
      required:
        - pop
      title: TablePopSpec
    TableInsertSpec:
      properties:
        insert:
          $ref: '#/components/schemas/TableInsertSpecPayload'
      type: object
      required:
        - insert
      title: TableInsertSpec
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
    TableAppendSpecPayload:
      properties:
        row:
          additionalProperties: true
          type: object
          title: Row
      type: object
      required:
        - row
      title: TableAppendSpecPayload
    TablePopSpecPayload:
      properties:
        index:
          type: integer
          title: Index
      type: object
      required:
        - index
      title: TablePopSpecPayload
    TableInsertSpecPayload:
      properties:
        index:
          type: integer
          title: Index
        row:
          additionalProperties: true
          type: object
          title: Row
      type: object
      required:
        - index
        - row
      title: TableInsertSpecPayload
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````