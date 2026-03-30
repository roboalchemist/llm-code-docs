# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flow-runs/bulk-delete-flow-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Delete Flow Runs

> Bulk delete flow runs matching the specified filter criteria.

Returns the IDs of flow runs that were deleted.



## OpenAPI

````yaml post /flow_runs/bulk_delete
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flow_runs/bulk_delete:
    post:
      tags:
        - Flow Runs
      summary: Bulk Delete Flow Runs
      description: |-
        Bulk delete flow runs matching the specified filter criteria.

        Returns the IDs of flow runs that were deleted.
      operationId: bulk_delete_flow_runs_flow_runs_bulk_delete_post
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
                #/components/schemas/Body_bulk_delete_flow_runs_flow_runs_bulk_delete_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FlowRunBulkDeleteResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_bulk_delete_flow_runs_flow_runs_bulk_delete_post:
      properties:
        flow_runs:
          anyOf:
            - $ref: '#/components/schemas/FlowRunFilter'
            - type: 'null'
          description: Filter criteria for flow runs to delete
        limit:
          type: integer
          maximum: 50
          minimum: 1
          title: Limit
          description: Maximum number of flow runs to delete. Defaults to 50.
          default: 50
      type: object
      title: Body_bulk_delete_flow_runs_flow_runs_bulk_delete_post
    FlowRunBulkDeleteResponse:
      properties:
        deleted:
          items:
            type: string
            format: uuid
          type: array
          title: Deleted
      type: object
      title: FlowRunBulkDeleteResponse
      description: Response from bulk flow run deletion.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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