# Source: https://checklyhq.com/docs/api-reference/alert-channels/update-the-subscriptions-of-an-alert-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update the subscriptions of an alert channel

> Update the subscriptions of an alert channel. Use this to add a check to an alert channel so failure and recovery alerts are send out for that check. Note: when passing the subscription object, you can only specify a "checkId" or a "groupId, not both.



## OpenAPI

````yaml put /v1/alert-channels/{id}/subscriptions
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
  /v1/alert-channels/{id}/subscriptions:
    put:
      tags:
        - Alert channels
      summary: Update the subscriptions of an alert channel
      description: >-
        Update the subscriptions of an alert channel. Use this to add a check to
        an alert channel so failure and recovery alerts are send out for that
        check. Note: when passing the subscription object, you can only specify
        a "checkId" or a "groupId, not both.
      operationId: putV1AlertchannelsIdSubscriptions
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
        - name: id
          in: path
          schema:
            type: integer
            x-constraint:
              sign: positive
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AlertChannelSubscriptionCreate'
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AlertChanelSubscription'
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
    AlertChannelSubscriptionCreate:
      type: object
      properties:
        checkId:
          type: string
          description: You can either pass a checkId or a groupId, but not both.
          example: 0bbfc00c-44df-46a7-a4d9-ba38deca8bfd
          nullable: true
          x-format:
            guid: true
        groupId:
          type: number
          description: You can either pass a checkId or a groupId, but not both.
          example: 'null'
          nullable: true
          x-constraint:
            sign: positive
        activated:
          type: boolean
      required:
        - activated
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