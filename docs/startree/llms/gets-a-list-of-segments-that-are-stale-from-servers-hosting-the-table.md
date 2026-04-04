# Source: https://docs.startree.ai/api-reference/segment/gets-a-list-of-segments-that-are-stale-from-servers-hosting-the-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gets a list of segments that are stale from servers hosting the table

> Gets a list of segments that are stale from servers hosting the table

## OpenAPI

````yaml get /segments/{tableNameWithType}/isStale
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
  /segments/{tableNameWithType}/isStale:
    get:
      tags:
        - Segment
      summary: Gets a list of segments that are stale from servers hosting the table
      description: Gets a list of segments that are stale from servers hosting the table
      operationId: getStaleSegments
      parameters:
        - name: tableNameWithType
          in: path
          description: Table name with type
          required: true
          schema:
            type: string
          example: myTable_REALTIME
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  $ref: '#/components/schemas/TableStaleSegmentResponse'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    TableStaleSegmentResponse:
      type: object
      properties:
        staleSegmentList:
          type: array
          readOnly: true
          items:
            $ref: '#/components/schemas/StaleSegment'
        validResponse:
          type: boolean
          readOnly: true
        errorMessage:
          type: string
          readOnly: true
    StaleSegment:
      type: object
      properties:
        segmentName:
          type: string
          readOnly: true
        reason:
          type: string
          readOnly: true
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
