# Source: https://docs.startree.ai/api-reference/table/gets-detailed-stats-of-a-rebalance-operation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gets detailed stats of a rebalance operation

> Gets detailed stats of a rebalance operation

## OpenAPI

````yaml get /rebalanceStatus/{jobId}
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
  /rebalanceStatus/{jobId}:
    get:
      tags:
        - Table
      summary: Gets detailed stats of a rebalance operation
      description: Gets detailed stats of a rebalance operation
      operationId: rebalanceStatus
      parameters:
        - name: jobId
          in: path
          description: Rebalance Job Id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ServerRebalanceJobStatusResponse'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    ServerRebalanceJobStatusResponse:
      type: object
      properties:
        tableRebalanceContext:
          $ref: '#/components/schemas/TableRebalanceContext'
        timeElapsedSinceStartInSeconds:
          type: integer
          format: int64
        tableRebalanceProgressStats:
          $ref: '#/components/schemas/TableRebalanceProgressStats'
    TableRebalanceContext:
      type: object
      properties:
        jobId:
          type: string
        originalJobId:
          type: string
        attemptId:
          type: integer
          format: int32
        config:
          $ref: '#/components/schemas/RebalanceConfig'
    TableRebalanceProgressStats:
      type: object
      properties:
        initialToTargetStateConvergence:
          $ref: '#/components/schemas/RebalanceStateStats'
        timeToFinishInSeconds:
          type: integer
          format: int64
        completionStatusMsg:
          type: string
        startTimeMs:
          type: integer
          format: int64
        externalViewToIdealStateConvergence:
          $ref: '#/components/schemas/RebalanceStateStats'
        currentToTargetConvergence:
          $ref: '#/components/schemas/RebalanceStateStats'
        status:
          type: string
          enum:
            - NO_OP
            - DONE
            - FAILED
            - IN_PROGRESS
            - ABORTED
            - CANCELLED
            - UNKNOWN_ERROR
    RebalanceConfig:
      type: object
      properties:
        minAvailableReplicas:
          type: integer
          format: int32
          example: 1
        heartbeatIntervalInMs:
          type: integer
          format: int64
          example: 300000
        heartbeatTimeoutInMs:
          type: integer
          format: int64
          example: 3600000
        retryInitialDelayInMs:
          type: integer
          format: int64
          example: 300000
        externalViewStabilizationTimeoutInMs:
          type: integer
          format: int64
          example: 3600000
        reassignInstances:
          type: boolean
          example: false
        includeConsuming:
          type: boolean
          example: false
        lowDiskMode:
          type: boolean
          example: false
        bestEfforts:
          type: boolean
          example: false
        updateTargetTier:
          type: boolean
          example: false
        maxAttempts:
          type: integer
          format: int32
          example: 3
        externalViewCheckIntervalInMs:
          type: integer
          format: int64
          example: 1000
        dryRun:
          type: boolean
          example: false
        preChecks:
          type: boolean
          example: false
        bootstrap:
          type: boolean
          example: false
        downtime:
          type: boolean
          example: false
    RebalanceStateStats:
      type: object
      properties:
        _segmentsMissing:
          type: integer
          format: int32
        _segmentsToRebalance:
          type: integer
          format: int32
        _percentSegmentsToRebalance:
          type: number
          format: double
        _replicasToRebalance:
          type: integer
          format: int32
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
