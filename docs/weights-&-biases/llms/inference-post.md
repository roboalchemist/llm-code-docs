# Source: https://docs.wandb.ai/weave/reference/service-api/inference/inference-post.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Inference Post

> OpenAI-compatible APIs.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /inference/v1{path}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /inference/v1{path}:
    post:
      tags:
        - Inference
      summary: Inference Post
      description: OpenAI-compatible APIs.
      operationId: inference_post_inference_v1_path__post
      parameters:
        - name: path
          in: path
          required: true
          schema:
            type: string
            title: Path
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CompletionsCreateRequestInputs'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBearer: []
components:
  schemas:
    CompletionsCreateRequestInputs:
      properties:
        model:
          type: string
          title: Model
        messages:
          items: {}
          type: array
          title: Messages
          default: []
        timeout:
          anyOf:
            - type: number
            - type: string
            - type: 'null'
          title: Timeout
        temperature:
          anyOf:
            - type: number
            - type: 'null'
          title: Temperature
        top_p:
          anyOf:
            - type: number
            - type: 'null'
          title: Top P
        'n':
          anyOf:
            - type: integer
            - type: 'null'
          title: 'N'
        stop:
          anyOf:
            - type: string
            - items: {}
              type: array
            - type: 'null'
          title: Stop
        max_completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Completion Tokens
        max_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Tokens
        modalities:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Modalities
        presence_penalty:
          anyOf:
            - type: number
            - type: 'null'
          title: Presence Penalty
        frequency_penalty:
          anyOf:
            - type: number
            - type: 'null'
          title: Frequency Penalty
        stream:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Stream
        logit_bias:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Logit Bias
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
        response_format:
          anyOf:
            - additionalProperties: true
              type: object
            - {}
            - type: 'null'
          title: Response Format
        seed:
          anyOf:
            - type: integer
            - type: 'null'
          title: Seed
        tools:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Tools
        tool_choice:
          anyOf:
            - type: string
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Tool Choice
        logprobs:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Logprobs
        top_logprobs:
          anyOf:
            - type: integer
            - type: 'null'
          title: Top Logprobs
        parallel_tool_calls:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Parallel Tool Calls
        extra_headers:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Extra Headers
        functions:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Functions
        function_call:
          anyOf:
            - type: string
            - type: 'null'
          title: Function Call
        api_version:
          anyOf:
            - type: string
            - type: 'null'
          title: Api Version
        prompt:
          anyOf:
            - type: string
            - type: 'null'
          title: Prompt
          description: >-
            Reference to a Weave Prompt object (e.g.,
            'weave:///entity/project/object/prompt_name:version'). If provided,
            the messages from this prompt will be prepended to the messages in
            this request. Template variables in the prompt messages can be
            substituted using the template_vars parameter.
        template_vars:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Template Vars
          description: >-
            Dictionary of template variables to substitute in prompt messages.
            Variables in messages like '{variable_name}' will be replaced with
            the corresponding values. Applied to both prompt messages (if prompt
            is provided) and regular messages.
      type: object
      required:
        - model
      title: CompletionsCreateRequestInputs
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    HTTPBearer:
      type: http
      scheme: bearer

````