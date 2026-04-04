# Source: https://docs.together.ai/reference/post-images-generations.md

# Create Image

> Use an image model to generate an image for a given prompt.



## OpenAPI

````yaml POST /images/generations
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
  /images/generations:
    post:
      tags:
        - Images
      summary: Create image
      description: Use an image model to generate an image for a given prompt.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - prompt
                - model
              properties:
                prompt:
                  type: string
                  description: >-
                    A description of the desired images. Maximum length varies
                    by model.
                  example: cat floating in space, cinematic
                model:
                  type: string
                  description: >
                    The model to use for image generation.<br> <br> [See all of
                    Together AI's image
                    models](https://docs.together.ai/docs/serverless-models#image-models)
                  example: black-forest-labs/FLUX.1-schnell
                  anyOf:
                    - type: string
                      enum:
                        - black-forest-labs/FLUX.1-schnell-Free
                        - black-forest-labs/FLUX.1-schnell
                        - black-forest-labs/FLUX.1.1-pro
                    - type: string
                steps:
                  type: integer
                  default: 20
                  description: Number of generation steps.
                image_url:
                  type: string
                  description: URL of an image to use for image models that support it.
                seed:
                  type: integer
                  description: >-
                    Seed used for generation. Can be used to reproduce image
                    generations.
                'n':
                  type: integer
                  default: 1
                  description: Number of image results to generate.
                height:
                  type: integer
                  default: 1024
                  description: Height of the image to generate in number of pixels.
                width:
                  type: integer
                  default: 1024
                  description: Width of the image to generate in number of pixels.
                negative_prompt:
                  type: string
                  description: The prompt or prompts not to guide the image generation.
                response_format:
                  type: string
                  description: >-
                    Format of the image response. Can be either a base64 string
                    or a URL.
                  enum:
                    - base64
                    - url
                guidance_scale:
                  type: number
                  description: >-
                    Adjusts the alignment of the generated image with the input
                    prompt. Higher values (e.g., 8-10) make the output more
                    faithful to the prompt, while lower values (e.g., 1-5)
                    encourage more creative freedom.
                  default: 3.5
                output_format:
                  type: string
                  description: >-
                    The format of the image response. Can be either be `jpeg` or
                    `png`. Defaults to `jpeg`.
                  default: jpeg
                  enum:
                    - jpeg
                    - png
                image_loras:
                  description: >-
                    An array of objects that define LoRAs (Low-Rank Adaptations)
                    to influence the generated image.
                  type: array
                  items:
                    type: object
                    required:
                      - path
                      - scale
                    properties:
                      path:
                        type: string
                        description: >-
                          The URL of the LoRA to apply (e.g.
                          https://huggingface.co/strangerzonehf/Flux-Midjourney-Mix2-LoRA).
                      scale:
                        type: number
                        description: >-
                          The strength of the LoRA's influence. Most LoRA's
                          recommend a value of 1.
                reference_images:
                  description: >-
                    An array of image URLs that guide the overall appearance and
                    style of the generated image. These reference images
                    influence the visual characteristics consistently across the
                    generation.
                  type: array
                  items:
                    type: string
                    description: URL of a reference image to guide the image generation.
                disable_safety_checker:
                  type: boolean
                  description: If true, disables the safety checker for image generation.
      responses:
        '200':
          description: Image generated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ImageResponse'
components:
  schemas:
    ImageResponse:
      type: object
      properties:
        id:
          type: string
        model:
          type: string
        object:
          enum:
            - list
          example: list
        data:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/ImageResponseDataB64'
              - $ref: '#/components/schemas/ImageResponseDataUrl'
            discriminator:
              propertyName: type
      required:
        - id
        - model
        - object
        - data
    ImageResponseDataB64:
      type: object
      required:
        - index
        - b64_json
        - type
      properties:
        index:
          type: integer
        b64_json:
          type: string
        type:
          type: string
          enum:
            - b64_json
    ImageResponseDataUrl:
      type: object
      required:
        - index
        - url
        - type
      properties:
        index:
          type: integer
        url:
          type: string
        type:
          type: string
          enum:
            - url
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt