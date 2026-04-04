# Source: https://docs.together.ai/reference/get-files-id-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get File Contents

> Get the contents of a single uploaded data file.



## OpenAPI

````yaml GET /files/{id}/content
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
  /files/{id}/content:
    get:
      tags:
        - Files
      summary: Get file contents
      description: Get the contents of a single uploaded data file.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: The ID of the file to get the content of
            type: string
      responses:
        '200':
          description: File content retrieved successfully
          content:
            text/plain:
              schema:
                type: string
                format: binary
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: >
            # Docs for v1 can be found by changing the above selector ^

            from together import Together

            import os


            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )


            with client.files.with_streaming_response.content(id="file-id") as
            response:
              for line in response.iter_lines():
                print(line)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            file = client.files.retrieve_content(id="file-id")

            print(file.filename)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.files.content("file-id");
            const content = await response.text();

            console.log(content);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.files.content("file-id");
            const content = await response.text();

            console.log(content);
        - lang: Shell
          label: cURL
          source: |
            curl "https://api.together.xyz/v1/files/file-id/content" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json"
components:
  schemas:
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