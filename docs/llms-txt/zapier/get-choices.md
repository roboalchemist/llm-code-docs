# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/get-choices.md

# Get Choices

> Get the possible values for a `SELECT` Input Field.

#### OAuth

This endpoint requires the `zap` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema post /v2/actions/{action_id}/inputs/{input_id}/choices
paths:
  path: /v2/actions/{action_id}/inputs/{input_id}/choices
  method: post
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
        action_id:
          schema:
            - type: string
              required: true
              description: An Action ID, as provided by the `/actions` endpoint.
        input_id:
          schema:
            - type: string
              required: true
              description: An Input Field ID, as provided by the `/inputs` endpoint.
      query:
        page:
          schema:
            - type: string
              description: The page of choices to return, defaults to the first
              default: '1'
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/ChoiceParams'
            required: true
            refIdentifier: '#/components/schemas/ChoiceRequest'
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                authentication: <string>
                inputs: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/ChoiceResponse'
        examples:
          ChoicesForSomeAction:
            summary: Choices for Some Action
            value:
              - data:
                  - id: 55c
                    type: choice
                    label: First
                    value: example
                  - id: a73
                    type: choice
                    label: Second
                    value: example
                links:
                  next: null
                  prev: null
                meta:
                  page: 1
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
    Choice:
      type: object
      description: A single element from a set of Choices, variants in an enumeration.
      properties:
        id:
          type: string
          description: The ID of this variant
        type:
          type: string
          description: The type of this object
        label:
          type:
            - string
            - 'null'
          description: >-
            An optional human-readable label for this variant. Useful if the
            actual value is not a human-readable value, such as an identifier.
        value:
          type: string
          description: The value of this variant.
      required:
        - id
        - type
        - value
    ChoiceParams:
      type: object
      description: A Choice as to be provided to the /choices endpoint
      properties:
        authentication:
          type:
            - string
            - 'null'
          description: The Authentication ID for this Choice, if present/required
        inputs:
          type:
            - object
            - 'null'
          additionalProperties: {}
          description: The Inputs for this Choice, if present/required
      required:
        - authentication
        - inputs
    ChoiceResponse:
      type: object
      description: A successful response for getting the requested Input Fields.
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/Choice'
          description: A list of Choices matching the given request
        links:
          allOf:
            - $ref: '#/components/schemas/Links'
          description: The links object returned in paginated response bodies.
        meta:
          allOf:
            - $ref: '#/components/schemas/Meta'
          description: The meta object returned in paginated response bodies.
      required:
        - links
        - meta
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
    Meta:
      type: object
      description: Metadata about a certain response
      properties:
        page:
          type: integer
          description: The current page
      required:
        - page

````