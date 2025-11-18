# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/step-test.md

# Step Test

> Tests the action (step) in the third party api, using the provided authentication and inputs.

#### OAuth

This endpoint requires the `zap:write` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema post /v2/actions/{action_id}/test
paths:
  path: /v2/actions/{action_id}/test
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
                  - $ref: '#/components/schemas/_ActionTestRequest'
            required: true
            refIdentifier: '#/components/schemas/ActionTestRequest'
            requiredProperties:
              - data
        examples:
          TestingAnAction:
            summary: Testing an action
            value:
              data:
                limit: 10
                offset: 0
                authentication: example_QVaAreV1
                inputs:
                  email: me@example.com
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
                      type: object
                      additionalProperties: {}
                    description: The result of executing said Action on the third-party API
            description: |-
              Base Response definition to be used in other Response Serializers.

              Be sure to include the `data` field after using this class
            refIdentifier: '#/components/schemas/ActionTestResponse'
            requiredProperties:
              - data
              - links
              - meta
        examples:
          ActionTestResponse:
            summary: Action Test Response
            value:
              links:
                next: null
                prev: null
              meta:
                count: 1
                limit: null
                offset: 0
              data:
                - Description: >-
                    A response from some example third party API related to the
                    action
                  Source: RFC 8259
                  Image:
                    Width: 800
                    Height: 600
                    Title: View from 15th Floor
                    Thumbnail:
                      Url: https://www.example.com/image/481989943
                      Height: 125
                      Width: 100
                    Animated: false
                    IDs:
                      - 116
                      - 943
                      - 234
                      - 38793
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
    _ActionTestRequest:
      type: object
      description: The request structure to test a particular Action
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
          description: Authentication, if required, to be able to run the given Action
        inputs:
          type: object
          additionalProperties: {}
          description: Inputs to be provided to the given 'read' Action's test run
      required:
        - authentication
        - inputs

````