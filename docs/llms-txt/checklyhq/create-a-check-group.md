# Source: https://checklyhq.com/docs/api-reference/check-groups/create-a-check-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a check group

> Creates a new check group. You can add checks to the group by setting the "groupId" property of individual checks.



## OpenAPI

````yaml post /v1/check-groups
openapi: 3.0.0
info:
  title: Checkly Public API
  version: v1
  description: >-
    These are the docs for the newly released Checkly Public API. If you have
    any questions, please do not hesitate to get in touch with us.
servers:
  - url: https://api.checklyhq.com
security:
  - Bearer: []
tags: []
paths:
  /v1/check-groups:
    post:
      tags:
        - Check groups
      summary: Create a check group
      description: >-
        Creates a new check group. You can add checks to the group by setting
        the "groupId" property of individual checks.
      operationId: postV1Checkgroups
      parameters:
        - name: x-checkly-account
          in: header
          schema:
            type: string
            description: >-
              Your Checkly account ID, you can find it at
              https://app.checklyhq.com/settings/account/general
            x-format:
              guid: true
          description: >-
            Your Checkly account ID, you can find it at
            https://app.checklyhq.com/settings/account/general
        - name: autoAssignAlerts
          in: query
          schema:
            type: boolean
            description: >-
              Determines whether a new check will automatically be added as a
              subscriber to all existing alert channels when it gets created.
            default: true
          description: >-
            Determines whether a new check will automatically be added as a
            subscriber to all existing alert channels when it gets created.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CheckGroupCreate'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckGroup'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '402':
          description: Payment Required
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentRequiredError'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForbiddenError'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
      deprecated: true
components:
  schemas:
    CheckGroupCreate:
      type: object
      properties:
        name:
          type: string
          description: The name of the check group.
          example: Check group
        activated:
          type: boolean
          description: Determines if the checks in the group are running or not.
          default: true
        muted:
          type: boolean
          description: >-
            Determines if any notifications will be send out when a check in
            this group fails and/or recovers.
          default: false
        tags:
          $ref: '#/components/schemas/CheckGroupTagList'
        locations:
          $ref: '#/components/schemas/Model42'
        concurrency:
          type: number
          description: >-
            Determines how many checks are invoked concurrently when triggering
            a check group from CI/CD or through the API.
          default: 3
          minimum: 1
          x-constraint:
            sign: positive
        apiCheckDefaults:
          $ref: '#/components/schemas/CheckGroupCreateAPICheckDefaults'
        browserCheckDefaults:
          type: string
        runtimeId:
          $ref: '#/components/schemas/Model43'
        environmentVariables:
          $ref: '#/components/schemas/environmentVariables'
        doubleCheck:
          type: boolean
          description: >-
            [Deprecated] Retry failed check runs. This property is deprecated,
            and `retryStrategy` can be used instead.
          default: true
        useGlobalAlertSettings:
          type: boolean
          description: >-
            When true, the account level alert setting will be used, not the
            alert setting defined on this check group.
          default: true
        alertSettings:
          $ref: '#/components/schemas/AlertSettings'
        alertChannelSubscriptions:
          $ref: '#/components/schemas/Model44'
        setupSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the setup phase of an API
            check in this group.
          example: 'null'
          default: null
          nullable: true
        tearDownSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the teardown phase of an API
            check in this group.
          example: 'null'
          default: null
          nullable: true
        localSetupScript:
          type: string
          description: >-
            A valid piece of Node.js code to run in the setup phase of an API
            check in this group.
          example: 'null'
          default: null
          nullable: true
        localTearDownScript:
          type: string
          description: >-
            A valid piece of Node.js code to run in the teardown phase of an API
            check in this group.
          example: 'null'
          default: null
          nullable: true
        privateLocations:
          $ref: '#/components/schemas/Model45'
        runParallel:
          type: boolean
          description: >-
            When true, the checks in the group will run in parallel in all
            selected locations.
          default: false
        retryStrategy:
          description: Either a retry strategy object or the literal string "FALLBACK".
          anyOf:
            - 78d3e700-6f41-4733-8e7b-47df99e9333a
            - 2313eddc-cf25-405f-903e-deb691a57cf7
      required:
        - name
    CheckGroup:
      type: object
      properties:
        id:
          type: number
          example: 1
        name:
          type: string
          description: The name of the check group.
          example: Check group
        activated:
          type: boolean
          description: Determines if the checks in the  group are running or not.
        muted:
          type: boolean
          description: >-
            Determines if any notifications will be send out when a check in
            this group fails and/or recovers.
        tags:
          $ref: '#/components/schemas/CheckGroupTagList'
        locations:
          $ref: '#/components/schemas/CheckGroupLocationList'
        concurrency:
          type: number
          description: >-
            Determines how many checks are invoked concurrently when triggering
            a check group from CI/CD or through the API.
          default: 3
          minimum: 1
          x-constraint:
            sign: positive
        apiCheckDefaults:
          $ref: '#/components/schemas/CheckGroupAPICheckDefaults'
        browserCheckDefaults:
          type: string
        environmentVariables:
          $ref: '#/components/schemas/EnvironmentVariableList'
        doubleCheck:
          type: boolean
          description: >-
            [Deprecated] Retry failed check runs. This property is deprecated,
            and `retryStrategy` can be used instead.
        useGlobalAlertSettings:
          type: boolean
          description: >-
            When true, the account level alert setting will be used, not the
            alert setting defined on this check group.
          nullable: true
        alertSettings:
          $ref: '#/components/schemas/CheckGroupAlertSettings'
        alertChannelSubscriptions:
          $ref: '#/components/schemas/AlertChannelSubscriptionCreateList'
        setupSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the setup phase of an API
            check in this group.
          example: 'null'
          nullable: true
        tearDownSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the teardown phase of an API
            check in this group.
          example: 'null'
          nullable: true
        localSetupScript:
          type: string
          description: >-
            A valid piece of Node.js code to run in the setup phase of an API
            check in this group.
          example: 'null'
          nullable: true
        localTearDownScript:
          type: string
          description: >-
            A valid piece of Node.js code to run in the teardown phase of an API
            check in this group.
          example: 'null'
          nullable: true
        runtimeId:
          $ref: '#/components/schemas/runtimeId'
        privateLocations:
          $ref: '#/components/schemas/privateLocations'
        retryStrategy:
          description: Either a retry strategy object or the literal string "FALLBACK".
          anyOf:
            - 78d3e700-6f41-4733-8e7b-47df99e9333a
            - 2313eddc-cf25-405f-903e-deb691a57cf7
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date-time
          nullable: true
        runParallel:
          type: boolean
          description: >-
            When true, the checks in the group will run in parallel in all
            selected locations.
          default: false
          nullable: true
      required:
        - name
        - activated
        - concurrency
        - apiCheckDefaults
    UnauthorizedError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 401
        error:
          $ref: '#/components/schemas/error'
        message:
          type: string
          example: Bad Token
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    PaymentRequiredError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 402
        error:
          $ref: '#/components/schemas/Model7'
        message:
          type: string
          example: Payment Required
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    ForbiddenError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 403
        error:
          $ref: '#/components/schemas/Model1'
        message:
          type: string
          example: Forbidden
      required:
        - statusCode
        - error
    TooManyRequestsError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 429
        error:
          $ref: '#/components/schemas/Model2'
        message:
          type: string
          example: Too Many Requests
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    CheckGroupTagList:
      type: array
      description: Tags for organizing and filtering checks.
      example:
        - production
      items:
        type: string
    Model42:
      type: array
      description: An array of one or more data center locations where to run the checks.
      example:
        - us-east-1
        - eu-central-1
      items:
        $ref: '#/components/schemas/Model41'
    CheckGroupCreateAPICheckDefaults:
      type: object
      example:
        url: https://api.example.com/v1
        headers:
          - key: Cache-Control
            value: no-store
        queryParameters:
          - key: Page
            value: '1'
        assertions:
          - source: STATUS_CODE
            comparison: NOT_EMPTY
            target: '200'
        basicAuth:
          username: admin
          password: abc12345
      default: {}
      properties:
        url:
          type: string
          description: >-
            The base url for this group which you can reference with the
            {{GROUP_BASE_URL}} variable in all group checks.
          example: https://api.example.com/v1
          default: ''
          nullable: true
        headers:
          $ref: '#/components/schemas/HeaderList'
        queryParameters:
          $ref: '#/components/schemas/QueryParameterList'
        assertions:
          $ref: '#/components/schemas/AssertionList'
        basicAuth:
          $ref: '#/components/schemas/BasicAuth'
    Model43:
      type: string
      description: >-
        The runtime version, i.e. fixed set of runtime dependencies, used to
        execute checks in this group.
      default: null
      enum:
        - '2026.04'
        - '2025.04'
        - '2024.09'
        - '2024.02'
        - '2023.09'
        - '2023.02'
        - '2022.10'
      nullable: true
    environmentVariables:
      type: array
      nullable: true
      maxItems: 50
      items:
        $ref: '#/components/schemas/EnvironmentVariableUpdate'
    AlertSettings:
      type: object
      description: Alert settings.
      default:
        escalationType: RUN_BASED
        runBasedEscalation:
          failedRunThreshold: 1
        reminders:
          amount: 0
          interval: 5
        parallelRunFailureThreshold:
          enabled: false
          percentage: 10
      properties:
        escalationType:
          $ref: '#/components/schemas/escalationType'
        reminders:
          $ref: '#/components/schemas/AlertSettingsReminders'
        sslCertificates:
          $ref: '#/components/schemas/AlertSettingsSSLCertificates'
        runBasedEscalation:
          $ref: '#/components/schemas/AlertSettingsRunBasedEscalation'
        timeBasedEscalation:
          $ref: '#/components/schemas/AlertSettingsTimeBasedEscalation'
        parallelRunFailureThreshold:
          $ref: '#/components/schemas/parallelRunFailureThreshold'
    Model44:
      type: array
      description: List of alert channel subscriptions.
      example: []
      items:
        $ref: '#/components/schemas/Model40'
    Model45:
      type: array
      description: An array of one or more private locations where to run the checks.
      example:
        - data-center-eu
      nullable: true
      items:
        type: string
    CheckGroupLocationList:
      type: array
      description: An array of one or more data center locations where to run the checks.
      example:
        - us-east-1
        - eu-central-1
      items:
        $ref: '#/components/schemas/Model39'
    CheckGroupAPICheckDefaults:
      type: object
      properties:
        url:
          type: string
          description: >-
            The base url for this group which you can reference with the
            {{GROUP_BASE_URL}} variable in all group checks.
          example: https://api.example.com/v1
          default: ''
          nullable: true
        headers:
          $ref: '#/components/schemas/HeaderList'
        queryParameters:
          $ref: '#/components/schemas/QueryParameterList'
        assertions:
          $ref: '#/components/schemas/AssertionList'
        basicAuth:
          $ref: '#/components/schemas/BasicAuth'
    EnvironmentVariableList:
      type: array
      nullable: true
      maxItems: 50
      items:
        $ref: '#/components/schemas/EnvironmentVariableGet'
    CheckGroupAlertSettings:
      type: object
      description: Alert settings.
      default:
        escalationType: RUN_BASED
        runBasedEscalation:
          failedRunThreshold: 1
        reminders:
          amount: 0
          interval: 5
        parallelRunFailureThreshold:
          enabled: false
          percentage: 10
      enum:
        - value: {}
      nullable: true
      properties:
        escalationType:
          $ref: '#/components/schemas/escalationType'
        reminders:
          $ref: '#/components/schemas/AlertSettingsReminders'
        sslCertificates:
          $ref: '#/components/schemas/AlertSettingsSSLCertificates'
        runBasedEscalation:
          $ref: '#/components/schemas/AlertSettingsRunBasedEscalation'
        timeBasedEscalation:
          $ref: '#/components/schemas/AlertSettingsTimeBasedEscalation'
        parallelRunFailureThreshold:
          $ref: '#/components/schemas/parallelRunFailureThreshold'
    AlertChannelSubscriptionCreateList:
      type: array
      description: List of alert channel subscriptions.
      items:
        $ref: '#/components/schemas/Model40'
    runtimeId:
      type: string
      description: >-
        The runtime version, i.e. fixed set of runtime dependencies, used to
        execute checks in this group.
      example: 'null'
      enum:
        - '2026.04'
        - '2025.04'
        - '2024.09'
        - '2024.02'
        - '2023.09'
        - '2023.02'
        - '2022.10'
      nullable: true
    privateLocations:
      type: array
      description: An array of one or more private locations where to run the check.
      example:
        - data-center-eu
      nullable: true
      items:
        type: string
    error:
      type: string
      enum:
        - Unauthorized
    attributes:
      type: object
    Model7:
      type: string
      enum:
        - Payment Required
    Model1:
      type: string
      enum:
        - Forbidden
    Model2:
      type: string
      enum:
        - Too Many Requests
    Model41:
      type: string
      enum:
        - us-east-1
        - us-east-2
        - us-west-1
        - us-west-2
        - ca-central-1
        - sa-east-1
        - eu-west-1
        - eu-central-1
        - eu-west-2
        - eu-west-3
        - eu-north-1
        - eu-south-1
        - me-south-1
        - ap-southeast-1
        - ap-northeast-1
        - ap-east-1
        - ap-southeast-2
        - ap-southeast-3
        - ap-northeast-2
        - ap-northeast-3
        - ap-south-1
        - af-south-1
    HeaderList:
      type: array
      example:
        - key: Cache-Control
          value: no-store
      items:
        $ref: '#/components/schemas/KeyValue'
    QueryParameterList:
      type: array
      example:
        - key: Page
          value: '1'
      items:
        $ref: '#/components/schemas/KeyValue'
    AssertionList:
      type: array
      description: >-
        Check the main Checkly documentation on assertions for specific values
        like regular expressions and JSON path descriptors you can use in the
        "property" field.
      example:
        - source: STATUS_CODE
          comparison: NOT_EMPTY
          target: '200'
      items:
        $ref: '#/components/schemas/Assertion'
    BasicAuth:
      type: object
      nullable: true
      properties:
        username:
          type: string
          example: admin
          default: ''
        password:
          type: string
          example: abc12345
          default: ''
      required:
        - username
        - password
    EnvironmentVariableUpdate:
      type: object
      properties:
        key:
          type: string
          description: The key of the environment variable (this value cannot be changed).
          example: API_KEY
        value:
          type: string
          description: The value of the environment variable.
          example: bAxD7biGCZL6K60Q
        locked:
          type: boolean
          description: Used only in the UI to hide the value like a password.
          default: false
        secret:
          type: boolean
          description: >-
            Set an environment variable as secret. Once set, its value cannot be
            unlocked.
          default: false
      required:
        - value
    escalationType:
      type: string
      description: Determines what type of escalation to use.
      default: RUN_BASED
      enum:
        - RUN_BASED
        - TIME_BASED
    AlertSettingsReminders:
      type: object
      properties:
        amount:
          type: number
          description: How many reminders to send out after the initial alert notification.
          default: 0
          enum:
            - 0
            - 1
            - 2
            - 3
            - 4
            - 5
            - 100000
        interval:
          type: number
          description: At what interval the reminders should be send.
          default: 5
          enum:
            - 5
            - 10
            - 15
            - 30
    AlertSettingsSSLCertificates:
      type: object
      description: >-
        [DEPRECATED] `sslCertificates` is deprecated and is not longer used.
        Please ignore it, will be removed in a future version.
      properties:
        enabled:
          type: boolean
          description: >-
            Determines if alert notifications should be send for expiring SSL
            certificates.
        alertThreshold:
          type: integer
          description: At what moment in time to start alerting on SSL certificates.
    AlertSettingsRunBasedEscalation:
      type: object
      properties:
        failedRunThreshold:
          type: number
          description: >-
            After how many failed consecutive check runs an alert notification
            should be send.
          enum:
            - 1
            - 2
            - 3
            - 4
            - 5
    AlertSettingsTimeBasedEscalation:
      type: object
      properties:
        minutesFailingThreshold:
          type: number
          description: >-
            After how many minutes after a check starts failing an alert should
            be send.
          enum:
            - 5
            - 10
            - 15
            - 30
    parallelRunFailureThreshold:
      type: object
      properties:
        enabled:
          type: boolean
          description: Determines if parallel run threshold is enabled
          default: false
        percentage:
          type: number
          description: >-
            The percentage of parallel runs that should fail before an alert is
            triggered
          default: 10
          enum:
            - 10
            - 20
            - 30
            - 40
            - 50
            - 60
            - 70
            - 80
            - 90
            - 100
    Model40:
      type: object
      description: Alert channel subscription.
      properties:
        alertChannelId:
          type: number
        activated:
          type: boolean
          default: true
      required:
        - alertChannelId
        - activated
    Model39:
      type: string
      enum:
        - us-east-1
        - us-east-2
        - us-west-1
        - us-west-2
        - ca-central-1
        - sa-east-1
        - eu-west-1
        - eu-central-1
        - eu-west-2
        - eu-west-3
        - eu-north-1
        - eu-south-1
        - me-south-1
        - ap-southeast-1
        - ap-northeast-1
        - ap-east-1
        - ap-southeast-2
        - ap-southeast-3
        - ap-northeast-2
        - ap-northeast-3
        - ap-south-1
        - af-south-1
    EnvironmentVariableGet:
      type: object
      properties:
        key:
          type: string
          description: The key of the environment variable (this value cannot be changed).
          example: API_KEY
        value:
          type: string
        locked:
          type: boolean
          description: Used only in the UI to hide the value like a password.
          default: false
        secret:
          type: boolean
          description: >-
            Set an environment variable as secret. Once set, its value cannot be
            unlocked.
          default: false
      required:
        - key
        - value
    KeyValue:
      type: object
      properties:
        key:
          type: string
        value:
          type: string
          default: ''
        locked:
          type: boolean
          default: false
      required:
        - key
        - value
    Assertion:
      type: object
      properties:
        source:
          $ref: '#/components/schemas/AssertionSource'
        comparison:
          $ref: '#/components/schemas/AssertionComparison'
        property:
          type: string
          default: ''
        target:
          type: string
          default: ''
        regex:
          type: string
          default: ''
          nullable: true
    AssertionSource:
      type: string
      enum:
        - STATUS_CODE
        - JSON_BODY
        - HEADERS
        - TEXT_BODY
        - RESPONSE_TIME
    AssertionComparison:
      type: string
      enum:
        - EQUALS
        - NOT_EQUALS
        - HAS_KEY
        - NOT_HAS_KEY
        - HAS_VALUE
        - NOT_HAS_VALUE
        - IS_EMPTY
        - NOT_EMPTY
        - GREATER_THAN
        - LESS_THAN
        - CONTAINS
        - NOT_CONTAINS
        - IS_NULL
        - NOT_NULL
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer
      bearerFormat: Bearer
      description: >-
        The Checkly Public API uses API keys to authenticate requests. You can
        get the API Key
        [here](https://app.checklyhq.com/settings/user/api-keys). Your API key
        is like a password:  keep it secure!

        Authentication to the API is performed using the Bearer auth method in
        the Authorization header and using the account ID.

        For example, set **Authorization** header while using cURL: `curl -H
        "Authorization: Bearer [apiKey]" "X-Checkly-Account: [accountId]"` 

````

Built with [Mintlify](https://mintlify.com).