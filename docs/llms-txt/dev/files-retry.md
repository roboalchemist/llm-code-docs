# Source: https://dev.writer.com/api-reference/file-api/files-retry.md

# Retry failed files

> Retry processing of files that previously failed to process. This will re-attempt the processing of the specified files.

## OpenAPI

````yaml post /v1/files/retry
paths:
  path: /v1/files/retry
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              file_ids:
                allOf:
                  - type: array
                    items:
                      type: string
                      format: uuid
                    description: The unique identifier of the files to retry.
            required: true
            title: retry_files_request
            refIdentifier: '#/components/schemas/retry_files_request'
            requiredProperties:
              - file_ids
        examples:
          example:
            value:
              file_ids:
                - 3c90c3cc-0d44-4b50-8888-8dd25736052a
    codeSamples:
      - lang: cURL
        source: |-
          curl --location --request POST https://api.writer.com/v1/files/retry \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
           --data-raw '{"file_ids":["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const response = await client.files.retry({
              file_ids: [
                '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
                '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
                '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
              ],
            });

            console.log(response.success);
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
          response = client.files.retry(
              file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
          )
          print(response.success)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              success:
                allOf:
                  - type: boolean
                    description: Indicates whether the retry operation was successful.
            title: retry_files_response
            refIdentifier: '#/components/schemas/retry_files_response'
        examples:
          example:
            value:
              success: true
        description: The retry request is being processed
  deprecated: false
  type: path
components:
  schemas: {}

````