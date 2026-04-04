# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flow-runs/read-flow-run-graph-v1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Flow Run Graph V1

> Get a task run dependency map for a given flow run.



## OpenAPI

````yaml get /flow_runs/{id}/graph
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flow_runs/{id}/graph:
    get:
      tags:
        - Flow Runs
        - Flow Run Graph
      summary: Read Flow Run Graph V1
      description: Get a task run dependency map for a given flow run.
      operationId: read_flow_run_graph_v1_flow_runs__id__graph_get
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The flow run id
            title: Id
          description: The flow run id
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
                type: array
                items:
                  $ref: '#/components/schemas/DependencyResult'
                title: Response Read Flow Run Graph V1 Flow Runs  Id  Graph Get
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    DependencyResult:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        name:
          type: string
          title: Name
        upstream_dependencies:
          items:
            $ref: '#/components/schemas/TaskRunResult'
          type: array
          title: Upstream Dependencies
        state:
          anyOf:
            - $ref: '#/components/schemas/State'
            - type: 'null'
        expected_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Expected Start Time
        start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Start Time
        end_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: End Time
        total_run_time:
          anyOf:
            - type: number
            - type: 'null'
          title: Total Run Time
        estimated_run_time:
          anyOf:
            - type: number
            - type: 'null'
          title: Estimated Run Time
        untrackable_result:
          type: boolean
          title: Untrackable Result
      type: object
      required:
        - id
        - name
        - upstream_dependencies
        - state
        - expected_start_time
        - start_time
        - end_time
        - total_run_time
        - estimated_run_time
        - untrackable_result
      title: DependencyResult
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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