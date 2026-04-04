# Source: https://checklyhq.com/docs/api-reference/private-locations/retrieve-a-private-location.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a private location

> Show details of a specific private location.



## OpenAPI

````yaml get /v1/private-locations/{id}
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
  /v1/private-locations/{id}:
    get:
      tags:
        - Private locations
      summary: Retrieve a private location
      description: Show details of a specific private location.
      operationId: getV1PrivatelocationsId
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
                $ref: '#/components/schemas/privateLocationsSchema'
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
    privateLocationsSchema:
      type: object
      properties:
        id:
          type: string
          example: 0baf2a80-7266-44af-b56c-2af7086782ee
          x-format:
            guid: true
        name:
          type: string
          description: The name assigned to the private location.
          example: New Private Location
        slugName:
          type: string
          description: Valid slug name.
          example: new-private-location
        icon:
          type: string
          description: The private location icon.
          example: location
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date
          nullable: true
        keys:
          $ref: '#/components/schemas/Model224'
        proxyUrl:
          type: string
          description: >-
            A proxy for outgoing API check HTTP calls from your private
            location.
          example: https://user:password@164.92.149.127:3128
          nullable: true
        lastSeen:
          type: string
          format: date
          nullable: true
        agentCount:
          type: number
          nullable: true
        minAgentVersion:
          type: string
          description: >-
            The lowest agent version currently connected to this private
            location.
          nullable: true
        runningAgents:
          $ref: '#/components/schemas/runningAgents'
      required:
        - id
        - name
        - slugName
        - created_at
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
    Model224:
      type: array
      items:
        $ref: '#/components/schemas/privateLocationKeys'
    runningAgents:
      type: array
      description: >-
        A list of agent versions and their counts currently connected to this
        private location.
      items:
        $ref: '#/components/schemas/RunningAgent'
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
    privateLocationKeys:
      type: object
      properties:
        id:
          type: string
          example: fed3ada8-7d9b-4634-a0fe-471afe0518b6
          x-format:
            guid: true
        rawKey:
          type: string
          example: pl_a89026d28a0c45cf9e11b4c3637f3912
        maskedKey:
          type: string
          description: The masked key value.
          example: ...6a1e
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date
          nullable: true
      required:
        - id
        - rawKey
        - maskedKey
        - created_at
    RunningAgent:
      type: object
      properties:
        version:
          type: string
        count:
          type: number
        agents:
          $ref: '#/components/schemas/agents'
      required:
        - version
        - count
        - agents
    agents:
      type: array
      items:
        $ref: '#/components/schemas/RunningAgentInfo'
    RunningAgentInfo:
      type: object
      properties:
        id:
          type: string
        lastSeenAt:
          type: string
      required:
        - id
        - lastSeenAt
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