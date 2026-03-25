# Source: https://docs.wandb.ai/weave/reference/service-api/inference/inference-router-openrouter-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Inference Router Openrouter Models

> Returns a list of models that are available to be used with OpenRouter.

This API is available without authentication.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /inference/router/openrouter/models
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /inference/router/openrouter/models:
    get:
      tags:
        - Inference
      summary: Inference Router Openrouter Models
      description: |-
        Returns a list of models that are available to be used with OpenRouter.

        This API is available without authentication.
      operationId: >-
        inference_router_openrouter_models_inference_router_openrouter_models_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RouterOpenRouterModelsRes'
components:
  schemas:
    RouterOpenRouterModelsRes:
      properties:
        data:
          items:
            $ref: '#/components/schemas/RouterOpenRouterModel'
          type: array
          title: Data
      type: object
      required:
        - data
      title: RouterOpenRouterModelsRes
    RouterOpenRouterModel:
      properties:
        id:
          type: string
          title: Id
        name:
          type: string
          title: Name
        created:
          type: integer
          title: Created
        input_modalities:
          items:
            type: string
          type: array
          title: Input Modalities
        output_modalities:
          items:
            type: string
          type: array
          title: Output Modalities
        quantization:
          type: string
          enum:
            - int4
            - int8
            - fp4
            - fp6
            - fp8
            - fp16
            - bf16
            - fp32
          title: Quantization
        context_length:
          type: integer
          title: Context Length
        max_output_length:
          type: integer
          title: Max Output Length
        pricing:
          $ref: '#/components/schemas/Pricing'
        supported_sampling_parameters:
          items:
            type: string
            enum:
              - temperature
              - top_p
              - top_k
              - repetition_penalty
              - frequency_penalty
              - presence_penalty
              - stop
              - seed
          type: array
          title: Supported Sampling Parameters
        supported_features:
          items:
            type: string
            enum:
              - tools
              - json_mode
              - structured_outputs
              - web_search
              - reasoning
          type: array
          title: Supported Features
        datacenters:
          items:
            $ref: '#/components/schemas/Datacenter'
          type: array
          title: Datacenters
      type: object
      required:
        - id
        - name
        - created
        - input_modalities
        - output_modalities
        - quantization
        - context_length
        - max_output_length
        - pricing
        - supported_sampling_parameters
        - supported_features
        - datacenters
      title: RouterOpenRouterModel
    Pricing:
      properties:
        prompt:
          type: string
          title: Prompt
        completion:
          type: string
          title: Completion
        image:
          type: string
          title: Image
        request:
          type: string
          title: Request
        input_cache_reads:
          type: string
          title: Input Cache Reads
        input_cache_writes:
          type: string
          title: Input Cache Writes
      type: object
      required:
        - prompt
        - completion
        - image
        - request
        - input_cache_reads
        - input_cache_writes
      title: Pricing
      description: >-
        All pricing values are in USD per 1 token.


        Pricing fields are in string format to avoid floating point precision
        issues.
    Datacenter:
      properties:
        country_code:
          type: string
          title: Country Code
      type: object
      required:
        - country_code
      title: Datacenter

````