# Source: https://docs.zapier.com/powered-by-zapier/api-reference/promotions/get-enrollment.md

# Get Promotion Enrollment

> Retrieve promotion enrollment details by enrollment ID.

Endpoint available to Partners only.
The request must be authenticated by a user access token
that the user has granted to the Partner for the account.

#### OAuth

This endpoint requires the `promotions:read` OAuth scope.

## OpenAPI

````yaml powered-by-zapier/api-reference/promotions-openapi.yaml get /v2/promotions/{enrollment_id}
paths:
  path: /v2/promotions/{enrollment_id}
  method: get
  servers:
    - url: https://api.zapier.com
      description: Production
  request:
    security:
      - title: OAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: oauth2
              description: >-
                The user access token for the user you would like to enroll. See
                our [OAuth2 authentication
                documentation](https://docs.zapier.com/powered-by-zapier/api-reference/authentication#retrieving-a-user-access-token).
          cookie: {}
    parameters:
      path:
        enrollment_id:
          schema:
            - type: string
              required: true
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
              promotion_id:
                allOf:
                  - type: string
                    description: The unique identifier for the promotion
              enrollment_date:
                allOf:
                  - type:
                      - string
                      - 'null'
                    format: date-time
                    description: Date and time of enrollment
              expiration_date:
                allOf:
                  - type:
                      - string
                      - 'null'
                    format: date-time
                    description: Date and time when the promotion expires
              task_limit_per_month:
                allOf:
                  - type:
                      - integer
                      - 'null'
                    description: Maximum number of tasks allowed per monthly billing cycle
              tasks_used_this_month:
                allOf:
                  - type: integer
                    description: >-
                      Number of tasks already used this monthly billing cycle
                      (may not align with calendar month)
              status:
                allOf:
                  - type: string
                    description: Current status of the enrollment
            description: Succcessful retrieval of promotion details
            refIdentifier: '#/components/schemas/PromotionDetail'
            requiredProperties:
              - enrollment_date
              - expiration_date
              - promotion_id
              - status
              - task_limit_per_month
              - tasks_used_this_month
        examples:
          GetPromotionDetails:
            summary: Get Promotion Details
            value:
              promotion_id: test_promo
              enrollment_date: '2025-04-28T00:00:00Z'
              expiration_date: '2025-07-26T23:59:59Z'
              task_limit_per_month: 5
              tasks_used_this_month: 0
              status: enrolled
        description: Succcessful retrieval of promotion details
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - &ref_0
                    type: array
                    items:
                      $ref: '#/components/schemas/PromotionError'
                    description: Errors encountered processing the request
            refIdentifier: '#/components/schemas/PromotionErrorResponse'
            requiredProperties: &ref_1
              - errors
        examples:
          Access:
            value:
              errors:
                - status: '401'
                  code: not_authenticated
                  title: User Not Authenticated
                  detail: >-
                    User must be authenticated to access this resource. No valid
                    user access token was provided.
        description: >-
          Access denied: User does not have permission for enrollment_id:
          enroll_67890
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/PromotionErrorResponse'
            requiredProperties: *ref_1
        examples:
          Forbidden:
            value:
              errors:
                - status: '403'
                  code: permission_denied
                  title: Permission Denied
                  detail: You do not have permission to perform this action.
        description: Forbidden - User lacks permission to access this location
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: No response body
        examples: {}
        description: No response body
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/PromotionErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: <string>
                  code: <string>
                  title: <string>
                  detail: <string>
        description: ''
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/PromotionErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: <string>
                  code: <string>
                  title: <string>
                  detail: <string>
        description: ''
  deprecated: false
  type: path
components:
  schemas:
    PromotionError:
      type: object
      properties:
        status:
          type: string
          description: HTTP status code of the error
        code:
          type: string
          description: Machine-readable error code
        title:
          type: string
          description: Human-readable error title
        detail:
          type: string
          description: Detailed description of the error
      required:
        - code
        - detail
        - status
        - title

````