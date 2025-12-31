# Source: https://docs.argil.ai/api-reference/endpoint/avatars.list.md

# List all avatars

> Returns an array of Avatar objects available for the user

## OpenAPI

````yaml get /avatars
paths:
  path: /avatars
  method: get
  servers:
    - url: https://api.argil.ai/v1
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: API key to be included in the x-api-key header
          cookie: {}
    parameters:
      path: {}
      query:
        orientation:
          schema:
            - type: enum<string>
              enum:
                - ASPECT_RATIO_16_9
                - ASPECT_RATIO_9_16
              required: false
              description: Filter avatars by orientation
        model:
          schema:
            - type: enum<string>
              enum:
                - ARGIL_V1
                - ARGIL_ATOM
              required: false
              description: Filter avatars by model type
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Avatar'
        examples:
          example:
            value:
              - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                actorName: <string>
                createAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                gestures:
                  - label: <string>
                    slug: <string>
                    startFrame: 123
                status: NOT_TRAINED
                width: 123
                height: 123
                thumbnailUrl: <string>
                coverImageUrl: <string>
                extras: {}
                orientation: ASPECT_RATIO_16_9
                model: ARGIL_V1
        description: An array of avatars
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - type: integer
                    format: int32
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              code: 123
              message: <string>
        description: Unexpected error
  deprecated: false
  type: path
components:
  schemas:
    AvatarStatus:
      type: string
      enum:
        - NOT_TRAINED
        - TRAINING
        - TRAINING_FAILED
        - IDLE
        - REFUSED
      description: |
        * NOT_TRAINED - Initial state after creation
        * TRAINING - Avatar is currently training
        * TRAINING_FAILED - Training process failed
        * IDLE - Avatar is ready to use
        * REFUSED - Avatar was refused by moderation
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
        createAt:
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

````