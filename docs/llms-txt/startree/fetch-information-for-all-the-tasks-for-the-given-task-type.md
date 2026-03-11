# Source: https://docs.startree.ai/api-reference/task/fetch-information-for-all-the-tasks-for-the-given-task-type.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch information for all the tasks for the given task type

## OpenAPI

````yaml get /tasks/{taskType}/debug
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
  /tasks/{taskType}/debug:
    get:
      tags:
        - Task
      summary: Fetch information for all the tasks for the given task type
      operationId: getTasksDebugInfo
      parameters:
        - name: taskType
          in: path
          description: Task type
          required: true
          schema:
            type: string
        - name: verbosity
          in: query
          description: >-
            verbosity (Prints information for all the tasks for the given task
            type.By default, only prints subtask details for running and error
            tasks. Value of > 0 prints subtask details for all tasks)
          schema:
            type: integer
            format: int32
            default: 0
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  $ref: '#/components/schemas/TaskDebugInfo'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    TaskDebugInfo:
      type: object
      properties:
        taskState:
          type: string
          enum:
            - NOT_STARTED
            - IN_PROGRESS
            - STOPPED
            - STOPPING
            - FAILED
            - COMPLETED
            - ABORTED
            - TIMED_OUT
            - TIMING_OUT
            - FAILING
        subtaskCount:
          $ref: '#/components/schemas/TaskCount'
        startTime:
          type: string
        executionStartTime:
          type: string
        finishTime:
          type: string
        triggeredBy:
          type: string
        subtaskInfos:
          type: array
          items:
            $ref: '#/components/schemas/SubtaskDebugInfo'
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
    SubtaskDebugInfo:
      type: object
      properties:
        taskId:
          type: string
        state:
          type: string
          enum:
            - INIT
            - RUNNING
            - STOPPED
            - COMPLETED
            - TIMED_OUT
            - TASK_ERROR
            - TASK_ABORTED
            - ERROR
            - DROPPED
        startTime:
          type: string
        finishTime:
          type: string
        participant:
          type: string
        info:
          type: string
        triggeredBy:
          type: string
        taskConfig:
          $ref: '#/components/schemas/PinotTaskConfig'
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
