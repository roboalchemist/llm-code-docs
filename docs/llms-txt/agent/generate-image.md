# Source: https://docs.agent.ai/api-reference/use-ai/generate-image.md

# Generate Image

> Create visually engaging images using AI models, with options for style, aspect ratio, and detailed prompts.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/generate_image
paths:
  path: /action/generate_image
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
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
              prompt:
                allOf:
                  - type: string
                    description: >-
                      Generates an image based on the provided text. Example
                      user prompt: generate an image of a sunset using the
                      DALL-E 3 model.
                    example: A serene mountain lake at sunset
              model:
                allOf:
                  - type: string
                    enum:
                      - DALL-E 3
                      - Playground v3
                      - FLUX.1 [schnell]
                      - Ideogram
                    default: DALL-E 3
                    description: LLM model to use for text generation.
              model_style:
                allOf:
                  - type: string
                    enum:
                      - default
                      - photo
                      - digital art
                      - illustration
                      - drawing
                    default: default
                    description: Style
              model_aspect_ratio:
                allOf:
                  - type: string
                    enum:
                      - '9:16'
                      - '1:1'
                      - '4:3'
                      - '16:9'
                    default: '9:16'
                    description: Aspect Ratio
            required: true
            requiredProperties:
              - prompt
              - model
              - model_style
              - model_aspect_ratio
        examples:
          example:
            value:
              prompt: A serene mountain lake at sunset
              model: DALL-E 3
              model_style: default
              model_aspect_ratio: '9:16'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
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
        description: Generate Image
  deprecated: false
  type: path
components:
  schemas: {}

````