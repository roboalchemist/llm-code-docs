# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/deployments/bulk-create-flow-runs-from-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Create Flow Runs From Deployment

> Create multiple flow runs from a deployment.

Any parameters not provided will be inferred from the deployment's parameters.
If tags are not provided, the deployment's tags will be used.

If no state is provided, the flow runs will be created in a SCHEDULED state.



## OpenAPI

````yaml post /deployments/{id}/create_flow_run/bulk
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /deployments/{id}/create_flow_run/bulk:
    post:
      tags:
        - Deployments
      summary: Bulk Create Flow Runs From Deployment
      description: >-
        Create multiple flow runs from a deployment.


        Any parameters not provided will be inferred from the deployment's
        parameters.

        If tags are not provided, the deployment's tags will be used.


        If no state is provided, the flow runs will be created in a SCHEDULED
        state.
      operationId: >-
        bulk_create_flow_runs_from_deployment_deployments__id__create_flow_run_bulk_post
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The deployment id
            title: Id
          description: The deployment id
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
              type: array
              items:
                $ref: '#/components/schemas/DeploymentFlowRunCreate'
              description: List of flow run configurations to create
              title: Flow Runs
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FlowRunBulkCreateResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    DeploymentFlowRunCreate:
      properties:
        state:
          anyOf:
            - $ref: '#/components/schemas/StateCreate'
            - type: 'null'
          description: The state of the flow run to create
        name:
          type: string
          title: Name
          description: >-
            The name of the flow run. Defaults to a random slug if not
            specified.
          examples:
            - my-flow-run
        parameters:
          additionalProperties: true
          type: object
          title: Parameters
        enforce_parameter_schema:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Enforce Parameter Schema
          description: Whether or not to enforce the parameter schema on this run.
        context:
          additionalProperties: true
          type: object
          title: Context
        infrastructure_document_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Infrastructure Document Id
        empirical_policy:
          $ref: '#/components/schemas/FlowRunPolicy'
          description: The empirical policy for the flow run.
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of tags for the flow run.
          examples:
            - - tag-1
              - tag-2
        idempotency_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Idempotency Key
          description: >-
            An optional idempotency key. If a flow run with the same idempotency
            key has already been created, the existing flow run will be
            returned.
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
        parent_task_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Parent Task Run Id
        work_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Work Queue Name
        job_variables:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          additionalProperties: true
          title: Job Variables
      additionalProperties: false
      type: object
      title: DeploymentFlowRunCreate
      description: >-
        Data used by the Prefect REST API to create a flow run from a
        deployment.
    FlowRunBulkCreateResponse:
      properties:
        results:
          items:
            $ref: '#/components/schemas/FlowRunCreateResult'
          type: array
          title: Results
      type: object
      title: FlowRunBulkCreateResponse
      description: Response from bulk flow run creation.
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
    FlowRunCreateResult:
      properties:
        flow_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Flow Run Id
        status:
          type: string
          enum:
            - CREATED
            - FAILED
          title: Status
        error:
          anyOf:
            - type: string
            - type: 'null'
          title: Error
      type: object
      required:
        - status
      title: FlowRunCreateResult
      description: Per-run result for bulk create operations.
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