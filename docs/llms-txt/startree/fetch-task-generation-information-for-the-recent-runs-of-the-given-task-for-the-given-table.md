# Source: https://docs.startree.ai/api-reference/task/fetch-task-generation-information-for-the-recent-runs-of-the-given-task-for-the-given-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch task generation information for the recent runs of the given task for the given table

## OpenAPI

````yaml get /tasks/generator/{tableNameWithType}/{taskType}/debug
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
  /tasks/generator/{tableNameWithType}/{taskType}/debug:
    get:
      tags:
        - Task
      summary: >-
        Fetch task generation information for the recent runs of the given task
        for the given table
      operationId: getTaskGenerationDebugInto
      parameters:
        - name: taskType
          in: path
          description: Task type
          required: true
          schema:
            type: string
        - name: tableNameWithType
          in: path
          description: Table name with type
          required: true
          schema:
            type: string
        - name: localOnly
          in: query
          description: Whether to only lookup local cache for logs
          schema:
            type: boolean
            default: false
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
