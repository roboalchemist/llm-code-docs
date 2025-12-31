# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/get-output-fields.md

# Get Output Fields

> Get the Output Fields for a particular Action, using the provided authentication and inputs.

#### OAuth

This endpoint requires the `zap:write` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema post /v2/actions/{action_id}/outputs
paths:
  path: /v2/actions/{action_id}/outputs
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/_ListOutputFieldsRequest'
            required: true
            refIdentifier: '#/components/schemas/ListOutputFieldsRequest'
            requiredProperties:
              - data
        examples:
          FetchingOutputsForSomeApp:
            summary: Fetching outputs for some app
            value:
              data:
                authentication: example_QVaAreV1
                inputs:
                  someparam: somevalue
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              links:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/Links'
                    description: The links object returned in paginated response bodies.
              meta:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/BaseMeta'
                    description: The meta object returned in paginated response bodies.
              data:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/OutputField'
                    description: A list of the Output Fields matching the given request
            description: A successful response containing Output Field data
            refIdentifier: '#/components/schemas/OutputFieldsResponse'
            requiredProperties:
              - data
              - links
              - meta
        examples:
          OutputFieldsForSomeApp:
            summary: Output fields for some app
            value:
              links:
                next: null
                prev: null
              meta:
                count: 3
                limit: null
                offset: 0
              data:
                - type: output_fields
                  id: commit__message
                  title: Commit Message
                  sample: Git 2.0
                - type: output_field
                  id: parents[]sha
                  title: Parents Sha
                  sample: 4a28f169ad29ba452e0e7bea2583914c10c58322
                - type: output_field
                  id: parents[]url
                  title: Parents Url
                  sample: >-
                    https://github.com/git/git/commit/4a28f169ad29ba452e0e7bea2583914c10c58322
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
    OutputField:
      type: object
      properties:
        type:
          type: string
          readOnly: true
          description: The type of this specific Output Field
        id:
          type: string
          description: The identifier for this specific Output Field
        title:
          type: string
          description: The title of this specific Output Field
        sample:
          type: string
          description: An (optional) sample of what an Output Field's value may look like
      required:
        - id
        - title
        - type
    _ListOutputFieldsRequest:
      type: object
      description: The common data object that includes inputs and an authentication id.
      properties:
        limit:
          type:
            - integer
            - 'null'
          minimum: 1
          default: 10
          description: >-
            Used for paginating results. Specifies the maximum number of items
            to return per page.
        offset:
          type:
            - integer
            - 'null'
          minimum: 0
          default: 0
          description: >-
            Used for paginating results. Specifies the offset to use. Defaults
            to 0
        authentication:
          type:
            - string
            - 'null'
          description: >-
            An Authentication ID, as provided by the `/authentications`
            endpoint.
        inputs:
          type: object
          additionalProperties: {}
          description: >-
            The current set of input fields in a JSON object, where each key is
            the `id` of an Input Field, and the corresponding value the current
            value of the field.
        fetch_live_samples:
          type: boolean
          default: false
          description: >-
            Whether to retrieve live samples for the field. While this can be
            helpful in supporting the identification of an output, note that
            this has latency implications as it may require an additional
            request to 3rd party services. This is not supported for `WRITE`
            actions, please use step testing instead.
      required:
        - authentication
        - inputs

````