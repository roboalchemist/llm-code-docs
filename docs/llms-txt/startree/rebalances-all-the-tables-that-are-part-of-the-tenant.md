# Source: https://docs.startree.ai/api-reference/tenant/rebalances-all-the-tables-that-are-part-of-the-tenant.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rebalances all the tables that are part of the tenant

## OpenAPI

````yaml post /tenants/{tenantName}/rebalance
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
  /tenants/{tenantName}/rebalance:
    post:
      tags:
        - Tenant
      summary: Rebalances all the tables that are part of the tenant
      operationId: rebalance_1
      parameters:
        - name: tenantName
          in: path
          description: Name of the tenant whose table are to be rebalanced
          required: true
          schema:
            type: string
      requestBody:
        content:
          '*/*':
            schema:
              $ref: '#/components/schemas/TenantRebalanceConfig'
        required: true
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TenantRebalanceResult'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    TenantRebalanceConfig:
      type: object
      properties:
        degreeOfParallelism:
          type: integer
          format: int32
          example: 1
        verboseResult:
          type: boolean
        parallelWhitelist:
          uniqueItems: true
          type: array
          items:
            type: string
        parallelBlacklist:
          uniqueItems: true
          type: array
          items:
            type: string
        tenantName:
          type: string
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
    TenantRebalanceResult:
      type: object
      properties:
        rebalanceTableResults:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/RebalanceResult'
        jobId:
          type: string
    RebalanceResult:
      type: object
      properties:
        jobId:
          type: string
          readOnly: true
        status:
          type: string
          readOnly: true
          enum:
            - NO_OP
            - DONE
            - FAILED
            - IN_PROGRESS
            - ABORTED
            - CANCELLED
            - UNKNOWN_ERROR
        description:
          type: string
          readOnly: true
        instanceAssignment:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/InstancePartitions'
          readOnly: true
        tierInstanceAssignment:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/InstancePartitions'
          readOnly: true
        segmentAssignment:
          type: object
          additionalProperties:
            type: object
            additionalProperties:
              type: string
          readOnly: true
        preChecksResult:
          type: object
          additionalProperties:
            type: string
          readOnly: true
        rebalanceSummaryResult:
          $ref: '#/components/schemas/RebalanceSummaryResult'
    InstancePartitions:
      type: object
      properties:
        instancePartitionsName:
          type: string
          readOnly: true
        partitionToInstancesMap:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
          readOnly: true
    RebalanceSummaryResult:
      type: object
      properties:
        serverInfo:
          $ref: '#/components/schemas/ServerInfo'
        segmentInfo:
          $ref: '#/components/schemas/SegmentInfo'
    ServerInfo:
      type: object
      properties:
        numServersGettingNewSegments:
          type: integer
          format: int32
          readOnly: true
        numServers:
          $ref: '#/components/schemas/RebalanceChangeInfo'
        serversAdded:
          uniqueItems: true
          type: array
          readOnly: true
          items:
            type: string
        serversRemoved:
          uniqueItems: true
          type: array
          readOnly: true
          items:
            type: string
        serversUnchanged:
          uniqueItems: true
          type: array
          readOnly: true
          items:
            type: string
        serversGettingNewSegments:
          uniqueItems: true
          type: array
          readOnly: true
          items:
            type: string
        serverSegmentChangeInfo:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ServerSegmentChangeInfo'
          readOnly: true
    SegmentInfo:
      type: object
      properties:
        totalSegmentsToBeMoved:
          type: integer
          format: int32
          readOnly: true
        maxSegmentsAddedToASingleServer:
          type: integer
          format: int32
          readOnly: true
        estimatedAverageSegmentSizeInBytes:
          type: integer
          format: int64
          readOnly: true
        totalEstimatedDataToBeMovedInBytes:
          type: integer
          format: int64
          readOnly: true
        replicationFactor:
          $ref: '#/components/schemas/RebalanceChangeInfo'
        numSegmentsInSingleReplica:
          $ref: '#/components/schemas/RebalanceChangeInfo'
        numSegmentsAcrossAllReplicas:
          $ref: '#/components/schemas/RebalanceChangeInfo'
    RebalanceChangeInfo:
      type: object
      properties:
        valueBeforeRebalance:
          type: integer
          format: int32
          readOnly: true
        expectedValueAfterRebalance:
          type: integer
          format: int32
          readOnly: true
    ServerSegmentChangeInfo:
      type: object
      properties:
        serverStatus:
          type: string
          readOnly: true
          enum:
            - ADDED
            - REMOVED
            - UNCHANGED
        totalSegmentsAfterRebalance:
          type: integer
          format: int32
          readOnly: true
        totalSegmentsBeforeRebalance:
          type: integer
          format: int32
          readOnly: true
        segmentsAdded:
          type: integer
          format: int32
          readOnly: true
        segmentsDeleted:
          type: integer
          format: int32
          readOnly: true
        segmentsUnchanged:
          type: integer
          format: int32
          readOnly: true
        tagList:
          type: array
          readOnly: true
          items:
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
