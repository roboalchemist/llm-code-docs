# Source: https://docs.datafold.com/api-reference/monitors/list-monitors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Monitors



## OpenAPI

````yaml openapi-public.json get /api/v1/monitors
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
  /api/v1/monitors:
    get:
      tags:
        - Monitors
      summary: List Monitors
      operationId: list_monitors_api_v1_monitors_get
      parameters:
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
            default: 20
            description: The number of items to retrieve per page.
            title: Page Size
            type: integer
        - description: Field to order the monitors by.
          in: query
          name: order_by
          required: false
          schema:
            anyOf:
              - $ref: '#/components/schemas/SortableFields'
              - type: 'null'
            description: Field to order the monitors by.
            title: Order By
        - description: Specify the order direction for the monitors.
          in: query
          name: sort_order
          required: false
          schema:
            default: desc
            description: Specify the order direction for the monitors.
            enum:
              - asc
              - desc
            title: Sort Order
            type: string
        - description: Comma-separated tags to filter monitors by.
          in: query
          name: tags
          required: false
          schema:
            description: Comma-separated tags to filter monitors by.
            title: Tags
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiPublicListMonitorsOut'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    SortableFields:
      enum:
        - id
        - name
        - last_triggered
        - last_run
        - created_by_id
      title: SortableFields
      type: string
    ApiPublicListMonitorsOut:
      properties:
        count:
          description: Total number of monitors.
          title: Count
          type: integer
        monitors:
          description: List of monitor details.
          items:
            $ref: '#/components/schemas/ApiPublicGetMonitorOut'
          title: Monitors
          type: array
        page:
          description: Current page number in the paginated result.
          title: Page
          type: integer
        page_size:
          description: Number of monitors per page.
          title: Page Size
          type: integer
        total_pages:
          description: Total number of pages available.
          title: Total Pages
          type: integer
      required:
        - count
        - monitors
        - page
        - page_size
        - total_pages
      title: ApiPublicListMonitorsOut
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