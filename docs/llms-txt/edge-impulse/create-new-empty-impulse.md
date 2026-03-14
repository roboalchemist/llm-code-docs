# Source: https://docs.edgeimpulse.com/apis/studio/impulse/create-new-empty-impulse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create new empty impulse

> Create a new empty impulse, and return the ID.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/impulse/new
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
  /api/{projectId}/impulse/new:
    post:
      tags:
        - Impulse
      summary: Create new empty impulse
      description: Create a new empty impulse, and return the ID.
      operationId: createNewEmptyImpulse
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateNewEmptyImpulseRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateNewEmptyImpulseResponse'
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
    CreateNewEmptyImpulseRequest:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ImpulseType'
    CreateNewEmptyImpulseResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
            - redirectUrl
          properties:
            id:
              type: integer
              description: ID of the new impulse
            redirectUrl:
              type: string
              description: Link to redirect the user to afterwards
    ImpulseType:
      type: string
      description: >
        Specifies the type of impulse. Options include: - default: Standard Edge
        Impulse pipeline. - BYOM: Impulse that includes a pretrained model. -
        VLM: Impulse created as part of a Vision Learning Model (VLM) workflow.
      enum:
        - default
        - BYOM
        - VLM
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