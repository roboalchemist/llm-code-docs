# Source: https://docs.startree.ai/api-reference/segment/resets-all-segments-when-errorsegmentsonly-=-false-or-segments-with-error-state-when-errorsegmentsonly-=-true-of-the-table-by-first-disabling-them-waiting-for-external-view-to-stabilize-and-finally-enabling-them.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Resets all segments (when errorSegmentsOnly = false) or segments with Error state (when errorSegmentsOnly = true) of the table, by first disabling them, waiting for external view to stabilize, and finally enabling them

> Resets segments by disabling and then enabling them

## OpenAPI

````yaml post /segments/{tableNameWithType}/reset
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
  /segments/{tableNameWithType}/reset:
    post:
      tags:
        - Segment
      summary: >-
        Resets all segments (when errorSegmentsOnly = false) or segments with
        Error state (when errorSegmentsOnly = true) of the table, by first
        disabling them, waiting for external view to stabilize, and finally
        enabling them
      description: Resets segments by disabling and then enabling them
      operationId: resetSegments
      parameters:
        - name: tableNameWithType
          in: path
          description: Name of the table with type
          required: true
          schema:
            type: string
        - name: targetInstance
          in: query
          description: Name of the target instance to reset
          schema:
            type: string
        - name: errorSegmentsOnly
          in: query
          description: Whether to reset only segments with error state
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    SuccessResponse:
      type: object
      properties:
        status:
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
