# Source: https://docs.edgeimpulse.com/apis/studio/jobs/get-impulse-migration-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get impulse migration logs

> Get the logs for the multi-impulse migration job in this project. This is a separate route so public projects can access it. If no multi-impulse migration jobs are present, an error will be thrown.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/jobs/impulse-migration/stdout
openapi: 3.0.0
info:
  title: Edge Impulse API
  version: 1.0.0
servers:
  - url: https://studio.edgeimpulse.com/v1
security:
  - ApiKeyAuthentication: []
  - JWTAuthentication: []
  - JWTHttpHeaderAuthentication: []
  - OAuth2: []
paths:
  /api/{projectId}/jobs/impulse-migration/stdout:
    get:
      tags:
        - Jobs
      summary: Get impulse migration logs
      description: >-
        Get the logs for the multi-impulse migration job in this project. This
        is a separate route so public projects can access it. If no
        multi-impulse migration jobs are present, an error will be thrown.
      operationId: getImpulseMigrationJobsLogs
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/LogLevelParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LogStdoutResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    LimitResultsParameter:
      name: limit
      in: query
      required: false
      description: Maximum number of results
      schema:
        type: integer
    LogLevelParameter:
      name: logLevel
      in: query
      required: false
      description: Log level (error, warn, info, debug)
      schema:
        type: string
        enum:
          - error
          - warn
          - info
          - debug
  schemas:
    LogStdoutResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - stdout
            - totalCount
          properties:
            stdout:
              type: array
              items:
                type: object
                required:
                  - created
                  - data
                properties:
                  created:
                    type: string
                    format: date-time
                  data:
                    type: string
                  logLevel:
                    type: string
                    enum:
                      - error
                      - warn
                      - info
                      - debug
            totalCount:
              type: integer
              description: Total number of logs (only the last 1000 lines are returned)
    GenericApiResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
          description: Whether the operation succeeded
        error:
          type: string
          description: Optional error description (set if 'success' was false)
  securitySchemes:
    ApiKeyAuthentication:
      type: apiKey
      in: header
      name: x-api-key
    JWTAuthentication:
      type: apiKey
      in: cookie
      name: jwt
    JWTHttpHeaderAuthentication:
      type: apiKey
      in: header
      name: x-jwt-token
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: /v1/oauth/authorize
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        implicit:
          authorizationUrl: /v1/oauth/authorize
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        password:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        clientCredentials:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information

````

Built with [Mintlify](https://mintlify.com).