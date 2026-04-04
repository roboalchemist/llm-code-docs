# Source: https://checklyhq.com/docs/api-reference/check-results/retrieve-a-check-result.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a check result

> Show details of a specific check result.



## OpenAPI

````yaml get /v1/check-results/{checkId}/{checkResultId}
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
  /v1/check-results/{checkId}/{checkResultId}:
    get:
      tags:
        - Check results
      summary: Retrieve a check result
      description: Show details of a specific check result.
      operationId: getV1CheckresultsCheckidCheckresultid
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
        - name: checkResultId
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckResult'
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
    CheckResult:
      type: object
      properties:
        id:
          type: string
          description: The unique ID of this result.
        name:
          type: string
          description: The name of the check.
        checkId:
          type: string
          description: The ID of the check.
        hasFailures:
          type: boolean
          description: >-
            Describes if any failure has occurred during this check run. This is
            should be your mainmain focus for assessing API or browser check
            behaviour. Assertions that fail, timeouts or failing scripts all
            resolve tothis value being true.
        hasErrors:
          type: boolean
          description: >-
            Describes if an internal error has occured in Checkly's backend.
            This should be false in almost all cases.
        isDegraded:
          type: boolean
          description: >-
            A check is degraded if it is over the degradation limit set by the
            "degradedResponseTime" field on the check. Applies only to API
            checks.
          nullable: true
        overMaxResponseTime:
          type: boolean
          description: >-
            Set to true if the response time is over the limit set by the
            "maxResponseTime" field on the check. Applies only to API checks.
          nullable: true
        runLocation:
          type: string
          description: What data center location this check result originated from.
        startedAt:
          type: string
          format: date-time
          nullable: true
        stoppedAt:
          type: string
          format: date-time
          nullable: true
        created_at:
          type: string
          format: date-time
        responseTime:
          type: number
          description: >-
            Describes the time it took to execute relevant parts of this check.
            Any setup timeor system time needed to start executing this check in
            the Checkly backend is not part of this.
        apiCheckResult:
          $ref: '#/components/schemas/CheckResultAPI'
        browserCheckResult:
          $ref: '#/components/schemas/CheckResultBrowser'
        multiStepCheckResult:
          $ref: '#/components/schemas/MultiStepResultBrowser'
        checkRunId:
          type: number
          description: The id of the specific check run that created this check result.
        attempts:
          type: number
          description: >-
            How often this check was retried. This will be larger than 0 when
            double checking is enabled.
        resultType:
          $ref: '#/components/schemas/resultType'
        sequenceId:
          type: string
          description: >-
            The sequence ID of the check run. This is used to group check runs
            with multiple attempts together.
          example: 2dbfa2a3-5477-45ea-ac33-ee55b8ea66ff
          nullable: true
          x-format:
            guid: true
      required:
        - resultType
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
    CheckResultAPI:
      type: object
      description: The response data for an API check.
      nullable: true
      properties:
        assertions:
          $ref: '#/components/schemas/assertions'
        request:
          $ref: '#/components/schemas/request'
        response:
          $ref: '#/components/schemas/response'
        requestError:
          type: string
          description: Describes if an error occurred on the request.
          example: 'null'
          nullable: true
        jobLog:
          $ref: '#/components/schemas/jobLog'
        jobAssets:
          $ref: '#/components/schemas/jobAssets'
        pcapDataUrl:
          type: string
          description: Packet capture data if available as redirect/download URL.
          nullable: true
    CheckResultBrowser:
      type: object
      description: The response data for a browser check.
      example: 'null'
      nullable: true
      properties:
        type:
          type: string
          description: The type of framework the check is using.
          example: PLAYWRIGHT
        traceSummary:
          $ref: '#/components/schemas/traceSummary'
        pages:
          $ref: '#/components/schemas/pages'
        playwrightTestVideos:
          $ref: '#/components/schemas/playwrightTestVideos'
        errors:
          $ref: '#/components/schemas/errors'
        endTime:
          type: number
          description: End time of the check run.
          example: 1648573423995
        startTime:
          type: number
          description: Start time of the check run.
          example: 1648573423994
        runtimeVersion:
          type: string
          description: Active runtime version.
          example: '2023.09'
        jobLog:
          $ref: '#/components/schemas/Model53'
        jobAssets:
          $ref: '#/components/schemas/jobAssets'
        playwrightTestTraces:
          $ref: '#/components/schemas/playwrightTestTraces'
        playwrightTestJsonReportFile:
          type: string
          description: Playwright Test JSON report.
          example: >-
            https://api.checklyhq.com/v1/assets/checkRunData/eu-central-1/00000000-0000-0000-0000-0000000000/00000000-0000-0000-0000-0000000000/1675691025832/report.json
    MultiStepResultBrowser:
      type: object
      description: The response data for a multi-step check.
      example: 'null'
      nullable: true
      properties:
        errors:
          $ref: '#/components/schemas/errors'
        endTime:
          type: number
          description: End time of the check run.
          example: 1648573423995
        startTime:
          type: number
          description: Start time of the check run.
          example: 1648573423994
        runtimeVersion:
          type: string
          description: Active runtime version.
          example: '2023.09'
        jobLog:
          $ref: '#/components/schemas/Model54'
        jobAssets:
          $ref: '#/components/schemas/jobAssets'
        playwrightTestTraces:
          $ref: '#/components/schemas/playwrightTestTraces'
        playwrightTestJsonReportFile:
          type: string
          description: Playwright Test JSON report.
          example: >-
            https://api.checklyhq.com/v1/assets/checkRunData/eu-central-1/00000000-0000-0000-0000-0000000000/00000000-0000-0000-0000-0000000000/1675691025832/report.json
    resultType:
      type: string
      description: >-
        The type of result. FINAL means this is the final result of the check
        run. ATTEMPT means this is a result of a double check attempt.
      example: FINAL
      default: FINAL
      enum:
        - FINAL
        - ATTEMPT
        - ALL
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
    assertions:
      type: array
      description: List of API check assertions.
      example:
        - source: STATUS_CODE
          target: 200
      nullable: true
      items:
        type: string
    request:
      type: object
      description: The request for the API.
      properties:
        method:
          type: string
          example: GET
        url:
          type: string
          example: https://api.checklyhq.com
        data:
          type: string
          example: ''
        headers:
          $ref: '#/components/schemas/headers'
        params:
          $ref: '#/components/schemas/params'
    response:
      type: object
      description: The API response.
      properties:
        status:
          type: number
          example: 200
        statusText:
          type: string
          example: OK
        body:
          type: string
          example: <title> Checkly Public API </title>
        headers:
          $ref: '#/components/schemas/headers'
        timings:
          $ref: '#/components/schemas/timings'
        timingPhases:
          $ref: '#/components/schemas/timingPhases'
    jobLog:
      type: object
      description: Check run log results.
      nullable: true
    jobAssets:
      type: array
      description: Assets generated from the check run.
      example: 'null'
      nullable: true
      items:
        type: string
    traceSummary:
      type: object
      description: The summary of errors in the check run.
    pages:
      type: array
      description: List of pages used on the check run.
      example:
        - url: https://www.checklyhq.com/
          webVitals:
            CLS:
              score: GOOD
              value: 0.000146484375
      items:
        type: string
    playwrightTestVideos:
      type: array
      description: List of Playwright Test videos.
      example:
        - >-
          https://api.checklyhq.com/v1/assets/checkRunData/eu-central-1/00000000-0000-0000-0000-0000000000/00000000-0000-0000-0000-0000000000/1675691025832/visit-page-and-take-screenshot-1675691043856.webm
      items:
        type: string
    errors:
      type: array
      description: List of errors on the check run.
      example: []
      items:
        type: string
    Model53:
      type: array
      description: Check run log results.
      example:
        time: 1648573423995
        msg: Starting job
        level: DEBUG
      nullable: true
      items:
        type: string
    playwrightTestTraces:
      type: array
      description: List of Playwright Test traces.
      example:
        - >-
          https://api.checklyhq.com/v1/assets/checkRunData/eu-central-1/00000000-0000-0000-0000-0000000000/00000000-0000-0000-0000-0000000000/1675691025832/visit-page-and-take-screenshot.zip
      items:
        type: string
    Model54:
      type: array
      description: Check run log results.
      example:
        time: 1648573423995
        msg: Starting job
        level: DEBUG
      nullable: true
      items:
        type: string
    headers:
      type: object
    params:
      type: object
    timings:
      type: object
    timingPhases:
      type: object
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