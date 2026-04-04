# Source: https://docs.startree.ai/api-reference/table/get-the-aggregate-validdocids-metadata-of-all-segments-for-a-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the aggregate validDocIds metadata of all segments for a table

> Get the aggregate validDocIds metadata of all segments for a table

## OpenAPI

````yaml get /tables/{tableName}/validDocIdsMetadata
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
  /tables/{tableName}/validDocIdsMetadata:
    get:
      tags:
        - Table
      summary: Get the aggregate validDocIds metadata of all segments for a table
      description: Get the aggregate validDocIds metadata of all segments for a table
      operationId: getTableAggregateValidDocIdsMetadata
      parameters:
        - name: tableName
          in: path
          description: Name of the table
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: OFFLINE|REALTIME
          schema:
            type: string
        - name: segmentNames
          in: query
          description: A list of segments
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
        - name: validDocIdsType
          in: query
          description: Valid doc ids type
          schema:
            type: string
            default: SNAPSHOT
            enum:
              - SNAPSHOT
              - IN_MEMORY
              - IN_MEMORY_WITH_DELETE
        - name: serverRequestBatchSize
          in: query
          description: Number of segments in a batch per server request
          schema:
            type: integer
            format: int32
            default: 500
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: string
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
