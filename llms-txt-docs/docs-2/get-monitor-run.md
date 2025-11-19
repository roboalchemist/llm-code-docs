# Source: https://docs.datafold.com/api-reference/monitors/get-monitor-run.md

# Get Monitor Run

## OpenAPI

````yaml openapi-public.json get /api/v1/monitors/{id}/runs/{run_id}
paths:
  path: /api/v1/monitors/{id}/runs/{run_id}
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
        run_id:
          schema:
            - type: integer
              required: true
              title: Run Id
              description: The unique identifier of the run to retrieve.
        id:
          schema:
            - type: integer
              required: true
              title: Id
              description: The unique identifier of the monitor associated with the run.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              diff_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    description: Unique identifier for the associated datadiff.
                    title: Diff Id
              error:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: Error message if the run encountered an error.
                    title: Error
              monitor_id:
                allOf:
                  - description: Unique identifier for the associated monitor.
                    title: Monitor Id
                    type: integer
              run_id:
                allOf:
                  - description: Unique identifier for the monitor run result.
                    title: Run Id
                    type: integer
              started_at:
                allOf:
                  - anyOf:
                      - format: date-time
                        type: string
                      - type: 'null'
                    description: Timestamp when the monitor run started.
                    title: Started At
              state:
                allOf:
                  - $ref: '#/components/schemas/MonitorRunState'
                    description: Current state of the monitor run result.
              warnings:
                allOf:
                  - description: List of warning messages generated during the run.
                    items:
                      type: string
                    title: Warnings
                    type: array
            title: ApiPublicMonitorRunResultOut
            refIdentifier: '#/components/schemas/ApiPublicMonitorRunResultOut'
            requiredProperties:
              - run_id
              - monitor_id
              - state
              - warnings
        examples:
          example:
            value:
              diff_id: 123
              error: <string>
              monitor_id: 123
              run_id: 123
              started_at: '2023-11-07T05:31:56Z'
              state: ok
              warnings:
                - <string>
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