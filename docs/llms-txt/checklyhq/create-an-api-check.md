# Source: https://checklyhq.com/docs/api-reference/checks/create-an-api-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an API check

> Creates a new API check. Will return a `402` when you are over the limit of your plan.
    When using the `globalAlertSetting`, the `alertSetting` can be `null`



## OpenAPI

````yaml post /v1/checks/api
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
  /v1/checks/api:
    post:
      tags:
        - Checks
      summary: Create an API check
      description: >-
        Creates a new API check. Will return a `402` when you are over the limit
        of your plan.
            When using the `globalAlertSetting`, the `alertSetting` can be `null`
      operationId: postV1ChecksApi
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
              $ref: '#/components/schemas/CheckAPICreate'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckAPI'
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
components:
  schemas:
    CheckAPICreate:
      type: object
      properties:
        name:
          type: string
          description: The name of the check.
          example: Check
        activated:
          type: boolean
          description: Determines if the check is running or not.
          default: true
        muted:
          type: boolean
          description: >-
            Determines if any notifications will be send out when a check fails
            and/or recovers.
          default: false
        doubleCheck:
          type: boolean
          description: >-
            [Deprecated] Retry failed check runs. This property is deprecated,
            and `retryStrategy` can be used instead.
          default: true
        shouldFail:
          type: boolean
          description: >-
            Allows to invert the behaviour of when a check is considered to
            fail. Allows for validating error status like 404.
          default: false
        locations:
          $ref: '#/components/schemas/Model69'
        tags:
          $ref: '#/components/schemas/CheckTagList'
        alertSettings:
          $ref: '#/components/schemas/AlertSettings'
        useGlobalAlertSettings:
          type: boolean
          description: >-
            When true, the account level alert setting will be used, not the
            alert setting defined on this check.
          default: true
        groupId:
          type: number
          description: The id of the check group this check is part of.
          example: 'null'
          default: null
          nullable: true
        groupOrder:
          type: number
          description: >-
            The position of this check in a check group. It determines in what
            order checks are run when a group is triggered from the API or from
            CI/CD.
          example: 'null'
          default: null
          nullable: true
          minimum: 0
        runtimeId:
          $ref: '#/components/schemas/Model70'
        alertChannelSubscriptions:
          $ref: '#/components/schemas/Model71'
        retryStrategy:
          $ref: '#/components/schemas/RetryStrategy'
        triggerIncident:
          $ref: '#/components/schemas/TriggerIncident'
        runParallel:
          type: boolean
          description: When true, the check will run in parallel in all selected locations.
          default: false
        description:
          type: string
          description: A description of the check.
          default: null
          nullable: true
          maxLength: 500
        request:
          $ref: '#/components/schemas/Request'
        frequency:
          type: integer
          description: How often the check should run in minutes.
          default: 10
          enum:
            - 0
            - 1
            - 2
            - 5
            - 10
            - 15
            - 30
            - 60
            - 120
            - 180
            - 360
            - 720
            - 1440
        frequencyOffset:
          type: integer
          description: >-
            Used for setting seconds for check frequencies under 1 minutes (only
            for API & TCP checks) and spreading checks over a time range for
            frequencies over 1 minute. This works as follows: Checks with a
            frequency of 0 can have a frequencyOffset of 10, 20 or 30 meaning
            they will run every 10, 20 or 30 seconds. Checks with a frequency
            lower than and equal to 60 can have a frequencyOffset between 1 and
            a max value based on the formula "Math.floor(frequency * 10)", i.e.
            for a check that runs every 5 minutes the max frequencyOffset is 50.
            Checks with a frequency higher than 60 can have a frequencyOffset
            between 1 and a max value based on the formula "Math.ceil(frequency
            / 60)", i.e. for a check that runs every 720 minutes, the max
            frequencyOffset is 12. 
          minimum: 1
        degradedResponseTime:
          type: number
          description: >-
            The response time in milliseconds where a check should be considered
            degraded.
          default: 5000
          nullable: true
          minimum: 0
          maximum: 30000
        maxResponseTime:
          type: number
          description: >-
            The response time in milliseconds where a check should be considered
            failing.
          default: 20000
          nullable: true
          minimum: 0
          maximum: 30000
        privateLocations:
          $ref: '#/components/schemas/privateLocations'
        tearDownSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the teardown phase of an API
            check.
          example: 'null'
          default: null
          nullable: true
        setupSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the setup phase of an API
            check.
          example: 'null'
          default: null
          nullable: true
        localSetupScript:
          type: string
          description: A valid piece of Node.js code to run in the setup phase.
          example: ''
          default: null
          nullable: true
        localTearDownScript:
          type: string
          description: A valid piece of Node.js code to run in the teardown phase.
          example: ''
          default: null
          nullable: true
      required:
        - name
        - request
    CheckAPI:
      type: object
      properties:
        id:
          type: string
          example: 2739d22d-086f-481d-a484-8b93ac84de61
        name:
          type: string
          description: The name of the check.
          example: Check
        activated:
          type: boolean
          description: Determines if the check is running or not.
          default: true
        muted:
          type: boolean
          description: >-
            Determines if any notifications will be send out when a check fails
            and/or recovers.
          default: false
        doubleCheck:
          type: boolean
          description: >-
            [Deprecated] Retry failed check runs. This property is deprecated,
            and `retryStrategy` can be used instead.
          default: true
        shouldFail:
          type: boolean
          description: >-
            Allows to invert the behaviour of when a check is considered to
            fail. Allows for validating error status like 404.
          default: false
        locations:
          $ref: '#/components/schemas/Model75'
        tags:
          $ref: '#/components/schemas/CheckTagList'
        alertSettings:
          $ref: '#/components/schemas/CheckAlertSettings'
        useGlobalAlertSettings:
          type: boolean
          description: >-
            When true, the account level alert setting will be used, not the
            alert setting defined on this check.
          default: true
        groupId:
          type: number
          description: The id of the check group this check is part of.
          example: 'null'
          default: null
          nullable: true
        groupOrder:
          type: number
          description: >-
            The position of this check in a check group. It determines in what
            order checks are run when a group is triggered from the API or from
            CI/CD.
          example: 'null'
          default: null
          nullable: true
          minimum: 0
        runtimeId:
          $ref: '#/components/schemas/Model76'
        alertChannelSubscriptions:
          $ref: '#/components/schemas/CheckAlertChannelSubscriptionList'
        retryStrategy:
          $ref: '#/components/schemas/RetryStrategy'
        triggerIncident:
          $ref: '#/components/schemas/TriggerIncident'
        runParallel:
          type: boolean
          description: When true, the check will run in parallel in all selected locations.
          default: false
        description:
          type: string
          description: A description of the check.
          default: null
          nullable: true
          maxLength: 500
        frequency:
          type: integer
          description: How often the check should run in minutes.
          default: 10
          enum:
            - 0
            - 1
            - 2
            - 5
            - 10
            - 15
            - 30
            - 60
            - 120
            - 180
            - 360
            - 720
            - 1440
        frequencyOffset:
          type: integer
          description: >-
            Used for setting seconds for check frequencies under 1 minutes (only
            for API & TCP checks) and spreading checks over a time range for
            frequencies over 1 minute. This works as follows: Checks with a
            frequency of 0 can have a frequencyOffset of 10, 20 or 30 meaning
            they will run every 10, 20 or 30 seconds. Checks with a frequency
            lower than and equal to 60 can have a frequencyOffset between 1 and
            a max value based on the formula "Math.floor(frequency * 10)", i.e.
            for a check that runs every 5 minutes the max frequencyOffset is 50.
            Checks with a frequency higher than 60 can have a frequencyOffset
            between 1 and a max value based on the formula "Math.ceil(frequency
            / 60)", i.e. for a check that runs every 720 minutes, the max
            frequencyOffset is 12. 
          minimum: 1
        degradedResponseTime:
          type: number
          nullable: true
        maxResponseTime:
          type: number
          nullable: true
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date-time
          nullable: true
        alertChannels:
          $ref: '#/components/schemas/CheckAlertChannels'
        privateLocations:
          $ref: '#/components/schemas/privateLocations'
        request:
          $ref: '#/components/schemas/Model82'
        checkType:
          $ref: '#/components/schemas/Model83'
        tearDownSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the teardown phase of an API
            check.
          default: null
          nullable: true
        setupSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the setup phase of an API
            check.
          default: null
          nullable: true
        localSetupScript:
          type: string
          description: A valid piece of Node.js code to run in the setup phase.
          example: ''
          default: null
          nullable: true
        localTearDownScript:
          type: string
          description: A valid piece of Node.js code to run in the teardown phase.
          example: ''
          default: null
          nullable: true
      required:
        - name
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
    Model69:
      type: array
      description: An array of one or more data center locations where to run this check.
      example:
        - us-east-1
        - eu-central-1
      nullable: true
      items:
        $ref: '#/components/schemas/Model68'
    CheckTagList:
      type: array
      description: Tags for organizing and filtering checks.
      example:
        - production
      items:
        type: string
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
    Model70:
      type: string
      description: >-
        The runtime version, i.e. fixed set of runtime dependencies, used to
        execute this check.
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
    Model71:
      type: array
      description: List of alert channel subscriptions.
      example: []
      items:
        $ref: '#/components/schemas/Model40'
    RetryStrategy:
      type: object
      description: The strategy to determine how failed checks are retried.
      nullable: true
      properties:
        type:
          $ref: '#/components/schemas/RetryStrategyType'
        baseBackoffSeconds:
          type: number
          description: The number of seconds to wait before the first retry attempt.
          default: 60
        sameRegion:
          type: boolean
          description: >-
            Whether retries should be run in the same region as the initial
            check run.
          default: true
        maxRetries:
          type: number
          description: >-
            The maximum number of attempts to retry the check. Not supported for
            SINGLE_RETRY
          minimum: 1
          maximum: 10
        maxDurationSeconds:
          type: number
          description: >-
            The total amount of time to continue retrying the check. Not
            supported for SINGLE_RETRY
          minimum: 0
          maximum: 600
        onlyOn:
          $ref: '#/components/schemas/RetryOnlyOn'
      required:
        - type
    TriggerIncident:
      type: object
      description: >-
        Determines whether the check or monitor should create and resolve an
        incident based on its alert configuration. Useful for status page
        automation.
      nullable: true
      properties:
        serviceId:
          type: string
          description: The status page service that the incident will be associated with.
          x-format:
            guid: true
        severity:
          $ref: '#/components/schemas/severity'
        name:
          type: string
          description: The name of the incident.
        description:
          type: string
          description: A detailed description of the incident.
        notifySubscribers:
          type: boolean
          description: Whether to notify subscribers when the incident is triggered.
      required:
        - serviceId
        - severity
        - name
        - description
        - notifySubscribers
    Request:
      type: object
      description: Determines the request that the check is going to run.
      properties:
        method:
          $ref: '#/components/schemas/method'
        url:
          type: string
          default: https://api.checklyhq.com
          maxLength: 2048
        followRedirects:
          type: boolean
        skipSSL:
          type: boolean
          default: false
        ipFamily:
          $ref: '#/components/schemas/ipFamily'
        body:
          type: string
          default: ''
        bodyType:
          $ref: '#/components/schemas/bodyType'
        headers:
          $ref: '#/components/schemas/Model72'
        queryParameters:
          $ref: '#/components/schemas/Model73'
        assertions:
          $ref: '#/components/schemas/AssertionList'
        basicAuth:
          $ref: '#/components/schemas/BasicAuth'
      required:
        - method
        - url
    privateLocations:
      type: array
      description: An array of one or more private locations where to run the check.
      example:
        - data-center-eu
      nullable: true
      items:
        type: string
    Model75:
      type: array
      description: An array of one or more data center locations where to run this check.
      example:
        - us-east-1
        - eu-central-1
      nullable: true
      items:
        $ref: '#/components/schemas/Model74'
    CheckAlertSettings:
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
    Model76:
      type: string
      description: >-
        The runtime version, i.e. fixed set of runtime dependencies, used to
        execute this check.
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
    CheckAlertChannelSubscriptionList:
      type: array
      items:
        $ref: '#/components/schemas/CheckAlertChannelSubscription'
    CheckAlertChannels:
      type: object
      nullable: true
      properties:
        email:
          $ref: '#/components/schemas/CheckAlertEmailList'
        webhook:
          $ref: '#/components/schemas/CheckAlertWebhookList'
        slack:
          $ref: '#/components/schemas/CheckAlertSlackList'
        sms:
          $ref: '#/components/schemas/CheckAlertSMSList'
    Model82:
      type: object
      description: Determines the request that the check is going to run.
      properties:
        method:
          $ref: '#/components/schemas/method'
        url:
          type: string
          default: https://api.checklyhq.com
          maxLength: 2048
        followRedirects:
          type: boolean
        skipSSL:
          type: boolean
          default: false
        ipFamily:
          $ref: '#/components/schemas/ipFamily'
        body:
          type: string
          default: ''
        bodyType:
          $ref: '#/components/schemas/bodyType'
        headers:
          $ref: '#/components/schemas/Model80'
        queryParameters:
          $ref: '#/components/schemas/Model81'
        assertions:
          $ref: '#/components/schemas/AssertionList'
        basicAuth:
          $ref: '#/components/schemas/BasicAuth'
      required:
        - method
        - url
    Model83:
      type: string
      enum:
        - API
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
    Model68:
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
    RetryStrategyType:
      type: string
      description: Determines which type of retry strategy to use.
      enum:
        - FIXED
        - LINEAR
        - EXPONENTIAL
        - SINGLE_RETRY
    RetryOnlyOn:
      type: array
      x-constraint:
        length: 1
        unique: true
        single: true
      items:
        $ref: '#/components/schemas/RetryOnlyOnValue'
    severity:
      type: string
      description: The severity level of the incident.
      enum:
        - CRITICAL
        - MAJOR
        - MEDIUM
        - MINOR
    method:
      type: string
      default: GET
      enum:
        - GET
        - POST
        - PUT
        - HEAD
        - DELETE
        - PATCH
    ipFamily:
      type: string
      default: IPv4
      enum:
        - IPv4
        - IPv6
    bodyType:
      type: string
      default: NONE
      enum:
        - JSON
        - FORM
        - RAW
        - GRAPHQL
        - NONE
    Model72:
      type: array
      items:
        $ref: '#/components/schemas/KeyValue'
    Model73:
      type: array
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
    Model74:
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
    CheckAlertChannelSubscription:
      type: object
      properties:
        alertChannelId:
          type: number
        activated:
          type: boolean
          default: true
      required:
        - alertChannelId
        - activated
    CheckAlertEmailList:
      type: array
      items:
        $ref: '#/components/schemas/CheckAlertEmail'
    CheckAlertWebhookList:
      type: array
      items:
        $ref: '#/components/schemas/CheckAlertWebhook'
    CheckAlertSlackList:
      type: array
      items:
        $ref: '#/components/schemas/CheckAlertSlack'
    CheckAlertSMSList:
      type: array
      items:
        $ref: '#/components/schemas/CheckAlertSMS'
    Model80:
      type: array
      items:
        $ref: '#/components/schemas/KeyValue'
    Model81:
      type: array
      items:
        $ref: '#/components/schemas/KeyValue'
    RetryOnlyOnValue:
      type: string
      description: >-
        The HTTP request could not be completed due to a network error: no
        response status code was received
      enum:
        - NETWORK_ERROR
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
    CheckAlertEmail:
      type: object
      properties:
        address:
          type: string
          default: ''
      required:
        - address
    CheckAlertWebhook:
      type: object
      properties:
        name:
          type: string
          default: ''
        url:
          type: string
          default: ''
        method:
          $ref: '#/components/schemas/Model77'
        headers:
          $ref: '#/components/schemas/Model78'
        queryParameters:
          $ref: '#/components/schemas/Model79'
      required:
        - url
    CheckAlertSlack:
      type: object
      properties:
        url:
          type: string
          default: ''
      required:
        - url
    CheckAlertSMS:
      type: object
      properties:
        number:
          type: string
          example: '+549110000000'
          default: ''
        name:
          type: string
          example: SMS Alert
      required:
        - number
        - name
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
    Model77:
      type: string
      default: POST
      enum:
        - GET
        - POST
        - PUT
        - HEAD
        - DELETE
        - PATCH
      nullable: true
    Model78:
      type: array
      items:
        $ref: '#/components/schemas/KeyValue'
    Model79:
      type: array
      items:
        $ref: '#/components/schemas/KeyValue'
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