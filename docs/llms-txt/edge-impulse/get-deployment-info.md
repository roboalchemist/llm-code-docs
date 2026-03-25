# Source: https://docs.edgeimpulse.com/apis/studio/deployment/get-deployment-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get deployment info

> Gives information on whether a deployment was already built for a type



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/deployment
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
  /api/{projectId}/deployment:
    get:
      tags:
        - Deployment
      summary: Get deployment info
      description: Gives information on whether a deployment was already built for a type
      operationId: getDeployment
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DeploymentTypeParameter'
        - $ref: '#/components/parameters/ModelTypeParameter'
        - $ref: '#/components/parameters/ModelEngineParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetDeploymentResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    DeploymentTypeParameter:
      name: type
      in: query
      required: true
      description: >-
        The name of the built target. You can find this by listing all
        deployment targets through `listDeploymentTargetsForProject` (via `GET
        /v1/api/{projectId}/deployment/targets`) and see the `format` type.
      schema:
        type: string
    ModelTypeParameter:
      name: modelType
      in: query
      required: false
      description: >-
        Optional model type of the build (if not, it uses the settings in the
        Keras block)
      schema:
        $ref: '#/components/schemas/KerasModelTypeEnum'
    ModelEngineParameter:
      name: engine
      in: query
      required: false
      description: >-
        Optional engine for the build (if not, it uses the default engine for
        the deployment target)
      schema:
        $ref: '#/components/schemas/DeploymentTargetEngine'
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
      schema:
        type: integer
  schemas:
    GetDeploymentResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - hasDeployment
          properties:
            hasDeployment:
              type: boolean
            version:
              type: integer
    KerasModelTypeEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
        - requiresRetrain
    DeploymentTargetEngine:
      type: string
      enum:
        - tflite
        - tflite-eon
        - tflite-eon-ram-optimized
        - tensorrt
        - tensaiflow
        - drp-ai
        - tidl
        - akida
        - syntiant
        - memryx
        - neox
        - ethos-linux
        - st-aton
        - ceva-npn
        - nordic-axon
        - vlm-connector
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