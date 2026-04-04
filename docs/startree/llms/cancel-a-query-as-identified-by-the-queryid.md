# Source: https://docs.startree.ai/api-reference/query/cancel-a-query-as-identified-by-the-queryid.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel a query as identified by the queryId

> No effect if no query exists for the given queryId on the requested broker. Query may continue to run for a short while after calling cancel as it's done in a non-blocking manner. The cancel method can be called multiple times.

## OpenAPI

````yaml delete /query/{brokerId}/{queryId}
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
  /query/{brokerId}/{queryId}:
    delete:
      tags:
        - Query
      summary: Cancel a query as identified by the queryId
      description: >-
        No effect if no query exists for the given queryId on the requested
        broker. Query may continue to run for a short while after calling cancel
        as it's done in a non-blocking manner. The cancel method can be called
        multiple times.
      operationId: cancelQuery
      parameters:
        - name: brokerId
          in: path
          description: Broker that's running the query
          required: true
          schema:
            type: string
        - name: queryId
          in: path
          description: QueryId as assigned by the broker
          required: true
          schema:
            type: integer
            format: int64
        - name: timeoutMs
          in: query
          description: Timeout for servers to respond the cancel request
          schema:
            type: integer
            format: int32
            default: 3000
        - name: verbose
          in: query
          description: Return verbose responses for troubleshooting
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Success
          content: {}
        '404':
          description: Query not found on the requested broker
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
