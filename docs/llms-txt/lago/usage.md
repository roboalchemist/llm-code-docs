# Source: https://getlago.com/docs/api-reference/events/usage.md

# Send usage event

> This endpoint is used for transmitting usage measurement events to either a designated customer or a specific subscription.

## OpenAPI

````yaml POST /events
paths:
  path: /events
  method: post
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              event:
                allOf:
                  - $ref: '#/components/schemas/EventInputObject'
            required: true
            refIdentifier: '#/components/schemas/EventInput'
            requiredProperties:
              - event
        examples:
          example:
            value:
              event:
                transaction_id: transaction_1234567890
                external_subscription_id: sub_1234567890
                code: storage
                timestamp: '1651240791.123'
                precise_total_amount_cents: '1234.56'
                properties:
                  gb: 10
        description: Event payload
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              event:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/EventObject'
                      - type: object
                        properties:
                          lago_customer_id:
                            type: 'null'
                            description: >-
                              The value will always be null in this response as
                              the event processing is done asynchronously
                            example: null
            refIdentifier: '#/components/schemas/EventCreated'
            requiredProperties:
              - event
        examples:
          example:
            value:
              event:
                lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                transaction_id: transaction_1234567890
                lago_customer_id: null
                code: storage
                timestamp: '2022-04-29T08:59:51.123Z'
                precise_total_amount_cents: '1234.56'
                properties:
                  gb: 10
                lago_subscription_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                external_subscription_id: sub_1234567890
                created_at: '2022-04-29T08:59:51Z'
        description: Event
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 400
              error:
                allOf:
                  - type: string
                    example: Bad request
            refIdentifier: '#/components/schemas/ApiErrorBadRequest'
            requiredProperties:
              - status
              - error
        examples:
          example:
            value:
              status: 400
              error: Bad request
        description: Bad Request error
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
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 403
              error:
                allOf:
                  - type: string
                    example: Forbidden
              code:
                allOf:
                  - type: string
                    example: feature_unavailable
            refIdentifier: '#/components/schemas/ApiErrorForbidden'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 403
              error: Forbidden
              code: feature_unavailable
        description: Forbidden
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 422
              error:
                allOf:
                  - type: string
                    example: Unprocessable entity
              code:
                allOf:
                  - type: string
                    example: validation_errors
              error_details:
                allOf:
                  - type: object
            refIdentifier: '#/components/schemas/ApiErrorUnprocessableEntity'
            requiredProperties:
              - status
              - error
              - code
              - error_details
        examples:
          example:
            value:
              status: 422
              error: Unprocessable entity
              code: validation_errors
              error_details: {}
        description: Unprocessable entity error
  deprecated: false
  type: path
components:
  schemas:
    EventObject:
      type: object
      required:
        - lago_id
        - transaction_id
        - lago_customer_id
        - code
        - timestamp
        - lago_subscription_id
        - external_subscription_id
        - created_at
      properties:
        lago_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the event within the Lago application.
            This ID is exclusively created by Lago and serves as a unique
            identifier for the event's record within the Lago system
        transaction_id:
          type: string
          example: transaction_1234567890
          description: >-
            This field represents a unique identifier for the event. It is
            crucial for ensuring idempotency, meaning that each event can be
            uniquely identified and processed without causing any unintended
            side effects.
        lago_customer_id:
          type:
            - string
            - 'null'
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the customer within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the customer's record within the Lago system
        code:
          type: string
          example: storage
          description: >-
            The code that identifies a targeted billable metric. It is essential
            that this code matches the `code` property of one of your active
            billable metrics. If the provided code does not correspond to any
            active billable metric, it will be ignored during the process.
        timestamp:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51.123Z'
          description: >-
            This field captures the Unix timestamp in seconds indicating the
            occurrence of the event in Coordinated Universal Time (UTC). If this
            timestamp is not provided, the API will automatically set it to the
            time of event reception.
        precise_total_amount_cents:
          type:
            - string
            - 'null'
          example: '1234.56'
          description: >-
            The precise total amount that was sent in the event payload. This
            filed is used by the `dynamic` pricing model.
        properties:
          type: object
          description: >-
            This field represents additional properties associated with the
            event, which are utilized in the calculation of the final fee. This
            object becomes mandatory when the targeted billable metric employs a
            `sum_agg`, `max_agg`, or `unique_count_agg` aggregation method.
            However, when using a simple `count_agg`, this object is not
            required.
          properties:
            operation_type:
              type:
                - string
                - 'null'
              description: >-
                The `operation_type` field is only necessary when adding or
                removing a specific unit when the targeted billable metric
                adopts a `unique_count_agg` aggregation method. In other cases,
                the `operation_type` field is not required. The valid values for
                the `operation_type` field are `add` or `remove`, which indicate
                whether the unit is being added or removed from the unique count
                aggregation, respectively.
              enum:
                - add
                - remove
          additionalProperties:
            oneOf:
              - type: string
              - type: integer
              - type: number
          example:
            gb: 10
        lago_subscription_id:
          type:
            - string
            - 'null'
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the subscription within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the subscription's record within the Lago
            system
        external_subscription_id:
          type: string
          example: sub_1234567890
          description: >-
            The unique identifier of the subscription within your application.
            It is a mandatory field when the customer possesses multiple
            subscriptions or when the `external_customer_id` is not provided.
        created_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The creation date of the event's record in the Lago application,
            presented in the ISO 8601 datetime format, specifically in
            Coordinated Universal Time (UTC). It provides the precise timestamp
            of when the event's record was created within the Lago application
    EventInputObject:
      type: object
      required:
        - transaction_id
        - external_subscription_id
        - code
      properties:
        transaction_id:
          type: string
          example: transaction_1234567890
          description: >
            This field represents a unique identifier for the event.

            It is crucial for ensuring idempotency, meaning that each event can
            be uniquely identified and processed without causing any unintended
            side effects.


            WARNING: If the Lago organization is configured to use the new
            Clickhouse-based event pipeline (designed for high-volume
            processing), the idempotency logic is handled differently.

            Event uniqueness is maintained with both `transaction_id` and
            `timestamp` fields.

            If a new event arrives with identical values for these two fields as
            an existing event, the new one will overwrite the previous event
            rather than being rejected.
        external_subscription_id:
          type: string
          example: sub_1234567890
          description: >-
            The unique identifier of the subscription in your application. This
            field is mandatory in order to link events to the correct customer
            subscription.
        code:
          type: string
          example: storage
          description: >-
            The code that identifies a targeted billable metric. It is essential
            that this code matches the `code` property of one of your active
            billable metrics. If the provided code does not correspond to any
            active billable metric, it will be ignored during the process.
        timestamp:
          oneOf:
            - type: integer
            - type: string
          example: '1651240791.123'
          description: >
            This field captures the Unix timestamp in seconds indicating the
            occurrence of the event in Coordinated Universal Time (UTC).

            If this timestamp is not provided, the API will automatically set it
            to the time of event reception.

            You can also provide miliseconds precision by appending decimals to
            the timestamp.
        precise_total_amount_cents:
          type:
            - string
            - 'null'
          example: '1234.56'
          description: >-
            The precise total amount in cents with precision used by the
            `dynamic` pricing model to compute the usage amount.
        properties:
          type:
            - object
            - 'null'
          description: >-
            This field represents additional properties associated with the
            event, which are utilized in the calculation of the final fee. This
            object becomes mandatory when the targeted billable metric employs a
            `sum_agg`, `max_agg`, or `unique_count_agg` aggregation method.
            However, when using a simple `count_agg`, this object is not
            required.
          additionalProperties:
            oneOf:
              - type: string
              - type: integer
              - type: number
          example:
            gb: 10

````