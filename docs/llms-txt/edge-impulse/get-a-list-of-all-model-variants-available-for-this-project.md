# Source: https://docs.edgeimpulse.com/apis/studio/projects/get-a-list-of-all-model-variants-available-for-this-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a list of all model variants available for this project

> Get a list of model variants applicable to all trained learn blocks in this project.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/model-variants
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
  /api/{projectId}/model-variants:
    get:
      tags:
        - Projects
      summary: Get a list of all model variants available for this project
      description: >-
        Get a list of model variants applicable to all trained learn blocks in
        this project.
      operationId: getModelVariants
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetModelVariantsResponse'
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
    GetModelVariantsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - modelVariants
          properties:
            modelVariants:
              $ref: '#/components/schemas/AllProjectModelVariants'
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
    AllProjectModelVariants:
      type: array
      description: All model variants relevant for all learn blocks in the project
      items:
        $ref: '#/components/schemas/ProjectModelVariant'
    ProjectModelVariant:
      type: object
      required:
        - variant
        - isReferenceVariant
        - isEnabled
        - isSelected
      properties:
        variant:
          $ref: '#/components/schemas/KerasModelVariantEnum'
        isReferenceVariant:
          type: boolean
          description: >-
            True if this model variant is the default or "reference variant" for
            this project
        isEnabled:
          type: boolean
          description: >-
            True if profiling for this model variant is enabled for the current
            project
        isSelected:
          type: boolean
          description: >-
            True if this is the selected model variant for this project, used to
            keep the same view after refreshing. Update this via
            defaultProfilingVariant in UpdateProjectRequest.
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
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