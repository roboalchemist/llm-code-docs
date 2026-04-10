# Source: https://docs.edgeimpulse.com/apis/studio/jobs/build-on-device-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build on-device model

> Generate code to run the impulse on an embedded device. When this step is complete use `downloadHistoricDeployment` to download the artefacts. Updates are streamed over the websocket API.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/jobs/build-ondevice-model
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
  /api/{projectId}/jobs/build-ondevice-model:
    post:
      tags:
        - Jobs
      summary: Build on-device model
      description: >-
        Generate code to run the impulse on an embedded device. When this step
        is complete use `downloadHistoricDeployment` to download the artefacts.
        Updates are streamed over the websocket API.
      operationId: buildOnDeviceModelJob
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DeploymentTypeParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BuildOnDeviceModelRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BuildOnDeviceModelResponse'
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
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
      schema:
        type: integer
  schemas:
    BuildOnDeviceModelRequest:
      type: object
      required:
        - engine
      properties:
        engine:
          $ref: '#/components/schemas/DeploymentTargetEngine'
        modelType:
          $ref: '#/components/schemas/KerasModelVariantEnum'
        parameters:
          type: object
          description: >-
            List of custom parameters for this deployment job (see the list of
            parameters that the block exposes in DeploymentTarget#parameters).
          additionalProperties:
            type: string
    BuildOnDeviceModelResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
            - deploymentVersion
          properties:
            id:
              type: integer
              description: Job identifier. Status updates will include this identifier.
              example: 12873488112
            deploymentVersion:
              type: integer
              description: >-
                Deployment version, use `downloadHistoricDeployment` to later
                download the deployment using this identifier.
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
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
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