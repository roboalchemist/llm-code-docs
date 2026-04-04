# Source: https://docs.together.ai/reference/completions-1.md

# Create Completion

> Query a language, code, or image model.



## OpenAPI

````yaml POST /completions
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
  /completions:
    post:
      tags:
        - Completion
      summary: Create completion
      description: Query a language, code, or image model.
      operationId: completions
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CompletionRequest'
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompletionResponse'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/CompletionStream'
        '400':
          description: BadRequest
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
        '404':
          description: NotFound
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '429':
          description: RateLimit
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '503':
          description: Overloaded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '504':
          description: Timeout
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
      deprecated: false
components:
  schemas:
    CompletionRequest:
      type: object
      required:
        - model
        - prompt
      properties:
        prompt:
          type: string
          description: A string providing context for the model to complete.
          example: <s>[INST] What is the capital of France? [/INST]
        model:
          type: string
          description: >
            The name of the model to query.<br> <br> [See all of Together AI's
            chat
            models](https://docs.together.ai/docs/serverless-models#chat-models)
          example: mistralai/Mixtral-8x7B-Instruct-v0.1
          anyOf:
            - type: string
              enum:
                - meta-llama/Llama-2-70b-hf
                - mistralai/Mistral-7B-v0.1
                - mistralai/Mixtral-8x7B-v0.1
                - Meta-Llama/Llama-Guard-7b
            - type: string
        max_tokens:
          type: integer
          description: The maximum number of tokens to generate.
        stop:
          type: array
          description: >-
            A list of string sequences that will truncate (stop) inference text
            output. For example, "</s>" will stop generation as soon as the
            model generates the given token.
          items:
            type: string
        temperature:
          type: number
          description: >-
            A decimal number from 0-1 that determines the degree of randomness
            in the response. A temperature less than 1 favors more correctness
            and is appropriate for question answering or summarization. A value
            closer to 1 introduces more randomness in the output.
          format: float
        top_p:
          type: number
          description: >-
            A percentage (also called the nucleus parameter) that's used to
            dynamically adjust the number of choices for each predicted token
            based on the cumulative probabilities. It specifies a probability
            threshold below which all less likely tokens are filtered out. This
            technique helps maintain diversity and generate more fluent and
            natural-sounding text.
          format: float
        top_k:
          type: integer
          description: >-
            An integer that's used to limit the number of choices for the next
            predicted word or token. It specifies the maximum number of tokens
            to consider at each step, based on their probability of occurrence.
            This technique helps to speed up the generation process and can
            improve the quality of the generated text by focusing on the most
            likely options.
          format: int32
        repetition_penalty:
          type: number
          description: >-
            A number that controls the diversity of generated text by reducing
            the likelihood of repeated sequences. Higher values decrease
            repetition.
          format: float
        stream:
          type: boolean
          description: >-
            If true, stream tokens as Server-Sent Events as the model generates
            them instead of waiting for the full model response. The stream
            terminates with `data: [DONE]`. If false, return a single JSON
            object containing the results.
        logprobs:
          type: integer
          minimum: 0
          maximum: 20
          description: >-
            An integer between 0 and 20 of the top k tokens to return log
            probabilities for at each generation step, instead of just the
            sampled token. Log probabilities help assess model confidence in
            token predictions.
        echo:
          type: boolean
          description: >-
            If true, the response will contain the prompt. Can be used with
            `logprobs` to return prompt logprobs.
        'n':
          type: integer
          description: The number of completions to generate for each prompt.
          minimum: 1
          maximum: 128
        safety_model:
          type: string
          description: >-
            The name of the moderation model used to validate tokens. Choose
            from the available moderation models found
            [here](https://docs.together.ai/docs/inference-models#moderation-models).
          example: safety_model_name
          anyOf:
            - type: string
              enum:
                - Meta-Llama/Llama-Guard-7b
            - type: string
        min_p:
          type: number
          description: >-
            A number between 0 and 1 that can be used as an alternative to top-p
            and top-k.
          format: float
        presence_penalty:
          type: number
          description: >-
            A number between -2.0 and 2.0 where a positive value increases the
            likelihood of a model talking about new topics.
          format: float
        frequency_penalty:
          type: number
          description: >-
            A number between -2.0 and 2.0 where a positive value decreases the
            likelihood of repeating tokens that have already been mentioned.
          format: float
        logit_bias:
          type: object
          additionalProperties:
            type: number
            format: float
          description: >-
            Adjusts the likelihood of specific tokens appearing in the generated
            output.
          example:
            '105': 21.4
            '1024': -10.5
        seed:
          type: integer
          description: Seed value for reproducibility.
          example: 42
    CompletionResponse:
      type: object
      properties:
        id:
          type: string
        choices:
          $ref: '#/components/schemas/CompletionChoicesData'
        prompt:
          $ref: '#/components/schemas/PromptPart'
        usage:
          $ref: '#/components/schemas/UsageData'
        created:
          type: integer
        model:
          type: string
        object:
          type: string
          enum:
            - text.completion
      required:
        - id
        - choices
        - usage
        - created
        - model
        - object
    CompletionStream:
      oneOf:
        - $ref: '#/components/schemas/CompletionEvent'
        - $ref: '#/components/schemas/StreamSentinel'
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
    CompletionChoicesData:
      type: array
      items:
        type: object
        properties:
          text:
            type: string
            example: >-
              The capital of France is Paris. It's located in the north-central
              part of the country and is one of the most populous and visited
              cities in the world, known for its iconic landmarks like the
              Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and more. Paris
              is also the capital of the Île-de-France region and is a major
              global center for art, fashion, gastronomy, and culture.
          seed:
            type: integer
          finish_reason:
            $ref: '#/components/schemas/FinishReason'
          logprobs:
            $ref: '#/components/schemas/LogprobsPart'
    PromptPart:
      type: array
      items:
        type: object
        properties:
          text:
            type: string
            example: <s>[INST] What is the capital of France? [/INST]
          logprobs:
            $ref: '#/components/schemas/LogprobsPart'
    UsageData:
      type: object
      properties:
        prompt_tokens:
          type: integer
        completion_tokens:
          type: integer
        total_tokens:
          type: integer
      required:
        - prompt_tokens
        - completion_tokens
        - total_tokens
      nullable: true
    CompletionEvent:
      type: object
      required:
        - data
      properties:
        data:
          $ref: '#/components/schemas/CompletionChunk'
    StreamSentinel:
      type: object
      required:
        - data
      properties:
        data:
          title: stream_signal
          type: string
          enum:
            - '[DONE]'
    FinishReason:
      type: string
      enum:
        - stop
        - eos
        - length
        - tool_calls
        - function_call
    LogprobsPart:
      type: object
      properties:
        token_ids:
          type: array
          items:
            type: number
          description: List of token IDs corresponding to the logprobs
        tokens:
          type: array
          items:
            type: string
          description: List of token strings
        token_logprobs:
          type: array
          items:
            type: number
          description: List of token log probabilities
    CompletionChunk:
      type: object
      required:
        - id
        - token
        - choices
        - usage
        - finish_reason
      properties:
        id:
          type: string
        token:
          $ref: '#/components/schemas/CompletionToken'
        created:
          type: integer
        object:
          type: string
          enum:
            - completion.chunk
        choices:
          title: CompletionChoices
          type: array
          items:
            $ref: '#/components/schemas/CompletionChoice'
        usage:
          allOf:
            - $ref: '#/components/schemas/UsageData'
            - nullable: true
        seed:
          type: integer
        finish_reason:
          allOf:
            - $ref: '#/components/schemas/FinishReason'
            - nullable: true
    CompletionToken:
      type: object
      required:
        - id
        - text
        - logprob
        - special
      properties:
        id:
          type: integer
        text:
          type: string
        logprob:
          type: number
        special:
          type: boolean
    CompletionChoice:
      type: object
      required:
        - index
      properties:
        text:
          type: string
        index:
          type: integer
        delta:
          title: CompletionChoiceDelta
          type: object
          required:
            - role
          properties:
            token_id:
              type: integer
            role:
              type: string
              enum:
                - system
                - user
                - assistant
                - function
                - tool
            content:
              type: string
              nullable: true
            reasoning:
              type: string
              nullable: true
            tool_calls:
              type: array
              items:
                $ref: '#/components/schemas/ToolChoice'
            function_call:
              type: object
              deprecated: true
              nullable: true
              properties:
                arguments:
                  type: string
                name:
                  type: string
              required:
                - arguments
                - name
    ToolChoice:
      type: object
      required:
        - id
        - type
        - function
        - index
      properties:
        index:
          type: number
        id:
          type: string
        type:
          type: string
          enum:
            - function
        function:
          type: object
          required:
            - name
            - arguments
          properties:
            name:
              type: string
              example: function_name
            arguments:
              type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt