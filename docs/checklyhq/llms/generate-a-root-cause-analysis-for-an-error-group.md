# Source: https://checklyhq.com/docs/api-reference/rocky-ai/generate-a-root-cause-analysis-for-an-error-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Asynchronously generates a root cause analysis for a specific error group. Returns an `id` which you can use to poll the `/root-cause-analyses/{id}` endpoint.

> Asynchronously generates a root cause analysis for a specific error group. Returns an `id` which you can use to poll the `/root-cause-analyses/{id}` endpoint.



## OpenAPI

````yaml post /v1/root-cause-analyses/error-groups/{errorGroupId}
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
  /v1/root-cause-analyses/error-groups/{errorGroupId}:
    post:
      tags:
        - Rocky AI
      summary: >-
        Asynchronously generates a root cause analysis for a specific error
        group. Returns an `id` which you can use to poll the
        `/root-cause-analyses/{id}` endpoint.
      description: >-
        Asynchronously generates a root cause analysis for a specific error
        group. Returns an `id` which you can use to poll the
        `/root-cause-analyses/{id}` endpoint.
      operationId: postV1RootcauseanalysesErrorgroupsErrorgroupid
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
        - name: errorGroupId
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PostRcaErrorGroup'
      responses:
        '202':
          description: Accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model226'
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
    PostRcaErrorGroup:
      type: object
      nullable: true
      properties:
        userContext:
          type: string
          description: >-
            Optional user defined context to provide extra details useful for
            the user impact and root cause analysis.
          default: ''
          nullable: true
          maxLength: 256
    Model226:
      type: object
      properties:
        id:
          type: string
          x-format:
            guid: true
      required:
        - id
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
    Model7:
      type: string
      enum:
        - Payment Required
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