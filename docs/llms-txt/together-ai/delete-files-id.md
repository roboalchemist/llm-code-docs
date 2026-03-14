# Source: https://docs.together.ai/reference/delete-files-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete A File

> Delete a previously uploaded data file.



## OpenAPI

````yaml DELETE /files/{id}
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
    delete:
      tags:
        - Files
      summary: Delete a file
      description: Delete a previously uploaded data file.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: The ID of the file to delete
            type: string
      responses:
        '200':
          description: File deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileDeleteResponse'
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

            response = client.files.delete(id="file-id")

            print(response)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            response = client.files.delete(id="file-id")

            print(response)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.files.delete("file-id");

            console.log(response);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.files.delete("file-id");

            console.log(response);
        - lang: Shell
          label: cURL
          source: |
            curl -X "DELETE" "https://api.together.xyz/v1/files/file-id" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY"
components:
  schemas:
    FileDeleteResponse:
      type: object
      properties:
        id:
          type: string
        deleted:
          type: boolean
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).