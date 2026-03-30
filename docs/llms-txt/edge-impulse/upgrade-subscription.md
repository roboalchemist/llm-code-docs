# Source: https://docs.edgeimpulse.com/apis/studio/user/upgrade-subscription.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade subscription

> Upgrade the current subscription.



## OpenAPI

````yaml .assets/openapi.yaml post /api/user/subscription/upgrade
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
  /api/user/subscription/upgrade:
    post:
      tags:
        - User
      summary: Upgrade subscription
      description: Upgrade the current subscription.
      operationId: userUpgradeSubscription
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpgradeSubscriptionRequest'
      responses:
        '302':
          description: A redirect to the payment portal
components:
  schemas:
    UpgradeSubscriptionRequest:
      type: object
      required:
        - billingCycle
        - successUrl
        - cancelUrl
      properties:
        billingCycle:
          $ref: '#/components/schemas/BillingCycle'
          description: |
            Selects the billing frequency for the subscription.
            Either 'monthly' for regular monthly charges or 'yearly'
            for annual billing with a potential discount.
        successUrl:
          type: string
          description: URL to redirect the user to after a successful checkout process.
        cancelUrl:
          type: string
          description: URL to redirect the user to after the checkout process is canceled.
    BillingCycle:
      type: string
      enum:
        - monthly
        - yearly
      description: >
        Specifies the frequency at which the subscription fee is billed:

        - `monthly`: Billed once every month.

        - `yearly`: Billed once every year, often at a discounted rate compared
        to monthly billing.
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