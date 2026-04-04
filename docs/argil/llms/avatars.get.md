# Source: https://docs.argil.ai/api-reference/endpoint/avatars.get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an Avatar by id

> Returns a single Avatar identified by its id



## OpenAPI

````yaml get /avatars/{id}
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
  /avatars/{id}:
    get:
      summary: Get an Avatar by id
      description: Returns a single Avatar identified by its id
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            description: The id of the Avatar to retrieve
      responses:
        '200':
          description: Detailed information about the Avatar
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Avatar'
        '404':
          description: Avatar not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
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