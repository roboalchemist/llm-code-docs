# Source: https://docs.edgeimpulse.com/apis/studio/learn/anomaly-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Anomaly information

> Get information about an anomaly block, such as its dependencies. Use the impulse blocks to find the learnId.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/training/anomaly/{learnId}
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
  /api/{projectId}/training/anomaly/{learnId}:
    get:
      tags:
        - Learn
      summary: Anomaly information
      description: >-
        Get information about an anomaly block, such as its dependencies. Use
        the impulse blocks to find the learnId.
      operationId: getAnomaly
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LearnIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnomalyConfigResponse'
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
    AnomalyConfigResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/AnomalyConfig'
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
    AnomalyConfig:
      type: object
      required:
        - name
        - axes
        - trained
        - dependencies
        - selectedAxes
        - minimumConfidenceRating
        - thresholds
      properties:
        dependencies:
          $ref: '#/components/schemas/DependencyData'
        name:
          type: string
        axes:
          type: array
          description: Selectable axes for the anomaly detection block
          items:
            type: object
            required:
              - ix
              - label
              - selected
              - favourite
            properties:
              ix:
                type: integer
              label:
                type: string
              selected:
                type: boolean
              favourite:
                type: boolean
        trained:
          type: boolean
          description: Whether the block is trained
        clusterCount:
          type: integer
          description: >-
            Number of clusters for K-means, or number of components for GMM (in
            config)
        selectedAxes:
          type: array
          items:
            type: integer
          description: Selected clusters (in config)
        minimumConfidenceRating:
          type: number
          description: >-
            DEPRECATED, see "thresholds" instead. Minimum confidence rating for
            this block, scores above this number will be flagged as anomaly.
        thresholds:
          type: array
          description: List of configurable thresholds for this block.
          items:
            $ref: '#/components/schemas/BlockThreshold'
    DependencyData:
      type: object
      required:
        - classes
        - blockNames
        - featureCount
        - sampleCount
        - outputClasses
      properties:
        classes:
          type: array
          description: Set of all labels present in data feeding into this model
          items:
            type: string
        blockNames:
          type: array
          items:
            type: string
        featureCount:
          type: integer
        sampleCount:
          type: integer
        outputClasses:
          type: array
          description: Set of output classes for this model
          items:
            type: string
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