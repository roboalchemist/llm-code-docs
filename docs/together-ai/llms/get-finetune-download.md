# Source: https://docs.together.ai/reference/get-finetune-download.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Download Model

> Receive a compressed fine-tuned model or checkpoint.



## OpenAPI

````yaml GET /finetune/download
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
  /finetune/download:
    get:
      tags:
        - Fine-tuning
      summary: Download model
      description: Receive a compressed fine-tuned model or checkpoint.
      parameters:
        - in: query
          name: ft_id
          required: true
          schema:
            description: Fine-tune ID to download. A string that starts with `ft-`.
            type: string
        - in: query
          name: checkpoint_step
          required: false
          schema:
            description: >-
              Specifies step number for checkpoint to download. Ignores
              `checkpoint` value if set.
            type: integer
        - in: query
          name: checkpoint
          schema:
            description: >-
              Specifies checkpoint type to download - `merged` vs `adapter`.
              This field is required if the checkpoint_step is not set.
            type: string
            enum:
              - merged
              - adapter
              - model_output_path
      responses:
        '200':
          description: Successfully downloaded the fine-tuned model or checkpoint.
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '400':
          description: Invalid request parameters.
        '404':
          description: Fine-tune ID not found.
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


            # Using `with_streaming_response` gives you control to do what you
            want with the response.

            stream =
            client.fine_tuning.with_streaming_response.content(ft_id="ft-id")


            with stream as response:
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

            # This will download the content to a location on disk
            response = client.fine_tuning.download(id="ft-id")

            print(response)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.fineTuning.content({
              ft_id: "ft-id",
            });

            console.log(await response.blob());
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.fineTuning.content({
              ft_id: "ft-id",
            });

            console.log(await response.blob());
        - lang: Shell
          label: cURL
          source: >
            curl
            "https://api.together.xyz/v1/finetune/download?ft_id=ft-id&checkpoint=merged"
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json"
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).