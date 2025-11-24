# Source: https://docs.argil.ai/api-reference/endpoint/avatars.create.md

# Create a new Avatar

> Creates a new Avatar by uploading source videos and launches training. The process is asynchronous - the avatar will initially be created with 'NOT_TRAINED' status and will transition to 'TRAINING' then 'IDLE' once ready.

## OpenAPI

````yaml post /avatars
paths:
  path: /avatars
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: Name of the avatar
                    minLength: 1
                    maxLength: 256
              datasetVideo:
                allOf:
                  - type: object
                    required:
                      - url
                    properties:
                      url:
                        type: string
                        format: uri
                        pattern: ^https://.*
                        description: >-
                          HTTPS URL to the source video for training. Must be
                          1-5 minutes long, in MP4 or MOV format, resolution
                          between 720p and 4K. Max size 1.5GB.
                    additionalProperties: false
              consentVideo:
                allOf:
                  - type: object
                    required:
                      - url
                    properties:
                      url:
                        type: string
                        format: uri
                        pattern: ^https://.*
                        description: >-
                          HTTPS URL to the consent video recording. Must be 30
                          seconds or less, in MP4 or MOV format. Max size 100MB.
                    additionalProperties: false
              extras:
                allOf:
                  - type: object
                    description: >-
                      Optional dictionary of custom key-value pairs to extend
                      the video metadata. Maximum of 5 key-value pairs of 256
                      characters allowed
                    additionalProperties:
                      type: string
                    maxProperties: 10
            required: true
            refIdentifier: '#/components/schemas/AvatarCreateArgs'
            requiredProperties:
              - name
              - datasetVideo
              - consentVideo
            additionalProperties: false
            example:
              name: My Avatar
              datasetVideo:
                url: https://example.com/source-video.mp4
              consentVideo:
                url: https://example.com/consent-video.mp4
        examples:
          example:
            value:
              name: My Avatar
              datasetVideo:
                url: https://example.com/source-video.mp4
              consentVideo:
                url: https://example.com/consent-video.mp4
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
              name:
                allOf:
                  - type: string
              actorName:
                allOf:
                  - type: string
              createAt:
                allOf:
                  - type: string
                    format: date-time
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
              gestures:
                allOf:
                  - type: array
                    description: A list of labelized gestures available for your avatar.
                    items:
                      type: object
                      properties:
                        label:
                          type: string
                          description: >-
                            A label for user readability. Can be setup from the
                            app's UI.
                        slug:
                          type: string
                          description: >-
                            Allows identifying the gesture when using it for a
                            specific moment.
                        startFrame:
                          type: number
                          description: >-
                            The startFrame of the source Avatar video to be used
                            as start for the video template.
              status:
                allOf:
                  - $ref: '#/components/schemas/AvatarStatus'
              width:
                allOf:
                  - type: integer
              height:
                allOf:
                  - type: integer
              thumbnailUrl:
                allOf:
                  - type: string
                    description: The url of the thumbnail of the avatar (low resolution).
              coverImageUrl:
                allOf:
                  - type: string
                    description: >-
                      The url of the cover image of the avatar (high
                      resolution).
              extras:
                allOf:
                  - type: object
                    description: >-
                      A dictionary of custom key-value pairs to extend the
                      Avatar metadata. Maximum of 5 key-value pairs of 256
                      characters allowed.
                    additionalProperties:
                      type: string
                    maxProperties: 10
              orientation:
                allOf:
                  - $ref: '#/components/schemas/AvatarOrientation'
              model:
                allOf:
                  - $ref: '#/components/schemas/AvatarModel'
            refIdentifier: '#/components/schemas/Avatar'
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
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
        description: >-
          Successfully created Avatar. The training process will start
          automatically.
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
        description: Validation error
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