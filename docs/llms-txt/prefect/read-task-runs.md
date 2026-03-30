# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/task-runs/read-task-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Task Runs

> Query for task runs.



## OpenAPI

````yaml post /task_runs/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /task_runs/filter:
    post:
      tags:
        - Task Runs
      summary: Read Task Runs
      description: Query for task runs.
      operationId: read_task_runs_task_runs_filter_post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_read_task_runs_task_runs_filter_post'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/TaskRun'
                title: Response Read Task Runs Task Runs Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_task_runs_task_runs_filter_post:
      properties:
        sort:
          $ref: '#/components/schemas/TaskRunSort'
          default: ID_DESC
        offset:
          type: integer
          minimum: 0
          title: Offset
          default: 0
        flows:
          anyOf:
            - $ref: '#/components/schemas/FlowFilter'
            - type: 'null'
        flow_runs:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilter'
            - type: 'null'
        task_runs:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilter'
            - type: 'null'
        deployments:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilter'
            - type: 'null'
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_task_runs_task_runs_filter_post
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
    TaskRunSort:
      type: string
      enum:
        - ID_DESC
        - EXPECTED_START_TIME_ASC
        - EXPECTED_START_TIME_DESC
        - NAME_ASC
        - NAME_DESC
        - NEXT_SCHEDULED_START_TIME_ASC
        - END_TIME_DESC
      title: TaskRunSort
      description: Defines task run sorting options.
    FlowFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/FlowFilterId'
            - type: 'null'
          description: Filter criteria for `Flow.id`
        deployment:
          anyOf:
            - $ref: '#/components/schemas/FlowFilterDeployment'
            - type: 'null'
          description: Filter criteria for Flow deployments
        name:
          anyOf:
            - $ref: '#/components/schemas/FlowFilterName'
            - type: 'null'
          description: Filter criteria for `Flow.name`
        tags:
          anyOf:
            - $ref: '#/components/schemas/FlowFilterTags'
            - type: 'null'
          description: Filter criteria for `Flow.tags`
      additionalProperties: false
      type: object
      title: FlowFilter
      description: Filter for flows. Only flows matching all criteria will be returned.
    FlowRunFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterId'
            - type: 'null'
          description: Filter criteria for `FlowRun.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterName'
            - type: 'null'
          description: Filter criteria for `FlowRun.name`
        tags:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterTags'
            - type: 'null'
          description: Filter criteria for `FlowRun.tags`
        deployment_id:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterDeploymentId'
            - type: 'null'
          description: Filter criteria for `FlowRun.deployment_id`
        work_queue_name:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterWorkQueueName'
            - type: 'null'
          description: Filter criteria for `FlowRun.work_queue_name
        state:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterState'
            - type: 'null'
          description: Filter criteria for `FlowRun.state`
        flow_version:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterFlowVersion'
            - type: 'null'
          description: Filter criteria for `FlowRun.flow_version`
        start_time:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterStartTime'
            - type: 'null'
          description: Filter criteria for `FlowRun.start_time`
        end_time:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterEndTime'
            - type: 'null'
          description: Filter criteria for `FlowRun.end_time`
        expected_start_time:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterExpectedStartTime'
            - type: 'null'
          description: Filter criteria for `FlowRun.expected_start_time`
        next_scheduled_start_time:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterNextScheduledStartTime'
            - type: 'null'
          description: Filter criteria for `FlowRun.next_scheduled_start_time`
        parent_flow_run_id:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterParentFlowRunId'
            - type: 'null'
          description: Filter criteria for subflows of the given flow runs
        parent_task_run_id:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterParentTaskRunId'
            - type: 'null'
          description: Filter criteria for `FlowRun.parent_task_run_id`
        idempotency_key:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterIdempotencyKey'
            - type: 'null'
          description: Filter criteria for `FlowRun.idempotency_key`
        created_by:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterCreatedBy'
            - type: 'null'
          description: Filter criteria for `FlowRun.created_by`
      additionalProperties: false
      type: object
      title: FlowRunFilter
      description: Filter flow runs. Only flow runs matching all criteria will be returned
    TaskRunFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterId'
            - type: 'null'
          description: Filter criteria for `TaskRun.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterName'
            - type: 'null'
          description: Filter criteria for `TaskRun.name`
        tags:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterTags'
            - type: 'null'
          description: Filter criteria for `TaskRun.tags`
        state:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterState'
            - type: 'null'
          description: Filter criteria for `TaskRun.state`
        start_time:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterStartTime'
            - type: 'null'
          description: Filter criteria for `TaskRun.start_time`
        expected_start_time:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterExpectedStartTime'
            - type: 'null'
          description: Filter criteria for `TaskRun.expected_start_time`
        subflow_runs:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterSubFlowRuns'
            - type: 'null'
          description: Filter criteria for `TaskRun.subflow_run`
        flow_run_id:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterFlowRunId'
            - type: 'null'
          description: Filter criteria for `TaskRun.flow_run_id`
      additionalProperties: false
      type: object
      title: TaskRunFilter
      description: Filter task runs. Only task runs matching all criteria will be returned
    DeploymentFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterId'
            - type: 'null'
          description: Filter criteria for `Deployment.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterName'
            - type: 'null'
          description: Filter criteria for `Deployment.name`
        flow_or_deployment_name:
          anyOf:
            - $ref: '#/components/schemas/DeploymentOrFlowNameFilter'
            - type: 'null'
          description: Filter criteria for `Deployment.name` or `Flow.name`
        paused:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterPaused'
            - type: 'null'
          description: Filter criteria for `Deployment.paused`
        tags:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterTags'
            - type: 'null'
          description: Filter criteria for `Deployment.tags`
        work_queue_name:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterWorkQueueName'
            - type: 'null'
          description: Filter criteria for `Deployment.work_queue_name`
        concurrency_limit:
          anyOf:
            - $ref: '#/components/schemas/DeploymentFilterConcurrencyLimit'
            - type: 'null'
          description: >-
            DEPRECATED: Prefer `Deployment.concurrency_limit_id` over
            `Deployment.concurrency_limit`. If provided, will be ignored for
            backwards-compatibility. Will be removed after December 2024.
          deprecated: true
      additionalProperties: false
      type: object
      title: DeploymentFilter
      description: >-
        Filter for deployments. Only deployments matching all criteria will be
        returned.
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
    Operator:
      type: string
      enum:
        - and_
        - or_
      title: Operator
      description: Operators for combining filter criteria.
    FlowFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of flow ids to include
        not_any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Not Any
          description: A list of flow ids to exclude
      additionalProperties: false
      type: object
      title: FlowFilterId
      description: Filter by `Flow.id`.
    FlowFilterDeployment:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flows without deployments
      additionalProperties: false
      type: object
      title: FlowFilterDeployment
      description: Filter by flows by deployment
    FlowFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of flow names to include
          examples:
            - - my-flow-1
              - my-flow-2
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A case-insensitive partial match. For example,  passing 'marvin'
            will match 'marvin', 'sad-Marvin', and 'marvin-robot'.
          examples:
            - marvin
      additionalProperties: false
      type: object
      title: FlowFilterName
      description: Filter by `Flow.name`.
    FlowFilterTags:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        all_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: All
          description: >-
            A list of tags. Flows will be returned only if their tags are a
            superset of the list
          examples:
            - - tag-1
              - tag-2
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flows without tags
      additionalProperties: false
      type: object
      title: FlowFilterTags
      description: Filter by `Flow.tags`.
    FlowRunFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run ids to include
        not_any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Not Any
          description: A list of flow run ids to exclude
      additionalProperties: false
      type: object
      title: FlowRunFilterId
      description: Filter by `FlowRun.id`.
    FlowRunFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run names to include
          examples:
            - - my-flow-run-1
              - my-flow-run-2
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A case-insensitive partial match. For example,  passing 'marvin'
            will match 'marvin', 'sad-Marvin', and 'marvin-robot'.
          examples:
            - marvin
      additionalProperties: false
      type: object
      title: FlowRunFilterName
      description: Filter by `FlowRun.name`.
    FlowRunFilterTags:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        all_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: All
          description: >-
            A list of tags. Flow runs will be returned only if their tags are a
            superset of the list
          examples:
            - - tag-1
              - tag-2
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of tags to include
          examples:
            - - tag-1
              - tag-2
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flow runs without tags
      additionalProperties: false
      type: object
      title: FlowRunFilterTags
      description: Filter by `FlowRun.tags`.
    FlowRunFilterDeploymentId:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run deployment ids to include
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flow runs without deployment ids
      additionalProperties: false
      type: object
      title: FlowRunFilterDeploymentId
      description: Filter by `FlowRun.deployment_id`.
    FlowRunFilterWorkQueueName:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work queue names to include
          examples:
            - - work_queue_1
              - work_queue_2
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flow runs without work queue names
      additionalProperties: false
      type: object
      title: FlowRunFilterWorkQueueName
      description: Filter by `FlowRun.work_queue_name`.
    FlowRunFilterState:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        type:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterStateType'
            - type: 'null'
          description: Filter criteria for `FlowRun.state_type`
        name:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilterStateName'
            - type: 'null'
          description: Filter criteria for `FlowRun.state_name`
      additionalProperties: false
      type: object
      title: FlowRunFilterState
      description: Filter by `FlowRun.state_type` and `FlowRun.state_name`.
    FlowRunFilterFlowVersion:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run flow_versions to include
      additionalProperties: false
      type: object
      title: FlowRunFilterFlowVersion
      description: Filter by `FlowRun.flow_version`.
    FlowRunFilterStartTime:
      properties:
        before_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before
          description: Only include flow runs starting at or before this time
        after_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After
          description: Only include flow runs starting at or after this time
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only return flow runs without a start time
      additionalProperties: false
      type: object
      title: FlowRunFilterStartTime
      description: Filter by `FlowRun.start_time`.
    FlowRunFilterEndTime:
      properties:
        before_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before
          description: Only include flow runs ending at or before this time
        after_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After
          description: Only include flow runs ending at or after this time
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only return flow runs without an end time
      additionalProperties: false
      type: object
      title: FlowRunFilterEndTime
      description: Filter by `FlowRun.end_time`.
    FlowRunFilterExpectedStartTime:
      properties:
        before_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before
          description: Only include flow runs scheduled to start at or before this time
        after_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After
          description: Only include flow runs scheduled to start at or after this time
      additionalProperties: false
      type: object
      title: FlowRunFilterExpectedStartTime
      description: Filter by `FlowRun.expected_start_time`.
    FlowRunFilterNextScheduledStartTime:
      properties:
        before_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before
          description: >-
            Only include flow runs with a next_scheduled_start_time or before
            this time
        after_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After
          description: >-
            Only include flow runs with a next_scheduled_start_time at or after
            this time
      additionalProperties: false
      type: object
      title: FlowRunFilterNextScheduledStartTime
      description: Filter by `FlowRun.next_scheduled_start_time`.
    FlowRunFilterParentFlowRunId:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of parent flow run ids to include
      additionalProperties: false
      type: object
      title: FlowRunFilterParentFlowRunId
      description: Filter for subflows of a given flow run
    FlowRunFilterParentTaskRunId:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run parent_task_run_ids to include
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flow runs without parent_task_run_id
      additionalProperties: false
      type: object
      title: FlowRunFilterParentTaskRunId
      description: Filter by `FlowRun.parent_task_run_id`.
    FlowRunFilterIdempotencyKey:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run idempotency keys to include
        not_any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Not Any
          description: A list of flow run idempotency keys to exclude
      additionalProperties: false
      type: object
      title: FlowRunFilterIdempotencyKey
      description: Filter by FlowRun.idempotency_key.
    FlowRunFilterCreatedBy:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Id
          description: A list of creator IDs to include
        type_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Type
          description: >-
            A list of creator types to include. For example, 'DEPLOYMENT' for
            scheduled runs or 'AUTOMATION' for runs triggered by automations.
          examples:
            - - DEPLOYMENT
              - AUTOMATION
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include flow runs without a creator
      additionalProperties: false
      type: object
      title: FlowRunFilterCreatedBy
      description: Filter by `FlowRun.created_by`.
    TaskRunFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of task run ids to include
      additionalProperties: false
      type: object
      title: TaskRunFilterId
      description: Filter by `TaskRun.id`.
    TaskRunFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of task run names to include
          examples:
            - - my-task-run-1
              - my-task-run-2
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A case-insensitive partial match. For example,  passing 'marvin'
            will match 'marvin', 'sad-Marvin', and 'marvin-robot'.
          examples:
            - marvin
      additionalProperties: false
      type: object
      title: TaskRunFilterName
      description: Filter by `TaskRun.name`.
    TaskRunFilterTags:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        all_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: All
          description: >-
            A list of tags. Task runs will be returned only if their tags are a
            superset of the list
          examples:
            - - tag-1
              - tag-2
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include task runs without tags
      additionalProperties: false
      type: object
      title: TaskRunFilterTags
      description: Filter by `TaskRun.tags`.
    TaskRunFilterState:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        type:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterStateType'
            - type: 'null'
          description: Filter criteria for `TaskRun.state_type`
        name:
          anyOf:
            - $ref: '#/components/schemas/TaskRunFilterStateName'
            - type: 'null'
          description: Filter criteria for `TaskRun.state_name`
      additionalProperties: false
      type: object
      title: TaskRunFilterState
      description: Filter by `TaskRun.type` and `TaskRun.name`.
    TaskRunFilterStartTime:
      properties:
        before_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before
          description: Only include task runs starting at or before this time
        after_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After
          description: Only include task runs starting at or after this time
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only return task runs without a start time
      additionalProperties: false
      type: object
      title: TaskRunFilterStartTime
      description: Filter by `TaskRun.start_time`.
    TaskRunFilterExpectedStartTime:
      properties:
        before_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before
          description: Only include task runs expected to start at or before this time
        after_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After
          description: Only include task runs expected to start at or after this time
      additionalProperties: false
      type: object
      title: TaskRunFilterExpectedStartTime
      description: Filter by `TaskRun.expected_start_time`.
    TaskRunFilterSubFlowRuns:
      properties:
        exists_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Exists
          description: >-
            If true, only include task runs that are subflow run parents; if
            false, exclude parent task runs
      additionalProperties: false
      type: object
      title: TaskRunFilterSubFlowRuns
      description: Filter by `TaskRun.subflow_run`.
    TaskRunFilterFlowRunId:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of task run flow run ids to include
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: Filter for task runs with None as their flow run id
          default: false
      additionalProperties: false
      type: object
      title: TaskRunFilterFlowRunId
      description: Filter by `TaskRun.flow_run_id`.
    DeploymentFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of deployment ids to include
        not_any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Not Any
          description: A list of deployment ids to exclude
      additionalProperties: false
      type: object
      title: DeploymentFilterId
      description: Filter by `Deployment.id`.
    DeploymentFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of deployment names to include
          examples:
            - - my-deployment-1
              - my-deployment-2
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A case-insensitive partial match. For example,  passing 'marvin'
            will match 'marvin', 'sad-Marvin', and 'marvin-robot'.
          examples:
            - marvin
      additionalProperties: false
      type: object
      title: DeploymentFilterName
      description: Filter by `Deployment.name`.
    DeploymentOrFlowNameFilter:
      properties:
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A case-insensitive partial match on deployment or flow names. For
            example, passing 'example' might match deployments or flows with
            'example' in their names.
      additionalProperties: false
      type: object
      title: DeploymentOrFlowNameFilter
      description: >-
        Filter by `Deployment.name` or `Flow.name` with a single input string
        for ilike filtering.
    DeploymentFilterPaused:
      properties:
        eq_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Eq
          description: Only returns where deployment is/is not paused
      additionalProperties: false
      type: object
      title: DeploymentFilterPaused
      description: Filter by `Deployment.paused`.
    DeploymentFilterTags:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        all_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: All
          description: >-
            A list of tags. Deployments will be returned only if their tags are
            a superset of the list
          examples:
            - - tag-1
              - tag-2
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of tags to include
          examples:
            - - tag-1
              - tag-2
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include deployments without tags
      additionalProperties: false
      type: object
      title: DeploymentFilterTags
      description: Filter by `Deployment.tags`.
    DeploymentFilterWorkQueueName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work queue names to include
          examples:
            - - work_queue_1
              - work_queue_2
      additionalProperties: false
      type: object
      title: DeploymentFilterWorkQueueName
      description: Filter by `Deployment.work_queue_name`.
    DeploymentFilterConcurrencyLimit:
      properties:
        ge_:
          anyOf:
            - type: integer
            - type: 'null'
          title: Ge
          description: >-
            Only include deployments with a concurrency limit greater than or
            equal to this value
        le_:
          anyOf:
            - type: integer
            - type: 'null'
          title: Le
          description: >-
            Only include deployments with a concurrency limit less than or equal
            to this value
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include deployments without a concurrency limit
      additionalProperties: false
      type: object
      title: DeploymentFilterConcurrencyLimit
      description: >-
        DEPRECATED: Prefer `Deployment.concurrency_limit_id` over
        `Deployment.concurrency_limit`.
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
    FlowRunFilterStateType:
      properties:
        any_:
          anyOf:
            - items:
                $ref: '#/components/schemas/StateType'
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run state types to include
        not_any_:
          anyOf:
            - items:
                $ref: '#/components/schemas/StateType'
              type: array
            - type: 'null'
          title: Not Any
          description: A list of flow run state types to exclude
      additionalProperties: false
      type: object
      title: FlowRunFilterStateType
      description: Filter by `FlowRun.state_type`.
    FlowRunFilterStateName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run state names to include
        not_any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Not Any
          description: A list of flow run state names to exclude
      additionalProperties: false
      type: object
      title: FlowRunFilterStateName
      description: Filter by `FlowRun.state_name`.
    TaskRunFilterStateType:
      properties:
        any_:
          anyOf:
            - items:
                $ref: '#/components/schemas/StateType'
              type: array
            - type: 'null'
          title: Any
          description: A list of task run state types to include
      additionalProperties: false
      type: object
      title: TaskRunFilterStateType
      description: Filter by `TaskRun.state_type`.
    TaskRunFilterStateName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of task run state names to include
      additionalProperties: false
      type: object
      title: TaskRunFilterStateName
      description: Filter by `TaskRun.state_name`.

````

Built with [Mintlify](https://mintlify.com).