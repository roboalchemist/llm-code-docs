# Source: https://docs.startree.ai/api-reference/task/execute-a-task-on-minion.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute a task on minion

## OpenAPI

````yaml post /tasks/execute
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
  /tasks/execute:
    post:
      tags:
        - Task
      summary: Execute a task on minion
      operationId: executeAdhocTask
      requestBody:
        content:
          '*/*':
            schema:
              $ref: '#/components/schemas/AdhocTaskConfig'
        required: false
      responses:
        default:
          description: successful operation
          content: {}
      security:
        - oauth: []
        - database: []
components:
  schemas:
    AdhocTaskConfig:
      required:
        - tableName
        - taskType
      type: object
      properties:
        taskType:
          type: string
          readOnly: true
        tableName:
          type: string
          readOnly: true
        taskName:
          type: string
          readOnly: true
        taskConfigs:
          type: object
          additionalProperties:
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
