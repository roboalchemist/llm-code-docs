# Source: https://docs.together.ai/reference/create-videos.md

# Create Video

> Create a video



## OpenAPI

````yaml POST /videos
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /videos:
    post:
      tags:
        - Video
      summary: Create video
      description: Create a video
      operationId: createVideo
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateVideoBody'
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VideoJob'
      servers:
        - url: https://api.together.xyz/v2
components:
  schemas:
    CreateVideoBody:
      title: Create video request
      description: Parameters for creating a new video generation job.
      type: object
      required:
        - model
      properties:
        model:
          type: string
          description: The model to be used for the video creation request.
        prompt:
          type: string
          maxLength: 32000
          minLength: 1
          description: Text prompt that describes the video to generate.
        height:
          type: integer
        width:
          type: integer
        seconds:
          type: string
          description: Clip duration in seconds.
        fps:
          type: integer
          description: Frames per second. Defaults to 24.
        steps:
          type: integer
          minimum: 10
          maximum: 50
          description: >-
            The number of denoising steps the model performs during video
            generation. More steps typically result in higher quality output but
            require longer processing time.
        seed:
          type: integer
          description: >-
            Seed to use in initializing the video generation.  Using the same
            seed allows deterministic video generation.  If not provided a
            random seed is generated for each request.
        guidance_scale:
          type: integer
          description: "Controls how closely the video generation follows your prompt. Higher values make the model adhere more strictly to your text description, while lower values allow more creative freedom.\_guidence_scale\_affects both visual content and temporal consistency.Recommended range is 6.0-10.0 for most video models. Values above 12 may cause over-guidance artifacts or unnatural motion patterns."
        output_format:
          $ref: '#/components/schemas/VideoOutputFormat'
          description: Specifies the format of the output video. Defaults to MP4.
        output_quality:
          type: integer
          description: Compression quality. Defaults to 20.
        negative_prompt:
          type: string
          description: >-
            Similar to prompt, but specifies what to avoid instead of what to
            include
        frame_images:
          description: Array of images to guide video generation, similar to keyframes.
          example:
            - - input_image: aac49721-1964-481a-ae78-8a4e29b91402
                frame: 0
              - input_image: c00abf5f-6cdb-4642-a01d-1bfff7bc3cf7
                frame: 48
              - input_image: 3ad204c3-a9de-4963-8a1a-c3911e3afafe
                frame: last
          type: array
          items:
            $ref: '#/components/schemas/VideoFrameImageInput'
        reference_images:
          description: >-
            Unlike frame_images which constrain specific timeline positions,
            reference images guide the general appearance that should appear
            consistently across the video.
          type: array
          items:
            type: string
    VideoJob:
      properties:
        id:
          type: string
          description: Unique identifier for the video job.
        object:
          description: The object type, which is always video.
          type: string
          enum:
            - video
        model:
          type: string
          description: The video generation model that produced the job.
        status:
          $ref: '#/components/schemas/VideoStatus'
          description: Current lifecycle status of the video job.
        created_at:
          type: number
          description: Unix timestamp (seconds) for when the job was created.
        completed_at:
          type: number
          description: Unix timestamp (seconds) for when the job completed, if finished.
        size:
          type: string
          description: The resolution of the generated video.
        seconds:
          type: string
          description: Duration of the generated clip in seconds.
        error:
          description: Error payload that explains why generation failed, if applicable.
          type: object
          properties:
            code:
              type: string
            message:
              type: string
          required:
            - message
        outputs:
          description: >-
            Available upon completion, the outputs provides the cost charged and
            the hosted url to access the video
          type: object
          properties:
            cost:
              type: integer
              description: The cost of generated video charged to the owners account.
            video_url:
              type: string
              description: URL hosting the generated video
          required:
            - cost
            - video_url
      type: object
      required:
        - id
        - model
        - status
        - size
        - seconds
        - created_at
      title: Video job
      description: Structured information describing a generated video job.
    VideoOutputFormat:
      type: string
      enum:
        - MP4
        - WEBM
    VideoFrameImageInput:
      type: object
      required:
        - input_image
      properties:
        input_image:
          type: string
          description: URL path to hosted image that is used for a frame
        frame:
          description: >
            Optional param to specify where to insert the frame. If this is
            omitted, the following heuristics are applied:

            - frame_images size is one, frame is first.

            - If size is two, frames are first and last.

            - If size is larger, frames are first, last and evenly spaced
            between.
          anyOf:
            - type: number
            - type: string
              enum:
                - first
                - last
    VideoStatus:
      description: Current lifecycle status of the video job.
      type: string
      enum:
        - in_progress
        - completed
        - failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt