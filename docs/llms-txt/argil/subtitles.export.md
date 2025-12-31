# Source: https://docs.argil.ai/api-reference/endpoint/subtitles.export.md

# Export subtitles for a video project

> Exports subtitles for a video project in VTT or ASS format. The subtitles can optionally include styling information.



## OpenAPI

````yaml get /subtitles/videos/{videoProjectId}/export
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
  /subtitles/videos/{videoProjectId}/export:
    get:
      summary: Export subtitles for a video project
      description: >-
        Exports subtitles for a video project in VTT or ASS format. The
        subtitles can optionally include styling information.
      parameters:
        - name: videoProjectId
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The UUID of the video project to export subtitles for
        - name: format
          in: query
          description: Subtitle format to export (vtt or ass)
          required: false
          schema:
            type: string
            enum:
              - vtt
              - ass
            default: vtt
        - name: includeStyling
          in: query
          description: Whether to include styling information in the exported subtitles
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Subtitle file content
          content:
            text/vtt:
              schema:
                type: string
                description: VTT subtitle file content
            text/x-ass:
              schema:
                type: string
                description: ASS subtitle file content
          headers:
            Content-Type:
              description: Content type of the response (text/vtt or text/x-ass)
              schema:
                type: string
            Content-Disposition:
              description: Attachment header with filename
              schema:
                type: string
        '400':
          description: Validation error or invalid request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Video project not found or user does not have access
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.argil.ai/llms.txt