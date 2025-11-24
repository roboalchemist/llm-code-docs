# Source: https://docs.zapier.com/powered-by-zapier/api-reference/promotions/create-enrollment.md

# Create Promotion Enrollment

> Enrolls an account into an existing promotion.

Endpoint available to Partners only.
The request must be authenticated by an [access token](https://docs.zapier.com/powered-by-zapier/api-reference/authentication#retrieving-a-user-access-token)
that the user has granted to the Partner for the account.

The `enrollment_id`, returned after successfully enrolling a user,
**must** be stored by the partner in order to [retrieve](https://docs.zapier.com/powered-by-zapier/api-reference/promotions/get-enrollment)
or [delete](https://docs.zapier.com/powered-by-zapier/api-reference/promotions/delete-enrollment) the enrollment.

#### OAuth

This endpoint requires the `promotions:write` OAuth scope.

## OpenAPI

````yaml powered-by-zapier/api-reference/promotions-openapi.yaml post /v2/promotions
paths:
  path: /v2/promotions
  method: post
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              promotion_id:
                allOf:
                  - type: string
                    description: The unique identifier for the promotions
            required: true
            refIdentifier: '#/components/schemas/PromotionEnrollment'
            requiredProperties:
              - promotion_id
        examples:
          EnrollInAPromotion:
            summary: Enroll in a promotion
            value:
              promotion_id: promo_12345
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              enrollment_id:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier for the enrollment. This must be
                      stored by partners.
            description: Successful Enrollment
            refIdentifier: '#/components/schemas/PromotionEnrollmentResponse'
            requiredProperties:
              - enrollment_id
        examples:
          example:
            value:
              enrollment_id: <string>
        description: Successful Enrollment
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
          '404':
            value:
              errors:
                - status: '404'
                  code: promotion_not_found
                  title: Promotion Not Found
                  detail: >-
                    The requested promotion was not found. The specified
                    promotion_id may be invalid.
        description: 404 Not Found
    '409':
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
          Conflict:
            value:
              errors:
                - status: '409'
                  code: already_enrolled
                  title: Already Enrolled
                  detail: >-
                    The provided account is already enrolled in the specified
                    promotion.
        description: Conflict - User is already enrolled in this promotion
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