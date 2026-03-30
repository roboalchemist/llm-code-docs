# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flow-runs/update-flow-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Flow Run

> Updates a flow run.



## OpenAPI

````yaml patch /flow_runs/{id}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flow_runs/{id}:
    patch:
      tags:
        - Flow Runs
      summary: Update Flow Run
      description: Updates a flow run.
      operationId: update_flow_run_flow_runs__id__patch
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
              $ref: '#/components/schemas/FlowRunUpdate'
      responses:
        '204':
          description: Successful Response
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    FlowRunUpdate:
      properties:
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        flow_version:
          anyOf:
            - type: string
            - type: 'null'
          title: Flow Version
        parameters:
          additionalProperties: true
          type: object
          title: Parameters
        empirical_policy:
          $ref: '#/components/schemas/FlowRunPolicy'
        tags:
          items:
            type: string
          type: array
          title: Tags
        infrastructure_pid:
          anyOf:
            - type: string
            - type: 'null'
          title: Infrastructure Pid
        job_variables:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Job Variables
      additionalProperties: false
      type: object
      title: FlowRunUpdate
      description: Data used by the Prefect REST API to update a flow run.
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

````

Built with [Mintlify](https://mintlify.com).