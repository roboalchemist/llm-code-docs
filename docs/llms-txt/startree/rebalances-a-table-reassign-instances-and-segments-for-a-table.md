# Source: https://docs.startree.ai/api-reference/table/rebalances-a-table-reassign-instances-and-segments-for-a-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rebalances a table (reassign instances and segments for a table)

> Rebalances a table (reassign instances and segments for a table)

## OpenAPI

````yaml post /tables/{tableName}/rebalance
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
  /tables/{tableName}/rebalance:
    post:
      tags:
        - Table
      summary: Rebalances a table (reassign instances and segments for a table)
      description: Rebalances a table (reassign instances and segments for a table)
      operationId: rebalance
      parameters:
        - name: tableName
          in: path
          description: Name of the table to rebalance
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: OFFLINE|REALTIME
          required: true
          schema:
            type: string
        - name: dryRun
          in: query
          description: Whether to rebalance table in dry-run mode
          schema:
            type: boolean
            default: false
        - name: preChecks
          in: query
          description: >-
            Whether to enable pre-checks for table, must be in dry-run mode to
            enable
          schema:
            type: boolean
            default: false
        - name: reassignInstances
          in: query
          description: Whether to reassign instances before reassigning segments
          schema:
            type: boolean
            default: false
        - name: includeConsuming
          in: query
          description: Whether to reassign CONSUMING segments for real-time table
          schema:
            type: boolean
            default: false
        - name: bootstrap
          in: query
          description: >-
            Whether to rebalance table in bootstrap mode (regardless of minimum
            segment movement, reassign all segments in a round-robin fashion as
            if adding new segments to an empty table)
          schema:
            type: boolean
            default: false
        - name: downtime
          in: query
          description: Whether to allow downtime for the rebalance
          schema:
            type: boolean
            default: false
        - name: minAvailableReplicas
          in: query
          description: >-
            For no-downtime rebalance, minimum number of replicas to keep alive
            during rebalance, or maximum number of replicas allowed to be
            unavailable if value is negative
          schema:
            type: integer
            format: int32
            default: 1
        - name: lowDiskMode
          in: query
          description: >-
            For no-downtime rebalance, whether to enable low disk mode during
            rebalance. When enabled, segments will first be offloaded from
            servers, then added to servers after offload is done while
            maintaining the min available replicas. It may increase the total
            time of the rebalance, but can be useful when servers are low on
            disk space, and we want to scale up the cluster and rebalance the
            table to more servers.
          schema:
            type: boolean
            default: false
        - name: bestEfforts
          in: query
          description: >-
            Whether to use best-efforts to rebalance (not fail the rebalance
            when the no-downtime contract cannot be achieved)
          schema:
            type: boolean
            default: false
        - name: externalViewCheckIntervalInMs
          in: query
          description: How often to check if external view converges with ideal states
          schema:
            type: integer
            format: int64
            default: 1000
        - name: externalViewStabilizationTimeoutInMs
          in: query
          description: How long to wait till external view converges with ideal states
          schema:
            type: integer
            format: int64
            default: 3600000
        - name: heartbeatIntervalInMs
          in: query
          description: How often to make a status update (i.e. heartbeat)
          schema:
            type: integer
            format: int64
            default: 300000
        - name: heartbeatTimeoutInMs
          in: query
          description: >-
            How long to wait for next status update (i.e. heartbeat) before the
            job is considered failed
          schema:
            type: integer
            format: int64
            default: 3600000
        - name: maxAttempts
          in: query
          description: Max number of attempts to rebalance
          schema:
            type: integer
            format: int32
            default: 3
        - name: retryInitialDelayInMs
          in: query
          description: Initial delay to exponentially backoff retry
          schema:
            type: integer
            format: int64
            default: 300000
        - name: updateTargetTier
          in: query
          description: Whether to update segment target tier as part of the rebalance
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RebalanceResult'
      security:
        - oauth: []
        - database: []
components:
  schemas:
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
