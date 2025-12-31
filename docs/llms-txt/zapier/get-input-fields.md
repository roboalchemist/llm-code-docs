# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/get-input-fields.md

# Get Input Fields

> Get the Input Fields for a particular Action, using the provided authentication and inputs. See the fields and fieldsets guide for more information.

#### OAuth

This endpoint requires the `zap:write` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema post /v2/actions/{action_id}/inputs
paths:
  path: /v2/actions/{action_id}/inputs
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
                  - $ref: '#/components/schemas/_ListInputFieldsRequest'
            required: true
            description: Common inputs with inputs and an authentication id.
            refIdentifier: '#/components/schemas/ListInputFieldsRequest'
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                limit: 10
                offset: 0
                authentication: <string>
                inputs: {}
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
                  - $ref: '#/components/schemas/RootFieldset'
            description: >-
              A successful response for getting the input fields for a
              particular Action.
            refIdentifier: '#/components/schemas/InputFieldsResponse'
            requiredProperties:
              - data
              - links
              - meta
        examples:
          InputFieldsForSomeApp:
            summary: Input fields for some app
            value:
              links:
                next: null
                prev: null
              meta:
                count: 2
                limit: null
                offset: 0
              data:
                - type: input_field
                  id: input
                  default_value: ''
                  depends_on: []
                  description: >-
                    Use the Input Data fields above to assign key names (left)
                    and map values (right) from previous steps. Use notation
                    `inputData.keyName` or `inputData['keyName']` to access the
                    values within your code. The data will be provided **as
                    strings**. Learn more
                    [here](https://zapier.com/help/create/code-webhooks/use-javascript-code-in-zaps#input-data-for-code-steps).
                  invalidates_input_fields: false
                  is_required: false
                  placeholder: ''
                  title: Input Data
                  value_type: OBJECT
                - type: input_field
                  id: code
                  default_value: |-
                    // this is wrapped in an `async` function
                    // you can use await throughout the function

                    output = [{id: 123, hello: "world"}];
                  depends_on: []
                  description: >-
                    **Warning! This is an advanced action!** Uses Node 10.x.x.
                    Please read the [Code documentation for more
                    information](/help/create/code-webhooks/use-javascript-code-in-zaps).
                  format: CODE
                  invalidates_input_fields: false
                  is_required: true
                  placeholder: ''
                  title: Code
                  value_type: STRING
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
    Fieldset:
      type: object
      description: Represents a Fieldset
      properties:
        type:
          type: string
          readOnly: true
          description: The type of this Fieldset
        id:
          type: string
          description: The unique identifier for this Fieldset
        fields:
          allOf:
            - $ref: '#/components/schemas/FieldsetFieldsField'
          description: The fields this Fieldset consists of
        title:
          type: string
          description: The title of this Fieldset
      required:
        - fields
        - id
        - title
        - type
    FieldsetFieldsField:
      anyOf:
        - $ref: '#/components/schemas/InputField'
        - $ref: '#/components/schemas/InfoField'
      description: >-
        Somewhat confusingly named, a field that is a list of either input
        fields or info fields.
    FormatEnum:
      enum:
        - DATETIME
        - MULTILINE
        - PASSWORD
        - CODE
        - READONLY
        - FILE
        - SELECT
      type: string
      description: |-
        * `DATETIME` - DATETIME
        * `MULTILINE` - MULTILINE
        * `PASSWORD` - PASSWORD
        * `CODE` - CODE
        * `READONLY` - READONLY
        * `FILE` - FILE
        * `SELECT` - SELECT
    InfoField:
      type: object
      description: Represents an Info-type Fieldset
      properties:
        type:
          type: string
          readOnly: true
          description: The type of this Info Field
        id:
          type: string
          description: The identifier of this Info Field
        description:
          type: string
          description: The description for this Info Field
      required:
        - description
        - id
        - type
    InputField:
      type: object
      description: Represents Input Field data as accepted by the API
      properties:
        type:
          type: string
          readOnly: true
          description: The type of Input Field
        id:
          type: string
          description: The identifier for this Input Field
        default_value:
          type: string
          description: The default value for this Input Field if not otherwise specified
        depends_on:
          type: array
          items:
            type: string
          description: A list of dependencies for this Input Field
        description:
          type: string
          description: The description of this Input Field
        format:
          allOf:
            - $ref: '#/components/schemas/FormatEnum'
          description: |-
            The format of this Input Field from one of options provided

            * `DATETIME` - DATETIME
            * `MULTILINE` - MULTILINE
            * `PASSWORD` - PASSWORD
            * `CODE` - CODE
            * `READONLY` - READONLY
            * `FILE` - FILE
            * `SELECT` - SELECT
        invalidates_input_fields:
          type: boolean
          description: Whether this Input Field invalidates
        is_required:
          type: boolean
          description: Whether this Input Field is required
        items:
          type: object
          additionalProperties:
            type: string
          description: A freeform object of items for this Input Field
        placeholder:
          type: string
          description: The placeholder for this Input Field when shown
        title:
          type: string
          description: The title of this Input Field
        value_type:
          allOf:
            - $ref: '#/components/schemas/ValueTypeEnum'
          description: |-
            The type of the *value* of this Input Field

            * `STRING` - STRING
            * `NUMBER` - NUMBER
            * `INTEGER` - INTEGER
            * `BOOLEAN` - BOOLEAN
            * `ARRAY` - ARRAY
            * `OBJECT` - OBJECT
      required:
        - default_value
        - depends_on
        - description
        - format
        - id
        - invalidates_input_fields
        - is_required
        - items
        - placeholder
        - title
        - type
        - value_type
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
    RootFieldset:
      type: array
      items:
        anyOf:
          - $ref: '#/components/schemas/InputField'
          - $ref: '#/components/schemas/InfoField'
          - $ref: '#/components/schemas/Fieldset'
      description: The base concept of a Fieldset, from which others extend
    ValueTypeEnum:
      enum:
        - STRING
        - NUMBER
        - INTEGER
        - BOOLEAN
        - ARRAY
        - OBJECT
      type: string
      description: |-
        * `STRING` - STRING
        * `NUMBER` - NUMBER
        * `INTEGER` - INTEGER
        * `BOOLEAN` - BOOLEAN
        * `ARRAY` - ARRAY
        * `OBJECT` - OBJECT
    _ListInputFieldsRequest:
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
          description: An Authentication ID provided by the `/authentications` endpoint.
        inputs:
          type: object
          additionalProperties: {}
          description: >-
            The current set of input fields in a JSON object, where each key is
            the `id` of an Input Field, and the corresponding value the current
            value of the field.
      required:
        - authentication
        - inputs

````