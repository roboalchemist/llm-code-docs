# Source: https://docs.zapier.com/powered-by-zapier/api-reference/actions/get-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Actions

> Fetch the available actions for the provided App. It's typical to filter by type so that only actions that make sense for a particular step are shown. Action IDs may not be reused, see our documentation for how to hardcode a particular action.

#### When using Client ID

Simply providing a client ID query parameter is sufficient. If an Authorization header is present, it will be used instead.

#### When using OAuth

This endpoint requires the `zap` OAuth scope.



## OpenAPI

````yaml https://api.zapier.com/schema get /v2/actions
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
  /v2/actions:
    get:
      tags:
        - Actions
        - Apps
      summary: Get Actions
      description: >-
        Fetch the available actions for the provided App. It's typical to filter
        by type so that only actions that make sense for a particular step are
        shown. Action IDs may not be reused, see our documentation for how to
        hardcode a particular action.


        #### When using Client ID


        Simply providing a client ID query parameter is sufficient. If an
        Authorization header is present, it will be used instead.


        #### When using OAuth


        This endpoint requires the `zap` OAuth scope.
      operationId: get-actions
      parameters:
        - in: query
          name: action_type
          schema:
            type: string
            enum:
              - READ
              - READ_BULK
              - SEARCH
              - SEARCH_AND_WRITE
              - SEARCH_OR_WRITE
              - WRITE
          description: >-
            The type of Action to filter for. Defaults to returning all actions
            regardless of type.
          example: READ
        - in: query
          name: app
          schema:
            type: string
            format: uuid
          description: A canonical App ID, as provided by the `/apps` endpoint.
          required: true
          example: 868f9d3c-2ea0-4f19-a32d-a61b276ab8de
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ActionsResponse'
              examples:
                ActionsExample:
                  value:
                    - links:
                        next: null
                        prev: null
                      meta:
                        count: 1
                        limit: 10
                        offset: 0
                      data:
                        - id: uag:1f188536-6dd0-4172-8414-2b90914ddee9
                          key: new_lead
                          app: 83b47c0e-adda-44da-a45d-42565fe521ef
                          type: action
                          action_type: action
                          is_instant: true
                          title: New Lead
                          description: Triggers when a new lead is added to SuperExampleCRM
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
            - zap
        - ClientIDAuthentication: []
components:
  schemas:
    ActionsResponse:
      type: object
      description: A valid response for fetching available actions for the App
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
            $ref: '#/components/schemas/Action'
          description: List of Actions for the provided App
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
    Action:
      type: object
      description: >-
        An Action is an operation that can be performed against a third-party
        API; either a read or a write. A Zap is composed of a read, followed by
        one or more writes.
      properties:
        id:
          type: string
          description: >-
            The ID to refer to this action (unstable, may change when referenced
            app changes)
        key:
          type: string
          description: The developer provided identifier for this Action (stable)
        app:
          description: Apps
          oneOf:
            - $ref: '#/components/schemas/Apps'
            - type: string
        type:
          allOf:
            - $ref: '#/components/schemas/ActionTypeEnum'
          description: |-
            The type of this object

            * `action` - action
        action_type:
          allOf:
            - $ref: '#/components/schemas/ActionTypeEnum'
          description: |-
            The type of this Action

            * `READ` - READ
            * `READ_BULK` - READ_BULK
            * `WRITE` - WRITE
            * `SEARCH` - SEARCH
            * `SEARCH_OR_WRITE` - SEARCH_OR_WRITE
            * `SEARCH_AND_WRITE` - SEARCH_AND_WRITE
            * `FILTER` - FILTER
        is_instant:
          type: boolean
          description: >-
            Will be set to `true` if this Action triggers instantly. May only be
            `true` when `type` is `READ`.
        title:
          type: string
          description: The title of this Action.
        description:
          type: string
          description: >-
            A longer description of this Action, usually describing what it does
            in more detail.
      required:
        - action_type
        - app
        - description
        - id
        - is_instant
        - key
        - title
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
    Apps:
      type: object
      description: An app that integrates with Zapier
      properties:
        id:
          type: string
          description: Unique id of the app
        type:
          type: string
          default: app
          description: The type of this object.
        image:
          type: string
          description: Default image/icon to represent the app.
        links:
          type: object
          additionalProperties: {}
          description: >-
            A url that, when visited, will direct the user to authenticate with
            the app and allow Zapier access to the app, thus creating a new
            Authentication.

                        If value is `null`, then no authentication is required to use the app. Client ID-authenticated requests will never have this object's fields populated.
        action_types:
          type: array
          items: {}
          description: A list of action types for this specific App
        title:
          type: string
          description: Human readable name of the app
        images:
          allOf:
            - $ref: '#/components/schemas/AppsImages'
          description: The URL of images (of various sizes) for this specific App
        hex_color:
          type: string
          description: A branded color that can be used to represent the app.
        categories:
          type: array
          items:
            $ref: '#/components/schemas/Category'
          description: >-
            A list of categories to which this app belongs. Helpful in
            identifying apps by type and functionality.
        description:
          type: string
          description: Human readable description of the app.
      required:
        - action_types
        - categories
        - description
        - hex_color
        - id
        - image
        - images
        - links
        - title
    ActionTypeEnum:
      enum:
        - action
      type: string
      description: '* `action` - action'
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
    AppsImages:
      type: object
      description: Images/icons of various resolutions to represent the app.
      properties:
        url_16x16:
          type: string
          description: 16x16 resolution image URL
        url_32x32:
          type: string
          description: 32x32 resolution image URL
        url_64x64:
          type: string
          description: 64x64 resolution image URL
        url_128x128:
          type: string
          description: 128x128 resolution image URL
      required:
        - url_128x128
        - url_16x16
        - url_32x32
        - url_64x64
    Category:
      type: object
      description: Category an app belongs to.
      properties:
        slug:
          type: string
          description: The shortened slug name for this category
      required:
        - slug
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
    ClientIDAuthentication:
      type: apiKey
      in: query
      name: client_id
      description: See our authentication documentation for how to find your Client ID
      x-zapier-auth-scheme-exempt: true

````