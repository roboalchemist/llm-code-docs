# Source: https://docs.tavus.io/api-reference/phoenix-replica-model/create-replica.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

> This endpoint creates a new replica using the latest `phoenix-3` model, which can be used in real-time conversations.



To ensure high-quality replica creation, follow the steps in the [Replica Training](/sections/replica/replica-training) guide.


# Create Replica

<Note>
  By default, all new replicas are trained using the `phoenix-3` model.\
  To use the older `phoenix-2` model, set the `model_name` parameter to `phoenix-2`.
</Note>

<Accordion title="Required Parameters" icon="lightbulb">
  Required parameters vary based on the replica type:

  **Personal Replica:**

  * `train_video_url`
  * `consent_video_url`

  **Non-Human Replica:**

  * `train_video_url`

  <Warning>
    Make sure the `train_video_url` and `consent_video_url` are publicly accessible download links, such as presigned S3 URLs.
  </Warning>
</Accordion>


## OpenAPI

````yaml post /v2/replicas
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/replicas:
    post:
      tags:
        - Replicas
      summary: Create Replica
      description: >
        This endpoint creates a new Replica that can be used in a conversation.


        By default, all new replicas will be trained using the `phoenix-3`
        model. You can optionally create phoenix-2 replicas by setting the
        `model_name` parameter to `phoenix-2`.


        The only required body parameter is `train_video_url`. This url must be
        a download link such as a presigned S3 url. Please ensure you pass in a
        video that meets the
        [requirements](/sections/troubleshooting/training-video-size) for
        training.


        Replica training will fail without the following consent statement being
        present at the beginning of the video:

        > I, [FULL NAME], am currently speaking and consent Tavus to create an
        AI clone of me by using the audio and video samples I provide. I
        understand that this AI clone can be used to create videos that look and
        sound like me.


        Learn more about the consent statement
        [here](/sections/troubleshooting/consent-statement).


        Learn more about training a personal Replica
        [here](/sections/replicas/personal-replicas).
      operationId: createReplica
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                consent_video_url:
                  type: string
                  description: >-
                    A direct link to a video that contains the consent
                    statement. You may optionally send the consent statement in
                    a separate video from your training video. If you do not
                    provide a consent video, the consent statement must be
                    present at the beginning of the training video. **This value
                    is required if you want to create a personal replica**.
                  example: >-
                    https://my-example-bucket.s3.us-east-1.amazonaws.com/your-consent-video.mp4
                train_video_url:
                  type: string
                  description: >-
                    A direct link to a publicly accessible storage location such
                    as an S3 bucket. This video will be used for replica
                    training.
                  example: >-
                    https://my-example-bucket.s3.us-east-1.amazonaws.com/your-train-video.mp4
                callback_url:
                  type: string
                  description: >-
                    A url that will receive a callback on completion of replica
                    training or on error.
                  example: https://yourwebsite.com/webhook
                replica_name:
                  type: string
                  description: A name for the replica.
                  example: Rio
                model_name:
                  type: string
                  description: >-
                    The phoenix model version that will be used to train the
                    replica. The current default is `phoenix-3`.
                  example: phoenix-3
                properties:
                  type: object
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
              required:
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  replica_id:
                    type: string
                    example: r783537ef5
                    description: A unique identifier for the replica.
                  status:
                    type: string
                    example: started
                    description: >-
                      The status of the replica. Possible values: `started`,
                      `completed`, `error`.
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Invalid train_video_url
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid access token
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````