# Source: https://docs.edgeimpulse.com/apis/studio/deployment/check-evaluate-job-result-cache.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Check evaluate job result (cache)

> Get evaluate job result, containing detailed performance statistics for every possible variant of the impulse. This only checks cache, and throws an error if there is no data in cache.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/deployment/evaluate/cache
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
  /api/{projectId}/deployment/evaluate/cache:
    get:
      tags:
        - Deployment
      summary: Check evaluate job result (cache)
      description: >-
        Get evaluate job result, containing detailed performance statistics for
        every possible variant of the impulse. This only checks cache, and
        throws an error if there is no data in cache.
      operationId: getEvaluateJobResultCache
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluateJobResponse'
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
    EvaluateJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - result
          properties:
            result:
              type: array
              items:
                $ref: '#/components/schemas/ModelVariantStats'
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
    ModelVariantStats:
      type: object
      required:
        - modelType
        - learnBlockType
        - learnBlockId
        - confusionMatrix
        - confusionMatrixRowHeaders
        - confusionMatrixColumnHeaders
        - accuracy
        - trainingLabels
        - classificationLabels
      properties:
        modelType:
          $ref: '#/components/schemas/KerasModelTypeEnum'
          description: The type of model
        learnBlockId:
          description: The learning block this model variant is from
          type: integer
        learnBlockType:
          $ref: '#/components/schemas/LearnBlockType'
        confusionMatrix:
          description: >-
            A map from actual labels to predicted labels, where actual labels
            are listed in `trainingLabels` and possible predicted labels are
            listed in `classificationLabels`.
          type: object
          additionalProperties:
            type: object
            additionalProperties:
              $ref: '#/components/schemas/EvaluateResultValue'
              type: object
        trainingLabels:
          description: >-
            The labels present in the model's training data. These are all
            present in the first dimension of the confusion matrix.
          type: array
          items:
            type: string
        classificationLabels:
          description: >-
            The possible labels resulting from classification. These may be
            present in the second dimension of the confusion matrix.
          type: array
          items:
            type: string
        totalWindowCount:
          description: The total number of windows that were evaluated
          type: integer
        totalCorrectWindowCount:
          $ref: '#/components/schemas/EvaluateResultValue'
          description: The total number of windows that the model classified correctly
        accuracy:
          $ref: '#/components/schemas/EvaluateResultValue'
          description: The model's accuracy as a percentage
    KerasModelTypeEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
        - requiresRetrain
    LearnBlockType:
      type: string
      description: >-
        The type of learning block (anomaly, keras, keras-transfer-image,
        keras-transfer-kws, keras-object-detection, keras-regression,
        keras-freeform). Each behaves differently.
      enum:
        - anomaly
        - anomaly-gmm
        - keras
        - keras-transfer-image
        - keras-transfer-kws
        - keras-object-detection
        - keras-regression
        - keras-akida
        - keras-akida-transfer-image
        - keras-akida-object-detection
        - keras-visual-anomaly
        - keras-freeform
        - keras-anomaly
        - vlm
    EvaluateResultValue:
      type: object
      properties:
        raw:
          description: The value based on the model alone
          type: number
        withAnomaly:
          description: The value including the result of anomaly detection
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