# Source: https://docs.edgeimpulse.com/apis/studio/impulse/get-all-impulses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all impulses

> Retrieve all impulse for a project



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/impulses
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
  /api/{projectId}/impulses:
    get:
      tags:
        - Impulse
      summary: Get all impulses
      description: Retrieve all impulse for a project
      operationId: getAllImpulses
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAllImpulsesResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
  schemas:
    GetAllImpulsesResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - impulses
          properties:
            impulses:
              type: array
              items:
                $ref: '#/components/schemas/Impulse'
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
    Impulse:
      type: object
      required:
        - id
        - name
        - inputBlocks
        - dspBlocks
        - learnBlocks
        - postProcessingBlocks
        - type
      properties:
        id:
          type: integer
          description: ID for this impulse.
        name:
          type: string
          description: Name for this impulse.
        inputBlocks:
          type: array
          description: Input Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/ImpulseInputBlock'
        dspBlocks:
          type: array
          description: DSP Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/ImpulseDspBlock'
        learnBlocks:
          type: array
          description: Learning Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/ImpulseLearnBlock'
        postProcessingBlocks:
          type: array
          description: Post-processing blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/ImpulsePostProcessingBlock'
        type:
          $ref: '#/components/schemas/ImpulseType'
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
    ImpulseDspBlock:
      type: object
      required:
        - id
        - type
        - name
        - axes
        - title
        - implementationVersion
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
          description: Block type
          example: spectral-analysis
        name:
          type: string
          description: Block name, will be used in menus
          example: Spectral features
        axes:
          type: array
          description: Input axes, identified by the name in the name of the axis
          items:
            type: string
            example: accX
        title:
          type: string
          description: Block title, used in the impulse UI
          example: Spectral Analysis
        valuesPerAxis:
          type: integer
          description: >-
            Number of features this DSP block outputs per axis. This is only set
            when the DSP block is configured.
          example: 11
        input:
          type: integer
          description: The ID of the Input block a DSP block is connected to
          example: 1
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
        implementationVersion:
          type: integer
          description: Implementation version of the block
        organization:
          type: object
          required:
            - id
            - dspId
          properties:
            id:
              type: integer
            dspId:
              type: integer
        customUrl:
          type: string
          description: Required for type 'custom'
        namedAxes:
          type: array
          description: Named axes for the block
          items:
            type: object
            required:
              - name
            properties:
              name:
                type: string
                description: Name of the axis
              description:
                type: string
                description: Description of the axis
              required:
                type: boolean
                description: Whether the axis is required
              selectedAxis:
                type: string
                description: The selected axis for the block
    ImpulseLearnBlock:
      type: object
      required:
        - id
        - type
        - name
        - dsp
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
          $ref: '#/components/schemas/LearnBlockType'
        name:
          type: string
          description: >-
            Block name, will be used in menus. If a block has a baseBlockId,
            this field is ignored and the base block's name is used instead.
          example: NN Classifier
        dsp:
          type: array
          description: DSP dependencies, identified by DSP block ID
          items:
            type: integer
            example: 27
        title:
          type: string
          description: Block title, used in the impulse UI
          example: Classification (Keras)
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
    ImpulsePostProcessingBlock:
      type: object
      required:
        - id
        - type
        - name
        - title
        - implementationVersion
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
          description: Block type
          example: object-tracking
        name:
          type: string
          description: Block name, will be used in menus
          example: Object tracking
        title:
          type: string
          description: Block title, used in the impulse UI
          example: Object tracking
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
        implementationVersion:
          type: integer
          description: Implementation version of the block
    ImpulseType:
      type: string
      description: >
        Specifies the type of impulse. Options include: - default: Standard Edge
        Impulse pipeline. - BYOM: Impulse that includes a pretrained model. -
        VLM: Impulse created as part of a Vision Learning Model (VLM) workflow.
      enum:
        - default
        - BYOM
        - VLM
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