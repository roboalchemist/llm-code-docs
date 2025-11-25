# Source: https://docs.zapier.com/powered-by-zapier/running-actions/retrieve-action-run.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/retrieve-action-run.md

# Source: https://docs.zapier.com/powered-by-zapier/running-actions/retrieve-action-run.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/retrieve-action-run.md

# Source: https://docs.zapier.com/powered-by-zapier/running-actions/retrieve-action-run.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/retrieve-action-run.md

# Retrieve Action Run

> Retrieves an Action Run.

#### OAuth

This endpoint requires the `action:run` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema get /v2/action-runs/{id}
paths:
  path: /v2/action-runs/{id}
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: An Action Run ID.
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
              data:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/_ActionRunResponse'
                    description: The resulting data after a given Action was run
            description: The response of a given Action Run
            refIdentifier: '#/components/schemas/ActionRunResponse'
            requiredProperties:
              - data
        examples:
          RetrievingARun:
            summary: Retrieving a run
            value:
              data:
                type: run
                status: success
                results:
                  - id: 123
                errors: []
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
    CodeEnum:
      enum:
        - user
        - authentication
        - partner
        - system
        - throttled
        - system_throttled
        - hydration
      type: string
      description: |-
        * `user` - user
        * `authentication` - authentication
        * `partner` - partner
        * `system` - system
        * `throttled` - throttled
        * `system_throttled` - system_throttled
        * `hydration` - hydration
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
    RunTypeEnum:
      enum:
        - run
      type: string
      description: '* `run` - Run'
    _ActionRunResponse:
      type: object
      properties:
        type:
          allOf:
            - $ref: '#/components/schemas/RunTypeEnum'
          description: |-
            The type of this object

            * `run` - Run
        status:
          $ref: '#/components/schemas/_ActionRunResponseStatusEnum'
        results:
          type: array
          items:
            type: object
            additionalProperties: {}
          description: Could be empty, even if the action was successfully run.
        errors:
          type: array
          items:
            $ref: '#/components/schemas/_ActionRunResponseError'
          description: Any errors returned by the partner when running this action.
      required:
        - errors
        - status
        - type
    _ActionRunResponseError:
      type: object
      description: >-
        The error information returned from a third party when running an
        action.
      properties:
        code:
          allOf:
            - $ref: '#/components/schemas/CodeEnum'
          description: |-
            Error type of the result object.

            * `user` - user
            * `authentication` - authentication
            * `partner` - partner
            * `system` - system
            * `throttled` - throttled
            * `system_throttled` - system_throttled
            * `hydration` - hydration
        title:
          type: string
          description: A short summary of the problem.
        detail:
          type: string
          description: >-
            A human-readable explanation specific to this occurrence of the
            problem.
        delay:
          type: integer
          description: >-
            When a partner throttled the execution call (error_type =
            throttled), this value will hold the number of seconds to wait
            before retrying.
        meta:
          type:
            - object
            - 'null'
          additionalProperties: {}
          description: Any additional error information returned from the partner.
    _ActionRunResponseStatusEnum:
      enum:
        - success
        - error
        - waiting
      type: string
      description: |-
        * `success` - success
        * `error` - error
        * `waiting` - waiting

````