# Source: https://checklyhq.com/docs/api-reference/alert-channels/list-all-alert-channels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all alert channels

> Lists all configured alert channels and their subscribed checks.



## OpenAPI

````yaml get /v1/alert-channels
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
    get:
      tags:
        - Alert channels
      summary: List all alert channels
      description: Lists all configured alert channels and their subscribed checks.
      operationId: getV1Alertchannels
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
        - name: limit
          in: query
          schema:
            type: integer
            description: Limit the number of results
            default: 10
            minimum: 1
            maximum: 100
          description: Limit the number of results
        - name: page
          in: query
          schema:
            type: number
            description: Page number
            default: 1
            x-constraint:
              sign: positive
          description: Page number
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AlertChannelList'
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
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    AlertChannelList:
      type: array
      items:
        $ref: '#/components/schemas/AlertChannel'
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
    Model2:
      type: string
      enum:
        - Too Many Requests
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
    AlertChanelSubscriptionList:
      type: array
      description: All checks subscribed to this channel.
      example: []
      items:
        $ref: '#/components/schemas/AlertChanelSubscription'
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