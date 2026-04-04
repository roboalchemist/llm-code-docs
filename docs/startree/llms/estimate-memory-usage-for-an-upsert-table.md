# Source: https://docs.startree.ai/api-reference/upsert/estimate-memory-usage-for-an-upsert-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Estimate memory usage for an upsert table

> This API returns the estimated heap usage based on primary key column stats. This allows us to estimate table size before onboarding.

## OpenAPI

````yaml post /upsert/estimateHeapUsage
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
  /upsert/estimateHeapUsage:
    post:
      tags:
        - Upsert
      summary: Estimate memory usage for an upsert table
      description: >-
        This API returns the estimated heap usage based on primary key column
        stats. This allows us to estimate table size before onboarding.
      operationId: estimateHeapUsage
      parameters:
        - name: cardinality
          in: query
          description: cardinality
          required: true
          schema:
            type: integer
            format: int64
        - name: primaryKeySize
          in: query
          description: primaryKeySize
          schema:
            type: integer
            format: int32
            default: -1
        - name: numPartitions
          in: query
          description: numPartitions
          schema:
            type: integer
            format: int32
            default: -1
      requestBody:
        content:
          application/json:
            schema:
              type: string
        required: false
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
