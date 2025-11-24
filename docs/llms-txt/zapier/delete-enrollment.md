# Source: https://docs.zapier.com/powered-by-zapier/api-reference/promotions/delete-enrollment.md

# Delete Promotion Enrollment

> Unenroll an account from a promotion.

Endpoint available to Partners only.
The request must be authenticated by an app access token the
Partner has received using the Client Credentials flow.

#### OAuth

This endpoint requires the `promotions:write` OAuth scope.

## OpenAPI

````yaml powered-by-zapier/api-reference/promotions-openapi.yaml delete /v2/promotions/{enrollment_id}
paths:
  path: /v2/promotions/{enrollment_id}
  method: delete
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
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: No response body
        examples: {}
        description: No response body
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