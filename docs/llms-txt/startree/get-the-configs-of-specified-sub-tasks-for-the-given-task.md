# Source: https://docs.startree.ai/api-reference/task/get-the-configs-of-specified-sub-tasks-for-the-given-task.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the configs of specified sub tasks for the given task

## OpenAPI

````yaml get /tasks/subtask/{taskName}/config
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
  /tasks/subtask/{taskName}/config:
    get:
      tags:
        - Task
      summary: Get the configs of specified sub tasks for the given task
      operationId: getSubtaskConfigs
      parameters:
        - name: taskName
          in: path
          description: Task name
          required: true
          schema:
            type: string
        - name: subtaskNames
          in: query
          description: Sub task names separated by comma
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
                  $ref: '#/components/schemas/PinotTaskConfig'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    PinotTaskConfig:
      type: object
      properties:
        taskType:
          type: string
        taskId:
          type: string
        configs:
          type: object
          additionalProperties:
            type: string
        tableName:
          type: string
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
