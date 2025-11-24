# Source: https://dev.writer.com/api-reference/tool-api/pdf-parser.md

# Parse PDF

> Parse PDF to other formats.

## OpenAPI

````yaml post /v1/tools/pdf-parser/{file_id}
paths:
  path: /v1/tools/pdf-parser/{file_id}
  method: post
  servers:
    - url: https://api.writer.com
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
                Bearer authentication header of the form `Bearer <token>`, where
                `<token>` is your [Writer API
                key](https://dev.writer.com/api-reference/api-keys).
          cookie: {}
    parameters:
      path:
        file_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the file.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              format:
                allOf:
                  - $ref: '#/components/schemas/pdf_conversion_format'
            required: true
            title: parse_pdf_request
            refIdentifier: '#/components/schemas/parse_pdf_request'
            requiredProperties:
              - format
        examples:
          example:
            value:
              format: text
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST
          https://api.writer.com/v1/tools/pdf-parser/{file_id} \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw '{"format":"text"}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const response = await client.tools.parsePdf('file_id', { format: 'text' });

            console.log(response.content);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              # This is the default and can be omitted
              api_key=os.environ.get("WRITER_API_KEY"),
          )
          response = client.tools.parse_pdf(
              file_id="file_id",
              format="text",
          )
          print(response.content)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              content:
                allOf:
                  - type: string
                    description: >-
                      The extracted content from the PDF file, converted to the
                      specified format.
            title: parse_pdf_response
            refIdentifier: '#/components/schemas/parse_pdf_response'
            requiredProperties:
              - content
        examples:
          example:
            value:
              content: <string>
        description: ''
  deprecated: false
  type: path
components:
  schemas:
    pdf_conversion_format:
      title: pdf_conversion_format
      type: string
      enum:
        - text
        - markdown
      description: The format into which the PDF content should be converted.

````