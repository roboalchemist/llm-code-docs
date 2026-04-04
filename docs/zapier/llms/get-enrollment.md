# Source: https://docs.zapier.com/powered-by-zapier/api-reference/promotions/get-enrollment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Promotion Enrollment

> Retrieve promotion enrollment details by enrollment ID.

Endpoint available to Partners only.
The request must be authenticated by a user access token
that the user has granted to the Partner for the account.

#### OAuth

This endpoint requires the `promotions:read` OAuth scope.

This API is [rate limited](/powered-by-zapier/api-reference/rate-limiting).


## OpenAPI

````yaml powered-by-zapier/api-reference/promotions-openapi.yaml get /v2/promotions/{enrollment_id}
openapi: 3.1.0
info:
  title: Powered by Zapier Promotions API
  version: promotions
  description: >-
    The API to define promotions, powered by Zapier. See
    https://docs.zapier.com/powered-by-zapier/introduction for more information.
  contact:
    name: Partner Sharing
servers:
  - url: https://api.zapier.com
    description: Production
security: []
tags:
  - name: Promotions
    description: Operations related to managing Promotions
  - name: Experimental
    description: >-
      Operations that are not to be considered finalized, and are subject to
      change
paths:
  /v2/promotions/{enrollment_id}:
    get:
      tags:
        - Promotions
        - Experimental
      description: |-
        Retrieve promotion enrollment details by enrollment ID.

        Endpoint available to Partners only.
        The request must be authenticated by a user access token
        that the user has granted to the Partner for the account.

        #### OAuth

        This endpoint requires the `promotions:read` OAuth scope.
      operationId: root_retrieve
      parameters:
        - in: path
          name: enrollment_id
          schema:
            type: string
          required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromotionDetail'
              examples:
                GetPromotionDetails:
                  value:
                    promotion_id: test_promo
                    enrollment_date: '2026-04-28T00:00:00Z'
                    expiration_date: '2026-07-26T23:59:59Z'
                    task_limit_per_month: 5
                    tasks_used_this_month: 0
                    status: enrolled
                  summary: Get Promotion Details
          description: Succcessful retrieval of promotion details
        '401':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromotionErrorResponse'
              examples:
                Access:
                  value:
                    errors:
                      - status: '401'
                        code: not_authenticated
                        title: User Not Authenticated
                        detail: >-
                          User must be authenticated to access this resource. No
                          valid user access token was provided.
          description: >-
            Access denied: User does not have permission for enrollment_id:
            enroll_67890
        '403':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromotionErrorResponse'
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
          description: No response body
        '429':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromotionErrorResponse'
          description: ''
        '503':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromotionErrorResponse'
          description: ''
      security:
        - OAuth:
            - promotions:read
components:
  schemas:
    PromotionDetail:
      type: object
      description: Succcessful retrieval of promotion details
      properties:
        promotion_id:
          type: string
          description: The unique identifier for the promotion
        enrollment_date:
          type:
            - string
            - 'null'
          format: date-time
          description: Date and time of enrollment
        expiration_date:
          type:
            - string
            - 'null'
          format: date-time
          description: Date and time when the promotion expires
        task_limit_per_month:
          type:
            - integer
            - 'null'
          description: Maximum number of tasks allowed per monthly billing cycle
        tasks_used_this_month:
          type: integer
          description: >-
            Number of tasks already used this monthly billing cycle (may not
            align with calendar month)
        status:
          type: string
          description: Current status of the enrollment
      required:
        - enrollment_date
        - expiration_date
        - promotion_id
        - status
        - task_limit_per_month
        - tasks_used_this_month
    PromotionErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/PromotionError'
          description: Errors encountered processing the request
      required:
        - errors
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
  securitySchemes:
    OAuth:
      type: oauth2
      description: >-
        The user access token for the user you would like to enroll. See our
        [OAuth2 authentication
        documentation](https://docs.zapier.com/powered-by-zapier/api-reference/authentication#retrieving-a-user-access-token).
      flows:
        authorizationCode:
          authorizationUrl: https://zapier.com/oauth/authorize/
          tokenUrl: https://zapier.com/oauth/token/
          refreshUrl: https://zapier.com/oauth/token/
          scopes:
            promotions:write: Enroll or unenroll accounts into promotions
            promotions:read: View usage of promotions you manage on an account
        clientCredentials:
          tokenUrl: /oauth/token
          scopes:
            promotions:write: Unenroll accounts from promotions

````