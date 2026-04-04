# Source: https://docs.argil.ai/api-reference/endpoint/avatars.list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List all avatars

> Returns an array of Avatar objects available for the user



## OpenAPI

````yaml get /avatars
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
    get:
      summary: List all avatars
      description: Returns an array of Avatar objects available for the user
      parameters:
        - name: orientation
          in: query
          description: Filter avatars by orientation
          required: false
          schema:
            $ref: '#/components/schemas/AvatarOrientation'
        - name: model
          in: query
          description: Filter avatars by model type
          required: false
          schema:
            $ref: '#/components/schemas/AvatarModel'
      responses:
        '200':
          description: An array of avatars
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Avatar'
        '400':
          description: Unexpected error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````