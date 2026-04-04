# Source: https://checklyhq.com/docs/api-reference/heartbeats/create-a-heartbeat-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a heartbeat monitor

> Creates a new Heartbeat check. Will return a `402` when you are over the limit of your plan.
    When using the `globalAlertSetting`, the `alertSetting` can be `null`



## OpenAPI

````yaml post /v1/checks/heartbeat
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
  /v1/checks/heartbeat:
    post:
      tags:
        - Heartbeats
      summary: Create a heartbeat check
      description: >-
        Creates a new Heartbeat check. Will return a `402` when you are over the
        limit of your plan.
            When using the `globalAlertSetting`, the `alertSetting` can be `null`
      operationId: postV1ChecksHeartbeat
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
              $ref: '#/components/schemas/CheckHeartbeatCreate'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckHeartbeat'
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
    CheckHeartbeatCreate:
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
          $ref: '#/components/schemas/Model116'
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
          $ref: '#/components/schemas/Model117'
        alertChannelSubscriptions:
          $ref: '#/components/schemas/Model118'
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
        frequencyOffset:
          type: integer
          minimum: 1
        request:
          $ref: '#/components/schemas/CheckRequest'
        heartbeat:
          $ref: '#/components/schemas/Model119'
        script:
          type: string
        scriptPath:
          type: string
          description: Path of the script in the runtime.
          nullable: true
        sslCheckDomain:
          type: string
        environmentVariables:
          $ref: '#/components/schemas/CheckEnvironmentVariableList'
        setupSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the setup phase of an API
            check.
          default: null
          nullable: true
        tearDownSnippetId:
          type: number
          description: >-
            An ID reference to a snippet to use in the teardown phase of an API
            check.
          default: null
          nullable: true
        localSetupScript:
          type: string
          description: A valid piece of Node.js code to run in the setup phase.
          default: null
          nullable: true
        localTearDownScript:
          type: string
          description: A valid piece of Node.js code to run in the teardown phase.
          default: null
          nullable: true
        degradedResponseTime:
          type: number
          description: >-
            The response time in milliseconds where a check should be considered
            degraded.
          default: 10000
          nullable: true
          minimum: 0
          maximum: 300000
        maxResponseTime:
          type: number
          description: >-
            The response time in milliseconds where a check should be considered
            failing.
          default: 20000
          nullable: true
          minimum: 0
          maximum: 300000
      required:
        - name
        - heartbeat
        - script
    CheckHeartbeat:
      type: object
      properties:
        id:
          type: string
          example: d432cf89-010b-4b12-8150-958c8eb1d5ca
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
        alertChannelSubscriptions:
          $ref: '#/components/schemas/CheckAlertChannelSubscriptionList'
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
        checkType:
          $ref: '#/components/schemas/Model120'
        heartbeat:
          $ref: '#/components/schemas/Model121'
        alertChannels:
          $ref: '#/components/schemas/CheckAlertChannels'
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date-time
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
    Model116:
      type: array
      description: An array of one or more data center locations where to run this check.
      example:
        - us-east-1
        - eu-central-1
      nullable: true
      items:
        $ref: '#/components/schemas/Model115'
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
    Model117:
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
    Model118:
      type: array
      description: List of alert channel subscriptions.
      example: []
      items:
        $ref: '#/components/schemas/Model40'
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
    CheckRequest:
      type: object
    Model119:
      type: object
      properties:
        period:
          type: number
          description: Interval expected between pings.
        periodUnit:
          $ref: '#/components/schemas/periodUnit'
        grace:
          type: number
          description: Grace added to the period.
        graceUnit:
          $ref: '#/components/schemas/graceUnit'
        pingToken:
          type: string
          description: UUID token used to build a unique ping URL.
          nullable: true
          x-format:
            guid: true
      required:
        - period
        - periodUnit
        - grace
        - graceUnit
    CheckEnvironmentVariableList:
      type: array
      description: >-
        Key/value pairs for setting environment variables during check
        execution. These are only relevant for Browser checks. Use global
        environment variables whenever possible.
      nullable: true
      maxItems: 50
      items:
        $ref: '#/components/schemas/EnvironmentVariable'
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
    CheckAlertChannelSubscriptionList:
      type: array
      items:
        $ref: '#/components/schemas/CheckAlertChannelSubscription'
    Model120:
      type: string
      enum:
        - HEARTBEAT
    Model121:
      type: object
      properties:
        period:
          type: number
          description: Interval expected between pings.
        periodUnit:
          $ref: '#/components/schemas/periodUnit'
        grace:
          type: number
          description: Grace added to the period.
        graceUnit:
          $ref: '#/components/schemas/graceUnit'
        pingToken:
          type: string
          description: UUID token used to build a unique ping URL.
          nullable: true
          x-format:
            guid: true
        pingUrl:
          type: string
          example: https://ping.checklyhq.com/22868839-8450-4010-9241-1ea83a2e425f
      required:
        - period
        - periodUnit
        - grace
        - graceUnit
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
    Model115:
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
    severity:
      type: string
      description: The severity level of the incident.
      enum:
        - CRITICAL
        - MAJOR
        - MEDIUM
        - MINOR
    periodUnit:
      type: string
      enum:
        - seconds
        - minutes
        - hours
        - days
    graceUnit:
      type: string
      enum:
        - seconds
        - minutes
        - hours
        - days
    EnvironmentVariable:
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