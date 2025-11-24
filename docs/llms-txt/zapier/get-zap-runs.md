# Source: https://docs.zapier.com/powered-by-zapier/api-reference/experimental/get-zap-runs.md

# Get Zap Runs

> This endpoint returns runs for the specified Zaps and provides basic yet essential details about their execution. As the initial version, it serves foundational information, with plans for continuous enhancement to expand its capabilities and improve data output over time.

#### OAuth

This endpoint requires the `zap:runs` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema get /v2/zap-runs
paths:
  path: /v2/zap-runs
  method: get
  servers:
    - url: https://api.zapier.com
  request:
    security:
      - title: OAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: oauth2
              description: >-
                See our OAuth2 authentication documentation here:
                https://docs.zapier.com/powered-by-zapier/api-reference/authentication
          cookie: {}
    parameters:
      path: {}
      query:
        from_date:
          schema:
            - type: string
              description: >-
                Filter Zap runs that occurred on or after this date. If not
                provided, the results default to Zap runs from the last 30 days.
        limit:
          schema:
            - type: integer
              description: >-
                Used for paginating results. Specifies the maximum number of
                items to return per page. If this value is not set, it defaults
                to 10.
        offset:
          schema:
            - type: integer
              description: Used for paginating results. Specifies the offset to use.
        search:
          schema:
            - type: string
              description: >-
                Performs a text search against the zap_title, data_in, and
                data_out fields, returning only zap runs that match the
                specified keywords.
        statuses:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
                    enum:
                      - delayed
                      - scheduled
                      - pending
                      - error
                      - error_handled
                      - halted
                      - throttled
                      - held
                      - filtered
                      - skipped
                      - success
              description: >-
                Accepts one or more status values separated by comma, enabling
                the filtering of zap runs based on the specified status or
                statuses provided.
          style: form
          explode: false
        to_date:
          schema:
            - type: string
              description: Filter Zap runs that occurred before this date.
        zap_id:
          schema:
            - type: integer
              description: Find Zap runs for the specified Zap ID.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/ZapRunsResponse'
        examples:
          /v2/zap-runs:
            value:
              - links:
                  next: https://api.zapier.com/v2/zap-runs?offset=10&limit=10
                  prev: https://api.zapier.com/v2/zap-runs?offset=0&limit=10
                meta:
                  count: 30
                  limit: 10
                  offset: 10
                data:
                  - id: 123e4567-e89b-12d3-a456-426614174000
                    zap_id: 104445735
                    start_time: '2024-10-16T06:29:10.360000Z'
                    end_time: '2024-10-16T06:29:10.360000Z'
                    status: success
                    zap_title: My Awesome Zap
                    steps:
                      - status: success
                        start_time: '2024-10-16T06:29:10.360000Z'
                    data_in: ''
                    data_out: ''
        description: ''
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - &ref_0
                    type: array
                    items:
                      $ref: '#/components/schemas/Error'
                    description: An array of error objects.
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_1
              - errors
        examples:
          MalformedRequest.:
            summary: Malformed request.
            value:
              errors:
                - status: 400
                  code: parse_error
                  title: ParseError
                  detail: Malformed request.
                  source: null
                  meta:
                    source: ZAPIER
                    full_details:
                      message: Malformed request.
                      code: parse_error
        description: This schema can be expected for 4xx 'Malformed request.' errors
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 401 Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 403 Response
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 409 Response
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 429 Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          AServerErrorOccurred.:
            summary: A server error occurred.
            value:
              errors:
                - status: 500
                  code: error
                  title: APIException
                  detail: A server error occurred.
                  source: null
                  meta:
                    source: ZAPIER
                    full_details:
                      message: A server error occurred.
                      code: error
        description: This schema can be expected for 5xx 'A server error occurred.' errors
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 503 Response
  deprecated: false
  type: path
components:
  schemas:
    BaseMeta:
      type: object
      description: The meta object returned in paginated response bodies.
      properties:
        count:
          type: integer
          minimum: 0
          description: >-
            The total number of objects in the collection represented by the
            endpoint.
        limit:
          type:
            - integer
            - 'null'
          minimum: 1
          description: The limit value used in the request.
        offset:
          type: integer
          minimum: 0
          default: 0
          description: The offset value used in the request.
      required:
        - count
        - limit
    Error:
      type: object
      description: Base Error definition
      properties:
        status:
          type: integer
          description: The HTTP status code applicable to this problem.
        code:
          type: string
          description: A unique identifier for this particular occurrence of the problem.
        title:
          type: string
          description: A short summary of the problem.
        detail:
          type: string
          description: >-
            A human-readable explanation specific to this occurrence of the
            problem.
        source:
          oneOf:
            - $ref: '#/components/schemas/ErrorSource'
            - type: 'null'
          description: An object containing references to the primary source of the error.
        meta:
          type:
            - object
            - 'null'
          additionalProperties: {}
          description: Freeform metadata about the error
    ErrorSource:
      type: object
      description: Populates the `source` object inside our error responses.
      properties:
        pointer:
          type: string
          description: >-
            Pointer to the value in the request document that caused the error
            e.g. `/actions`.
        parameter:
          type: string
          description: A string indicating which URI query parameter caused the error.
        header:
          type: string
          description: >-
            A string indicating the name of a single request header which caused
            the error.
    Links:
      type: object
      description: The links object returned in paginated response bodies.
      properties:
        next:
          type:
            - string
            - 'null'
          description: The URL of the next page of paginated results.
        prev:
          type:
            - string
            - 'null'
          description: The URL of the previous page of paginated results.
    ZapRun:
      type: object
      description: A single Zap Run response.
      properties:
        id:
          type: string
          format: uuid
          description: Zap Run ID
        zap_id:
          type: integer
          description: Associated Zap ID
        start_time:
          type:
            - string
            - 'null'
          format: date-time
          description: Datetime when the Zap Run started
        end_time:
          type:
            - string
            - 'null'
          format: date-time
          description: Datetime when the Zap Run ended
        status:
          type: string
          description: Execution status of the Zap Run
        zap_title:
          type:
            - string
            - 'null'
          description: The title of the Zap at the time it ran
        steps:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ZapRunStep'
          description: Contains the execution details of each step
        data_in:
          oneOf:
            - {}
            - type: 'null'
          description: The input data for the Zap Run
        data_out:
          oneOf:
            - {}
            - type: 'null'
          description: The output data for the Zap Run
      required:
        - id
        - status
        - steps
        - zap_id
        - zap_title
    ZapRunStep:
      type: object
      description: A single step in a Zap Run.
      properties:
        status:
          type:
            - string
            - 'null'
          description: Execution status of the step
        start_time:
          type:
            - string
            - 'null'
          format: date-time
          description: Datetime when the step was executed
      required:
        - status
    ZapRunsResponse:
      type: object
      description: A list of Zap Runs.
      properties:
        links:
          allOf:
            - $ref: '#/components/schemas/Links'
          description: The links object returned in paginated response bodies.
        meta:
          allOf:
            - $ref: '#/components/schemas/BaseMeta'
          description: The meta object returned in paginated response bodies.
        data:
          type: array
          items:
            $ref: '#/components/schemas/ZapRun'
          description: The returned data after a successful Zap run
      required:
        - links
        - meta

````