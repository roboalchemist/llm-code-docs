# Source: https://docs.zapier.com/powered-by-zapier/api-reference/zaps/create-a-zap.md

# Create a Zap

> This URL creates a Zap based on the given steps and title.

#### OAuth

This endpoint requires the `zap:write` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema post /v2/zaps
paths:
  path: /v2/zaps
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
      path: {}
      query:
        expand:
          schema:
            - type: string
              description: >-
                A comma separated list of Zap fields that should be expanded
                from ids to full objects in the response. Fields that may not be
                expanded will remain as ids.
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/CreateZapRequest'
            required: true
            refIdentifier: '#/components/schemas/ZapRequest'
            requiredProperties:
              - data
        examples:
          ToBeCreatedZap:
            summary: To be created Zap
            value:
              data:
                steps:
                  - action: example_core:5m2y9p7J
                    inputs:
                      code: >-
                        output = [{id: Math.round(Date.now()/1000), n:
                        Math.random()}];
                    authentication: null
                    alias: null
                  - action: example_core:VBz2NGB5
                    inputs:
                      code: 'output = [{ id: inputData.id, n: inputData.n * 2}];'
                      inputs:
                        'n': '{{n}}'
                        id: '{{id}}'
                    authentication: null
                    alias: null
                title: My Critically Important Program
          ManyStepZap:
            summary: Many Step Zap
            value:
              data:
                steps:
                  - action: core:9QKqnTZ54VnrL2opYbkJJKveKEr2GJ
                    inputs: {}
                    authentication: Vx4PEEeV
                    alias: slack_new_saved_message
                  - action: core:2oY5MSxlgML1jb43A0nroedgjdnVM
                    inputs:
                      to:
                        - chang.hsiao@irohalen.example
                      subject: 3 step zap - new message saved in slack
                      body: |-
                        Saved new message from:
                        {{slack_new_saved_message.user__real_name}}


                        Message Content:
                        {{text}}
                    authentication: k0QBMMDK
                    alias: null
                  - action: core:vDakLS1PLO4J29eodDRLa5okErEn0
                    inputs:
                      channel: U036ZHWNHU2
                      text: |-
                        Saved new message from:
                        {{slack_new_saved_message.user__real_name}}


                        Email thread id:
                        {{threadId}}


                        Message Content:
                        {{slack_new_saved_message.text}}
                    authentication: Vx4PEEeV
                    alias: slack_send_direct_message
                title: My 3 step zap
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    readOnly: true
                    description: The type of this object.
              id:
                allOf:
                  - type: string
                    readOnly: true
                    description: A unique identifier of the Zap.
              is_enabled:
                allOf:
                  - type: boolean
                    default: true
                    description: Whether the Zap is enabled (running) or not.
              last_successful_run_date:
                allOf:
                  - type:
                      - string
                      - 'null'
                    readOnly: true
                    description: >-
                      The date/time at which this Zap last ran successfully. A
                      null value indicates that a Zap has never run
                      successfully.
              updated_at:
                allOf:
                  - type: string
                    readOnly: true
                    description: The last time this Zap was updated
              title:
                allOf:
                  - type: string
                    description: The human readable name of the Zap.
              links:
                allOf:
                  - type: object
                    additionalProperties: {}
                    readOnly: true
                    description: Link to open this Zap in the Zapier Editor
              steps:
                allOf:
                  - description: A list of the steps this Zap consists of
                    type: array
                    items:
                      oneOf:
                        - $ref: '#/components/schemas/ExpandedZapStep'
                        - type: string
            description: >-
              A Zap is an automated workflow that connects your apps and
              services together.
            refIdentifier: '#/components/schemas/ExpandedZap'
            requiredProperties:
              - id
              - last_successful_run_date
              - links
              - steps
              - title
              - type
              - updated_at
        examples:
          CustomCreatedZap:
            summary: Custom created zap
            value:
              type: zap
              id: 033cc069f2d3-4d63-8666-10c07ab38dac
              is_enabled: true
              last_successful_run_date: '2019-08-24T14:15:22Z'
              updated_at: '2024-03-14T22:02:36+00:00'
              title: My Critically Important Program
              links:
                html_editor: >-
                  https://zapier.com/editor/104826178?utm_source=partner&utm_medium=embed&utm_campaign=partner_api&referer=zapier
              steps:
                - action: example_core:Vn7xbE60
                  authentication: 2kyXZ8VJ
                  inputs: {}
                  title: null
                - action: example_core:V7GpzX40
                  authentication: null
                  inputs: null
                  title: null
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
    ActionTypeEnum:
      enum:
        - action
      type: string
      description: '* `action` - action'
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

                        If value is `null`, then no authentication is required to use the app.
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
    Authentication:
      type: object
      description: >-
        An Authentication contains various fields, often credentials such as API
        tokens, used to access Partner APIs on

        behalf of a user. The actual fields are held securely by Zapier
      properties:
        type:
          allOf:
            - $ref: '#/components/schemas/AuthenticationTypeEnum'
          readOnly: true
          default: authentication
          description: |-
            The type of this object.

            * `authentication` - authentication
        id:
          type: string
          description: The identifier for this specific Authentication
        app:
          description: An app that integrates with Zapier.
          oneOf:
            - $ref: '#/components/schemas/Apps'
            - type: string
        is_expired:
          type: boolean
          description: >-
            If `true`, this Authentication has expired. It will not be usable,
            and the user needs to be directed to reconnect it.
        title:
          type: string
          description: The title of this specific Authentication
      required:
        - app
        - id
        - is_expired
        - title
        - type
    AuthenticationTypeEnum:
      enum:
        - authentication
      type: string
      description: '* `authentication` - authentication'
    Category:
      type: object
      description: Category an app belongs to.
      properties:
        slug:
          type: string
          description: The shortened slug name for this category
      required:
        - slug
    CreateZapRequest:
      type: object
      description: See our Building a Zap guide to get started.
      properties:
        steps:
          type: array
          items:
            $ref: '#/components/schemas/CreateZapRequestStep'
          description: The list of steps that the Zap should consist of
        title:
          type: string
          description: The title to be set for this Zap
      required:
        - steps
        - title
    CreateZapRequestStep:
      type: object
      properties:
        action:
          type: string
          description: The ID of the Action to be associated with this step
        inputs:
          type: object
          additionalProperties: {}
          description: The inputs for the Action associated with this step
        authentication:
          type:
            - string
            - 'null'
          description: The authentication, if required, for this Action to run
        alias:
          type:
            - string
            - 'null'
          description: >-
            Optional alias for this step to be referenced by later steps
            (snake_case, max 64 chars)
          maxLength: 64
          pattern: ^[a-z][a-z0-9_]*$
      required:
        - action
        - authentication
        - inputs
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
    ExpandedZapStep:
      type: object
      description: An ordered list of steps that define the logic of the Zap.
      properties:
        action:
          description: Action
          oneOf:
            - $ref: '#/components/schemas/Action'
            - type: string
        authentication:
          description: Authentication
          oneOf:
            - $ref: '#/components/schemas/Authentication'
            - type:
                - string
                - 'null'
        inputs:
          readOnly: true
          description: The inputs for this specific Zap's step
        title:
          type:
            - string
            - 'null'
          readOnly: true
          description: >-
            The custom title of a Zap Step. If a step has not been given a
            custom title by the user, then the value will be null.
      required:
        - action
        - authentication
        - inputs
        - title

````