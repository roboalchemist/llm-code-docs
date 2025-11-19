# Source: https://docs.datafold.com/api-reference/monitors/list-monitors.md

# List Monitors

## OpenAPI

````yaml openapi-public.json get /api/v1/monitors
paths:
  path: /api/v1/monitors
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
      path: {}
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
              default: 20
        order_by:
          schema:
            - type: enum<string>
              enum:
                - id
                - name
                - last_triggered
                - last_run
                - created_by_id
              required: false
              title: SortableFields
              description: Field to order the monitors by.
              refIdentifier: '#/components/schemas/SortableFields'
            - type: 'null'
              required: false
              title: Order By
              description: Field to order the monitors by.
        sort_order:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              required: false
              title: Sort Order
              description: Specify the order direction for the monitors.
              default: desc
        tags:
          schema:
            - type: string
              required: false
              title: Tags
              description: Comma-separated tags to filter monitors by.
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
                  - description: Total number of monitors.
                    title: Count
                    type: integer
              monitors:
                allOf:
                  - description: List of monitor details.
                    items:
                      $ref: '#/components/schemas/ApiPublicGetMonitorOut'
                    title: Monitors
                    type: array
              page:
                allOf:
                  - description: Current page number in the paginated result.
                    title: Page
                    type: integer
              page_size:
                allOf:
                  - description: Number of monitors per page.
                    title: Page Size
                    type: integer
              total_pages:
                allOf:
                  - description: Total number of pages available.
                    title: Total Pages
                    type: integer
            title: ApiPublicListMonitorsOut
            refIdentifier: '#/components/schemas/ApiPublicListMonitorsOut'
            requiredProperties:
              - count
              - monitors
              - page
              - page_size
              - total_pages
        examples:
          example:
            value:
              count: 123
              monitors:
                - created_at: '2023-11-07T05:31:56Z'
                  enabled: true
                  id: 123
                  last_alert: '2023-11-07T05:31:56Z'
                  last_run: '2023-11-07T05:31:56Z'
                  modified_at: '2023-11-07T05:31:56Z'
                  monitor_type: diff
                  name: <string>
                  state: ok
                  tags:
                    - <string>
              page: 123
              page_size: 123
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
    ApiPublicGetMonitorOut:
      properties:
        created_at:
          description: Timestamp when the monitor was created.
          format: date-time
          title: Created At
          type: string
        enabled:
          description: Indicates whether the monitor is enabled.
          title: Enabled
          type: boolean
        id:
          description: Unique identifier for the monitor.
          title: Id
          type: integer
        last_alert:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          description: Timestamp of the last alert.
          title: Last Alert
        last_run:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          description: Timestamp of the last monitor run.
          title: Last Run
        modified_at:
          description: Timestamp when the monitor was last modified.
          format: date-time
          title: Modified At
          type: string
        monitor_type:
          anyOf:
            - enum:
                - diff
                - metric
                - schema
                - test
              type: string
            - type: 'null'
          description: Type of the monitor.
          title: Monitor Type
        name:
          anyOf:
            - type: string
            - type: 'null'
          description: Name of the monitor.
          title: Name
        state:
          anyOf:
            - $ref: '#/components/schemas/MonitorRunState'
            - type: 'null'
          description: Current state of the monitor run.
        tags:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          description: Tags associated with the monitor.
          title: Tags
      required:
        - id
        - name
        - monitor_type
        - created_at
        - modified_at
        - enabled
      title: ApiPublicGetMonitorOut
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