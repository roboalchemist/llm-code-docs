# Source: https://docs.datafold.com/api-reference/monitors/create-a-data-test-monitor.md

# Create a Data Test Monitor

## OpenAPI

````yaml openapi-public.json post /api/v1/monitors/create/test
paths:
  path: /api/v1/monitors/create/test
  method: post
  servers:
    - url: https://app.datafold.com
      description: Default server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: Use the 'Authorization' header with the format 'Key <api-key>'
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              connection_id:
                allOf:
                  - description: The identifier for the data source configuration.
                    title: Connection Id
                    type: integer
              description:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The description of the monitor.
                    title: Description
              enabled:
                allOf:
                  - default: true
                    description: Indicates whether the monitor is enabled.
                    title: Enabled
                    type: boolean
              name:
                allOf:
                  - description: The name of the monitor.
                    title: Name
                    type: string
              notifications:
                allOf:
                  - description: Notification configuration for the monitor.
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
              query:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The SQL query to be evaluated.
                    title: Query
              schedule:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/IntervalSchedule'
                      - $ref: '#/components/schemas/CronSchedule'
                      - $ref: '#/components/schemas/NoneSchedule'
                    description: The schedule at which the monitor runs.
              tags:
                allOf:
                  - description: Tags associated with the monitor.
                    items:
                      type: string
                    title: Tags
                    type: array
              test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/StandardDataTestMonitorSpec'
                      - type: 'null'
            required: true
            title: DataTestMonitorSpecPublic
            refIdentifier: '#/components/schemas/DataTestMonitorSpecPublic'
            requiredProperties:
              - schedule
              - name
              - connection_id
        examples:
          example:
            value:
              connection_id: 123
              description: <string>
              enabled: true
              name: <string>
              notifications:
                - features:
                    - attach_csv
                  recipients:
                    - <string>
                  type: email
              query: <string>
              schedule:
                interval:
                  every: <string>
                  type: hourly
              tags:
                - <string>
              test:
                tables:
                  - columns:
                      - <string>
                    path: <string>
                type: unique
                variables: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - description: Unique identifier for the monitor.
                    title: Id
                    type: integer
            title: ApiPublicCreateMonitorOut
            refIdentifier: '#/components/schemas/ApiPublicCreateMonitorOut'
            requiredProperties:
              - id
        examples:
          example:
            value:
              id: 123
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    title: Detail
                    type: array
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
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
    DestinationFeatures:
      enum:
        - attach_csv
        - notify_first_triggered_only
        - disable_recovery_notifications
        - notify_every_run
      title: DestinationFeatures
      type: string
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
    NoneSchedule:
      properties:
        type:
          const: none
          default: none
          title: Type
          type: string
      title: None
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
    SDTTable:
      properties:
        columns:
          items:
            type: string
          title: Columns
          type: array
        path:
          title: Path
          type: string
      required:
        - path
        - columns
      title: SDTTable
      type: object
    SDTVariable:
      properties:
        quote:
          default: true
          title: Quote
          type: boolean
        value:
          anyOf:
            - type: string
            - type: integer
            - type: number
            - items:
                type: string
              type: array
            - items:
                type: integer
              type: array
            - items:
                type: number
              type: array
            - items:
                anyOf:
                  - type: string
                  - type: integer
                  - type: number
              type: array
          title: Value
      required:
        - value
      title: SDTVariable
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
    StandardDataTestMonitorSpec:
      properties:
        tables:
          anyOf:
            - items:
                $ref: '#/components/schemas/SDTTable'
              type: array
            - type: 'null'
          title: Tables
        type:
          $ref: '#/components/schemas/StandardDataTestTypes'
        variables:
          anyOf:
            - additionalProperties:
                $ref: '#/components/schemas/SDTVariable'
              type: object
            - type: 'null'
          title: Variables
      required:
        - type
      title: Standard DT
      type: object
    StandardDataTestTypes:
      enum:
        - unique
        - not_null
        - accepted_values
        - referential_integrity
        - numeric_range
        - custom_template
      title: StandardDataTestTypes
      type: string
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

````