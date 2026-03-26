# Source: https://checklyhq.com/docs/api-reference/check-sessions/trigger-a-new-check-session.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger a new check session

> Starts a check session for each check that matches the provided target filters. If no filters are given, matches all eligible checks.

This endpoint does not wait for the check session to complete. Use the `GET /v1/check-sessions/{checkSessionId}/completion` or `GET /v1/check-sessions/{checkSessionId}` endpoints to track progress if needed.

Standard alerting rules apply to finished check runs.

Equivalent to the _Schedule Now_ button in the UI.



## OpenAPI

````yaml post /v1/check-sessions/trigger
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
  /v1/check-sessions/trigger:
    post:
      tags:
        - Check sessions
        - Triggers
      summary: Trigger a new check session
      description: >-
        Starts a check session for each check that matches the provided target
        filters. If no filters are given, matches all eligible checks.


        This endpoint does not wait for the check session to complete. Use the
        `GET /v1/check-sessions/{checkSessionId}/completion` or `GET
        /v1/check-sessions/{checkSessionId}` endpoints to track progress if
        needed.


        Standard alerting rules apply to finished check runs.


        Equivalent to the _Schedule Now_ button in the UI.
      operationId: postV1ChecksessionsTrigger
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TriggerCheckSessionRequestPayload'
      responses:
        '201':
          description: Returns a check session for each check matching target conditions.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TriggerCheckSessionResponse'
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
        '404':
          description: Returned when there are no matching checks.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NoMatchingChecksFoundErrorResponse'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    TriggerCheckSessionRequestPayload:
      type: object
      properties:
        target:
          $ref: '#/components/schemas/TriggerCheckSessionTarget'
        refreshCache:
          type: boolean
          description: >-
            If true, the runner will skip existing caches and install
            dependencies from scratch. This applies only to Playwright Check
            Suites.
          default: false
    TriggerCheckSessionResponse:
      type: object
      description: Returns a check session for each check matching target conditions.
      properties:
        sessions:
          $ref: '#/components/schemas/sessions'
      required:
        - sessions
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
    NoMatchingChecksFoundErrorResponse:
      type: object
      description: Returned when there are no matching checks.
      properties:
        statusCode:
          type: number
          enum:
            - 404
        error:
          type: string
          example: Not Found
        message:
          type: string
          example: No matching checks were found.
      required:
        - statusCode
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
    TriggerCheckSessionTarget:
      type: object
      properties:
        matchTags:
          $ref: '#/components/schemas/matchTags'
        checkId:
          $ref: '#/components/schemas/checkId'
    sessions:
      type: array
      description: A list of check sessions, with one check session for each check.
      items:
        $ref: '#/components/schemas/CheckSession'
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
    matchTags:
      type: array
      description: >-
        Match checks with the given tags. Group tags also match.


        The value is a two-dimensional array. The top level array defines `OR`
        conditions, and the second level `AND` conditions. Tags can also be
        prefixed with `!` to only match checks without those tags.


        Example: `[[a, b], [a, c, !d]]` means `(a && b) || (a && c && !d)`.
      example:
        - - production
          - '!skip-e2e'
      items:
        $ref: '#/components/schemas/Model55'
    checkId:
      type: array
      description: Match checks with the given identifiers.
      example:
        - a4cd4ad9-4815-4a9e-92d2-0a7c562ee69a
      x-constraint:
        single: true
      items:
        type: string
        x-format:
          guid: true
    CheckSession:
      type: object
      properties:
        checkSessionId:
          type: string
          description: The unique identifier of the check session.
          example: 8166fa86-c9b4-4162-8541-d380c6c212d8
          x-format:
            guid: true
        checkSessionLink:
          type: string
          description: A link to the check session.
          example: >-
            https://app.checklyhq.com/accounts/1397c172-1938-4973-a225-5862298e571a/checks/a4cd4ad9-4815-4a9e-92d2-0a7c562ee69a/check-sessions/8166fa86-c9b4-4162-8541-d380c6c212d8
          x-format:
            uri: true
        checkId:
          type: string
          description: The ID of the check.
          example: a4cd4ad9-4815-4a9e-92d2-0a7c562ee69a
          x-format:
            guid: true
        checkType:
          $ref: '#/components/schemas/Model56'
        name:
          type: string
          example: Example API Check
        status:
          $ref: '#/components/schemas/Model57'
        startedAt:
          type: string
          format: date-time
          description: The date and time when the session started.
          example: '2025-08-28T18:23:40.262Z'
        stoppedAt:
          type: string
          format: date-time
          description: The date and time when the session stopped.
          example: '2025-08-28T18:28:40.993Z'
          nullable: true
        timeElapsed:
          type: number
          description: The time the check session took, in milliseconds.
          example: 300731
        runLocations:
          $ref: '#/components/schemas/runLocations'
      required:
        - checkSessionId
        - checkSessionLink
        - checkId
        - checkType
        - status
        - startedAt
        - timeElapsed
        - runLocations
    Model55:
      type: array
      x-constraint:
        single: true
      items:
        type: string
    Model56:
      type: string
      example: API
      enum:
        - AGENTIC
        - API
        - BROWSER
        - ICMP
        - MULTI_STEP
        - TCP
        - PLAYWRIGHT
        - URL
        - DNS
    Model57:
      type: string
      description: The status of the check session.
      example: PASSED
      enum:
        - STARTED
        - PROGRESS
        - FAILED
        - PASSED
        - DEGRADED
        - PROGRESS_FAILED
        - PROGRESS_DEGRADED
        - TIMED_OUT
    runLocations:
      type: array
      description: The run locations of the check session.
      example:
        - us-east-1
        - eu-central-1
      items:
        type: string
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