# Source: https://docs.together.ai/reference/upload-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a file

> Upload a file with specified purpose, file name, and file type.



## OpenAPI

````yaml POST /files/upload
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
  /files/upload:
    post:
      tags:
        - Files
      summary: Upload a file
      description: Upload a file with specified purpose, file name, and file type.
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - purpose
                - file_name
                - file
              properties:
                purpose:
                  $ref: '#/components/schemas/FilePurpose'
                file_name:
                  type: string
                  description: The name of the file being uploaded
                  example: dataset.csv
                file_type:
                  $ref: '#/components/schemas/FileType'
                file:
                  type: string
                  format: binary
                  description: The content of the file being uploaded
      responses:
        '200':
          description: File uploaded successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
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

            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "data.jsonl")
            file = client.files.upload(file=file_path)

            print(file.id)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "data.jsonl")
            file = client.files.upload(file=file_path)

            print(file.id)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import { upload } from "together-ai/lib/upload"
            import path from "path";
            import { fileURLToPath } from "url";

            const __filename = fileURLToPath(import.meta.url);
            const __dirname = path.dirname(__filename);
            const filepath = path.join(__dirname, "data.jsonl");
            const file = await upload(filepath);

            console.log(file.id);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import { upload } from "together-ai/lib/upload"
            import path from "path";
            import { fileURLToPath } from "url";

            const __filename = fileURLToPath(import.meta.url);
            const __dirname = path.dirname(__filename);
            const filepath = path.join(__dirname, "data.jsonl");
            const file = await upload(filepath);

            console.log(file.id);
        - lang: Shell
          label: cURL
          source: |
            curl "https://api.together.xyz/v1/files/upload" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -F "file=@/path/to/data.jsonl" \
                 -F "file_name=data.jsonl" \
                 -F "purpose=fine-tune"
components:
  schemas:
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
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).