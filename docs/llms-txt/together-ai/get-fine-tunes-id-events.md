# Source: https://docs.together.ai/reference/get-fine-tunes-id-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Job Events

> List the events for a single fine-tuning job.



## OpenAPI

````yaml GET /fine-tunes/{id}/events
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
  /fine-tunes/{id}/events:
    get:
      tags:
        - Fine-tuning
      summary: List job events
      description: List the events for a single fine-tuning job.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: The ID of the fine-tune job to list events for
            type: string
      responses:
        '200':
          description: List of fine-tune events
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinetuneListEvents'
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

            response = client.fine_tuning.list_events(id="ft-id")

            for event in response.data:
                print(event)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            events = client.fine_tuning.list_events(id="ft-id")

            print(events)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const events = await client.fineTuning.listEvents("ft-id");

            console.log(events);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const events = await client.fineTuning.listEvents("ft-id");

            console.log(events);
        - lang: Shell
          label: cURL
          source: |
            curl "https://api.together.xyz/v1/fine-tunes/ft-id/events" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json"
components:
  schemas:
    FinetuneListEvents:
      type: object
      required:
        - data
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/FineTuneEvent'
    FineTuneEvent:
      type: object
      required:
        - object
        - created_at
        - message
        - type
        - param_count
        - token_count
        - total_steps
        - wandb_url
        - step
        - checkpoint_path
        - model_path
        - training_offset
        - hash
      properties:
        object:
          description: The object type, which is always `fine-tune-event`.
          const: fine-tune-event
        created_at:
          type: string
        level:
          anyOf:
            - $ref: '#/components/schemas/FinetuneEventLevels'
        message:
          type: string
        type:
          $ref: '#/components/schemas/FinetuneEventType'
        param_count:
          type: integer
        token_count:
          type: integer
        total_steps:
          type: integer
        wandb_url:
          type: string
        step:
          type: integer
        checkpoint_path:
          type: string
        model_path:
          type: string
        training_offset:
          type: integer
        hash:
          type: string
    FinetuneEventLevels:
      type: string
      enum:
        - null
        - info
        - warning
        - error
        - legacy_info
        - legacy_iwarning
        - legacy_ierror
    FinetuneEventType:
      type: string
      enum:
        - job_pending
        - job_start
        - job_stopped
        - model_downloading
        - model_download_complete
        - training_data_downloading
        - training_data_download_complete
        - validation_data_downloading
        - validation_data_download_complete
        - wandb_init
        - training_start
        - checkpoint_save
        - billing_limit
        - epoch_complete
        - training_complete
        - model_compressing
        - model_compression_complete
        - model_uploading
        - model_upload_complete
        - job_complete
        - job_error
        - cancel_requested
        - job_restarted
        - refund
        - warning
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).