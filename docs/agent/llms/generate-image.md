# Source: https://docs.agent.ai/api-reference/use-ai/generate-image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate Image

> Create visually engaging images using AI models, with options for style, aspect ratio, and detailed prompts.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/generate_image
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/generate_image:
    post:
      tags:
        - Use AI
      summary: Generate Image
      description: >-
        Create visually engaging images using AI models, with options for style,
        aspect ratio, and detailed prompts.
      operationId: generateImage
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
                  description: >-
                    Generates an image based on the provided text. Example user
                    prompt: generate an image of a sunset using the DALL-E 3
                    model.
                  example: A serene mountain lake at sunset
                model:
                  type: string
                  enum:
                    - DALL-E 3
                    - Playground v3
                    - FLUX.1 [schnell]
                    - Ideogram
                  default: DALL-E 3
                  description: LLM model to use for text generation.
                model_style:
                  type: string
                  enum:
                    - default
                    - photo
                    - digital art
                    - illustration
                    - drawing
                  default: default
                  description: Style
                model_aspect_ratio:
                  type: string
                  enum:
                    - '9:16'
                    - '1:1'
                    - '4:3'
                    - '16:9'
                  default: '9:16'
                  description: Aspect Ratio
              required:
                - prompt
                - model
                - model_style
                - model_aspect_ratio
      responses:
        '200':
          description: Generate Image
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                metadata:
                  images:
                    - prompt: A serene mountain lake at sunset
                      url: >-
                        https://s3.us-east-2.amazonaws.com/asset-uploads.agent.ai/6b55e6923a78a17534d298e0708c764425dffc85fbd9c1c2d4f8fb3f_8af27bf1-c121-484f-a456-4c6c5628c5d0_20250217144148.jpg
                response: >-
                  <img
                  src="https://s3.us-east-2.amazonaws.com/asset-uploads.agent.ai/6b55e6923a78a17534d298e0708c764425dffc85fbd9c1c2d4f8fb3f_8af27bf1-c121-484f-a456-4c6c5628c5d0_20250217144148.jpg"
                  alt="A serene mountain lake at sunset" /><br />
                status: 200
components:
  schemas:
    ActionResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        response:
          type: object
          description: Response data from the action
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````