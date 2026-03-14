# Source: https://docs.startree.ai/api-reference/table/force-commit-the-current-consuming-segments.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Force commit the current consuming segments

> Force commit the current segments in consuming state and restart consumption. This should be used after schema/table config changes. Please note that this is an asynchronous operation, and 200 response does not mean it has actually been done already.If specific partitions or consuming segments are provided, only those partitions or consuming segments will be force committed.

## OpenAPI

````yaml post /tables/{tableName}/forceCommit
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
  /tables/{tableName}/forceCommit:
    post:
      tags:
        - Table
      summary: Force commit the current consuming segments
      description: >-
        Force commit the current segments in consuming state and restart
        consumption. This should be used after schema/table config changes.
        Please note that this is an asynchronous operation, and 200 response
        does not mean it has actually been done already.If specific partitions
        or consuming segments are provided, only those partitions or consuming
        segments will be force committed.
      operationId: forceCommit
      parameters:
        - name: tableName
          in: path
          description: Name of the table
          required: true
          schema:
            type: string
        - name: partitions
          in: query
          description: Comma separated list of partition group IDs to be committed
          schema:
            type: string
        - name: segments
          in: query
          description: Comma separated list of consuming segments to be committed
          schema:
            type: string
        - name: batchSize
          in: query
          description: >-
            Max number of consuming segments to commit at once (default =
            Integer.MAX_VALUE)
          schema:
            type: integer
            format: int32
            default: 2147483647
        - name: batchStatusCheckIntervalSec
          in: query
          description: >-
            How often to check whether the current batch of segments have been
            successfully committed or not (default = 5)
          schema:
            type: integer
            format: int32
            default: 5
        - name: batchStatusCheckTimeoutSec
          in: query
          description: >-
            Timeout based on which the controller will stop checking the
            forceCommit status of the batch of segments and throw an exception.
            (default = 180)
          schema:
            type: integer
            format: int32
            default: 180
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
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
