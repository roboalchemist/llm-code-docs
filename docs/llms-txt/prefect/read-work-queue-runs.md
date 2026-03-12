# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-queues/read-work-queue-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Work Queue Runs

> Get flow runs from the work queue.



## OpenAPI

````yaml post /work_queues/{id}/get_runs
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_queues/{id}/get_runs:
    post:
      tags:
        - Work Queues
      summary: Read Work Queue Runs
      description: Get flow runs from the work queue.
      operationId: read_work_queue_runs_work_queues__id__get_runs_post
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The work queue id
            title: Id
          description: The work queue id
        - name: x-prefect-ui
          in: header
          required: false
          schema:
            anyOf:
              - type: boolean
              - type: 'null'
            description: A header to indicate this request came from the Prefect UI.
            default: false
            title: X-Prefect-Ui
          description: A header to indicate this request came from the Prefect UI.
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
              $ref: >-
                #/components/schemas/Body_read_work_queue_runs_work_queues__id__get_runs_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/FlowRunResponse'
                title: Response Read Work Queue Runs Work Queues  Id  Get Runs Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_work_queue_runs_work_queues__id__get_runs_post:
      properties:
        scheduled_before:
          type: string
          format: date-time
          title: Scheduled Before
          description: Only flow runs scheduled to start before this time will be returned.
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_work_queue_runs_work_queues__id__get_runs_post
    FlowRunResponse:
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
          description: >-
            The name of the flow run. Defaults to a random slug if not
            specified.
          examples:
            - my-flow-run
        flow_id:
          type: string
          format: uuid
          title: Flow Id
          description: The id of the flow being run.
        state_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: State Id
          description: The id of the flow run's current state.
        deployment_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Deployment Id
          description: >-
            The id of the deployment associated with this flow run, if
            available.
        deployment_version:
          anyOf:
            - type: string
            - type: 'null'
          title: Deployment Version
          description: The version of the deployment associated with this flow run.
          examples:
            - '1.0'
        work_queue_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Work Queue Id
          description: The id of the run's work pool queue.
        work_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Work Queue Name
          description: The work queue that handled this flow run.
        flow_version:
          anyOf:
            - type: string
            - type: 'null'
          title: Flow Version
          description: The version of the flow executed in this flow run.
          examples:
            - '1.0'
        parameters:
          additionalProperties: true
          type: object
          title: Parameters
          description: Parameters for the flow run.
        idempotency_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Idempotency Key
          description: >-
            An optional idempotency key for the flow run. Used to ensure the
            same flow run is not created multiple times.
        context:
          additionalProperties: true
          type: object
          title: Context
          description: Additional context for the flow run.
          examples:
            - my_var: my_val
        empirical_policy:
          $ref: '#/components/schemas/FlowRunPolicy'
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of tags on the flow run
          examples:
            - - tag-1
              - tag-2
        labels:
          additionalProperties:
            anyOf:
              - type: boolean
              - type: integer
              - type: number
              - type: string
          type: object
          title: Labels
          description: >-
            A dictionary of key-value labels. Values can be strings, numbers, or
            booleans.
          examples:
            - key: value1
              key2: 42
        parent_task_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Parent Task Run Id
          description: >-
            If the flow run is a subflow, the id of the 'dummy' task in the
            parent flow used to track subflow state.
        state_type:
          anyOf:
            - $ref: '#/components/schemas/StateType'
            - type: 'null'
          description: The type of the current flow run state.
        state_name:
          anyOf:
            - type: string
            - type: 'null'
          title: State Name
          description: The name of the current flow run state.
        run_count:
          type: integer
          title: Run Count
          description: The number of times the flow run was executed.
          default: 0
        expected_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Expected Start Time
          description: The flow run's expected start time.
        next_scheduled_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Next Scheduled Start Time
          description: The next time the flow run is scheduled to start.
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
            Total run time. If the flow run was executed multiple times, the
            time of each run will be summed.
          default: 0
        estimated_run_time:
          type: number
          title: Estimated Run Time
          description: A real-time estimate of the total run time.
          default: 0
        estimated_start_time_delta:
          type: number
          title: Estimated Start Time Delta
          description: The difference between actual and expected start time.
          default: 0
        auto_scheduled:
          type: boolean
          title: Auto Scheduled
          description: Whether or not the flow run was automatically scheduled.
          default: false
        infrastructure_document_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Infrastructure Document Id
          description: The block document defining infrastructure to use this flow run.
        infrastructure_pid:
          anyOf:
            - type: string
            - type: 'null'
          title: Infrastructure Pid
          description: The id of the flow run as returned by an infrastructure block.
        created_by:
          anyOf:
            - $ref: '#/components/schemas/CreatedBy'
            - type: 'null'
          description: Optional information about the creator of this flow run.
        work_pool_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Work Pool Id
          description: The id of the flow run's work pool.
        work_pool_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Work Pool Name
          description: The name of the flow run's work pool.
          examples:
            - my-work-pool
        state:
          anyOf:
            - $ref: '#/components/schemas/State'
            - type: 'null'
          description: The current state of the flow run.
        job_variables:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Job Variables
          description: Variables used as overrides in the base job template
      type: object
      required:
        - flow_id
        - id
        - created
        - updated
      title: FlowRunResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    FlowRunPolicy:
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
            - type: 'null'
          title: Retry Delay
          description: The delay time between retries, in seconds.
        pause_keys:
          anyOf:
            - items:
                type: string
              type: array
              uniqueItems: true
            - type: 'null'
          title: Pause Keys
          description: Tracks pauses this run has observed.
        resuming:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Resuming
          description: Indicates if this run is resuming from a pause.
          default: false
        retry_type:
          anyOf:
            - type: string
              enum:
                - in_process
                - reschedule
            - type: 'null'
          title: Retry Type
          description: The type of retry this run is undergoing.
      type: object
      title: FlowRunPolicy
      description: Defines of how a flow run should retry.
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
    CreatedBy:
      properties:
        id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Id
          description: The id of the creator of the object.
        type:
          anyOf:
            - type: string
            - type: 'null'
          title: Type
          description: The type of the creator of the object.
        display_value:
          anyOf:
            - type: string
            - type: 'null'
          title: Display Value
          description: The display value for the creator.
      type: object
      title: CreatedBy
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