# Source: https://docs.edgeimpulse.com/apis/studio/performancecalibration/get-parameter-sets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get parameter sets

> Get performance calibration parameter sets



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/performance-calibration/parameter-sets
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
  /api/{projectId}/performance-calibration/parameter-sets:
    get:
      tags:
        - PerformanceCalibration
      summary: Get parameter sets
      description: Get performance calibration parameter sets
      operationId: getPerformanceCalibrationParameterSets
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: File
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/GetPerformanceCalibrationParameterSetsResponse
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
    GetPerformanceCalibrationParameterSetsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - parameterSets
          properties:
            parameterSets:
              type: array
              items:
                $ref: '#/components/schemas/PerformanceCalibrationParameterSet'
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
    PerformanceCalibrationParameterSet:
      type: object
      required:
        - detections
        - isBest
        - labels
        - stats
        - aggregateStats
        - params
        - windowSizeMs
      properties:
        detections:
          type: array
          description: All of the detections using this parameter set
          items:
            $ref: '#/components/schemas/PerformanceCalibrationDetection'
        isBest:
          type: boolean
          description: Whether this is considered the best parameter set
        labels:
          type: array
          description: All of the possible labels in the detections array
          items:
            type: string
        aggregateStats:
          type: object
          required:
            - falsePositiveRate
            - falseNegativeRate
          properties:
            falsePositiveRate:
              type: number
            falseNegativeRate:
              type: number
        stats:
          type: array
          items:
            type: object
            required:
              - label
              - truePositives
              - falsePositives
              - falseNegatives
              - trueNegatives
              - falsePositiveRate
              - falseNegativeRate
              - wrongMatches
              - falsePositiveTimes
              - falseNegativeTimes
            properties:
              label:
                type: string
              truePositives:
                type: integer
              falsePositives:
                type: integer
              falseNegatives:
                type: integer
              trueNegatives:
                type: integer
              falsePositiveRate:
                type: number
              falseNegativeRate:
                type: number
              falsePositiveDetails:
                type: array
                description: The details of every false positive detection.
                items:
                  $ref: '#/components/schemas/PerformanceCalibrationFalsePositive'
              falseNegativeTimes:
                type: array
                description: >-
                  The times in ms at which false negatives occurred. These
                  correspond to specific items in the ground truth.
                items:
                  type: number
        params:
          $ref: '#/components/schemas/PerformanceCalibrationParameters'
        windowSizeMs:
          type: number
          description: The size of the input block window in milliseconds.
    PerformanceCalibrationDetection:
      type: object
      required:
        - time
        - label
      properties:
        time:
          type: integer
          description: The time of the detection in milliseconds
        label:
          type: string
          description: The label that was detected
    PerformanceCalibrationFalsePositive:
      type: object
      required:
        - type
        - detectionTime
      properties:
        type:
          type: string
          enum:
            - incorrect
            - duplicate
            - spurious
          description: >-
            The type of false positive. Incorrect is when a detection matches
            the wrong ground truth. Duplicate is when the same ground truth was
            detected more than once. The first correct detection is considered a
            true positive but subsequent detections are considered false
            positives. Spurious is when the detection was not associated with
            any ground truth.
        detectionTime:
          type: integer
          description: The time of the detection in milliseconds
        groundTruthLabel:
          type: string
          description: The label of any associated ground truth
        groundTruthStart:
          type: number
          description: The start time of any associated ground truth
        sampleIds:
          type: array
          description: All of the sample IDs in the affected region
          items:
            type: integer
    PerformanceCalibrationParameters:
      type: object
      required:
        - type
        - version
      properties:
        type:
          type: string
          description: The post-processing algorithm type.
          enum:
            - standard
        version:
          type: integer
          description: The version number of the post-processing algorithm.
          example: 1
        parametersStandard:
          $ref: '#/components/schemas/PerformanceCalibrationParametersStandard'
    PerformanceCalibrationParametersStandard:
      type: object
      required:
        - averageWindowDurationMs
        - detectionThreshold
        - suppressionMs
      properties:
        averageWindowDurationMs:
          type: number
          description: The length of the averaging window in milliseconds.
          example: 1000
        detectionThreshold:
          type: number
          description: The minimum threshold for detection, from 0-1.
          example: 0.8
        suppressionMs:
          type: number
          description: >-
            The amount of time new matches will be ignored after a positive
            result.
          example: 500
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