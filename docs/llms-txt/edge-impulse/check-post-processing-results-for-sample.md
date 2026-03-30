# Source: https://docs.edgeimpulse.com/apis/studio/postprocessing/check-post-processing-results-for-sample.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Check post-processing results for sample

> Retrieve post-processing results for a specific sample, e.g. whether it has generated features already.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/post-processing/{postProcessingId}/samples/{sampleId}
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
  /api/{projectId}/post-processing/{postProcessingId}/samples/{sampleId}:
    post:
      tags:
        - PostProcessing
      summary: Check post-processing results for sample
      description: >-
        Retrieve post-processing results for a specific sample, e.g. whether it
        has generated features already.
      operationId: getPostProcessingResultsForSample
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/PostProcessingIdParameter'
        - $ref: '#/components/parameters/SampleIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PostProcessingFeaturesForSampleRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPostProcessingResultsForSampleResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    PostProcessingIdParameter:
      name: postProcessingId
      in: path
      required: true
      description: Post-processing Block ID, use the impulse functions to retrieve the ID
      schema:
        type: integer
    SampleIdParameter:
      name: sampleId
      in: path
      required: true
      description: Sample ID
      schema:
        type: integer
  schemas:
    PostProcessingFeaturesForSampleRequest:
      type: object
      required:
        - config
        - variant
      properties:
        config:
          $ref: '#/components/schemas/PostProcessingConfigRequest'
        variant:
          $ref: '#/components/schemas/KerasModelVariantEnum'
    GetPostProcessingResultsForSampleResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - hasResults
          properties:
            hasResults:
              type: string
              enum:
                - has-results
                - job-is-running
                - no-results
            results:
              type: object
              properties:
                objectTracking:
                  $ref: '#/components/schemas/ObjectTrackingPostProcessingResult'
                objectDetection:
                  $ref: '#/components/schemas/ObjectDetectionPostProcessingResult'
            jobIsRunning:
              type: object
              required:
                - jobId
                - config
              properties:
                jobId:
                  type: integer
                config:
                  $ref: '#/components/schemas/PostProcessingConfigRequest'
    PostProcessingConfigRequest:
      type: object
      required:
        - enabled
        - parameters
      properties:
        enabled:
          type: boolean
        parameters:
          type: object
          additionalProperties:
            type: string
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
    ObjectTrackingPostProcessingResult:
      type: object
      required:
        - frames
        - parameters
      properties:
        frames:
          type: array
          items:
            type: object
            required:
              - frameIndex
              - objects
            properties:
              frameIndex:
                type: integer
              objects:
                type: array
                items:
                  $ref: '#/components/schemas/ObjectTrackingPostProcessingObject'
        parameters:
          type: object
          additionalProperties:
            type: string
    ObjectDetectionPostProcessingResult:
      type: object
      required:
        - frames
      properties:
        frames:
          type: array
          items:
            type: object
            required:
              - frameIndex
              - objects
            properties:
              frameIndex:
                type: integer
              objects:
                type: array
                items:
                  $ref: '#/components/schemas/ObjectDetectionPostProcessingObject'
    ObjectTrackingPostProcessingObject:
      type: object
      required:
        - label
        - id
        - x
        - 'y'
        - width
        - height
      properties:
        label:
          type: string
        id:
          type: integer
        x:
          type: number
        'y':
          type: number
        width:
          type: number
        height:
          type: number
    ObjectDetectionPostProcessingObject:
      type: object
      required:
        - label
        - x
        - 'y'
        - width
        - height
        - score
      properties:
        label:
          type: string
        x:
          type: number
        'y':
          type: number
        width:
          type: number
        height:
          type: number
        score:
          type: number
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