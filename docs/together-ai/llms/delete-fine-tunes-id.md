# Source: https://docs.together.ai/reference/delete-fine-tunes-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete A Fine-tuning Event

> Delete a fine-tuning job.



## OpenAPI

````yaml DELETE /fine-tunes/{id}
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
  /fine-tunes/{id}:
    delete:
      tags:
        - Fine-tuning
      summary: Delete a fine-tune job
      description: Delete a fine-tuning job.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: The ID of the fine-tune job to delete
            type: string
        - name: force
          deprecated: true
          in: query
          schema:
            description: Deprecated and unused parameter.
            type: boolean
            default: false
      responses:
        '200':
          description: Fine-tune job deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinetuneDeleteResponse'
        '404':
          description: Fine-tune job not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Internal server error
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

            response = client.fine_tuning.delete(id="ft-id")

            print(response)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            response = client.fine_tuning.delete(id="ft-id")

            print(response)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.fineTuning.delete("ft-id");

            console.log(response);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.fineTuning.delete("ft-id");

            console.log(response);
        - lang: Shell
          label: cURL
          source: >
            curl -X "DELETE"
            "https://api.together.xyz/v1/fine-tunes/ft-id?force=false" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json"
components:
  schemas:
    FinetuneDeleteResponse:
      type: object
      properties:
        message:
          type: string
          description: Message indicating the result of the deletion
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