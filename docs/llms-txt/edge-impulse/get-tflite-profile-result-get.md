# Source: https://docs.edgeimpulse.com/apis/studio/jobs/get-tflite-profile-result-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get TFLite profile result (GET)

> Get the results from a job started from startProfileTfliteJob (via a GET request).



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/jobs/profile-tflite/{jobId}/result
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
  /api/{projectId}/jobs/profile-tflite/{jobId}/result:
    get:
      tags:
        - Jobs
      summary: Get TFLite profile result (GET)
      description: >-
        Get the results from a job started from startProfileTfliteJob (via a GET
        request).
      operationId: getProfileTfliteJobResult
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/JobIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProfileTfLiteResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    JobIdParameter:
      name: jobId
      in: path
      required: true
      description: Job ID
      schema:
        type: integer
  schemas:
    ProfileTfLiteResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/ProfileModelInfo'
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
    ProfileModelInfo:
      type: object
      required:
        - variant
        - device
        - tfliteFileSizeBytes
        - isSupportedOnMcu
        - customMetrics
        - hasPerformance
      properties:
        variant:
          $ref: '#/components/schemas/KerasModelVariantEnum'
        device:
          type: string
        tfliteFileSizeBytes:
          type: integer
        isSupportedOnMcu:
          type: boolean
        memory:
          type: object
          properties:
            tflite:
              $ref: '#/components/schemas/ProfileModelInfoMemoryDetails'
            eon:
              $ref: '#/components/schemas/ProfileModelInfoMemoryDetails'
            eonRamOptimized:
              $ref: '#/components/schemas/ProfileModelInfoMemoryDetails'
        timePerInferenceMs:
          type: integer
        mcuSupportError:
          type: string
        customMetrics:
          description: Custom, device-specific performance metrics
          type: array
          items:
            $ref: '#/components/schemas/KerasCustomMetric'
        hasPerformance:
          description: If false, then no metrics are available for this target
          type: boolean
        profilingError:
          description: Specific error during profiling (e.g. model not supported)
          type: string
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
    ProfileModelInfoMemoryDetails:
      type: object
      required:
        - ram
        - rom
        - arenaSize
      properties:
        ram:
          type: integer
          description: Estimated amount of RAM required by the model, measured in bytes
        rom:
          type: integer
          description: Estimated amount of ROM required by the model, measured in bytes
        arenaSize:
          type: integer
          description: Estimated arena size required for model inference, measured in bytes
    KerasCustomMetric:
      type: object
      required:
        - name
        - value
      properties:
        name:
          description: The name of the metric
          type: string
        value:
          description: The value of this metric for this model type
          type: string
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