# Source: https://docs.startree.ai/api-reference/table/ingest-a-file.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ingest a file

> Creates a segment using given file and pushes it to Pinot.
 All steps happen on the controller. This API is NOT meant for production environments/large input files.
 Example usage (query params need encoding):

```
curl -X POST -F file=@data.json -H "Content-Type: multipart/form-data" "http://localhost:9000/ingestFromFile?tableNameWithType=foo_OFFLINE&
batchConfigMapStr={
  "inputFormat":"csv",
  "recordReader.prop.delimiter":"|"
}" 
```

## OpenAPI

````yaml post /ingestFromFile
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
  /ingestFromFile:
    post:
      tags:
        - Table
      summary: Ingest a file
      description: >-
        Creates a segment using given file and pushes it to Pinot. 
         All steps happen on the controller. This API is NOT meant for production environments/large input files. 
         Example usage (query params need encoding):
        ```

        curl -X POST -F file=@data.json -H "Content-Type: multipart/form-data"
        "http://localhost:9000/ingestFromFile?tableNameWithType=foo_OFFLINE&

        batchConfigMapStr={
          "inputFormat":"csv",
          "recordReader.prop.delimiter":"|"
        }" 

        ```
      operationId: ingestFromFile
      parameters:
        - name: tableNameWithType
          in: query
          description: Name of the table to upload the file to
          required: true
          schema:
            type: string
        - name: batchConfigMapStr
          in: query
          description: >-
            Batch config Map as json string. Must pass inputFormat, and
            optionally record reader properties. e.g. {"inputFormat":"json"}
          required: true
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/FormDataMultiPart'
        required: false
      responses:
        default:
          description: successful operation
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
