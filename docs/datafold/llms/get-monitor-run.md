# Source: https://docs.datafold.com/api-reference/monitors/get-monitor-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Monitor Run



## OpenAPI

````yaml openapi-public.json get /api/v1/monitors/{id}/runs/{run_id}
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/monitors/{id}/runs/{run_id}:
    get:
      tags:
        - Monitors
      summary: Get Monitor Run
      operationId: get_monitor_run_api_v1_monitors__id__runs__run_id__get
      parameters:
        - description: The unique identifier of the run to retrieve.
          in: path
          name: run_id
          required: true
          schema:
            description: The unique identifier of the run to retrieve.
            title: Run Id
            type: integer
        - description: The unique identifier of the monitor associated with the run.
          in: path
          name: id
          required: true
          schema:
            description: The unique identifier of the monitor associated with the run.
            title: Id
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiPublicMonitorRunResultOut'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiPublicMonitorRunResultOut:
      properties:
        diff_id:
          anyOf:
            - type: integer
            - type: 'null'
          description: Unique identifier for the associated datadiff.
          title: Diff Id
        error:
          anyOf:
            - type: string
            - type: 'null'
          description: Error message if the run encountered an error.
          title: Error
        monitor_id:
          description: Unique identifier for the associated monitor.
          title: Monitor Id
          type: integer
        run_id:
          description: Unique identifier for the monitor run result.
          title: Run Id
          type: integer
        started_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          description: Timestamp when the monitor run started.
          title: Started At
        state:
          $ref: '#/components/schemas/MonitorRunState'
          description: Current state of the monitor run result.
        warnings:
          description: List of warning messages generated during the run.
          items:
            type: string
          title: Warnings
          type: array
      required:
        - run_id
        - monitor_id
        - state
        - warnings
      title: ApiPublicMonitorRunResultOut
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
    MonitorRunState:
      enum:
        - ok
        - alert
        - error
        - learning
        - checking
        - created
        - skipped
        - cancelled
      title: MonitorRunState
      type: string
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````