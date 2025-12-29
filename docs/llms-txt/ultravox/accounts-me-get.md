# Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-get.md

# Get Account

> Returns account details for a single account



## OpenAPI

````yaml get /api/accounts/me
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/accounts/me:
    get:
      tags:
        - accounts
      operationId: accounts_me_retrieve
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Account'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    Account:
      type: object
      properties:
        name:
          type: string
          readOnly: true
        billingUrl:
          type: string
          readOnly: true
        freeTimeUsed:
          type: string
          readOnly: true
          description: How much free time has been used by previous (or ongoing) calls.
        freeTimeRemaining:
          type: string
          readOnly: true
          description: >-
            How much free call time this account has remaining. (This could
            increase if an existing call ends without using its maximum duration
            or an unjoined call times out.)
        hasActiveSubscription:
          type: boolean
          description: Whether the account has an active subscription.
        subscriptionTier:
          type: string
          nullable: true
          readOnly: true
          description: The current subscription tier for this account.
        subscriptionCadence:
          type: string
          nullable: true
          readOnly: true
          description: How often the subscription is billed for this account.
        subscriptionExpiration:
          type: string
          format: date-time
          nullable: true
          readOnly: true
          description: >-
            The expiration date of the current subscription for this account, if
            any. This is the point at which access will end unless credit
            remains.
        subscriptionScheduledUpdate:
          type: string
          format: date-time
          nullable: true
          readOnly: true
          description: >-
            The point in the future where this account's subscription is
            scheduled to change.
        subscriptionRenewal:
          type: string
          format: date-time
          nullable: true
          readOnly: true
          description: When this account's subscription renews, if applicable.
        activeCalls:
          type: integer
          readOnly: true
          description: The number of active calls for this account.
        allowedConcurrentCalls:
          type: integer
          nullable: true
          readOnly: true
          description: The maximum number of concurrent calls allowed for this account.
        allowedVoices:
          type: integer
          nullable: true
          readOnly: true
          description: The maximum number of custom voices allowed for this account.
        allowedCorpora:
          type: integer
          nullable: true
          readOnly: true
          description: The maximum number of corpora allowed for this account.
      required:
        - activeCalls
        - allowedConcurrentCalls
        - allowedCorpora
        - allowedVoices
        - billingUrl
        - freeTimeRemaining
        - freeTimeUsed
        - hasActiveSubscription
        - name
        - subscriptionCadence
        - subscriptionExpiration
        - subscriptionRenewal
        - subscriptionScheduledUpdate
        - subscriptionTier
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt