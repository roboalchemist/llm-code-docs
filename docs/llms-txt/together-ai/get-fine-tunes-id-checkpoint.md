# Source: https://docs.together.ai/reference/get-fine-tunes-id-checkpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List checkpoints

> List the checkpoints for a single fine-tuning job.



## OpenAPI

````yaml GET /fine-tunes/{id}/checkpoints
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
  /fine-tunes/{id}/checkpoints:
    get:
      tags:
        - Fine-tuning
      summary: List checkpoints
      description: List the checkpoints for a single fine-tuning job.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: The ID of the fine-tune job to list checkpoints for
            type: string
      responses:
        '200':
          description: List of fine-tune checkpoints
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinetuneListCheckpoints'
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

            checkpoints = client.fine_tuning.list_checkpoints(id="ft-id")

            print(checkpoints)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            checkpoints = client.fine_tuning.list_checkpoints(id="ft-id")

            print(checkpoints)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: >
            import Together from "together-ai";


            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });


            const checkpoints = await
            client.fineTuning.listCheckpoints("ft-id");


            console.log(checkpoints);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: >
            import Together from "together-ai";


            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });


            const checkpoints = await
            client.fineTuning.listCheckpoints("ft-id");


            console.log(checkpoints);
        - lang: Shell
          label: cURL
          source: |
            curl "https://api.together.xyz/v1/fine-tunes/ft-id/checkpoints" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json"
components:
  schemas:
    FinetuneListCheckpoints:
      type: object
      required:
        - data
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/FineTuneCheckpoint'
    FineTuneCheckpoint:
      type: object
      required:
        - step
        - path
        - created_at
        - checkpoint_type
      properties:
        step:
          type: integer
        created_at:
          type: string
        path:
          type: string
        checkpoint_type:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).