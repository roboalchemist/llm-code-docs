# Source: https://docs.edgeimpulse.com/apis/studio/user/get-user-billable-compute-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get user billable compute metrics

> Get billable compute metrics for a user. This function is only available to users with an active subscription.



## OpenAPI

````yaml .assets/openapi.yaml get /api/user/subscription/metrics
openapi: 3.0.0
info:
  title: Edge Impulse API
  version: 1.0.0
servers:
  - url: https://studio.edgeimpulse.com/v1
security:
  - ApiKeyAuthentication: []
  - JWTAuthentication: []
  - JWTHttpHeaderAuthentication: []
  - OAuth2: []
paths:
  /api/user/subscription/metrics:
    get:
      tags:
        - User
      summary: Get user billable compute metrics
      description: >-
        Get billable compute metrics for a user. This function is only available
        to users with an active subscription.
      operationId: userGetSubscriptionMetrics
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserSubscriptionMetricsResponse'
components:
  schemas:
    UserSubscriptionMetricsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            metrics:
              type: object
              required:
                - computeMinutesCpu
                - computeMinutesGpu
                - computeMinutesTotal
                - computeMinutesLimit
              properties:
                computeMinutesCpu:
                  type: number
                  description: >-
                    Total compute of all user jobs, running on CPU, in the
                    current billing period.
                computeMinutesGpu:
                  type: number
                  description: >-
                    Total compute of all user jobs, running on GPU, in the
                    current billing period.
                computeMinutesTotal:
                  type: number
                  description: >-
                    Total compute of all user jobs in the current billing
                    period, calculated as CPU + 3*GPU compute.
                computeMinutesLimit:
                  type: number
                  description: Overall compute limit for the current billing period.
                computeResetDate:
                  type: string
                  format: date-time
                  description: >-
                    The date at which the current compute billing period will
                    reset.
            approachingComputeLimitMinutesLeft:
              type: number
              description: >
                Number of compute minutes remaining before reaching the monthly
                compute limit. This field is only present when the user has
                fewer than 60 minutes left. Once the limit is reached, users can
                continue using compute resources by subscribing to the
                pay-as-you-go plan.
    GenericApiResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
          description: Whether the operation succeeded
        error:
          type: string
          description: Optional error description (set if 'success' was false)
  securitySchemes:
    ApiKeyAuthentication:
      type: apiKey
      in: header
      name: x-api-key
    JWTAuthentication:
      type: apiKey
      in: cookie
      name: jwt
    JWTHttpHeaderAuthentication:
      type: apiKey
      in: header
      name: x-jwt-token
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: /v1/oauth/authorize
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        implicit:
          authorizationUrl: /v1/oauth/authorize
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        password:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        clientCredentials:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information

````

Built with [Mintlify](https://mintlify.com).