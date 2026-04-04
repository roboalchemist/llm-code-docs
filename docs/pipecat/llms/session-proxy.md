# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/rest-reference/endpoint/session-proxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pipecat.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Session API

> Send HTTP requests directly to your running Pipecat Cloud agent sessions.

Send HTTP requests to endpoints defined in your running bot. Supports `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`, and `HEAD` methods.

## Request Headers

Headers are forwarded to your bot with these exceptions:

* `host` - Excluded
* `content-length` - Excluded
* `authorization` - Excluded (authentication is handled by the API gateway)

<Note>
  Requires base image version `0.1.2` or later. See the [Session API
  guide](/deployment/pipecat-cloud/guides/session-api) for setup instructions
  and examples.
</Note>


## OpenAPI

````yaml GET /{serviceName}/sessions/{sessionId}/{path}
openapi: 3.0.0
info:
  title: Pipecat Cloud - Session API
  version: 1.0.0
  description: Send HTTP requests directly to running Pipecat Cloud agent sessions
servers:
  - url: https://api.pipecat.daily.co/v1/public
    description: Public API server
security:
  - PublicKeyAuth: []
paths:
  /{serviceName}/sessions/{sessionId}/{path}:
    get:
      summary: Send GET request to session
      description: >-
        Proxies a GET request to an endpoint defined in your running bot. The
        response is returned directly from the bot.
      operationId: sessionProxyGet
      parameters:
        - $ref: '#/components/parameters/ServiceName'
        - $ref: '#/components/parameters/SessionId'
        - $ref: '#/components/parameters/Path'
      responses:
        '200':
          description: Successful response from the bot
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProxiedResponse'
        '400':
          $ref: '#/components/responses/ServiceNotAvailable'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalServerError'
      security:
        - PublicKeyAuth: []
components:
  parameters:
    ServiceName:
      name: serviceName
      in: path
      required: true
      description: Name of the deployed agent
      schema:
        type: string
      example: my-agent
    SessionId:
      name: sessionId
      in: path
      required: true
      description: Session ID returned from the start endpoint
      schema:
        type: string
        format: uuid
      example: 57af5437-97a2-4646-9873-a5c5935bd705
    Path:
      name: path
      in: path
      required: true
      description: The endpoint path defined in your bot using the `@app` decorator
      schema:
        type: string
      example: status
  schemas:
    ProxiedResponse:
      type: object
      description: >-
        Response from your bot endpoint. The schema depends on what your bot
        returns.
      additionalProperties: true
      example:
        status: active
        message_count: 5
        user_name: Alice
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Error message describing what went wrong
        code:
          type: string
          description: Error code for programmatic handling
      required:
        - error
        - code
  responses:
    ServiceNotAvailable:
      description: Service deployment is not available
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            error: >-
              Attempt to start agent when deployment is not in ready state. Is
              your image pull secret valid?
            code: PCC-1001
    Unauthorized:
      description: Invalid or missing API key
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            error: Unauthorized / token expired
            code: '401'
    NotFound:
      description: Service or session not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            error: Service not found
            code: '404'
    InternalServerError:
      description: Internal server error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            error: >-
              Internal server error. Please check logs for more information or
              contact support.
            code: '500'
  securitySchemes:
    PublicKeyAuth:
      type: http
      scheme: bearer
      description: >-
        Authentication using a Pipecat Cloud public API key.


        Generate a public API key from your Dashboard (Settings > API Keys >
        Public > Create key) and include it as a Bearer token in the
        Authorization header.

````