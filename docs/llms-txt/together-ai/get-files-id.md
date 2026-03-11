# Source: https://docs.together.ai/reference/get-files-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List File

> Retrieve the metadata for a single uploaded data file.



## OpenAPI

````yaml GET /files/{id}
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
  /files/{id}:
    get:
      tags:
        - Files
      summary: Retrieve file metadata
      description: Retrieve the metadata for a single uploaded data file.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: The ID of the file to retrieve
            type: string
      responses:
        '200':
          description: File retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileResponse'
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            # Docs for v1 can be found by changing the above selector ^
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            file = client.files.retrieve(id="file-id")

            print(file)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            file = client.files.retrieve(id="file-id")

            print(file)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const file = await client.files.retrieve("file-id");

            console.log(file);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const file = await client.files.retrieve("file-id");

            console.log(file);
        - lang: Shell
          label: cURL
          source: |
            curl "https://api.together.xyz/v1/files/ID" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json"
components:
  schemas:
    FileResponse:
      description: Structured information describing a file uploaded to Together.
      type: object
      required:
        - id
        - object
        - created_at
        - filename
        - bytes
        - purpose
        - FileType
        - Processed
      properties:
        id:
          description: ID of the file.
          type: string
        object:
          description: The object type, which is always `file`.
          const: file
        created_at:
          description: The timestamp when the file was created.
          type: integer
        filename:
          description: The name of the file as it was uploaded.
          type: string
          example: my_file.jsonl
        bytes:
          description: The number of bytes in the file.
          type: integer
        purpose:
          $ref: '#/components/schemas/FilePurpose'
          description: The purpose of the file as it was uploaded.
        Processed:
          description: >-
            Whether the file has been parsed and analyzed for correctness for
            fine-tuning.
          type: boolean
        FileType:
          $ref: '#/components/schemas/FileType'
          description: The type of the file such as `jsonl`, `csv`, or `parquet`.
    FilePurpose:
      type: string
      description: The purpose of the file
      example: fine-tune
      enum:
        - fine-tune
        - eval
        - eval-sample
        - eval-output
        - eval-summary
        - batch-generated
        - batch-api
    FileType:
      type: string
      description: The type of the file
      default: jsonl
      example: jsonl
      enum:
        - csv
        - jsonl
        - parquet
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).