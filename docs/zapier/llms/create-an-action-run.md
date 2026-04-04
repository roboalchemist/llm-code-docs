# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/create-an-action-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an Action Run

> Runs an action (step) in the third party API, using the provided authentication and inputs.

This endpoint is asynchronous, and the response will contain an Action Run ID. You can use the `/v2/action-runs/:id` endpoint to check the status of the run and retrieve the results.

#### When using OAuth

This endpoint requires the `action:run` OAuth scope.

<Warning>
  Running actions via the Workflow API is currently in limited beta. If you
  would like access to run actions, please use [this
  form](https://zapier.com/developer-platform#form) to request access.
</Warning>

This API is [rate limited](/powered-by-zapier/api-reference/rate-limiting).


## OpenAPI

````yaml https://api.zapier.com/schema post /v2/action-runs
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
  /v2/action-runs:
    post:
      tags:
        - Experimental
      summary: Create an Action Run
      description: >-
        Runs an action (step) in the third party API, using the provided
        authentication and inputs.


        This endpoint is asynchronous, and the response will contain an Action
        Run ID. You can use the `/v2/action-runs/:id` endpoint to check the
        status of the run and retrieve the results.


        #### When using OAuth


        This endpoint requires the `action:run` OAuth scope.
      operationId: create-action-run
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RunActionRequest'
            examples:
              CreatingAnActionRun(runningAnAction):
                value:
                  data:
                    action: example_core:Vn7xbE60
                    authentication: example_QVaAreV1
                    inputs:
                      email: me@example.com
                summary: Creating an Action Run (running an action)
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RunActionResponse'
              examples:
                CreateActionRunResponse:
                  value:
                    data:
                      type: run
                      id: 123e4567-e89b-12d3-a456-426614174000
                  summary: Create Action Run Response
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
            - action:run
components:
  schemas:
    RunActionRequest:
      type: object
      properties:
        data:
          allOf:
            - $ref: '#/components/schemas/_RunActionRequest'
          description: Data for the Action Run
      required:
        - data
    RunActionResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/_RunActionResponse'
      required:
        - data
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
    _RunActionRequest:
      type: object
      properties:
        action:
          type: string
          description: The ID for the Action to be run
        authentication:
          type:
            - string
            - 'null'
          description: The ID for Authentication (if required)
        inputs:
          type: object
          additionalProperties: {}
          description: >-
            Inputs to be provided to the Action referenced by the ID field, when
            run
      required:
        - action
        - authentication
        - inputs
    _RunActionResponse:
      type: object
      description: The response after an Action Run
      properties:
        type:
          allOf:
            - $ref: '#/components/schemas/RunTypeEnum'
          description: |-
            The type of this object

            * `run` - Run
        id:
          type: string
          format: uuid
          description: The UUID of this Action Run
      required:
        - id
        - type
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
    RunTypeEnum:
      enum:
        - run
      type: string
      description: '* `run` - Run'
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