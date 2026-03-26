# Source: https://checklyhq.com/docs/api-reference/check-sessions/await-the-completion-of-a-check-session.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Await the completion of a check session

> Call this endpoint to await the completion of a check session. A successful response will be returned once the check session reaches its final state (i.e. when it passes or fails).

If the check session takes a long time to complete, the endpoint will return a timeout error code. You should keep calling the endpoint until you receive a successful response, or a non-timeout related error code. If using *curl*, its `--retry` option is suitable.

The successful response of this endpoint is equivalent to the `GET /v1/check-sessions/{checkSessionId}` endpoint's response for a completed check session.



## OpenAPI

````yaml get /v1/check-sessions/{checkSessionId}/completion
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
  /v1/check-sessions/{checkSessionId}/completion:
    get:
      tags:
        - Check sessions
      summary: Await the completion of a check session
      description: >-
        Call this endpoint to await the completion of a check session. A
        successful response will be returned once the check session reaches its
        final state (i.e. when it passes or fails).


        If the check session takes a long time to complete, the endpoint will
        return a timeout error code. You should keep calling the endpoint until
        you receive a successful response, or a non-timeout related error code.
        If using *curl*, its `--retry` option is suitable.


        The successful response of this endpoint is equivalent to the `GET
        /v1/check-sessions/{checkSessionId}` endpoint's response for a completed
        check session.
      operationId: getV1ChecksessionsChecksessionidCompletion
      parameters:
        - name: checkSessionId
          in: path
          schema:
            type: string
            description: The unique identifier of the check session.
            x-format:
              guid: true
          description: The unique identifier of the check session.
          required: true
        - name: maxWaitSeconds
          in: query
          schema:
            type: number
            description: The maximum time to wait for completion, in seconds.
            example: 30
            minimum: 1
            maximum: 30
          description: The maximum time to wait for completion, in seconds.
      responses:
        '200':
          description: Returned when the check session has finished running.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AwaitCheckSessionCompletionResponse'
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
          description: No such check session exists.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckSessionNotFoundErrorResponse'
        '408':
          description: >-
            The check session is still pending, but the server requests a quick
            break. You should call the endpoint again. Optionally, try to
            respect the `Retry-After` header.


            This error code is one of the transient error codes supported by
            *curl*'s `--retry` option.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/AwaitCheckSessionCompletionTryAgainResponse
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    AwaitCheckSessionCompletionResponse:
      type: object
      description: Returned when the check session has finished running.
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
          $ref: '#/components/schemas/Model62'
        name:
          type: string
          example: Example API Check
        status:
          $ref: '#/components/schemas/Model63'
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
        timeElapsed:
          type: number
          description: The time the check session took, in milliseconds.
          example: 300731
        runLocations:
          $ref: '#/components/schemas/runLocations'
        results:
          $ref: '#/components/schemas/Model64'
      required:
        - checkSessionId
        - checkSessionLink
        - checkId
        - checkType
        - status
        - startedAt
        - stoppedAt
        - timeElapsed
        - runLocations
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
    CheckSessionNotFoundErrorResponse:
      type: object
      description: No such check session exists.
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
          example: No such check session.
      required:
        - statusCode
    AwaitCheckSessionCompletionTryAgainResponse:
      type: object
      description: >-
        The check session is still pending, but the server requests a quick
        break. You should call the endpoint again. Optionally, try to respect
        the `Retry-After` header.


        This error code is one of the transient error codes supported by
        *curl*'s `--retry` option.
      properties:
        statusCode:
          type: number
          enum:
            - 408
        error:
          type: string
          example: Request Time-out
        message:
          type: string
          example: >-
            Check session is still in progress, but maximum per-request wait
            time was exceeded. Please retry.
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
    Model62:
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
    Model63:
      type: string
      description: The final status of the check session.
      example: PASSED
      enum:
        - FAILED
        - PASSED
        - DEGRADED
        - TIMED_OUT
    runLocations:
      type: array
      description: The run locations of the check session.
      example:
        - us-east-1
        - eu-central-1
      items:
        type: string
    Model64:
      type: array
      description: The results of the check session.
      items:
        $ref: '#/components/schemas/CheckSessionConciseCheckResult'
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
    CheckSessionConciseCheckResult:
      type: object
      properties:
        checkResultId:
          type: string
          description: The ID of the check result.
          example: 22be3b52-5ec2-4894-9086-b5b4a8b00a89
          x-format:
            guid: true
        checkResultLink:
          type: string
          description: A link to the check result.
          example: >-
            https://app.checklyhq.com/accounts/1397c172-1938-4973-a225-5862298e571a/checks/a4cd4ad9-4815-4a9e-92d2-0a7c562ee69a/check-sessions/8166fa86-c9b4-4162-8541-d380c6c212d8/results/22be3b52-5ec2-4894-9086-b5b4a8b00a89
          x-format:
            uri: true
        checkId:
          type: string
          description: The ID of the check.
          example: a4cd4ad9-4815-4a9e-92d2-0a7c562ee69a
          x-format:
            guid: true
        checkType:
          $ref: '#/components/schemas/Model60'
        name:
          type: string
          example: Example API Check
        runLocation:
          type: string
          description: The location where the check ran.
          example: us-east-1
        resultType:
          $ref: '#/components/schemas/Model61'
        hasErrors:
          type: boolean
          description: Whether the result has errors.
          example: false
        hasFailures:
          type: boolean
          description: Whether the result has failures.
          example: false
        isDegraded:
          type: boolean
          description: Whether the result is degraded.
          example: false
        aborted:
          type: boolean
          description: Whether the check was aborted.
          example: false
      required:
        - checkResultId
        - checkResultLink
        - checkId
        - checkType
        - runLocation
        - resultType
        - hasErrors
        - hasFailures
        - isDegraded
        - aborted
    Model60:
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
    Model61:
      type: string
      description: The type of the result.
      example: FINAL
      enum:
        - FINAL
        - ATTEMPT
        - ALL
      nullable: true
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