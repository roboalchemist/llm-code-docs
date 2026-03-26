# Source: https://checklyhq.com/docs/api-reference/alert-notifications/lists-all-alert-notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lists all alert notifications

> Lists the alert notifications that have been sent for your account. You can filter by alert channel ID or limit to only failing notifications.
Use the `to` and `from` parameters to specify a date range (UNIX timestamp in seconds). This endpoint will return data within a 24-hour timeframe. If the `from` and `to` params are set, they must be at most 24 hours apart. If none are set, we will consider the `to` param to be now and the `from` param to be 24 hours earlier. If only the `to` param is set we will set `from` to be 24 hours earlier. If only the `from` param is set we will consider the `to` param to be 24 hours later.
**Rate-limiting is applied to this endpoint, you can send 5 requests / 10 seconds at most.**



## OpenAPI

````yaml get /v1/alert-notifications
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
  /v1/alert-notifications:
    get:
      tags:
        - Alert notifications
      summary: Lists all alert notifications
      description: >-
        Lists the alert notifications that have been sent for your account. You
        can filter by alert channel ID or limit to only failing notifications.

        Use the `to` and `from` parameters to specify a date range (UNIX
        timestamp in seconds). This endpoint will return data within a 24-hour
        timeframe. If the `from` and `to` params are set, they must be at most
        24 hours apart. If none are set, we will consider the `to` param to be
        now and the `from` param to be 24 hours earlier. If only the `to` param
        is set we will set `from` to be 24 hours earlier. If only the `from`
        param is set we will consider the `to` param to be 24 hours later.

        **Rate-limiting is applied to this endpoint, you can send 5 requests /
        10 seconds at most.**
      operationId: getV1Alertnotifications
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
        - name: from
          in: query
          schema:
            type: string
            format: date
            description: >-
              Select records up from this UNIX timestamp (>= date). Defaults to
              now - 6 hours.
          description: >-
            Select records up from this UNIX timestamp (>= date). Defaults to
            now - 6 hours.
        - name: to
          in: query
          schema:
            type: string
            format: date
            description: >-
              Optional. Select records up to this UNIX timestamp (< date).
              Defaults to 6 hours after "from".
          description: >-
            Optional. Select records up to this UNIX timestamp (< date).
            Defaults to 6 hours after "from".
        - name: alertChannelId
          in: query
          schema:
            type: integer
            description: Limit results to an alert channel
            x-constraint:
              sign: positive
          description: Limit results to an alert channel
        - name: hasFailures
          in: query
          schema:
            type: boolean
            description: Sending the alert notification was unsuccessful
          description: Sending the alert notification was unsuccessful
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AlertNotificationList'
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
    AlertNotificationList:
      type: array
      items:
        $ref: '#/components/schemas/AlertNotification'
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
    AlertNotification:
      type: object
      properties:
        id:
          type: string
          description: The unique ID of this alert notification.
        type:
          $ref: '#/components/schemas/Model8'
        status:
          $ref: '#/components/schemas/status'
        alertConfig:
          $ref: '#/components/schemas/alertConfig'
        notificationResult:
          type: string
          description: >-
            The result of sending the alert notification.For example, this could
            be the response body of the Webhook.
          nullable: true
        timestamp:
          type: string
          format: date-time
          description: The time that the alert was sent.
          nullable: true
        checkType:
          $ref: '#/components/schemas/checkType'
        checkId:
          type: string
          description: The ID of the check.
        checkAlertId:
          type: string
          description: The ID of the check alert.
        alertChannelId:
          type: number
          description: The ID of the alert channel which this alert was sent to.
        checkResultId:
          type: string
          description: The ID of the corresponding check result.
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
    Model8:
      type: string
      description: The type of alert channel (SMS, Slack, Webhook, etc).
      enum:
        - EMAIL
        - SLACK
        - WEBHOOK
        - SMS
        - PAGERDUTY
        - OPSGENIE
        - CALL
    status:
      type: string
      description: The status of the alert.
      enum:
        - IN_PROGRESS
        - SUCCESS
        - FAILURE
        - RATE_LIMITED
    alertConfig:
      type: object
      description: The configuration which was used to send the alert.
    checkType:
      type: string
      description: The type of the check.
      enum:
        - AGENTIC
        - API
        - BROWSER
        - HEARTBEAT
        - ICMP
        - MULTI_STEP
        - TCP
        - PLAYWRIGHT
        - URL
        - DNS
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