# Source: https://getlago.com/docs/api-reference/audit-logs/get-specific-activity-log.md

# Retrieve an activity log

> This endpoint retrieves an existing activity log that represents an action performed on some resource. The activity log is identified by its unique activity_id.

## OpenAPI

````yaml GET /activity_logs/{activity_id}
paths:
  path: /activity_logs/{activity_id}
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
      path:
        activity_id:
          schema:
            - type: string
              required: true
              description: The Activity Id of the existing activity log.
              example: bdc0eda6-ea52-4f72-a46a-94f47a89b546
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
              activity_log:
                allOf:
                  - $ref: '#/components/schemas/ActivityLogObject'
            refIdentifier: '#/components/schemas/ActivityLog'
            requiredProperties:
              - activity_log
        examples:
          example:
            value:
              activity_log:
                activity_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
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
        description: Activity Log
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

````