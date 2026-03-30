# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/task-runs/read-task-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Task Run

> Get a task run by id.



## OpenAPI

````yaml get /task_runs/{id}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /task_runs/{id}:
    get:
      tags:
        - Task Runs
      summary: Read Task Run
      description: Get a task run by id.
      operationId: read_task_run_task_runs__id__get
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The task run id
            title: Id
          description: The task run id
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskRun'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    TaskRun:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
        name:
          type: string
          title: Name
          examples:
            - my-task-run
        flow_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Flow Run Id
          description: The flow run id of the task run.
        task_key:
          type: string
          title: Task Key
          description: A unique identifier for the task being run.
        dynamic_key:
          type: string
          title: Dynamic Key
          description: >-
            A dynamic key used to differentiate between multiple runs of the
            same task within the same flow run.
        cache_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Cache Key
          description: >-
            An optional cache key. If a COMPLETED state associated with this
            cache key is found, the cached COMPLETED state will be used instead
            of executing the task run.
        cache_expiration:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Cache Expiration
          description: Specifies when the cached state should expire.
        task_version:
          anyOf:
            - type: string
            - type: 'null'
          title: Task Version
          description: The version of the task being run.
        empirical_policy:
          $ref: '#/components/schemas/TaskRunPolicy'
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of tags for the task run.
          examples:
            - - tag-1
              - tag-2
        labels:
          anyOf:
            - additionalProperties:
                anyOf:
                  - type: boolean
                  - type: integer
                  - type: number
                  - type: string
              type: object
            - type: 'null'
          title: Labels
          description: >-
            A dictionary of key-value labels. Values can be strings, numbers, or
            booleans.
          examples:
            - key: value1
              key2: 42
        state_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: State Id
          description: The id of the current task run state.
        task_inputs:
          additionalProperties:
            items:
              anyOf:
                - $ref: '#/components/schemas/TaskRunResult'
                - $ref: '#/components/schemas/FlowRunResult'
                - $ref: '#/components/schemas/Parameter'
                - $ref: '#/components/schemas/Constant'
            type: array
          type: object
          title: Task Inputs
          description: >-
            Tracks the source of inputs to a task run. Used for internal
            bookkeeping.
        state_type:
          anyOf:
            - $ref: '#/components/schemas/StateType'
            - type: 'null'
          description: The type of the current task run state.
        state_name:
          anyOf:
            - type: string
            - type: 'null'
          title: State Name
          description: The name of the current task run state.
        run_count:
          type: integer
          title: Run Count
          description: The number of times the task run has been executed.
          default: 0
        flow_run_run_count:
          type: integer
          title: Flow Run Run Count
          description: >-
            If the parent flow has retried, this indicates the flow retry this
            run is associated with.
          default: 0
        expected_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Expected Start Time
          description: The task run's expected start time.
        next_scheduled_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Next Scheduled Start Time
          description: The next time the task run is scheduled to start.
        start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Start Time
          description: The actual start time.
        end_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: End Time
          description: The actual end time.
        total_run_time:
          type: number
          title: Total Run Time
          description: >-
            Total run time. If the task run was executed multiple times, the
            time of each run will be summed.
          default: 0
        estimated_run_time:
          type: number
          title: Estimated Run Time
          description: A real-time estimate of total run time.
          default: 0
        estimated_start_time_delta:
          type: number
          title: Estimated Start Time Delta
          description: The difference between actual and expected start time.
          default: 0
        state:
          anyOf:
            - $ref: '#/components/schemas/State'
            - type: 'null'
          description: The current task run state.
      type: object
      required:
        - task_key
        - dynamic_key
        - id
        - created
        - updated
      title: TaskRun
      description: An ORM representation of task run data.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    TaskRunPolicy:
      properties:
        max_retries:
          type: integer
          title: Max Retries
          description: >-
            The maximum number of retries. Field is not used. Please use
            `retries` instead.
          default: 0
          deprecated: true
        retry_delay_seconds:
          type: number
          title: Retry Delay Seconds
          description: >-
            The delay between retries. Field is not used. Please use
            `retry_delay` instead.
          default: 0
          deprecated: true
        retries:
          anyOf:
            - type: integer
            - type: 'null'
          title: Retries
          description: The number of retries.
        retry_delay:
          anyOf:
            - type: integer
            - type: number
            - items:
                type: integer
              type: array
            - items:
                type: number
              type: array
            - type: 'null'
          title: Retry Delay
          description: A delay time or list of delay times between retries, in seconds.
        retry_jitter_factor:
          anyOf:
            - type: number
            - type: 'null'
          title: Retry Jitter Factor
          description: Determines the amount a retry should jitter
      type: object
      title: TaskRunPolicy
      description: Defines of how a task run should retry.
    TaskRunResult:
      properties:
        input_type:
          type: string
          const: task_run
          title: Input Type
          default: task_run
        id:
          type: string
          format: uuid
          title: Id
      type: object
      required:
        - id
      title: TaskRunResult
      description: Represents a task run result input to another task run.
    FlowRunResult:
      properties:
        input_type:
          type: string
          const: flow_run
          title: Input Type
          default: flow_run
        id:
          type: string
          format: uuid
          title: Id
      type: object
      required:
        - id
      title: FlowRunResult
    Parameter:
      properties:
        input_type:
          type: string
          const: parameter
          title: Input Type
          default: parameter
        name:
          type: string
          title: Name
      type: object
      required:
        - name
      title: Parameter
      description: Represents a parameter input to a task run.
    Constant:
      properties:
        input_type:
          type: string
          const: constant
          title: Input Type
          default: constant
        type:
          type: string
          title: Type
      type: object
      required:
        - type
      title: Constant
      description: Represents constant input value to a task run.
    StateType:
      type: string
      enum:
        - SCHEDULED
        - PENDING
        - RUNNING
        - COMPLETED
        - FAILED
        - CANCELLED
        - CRASHED
        - PAUSED
        - CANCELLING
      title: StateType
      description: Enumeration of state types.
    State:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        type:
          $ref: '#/components/schemas/StateType'
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        timestamp:
          type: string
          format: date-time
          title: Timestamp
        message:
          anyOf:
            - type: string
            - type: 'null'
          title: Message
          examples:
            - Run started
        data:
          anyOf:
            - {}
            - type: 'null'
          title: Data
          description: >-
            Data associated with the state, e.g. a result. Content must be
            storable as JSON.
        state_details:
          $ref: '#/components/schemas/StateDetails'
      type: object
      required:
        - type
        - id
      title: State
      description: Represents the state of a run.
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    StateDetails:
      properties:
        flow_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Flow Run Id
        task_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Task Run Id
        child_flow_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Child Flow Run Id
        scheduled_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Scheduled Time
        cache_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Cache Key
        cache_expiration:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Cache Expiration
        deferred:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Deferred
          default: false
        untrackable_result:
          type: boolean
          title: Untrackable Result
          default: false
        pause_timeout:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Pause Timeout
        pause_reschedule:
          type: boolean
          title: Pause Reschedule
          default: false
        pause_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Pause Key
        run_input_keyset:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Run Input Keyset
        refresh_cache:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Refresh Cache
        retriable:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Retriable
        transition_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Transition Id
        task_parameters_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Task Parameters Id
        traceparent:
          anyOf:
            - type: string
            - type: 'null'
          title: Traceparent
        deployment_concurrency_lease_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Deployment Concurrency Lease Id
      type: object
      title: StateDetails

````

Built with [Mintlify](https://mintlify.com).