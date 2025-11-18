# Source: https://docs.zapier.com/powered-by-zapier/api-reference/accounts/create-account.md

# Create Account

> Create a new user and obtain an access token. See our Quick Account Creation guide to get started.

## OpenAPI

````yaml https://api.zapier.com/schema get /v2/authorize
paths:
  path: /v2/authorize
  method: get
  servers:
    - url: https://api.zapier.com
  request:
    security:
      - title: ClientIDAuthentication
        parameters:
          query:
            ClientIDAuthentication:
              type: apiKey
              description: >-
                See our authentication documentation for how to find your Client
                ID
          header: {}
          cookie: {}
    parameters:
      path: {}
      query:
        client_id:
          schema:
            - type: string
              required: true
              description: Your application Client ID.
              minLength: 1
        redirect_uri:
          schema:
            - type: string
              required: true
              description: The page the user will be redirect to after OAuth flow.
              minLength: 1
        referer:
          schema:
            - type: string
              minLength: 1
        response_type:
          schema:
            - type: string
              required: true
              description: Only OAuth response type `code` is supported
              minLength: 1
        scope:
          schema:
            - type: string
              required: true
              description: Space (`%20`) separated values
              minLength: 1
        sign_up_email:
          schema:
            - type: string
              description: Email of the user signing up.
              format: email
              minLength: 1
        sign_up_first_name:
          schema:
            - type: string
              description: First name of the user signing up.
              minLength: 1
        sign_up_last_name:
          schema:
            - type: string
              description: Last name of the user signing up.
              minLength: 1
        utm_campaign:
          schema:
            - type: string
              minLength: 1
              default: workflow_api
        utm_content:
          schema:
            - type: string
              minLength: 1
        utm_medium:
          schema:
            - type: string
              minLength: 1
              default: embed
        utm_source:
          schema:
            - type: string
              minLength: 1
              default: partner
      header: {}
      cookie: {}
    body: {}
  response:
    '302':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Redirect to authorization URL
        examples: {}
        description: Redirect to authorization URL
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

````