# Source: https://dev.writer.com/api-reference/tool-api/pdf-parser.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Parse PDF

> Parse PDF to other formats.

<Warning>
  **Deprecation notice**: The [parse PDF API endpoint](/api-reference/tool-api/pdf-parser) at `/v1/tools/pdf-parser/{file_id}` is deprecated and will be removed on **December 22, 2025**.

  **Migration path**: We plan to introduce a prebuilt PDF parsing tool for chat completions that will provide similar functionality. This tool will work similarly to other prebuilt tools like the [Vision tool](/home/vision-tool) or [LLM tool](/home/model-delegation). We will provide more details about this alternative when it becomes available.
</Warning>


## OpenAPI

````yaml post /v1/tools/pdf-parser/{file_id}
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/tools/pdf-parser/{file_id}:
    post:
      tags:
        - Tools API
      summary: Parse PDF
      description: Parse PDF to other formats.
      parameters:
        - name: file_id
          in: path
          required: true
          schema:
            type: string
          description: The unique identifier of the file.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/parse_pdf_request'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/parse_pdf_response'
      security:
        - bearerAuth: []
components:
  schemas:
    parse_pdf_request:
      title: parse_pdf_request
      required:
        - format
      type: object
      properties:
        format:
          $ref: '#/components/schemas/pdf_conversion_format'
    parse_pdf_response:
      title: parse_pdf_response
      required:
        - content
      type: object
      properties:
        content:
          type: string
          description: >-
            The extracted content from the PDF file, converted to the specified
            format.
    pdf_conversion_format:
      title: pdf_conversion_format
      type: string
      enum:
        - text
        - markdown
      description: The format into which the PDF content should be converted.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````