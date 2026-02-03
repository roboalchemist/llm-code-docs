# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/get-input-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Input Fields

> Get the Input Fields for a particular Action, using the provided authentication and inputs. See the fields and fieldsets guide for more information.
See [our docs](https://docs.zapier.com/powered-by-zapier/zap-creation/fields-and-fieldsets#input-fields) for more information.

#### When using OAuth

This endpoint requires the `zap:write` OAuth scope.



## OpenAPI

````yaml https://api.zapier.com/schema post /v2/actions/{action_id}/inputs
openapi: 3.1.0
info:
  title: Partner API
  version: 2024.11.0
  description: >

    ## Introduction


    The Partner API is the best tool for complete style control over a user's
    Zapier experience within your app.

    Essentially, it lets you customize how you present Zapier within your
    product without sacrificing your app's look,

    feel, and flow.


    Think of it as a native Zapier integration, helping you showcase your best
    Zapier-powered workflows where it's most

    helpful to your users (within the flow of your tool). You can customize
    styling, streamline Zap set-up for users,

    expose relevant Zap information, and more!


    With the Partner API, you can:


    - Get a list of all the apps available in Zapier's app directory so you can
    power your app directory and show your

    users all the integration possibilities with your Zapier integration.

    - Have complete style control over how you present Zap templates in your
    product. The Partner API gives you access

    to the raw Zap Template data so you can give your users access to your Zap
    template with your product's style, look

    and feel.

    - Get access to all your Zap templates and give your users the ability to
    search to quickly find the one they need.

    - Streamline Zap setup by pre-filling fields on behalf of your users.

    - Show users the Zaps they have set up from right within your product
    keeping them on your site longer and giving them

    complete confidence in their Zapier integration.

    - Embed our Zapier Editor to allow your users to create new Zaps and modify
    existing ones, without needing to leave

    your product.


    ## Authentication


    There are two ways to authenticate with the Partner API.


    1. Your application's `client_id` which you will receive once you are
    approved for access to the API

    (Client ID Authentication)

    2. A user's access token (Access Token Authentication).


    Which authentication method you should use depends on which endpoint(s) you
    are using.

    Review each endpoint's documentation to understand which parameters are
    required.


    > Note: while we do generate a `client_secret`, the type of grant we use
    (implicit) doesn't

    need it so it's not something we provide.'


    ## Learn more


    See the [Workflow API
    documentation](https://docs.zapier.com/partner-solutions/workflow-api/intro)
    for more information.
  contact:
    name: Zapier
    url: https://developer.zapier.com/contact
servers:
  - url: https://api.zapier.com
security: []
tags:
  - name: Accounts
    description: Refers to resources interacting with 'Accounts' associated resources
  - name: Actions
    description: Refers to resources interacting with 'Actions' associated resources
  - name: Apps
    description: Refers to resources interacting with 'Apps' associated resources
  - name: Authentications
    description: >-
      Refers to resources interacting with 'Authentications' associated
      resources
  - name: Categories
    description: Refers to resources interacting with 'Categories' associated resources
  - name: Experimental
    description: Refers to resources interacting with 'Experimental' associated resources
  - name: Inputs
    description: Refers to resources interacting with 'Inputs' associated resources
  - name: Outputs
    description: Refers to resources interacting with 'Outputs' associated resources
  - name: Zaps
    description: Refers to resources interacting with 'Zaps' associated resources
  - name: Zap Templates
    description: Refers to resources interacting with 'Zap Templates' associated resources
paths:
  /v2/actions/{action_id}/inputs:
    post:
      tags:
        - Actions
        - Inputs
      summary: Get Input Fields
      description: >-
        Get the Input Fields for a particular Action, using the provided
        authentication and inputs. See the fields and fieldsets guide for more
        information.

        See [our
        docs](https://docs.zapier.com/powered-by-zapier/zap-creation/fields-and-fieldsets#input-fields)
        for more information.


        #### When using OAuth


        This endpoint requires the `zap:write` OAuth scope.
      operationId: get-fields-inputs
      parameters:
        - in: path
          name: action_id
          schema:
            type: string
          description: An Action ID, as provided by the `/actions` endpoint.
          required: true
          example: uag:87b1c14e-ef30-43d5-9395-6c6514dbb123
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ListInputFieldsRequest'
            examples:
              FetchInputFields:
                value:
                  data:
                    limit: 10
                    offset: 0
                    authentication: '928117'
                    inputs:
                      spreadsheet: my_sheet
                summary: Fetch input fields
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InputFieldsResponse'
              examples:
                InputFieldsForSomeApp:
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
                          Use the Input Data fields above to assign key names
                          (left) and map values (right) from previous steps. Use
                          notation `inputData.keyName` or `inputData['keyName']`
                          to access the values within your code. The data will
                          be provided **as strings**. Learn more
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
                          **Warning! This is an advanced action!** Uses Node
                          10.x.x. Please read the [Code documentation for more
                          information](/help/create/code-webhooks/use-javascript-code-in-zaps).
                        format: CODE
                        invalidates_input_fields: false
                        is_required: true
                        placeholder: ''
                        title: Code
                        value_type: STRING
                  summary: Input fields for some app
          description: ''
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                MalformedRequest.:
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
                  summary: Malformed request.
          description: This schema can be expected for 4xx 'Malformed request.' errors
        '401':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 401 Response
        '403':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 403 Response
        '409':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 409 Response
        '429':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 429 Response
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                AServerErrorOccurred.:
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
                  summary: A server error occurred.
          description: >-
            This schema can be expected for 5xx 'A server error occurred.'
            errors
        '503':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 503 Response
        '504':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 504 Response
      security:
        - OAuth:
            - zap:write
components:
  schemas:
    ListInputFieldsRequest:
      type: object
      description: Common inputs with inputs and an authentication id.
      properties:
        data:
          $ref: '#/components/schemas/_ListInputFieldsRequest'
      required:
        - data
    InputFieldsResponse:
      type: object
      description: >-
        A successful response for getting the input fields for a particular
        Action.
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
          $ref: '#/components/schemas/RootFieldset'
      required:
        - data
        - links
        - meta
    ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: An array of error objects.
      required:
        - errors
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
    RootFieldset:
      type: array
      items:
        anyOf:
          - $ref: '#/components/schemas/InputField'
          - $ref: '#/components/schemas/InfoField'
          - $ref: '#/components/schemas/Fieldset'
      description: The base concept of a Fieldset, from which others extend
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
    FieldsetFieldsField:
      anyOf:
        - $ref: '#/components/schemas/InputField'
        - $ref: '#/components/schemas/InfoField'
      description: >-
        Somewhat confusingly named, a field that is a list of either input
        fields or info fields.
  securitySchemes:
    OAuth:
      type: oauth2
      description: >-
        See our OAuth2 authentication documentation here:
        https://docs.zapier.com/powered-by-zapier/api-reference/authentication
      flows:
        authorizationCode:
          authorizationUrl: https://zapier.com/oauth/authorize/
          tokenUrl: https://zapier.com/oauth/token/
          refreshUrl: https://zapier.com/oauth/token/
          scopes:
            profile: Read profile information about the currently-authenticated user
            zap: Read Zaps
            zap:write: Write Zaps
            authentication: Read Authentications
            authentication:write: Write Authentications
            zap:runs: Read Zap Runs
            action:run: Run an Action
            zap:all: Read Zaps accessible to the account
        implicit:
          authorizationUrl: https://zapier.com/oauth/authorize/
          scopes:
            profile: Read profile information about the currently-authenticated user
            zap: Read Zaps
            zap:write: Write Zaps
            authentication: Read Authentications
            authentication:write: Write Authentications
            zap:runs: Read Zap Runs
            action:run: Run an Action
            zap:all: Read Zaps accessible to the account

````