# Source: https://docs.together.ai/reference/get-videos-id.md

# Get Video

> Fetch video metadata



## OpenAPI

````yaml GET /videos/{id}
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
  /videos/{id}:
    get:
      tags:
        - Video
      summary: Fetch video metadata
      description: Fetch video metadata
      operationId: retrieveVideo
      parameters:
        - in: path
          name: id
          schema:
            type: string
          required: true
          description: Identifier of video from create response.
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VideoJob'
        '400':
          description: Invalid request parameters.
        '404':
          description: Video ID not found.
      servers:
        - url: https://api.together.xyz/v2
components:
  schemas:
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