# Source: https://docs.startree.ai/api-reference/schema/update-a-schema.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a schema

> Updates a schema

## OpenAPI

````yaml put /schemas/{schemaName}
openapi: 3.0.1
info:
  title: Pinot Controller API
  description: APIs for accessing Pinot Controller information
  contact:
    name: https://github.com/apache/pinot
  version: '1.0'
servers:
  - url: https://dev.startree.ai/
security: []
tags:
  - name: AtomicIngestion
  - name: BatchRestart
  - name: ClusterHealth
  - name: Connection
  - name: ConsistentPush
  - name: DedupSnapshot
  - name: PerfAdvisor
  - name: RateLimiter
  - name: Table
  - name: Restream
  - name: Tuner
  - name: AlterTable
  - name: UpsertSnapshot
  - name: Cluster
  - name: User
  - name: Application
  - name: Broker
  - name: AppConfigs
  - name: Auth
  - name: Health
  - name: Logger
  - name: PeriodicTask
  - name: Database
  - name: Instance
  - name: Leader
  - name: Query
  - name: Schema
  - name: Segment
  - name: Tenant
  - name: Task
  - name: Upsert
  - name: Version
  - name: Zookeeper
paths:
  /schemas/{schemaName}:
    put:
      tags:
        - Schema
      summary: Update a schema
      description: Updates a schema
      operationId: updateSchema_1
      parameters:
        - name: schemaName
          in: path
          description: Name of the schema
          required: true
          schema:
            type: string
        - name: reload
          in: query
          description: Whether to reload the table if the new schema is backward compatible
          schema:
            type: boolean
            default: false
      requestBody:
        content:
          '*/*':
            schema:
              $ref: '#/components/schemas/FormDataMultiPart'
        required: false
      responses:
        '200':
          description: Successfully updated schema
          content: {}
        '400':
          description: Missing or invalid request body
          content: {}
        '404':
          description: Schema not found
          content: {}
        '500':
          description: Internal error
          content: {}
      security:
        - oauth: []
        - database: []
components:
  schemas:
    FormDataMultiPart:
      type: object
      properties:
        contentDisposition:
          $ref: '#/components/schemas/ContentDisposition'
        entity:
          type: object
          properties: {}
        headers:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
        mediaType:
          $ref: '#/components/schemas/MediaType'
        messageBodyWorkers:
          $ref: '#/components/schemas/MessageBodyWorkers'
        parent:
          $ref: '#/components/schemas/MultiPart'
        providers:
          $ref: '#/components/schemas/Providers'
        bodyParts:
          type: array
          items:
            $ref: '#/components/schemas/BodyPart'
        fields:
          type: object
          additionalProperties:
            type: array
            items:
              $ref: '#/components/schemas/FormDataBodyPart'
        parameterizedHeaders:
          type: object
          additionalProperties:
            type: array
            items:
              $ref: '#/components/schemas/ParameterizedHeader'
    ContentDisposition:
      type: object
      properties:
        type:
          type: string
        parameters:
          type: object
          additionalProperties:
            type: string
        fileName:
          type: string
        creationDate:
          type: string
          format: date-time
        modificationDate:
          type: string
          format: date-time
        readDate:
          type: string
          format: date-time
        size:
          type: integer
          format: int64
    MediaType:
      type: object
      properties:
        type:
          type: string
        subtype:
          type: string
        parameters:
          type: object
          additionalProperties:
            type: string
        wildcardType:
          type: boolean
        wildcardSubtype:
          type: boolean
    MessageBodyWorkers:
      type: object
    MultiPart:
      type: object
      properties:
        contentDisposition:
          $ref: '#/components/schemas/ContentDisposition'
        entity:
          type: object
          properties: {}
        headers:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
        mediaType:
          $ref: '#/components/schemas/MediaType'
        messageBodyWorkers:
          $ref: '#/components/schemas/MessageBodyWorkers'
        parent:
          $ref: '#/components/schemas/MultiPart'
        providers:
          $ref: '#/components/schemas/Providers'
        bodyParts:
          type: array
          items:
            $ref: '#/components/schemas/BodyPart'
        parameterizedHeaders:
          type: object
          additionalProperties:
            type: array
            items:
              $ref: '#/components/schemas/ParameterizedHeader'
    Providers:
      type: object
    BodyPart:
      type: object
      properties:
        contentDisposition:
          $ref: '#/components/schemas/ContentDisposition'
        entity:
          type: object
          properties: {}
        headers:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
        mediaType:
          $ref: '#/components/schemas/MediaType'
        messageBodyWorkers:
          $ref: '#/components/schemas/MessageBodyWorkers'
        parent:
          $ref: '#/components/schemas/MultiPart'
        providers:
          $ref: '#/components/schemas/Providers'
        parameterizedHeaders:
          type: object
          additionalProperties:
            type: array
            items:
              $ref: '#/components/schemas/ParameterizedHeader'
    FormDataBodyPart:
      type: object
      properties:
        contentDisposition:
          $ref: '#/components/schemas/ContentDisposition'
        entity:
          type: object
          properties: {}
        headers:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
        mediaType:
          $ref: '#/components/schemas/MediaType'
        messageBodyWorkers:
          $ref: '#/components/schemas/MessageBodyWorkers'
        parent:
          $ref: '#/components/schemas/MultiPart'
        providers:
          $ref: '#/components/schemas/Providers'
        formDataContentDisposition:
          $ref: '#/components/schemas/FormDataContentDisposition'
        simple:
          type: boolean
        name:
          type: string
        value:
          type: string
        parameterizedHeaders:
          type: object
          additionalProperties:
            type: array
            items:
              $ref: '#/components/schemas/ParameterizedHeader'
    ParameterizedHeader:
      type: object
      properties:
        value:
          type: string
        parameters:
          type: object
          additionalProperties:
            type: string
    FormDataContentDisposition:
      type: object
      properties:
        type:
          type: string
        parameters:
          type: object
          additionalProperties:
            type: string
        fileName:
          type: string
        creationDate:
          type: string
          format: date-time
        modificationDate:
          type: string
          format: date-time
        readDate:
          type: string
          format: date-time
        size:
          type: integer
          format: int64
        name:
          type: string
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header
    database:
      type: apiKey
      description: >-
        Database context passed through http header. If no context is provided
        'default' database context will be considered.
      name: database
      in: header

````

Built with [Mintlify](https://mintlify.com).
