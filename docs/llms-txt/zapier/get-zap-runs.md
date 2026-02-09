# Source: https://docs.zapier.com/powered-by-zapier/api-reference/experimental/get-zap-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Zap Runs

> This endpoint returns runs for the specified Zaps and provides basic yet essential details about their execution. As the initial version, it serves foundational information, with plans for continuous enhancement to expand its capabilities and improve data output over time.

#### When using OAuth

This endpoint requires the `zap:runs` OAuth scope.



## OpenAPI

````yaml https://api.zapier.com/schema get /v2/zap-runs
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
  /v2/zap-runs:
    get:
      tags:
        - Experimental
        - Zaps
      summary: Get Zap Runs
      description: >-
        This endpoint returns runs for the specified Zaps and provides basic yet
        essential details about their execution. As the initial version, it
        serves foundational information, with plans for continuous enhancement
        to expand its capabilities and improve data output over time.


        #### When using OAuth


        This endpoint requires the `zap:runs` OAuth scope.
      operationId: get-zap-runs
      parameters:
        - in: query
          name: from_date
          schema:
            type: string
          description: >-
            Filter Zap runs that occurred on or after this date. If not
            provided, the results default to Zap runs from the last 30 days.
          example: '2024-10-16T06:29:10.360000Z'
        - in: query
          name: limit
          schema:
            type: integer
          description: >-
            Used for paginating results. Specifies the maximum number of items
            to return per page. If this value is not set, it defaults to 10.
          example: 10
        - in: query
          name: offset
          schema:
            type: integer
          description: Used for paginating results. Specifies the offset to use.
        - in: query
          name: search
          schema:
            type: string
          description: >-
            Performs a text search against the zap_title, data_in, and data_out
            fields, returning only zap runs that match the specified keywords.
          x-maxLength: 150
          example: My Zap Title
        - in: query
          name: statuses
          schema:
            type: array
            items:
              type: string
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
            Accepts one or more status values separated by comma, enabling the
            filtering of zap runs based on the specified status or statuses
            provided.
          explode: false
          style: form
          example:
            - error
            - success
        - in: query
          name: to_date
          schema:
            type: string
          description: Filter Zap runs that occurred before this date.
          example: '2024-10-16T06:29:10.360000Z'
        - in: query
          name: zap_id
          schema:
            type: integer
          description: Find Zap runs for the specified Zap ID.
          example: 104445735
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ZapRunsResponse'
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
            - zap:runs
components:
  schemas:
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