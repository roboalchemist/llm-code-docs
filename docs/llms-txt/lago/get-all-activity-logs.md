# Source: https://getlago.com/docs/api-reference/audit-logs/get-all-activity-logs.md

# List all activity logs

> This endpoint retrieves all existing activity logs that represent actions performed on application resources.

## OpenAPI

````yaml GET /activity_logs
paths:
  path: /activity_logs
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
        from_date:
          schema:
            - type: string
              required: false
              description: Filter activity logs from a specific date.
              format: date
              example: '2022-08-09'
          explode: true
        to_date:
          schema:
            - type: string
              required: false
              description: Filter activity logs up to a specific date.
              format: date
              example: '2022-08-09'
          explode: true
        activity_types[]:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              required: false
              description: Filter results by activity types
              example:
                - billing_metric.created
                - billing_metric.updated
          explode: true
        activity_sources[]:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
                    enum:
                      - api
                      - front
                      - system
              required: false
              description: Filter results by activity sources
              example:
                - api
                - front
          explode: true
        user_emails[]:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              required: false
              description: Filter results by user emails
              example:
                - dinesh@piedpiper.test
          explode: true
        external_customer_id:
          schema:
            - type: string
              required: false
              description: Unique identifier assigned to the customer in your application.
              example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
          explode: true
        external_subscription_id:
          schema:
            - type: string
              required: false
              description: External subscription ID
              example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
          explode: true
        resource_ids[]:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
                    format: uuid
              required: false
              description: Filter results by resources unique identifiers
              example:
                - 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                - 1a901a90-1a90-1a90-1a90-1a901a901a90
          explode: true
        resource_types[]:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              required: false
              description: Filter results by resource class types
              example:
                - BillableMetric
                - Invoice
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
              activity_logs:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/ActivityLogObject'
              meta:
                allOf:
                  - $ref: '#/components/schemas/PaginationMeta'
            refIdentifier: '#/components/schemas/ActivityLogsPaginated'
            requiredProperties:
              - activity_logs
              - meta
        examples:
          example:
            value:
              activity_logs:
                - activity_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  user_email: dinesh@piedpiper.test
                  activity_type: billing_metric.created
                  activity_source: api
                  activity_object:
                    lago_id: dad68bc7-c01a-4ad8-a87b-13e78693a5bc
                    plan_id: b9155544-e261-4e92-b54e-f65d7609294c
                  activity_object_changes:
                    plan_id:
                      - null
                      - b9155544-e261-4e92-b54e-f65d7609294c
                  external_customer_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                  external_subscription_id: external_id
                  resource_id: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
                  resource_type: BillableMetric
                  organization_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  logged_at: '2025-03-31T12:31:44Z'
                  created_at: '2022-04-29T08:59:51Z'
              meta:
                current_page: 2
                next_page: 3
                prev_page: 1
                total_pages: 4
                total_count: 70
        description: List of activity logs
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
  deprecated: false
  type: path
components:
  schemas:
    ActivityLogObject:
      type: object
      required:
        - activity_id
        - activity_source
        - activity_type
        - logged_at
        - resource_id
        - resource_type
        - organization_id
        - created_at
      properties:
        activity_id:
          type: string
          format: uuid
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
          description: >-
            Unique identifier assigned to the activity log within the Lago
            application. This ID is exclusively created by Lago and serves as a
            unique identifier for the activity log record within the Lago system
        user_email:
          type:
            - string
            - 'null'
          format: email
          example: dinesh@piedpiper.test
          description: The email of the user who performed the activity
        activity_type:
          type: string
          example: billing_metric.created
          description: >-
            This field stores the actitivy action that was performed to the
            activity_object.
        activity_source:
          type: string
          example: api
          enum:
            - api
            - front
            - system
          description: >-
            This field represents the source of the activity log, the
            interaction source that triggered the action.
        activity_object:
          type:
            - object
            - 'null'
          format: object
          example:
            lago_id: dad68bc7-c01a-4ad8-a87b-13e78693a5bc
            plan_id: b9155544-e261-4e92-b54e-f65d7609294c
          description: >-
            This field represents the final state of the object that the action
            was applied.
        activity_object_changes:
          type:
            - object
            - 'null'
          format: object
          example:
            plan_id:
              - null
              - b9155544-e261-4e92-b54e-f65d7609294c
        external_customer_id:
          type:
            - string
            - 'null'
          description: >-
            The customer external unique identifier (provided by your own
            application)
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        external_subscription_id:
          type:
            - string
            - 'null'
          description: Unique identifier assigned to the subscription in your application.
          example: external_id
        resource_id:
          type: string
          description: The resource id of the object that the action was applied.
          format: uuid
          example: 5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba
        resource_type:
          type: string
          description: The resource type of the resource_id record.
          example: BillableMetric
        organization_id:
          type: string
          format: uuid
          description: >-
            Unique identifier for the organization associated with the activity
            log.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        logged_at:
          type: string
          format: date-time
          example: '2025-03-31T12:31:44Z'
          description: >-
            The logged date of the activity, presented in the ISO 8601 datetime
            format, specifically in Coordinated Universal Time (UTC). It
            provides the precise timestamp of when the event's record was
            created within the Lago application
        created_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The creation date of the activity record in the Lago application,
            presented in the ISO 8601 datetime format, specifically in
            Coordinated Universal Time (UTC). It provides the precise timestamp
            of when the event's record was created within the Lago application
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

````