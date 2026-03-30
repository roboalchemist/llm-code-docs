# Source: https://checklyhq.com/docs/api-reference/check-alerts/list-alerts-for-a-specific-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List alerts for a specific check

> Lists all the alerts for a specific check.
Use the `to` and `from` parameters to specify a date range (UNIX timestamp in seconds). This endpoint will return data within a 6-hour timeframe. If the `from` and `to` params are set, they must be at most 6 hours apart. If none are set, we will consider the `to` param to be now and the `from` param to be 6 hours earlier. If only the `to` param is set we will set `from` to be 6 hours earlier. If only the `from` param is set we will consider the `to` param to be 6 hours later.



## OpenAPI

````yaml get /v1/check-alerts/{checkId}
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
  /v1/check-alerts/{checkId}:
    get:
      tags:
        - Check alerts
      summary: List alerts for a specific check
      description: >-
        Lists all the alerts for a specific check.

        Use the `to` and `from` parameters to specify a date range (UNIX
        timestamp in seconds). This endpoint will return data within a 6-hour
        timeframe. If the `from` and `to` params are set, they must be at most 6
        hours apart. If none are set, we will consider the `to` param to be now
        and the `from` param to be 6 hours earlier. If only the `to` param is
        set we will set `from` to be 6 hours earlier. If only the `from` param
        is set we will consider the `to` param to be 6 hours later.
      operationId: getV1CheckalertsCheckid
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
        - name: checkId
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
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
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckAlertList'
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
    CheckAlertList:
      type: array
      items:
        $ref: '#/components/schemas/CheckAlert'
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
    CheckAlert:
      type: object
      properties:
        id:
          type: string
          description: The unique ID of this alert.
          example: '1'
        name:
          type: string
          description: The name of the check.
          example: API Check
        checkId:
          type: string
          description: The ID of check this alert belongs to.
          example: db147a95-6ed6-44c9-a584-c5dca2db3aaa
        alertType:
          $ref: '#/components/schemas/alertType'
        checkType:
          $ref: '#/components/schemas/Model38'
        runLocation:
          type: string
          description: What data center location this check alert was triggered from.
          example: us-east-1
        responseTime:
          type: number
          description: >-
            Describes the time it took to execute relevant parts of this check.
            Any setup timeor system time needed to start executing this check in
            the Checkly backend is not part of this.
          example: 10
        error:
          type: string
          description: >-
            Any specific error messages that were part of the failing check
            triggering the alert.
          example: OK
          nullable: true
        statusCode:
          type: string
          description: The status code of the response. Only applies to API checks.
          example: '200'
          nullable: true
        created_at:
          type: string
          format: date
          description: The date and time this check alert was created.
        startedAt:
          type: string
          format: date
          description: The date and time this check alert was started.
      required:
        - name
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
    alertType:
      type: string
      description: The type of alert.
      example: ALERT_FAILURE
      enum:
        - NO_ALERT
        - ALERT_FAILURE
        - ALERT_FAILURE_REMAIN
        - ALERT_FAILURE_DEGRADED
        - ALERT_RECOVERY
        - ALERT_DEGRADED
        - ALERT_DEGRADED_REMAIN
        - ALERT_DEGRADED_FAILURE
        - ALERT_DEGRADED_RECOVERY
        - ALERT_SSL
    Model38:
      type: string
      description: The type of the check.
      example: API
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