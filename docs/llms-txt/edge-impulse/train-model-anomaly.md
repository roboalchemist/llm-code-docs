# Source: https://docs.edgeimpulse.com/apis/studio/jobs/train-model-anomaly.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Train model (Anomaly)

> Take the output from a DSP block and train an anomaly detection model using K-means or GMM. Updates are streamed over the websocket API.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/jobs/train/anomaly/{learnId}
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
  /api/{projectId}/jobs/train/anomaly/{learnId}:
    post:
      tags:
        - Jobs
      summary: Train model (Anomaly)
      description: >-
        Take the output from a DSP block and train an anomaly detection model
        using K-means or GMM. Updates are streamed over the websocket API.
      operationId: trainAnomalyJob
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LearnIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/StartTrainingRequestAnomaly'
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
    LearnIdParameter:
      name: learnId
      in: path
      required: true
      description: Learn Block ID, use the impulse functions to retrieve the ID
      schema:
        type: integer
  schemas:
    StartTrainingRequestAnomaly:
      type: object
      required:
        - axes
        - minimumConfidenceRating
      properties:
        axes:
          type: array
          description: Which axes (indexes from DSP script) to include in the training set
          example:
            - 0
            - 11
            - 22
          items:
            type: integer
        clusterCount:
          type: integer
          description: Number of clusters for K-means, or number of components for GMM
          example: 32
        minimumConfidenceRating:
          type: number
          description: >-
            DEPRECATED, use "thresholds" instead. Minimum confidence rating
            required before tagging as anomaly
          example: 0.3
        skipEmbeddingsAndMemory:
          type: boolean
          description: >-
            If set, skips creating embeddings and measuring memory (used in
            tests)
        thresholds:
          type: array
          description: List of configurable thresholds for this block.
          items:
            $ref: '#/components/schemas/BlockThreshold'
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
    BlockThreshold:
      type: object
      description: >-
        Configurable threshold for this block (e.g. minimum score before tagging
        as an anomaly, or the min. score to save bounding boxes)
      required:
        - key
        - description
        - helpText
        - value
      properties:
        key:
          type: string
          description: >-
            Identifier to reference the threshold. You'll need to refer to the
            threshold by this key when you set the threshold).
          example: min_score
        description:
          type: string
          description: User-friendly description of the threshold.
          example: Score threshold
        helpText:
          type: string
          description: Additional help text (shown in the UI under a "?" icon)
          example: >-
            Threshold score for bounding boxes. If the score for a bounding box
            is below this the box will be discarded.
        suggestedValue:
          type: number
          description: >-
            If the threshold has a suggested value, e.g. a max. absolute error
            for regression projects; or the min. anomaly score for visual
            anomaly detection, then this is the numeric value of that threshold.
        suggestedValueText:
          type: string
          description: >-
            If the threshold has a suggested value, e.g. a max. absolute error
            for regression projects; or the min. anomaly score for visual
            anomaly detection, then this is the stringified value of that
            threshold.
        value:
          description: Current value of the threshold
          example: 0.5
          oneOf:
            - type: number
            - type: string
        dropdownOptions:
          description: Optional list of options, will be shown in a dropdown.
          type: array
          items:
            type: object
            required:
              - description
              - value
            properties:
              description:
                type: string
                description: Full description of the value
              value:
                type: string
                description: Value, maps back to "BlockThreshold#value"
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