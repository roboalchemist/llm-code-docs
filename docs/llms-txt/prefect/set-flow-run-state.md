# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flow-runs/set-flow-run-state.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Flow Run State

> Set a flow run state, invoking any orchestration rules.



## OpenAPI

````yaml post /flow_runs/{id}/set_state
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flow_runs/{id}/set_state:
    post:
      tags:
        - Flow Runs
      summary: Set Flow Run State
      description: Set a flow run state, invoking any orchestration rules.
      operationId: set_flow_run_state_flow_runs__id__set_state_post
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_set_flow_run_state_flow_runs__id__set_state_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrchestrationResult'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_set_flow_run_state_flow_runs__id__set_state_post:
      properties:
        state:
          $ref: '#/components/schemas/StateCreate'
          description: The intended state.
        force:
          type: boolean
          title: Force
          description: >-
            If false, orchestration rules will be applied that may alter or
            prevent the state transition. If True, orchestration rules are not
            applied.
          default: false
      type: object
      required:
        - state
      title: Body_set_flow_run_state_flow_runs__id__set_state_post
    OrchestrationResult:
      properties:
        state:
          anyOf:
            - $ref: '#/components/schemas/State'
            - type: 'null'
        status:
          $ref: '#/components/schemas/SetStateStatus'
        details:
          anyOf:
            - $ref: '#/components/schemas/StateAcceptDetails'
            - $ref: '#/components/schemas/StateWaitDetails'
            - $ref: '#/components/schemas/StateRejectDetails'
            - $ref: '#/components/schemas/StateAbortDetails'
          title: Details
      type: object
      required:
        - state
        - status
        - details
      title: OrchestrationResult
      description: A container for the output of state orchestration.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    StateCreate:
      properties:
        type:
          $ref: '#/components/schemas/StateType'
          description: The type of the state to create
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
          description: The name of the state to create
        message:
          anyOf:
            - type: string
            - type: 'null'
          title: Message
          description: The message of the state to create
        data:
          anyOf:
            - {}
            - type: 'null'
          title: Data
          description: The data of the state to create
        state_details:
          $ref: '#/components/schemas/StateDetails'
          description: The details of the state to create
      additionalProperties: false
      type: object
      required:
        - type
      title: StateCreate
      description: Data used by the Prefect REST API to create a new state.
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
    SetStateStatus:
      type: string
      enum:
        - ACCEPT
        - REJECT
        - ABORT
        - WAIT
      title: SetStateStatus
      description: Enumerates return statuses for setting run states.
    StateAcceptDetails:
      properties:
        type:
          type: string
          const: accept_details
          title: Type
          description: >-
            The type of state transition detail. Used to ensure pydantic does
            not coerce into a different type.
          default: accept_details
      type: object
      title: StateAcceptDetails
      description: Details associated with an ACCEPT state transition.
    StateWaitDetails:
      properties:
        type:
          type: string
          const: wait_details
          title: Type
          description: >-
            The type of state transition detail. Used to ensure pydantic does
            not coerce into a different type.
          default: wait_details
        delay_seconds:
          type: integer
          title: Delay Seconds
          description: >-
            The length of time in seconds the client should wait before
            transitioning states.
        reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Reason
          description: The reason why the state transition should wait.
      type: object
      required:
        - delay_seconds
      title: StateWaitDetails
      description: Details associated with a WAIT state transition.
    StateRejectDetails:
      properties:
        type:
          type: string
          const: reject_details
          title: Type
          description: >-
            The type of state transition detail. Used to ensure pydantic does
            not coerce into a different type.
          default: reject_details
        reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Reason
          description: The reason why the state transition was rejected.
      type: object
      title: StateRejectDetails
      description: Details associated with a REJECT state transition.
    StateAbortDetails:
      properties:
        type:
          type: string
          const: abort_details
          title: Type
          description: >-
            The type of state transition detail. Used to ensure pydantic does
            not coerce into a different type.
          default: abort_details
        reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Reason
          description: The reason why the state transition was aborted.
      type: object
      title: StateAbortDetails
      description: Details associated with an ABORT state transition.
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