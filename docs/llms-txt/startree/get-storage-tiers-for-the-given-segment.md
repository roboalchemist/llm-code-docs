# Source: https://docs.startree.ai/api-reference/segment/get-storage-tiers-for-the-given-segment.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get storage tiers for the given segment

> Get storage tiers for the given segment

## OpenAPI

````yaml get /segments/{tableName}/{segmentName}/tiers
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
  /segments/{tableName}/{segmentName}/tiers:
    get:
      tags:
        - Segment
      summary: Get storage tiers for the given segment
      description: Get storage tiers for the given segment
      operationId: getSegmentTiers
      parameters:
        - name: tableName
          in: path
          description: Name of the table
          required: true
          schema:
            type: string
        - name: segmentName
          in: path
          description: Name of the segment
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: OFFLINE|REALTIME
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Success
          content: {}
        '404':
          description: Table or segment not found
          content: {}
        '500':
          description: Internal server error
          content: {}
      security:
        - oauth: []
        - database: []
components:
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
