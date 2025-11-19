# Source: https://docs.datafold.com/api-reference/monitors/update-a-monitor.md

# Update a Monitor

## OpenAPI

````yaml openapi-public.json patch /api/v1/monitors/{id}/update
paths:
  path: /api/v1/monitors/{id}/update
  method: patch
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
      path:
        id:
          schema:
            - type: integer
              required: true
              title: Id
              description: The unique identifier of the monitor.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              alert:
                allOf:
                  - anyOf:
                      - $ref: >-
                          #/components/schemas/datafold__monitors__schemas__DiffAlertCondition
                      - type: 'null'
                    description: Condition for triggering alerts based on the data diff.
              datadiff:
                allOf:
                  - anyOf:
                      - discriminator:
                          mapping:
                            indb: '#/components/schemas/InDbUpdateDataDiffConfig'
                            inmem: '#/components/schemas/InMemUpdateDataDiffConfig'
                          propertyName: diff_type
                        oneOf:
                          - $ref: '#/components/schemas/InDbUpdateDataDiffConfig'
                          - $ref: '#/components/schemas/InMemUpdateDataDiffConfig'
                      - type: 'null'
                    description: Configuration for the data diff.
              description:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The description of the monitor.
                    title: Description
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The name of the monitor.
                    title: Name
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
              schedule:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/IntervalSchedule'
                      - $ref: '#/components/schemas/CronSchedule'
                      - $ref: '#/components/schemas/NoneSchedule'
                      - type: 'null'
                    description: The schedule at which the monitor runs.
              tags:
                allOf:
                  - description: Tags associated with the monitor.
                    items:
                      type: string
                    title: Tags
                    type: array
              type:
                allOf:
                  - const: diff
                    description: The type of monitor.
                    title: Type
                    type: string
            required: true
            title: Diff
            refIdentifier: '#/components/schemas/DataDiffUpdateMonitorSpecPublic'
            requiredProperties:
              - type
          - type: object
            properties:
              alert:
                allOf:
                  - anyOf:
                      - discriminator:
                          mapping:
                            absolute: '#/components/schemas/AbsoluteThreshold'
                            automatic: '#/components/schemas/AnomalyDetectionThreshold'
                            percentage: '#/components/schemas/PercentageThreshold'
                          propertyName: type
                        oneOf:
                          - $ref: '#/components/schemas/AnomalyDetectionThreshold'
                          - $ref: '#/components/schemas/AbsoluteThreshold'
                          - $ref: '#/components/schemas/PercentageThreshold'
                      - type: 'null'
                    description: Condition for triggering alerts.
              description:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The description of the monitor.
                    title: Description
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The name of the monitor.
                    title: Name
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
              schedule:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/IntervalSchedule'
                      - $ref: '#/components/schemas/CronSchedule'
                      - $ref: '#/components/schemas/NoneSchedule'
                      - type: 'null'
                    description: The schedule at which the monitor runs.
              tags:
                allOf:
                  - description: Tags associated with the monitor.
                    items:
                      type: string
                    title: Tags
                    type: array
              type:
                allOf:
                  - const: metric
                    description: The type of monitor.
                    title: Type
                    type: string
            required: true
            title: Metric
            refIdentifier: '#/components/schemas/MetricUpdateMonitorSpecPublic'
            requiredProperties:
              - type
          - type: object
            properties:
              description:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The description of the monitor.
                    title: Description
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The name of the monitor.
                    title: Name
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
              schedule:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/IntervalSchedule'
                      - $ref: '#/components/schemas/CronSchedule'
                      - $ref: '#/components/schemas/NoneSchedule'
                      - type: 'null'
                    description: The schedule at which the monitor runs.
              tags:
                allOf:
                  - description: Tags associated with the monitor.
                    items:
                      type: string
                    title: Tags
                    type: array
              type:
                allOf:
                  - const: schema
                    description: The type of monitor.
                    title: Type
                    type: string
            required: true
            title: Schema
            refIdentifier: '#/components/schemas/SchemaChangeUpdateMonitorSpecPublic'
            requiredProperties:
              - type
          - type: object
            properties:
              description:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The description of the monitor.
                    title: Description
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The name of the monitor.
                    title: Name
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
                      - type: 'null'
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
              type:
                allOf:
                  - const: test
                    description: The type of monitor.
                    title: Type
                    type: string
            required: true
            title: Data
            refIdentifier: '#/components/schemas/DataTestUpdateMonitorSpecPublic'
            requiredProperties:
              - type
        examples:
          example:
            value:
              alert:
                different_rows_count: 123
                different_rows_percent: 123
              datadiff:
                column_remapping: {}
                columns_to_compare:
                  - <string>
                ignore_string_case: true
                materialize_results: true
                primary_key:
                  - <string>
                sampling:
                  confidence: 123
                  threshold: 123
                  tolerance: 123
                timeseries_dimension_column: <string>
                tolerance:
                  float:
                    column_tolerance: {}
                    default: {}
              description: <string>
              name: <string>
              notifications:
                - features:
                    - attach_csv
                  recipients:
                    - <string>
                  type: email
              schedule:
                interval:
                  every: <string>
                  type: <string>
              tags:
                - <string>
              type: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
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
    AbsoluteColumnTolerance:
      properties:
        type:
          const: absolute
          default: absolute
          description: The type of Column Tolerance.
          title: Type
          type: string
        value:
          description: Value of Column Tolerance.
          title: Value
          type: number
      required:
        - value
      title: Absolute
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
    ColumnToleranceConfig:
      properties:
        column_tolerance:
          anyOf:
            - additionalProperties:
                discriminator:
                  mapping:
                    absolute: '#/components/schemas/AbsoluteColumnTolerance'
                    relative: '#/components/schemas/RelativeColumnTolerance'
                  propertyName: type
                oneOf:
                  - $ref: '#/components/schemas/RelativeColumnTolerance'
                  - $ref: '#/components/schemas/AbsoluteColumnTolerance'
              type: object
            - type: 'null'
          description: Specific tolerance per column.
          title: Column Tolerance
        default:
          anyOf:
            - discriminator:
                mapping:
                  absolute: '#/components/schemas/AbsoluteColumnTolerance'
                  relative: '#/components/schemas/RelativeColumnTolerance'
                propertyName: type
              oneOf:
                - $ref: '#/components/schemas/RelativeColumnTolerance'
                - $ref: '#/components/schemas/AbsoluteColumnTolerance'
            - type: 'null'
          description: Default tolerance applied to all columns.
          title: Default
      title: ColumnToleranceConfig
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
    DataDiffToleranceConfig:
      properties:
        float:
          anyOf:
            - $ref: '#/components/schemas/ColumnToleranceConfig'
            - type: 'null'
          description: Configuration for float columns tolerance.
      title: DataDiffToleranceConfig
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
    InDbUpdateDataDiffConfig:
      properties:
        column_remapping:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          description: Mapping of columns from one dataset to another for comparison.
          title: Column Remapping
        columns_to_compare:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          description: Optional list of columns to compare between the datasets.
          title: Columns To Compare
        ignore_string_case:
          anyOf:
            - type: boolean
            - type: 'null'
          description: Indicates whether to ignore case differences in string comparisons.
          title: Ignore String Case
        materialize_results:
          anyOf:
            - type: boolean
            - type: 'null'
          description: Indicates whether to materialize the results of the comparison.
          title: Materialize Results
        primary_key:
          description: List of columns that make up the primary key for the datasets.
          items:
            type: string
          title: Primary Key
          type: array
        sampling:
          anyOf:
            - $ref: '#/components/schemas/ToleranceBasedSampling'
            - $ref: '#/components/schemas/PercentageSampling'
            - type: 'null'
          description: Sampling configuration for the data comparison.
        timeseries_dimension_column:
          anyOf:
            - type: string
            - type: 'null'
          description: Column used for time series dimensioning in the comparison.
          title: Timeseries Dimension Column
        tolerance:
          anyOf:
            - $ref: '#/components/schemas/DataDiffToleranceConfig'
            - type: 'null'
          description: Configuration for tolerance applied to FLOAT columns.
      title: In-Database
      type: object
    InMemUpdateDataDiffConfig:
      properties:
        column_remapping:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          description: Mapping of columns from one dataset to another for comparison.
          title: Column Remapping
        columns_to_compare:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          description: Optional list of columns to compare between the datasets.
          title: Columns To Compare
        ignore_string_case:
          default: false
          description: Indicates whether to ignore case differences in string comparisons.
          title: Ignore String Case
          type: boolean
        materialize_results:
          anyOf:
            - type: boolean
            - type: 'null'
          description: Indicates whether to materialize the results of the comparison.
          title: Materialize Results
        materialize_results_to:
          anyOf:
            - type: integer
            - type: 'null'
          description: Identifier for the destination where results should be materialized.
          title: Materialize Results To
        primary_key:
          description: List of columns that make up the primary key for the datasets.
          items:
            type: string
          title: Primary Key
          type: array
        sampling:
          anyOf:
            - $ref: '#/components/schemas/ToleranceBasedSampling'
            - $ref: '#/components/schemas/PercentageSampling'
            - type: 'null'
          description: Sampling configuration for the data comparison.
          title: Sampling
        tolerance:
          anyOf:
            - $ref: '#/components/schemas/DataDiffToleranceConfig'
            - type: 'null'
          description: Configuration for tolerance.
      title: In-Memory
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
    PercentageSampling:
      properties:
        rate:
          description: The sampling rate as a percentage.
          title: Rate
          type: number
        threshold:
          anyOf:
            - type: integer
            - type: 'null'
          description: Threshold for triggering actions based on sampling.
          title: Threshold
      required:
        - rate
      title: Percentage
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
    RelativeColumnTolerance:
      properties:
        type:
          const: relative
          default: relative
          description: The type of Column Tolerance.
          title: Type
          type: string
        value:
          anyOf:
            - type: number
            - type: integer
          description: Value of Column Tolerance.
          title: Value
      required:
        - value
      title: Relative
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
    ToleranceBasedSampling:
      properties:
        confidence:
          description: The confidence level for the sampling results.
          title: Confidence
          type: number
        threshold:
          anyOf:
            - type: integer
            - type: 'null'
          description: Threshold for triggering actions based on sampling.
          title: Threshold
        tolerance:
          description: The allowable margin of error for sampling.
          title: Tolerance
          type: number
      required:
        - tolerance
        - confidence
      title: Tolerance
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
    datafold__monitors__schemas__DiffAlertCondition:
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
      title: Diff Conditions
      type: object

````