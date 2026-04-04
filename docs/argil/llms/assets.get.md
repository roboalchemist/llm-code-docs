# Source: https://docs.argil.ai/api-reference/endpoint/assets.get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an Asset by id

> Returns a single Asset identified by its id

Returns an asset identified by its id from your library that can be used in your videos.

## Audio Assets

Audio assets from this endpoint can be used as background music in your videos. When creating a video, you can reference an audio asset's ID in the `backgroundMusic` parameter to add it as background music. See the [Create Video endpoint](/api-reference/endpoint/videos.create) for more details.

***


## OpenAPI

````yaml get /assets/{id}
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
  /assets/{id}:
    get:
      summary: Get an Asset by id
      description: Returns a single Asset identified by its id
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            description: The id of the Asset to retrieve
      responses:
        '200':
          description: Detailed information about the Asset
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Asset'
        '404':
          description: Asset not found
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