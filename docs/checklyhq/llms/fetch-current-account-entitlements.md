# Source: https://checklyhq.com/docs/api-reference/accounts/fetch-current-account-entitlements.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch current account entitlements

> Fetch the entitlements for the account, including feature access and limits based on the current plan.



## OpenAPI

````yaml get /v1/accounts/me/entitlements
openapi: 3.0.0
info:
  title: Checkly Public API
  version: v1
  description: >-
    These are the docs for the newly released Checkly Public API. If you have
    any questions, please do not hesitate to get in touch with us.
servers:
  - url: https://api.checklyhq.com
security:
  - Bearer: []
tags: []
paths:
  /v1/accounts/me/entitlements:
    get:
      tags:
        - Accounts
      summary: Fetch current account entitlements
      description: >-
        Fetch the entitlements for the account, including feature access and
        limits based on the current plan.
      operationId: getV1AccountsMeEntitlements
      parameters:
        - name: x-checkly-account
          in: header
          schema:
            type: string
            description: >-
              Your Checkly account ID, you can find it at
              https://app.checklyhq.com/settings/account/general
            x-format:
              guid: true
          description: >-
            Your Checkly account ID, you can find it at
            https://app.checklyhq.com/settings/account/general
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Entitlements'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForbiddenError'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFoundError'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    Entitlements:
      type: object
      properties:
        plan:
          type: string
          description: The account plan type.
          example: team
        planDisplayName:
          type: string
          description: The human-readable display name of the account plan.
          example: Team
        addons:
          $ref: '#/components/schemas/addons'
        locations:
          $ref: '#/components/schemas/Locations'
        entitlements:
          $ref: '#/components/schemas/entitlements'
      required:
        - plan
        - locations
        - entitlements
    UnauthorizedError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 401
        error:
          $ref: '#/components/schemas/error'
        message:
          type: string
          example: Bad Token
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    ForbiddenError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 403
        error:
          $ref: '#/components/schemas/Model1'
        message:
          type: string
          example: Forbidden
      required:
        - statusCode
        - error
    NotFoundError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 404
        error:
          $ref: '#/components/schemas/Model3'
        message:
          type: string
          example: Not Found
      required:
        - statusCode
        - error
    TooManyRequestsError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 429
        error:
          $ref: '#/components/schemas/Model2'
        message:
          type: string
          example: Too Many Requests
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    addons:
      type: object
      description: The add-ons available to the account.
      properties:
        communicate:
          $ref: '#/components/schemas/AddonTier'
        resolve:
          $ref: '#/components/schemas/AddonTier'
    Locations:
      type: object
      description: Check run locations and limits for this account.
      properties:
        all:
          $ref: '#/components/schemas/all'
        maxPerCheck:
          type: integer
          description: Maximum locations selectable per check. Absent when unlimited.
          minimum: 1
      required:
        - all
    entitlements:
      type: array
      description: List of entitled features for this account.
      items:
        $ref: '#/components/schemas/Entitlement'
    error:
      type: string
      enum:
        - Unauthorized
    attributes:
      type: object
    Model1:
      type: string
      enum:
        - Forbidden
    Model3:
      type: string
      enum:
        - Not Found
    Model2:
      type: string
      enum:
        - Too Many Requests
    AddonTier:
      type: object
      properties:
        tier:
          $ref: '#/components/schemas/tier'
        tierDisplayName:
          type: string
          description: The human-readable display name of the add-on tier.
          example: Communicate Starter
    all:
      type: array
      description: All Checkly locations with availability for this account.
      items:
        $ref: '#/components/schemas/Location'
    Entitlement:
      type: object
      properties:
        key:
          type: string
          description: Unique entitlement identifier.
        name:
          type: string
          description: Human-friendly display name.
        description:
          type: string
          description: Short description of what this entitlement controls.
        type:
          $ref: '#/components/schemas/type'
        enabled:
          type: boolean
          description: Whether this entitlement is available on the current plan.
        quantity:
          type: integer
          description: Maximum allowed quantity. Only present for metered entitlements.
          minimum: 0
        requiredPlan:
          type: string
          description: >-
            The minimum plan required to unlock this entitlement. Only present
            for disabled entitlements.
        requiredPlanDisplayName:
          type: string
          description: Human-readable name of the required plan.
        requiredAddon:
          $ref: '#/components/schemas/RequiredAddon'
      required:
        - key
        - name
        - description
        - type
        - enabled
    tier:
      type: string
      description: The add-on tier.
      example: starter
      enum:
        - hobby
        - starter
        - team
    Location:
      type: object
      properties:
        id:
          type: string
          description: Location identifier (e.g. us-east-1).
        name:
          type: string
          description: Human-readable location name (e.g. N. Virginia).
        available:
          type: boolean
          description: Whether this location is available on the current plan.
      required:
        - id
        - name
        - available
    type:
      type: string
      description: >-
        Whether this entitlement is a boolean feature flag or a metered resource
        with a quantity limit.
      enum:
        - flag
        - metered
    RequiredAddon:
      type: object
      description: >-
        The addon and tier required to unlock this entitlement. Only present for
        disabled entitlements.
      properties:
        name:
          type: string
          description: The addon name.
        displayName:
          type: string
          description: Human-readable addon name.
        tier:
          $ref: '#/components/schemas/Model4'
        tierDisplayName:
          type: string
          description: Human-readable addon tier name.
      required:
        - name
        - displayName
        - tier
        - tierDisplayName
    Model4:
      type: string
      description: The minimum addon tier required (e.g. starter, team).
      enum:
        - hobby
        - starter
        - team
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer
      bearerFormat: Bearer
      description: >-
        The Checkly Public API uses API keys to authenticate requests. You can
        get the API Key
        [here](https://app.checklyhq.com/settings/user/api-keys). Your API key
        is like a password:  keep it secure!

        Authentication to the API is performed using the Bearer auth method in
        the Authorization header and using the account ID.

        For example, set **Authorization** header while using cURL: `curl -H
        "Authorization: Bearer [apiKey]" "X-Checkly-Account: [accountId]"` 

````

Built with [Mintlify](https://mintlify.com).