# Source: https://checklyhq.com/docs/api-reference/alert-channels/create-an-alert-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an alert channel

> Creates a new alert channel



## OpenAPI

````yaml post /v1/alert-channels
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
  /v1/alert-channels:
    post:
      tags:
        - Alert channels
      summary: Create an alert channel
      description: Creates a new alert channel
      operationId: postV1Alertchannels
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AlertChannelCreate'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AlertChannel'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '402':
          description: Payment Required
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentRequiredError'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForbiddenError'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    AlertChannelCreate:
      type: object
      properties:
        subscriptions:
          $ref: '#/components/schemas/AlertChanelSubscriptionList'
        type:
          $ref: '#/components/schemas/Model6'
        config:
          $ref: '#/components/schemas/AlertChannelCreateConfig'
        sendRecovery:
          type: boolean
        sendFailure:
          type: boolean
        sendDegraded:
          type: boolean
        sslExpiry:
          type: boolean
          description: Determines if an alert should be sent for expiring SSL certificates.
          default: false
        sslExpiryThreshold:
          type: integer
          description: At what moment in time to start alerting on SSL certificates.
          default: 30
          minimum: 1
          maximum: 30
        autoSubscribe:
          type: boolean
          description: Automatically subscribe newly created checks to this alert channel.
          default: false
      required:
        - type
        - config
    AlertChannel:
      type: object
      properties:
        id:
          type: number
          example: 1
          x-constraint:
            sign: positive
        type:
          $ref: '#/components/schemas/Model5'
        config:
          $ref: '#/components/schemas/AlertChannelConfig'
        subscriptions:
          $ref: '#/components/schemas/AlertChanelSubscriptionList'
        sendRecovery:
          type: boolean
        sendFailure:
          type: boolean
        sendDegraded:
          type: boolean
        sslExpiry:
          type: boolean
          description: Determines if an alert should be sent for expiring SSL certificates.
          default: false
        sslExpiryThreshold:
          type: integer
          description: At what moment in time to start alerting on SSL certificates.
          default: 30
          minimum: 1
          maximum: 30
        autoSubscribe:
          type: boolean
          description: Automatically subscribe newly created checks to this alert channel.
          default: false
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
          nullable: true
      required:
        - id
        - type
        - config
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
    PaymentRequiredError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 402
        error:
          $ref: '#/components/schemas/Model7'
        message:
          type: string
          example: Payment Required
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
    AlertChanelSubscriptionList:
      type: array
      description: All checks subscribed to this channel.
      example: []
      items:
        $ref: '#/components/schemas/AlertChanelSubscription'
    Model6:
      type: string
      example: SMS
      enum:
        - EMAIL
        - SLACK
        - WEBHOOK
        - SMS
        - PAGERDUTY
        - OPSGENIE
        - CALL
    AlertChannelCreateConfig:
      type: object
    Model5:
      type: string
      example: SMS
      enum:
        - EMAIL
        - SLACK
        - WEBHOOK
        - SMS
        - PAGERDUTY
        - OPSGENIE
        - CALL
    AlertChannelConfig:
      type: object
      description: >-
        The configuration details for this alert channel. These can be very
        different based on the type of the channel.
    error:
      type: string
      enum:
        - Unauthorized
    attributes:
      type: object
    Model7:
      type: string
      enum:
        - Payment Required
    Model1:
      type: string
      enum:
        - Forbidden
    Model2:
      type: string
      enum:
        - Too Many Requests
    AlertChanelSubscription:
      type: object
      properties:
        id:
          type: number
          example: 1
        checkId:
          type: string
          example: 47ccf418-6224-429c-a096-637364249882
          nullable: true
          x-format:
            guid: true
        groupId:
          type: number
          example: 'null'
          nullable: true
          x-constraint:
            sign: positive
        activated:
          type: boolean
      required:
        - activated
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