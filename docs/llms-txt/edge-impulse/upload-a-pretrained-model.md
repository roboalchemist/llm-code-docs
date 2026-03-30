# Source: https://docs.edgeimpulse.com/apis/studio/learn/upload-a-pretrained-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a pretrained model

> Upload a pretrained model and receive info back about the input/output tensors. If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/pretrained-model/upload
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
  /api/{projectId}/pretrained-model/upload:
    post:
      tags:
        - Learn
      summary: Upload a pretrained model
      description: >-
        Upload a pretrained model and receive info back about the input/output
        tensors. If you want to deploy a pretrained model from the API, see
        `startDeployPretrainedModelJob`.
      operationId: uploadPretrainedModel
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/UploadPretrainedModelRequest'
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
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
      schema:
        type: integer
  schemas:
    UploadPretrainedModelRequest:
      type: object
      required:
        - modelFile
        - modelFileName
        - modelFileType
      properties:
        modelFile:
          type: string
          format: binary
        modelFileName:
          type: string
        modelFileType:
          type: string
          enum:
            - tflite
            - onnx
            - saved_model
        representativeFeatures:
          type: string
          format: binary
        device:
          description: >-
            MCU used for calculating latency, query `latencyDevices` in
            `listProject` for a list of supported devices (and use the "mcu"
            property here). If this is kept empty then we'll show an overview of
            multiple devices.
          type: string
        overrideInputShape:
          description: >-
            Optional for ONNX files: overrides the input shape of the model.
            This is highly suggested if the model has dynamic dimensions. If
            this field is not set, then all dynamic dimensions will be set to
            '1'.
          type: array
          items:
            type: integer
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