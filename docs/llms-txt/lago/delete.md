# Source: https://getlago.com/docs/api-reference/customers/delete.md

# Source: https://getlago.com/docs/api-reference/alerts/delete.md

# Source: https://getlago.com/docs/api-reference/customers/delete.md

# Source: https://getlago.com/docs/api-reference/alerts/delete.md

# Source: https://getlago.com/docs/api-reference/customers/delete.md

# Source: https://getlago.com/docs/api-reference/alerts/delete.md

# Source: https://getlago.com/docs/api-reference/customers/delete.md

# Source: https://getlago.com/docs/api-reference/alerts/delete.md

# Delete an alert

> This endpoint allows you to delete an existing alert for a subscription.

## OpenAPI

````yaml DELETE /subscriptions/{external_id}/alerts/{code}
paths:
  path: /subscriptions/{external_id}/alerts/{code}
  method: delete
  servers:
    - url: https://api.getlago.com/api/v1
      description: US Lago cluster
    - url: https://api.eu.getlago.com/api/v1
      description: EU Lago cluster
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        external_id:
          schema:
            - type: string
              required: true
              description: External ID of the existing subscription
              example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        code:
          schema:
            - type: string
              required: true
              description: Unique code of the alert
              example: storage_threshold_alert
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              alert:
                allOf:
                  - $ref: '#/components/schemas/AlertObject'
            refIdentifier: '#/components/schemas/Alert'
            requiredProperties:
              - alert
        examples:
          example:
            value:
              alert:
                lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                lago_organization_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                subscription_external_id: sub_1234567890
                customer_external_id: cus_0987654321
                billable_metric:
                  lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  name: Storage
                  code: storage
                  description: GB of storage used in my application
                  recurring: false
                  rounding_function: round
                  rounding_precision: 2
                  created_at: '2022-09-14T16:35:31Z'
                  expression: round((ended_at - started_at) * units)
                  field_name: gb
                  aggregation_type: sum_agg
                  weighted_interval: seconds
                  filters:
                    - key: region
                      values:
                        - us-east-1
                alert_type: billable_metric_current_usage_amount
                code: storage_threshold_alert
                name: Storage Usage Alert
                previous_value: 1000
                last_processed_at: '2025-05-19T10:04:21Z'
                thresholds:
                  - code: warn
                    recurring: false
                    value: '99.0'
                created_at: '2025-03-20T10:00:00Z'
        description: Subscription alert deleted
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 401
              error:
                allOf:
                  - type: string
                    example: Unauthorized
            refIdentifier: '#/components/schemas/ApiErrorUnauthorized'
            requiredProperties:
              - status
              - error
        examples:
          example:
            value:
              status: 401
              error: Unauthorized
        description: Unauthorized error
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 404
              error:
                allOf:
                  - type: string
                    example: Not Found
              code:
                allOf:
                  - type: string
                    example: object_not_found
            refIdentifier: '#/components/schemas/ApiErrorNotFound'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 404
              error: Not Found
              code: object_not_found
        description: Not Found error
  deprecated: false
  type: path
components:
  schemas:
    BillableMetricFilterObject:
      type: object
      description: >-
        Values used to apply differentiated pricing based on additional event
        properties.
      required:
        - key
        - values
      properties:
        key:
          type: string
          example: region
          description: Filter key to add to the event properties payload
        values:
          type: array
          items:
            type: string
            example: us-east-1
          description: List of possible filter values
    BillableMetricObject:
      type: object
      required:
        - lago_id
        - name
        - code
        - aggregation_type
        - recurring
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: Unique identifier of the billable metric created by Lago.
        name:
          type: string
          example: Storage
          description: Name of the billable metric.
        code:
          type: string
          example: storage
          description: >-
            Unique code used to identify the billable metric associated with the
            API request. This code associates each event with the correct
            metric.
        description:
          type:
            - string
            - 'null'
          example: GB of storage used in my application
          description: Internal description of the billable metric.
        recurring:
          type: boolean
          example: false
          description: >-
            Defines if the billable metric is persisted billing period over
            billing period.


            - If set to `true`: the accumulated number of units calculated from
            the previous billing period is persisted to the next billing period.

            - If set to `false`: the accumulated number of units is reset to 0
            at the end of the billing period.

            - If not defined in the request, default value is `false`.
        rounding_function:
          type:
            - string
            - 'null'
          enum:
            - ceil
            - floor
            - round
            - null
          example: round
          description: >-
            Refers to the numeric value or mathematical expression that will be
            rounded based on the calculated number of billing units. Possible
            values are `round`, `ceil` and `floor`.
        rounding_precision:
          type:
            - integer
            - 'null'
          example: 2
          description: >-
            Specifies the number of decimal places to which the
            `rounding_function` will be rounded. It can be a positive or
            negative value.
        created_at:
          type: string
          format: date-time
          example: '2022-09-14T16:35:31Z'
          description: Creation date of the billable metric.
        expression:
          type: string
          example: round((ended_at - started_at) * units)
          description: >-
            Expression used to calculate the event units. The expression is
            evalutated for each event and the result is then used to calculate
            the total aggregated units.
        field_name:
          type:
            - string
            - 'null'
          example: gb
          description: >-
            Property of the billable metric used for aggregating usage data.
            This field is not required for `count_agg`.
        aggregation_type:
          type: string
          description: Aggregation method used to compute usage for this billable metric.
          example: sum_agg
          enum:
            - count_agg
            - sum_agg
            - max_agg
            - unique_count_agg
            - weighted_sum_agg
            - latest_agg
        weighted_interval:
          type:
            - string
            - 'null'
          enum:
            - seconds
            - null
          example: seconds
          description: >-
            Parameter exclusively utilized in conjunction with the
            `weighted_sum` aggregation type. It serves to adjust the aggregation
            result by assigning weights and proration to the result based on
            time intervals. When this field is not provided, the default time
            interval is assumed to be in `seconds`.
        filters:
          type: array
          items:
            $ref: '#/components/schemas/BillableMetricFilterObject'
    AlertThresholdBaseObject:
      type: object
      properties:
        code:
          type:
            - string
            - 'null'
          description: Unique identifier of the usage threshold created by Lago.
          example: warn
        recurring:
          type: boolean
          default: false
          description: >-
            This field when set to `true` indicates that the alert will be
            retrigger when this threshold is reached after the last
            non-recurring threshold. Only one recurring threshold per alert
            allowed.
          example: false
    AlertThresholdObject:
      allOf:
        - $ref: '#/components/schemas/AlertThresholdBaseObject'
        - type: object
          required:
            - code
            - value
            - recurring
          properties:
            value:
              type: string
              pattern: ^[0-9]+.?[0-9]*$
              description: >-
                A value that should trigger this alert, formatted as a
                BigDecimal.
              example: '99.0'
    AlertObject:
      type: object
      required:
        - lago_id
        - lago_organization_id
        - subscription_external_id
        - customer_external_id
        - billable_metric
        - alert_type
        - code
        - name
        - previous_value
        - last_processed_at
        - thresholds
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          description: Unique identifier of the alert, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        lago_organization_id:
          type: string
          format: uuid
          description: Unique identifier of the organization, created by Lago.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        subscription_external_id:
          type: string
          description: >-
            The subscription external unique identifier (provided by your own
            application).
          example: sub_1234567890
        customer_external_id:
          type: string
          description: >-
            The customer external unique identifier (provided by your own
            application).
          example: cus_0987654321
        billable_metric:
          $ref: '#/components/schemas/BillableMetricObject'
          description: >-
            The billable metric associated with the alert. Only for alerts based
            on a billable metric.
        alert_type:
          type: string
          description: The type of alert.
          enum:
            - current_usage_amount
            - billable_metric_current_usage_amount
            - billable_metric_current_usage_units
            - lifetime_usage_amount
          example: billable_metric_current_usage_amount
        code:
          type: string
          description: Unique code used to identify the alert.
          example: storage_threshold_alert
        name:
          type:
            - string
            - 'null'
          description: The name of the alert.
          example: Storage Usage Alert
        previous_value:
          type: number
          description: >-
            When the system checked if this alert should be triggered, this
            value was retrieved and checked against the thresholds.
          example: 1000
        last_processed_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            The date and time in UTC (ISO 8601) when the system checked if this
            alert should be triggered. Null until it's processed for the first
            time.
          example: '2025-05-19T10:04:21Z'
        thresholds:
          type: array
          description: Array of thresholds associated with the alert.
          items:
            $ref: '#/components/schemas/AlertThresholdObject'
        created_at:
          type: string
          format: date-time
          description: The date and time in UTC (ISO 8601) when the alert was created.
          example: '2025-03-20T10:00:00Z'

````