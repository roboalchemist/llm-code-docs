# Source: https://docs.edgeimpulse.com/apis/studio/jobs/version-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Version project

> Create a new version of the project. This stores all data and configuration offsite. If you have access to the enterprise version of Edge Impulse you can store your data in your own storage buckets (only through JWT token authentication).



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/jobs/version
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
  /api/{projectId}/jobs/version:
    post:
      tags:
        - Jobs
      summary: Version project
      description: >-
        Create a new version of the project. This stores all data and
        configuration offsite. If you have access to the enterprise version of
        Edge Impulse you can store your data in your own storage buckets (only
        through JWT token authentication).
      operationId: startVersionJob
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProjectVersionRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartJobResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
  schemas:
    ProjectVersionRequest:
      type: object
      required:
        - description
        - makePublic
      properties:
        bucketId:
          type: integer
          description: Data bucket ID. Keep empty to store in Edge Impulse hosted storage.
        description:
          type: string
        makePublic:
          type: boolean
          description: Whether to make this version available on a public URL.
        runModelTestingWhileVersioning:
          type: boolean
          description: >-
            Whether to run model testing when creating this version (if this
            value is omitted, it will use the current state of
            'runModelTestingWhileVersioning' that is returned in
            ListVersionsResponse).
    StartJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Job identifier. Status updates will include this identifier.
              example: 12873488112
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