# Source: https://docs.argil.ai/api-reference/endpoint/assets.list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Assets

> Get a list of available assets from your library

Returns an array of assets from your library that can be used in your videos.

## Audio Assets

Audio assets from this endpoint can be used as background music in your videos. When creating a video, you can reference an audio asset's ID in the `backgroundMusic` parameter to add it as background music. See the [Create Video endpoint](/api-reference/endpoint/videos.create) for more details.

***


## OpenAPI

````yaml get /assets
openapi: 3.0.1
info:
  title: Argil API
  description: API for AI clone video generation
  version: 1.0.0
  license:
    name: MIT
servers:
  - url: https://api.argil.ai/v1
security:
  - ApiKeyAuth: []
paths:
  /assets:
    get:
      summary: List audio assets
      description: Returns an array of audio assets available for the user
      responses:
        '200':
          description: An array of audio assets
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Asset'
        '400':
          description: Unexpected error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Asset:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        type:
          type: string
          enum:
            - AUDIO
        fileUrl:
          type: string
          description: URL to access the asset
    Error:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````