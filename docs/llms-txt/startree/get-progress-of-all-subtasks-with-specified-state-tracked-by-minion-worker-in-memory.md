# Source: https://docs.startree.ai/api-reference/task/get-progress-of-all-subtasks-with-specified-state-tracked-by-minion-worker-in-memory.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get progress of all subtasks with specified state tracked by minion worker in memory

## OpenAPI

````yaml get /tasks/subtask/workers/progress
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
  /tasks/subtask/workers/progress:
    get:
      tags:
        - Task
      summary: >-
        Get progress of all subtasks with specified state tracked by minion
        worker in memory
      operationId: getSubtaskOnWorkerProgress
      parameters:
        - name: subTaskState
          in: query
          description: Subtask state (UNKNOWN,IN_PROGRESS,SUCCEEDED,CANCELLED,ERROR)
          required: true
          schema:
            type: string
        - name: minionWorkerIds
          in: query
          description: Minion worker IDs separated by comma
          schema:
            type: string
      responses:
        '200':
          description: Success
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
