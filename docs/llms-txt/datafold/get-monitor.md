# Source: https://docs.datafold.com/api-reference/monitors/get-monitor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Monitor



## OpenAPI

````yaml openapi-public.json get /api/v1/monitors/{id}
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/monitors/{id}:
    get:
      tags:
        - Monitors
      summary: Get Monitor
      operationId: get_monitor_api_v1_monitors__id__get
      parameters:
        - description: The unique identifier of the monitor.
          in: path
          name: id
          required: true
          schema:
            description: The unique identifier of the monitor.
            title: Id
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiPublicGetMonitorOutFull'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiPublicGetMonitorOutFull:
      properties:
        alert:
          anyOf:
            - discriminator:
                mapping:
                  absolute: '#/components/schemas/AbsoluteThreshold'
                  automatic: '#/components/schemas/AnomalyDetectionThreshold'
                  diff: >-
                    #/components/schemas/datafold__api__v1__monitors__DiffAlertCondition
                  percentage: '#/components/schemas/PercentageThreshold'
                propertyName: type
              oneOf:
                - $ref: >-
                    #/components/schemas/datafold__api__v1__monitors__DiffAlertCondition
                - $ref: '#/components/schemas/AnomalyDetectionThreshold'
                - $ref: '#/components/schemas/AbsoluteThreshold'
                - $ref: '#/components/schemas/PercentageThreshold'
            - type: 'null'
          description: Condition for triggering alerts based on the data diff.
        created_at:
          description: Timestamp when the monitor was created.
          format: date-time
          title: Created At
          type: string
        dataset:
          description: Dataset configuration for the monitor.
          items:
            $ref: '#/components/schemas/MonitorDataset'
          title: Dataset
          type: array
        description:
          anyOf:
            - type: string
            - type: 'null'
          description: The description of the monitor.
          title: Description
        enabled:
          description: Indicates whether the monitor is enabled.
          title: Enabled
          type: boolean
        id:
          description: Unique identifier for the monitor.
          title: Id
          type: integer
        last_alert:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          description: Timestamp of the last alert.
          title: Last Alert
        last_run:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          description: Timestamp of the last monitor run.
          title: Last Run
        modified_at:
          description: Timestamp when the monitor was last modified.
          format: date-time
          title: Modified At
          type: string
        monitor_type:
          anyOf:
            - enum:
                - diff
                - metric
                - schema
                - test
              type: string
            - type: 'null'
          description: Type of the monitor.
          title: Monitor Type
        name:
          anyOf:
            - type: string
            - type: 'null'
          description: Name of the monitor.
          title: Name
        notifications:
          description: Notification configuration for the monitor.
          items:
            discriminator:
              mapping:
                email: '#/components/schemas/EmailNotification'
                pagerduty: '#/components/schemas/PagerDutyNotification'
                slack: '#/components/schemas/SlackNotification'
                teams: '#/components/schemas/TeamsNotification'
                webhook: '#/components/schemas/WebhookNotification'
              propertyName: type
            oneOf:
              - $ref: '#/components/schemas/EmailNotification'
              - $ref: '#/components/schemas/PagerDutyNotification'
              - $ref: '#/components/schemas/WebhookNotification'
              - $ref: '#/components/schemas/SlackNotification'
              - $ref: '#/components/schemas/TeamsNotification'
          title: Notifications
          type: array
        schedule:
          anyOf:
            - $ref: '#/components/schemas/IntervalSchedule'
            - $ref: '#/components/schemas/CronSchedule'
            - $ref: '#/components/schemas/NoneSchedule'
          description: The schedule at which the monitor runs.
        state:
          anyOf:
            - $ref: '#/components/schemas/MonitorRunState'
            - type: 'null'
          description: Current state of the monitor run.
        tags:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          description: Tags associated with the monitor.
          title: Tags
      required:
        - id
        - name
        - monitor_type
        - created_at
        - modified_at
        - enabled
        - schedule
      title: ApiPublicGetMonitorOutFull
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
    datafold__api__v1__monitors__DiffAlertCondition:
      properties:
        different_rows_count:
          anyOf:
            - type: integer
            - type: 'null'
          description: >-
            Threshold for the number of different rows allowed between the
            datasets.
          title: Different Rows Count
        different_rows_percent:
          anyOf:
            - type: integer
            - type: 'null'
          description: >-
            Threshold for the percentage of different rows allowed between the
            datasets.
          title: Different Rows Percent
        type:
          const: diff
          title: Type
          type: string
      required:
        - type
      title: Diff Conditions
      type: object
    AnomalyDetectionThreshold:
      properties:
        sensitivity:
          description: Sensitivity level for anomaly detection, ranging from 0 to 100.
          maximum: 100
          minimum: 0
          title: Sensitivity
          type: integer
        type:
          const: automatic
          title: Type
          type: string
      required:
        - type
        - sensitivity
      title: Anomaly Detection
      type: object
    AbsoluteThreshold:
      properties:
        max:
          anyOf:
            - type: number
            - type: 'null'
          description: Maximum value for the absolute threshold.
          title: Max
        min:
          anyOf:
            - type: number
            - type: 'null'
          description: Minimum value for the absolute threshold.
          title: Min
        type:
          const: absolute
          title: Type
          type: string
      required:
        - type
      title: Absolute
      type: object
    PercentageThreshold:
      properties:
        decrease:
          anyOf:
            - type: number
            - type: integer
            - type: 'null'
          description: Threshold for allowable percentage decrease.
          title: Decrease
        increase:
          anyOf:
            - type: number
            - type: integer
            - type: 'null'
          description: Threshold for allowable percentage increase.
          title: Increase
        type:
          const: percentage
          title: Type
          type: string
      required:
        - type
      title: Percentage
      type: object
    MonitorDataset:
      properties:
        column:
          anyOf:
            - type: string
            - type: 'null'
          description: The column of the table.
          title: Column
        connection_id:
          description: The identifier for the data source configuration.
          title: Connection Id
          type: integer
        filter:
          anyOf:
            - type: string
            - type: 'null'
          description: Filter condition being evaluated.
          title: Filter
        metric:
          anyOf:
            - type: string
            - type: 'null'
          description: The column metric configuration.
          title: Metric
        query:
          anyOf:
            - type: string
            - type: 'null'
          description: The SQL query being evaluated.
          title: Query
        table:
          anyOf:
            - type: string
            - type: 'null'
          description: The name of the table.
          title: Table
      required:
        - connection_id
      title: MonitorDataset
      type: object
    EmailNotification:
      properties:
        features:
          anyOf:
            - items:
                $ref: '#/components/schemas/DestinationFeatures'
              type: array
            - type: 'null'
          description: A list of features to enable for this notification.
          title: Features
        recipients:
          description: A list of email addresses to receive the notification.
          items:
            type: string
          title: Recipients
          type: array
        type:
          const: email
          default: email
          title: Type
          type: string
      required:
        - recipients
      title: Email
      type: object
    PagerDutyNotification:
      properties:
        features:
          anyOf:
            - items:
                $ref: '#/components/schemas/DestinationFeatures'
              type: array
            - type: 'null'
          description: A list of features to enable for this notification.
          title: Features
        integration:
          description: The identifier for the integration.
          title: Integration
          type: integer
        type:
          const: pagerduty
          default: pagerduty
          title: Type
          type: string
      required:
        - integration
      title: PagerDuty
      type: object
    WebhookNotification:
      properties:
        features:
          anyOf:
            - items:
                $ref: '#/components/schemas/DestinationFeatures'
              type: array
            - type: 'null'
          description: A list of features to enable for this notification.
          title: Features
        integration:
          description: The identifier for the integration.
          title: Integration
          type: integer
        type:
          const: webhook
          default: webhook
          title: Type
          type: string
      required:
        - integration
      title: Webhook
      type: object
    SlackNotification:
      properties:
        channel:
          description: The channel through which the notification will be sent.
          title: Channel
          type: string
        features:
          anyOf:
            - items:
                $ref: '#/components/schemas/DestinationFeatures'
              type: array
            - type: 'null'
          description: A list of features to enable for this notification.
          title: Features
        integration:
          description: The identifier for the integration.
          title: Integration
          type: integer
        mentions:
          description: A list of mentions to include in the notification.
          items:
            type: string
          title: Mentions
          type: array
        type:
          const: slack
          default: slack
          title: Type
          type: string
      required:
        - integration
        - channel
      title: Slack
      type: object
    TeamsNotification:
      properties:
        channel:
          description: The channel through which the notification will be sent.
          title: Channel
          type: string
        features:
          anyOf:
            - items:
                $ref: '#/components/schemas/DestinationFeatures'
              type: array
            - type: 'null'
          description: A list of features to enable for this notification.
          title: Features
        integration:
          description: The identifier for the integration.
          title: Integration
          type: integer
        mentions:
          description: A list of mentions names to include in the notification.
          items:
            type: string
          title: Mentions
          type: array
        type:
          const: teams
          default: teams
          title: Type
          type: string
      required:
        - integration
        - channel
      title: Teams
      type: object
    IntervalSchedule:
      properties:
        interval:
          anyOf:
            - $ref: '#/components/schemas/HourIntervalSchedule'
            - $ref: '#/components/schemas/DayIntervalSchedule'
          description: Specifies the scheduling interval.
      required:
        - interval
      title: Interval
      type: object
    CronSchedule:
      properties:
        cron:
          description: The cron expression that defines the schedule.
          title: Cron
          type: string
        type:
          const: crontab
          default: crontab
          title: Type
          type: string
      required:
        - cron
      title: Cron
      type: object
    NoneSchedule:
      properties:
        type:
          const: none
          default: none
          title: Type
          type: string
      title: None
      type: object
    MonitorRunState:
      enum:
        - ok
        - alert
        - error
        - learning
        - checking
        - created
        - skipped
        - cancelled
      title: MonitorRunState
      type: string
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object
    DestinationFeatures:
      enum:
        - attach_csv
        - notify_first_triggered_only
        - disable_recovery_notifications
        - notify_every_run
      title: DestinationFeatures
      type: string
    HourIntervalSchedule:
      properties:
        every:
          const: hour
          title: Every
          type: string
        type:
          const: hourly
          default: hourly
          title: Type
          type: string
      required:
        - every
      title: Hour
      type: object
    DayIntervalSchedule:
      properties:
        every:
          const: day
          title: Every
          type: string
        hour:
          anyOf:
            - type: integer
            - type: 'null'
          description: The hour at which the monitor should trigger. (0 - 23)
          title: Hour
        type:
          const: daily
          default: daily
          title: Type
          type: string
        utc_at:
          anyOf:
            - format: time
              type: string
            - type: 'null'
          description: The UTC time at which the monitor should trigger.
          title: Utc At
      required:
        - every
      title: Day
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````