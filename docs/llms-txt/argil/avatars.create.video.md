# Source: https://docs.argil.ai/api-reference/endpoint/avatars.create.video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new Avatar

> Creates a new avatar.


<Warning>
  **This endpoint is deprecated.** Video-based avatar creation will be removed
  in a future version. Please use [image-based avatar
  creation](/api-reference/endpoint/avatars.create) instead.
</Warning>

## Overview

Create a new avatar from a video. This method requires both a dataset video and a consent video.

<Warning>
  **Deprecation Notice**: This video-based avatar creation method is deprecated
  and will be removed in a future API version. Migrate to image-based avatar
  creation for better performance and simpler workflow.
</Warning>

### Video Requirements

**Dataset Video:**

* Duration: 1-5 minutes
* Format: MP4 or MOV
* Resolution: Between 720p and 4K
* Max size: 1.5GB
* Protocol: HTTPS only

**Consent Video:**

* Duration: 30 seconds or less
* Format: MP4 or MOV
* Max size: 100MB
* Protocol: HTTPS only

### Optional Fields

* `extras`: Custom metadata dictionary (max 10 key-value pairs, 256 characters each)


## OpenAPI

````yaml post /avatars
openapi: 3.0.1
info:
  title: Argil API
  description: API for AI clone video generation
  version: 1.0.0
  license:
    name: MIT
servers:
  - url: https://api.argil.ai/v1
security:
  - ApiKeyAuth: []
paths:
  /avatars:
    post:
      summary: Create a new Avatar
      description: |
        Creates a new avatar.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AvatarCreateArgsImage'
            examples:
              image_url:
                summary: Create avatar from image URL
                value:
                  type: IMAGE
                  name: My Image Avatar
                  datasetImage:
                    url: https://example.com/avatar-image.jpg
                  voiceId: 123e4567-e89b-12d3-a456-426614174000
              image_base64:
                summary: Create avatar from base64 image
                value:
                  type: IMAGE
                  name: My Image Avatar
                  datasetImage:
                    base64: data:image/png;base64,iVBORw0KGgoAAAANS...
              image_with_voice_design:
                summary: Create avatar with automatic voice design
                value:
                  type: IMAGE
                  name: My Image Avatar
                  datasetImage:
                    url: https://example.com/avatar-image.jpg
      responses:
        '201':
          description: >-
            Successfully created Avatar. The training process will start
            automatically.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Avatar'
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    AvatarCreateArgsImage:
      type: object
      required:
        - name
        - type
        - datasetImage
      properties:
        type:
          type: string
          enum:
            - IMAGE
          description: Avatar creation type - must be 'IMAGE' for image-based avatars
        name:
          type: string
          description: Name of the avatar
          minLength: 1
          maxLength: 256
        datasetImage:
          description: >-
            Image source for avatar creation. Either 'url' or 'base64' must be
            provided.
          oneOf:
            - type: object
              title: Image URL
              required:
                - url
              properties:
                url:
                  type: string
                  format: uri
                  pattern: ^https://.*
                  description: >
                    HTTPS URL to the source image for training. Must meet the
                    following requirements:

                    - Format: PNG, JPEG, or WEBP

                    - Resolution: Between 720p (1280x720 or 720x1280) and 4K
                    (3840x2160 or 2160x3840)

                    - Aspect ratio: 16:9 (landscape) or 9:16 (portrait)

                    - Max size: 10MB
              additionalProperties: false
            - type: object
              title: Base64 Image
              required:
                - base64
              properties:
                base64:
                  type: string
                  pattern: ^data:image/(png|jpeg|jpg|webp);base64,.*
                  description: >
                    Base64-encoded image data. Must be in format:
                    data:image/{format};base64,{data}

                    - Format: PNG, JPEG, or WEBP

                    - Resolution: Between 720p (1280x720 or 720x1280) and 4K
                    (3840x2160 or 2160x3840)

                    - Aspect ratio: 16:9 (landscape) or 9:16 (portrait)

                    - Max size: 10MB
              additionalProperties: false
        voiceId:
          type: string
          format: uuid
          description: >
            Optional voice ID to use for this avatar. If not provided, a voice
            design will be automatically created from the image.
        extras:
          type: object
          description: >-
            Optional dictionary of custom key-value pairs to extend the avatar
            metadata. Maximum of 10 key-value pairs of 256 characters allowed
          additionalProperties:
            type: string
          maxProperties: 10
      additionalProperties: false
    Avatar:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        actorName:
          type: string
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        gestures:
          type: array
          description: A list of labelized gestures available for your avatar.
          items:
            type: object
            properties:
              label:
                type: string
                description: A label for user readability. Can be setup from the app's UI.
              slug:
                type: string
                description: >-
                  Allows identifying the gesture when using it for a specific
                  moment.
              startFrame:
                type: number
                description: >-
                  The startFrame of the source Avatar video to be used as start
                  for the video template.
        status:
          $ref: '#/components/schemas/AvatarStatus'
        width:
          type: integer
        height:
          type: integer
        thumbnailUrl:
          type: string
          description: The url of the thumbnail of the avatar (low resolution).
        coverImageUrl:
          type: string
          description: The url of the cover image of the avatar (high resolution).
        extras:
          type: object
          description: >-
            A dictionary of custom key-value pairs to extend the Avatar
            metadata. Maximum of 5 key-value pairs of 256 characters allowed.
          additionalProperties:
            type: string
          maxProperties: 10
        orientation:
          $ref: '#/components/schemas/AvatarOrientation'
        model:
          $ref: '#/components/schemas/AvatarModel'
    Error:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
    AvatarStatus:
      type: string
      enum:
        - NOT_TRAINED
        - TRAINING
        - TRAINING_FAILED
        - IDLE
        - REFUSED
      description: >
        * NOT_TRAINED - Initial state after VIDEO mode avatar creation (before
        training starts)

        * TRAINING - Avatar is currently training. For IMAGE mode avatars, this
        is the initial status after creation.

        * TRAINING_FAILED - Training process failed

        * IDLE - Avatar is ready to use

        * REFUSED - Avatar was refused by moderation
    AvatarOrientation:
      type: string
      enum:
        - ASPECT_RATIO_16_9
        - ASPECT_RATIO_9_16
    AvatarModel:
      type: string
      enum:
        - ARGIL_V1
        - ARGIL_ATOM
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````