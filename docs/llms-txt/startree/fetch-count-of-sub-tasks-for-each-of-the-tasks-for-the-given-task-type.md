# Source: https://docs.startree.ai/api-reference/task/fetch-count-of-sub-tasks-for-each-of-the-tasks-for-the-given-task-type.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch count of sub-tasks for each of the tasks for the given task type

## OpenAPI

````yaml get /tasks/{taskType}/taskcounts
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
  /tasks/{taskType}/taskcounts:
    get:
      tags:
        - Task
      summary: Fetch count of sub-tasks for each of the tasks for the given task type
      operationId: getTaskCounts
      parameters:
        - name: taskType
          in: path
          description: Task type
          required: true
          schema:
            type: string
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  $ref: '#/components/schemas/TaskCount'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    TaskCount:
      type: object
      properties:
        total:
          type: integer
          format: int32
        completed:
          type: integer
          format: int32
        running:
          type: integer
          format: int32
        waiting:
          type: integer
          format: int32
        error:
          type: integer
          format: int32
        unknown:
          type: integer
          format: int32
        dropped:
          type: integer
          format: int32
        timedOut:
          type: integer
          format: int32
        aborted:
          type: integer
          format: int32
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
