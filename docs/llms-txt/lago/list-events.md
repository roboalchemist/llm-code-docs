# Source: https://getlago.com/docs/api-reference/events/list-events.md

# List all events

> This endpoint is used for retrieving all events.

## OpenAPI

````yaml GET /events
paths:
  path: /events
  method: get
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
      query:
        page:
          schema:
            - type: integer
              required: false
              description: Page number.
              example: 1
          explode: true
        per_page:
          schema:
            - type: integer
              required: false
              description: Number of records per page.
              example: 20
          explode: true
        external_subscription_id:
          schema:
            - type: string
              required: false
              description: External subscription ID
              example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
          explode: true
        code:
          schema:
            - type: string
              required: false
              description: Filter events by its code.
              example: event-123
          explode: true
        timestamp_from_started_at:
          schema:
            - type: boolean
              required: false
              description: >-
                Requires `external_subscription_id` to be set. Filter events by
                timestamp after the subscription started at datetime.
              example: true
          explode: true
        timestamp_from:
          schema:
            - type: string
              required: false
              description: Filter events by timestamp starting from a specific date.
              format: date-time
              example: '2022-08-08T00:00:00Z'
          explode: true
        timestamp_to:
          schema:
            - type: string
              required: false
              description: Filter events by timestamp up to a specific date.
              format: date-time
              example: '2022-08-08T00:00:00Z'
          explode: true
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              events:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/EventObject'
              meta:
                allOf:
                  - $ref: '#/components/schemas/PaginationMeta'
            refIdentifier: '#/components/schemas/EventsPaginated'
            requiredProperties:
              - events
              - meta
        examples:
          example:
            value:
              events:
                - lago_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  transaction_id: transaction_1234567890
                  lago_customer_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  code: storage
                  timestamp: '2022-04-29T08:59:51.123Z'
                  precise_total_amount_cents: '1234.56'
                  properties:
                    gb: 10
                  lago_subscription_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  external_subscription_id: sub_1234567890
                  created_at: '2022-04-29T08:59:51Z'
              meta:
                current_page: 2
                next_page: 3
                prev_page: 1
                total_pages: 4
                total_count: 70
        description: Events
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
    PaginationMeta:
      type: object
      required:
        - current_page
        - total_pages
        - total_count
      properties:
        current_page:
          type: integer
          description: Current page.
          example: 2
        next_page:
          type:
            - integer
            - 'null'
          description: Next page.
          example: 3
        prev_page:
          type:
            - integer
            - 'null'
          description: Previous page.
          example: 1
        total_pages:
          type: integer
          description: Total number of pages.
          example: 4
        total_count:
          type: integer
          description: Total number of records.
          example: 70
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

````