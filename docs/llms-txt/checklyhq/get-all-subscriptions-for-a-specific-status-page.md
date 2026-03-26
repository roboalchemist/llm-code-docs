# Source: https://checklyhq.com/docs/api-reference/status-pages/get-all-subscriptions-for-a-specific-status-page.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all subscriptions for a specific status page

> Get all subscriptions for a specific status page



## OpenAPI

````yaml get /v1/status-pages/{statusPageId}/subscriptions
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
  /v1/status-pages/{statusPageId}/subscriptions:
    get:
      tags:
        - Status Pages
        - Subscriptions
      summary: Get all subscriptions for a specific status page
      description: Get all subscriptions for a specific status page
      operationId: getV1StatuspagesStatuspageidSubscriptions
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
        - name: statusPageId
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
      responses:
        '200':
          description: The list of subscriptions for the status page.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubscriptionsList'
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
    SubscriptionsList:
      type: array
      description: The list of subscriptions for the status page.
      items:
        $ref: '#/components/schemas/Subscription'
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
    Subscription:
      type: object
      properties:
        id:
          type: string
          description: The ID of the subscription.
        type:
          $ref: '#/components/schemas/Model233'
        address:
          type: string
          description: The email address to subscribe to the status page.
          x-format:
            email: true
        status:
          $ref: '#/components/schemas/Model234'
        created_at:
          type: string
          format: date
          description: The date the subscription was created.
        updated_at:
          type: string
          format: date
          description: The date the subscription was last updated.
      required:
        - id
        - type
        - address
        - status
        - created_at
        - updated_at
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
    Model233:
      type: string
      description: The type of subscription.
      enum:
        - EMAIL
    Model234:
      type: string
      description: The status of the subscription.
      enum:
        - PENDING
        - VERIFIED
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