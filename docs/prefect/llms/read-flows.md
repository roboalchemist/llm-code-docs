# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flows/read-flows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Flows

> Query for flows.



## OpenAPI

````yaml post /flows/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flows/filter:
    post:
      tags:
        - Flows
      summary: Read Flows
      description: Query for flows.
      operationId: read_flows_flows_filter_post
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
              $ref: '#/components/schemas/Body_read_flows_flows_filter_post'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Flow'
                title: Response Read Flows Flows Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_flows_flows_filter_post:
      properties:
        offset:
          type: integer
          minimum: 0
          title: Offset
          default: 0
        flows:
          $ref: '#/components/schemas/FlowFilter'
        flow_runs:
          $ref: '#/components/schemas/FlowRunFilter'
        task_runs:
          $ref: '#/components/schemas/TaskRunFilter'
        deployments:
          $ref: '#/components/schemas/DeploymentFilter'
        work_pools:
          $ref: '#/components/schemas/WorkPoolFilter'
        sort:
          $ref: '#/components/schemas/FlowSort'
          default: NAME_ASC
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_flows_flows_filter_post
    Flow:
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
          pattern: ^[^/%&><]+$
          title: Name
          description: The name of the flow
          examples:
            - my-flow
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of flow tags
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
      type: object
      required:
        - name
        - id
        - created
        - updated
      title: Flow
      description: An ORM representation of flow data.
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
    FlowSort:
      type: string
      enum:
        - CREATED_DESC
        - UPDATED_DESC
        - NAME_ASC
        - NAME_DESC
      title: FlowSort
      description: Defines flow sorting options.
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