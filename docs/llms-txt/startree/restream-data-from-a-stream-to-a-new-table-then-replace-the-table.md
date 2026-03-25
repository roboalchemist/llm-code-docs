# Source: https://docs.startree.ai/api-reference/restream/restream-data-from-a-stream-to-a-new-table-then-replace-the-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Restream data from a stream to a new table. Then replace the table

> Restream a table

## OpenAPI

````yaml post /tables/{tableName}/restream
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
  /tables/{tableName}/restream:
    post:
      tags:
        - Restream
      summary: Restream data from a stream to a new table. Then replace the table
      description: Restream a table
      operationId: restream
      parameters:
        - name: tableName
          in: path
          description: Name of the table with type to restream
          required: true
          schema:
            type: string
        - name: destTableNameWithType
          in: query
          description: Name of the destination table with type
          required: true
          schema:
            type: string
        - name: destTenant
          in: query
          description: Name of the tenant of the destination table
          required: true
          schema:
            type: string
        - name: destBrokerTenant
          in: query
          description: Name of the tenant of the destination table
          schema:
            type: string
        - name: debugPause
          in: query
          description: Pause at start
          schema:
            type: boolean
        - name: maxTableStreamLag
          in: query
          description: Max TableStream Lag
          schema:
            type: integer
            format: int64
        - name: maxRebalanceTimeMin
          in: query
          description: Max Rebalance Time (Mins)
          schema:
            type: integer
            format: int32
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TableRestreamStatusResponse'
      security:
        - oauth: []
components:
  schemas:
    TableRestreamStatusResponse:
      type: object
      properties:
        timeElapsedSinceStartInSeconds:
          type: integer
          format: int64
          readOnly: true
        jobId:
          type: string
          readOnly: true
        stage:
          type: string
          readOnly: true
          enum:
            - INIT
            - TABLE_STREAM
            - FORCE_COMMIT
            - REBALANCE
            - DONE
            - FAILED
            - CANCELLED
        restreamConfig:
          $ref: '#/components/schemas/TableRestreamConfig'
        tableStreamProgress:
          $ref: '#/components/schemas/TableStreamProgress'
        verboseTableStreamLag:
          type: object
          additionalProperties:
            type: object
            additionalProperties:
              type: integer
              format: int64
          readOnly: true
        forceCommitProgress:
          $ref: '#/components/schemas/ForceCommitProgress'
        segmentsToBeCommitted:
          uniqueItems: true
          type: array
          readOnly: true
          items:
            type: string
    TableRestreamConfig:
      type: object
      properties:
        debugPause:
          type: boolean
          example: false
        destTableNameWithType:
          type: string
          example: newTableName_REALTIME
        maxRebalanceTimeMin:
          type: integer
          format: int32
          example: 120
        destServerTenant:
          type: string
          example: restreamTenant
        destBrokerTenant:
          type: string
          example: restreamTenant
        maxTableStreamLag:
          type: integer
          format: int64
          example: 5000
        tableNameWithType:
          type: string
          example: tableName_REALTIME
    TableStreamProgress:
      type: object
      properties:
        lastProbedLag:
          type: integer
          format: int64
        lastProbeTimeMs:
          type: integer
          format: int64
        startTime:
          type: integer
          format: int64
    ForceCommitProgress:
      type: object
      properties:
        lastProbeTimeMs:
          type: integer
          format: int64
        startTime:
          type: integer
          format: int64
        totalConsumingSegments:
          type: integer
          format: int32
        consumingSegmentsCommitted:
          type: integer
          format: int32
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
