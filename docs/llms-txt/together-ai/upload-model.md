# Source: https://docs.together.ai/reference/upload-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a custom model or adapter

> Upload a custom model or adapter from Hugging Face or S3



## OpenAPI

````yaml POST /models
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
  /models:
    post:
      tags:
        - Models
      summary: Upload a custom model or adapter
      description: Upload a custom model or adapter from Hugging Face or S3
      operationId: uploadModel
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ModelUploadRequest'
      responses:
        '200':
          description: Model / adapter upload job created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelUploadSuccessResponse'
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

            response = client.models.upload(
                model_name="My-Fine-Tuned-Model",
                model_source="https://ml-models.s3.us-west-2.amazonaws.com/models/my-fine-tuned-model.tar.gz",
            )

            print(response.data.job_id)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            response = client.models.upload(
                "My-Fine-Tuned-Model",
                "https://ml-models.s3.us-west-2.amazonaws.com/models/my-fine-tuned-model.tar.gz",
            )

            print(response.job_id)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.models.upload({
              model_name: "My-Fine-Tuned-Model",
              model_source: "https://ml-models.s3.us-west-2.amazonaws.com/models/my-fine-tuned-model.tar.gz",
            })

            console.log(response);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.models.upload({
              model_name: "My-Fine-Tuned-Model",
              model_source: "https://ml-models.s3.us-west-2.amazonaws.com/models/my-fine-tuned-model.tar.gz",
            })

            console.log(response);
        - lang: Shell
          label: cURL
          source: |
            curl -X POST "https://api.together.xyz/v1/models" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json" \
                 -d '{
                    "model_name": "My-Fine-Tuned-Model",
                    "model_source": "https://ml-models.s3.us-west-2.amazonaws.com/models/my-fine-tuned-model.tar.gz"
                  }'
components:
  schemas:
    ModelUploadRequest:
      type: object
      required:
        - model_name
        - model_source
      properties:
        model_name:
          type: string
          description: The name to give to your uploaded model
          example: Qwen2.5-72B-Instruct
        model_source:
          type: string
          description: The source location of the model (Hugging Face repo or S3 path)
          example: unsloth/Qwen2.5-72B-Instruct
        model_type:
          type: string
          description: Whether the model is a full model or an adapter
          default: model
          enum:
            - model
            - adapter
          example: model
        hf_token:
          type: string
          description: Hugging Face token (if uploading from Hugging Face)
          example: hf_examplehuggingfacetoken
        description:
          type: string
          description: A description of your model
          example: Finetuned Qwen2.5-72B-Instruct by Unsloth
        base_model:
          type: string
          description: >-
            The base model to use for an adapter if setting it to run against a
            serverless pool.  Only used for model_type `adapter`.
          example: Qwen/Qwen2.5-72B-Instruct
        lora_model:
          type: string
          description: >-
            The lora pool to use for an adapter if setting it to run against,
            say, a dedicated pool.  Only used for model_type `adapter`.
          example: my_username/Qwen2.5-72B-Instruct-lora
    ModelUploadSuccessResponse:
      type: object
      required:
        - data
        - message
      properties:
        data:
          type: object
          required:
            - job_id
            - model_name
            - model_id
            - model_source
          properties:
            job_id:
              type: string
              example: job-a15dad11-8d8e-4007-97c5-a211304de284
            model_name:
              type: string
              example: necolinehubner/Qwen2.5-72B-Instruct
            model_id:
              type: string
              example: model-c0e32dfc-637e-47b2-bf4e-e9b2e58c9da7
            model_source:
              type: string
              example: huggingface
        message:
          type: string
          example: Processing model weights. Job created.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).