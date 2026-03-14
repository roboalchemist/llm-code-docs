# Source: https://docs.edgeimpulse.com/apis/studio/impulse/update-impulse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update impulse

> Update the impulse for this project.  If you specify `impulseId` then that impulse is created/updated, otherwise the default impulse is created/updated.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/impulse/update
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
  /api/{projectId}/impulse/update:
    post:
      tags:
        - Impulse
      summary: Update impulse
      description: >-
        Update the impulse for this project.  If you specify `impulseId` then
        that impulse is created/updated, otherwise the default impulse is
        created/updated.
      operationId: updateImpulse
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateImpulseRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
      schema:
        type: integer
  schemas:
    UpdateImpulseRequest:
      type: object
      properties:
        name:
          type: string
        tags:
          type: array
          items:
            type: string
        type:
          $ref: '#/components/schemas/ImpulseType'
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