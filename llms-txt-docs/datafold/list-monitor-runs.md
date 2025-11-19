# Source: https://docs.datafold.com/api-reference/monitors/list-monitor-runs.md

# List Monitor Runs

## OpenAPI

````yaml openapi-public.json get /api/v1/monitors/{id}/runs
paths:
  path: /api/v1/monitors/{id}/runs
  method: get
  servers:
    - url: https://app.datafold.com
      description: Default server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: Use the 'Authorization' header with the format 'Key <api-key>'
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: integer
              required: true
              title: Id
              description: The unique identifier of the monitor.
      query:
        page:
          schema:
            - type: integer
              required: false
              title: Page
              description: The page number to retrieve.
              default: 1
        page_size:
          schema:
            - type: integer
              required: false
              title: Page Size
              description: The number of items to retrieve per page.
              default: 10
        start_time:
          schema:
            - type: string
              required: false
              title: Start Time
              description: Include runs with a timestamp >= this value.
              format: date-time
            - type: 'null'
              required: false
              title: Start Time
              description: Include runs with a timestamp >= this value.
        end_time:
          schema:
            - type: string
              required: false
              title: End Time
              description: Include runs with a timestamp <= this value.
              format: date-time
            - type: 'null'
              required: false
              title: End Time
              description: Include runs with a timestamp <= this value.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              count:
                allOf:
                  - description: Total number of monitor runs.
                    title: Count
                    type: integer
              page:
                allOf:
                  - description: Current page number in the paginated result.
                    title: Page
                    type: integer
              page_size:
                allOf:
                  - description: Number of runs per page.
                    title: Page Size
                    type: integer
              runs:
                allOf:
                  - description: List of monitor runs.
                    items:
                      $ref: '#/components/schemas/ApiPublicMonitorRunOut'
                    title: Runs
                    type: array
              total_pages:
                allOf:
                  - description: Total number of pages available.
                    title: Total Pages
                    type: integer
            title: ApiPublicListMonitorRunsOut
            refIdentifier: '#/components/schemas/ApiPublicListMonitorRunsOut'
            requiredProperties:
              - count
              - runs
              - page
              - page_size
              - total_pages
        examples:
          example:
            value:
              count: 123
              page: 123
              page_size: 123
              runs:
                - diff_id: 123
                  monitor_id: 123
                  run_id: 123
                  started_at: '2023-11-07T05:31:56Z'
                  state: ok
              total_pages: 123
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    title: Detail
                    type: array
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
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

````