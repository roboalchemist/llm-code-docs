# Source: https://docs.startree.ai/api-reference/connection/browse.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# browse

> Browse resources in a connection. Eg list directories/files in a s3 bucket, list tables in a database, list topics in a Kafka cluster etc.

## OpenAPI

````yaml post /connections/browse
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
  /connections/browse:
    post:
      tags:
        - Connection
      summary: browse
      description: >-
        Browse resources in a connection. Eg list directories/files in a s3
        bucket, list tables in a database, list topics in a Kafka cluster etc.
      operationId: browse
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Request'
        required: false
      responses:
        '200':
          description: List of keys based on input locator
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Response'
        '500':
          description: Internal error
          content: {}
      security:
        - oauth: []
components:
  schemas:
    Request:
      type: object
      properties:
        connection:
          $ref: '#/components/schemas/ConnectionApi'
        path:
          type: string
    Response:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/ItemApi'
    ConnectionApi:
      type: object
      properties:
        type:
          type: string
        params:
          type: object
          additionalProperties:
            type: object
            properties: {}
    ItemApi:
      type: object
      properties:
        name:
          type: string
        type:
          type: string
          enum:
            - DIR
            - FILE
            - TABLE
            - TOPIC
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
