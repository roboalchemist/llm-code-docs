# Source: https://docs.datafold.com/api-reference/monitors/create-a-schema-change-monitor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Schema Change Monitor



## OpenAPI

````yaml openapi-public.json post /api/v1/monitors/create/schema
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
  /api/v1/monitors/create/schema:
    post:
      tags:
        - Monitors
      summary: Create a Schema Change Monitor
      operationId: create_monitor_schema_api_v1_monitors_create_schema_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SchemaChangeMonitorSpecPublic'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiPublicCreateMonitorOut'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    SchemaChangeMonitorSpecPublic:
      properties:
        connection_id:
          description: The identifier for the data source configuration.
          title: Connection Id
          type: integer
        description:
          anyOf:
            - type: string
            - type: 'null'
          description: The description of the monitor.
          title: Description
        enabled:
          default: true
          description: Indicates whether the monitor is enabled.
          title: Enabled
          type: boolean
        name:
          description: The name of the monitor.
          title: Name
          type: string
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
        table:
          anyOf:
            - type: string
            - type: 'null'
          description: The name of the table.
          title: Table
        tags:
          description: Tags associated with the monitor.
          items:
            type: string
          title: Tags
          type: array
      required:
        - schedule
        - name
        - connection_id
      title: SchemaChangeMonitorSpecPublic
      type: object
    ApiPublicCreateMonitorOut:
      properties:
        id:
          description: Unique identifier for the monitor.
          title: Id
          type: integer
      required:
        - id
      title: ApiPublicCreateMonitorOut
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