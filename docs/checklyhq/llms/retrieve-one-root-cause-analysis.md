# Source: https://checklyhq.com/docs/api-reference/rocky-ai/retrieve-one-root-cause-analysis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Show details of a specific root cause analysis. Use the `id` returned from the POST endpoint to poll until this endpoint stops returning a 404.

> Show details of a specific root cause analysis. Use the `id` returned from the POST endpoint to poll until this endpoint stops returning a 404.



## OpenAPI

````yaml get /v1/root-cause-analyses/{id}
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
  /v1/root-cause-analyses/{id}:
    get:
      tags:
        - Rocky AI
      summary: >-
        Show details of a specific root cause analysis. Use the `id` returned
        from the POST endpoint to poll until this endpoint stops returning a
        404.
      description: >-
        Show details of a specific root cause analysis. Use the `id` returned
        from the POST endpoint to poll until this endpoint stops returning a
        404.
      operationId: getV1RootcauseanalysesId
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
                $ref: '#/components/schemas/GetRca'
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
    GetRca:
      type: object
      properties:
        id:
          type: string
          x-format:
            guid: true
        checkType:
          type: string
          description: Type of check that triggered this analysis, e.g. "API" or "BROWSER"
        provider:
          type: string
          description: AI provider used for the analysis
        model:
          type: string
          description: AI model used for the analysis
        checkId:
          type: string
          nullable: true
          x-format:
            guid: true
        errorGroupId:
          type: string
          nullable: true
          x-format:
            guid: true
        durationMs:
          type: number
          description: Time taken to generate the analysis in milliseconds
        analysis:
          $ref: '#/components/schemas/analysis'
        created_at:
          type: string
          format: date
      required:
        - id
        - checkType
        - provider
        - model
        - durationMs
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
    analysis:
      type: object
      properties:
        classification:
          type: string
          description: High-level error categorization. e.g. "INFRA ERROR"
        userImpact:
          type: string
          description: Human-readable summary of how this failure affects end users
        rootCause:
          type: string
          description: Explanation of the underlying cause of the failure
        codeFix:
          type: string
          description: Suggested code or configuration change to resolve the issue
          nullable: true
        evidence:
          $ref: '#/components/schemas/evidence'
        referenceLinks:
          $ref: '#/components/schemas/referenceLinks'
      required:
        - classification
        - userImpact
        - rootCause
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
    evidence:
      type: array
      description: Supporting evidence derived from check result artifacts
      nullable: true
      items:
        $ref: '#/components/schemas/Model228'
    referenceLinks:
      type: array
      description: Links to relevant documentation or external resources
      nullable: true
      items:
        $ref: '#/components/schemas/Model229'
    Model228:
      type: object
      properties:
        artifacts:
          $ref: '#/components/schemas/artifacts'
        description:
          type: string
          description: Explanation of how this evidence support the root cause analysis
      required:
        - artifacts
        - description
    Model229:
      type: object
      properties:
        url:
          type: string
          description: URL of the reference resource
          x-format:
            uri: true
        title:
          type: string
          description: Display title for the link
      required:
        - url
        - title
    artifacts:
      type: array
      description: Artifacts referenced by this piece of evidence
      items:
        $ref: '#/components/schemas/Model227'
    Model227:
      type: object
      properties:
        name:
          type: string
          description: Identifier of the artifact, e.g. "HTTP_REQUEST" or "TIMING_PHASES"
        type:
          type: string
          description: Category of the artifact, e.g. "REQUEST", "TIMINGS", or "TRACE"
      required:
        - name
        - type
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