# Source: https://docs.wandb.ai/weave/reference/service-api/images/image-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Create



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /image/create
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /image/create:
    post:
      tags:
        - Images
      summary: Image Create
      operationId: image_create_image_create_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ImageGenerationCreateReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ImageGenerationCreateRes'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBasic: []
components:
  schemas:
    ImageGenerationCreateReq:
      properties:
        project_id:
          type: string
          title: Project Id
        inputs:
          $ref: '#/components/schemas/ImageGenerationRequestInputs'
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
        track_llm_call:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Track Llm Call
          description: Whether to track this image generation call in the trace server
          default: true
      type: object
      required:
        - project_id
        - inputs
      title: ImageGenerationCreateReq
    ImageGenerationCreateRes:
      properties:
        response:
          additionalProperties: true
          type: object
          title: Response
        weave_call_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Weave Call Id
      type: object
      required:
        - response
      title: ImageGenerationCreateRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ImageGenerationRequestInputs:
      properties:
        model:
          type: string
          title: Model
        prompt:
          type: string
          title: Prompt
        'n':
          anyOf:
            - type: integer
            - type: 'null'
          title: 'N'
      type: object
      required:
        - model
        - prompt
      title: ImageGenerationRequestInputs
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````