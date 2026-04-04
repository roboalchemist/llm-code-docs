# Source: https://docs.tavus.io/api-reference/video-request/create-video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate Video

> This endpoint generates a new video using a Replica and either a script or an audio file. 

The only required body parameters are `replica_id` and either `script` or `audio_file`. 

The `replica_id` is a unique identifier for the Replica that will be used to generate the video. The `script` is the text that will be spoken by the Replica in the video. If you would like to generate a video using an audio file instead of a script, you can provide `audio_url` instead of `script`. Currently, `.wav` and `.mp3` files are supported for audio file input.

If a `background_url` is provided, Tavus will record a video of the website and use it as the background for the video. If a `background_source_url` is provided, where the URL points to a download link such as a presigned S3 URL, Tavus will use the video as the background for the video. If neither are provided, the video will consist of a full screen Replica.

To learn more about generating videos with Replicas, see [here](/sections/video/quickstart).

To learn more about writing an effective script for your video, see [Scripting prompting](/sections/troubleshooting#script-length).




## OpenAPI

````yaml post /v2/videos
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
  /v2/videos:
    post:
      tags:
        - Videos
      summary: Generate Video
      description: >
        This endpoint generates a new video using a Replica and either a script
        or an audio file. 


        The only required body parameters are `replica_id` and either `script`
        or `audio_file`. 


        The `replica_id` is a unique identifier for the Replica that will be
        used to generate the video. The `script` is the text that will be spoken
        by the Replica in the video. If you would like to generate a video using
        an audio file instead of a script, you can provide `audio_url` instead
        of `script`. Currently, `.wav` and `.mp3` files are supported for audio
        file input.


        If a `background_url` is provided, Tavus will record a video of the
        website and use it as the background for the video. If a
        `background_source_url` is provided, where the URL points to a download
        link such as a presigned S3 URL, Tavus will use the video as the
        background for the video. If neither are provided, the video will
        consist of a full screen Replica.


        To learn more about generating videos with Replicas, see
        [here](/sections/video/quickstart).


        To learn more about writing an effective script for your video, see
        [Scripting prompting](/sections/troubleshooting#script-length).
      operationId: generateVideo
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                replica_id:
                  type: string
                  description: >-
                    A unique identifier for the replica that will be used to
                    generate the video.
                  example: r783537ef5
                video_name:
                  type: string
                  description: A name for the video.
                  example: My First Video
                background_url:
                  type: string
                  description: >-
                    A link to a website. This will be used as the background for
                    the video. The website must be publicly accessible and
                    properly formed.
                  example: https://yourwebsite.com/
                background_source_url:
                  type: string
                  description: >-
                    A direct link to a video that is publicly accessible via a
                    storage location such as an S3 bucket. This will be used as
                    the background for the video. The video must be publicly
                    accessible.
                  example: >-
                    https://my-example-bucket.s3.us-east-1.amazonaws.com/your-background-video.mp4
                callback_url:
                  type: string
                  description: >-
                    A url that will receive a callback on completion of video
                    generation or on error.
                  example: https://yourwebsite.com/webhook
                fast:
                  type: boolean
                  description: >-
                    If set to true, the video will be generated using a
                    barebones fast rendering process. This will result in a
                    faster generation of the video but some features will be
                    disabled. Features such as background generation, thumbnail
                    images, and streaming urls are not supported when using this
                    fast rendering process.
                  example: false
                transparent_background:
                  type: boolean
                  description: >
                    If set to true, the generated video will be a `.webm` video
                    with a transparent background.


                    Please note that this feature only works if the `fast`
                    parameter is set to `true`.
                  example: false
                watermark_image_url:
                  type: string
                  description: >-
                    A direct link to a image that is publicly accessible via a
                    storage location such as an S3 bucket. This will be used as
                    the watermark on the video. Currently, it support `png` &
                    `jpeg` formats only. Ensure the image is publicly
                    accessible.
                  example: https://s3.amazonaws.com/watermark.png
                properties:
                  type: object
                  properties:
                    background_scroll:
                      type: boolean
                      description: >
                        If `background_url` is provided, this option may be
                        configured.


                        If set to `true`, the background video will scroll down
                        through the website. If set to `false`, the background
                        video will display the top of the website. 


                        The default is `true`.
                      example: true
                    background_scroll_type:
                      type: string
                      description: >
                        If `background_url` is provided and `background_scroll`
                        is set to `true`, this option may be configured.


                        This parameter defines the scroll pattern if
                        `background_scroll` is set to `true`. 


                        There are two options: `human`, `smooth`. 


                        The `human` scroll type is the default type and mimics a
                        human scrolling through the webpage, briefly stopping at
                        certain intervals to give a natural appearance. The
                        `smooth` scroll type scroll in a uniform manner all the
                        way down the website without stopping.


                        The default is `human`.
                    background_scroll_depth:
                      type: string
                      description: >
                        If `background_url` is provided and `background_scroll`
                        is set to `true`, this option may be configured.

                         This parameter defines how far down the webpage the background video will scroll.
                         
                         There are two options: `middle`, `bottom`.
                         
                         The `middle` depth option will stop scrolling once the middle of the webpage has been hit. The `bottom` will scroll the webpage all the way to the bottom of the page.
                         
                         The default is `middle`.
                    background_scroll_return:
                      type: string
                      description: >
                        If `background_url` is provided and `background_scroll`
                        is set to `true`, this option may be configured.


                        This parameter defines the scrolling behavior once the
                        webpage has been scrolled to the depth specified by the
                        `background_scroll_depth` parameter.


                        There are two options: `return`, `halt`.


                        The `return` option will scroll back up once the webpage
                        has reached `background_scroll_depth`. The `halt` option
                        will pause the background video at the location
                        specified in `background_scroll_depth`.


                        The default is `return`.
                    start_with_wave:
                      type: boolean
                      description: >
                        If set to true, the video will start with a wave
                        animation. This is only supported for select stock
                        replicas.


                        The default is `true`.
                      example: true
              required:
                - replica_id
              oneOf:
                - title: Generate from Text
                  type: object
                  properties:
                    script:
                      type: string
                      description: >-
                        A text script that will be used to generate the audio in
                        the video.
                      example: Hello from Tavus! Enjoy your new replica
                  required:
                    - script
                - title: Generate from Audio File
                  type: object
                  properties:
                    audio_url:
                      type: string
                      description: >-
                        A download link to a .wav or .mp3 file that is publicly
                        accessible via a storage location such as an S3 bucket.
                        This audio file will be used as the audio for the
                        generated video.
                  required:
                    - audio_url
            examples:
              Generate Video:
                value:
                  background_url: https://yourwebsite.com/
                  replica_id: r665388ec672
                  script: Hi, this is my first video.
                  video_name: My First Video
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  video_id:
                    type: string
                    example: abcd123
                    description: A unique identifier for the video.
                  video_name:
                    type: string
                    example: Sample Video
                    description: The name of the video.
                  status:
                    type: string
                    example: queued
                    description: >-
                      The status of the video. Possible values: queued,
                      generating, ready, deleted, error.
                  hosted_url:
                    type: string
                    example: https://tavus.video/abcd123
                    description: >-
                      A direct link to view your video once generation has
                      completed, hosted by Tavus.
                  created_at:
                    type: string
                    example: Mon, 14 Jul 2025 09:14:24 GMT
                    description: The date and time the video was created.
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
                    example: Invalid replica_id
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