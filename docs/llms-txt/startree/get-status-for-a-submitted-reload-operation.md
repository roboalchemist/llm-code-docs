# Source: https://docs.startree.ai/api-reference/segment/get-status-for-a-submitted-reload-operation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get status for a submitted reload operation

> Get status for a submitted reload operation

## OpenAPI

````yaml get /segments/segmentReloadStatus/{jobId}
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
  /segments/segmentReloadStatus/{jobId}:
    get:
      tags:
        - Segment
      summary: Get status for a submitted reload operation
      description: Get status for a submitted reload operation
      operationId: getReloadJobStatus
      parameters:
        - name: jobId
          in: path
          description: Reload job id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ServerReloadControllerJobStatusResponse'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    ServerReloadControllerJobStatusResponse:
      type: object
      properties:
        timeElapsedInMinutes:
          type: number
          format: double
        totalServersQueried:
          type: integer
          format: int32
        estimatedTimeRemainingInMinutes:
          type: number
          format: double
        totalServerCallsFailed:
          type: integer
          format: int32
        successCount:
          type: integer
          format: int32
        totalSegmentCount:
          type: integer
          format: int32
        metadata:
          type: object
          additionalProperties:
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
