# Source: https://checklyhq.com/docs/api-reference/checks/update-an-tcp-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a TCP monitor

> Updates an TCP check.



## OpenAPI

````yaml put /v1/checks/tcp/{id}
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
  /v1/checks/tcp/{id}:
    put:
      tags:
        - Checks
      summary: Update an TCP check
      description: Updates an TCP check.
      operationId: putV1ChecksTcpId
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
        - name: id
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
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
              $ref: '#/components/schemas/CheckTCPUpdate'
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckTCP'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
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
    CheckTCPUpdate:
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
          $ref: '#/components/schemas/Model183'
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
          $ref: '#/components/schemas/Model184'
        alertChannelSubscriptions:
          $ref: '#/components/schemas/Model185'
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
          $ref: '#/components/schemas/Model187'
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
          default: 3000
          nullable: true
          minimum: 0
          maximum: 5000
        maxResponseTime:
          type: number
          description: >-
            The response time in milliseconds where a check should be considered
            failing.
          default: 5000
          nullable: true
          minimum: 0
          maximum: 5000
        privateLocations:
          $ref: '#/components/schemas/privateLocations'
    CheckTCP:
      type: object
      properties:
        id:
          type: string
          example: 9d6df684-0bc3-4a38-a094-4e97627dd93e
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
          $ref: '#/components/schemas/Model177'
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
          $ref: '#/components/schemas/Model178'
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
          $ref: '#/components/schemas/Model180'
        checkType:
          $ref: '#/components/schemas/Model181'
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
    Model183:
      type: array
      description: An array of one or more data center locations where to run this check.
      example:
        - us-east-1
        - eu-central-1
      nullable: true
      items:
        $ref: '#/components/schemas/Model182'
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
    Model184:
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
    Model185:
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
    Model187:
      type: object
      properties:
        hostname:
          type: string
          maxLength: 2048
        port:
          type: number
        data:
          type: string
          default: null
          nullable: true
        assertions:
          $ref: '#/components/schemas/Model186'
        ipFamily:
          $ref: '#/components/schemas/ipFamily'
      required:
        - port
    privateLocations:
      type: array
      description: An array of one or more private locations where to run the check.
      example:
        - data-center-eu
      nullable: true
      items:
        type: string
    Model177:
      type: array
      description: An array of one or more data center locations where to run this check.
      example:
        - us-east-1
        - eu-central-1
      nullable: true
      items:
        $ref: '#/components/schemas/Model176'
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
    Model178:
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
    Model180:
      type: object
      properties:
        hostname:
          type: string
          maxLength: 2048
        port:
          type: number
        data:
          type: string
          default: null
          nullable: true
        assertions:
          $ref: '#/components/schemas/Model179'
        ipFamily:
          $ref: '#/components/schemas/ipFamily'
      required:
        - port
    Model181:
      type: string
      enum:
        - TCP
    error:
      type: string
      enum:
        - Unauthorized
    attributes:
      type: object
    Model1:
      type: string
      enum:
        - Forbidden
    Model2:
      type: string
      enum:
        - Too Many Requests
    Model182:
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
    Model186:
      type: array
      description: >-
        Check the main Checkly documentation on assertions for specific values
        like regular expressions and JSON path descriptors you can use in the
        "property" field.
      example:
        - source: TEXT_BODY
          comparison: NOT_EMPTY
          target: '200'
      items:
        $ref: '#/components/schemas/TcpCheckAssertion'
    ipFamily:
      type: string
      default: IPv4
      enum:
        - IPv4
        - IPv6
    Model176:
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
    Model179:
      type: array
      description: >-
        Check the main Checkly documentation on assertions for specific values
        like regular expressions and JSON path descriptors you can use in the
        "property" field.
      example:
        - source: TEXT_BODY
          comparison: NOT_EMPTY
          target: '200'
      items:
        $ref: '#/components/schemas/TcpCheckAssertion'
    RetryOnlyOnValue:
      type: string
      description: >-
        The HTTP request could not be completed due to a network error: no
        response status code was received
      enum:
        - NETWORK_ERROR
    TcpCheckAssertion:
      type: object
      properties:
        source:
          $ref: '#/components/schemas/Model173'
        comparison:
          type: string
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
    Model173:
      type: string
      enum:
        - RESPONSE_DATA
        - RESPONSE_TIME
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