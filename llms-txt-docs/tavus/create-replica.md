# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/create-replica.md

> This endpoint creates a new replica using the latest `phoenix-3` model, which can be used in real-time conversations.



To ensure high-quality replica creation, follow the steps in the [Replica Training](/sections/replica/replica-training) guide.


# Create Replica

## OpenAPI

````yaml post /v2/replicas
paths:
  path: /v2/replicas
  method: post
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
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
              consent_video_url:
                allOf:
                  - type: string
                    description: >-
                      A direct link to a video that contains the consent
                      statement. You may optionally send the consent statement
                      in a separate video from your training video. If you do
                      not provide a consent video, the consent statement must be
                      present at the beginning of the training video. **This
                      value is required if you want to create a personal
                      replica**.
                    example: >-
                      https://my-example-bucket.s3.us-east-1.amazonaws.com/your-consent-video.mp4
              train_video_url:
                allOf:
                  - type: string
                    description: >-
                      A direct link to a publicly accessible storage location
                      such as an S3 bucket. This video will be used for replica
                      training.
                    example: >-
                      https://my-example-bucket.s3.us-east-1.amazonaws.com/your-train-video.mp4
              callback_url:
                allOf:
                  - type: string
                    description: >-
                      A url that will receive a callback on completion of
                      replica training or on error.
                    example: https://yourwebsite.com/webhook
              replica_name:
                allOf:
                  - type: string
                    description: A name for the replica.
                    example: Rio
              model_name:
                allOf:
                  - type: string
                    description: >-
                      The phoenix model version that will be used to train the
                      replica. The current default is `phoenix-3`.
                    example: phoenix-3
              properties:
                allOf:
                  - type: object
                    properties:
                      gaze_correction:
                        type: boolean
                        description: >-
                          If set to true, the replica will have gaze correction
                          enabled.
                        example: false
                      background_green_screen:
                        type: boolean
                        description: >-
                          If set to true, the replica will have a green screen
                          background.
                        example: false
            requiredProperties:
              - train_video_url
        examples:
          Personal Replica:
            value:
              callback_url: https://yourwebsite.com/webhook
              replica_name: Rio
              train_video_url: >-
                https://my-example-bucket.s3.us-east-1.amazonaws.com/your-train-video.mp4
              consent_video_url: >-
                https://my-example-bucket.s3.us-east-1.amazonaws.com/your-consent-video.mp4
          Non-Human Replica:
            value:
              callback_url: https://yourwebsite.com/webhook
              replica_name: AI
              train_video_url: >-
                https://my-example-bucket.s3.us-east-1.amazonaws.com/your-train-video.mp4
          Older Model Replica:
            value:
              model_name: phoenix-2
              callback_url: https://yourwebsite.com/webhook
              replica_name: rfe12d8b9597
              train_video_url: >-
                https://my-example-bucket.s3.us-east-1.amazonaws.com/your-train-video.mp4
              consent_video_url: >-
                https://my-example-bucket.s3.us-east-1.amazonaws.com/your-consent-video.mp4
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              replica_id:
                allOf:
                  - type: string
                    example: r783537ef5
                    description: A unique identifier for the replica.
              status:
                allOf:
                  - type: string
                    example: started
                    description: >-
                      The status of the replica. Possible values: `started`,
                      `completed`, `error`.
        examples:
          example:
            value:
              replica_id: r783537ef5
              status: started
        description: ''
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid train_video_url
        examples:
          example:
            value:
              error: Invalid train_video_url
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
  deprecated: false
  type: path
components:
  schemas: {}

````