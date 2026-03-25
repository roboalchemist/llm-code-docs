# Source: https://docs.startree.ai/api-reference/table/cancel-all-rebalance-jobs-for-the-given-table-and-noop-if-no-rebalance-is-running.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel all rebalance jobs for the given table, and noop if no rebalance is running

> Cancel all rebalance jobs for the given table, and noop if no rebalance is running

## OpenAPI

````yaml delete /tables/{tableName}/rebalance
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
    delete:
      tags:
        - Table
      summary: >-
        Cancel all rebalance jobs for the given table, and noop if no rebalance
        is running
      description: >-
        Cancel all rebalance jobs for the given table, and noop if no rebalance
        is running
      operationId: cancelRebalance
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
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: array
                items:
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
