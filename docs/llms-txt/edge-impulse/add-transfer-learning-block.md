# Source: https://docs.edgeimpulse.com/apis/studio/organizationblocks/add-transfer-learning-block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add transfer learning block

> Adds a transfer learning block.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/transfer-learning
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
  /api/organizations/{organizationId}/transfer-learning:
    post:
      tags:
        - OrganizationBlocks
      summary: Add transfer learning block
      description: Adds a transfer learning block.
      operationId: addOrganizationTransferLearningBlock
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddOrganizationTransferLearningBlockRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EntityCreatedResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
  schemas:
    AddOrganizationTransferLearningBlockRequest:
      type: object
      required:
        - name
        - dockerContainer
        - description
        - operatesOn
        - implementationVersion
      properties:
        name:
          type: string
        dockerContainer:
          type: string
        description:
          type: string
        operatesOn:
          $ref: '#/components/schemas/OrganizationTransferLearningOperatesOn'
        objectDetectionLastLayer:
          $ref: '#/components/schemas/ObjectDetectionLastLayer'
        implementationVersion:
          type: integer
        isPublic:
          type: boolean
          description: >-
            Whether this block is publicly available to Edge Impulse users (if
            false, then only for members of the owning organization)
        isPublicForDevices:
          description: >-
            If `isPublic` is true, the list of devices (from latencyDevices) for
            which this model can be shown.
          type: array
          items:
            type: string
        publicProjectTierAvailability:
          $ref: '#/components/schemas/PublicProjectTierAvailability'
        repositoryUrl:
          type: string
          description: URL to the source code of this custom learn block.
        parameters:
          description: >-
            List of parameters, spec'ed according to
            https://docs.edgeimpulse.com/docs/tips-and-tricks/adding-parameters-to-custom-blocks
          type: array
          items:
            type: object
        imageInputScaling:
          $ref: '#/components/schemas/ImageInputScaling'
        indRequiresGpu:
          description: If set, requires this block to be scheduled on GPU.
          type: boolean
        customModelVariants:
          description: >-
            List of custom model variants produced when this block is trained.
            This is experimental and may change in the future.
          type: array
          items:
            $ref: >-
              #/components/schemas/OrganizationTransferLearningBlockCustomVariant
        displayCategory:
          $ref: '#/components/schemas/BlockDisplayCategory'
        indBlockNoLongerAvailable:
          type: boolean
          description: >-
            If set, then this block is no longer available for training; and
            blockNoLongerAvailableReason should be set.
        blockNoLongerAvailableReason:
          type: string
          description: >-
            In Markdown format. Should be set if `indBlockNoLongerAvailable` is
            true, contains migration information for existing users of this
            block.
        sourceCodeDownloadStaffOnly:
          type: boolean
          description: Whether the source code is only available for staff users.
    EntityCreatedResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Unique identifier of the created entity.
    OrganizationTransferLearningOperatesOn:
      type: string
      enum:
        - object_detection
        - audio
        - image
        - regression
        - anomaly_detection
        - visual_anomaly_detection
        - other
        - image_akida
        - object_detection_akida
        - classification_akida
    ObjectDetectionLastLayer:
      type: string
      enum:
        - mobilenet-ssd
        - fomo
        - yolov2-akida
        - yolov5
        - yolov5v5-drpai
        - yolox
        - yolov7
        - yolo-pro
        - tao-retinanet
        - tao-ssd
        - tao-yolov3
        - tao-yolov4
        - yolov11
        - yolov11-abs
        - paddleocr-detector
        - qc-face-det-lite
    PublicProjectTierAvailability:
      description: >-
        For public blocks, this indicates the project tiers for which this block
        is available.
      type: string
      enum:
        - enterprise-only
        - all-projects
        - all-projects-including-whitelabels
    ImageInputScaling:
      description: >-
        Normalization that is applied to images. If this is not set then 0..1 is
        used. "0..1" gives you non-normalized pixels between 0 and 1. "-1..1"
        gives you non-normalized pixels between -1 and 1. "0..255" gives you
        non-normalized pixels between 0 and 255. "-128..127" gives you
        non-normalized pixels between -128 and 127. "torch" first scales pixels
        between 0 and 1, then applies normalization using the ImageNet dataset
        (same as `torchvision.transforms.Normalize()`).
        "bgr-subtract-imagenet-mean" scales to 0..255, reorders pixels to BGR,
        and subtracts the ImageNet mean from each channel.
      type: string
      enum:
        - 0..1
        - '-1..1'
        - '-128..127'
        - 0..255
        - torch
        - bgr-subtract-imagenet-mean
    OrganizationTransferLearningBlockCustomVariant:
      type: object
      required:
        - key
        - name
        - inferencingEntrypoint
      properties:
        key:
          type: string
          description: Unique identifier or key for this custom variant
        name:
          type: string
          description: Custom variant display name
        inferencingEntrypoint:
          type: string
          description: >-
            The entrypoint command to run custom inferencing for this model
            variant, via the learn block container
        profilingEntrypoint:
          type: string
          description: >-
            The entrypoint command to run custom profiling for this model
            variant, via the learn block container
        modelFiles:
          type: array
          items:
            $ref: '#/components/schemas/OrganizationTransferLearningBlockModelFile'
    BlockDisplayCategory:
      description: Category to display this block in the UI.
      type: string
      enum:
        - classical
        - tao
        - developer-preview
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
    OrganizationTransferLearningBlockModelFile:
      type: object
      required:
        - id
        - name
        - type
        - description
      properties:
        id:
          type: string
          description: Output artifact unique file ID, in kebab case
        name:
          type: string
          description: Output artifact file name
        type:
          type: string
          description: Output artifact file type
          enum:
            - binary
            - json
            - text
        description:
          type: string
          description: Output artifact file description
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