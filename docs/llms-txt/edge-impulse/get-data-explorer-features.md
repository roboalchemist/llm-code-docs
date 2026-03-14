# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/get-data-explorer-features.md

# Source: https://docs.edgeimpulse.com/apis/studio/learn/get-data-explorer-features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data explorer features

> t-SNE2 output of the raw dataset using embeddings from this Keras block



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/training/keras/{learnId}/data-explorer/features
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
  /api/{projectId}/training/keras/{learnId}/data-explorer/features:
    get:
      tags:
        - Learn
      summary: Get data explorer features
      description: t-SNE2 output of the raw dataset using embeddings from this Keras block
      operationId: getKerasDataExplorerFeatures
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LearnIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetDataExplorerFeaturesResponse'
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
    GetDataExplorerFeaturesResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - hasFeatures
            - data
          properties:
            hasFeatures:
              type: boolean
            data:
              type: array
              items:
                type: object
                required:
                  - X
                  - 'y'
                  - yLabel
                properties:
                  X:
                    type: object
                    description: Data by feature index for this window
                    example: '`{ 0: 9.81, 11: 0.32, 22: 0.79 }`'
                    additionalProperties:
                      type: number
                  'y':
                    type: integer
                    description: Training label index
                  yLabel:
                    type: string
                    description: Training label string
                  sample:
                    type: object
                    required:
                      - id
                      - name
                      - startMs
                      - endMs
                      - category
                    properties:
                      id:
                        type: number
                      name:
                        type: string
                      startMs:
                        type: number
                      endMs:
                        type: number
                      category:
                        type: string
                        enum:
                          - training
                          - testing
            inputBlock:
              $ref: '#/components/schemas/ImpulseInputBlock'
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
    ImpulseInputBlock:
      type: object
      required:
        - id
        - type
        - name
        - title
      properties:
        id:
          type: integer
          minimum: 1
          description: >-
            Identifier for this block. Make sure to up this number when creating
            a new block via `getNewBlockId`, and don't re-use identifiers. If
            the block hasn't changed, keep the ID as-is. ID must be unique
            across the project and greather than zero (>0).
        type:
          type: string
          description: Block type (either time-series, image or features)
          example: time-series
          enum:
            - time-series
            - image
            - features
        name:
          type: string
          description: Block name, will be used in menus
          example: Time series
        title:
          type: string
          description: Block title, used in the impulse UI
          example: Time series
        windowSizeMs:
          type: integer
          description: Size of the sliding window in milliseconds
          example: 2004
        windowIncreaseMs:
          type: integer
          description: >-
            We use a sliding window to go over the raw data. How many
            milliseconds to increase the sliding window with for each step.
        frequencyHz:
          type: number
          description: (Input only) Frequency of the input data in Hz
          example: 60
        classificationWindowIncreaseMs:
          type: integer
          description: >-
            We use a sliding window to go over the raw data. How many
            milliseconds to increase the sliding window with for each step in
            classification mode.
        padZeros:
          type: boolean
          description: Whether to zero pad data when a data item is too short
        labelingMethodMultiLabel:
          type: object
          description: How to pick the label for multi-label samples
          required:
            - type
          properties:
            type:
              type: string
              enum:
                - end-of-window
                - anywhere-in-window
            labels:
              description: >-
                Required when choosing "anywhere-in-window". The list of classes
                that should trigger detection (e.g. "interference").
              type: array
              items:
                type: string
        imageWidth:
          type: integer
          description: Width all images are resized to before training
          example: 28
        imageHeight:
          type: integer
          description: Width all images are resized to before training
          example: 28
        resizeMode:
          $ref: '#/components/schemas/ImageInputResizeMode'
        resizeMethod:
          type: string
          description: Resize method to use when resizing images
          example: squash
          enum:
            - lanczos3
            - nearest
        cropAnchor:
          type: string
          description: If images are resized using a crop, choose where to anchor the crop
          example: middle-center
          enum:
            - top-left
            - top-center
            - top-right
            - middle-left
            - middle-center
            - middle-right
            - bottom-left
            - bottom-center
            - bottom-right
        createdBy:
          type: string
          description: >-
            The system component that created the block version (createImpulse |
            clone | tuner). Cannot be set via API.
          example: createImpulse
        createdAt:
          type: string
          format: date-time
          description: >-
            The datetime that the block version was created. Cannot be set via
            API.
        datasetSubset:
          $ref: '#/components/schemas/ImpulseInputBlockDatasetSubset'
    ImageInputResizeMode:
      type: string
      description: >
        Input images are resized automatically before training and testing, to
        match the impulse input shape.

        This determines the resize mode used when the aspect ratio of the input
        data is different to the aspect ratio of the impulse.
      example: squash
      enum:
        - squash
        - fit-short
        - fit-long
        - crop
    ImpulseInputBlockDatasetSubset:
      type: object
      description: >-
        Only generate features for samples where (sample_id + datasetSubsetSeed)
        % datasetSubset) == 0
      required:
        - includePercentage
      properties:
        includePercentage:
          description: >-
            Number between 0 and 100, with the % of data that should be
            _included_
          type: number
        seed:
          description: Seed number (optional). If not specified, the seed is set to 0.
          type: integer
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