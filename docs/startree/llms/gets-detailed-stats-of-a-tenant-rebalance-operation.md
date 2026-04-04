# Source: https://docs.startree.ai/api-reference/tenant/gets-detailed-stats-of-a-tenant-rebalance-operation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gets detailed stats of a tenant rebalance operation

> Gets detailed stats of a tenant rebalance operation

## OpenAPI

````yaml get /tenants/rebalanceStatus/{jobId}
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
  /tenants/rebalanceStatus/{jobId}:
    get:
      tags:
        - Tenant
      summary: Gets detailed stats of a tenant rebalance operation
      description: Gets detailed stats of a tenant rebalance operation
      operationId: rebalanceStatus_1
      parameters:
        - name: jobId
          in: path
          description: Tenant rebalance job id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TenantRebalanceJobStatusResponse'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    TenantRebalanceJobStatusResponse:
      type: object
      properties:
        timeElapsedSinceStartInSeconds:
          type: integer
          format: int64
        tenantRebalanceProgressStats:
          $ref: '#/components/schemas/TenantRebalanceProgressStats'
    TenantRebalanceProgressStats:
      type: object
      properties:
        timeToFinishInSeconds:
          type: integer
          format: int64
        completionStatusMsg:
          type: string
        startTimeMs:
          type: integer
          format: int64
        tableStatusMap:
          type: object
          additionalProperties:
            type: string
        totalTables:
          type: integer
          format: int32
        remainingTables:
          type: integer
          format: int32
        tableRebalanceJobIdMap:
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
