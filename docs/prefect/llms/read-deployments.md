# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/deployments/read-deployments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Deployments

> Query for deployments.



## OpenAPI

````yaml post /deployments/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /deployments/filter:
    post:
      tags:
        - Deployments
      summary: Read Deployments
      description: Query for deployments.
      operationId: read_deployments_deployments_filter_post
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
              $ref: >-
                #/components/schemas/Body_read_deployments_deployments_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/DeploymentResponse'
                title: Response Read Deployments Deployments Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_deployments_deployments_filter_post:
      properties:
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
        work_pools:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilter'
            - type: 'null'
        work_pool_queues:
          anyOf:
            - $ref: '#/components/schemas/WorkQueueFilter'
            - type: 'null'
        sort:
          $ref: '#/components/schemas/DeploymentSort'
          default: NAME_ASC
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_deployments_deployments_filter_post
    DeploymentResponse:
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
          description: The name of the deployment.
        version:
          anyOf:
            - type: string
            - type: 'null'
          title: Version
          description: An optional version for the deployment.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A description for the deployment.
        flow_id:
          type: string
          format: uuid
          title: Flow Id
          description: The flow id associated with the deployment.
        paused:
          type: boolean
          title: Paused
          description: Whether or not the deployment is paused.
          default: false
        schedules:
          items:
            $ref: '#/components/schemas/DeploymentSchedule'
          type: array
          title: Schedules
          description: A list of schedules for the deployment.
        concurrency_limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Concurrency Limit
          description: >-
            DEPRECATED: Prefer `global_concurrency_limit`. Will always be None
            for backwards compatibility. Will be removed after December 2024.
          deprecated: true
        global_concurrency_limit:
          anyOf:
            - $ref: '#/components/schemas/GlobalConcurrencyLimitResponse'
            - type: 'null'
          description: >-
            The global concurrency limit object for enforcing the maximum number
            of flow runs that can be active at once.
        concurrency_options:
          anyOf:
            - $ref: '#/components/schemas/ConcurrencyOptions'
            - type: 'null'
          description: The concurrency options for the deployment.
        job_variables:
          additionalProperties: true
          type: object
          title: Job Variables
          description: Overrides to apply to the base infrastructure block at runtime.
        parameters:
          additionalProperties: true
          type: object
          title: Parameters
          description: Parameters for flow runs scheduled by the deployment.
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of tags for the deployment
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
        work_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Work Queue Name
          description: >-
            The work queue for the deployment. If no work queue is set, work
            will not be scheduled.
        work_queue_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Work Queue Id
          description: The id of the work pool queue to which this deployment is assigned.
        last_polled:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Polled
          description: The last time the deployment was polled for status updates.
        parameter_openapi_schema:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          additionalProperties: true
          title: Parameter Openapi Schema
          description: The parameter schema of the flow, including defaults.
        path:
          anyOf:
            - type: string
            - type: 'null'
          title: Path
          description: >-
            The path to the working directory for the workflow, relative to
            remote storage or an absolute path.
        pull_steps:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Pull Steps
          description: Pull steps for cloning and running this deployment.
        entrypoint:
          anyOf:
            - type: string
            - type: 'null'
          title: Entrypoint
          description: The path to the entrypoint for the workflow, relative to the `path`.
        storage_document_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Storage Document Id
          description: The block document defining storage used for this flow.
        infrastructure_document_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Infrastructure Document Id
          description: The block document defining infrastructure to use for flow runs.
        created_by:
          anyOf:
            - $ref: '#/components/schemas/CreatedBy'
            - type: 'null'
          description: Optional information about the creator of this deployment.
        updated_by:
          anyOf:
            - $ref: '#/components/schemas/UpdatedBy'
            - type: 'null'
          description: Optional information about the updater of this deployment.
        work_pool_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Work Pool Name
          description: The name of the deployment's work pool.
        status:
          anyOf:
            - $ref: '#/components/schemas/DeploymentStatus'
            - type: 'null'
          description: Whether the deployment is ready to run flows.
          default: NOT_READY
        enforce_parameter_schema:
          type: boolean
          title: Enforce Parameter Schema
          description: Whether or not the deployment should enforce the parameter schema.
          default: true
      type: object
      required:
        - name
        - flow_id
        - id
        - created
        - updated
      title: DeploymentResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
    WorkPoolFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterId'
            - type: 'null'
          description: Filter criteria for `WorkPool.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterName'
            - type: 'null'
          description: Filter criteria for `WorkPool.name`
        type:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterType'
            - type: 'null'
          description: Filter criteria for `WorkPool.type`
      additionalProperties: false
      type: object
      title: WorkPoolFilter
      description: >-
        Filter work pools. Only work pools matching all criteria will be
        returned
    WorkQueueFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/WorkQueueFilterId'
            - type: 'null'
          description: Filter criteria for `WorkQueue.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/WorkQueueFilterName'
            - type: 'null'
          description: Filter criteria for `WorkQueue.name`
      additionalProperties: false
      type: object
      title: WorkQueueFilter
      description: |-
        Filter work queues. Only work queues matching all criteria will be
        returned
    DeploymentSort:
      type: string
      enum:
        - CREATED_DESC
        - UPDATED_DESC
        - NAME_ASC
        - NAME_DESC
      title: DeploymentSort
      description: Defines deployment sorting options.
    DeploymentSchedule:
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
        deployment_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Deployment Id
          description: The deployment id associated with this schedule.
        schedule:
          anyOf:
            - $ref: '#/components/schemas/IntervalSchedule'
            - $ref: '#/components/schemas/CronSchedule'
            - $ref: '#/components/schemas/RRuleSchedule'
          title: Schedule
          description: The schedule for the deployment.
        active:
          type: boolean
          title: Active
          description: Whether or not the schedule is active.
          default: true
        max_scheduled_runs:
          anyOf:
            - type: integer
              exclusiveMinimum: 0
            - type: 'null'
          title: Max Scheduled Runs
          description: The maximum number of scheduled runs for the schedule.
        parameters:
          additionalProperties: true
          type: object
          title: Parameters
          description: A dictionary of parameter value overrides.
        slug:
          anyOf:
            - type: string
            - type: 'null'
          title: Slug
          description: A unique slug for the schedule.
      type: object
      required:
        - schedule
        - id
        - created
        - updated
      title: DeploymentSchedule
    GlobalConcurrencyLimitResponse:
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
        active:
          type: boolean
          title: Active
          description: Whether the global concurrency limit is active.
          default: true
        name:
          type: string
          title: Name
          description: The name of the global concurrency limit.
        limit:
          type: integer
          title: Limit
          description: The concurrency limit.
        active_slots:
          type: integer
          title: Active Slots
          description: The number of active slots.
        slot_decay_per_second:
          type: number
          title: Slot Decay Per Second
          description: The decay rate for active slots when used as a rate limit.
          default: 2
      type: object
      required:
        - name
        - limit
        - active_slots
        - id
        - created
        - updated
      title: GlobalConcurrencyLimitResponse
      description: A response object for global concurrency limits.
    ConcurrencyOptions:
      properties:
        collision_strategy:
          $ref: '#/components/schemas/ConcurrencyLimitStrategy'
        grace_period_seconds:
          anyOf:
            - type: integer
              maximum: 86400
              minimum: 60
            - type: 'null'
          title: Grace Period Seconds
          description: >-
            Grace period in seconds for infrastructure to start before
            concurrency slots are revoked. If not set, falls back to server
            setting.
      type: object
      required:
        - collision_strategy
      title: ConcurrencyOptions
      description: Class for storing the concurrency config in database.
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
    UpdatedBy:
      properties:
        id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Id
          description: The id of the updater of the object.
        type:
          anyOf:
            - type: string
            - type: 'null'
          title: Type
          description: The type of the updater of the object.
        display_value:
          anyOf:
            - type: string
            - type: 'null'
          title: Display Value
          description: The display value for the updater.
      type: object
      title: UpdatedBy
    DeploymentStatus:
      type: string
      enum:
        - READY
        - NOT_READY
      title: DeploymentStatus
      description: Enumeration of deployment statuses.
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
    WorkPoolFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool ids to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterId
      description: Filter by `WorkPool.id`.
    WorkPoolFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool names to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterName
      description: Filter by `WorkPool.name`.
    WorkPoolFilterType:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool types to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterType
      description: Filter by `WorkPool.type`.
    WorkQueueFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of work queue ids to include
      additionalProperties: false
      type: object
      title: WorkQueueFilterId
      description: Filter by `WorkQueue.id`.
    WorkQueueFilterName:
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
            - - wq-1
              - wq-2
        startswith_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Startswith
          description: >-
            A list of case-insensitive starts-with matches. For example, 
            passing 'marvin' will match 'marvin', and 'Marvin-robot', but not
            'sad-marvin'.
          examples:
            - - marvin
              - Marvin-robot
      additionalProperties: false
      type: object
      title: WorkQueueFilterName
      description: Filter by `WorkQueue.name`.
    IntervalSchedule:
      properties:
        interval:
          type: number
          title: Interval
        anchor_date:
          type: string
          format: date-time
          title: Anchor Date
          examples:
            - '2020-01-01T00:00:00Z'
        timezone:
          anyOf:
            - type: string
            - type: 'null'
          title: Timezone
          examples:
            - America/New_York
      additionalProperties: false
      type: object
      required:
        - interval
      title: IntervalSchedule
      description: >-
        A schedule formed by adding `interval` increments to an `anchor_date`.
        If no

        `anchor_date` is supplied, the current UTC time is used.  If a

        timezone-naive datetime is provided for `anchor_date`, it is assumed to
        be

        in the schedule's timezone (or UTC). Even if supplied with an IANA
        timezone,

        anchor dates are always stored as UTC offsets, so a `timezone` can be

        provided to determine localization behaviors like DST boundary handling.
        If

        none is provided it will be inferred from the anchor date.


        NOTE: If the `IntervalSchedule` `anchor_date` or `timezone` is provided
        in a

        DST-observing timezone, then the schedule will adjust itself
        appropriately.

        Intervals greater than 24 hours will follow DST conventions, while
        intervals

        of less than 24 hours will follow UTC intervals. For example, an hourly

        schedule will fire every UTC hour, even across DST boundaries. When
        clocks

        are set back, this will result in two runs that *appear* to both be

        scheduled for 1am local time, even though they are an hour apart in UTC

        time. For longer intervals, like a daily schedule, the interval schedule

        will adjust for DST boundaries so that the clock-hour remains constant.
        This

        means that a daily schedule that always fires at 9am will observe DST
        and

        continue to fire at 9am in the local time zone.


        Args:
            interval (datetime.timedelta): an interval to schedule on.
            anchor_date (DateTime, optional): an anchor date to schedule increments against;
                if not provided, the current timestamp will be used.
            timezone (str, optional): a valid timezone string.
    CronSchedule:
      properties:
        cron:
          type: string
          title: Cron
          examples:
            - 0 0 * * *
        timezone:
          anyOf:
            - type: string
            - type: 'null'
          title: Timezone
          examples:
            - America/New_York
        day_or:
          type: boolean
          title: Day Or
          description: Control croniter behavior for handling day and day_of_week entries.
          default: true
      additionalProperties: false
      type: object
      required:
        - cron
      title: CronSchedule
      description: >-
        Cron schedule


        NOTE: If the timezone is a DST-observing one, then the schedule will
        adjust

        itself appropriately. Cron's rules for DST are based on schedule times,
        not

        intervals. This means that an hourly cron schedule will fire on every
        new

        schedule hour, not every elapsed hour; for example, when clocks are set
        back

        this will result in a two-hour pause as the schedule will fire *the
        first

        time* 1am is reached and *the first time* 2am is reached, 120 minutes
        later.

        Longer schedules, such as one that fires at 9am every morning, will

        automatically adjust for DST.


        Args:
            cron (str): a valid cron string
            timezone (str): a valid timezone string in IANA tzdata format (for example,
                America/New_York).
            day_or (bool, optional): Control how croniter handles `day` and `day_of_week`
                entries. Defaults to True, matching cron which connects those values using
                OR. If the switch is set to False, the values are connected using AND. This
                behaves like fcron and enables you to e.g. define a job that executes each
                2nd friday of a month by setting the days of month and the weekday.
    RRuleSchedule:
      properties:
        rrule:
          type: string
          title: Rrule
        timezone:
          anyOf:
            - type: string
              pattern: >-
                Africa/Abidjan|Africa/Accra|Africa/Addis_Ababa|Africa/Algiers|Africa/Asmara|Africa/Asmera|Africa/Bamako|Africa/Bangui|Africa/Banjul|Africa/Bissau|Africa/Blantyre|Africa/Brazzaville|Africa/Bujumbura|Africa/Cairo|Africa/Casablanca|Africa/Ceuta|Africa/Conakry|Africa/Dakar|Africa/Dar_es_Salaam|Africa/Djibouti|Africa/Douala|Africa/El_Aaiun|Africa/Freetown|Africa/Gaborone|Africa/Harare|Africa/Johannesburg|Africa/Juba|Africa/Kampala|Africa/Khartoum|Africa/Kigali|Africa/Kinshasa|Africa/Lagos|Africa/Libreville|Africa/Lome|Africa/Luanda|Africa/Lubumbashi|Africa/Lusaka|Africa/Malabo|Africa/Maputo|Africa/Maseru|Africa/Mbabane|Africa/Mogadishu|Africa/Monrovia|Africa/Nairobi|Africa/Ndjamena|Africa/Niamey|Africa/Nouakchott|Africa/Ouagadougou|Africa/Porto-Novo|Africa/Sao_Tome|Africa/Timbuktu|Africa/Tripoli|Africa/Tunis|Africa/Windhoek|America/Adak|America/Anchorage|America/Anguilla|America/Antigua|America/Araguaina|America/Argentina/Buenos_Aires|America/Argentina/Catamarca|America/Argentina/ComodRivadavia|America/Argentina/Cordoba|America/Argentina/Jujuy|America/Argentina/La_Rioja|America/Argentina/Mendoza|America/Argentina/Rio_Gallegos|America/Argentina/Salta|America/Argentina/San_Juan|America/Argentina/San_Luis|America/Argentina/Tucuman|America/Argentina/Ushuaia|America/Aruba|America/Asuncion|America/Atikokan|America/Atka|America/Bahia|America/Bahia_Banderas|America/Barbados|America/Belem|America/Belize|America/Blanc-Sablon|America/Boa_Vista|America/Bogota|America/Boise|America/Buenos_Aires|America/Cambridge_Bay|America/Campo_Grande|America/Cancun|America/Caracas|America/Catamarca|America/Cayenne|America/Cayman|America/Chicago|America/Chihuahua|America/Ciudad_Juarez|America/Coral_Harbour|America/Cordoba|America/Costa_Rica|America/Coyhaique|America/Creston|America/Cuiaba|America/Curacao|America/Danmarkshavn|America/Dawson|America/Dawson_Creek|America/Denver|America/Detroit|America/Dominica|America/Edmonton|America/Eirunepe|America/El_Salvador|America/Ensenada|America/Fort_Nelson|America/Fort_Wayne|America/Fortaleza|America/Glace_Bay|America/Godthab|America/Goose_Bay|America/Grand_Turk|America/Grenada|America/Guadeloupe|America/Guatemala|America/Guayaquil|America/Guyana|America/Halifax|America/Havana|America/Hermosillo|America/Indiana/Indianapolis|America/Indiana/Knox|America/Indiana/Marengo|America/Indiana/Petersburg|America/Indiana/Tell_City|America/Indiana/Vevay|America/Indiana/Vincennes|America/Indiana/Winamac|America/Indianapolis|America/Inuvik|America/Iqaluit|America/Jamaica|America/Jujuy|America/Juneau|America/Kentucky/Louisville|America/Kentucky/Monticello|America/Knox_IN|America/Kralendijk|America/La_Paz|America/Lima|America/Los_Angeles|America/Louisville|America/Lower_Princes|America/Maceio|America/Managua|America/Manaus|America/Marigot|America/Martinique|America/Matamoros|America/Mazatlan|America/Mendoza|America/Menominee|America/Merida|America/Metlakatla|America/Mexico_City|America/Miquelon|America/Moncton|America/Monterrey|America/Montevideo|America/Montreal|America/Montserrat|America/Nassau|America/New_York|America/Nipigon|America/Nome|America/Noronha|America/North_Dakota/Beulah|America/North_Dakota/Center|America/North_Dakota/New_Salem|America/Nuuk|America/Ojinaga|America/Panama|America/Pangnirtung|America/Paramaribo|America/Phoenix|America/Port-au-Prince|America/Port_of_Spain|America/Porto_Acre|America/Porto_Velho|America/Puerto_Rico|America/Punta_Arenas|America/Rainy_River|America/Rankin_Inlet|America/Recife|America/Regina|America/Resolute|America/Rio_Branco|America/Rosario|America/Santa_Isabel|America/Santarem|America/Santiago|America/Santo_Domingo|America/Sao_Paulo|America/Scoresbysund|America/Shiprock|America/Sitka|America/St_Barthelemy|America/St_Johns|America/St_Kitts|America/St_Lucia|America/St_Thomas|America/St_Vincent|America/Swift_Current|America/Tegucigalpa|America/Thule|America/Thunder_Bay|America/Tijuana|America/Toronto|America/Tortola|America/Vancouver|America/Virgin|America/Whitehorse|America/Winnipeg|America/Yakutat|America/Yellowknife|Antarctica/Casey|Antarctica/Davis|Antarctica/DumontDUrville|Antarctica/Macquarie|Antarctica/Mawson|Antarctica/McMurdo|Antarctica/Palmer|Antarctica/Rothera|Antarctica/South_Pole|Antarctica/Syowa|Antarctica/Troll|Antarctica/Vostok|Arctic/Longyearbyen|Asia/Aden|Asia/Almaty|Asia/Amman|Asia/Anadyr|Asia/Aqtau|Asia/Aqtobe|Asia/Ashgabat|Asia/Ashkhabad|Asia/Atyrau|Asia/Baghdad|Asia/Bahrain|Asia/Baku|Asia/Bangkok|Asia/Barnaul|Asia/Beirut|Asia/Bishkek|Asia/Brunei|Asia/Calcutta|Asia/Chita|Asia/Choibalsan|Asia/Chongqing|Asia/Chungking|Asia/Colombo|Asia/Dacca|Asia/Damascus|Asia/Dhaka|Asia/Dili|Asia/Dubai|Asia/Dushanbe|Asia/Famagusta|Asia/Gaza|Asia/Harbin|Asia/Hebron|Asia/Ho_Chi_Minh|Asia/Hong_Kong|Asia/Hovd|Asia/Irkutsk|Asia/Istanbul|Asia/Jakarta|Asia/Jayapura|Asia/Jerusalem|Asia/Kabul|Asia/Kamchatka|Asia/Karachi|Asia/Kashgar|Asia/Kathmandu|Asia/Katmandu|Asia/Khandyga|Asia/Kolkata|Asia/Krasnoyarsk|Asia/Kuala_Lumpur|Asia/Kuching|Asia/Kuwait|Asia/Macao|Asia/Macau|Asia/Magadan|Asia/Makassar|Asia/Manila|Asia/Muscat|Asia/Nicosia|Asia/Novokuznetsk|Asia/Novosibirsk|Asia/Omsk|Asia/Oral|Asia/Phnom_Penh|Asia/Pontianak|Asia/Pyongyang|Asia/Qatar|Asia/Qostanay|Asia/Qyzylorda|Asia/Rangoon|Asia/Riyadh|Asia/Saigon|Asia/Sakhalin|Asia/Samarkand|Asia/Seoul|Asia/Shanghai|Asia/Singapore|Asia/Srednekolymsk|Asia/Taipei|Asia/Tashkent|Asia/Tbilisi|Asia/Tehran|Asia/Tel_Aviv|Asia/Thimbu|Asia/Thimphu|Asia/Tokyo|Asia/Tomsk|Asia/Ujung_Pandang|Asia/Ulaanbaatar|Asia/Ulan_Bator|Asia/Urumqi|Asia/Ust-Nera|Asia/Vientiane|Asia/Vladivostok|Asia/Yakutsk|Asia/Yangon|Asia/Yekaterinburg|Asia/Yerevan|Atlantic/Azores|Atlantic/Bermuda|Atlantic/Canary|Atlantic/Cape_Verde|Atlantic/Faeroe|Atlantic/Faroe|Atlantic/Jan_Mayen|Atlantic/Madeira|Atlantic/Reykjavik|Atlantic/South_Georgia|Atlantic/St_Helena|Atlantic/Stanley|Australia/ACT|Australia/Adelaide|Australia/Brisbane|Australia/Broken_Hill|Australia/Canberra|Australia/Currie|Australia/Darwin|Australia/Eucla|Australia/Hobart|Australia/LHI|Australia/Lindeman|Australia/Lord_Howe|Australia/Melbourne|Australia/NSW|Australia/North|Australia/Perth|Australia/Queensland|Australia/South|Australia/Sydney|Australia/Tasmania|Australia/Victoria|Australia/West|Australia/Yancowinna|Brazil/Acre|Brazil/DeNoronha|Brazil/East|Brazil/West|CET|CST6CDT|Canada/Atlantic|Canada/Central|Canada/Eastern|Canada/Mountain|Canada/Newfoundland|Canada/Pacific|Canada/Saskatchewan|Canada/Yukon|Chile/Continental|Chile/EasterIsland|Cuba|EET|EST|EST5EDT|Egypt|Eire|Etc/GMT|Etc/GMT+0|Etc/GMT+1|Etc/GMT+10|Etc/GMT+11|Etc/GMT+12|Etc/GMT+2|Etc/GMT+3|Etc/GMT+4|Etc/GMT+5|Etc/GMT+6|Etc/GMT+7|Etc/GMT+8|Etc/GMT+9|Etc/GMT-0|Etc/GMT-1|Etc/GMT-10|Etc/GMT-11|Etc/GMT-12|Etc/GMT-13|Etc/GMT-14|Etc/GMT-2|Etc/GMT-3|Etc/GMT-4|Etc/GMT-5|Etc/GMT-6|Etc/GMT-7|Etc/GMT-8|Etc/GMT-9|Etc/GMT0|Etc/Greenwich|Etc/UCT|Etc/UTC|Etc/Universal|Etc/Zulu|Europe/Amsterdam|Europe/Andorra|Europe/Astrakhan|Europe/Athens|Europe/Belfast|Europe/Belgrade|Europe/Berlin|Europe/Bratislava|Europe/Brussels|Europe/Bucharest|Europe/Budapest|Europe/Busingen|Europe/Chisinau|Europe/Copenhagen|Europe/Dublin|Europe/Gibraltar|Europe/Guernsey|Europe/Helsinki|Europe/Isle_of_Man|Europe/Istanbul|Europe/Jersey|Europe/Kaliningrad|Europe/Kiev|Europe/Kirov|Europe/Kyiv|Europe/Lisbon|Europe/Ljubljana|Europe/London|Europe/Luxembourg|Europe/Madrid|Europe/Malta|Europe/Mariehamn|Europe/Minsk|Europe/Monaco|Europe/Moscow|Europe/Nicosia|Europe/Oslo|Europe/Paris|Europe/Podgorica|Europe/Prague|Europe/Riga|Europe/Rome|Europe/Samara|Europe/San_Marino|Europe/Sarajevo|Europe/Saratov|Europe/Simferopol|Europe/Skopje|Europe/Sofia|Europe/Stockholm|Europe/Tallinn|Europe/Tirane|Europe/Tiraspol|Europe/Ulyanovsk|Europe/Uzhgorod|Europe/Vaduz|Europe/Vatican|Europe/Vienna|Europe/Vilnius|Europe/Volgograd|Europe/Warsaw|Europe/Zagreb|Europe/Zaporozhye|Europe/Zurich|Factory|GB|GB-Eire|GMT|GMT+0|GMT-0|GMT0|Greenwich|HST|Hongkong|Iceland|Indian/Antananarivo|Indian/Chagos|Indian/Christmas|Indian/Cocos|Indian/Comoro|Indian/Kerguelen|Indian/Mahe|Indian/Maldives|Indian/Mauritius|Indian/Mayotte|Indian/Reunion|Iran|Israel|Jamaica|Japan|Kwajalein|Libya|MET|MST|MST7MDT|Mexico/BajaNorte|Mexico/BajaSur|Mexico/General|NZ|NZ-CHAT|Navajo|PRC|PST8PDT|Pacific/Apia|Pacific/Auckland|Pacific/Bougainville|Pacific/Chatham|Pacific/Chuuk|Pacific/Easter|Pacific/Efate|Pacific/Enderbury|Pacific/Fakaofo|Pacific/Fiji|Pacific/Funafuti|Pacific/Galapagos|Pacific/Gambier|Pacific/Guadalcanal|Pacific/Guam|Pacific/Honolulu|Pacific/Johnston|Pacific/Kanton|Pacific/Kiritimati|Pacific/Kosrae|Pacific/Kwajalein|Pacific/Majuro|Pacific/Marquesas|Pacific/Midway|Pacific/Nauru|Pacific/Niue|Pacific/Norfolk|Pacific/Noumea|Pacific/Pago_Pago|Pacific/Palau|Pacific/Pitcairn|Pacific/Pohnpei|Pacific/Ponape|Pacific/Port_Moresby|Pacific/Rarotonga|Pacific/Saipan|Pacific/Samoa|Pacific/Tahiti|Pacific/Tarawa|Pacific/Tongatapu|Pacific/Truk|Pacific/Wake|Pacific/Wallis|Pacific/Yap|Poland|Portugal|ROC|ROK|Singapore|Turkey|UCT|US/Alaska|US/Aleutian|US/Arizona|US/Central|US/East-Indiana|US/Eastern|US/Hawaii|US/Indiana-Starke|US/Michigan|US/Mountain|US/Pacific|US/Samoa|UTC|Universal|W-SU|WET|Zulu
              examples:
                - America/New_York
            - type: 'null'
          title: Timezone
          default: UTC
      additionalProperties: false
      type: object
      required:
        - rrule
      title: RRuleSchedule
      description: >-
        RRule schedule, based on the iCalendar standard

        ([RFC 5545](https://datatracker.ietf.org/doc/html/rfc5545)) as

        implemented in `dateutils.rrule`.


        RRules are appropriate for any kind of calendar-date manipulation,
        including

        irregular intervals, repetition, exclusions, week day or day-of-month

        adjustments, and more.


        Note that as a calendar-oriented standard, `RRuleSchedules` are
        sensitive to

        to the initial timezone provided. A 9am daily schedule with a daylight
        saving

        time-aware start date will maintain a local 9am time through DST
        boundaries;

        a 9am daily schedule with a UTC start date will maintain a 9am UTC time.


        Args:
            rrule (str): a valid RRule string
            timezone (str, optional): a valid timezone string
    ConcurrencyLimitStrategy:
      type: string
      enum:
        - ENQUEUE
        - CANCEL_NEW
      title: ConcurrencyLimitStrategy
      description: Enumeration of concurrency collision strategies.
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

````

Built with [Mintlify](https://mintlify.com).