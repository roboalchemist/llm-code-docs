# Source: https://docs.datafold.com/api-reference/monitors/list-monitor-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Monitor Runs



## OpenAPI

````yaml openapi-public.json get /api/v1/monitors/{id}/runs
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
  /api/v1/monitors/{id}/runs:
    get:
      tags:
        - Monitors
      summary: List Monitor Runs
      operationId: list_monitor_runs_api_v1_monitors__id__runs_get
      parameters:
        - description: The unique identifier of the monitor.
          in: path
          name: id
          required: true
          schema:
            description: The unique identifier of the monitor.
            title: Id
            type: integer
        - description: The page number to retrieve.
          in: query
          name: page
          required: false
          schema:
            default: 1
            description: The page number to retrieve.
            title: Page
            type: integer
        - description: The number of items to retrieve per page.
          in: query
          name: page_size
          required: false
          schema:
            default: 10
            description: The number of items to retrieve per page.
            title: Page Size
            type: integer
        - description: Include runs with a timestamp >= this value.
          in: query
          name: start_time
          required: false
          schema:
            anyOf:
              - format: date-time
                type: string
              - type: 'null'
            description: Include runs with a timestamp >= this value.
            title: Start Time
        - description: Include runs with a timestamp <= this value.
          in: query
          name: end_time
          required: false
          schema:
            anyOf:
              - format: date-time
                type: string
              - type: 'null'
            description: Include runs with a timestamp <= this value.
            title: End Time
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiPublicListMonitorRunsOut'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiPublicListMonitorRunsOut:
      properties:
        count:
          description: Total number of monitor runs.
          title: Count
          type: integer
        page:
          description: Current page number in the paginated result.
          title: Page
          type: integer
        page_size:
          description: Number of runs per page.
          title: Page Size
          type: integer
        runs:
          description: List of monitor runs.
          items:
            $ref: '#/components/schemas/ApiPublicMonitorRunOut'
          title: Runs
          type: array
        total_pages:
          description: Total number of pages available.
          title: Total Pages
          type: integer
      required:
        - count
        - runs
        - page
        - page_size
        - total_pages
      title: ApiPublicListMonitorRunsOut
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
    ApiPublicMonitorRunOut:
      properties:
        diff_id:
          anyOf:
            - type: integer
            - type: 'null'
          description: Unique identifier for the associated datadiff.
          title: Diff Id
        monitor_id:
          description: Unique identifier for the associated monitor.
          title: Monitor Id
          type: integer
        run_id:
          description: Unique identifier for the monitor run.
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
          anyOf:
            - $ref: '#/components/schemas/MonitorRunState'
            - type: 'null'
          description: Current state of the monitor run.
      required:
        - run_id
        - monitor_id
      title: ApiPublicMonitorRunOut
      type: object
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
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````