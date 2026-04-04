# Source: https://docs.helicone.ai/rest/ai-gateway/post-v1-chat-completions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat Completions (Gateway)

> Create chat completions via the AI Gateway

This request schema applies when using the Helicone AI Gateway with pass‑through billing (credits). In BYOK mode, the standard OpenAI Chat Completions schema is allowed. The schema is defined based on fields that are stable across all provider-model mappings.

[Learn more about pass‑through billing vs BYOK](/gateway/provider-routing).

<RequestExample>
  ```bash cURL theme={null}
  curl https://ai-gateway.helicone.ai/v1/chat/completions \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "gpt-4o-mini",
      "messages": [
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "user", "content": "Say hello in one sentence." }
      ]
    }'
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from "openai";

  const client = new OpenAI({
    baseURL: "https://ai-gateway.helicone.ai/v1",
    apiKey: process.env.HELICONE_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "Say hello in one sentence." },
    ],
  });
  ```

  ```python Python theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://ai-gateway.helicone.ai/v1",
      api_key=os.environ.get("HELICONE_API_KEY"),
  )

  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Say hello in one sentence."},
      ],
  )
  ```
</RequestExample>


## OpenAPI

````yaml post /v1/chat/completions
openapi: 3.0.0
info:
  title: Helicone AI Gateway API
  version: 1.0.0
  description: OpenAPI spec derived from Zod schemas for AI Gateway.
servers:
  - url: https://ai-gateway.helicone.ai
security: []
paths:
  /v1/chat/completions:
    post:
      summary: Create Chat Completion
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                metadata:
                  anyOf:
                    - type: object
                      additionalProperties: {}
                    - type: string
                      nullable: true
                      enum:
                        - null
                top_logprobs:
                  nullable: true
                  type: integer
                  minimum: 0
                  maximum: 20
                temperature:
                  anyOf:
                    - type: number
                    - type: string
                      nullable: true
                      enum:
                        - null
                top_p:
                  anyOf:
                    - type: number
                    - type: string
                      nullable: true
                      enum:
                        - null
                top_k:
                  anyOf:
                    - type: number
                    - type: string
                      nullable: true
                      enum:
                        - null
                user:
                  type: string
                safety_identifier:
                  type: string
                prompt_cache_key:
                  type: string
                cache_control:
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - ephemeral
                    ttl:
                      type: string
                service_tier:
                  anyOf:
                    - type: string
                      enum:
                        - auto
                        - default
                        - flex
                        - scale
                        - priority
                    - type: string
                      nullable: true
                      enum:
                        - null
                messages:
                  minItems: 1
                  type: array
                  items:
                    anyOf:
                      - type: object
                        properties:
                          content:
                            anyOf:
                              - type: string
                              - type: array
                                items:
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - text
                                    text:
                                      type: string
                                  required:
                                    - type
                                    - text
                          role:
                            type: string
                            enum:
                              - developer
                          name:
                            type: string
                        required:
                          - content
                          - role
                      - type: object
                        properties:
                          content:
                            anyOf:
                              - type: string
                              - type: array
                                items:
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - text
                                    text:
                                      type: string
                                  required:
                                    - type
                                    - text
                          role:
                            type: string
                            enum:
                              - system
                          name:
                            type: string
                        required:
                          - content
                          - role
                      - type: object
                        properties:
                          content:
                            anyOf:
                              - type: string
                              - type: array
                                items:
                                  anyOf:
                                    - type: object
                                      properties:
                                        type:
                                          type: string
                                          enum:
                                            - text
                                        text:
                                          type: string
                                      required:
                                        - type
                                        - text
                                    - type: object
                                      properties:
                                        type:
                                          type: string
                                          enum:
                                            - image_url
                                        image_url:
                                          type: object
                                          properties:
                                            url:
                                              type: string
                                              format: uri
                                            detail:
                                              default: auto
                                              type: string
                                              enum:
                                                - auto
                                                - low
                                                - high
                                          required:
                                            - url
                                      required:
                                        - type
                                        - image_url
                                    - type: object
                                      properties:
                                        type:
                                          type: string
                                          enum:
                                            - document
                                        source:
                                          type: object
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - text
                                            media_type:
                                              type: string
                                            data:
                                              type: string
                                          required:
                                            - type
                                            - media_type
                                            - data
                                        title:
                                          type: string
                                        citations:
                                          type: object
                                          properties:
                                            enabled:
                                              type: boolean
                                          required:
                                            - enabled
                                      required:
                                        - type
                                        - source
                          role:
                            type: string
                            enum:
                              - user
                          name:
                            type: string
                        required:
                          - content
                          - role
                      - type: object
                        properties:
                          content:
                            anyOf:
                              - anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      anyOf:
                                        - type: object
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - text
                                            text:
                                              type: string
                                          required:
                                            - type
                                            - text
                                        - type: object
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - refusal
                                            refusal:
                                              type: string
                                          required:
                                            - type
                                            - refusal
                              - type: string
                                nullable: true
                                enum:
                                  - null
                          refusal:
                            anyOf:
                              - type: string
                              - type: string
                                nullable: true
                                enum:
                                  - null
                          role:
                            type: string
                            enum:
                              - assistant
                          name:
                            type: string
                          audio:
                            anyOf:
                              - type: object
                                properties:
                                  id:
                                    type: string
                                required:
                                  - id
                              - type: string
                                nullable: true
                                enum:
                                  - null
                          tool_calls:
                            type: array
                            items:
                              anyOf:
                                - type: object
                                  properties:
                                    id:
                                      type: string
                                    type:
                                      type: string
                                      enum:
                                        - function
                                    function:
                                      type: object
                                      properties:
                                        name:
                                          type: string
                                        arguments:
                                          type: string
                                      required:
                                        - name
                                        - arguments
                                  required:
                                    - id
                                    - type
                                    - function
                                - type: object
                                  properties:
                                    id:
                                      type: string
                                    type:
                                      type: string
                                      enum:
                                        - custom
                                    custom:
                                      type: object
                                      properties:
                                        name:
                                          type: string
                                        input:
                                          type: string
                                      required:
                                        - name
                                        - input
                                  required:
                                    - id
                                    - type
                                    - custom
                          function_call:
                            anyOf:
                              - type: object
                                properties:
                                  arguments:
                                    type: string
                                  name:
                                    type: string
                                required:
                                  - arguments
                                  - name
                              - type: string
                                nullable: true
                                enum:
                                  - null
                        required:
                          - role
                      - type: object
                        properties:
                          role:
                            type: string
                            enum:
                              - tool
                          content:
                            anyOf:
                              - type: string
                              - type: array
                                items:
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - text
                                    text:
                                      type: string
                                  required:
                                    - type
                                    - text
                          tool_call_id:
                            type: string
                        required:
                          - role
                          - content
                          - tool_call_id
                      - type: object
                        properties:
                          role:
                            type: string
                            enum:
                              - function
                          content:
                            anyOf:
                              - type: string
                              - type: string
                                nullable: true
                                enum:
                                  - null
                          name:
                            type: string
                        required:
                          - role
                          - content
                          - name
                model:
                  type: string
                modalities:
                  anyOf:
                    - type: array
                      items:
                        type: string
                        enum:
                          - text
                    - type: string
                      nullable: true
                      enum:
                        - null
                verbosity:
                  anyOf:
                    - type: string
                      enum:
                        - low
                        - medium
                        - high
                    - type: string
                      nullable: true
                      enum:
                        - null
                reasoning_effort:
                  anyOf:
                    - type: string
                      enum:
                        - minimal
                        - low
                        - medium
                        - high
                    - type: string
                      nullable: true
                      enum:
                        - null
                reasoning_options:
                  type: object
                  properties:
                    budget_tokens:
                      type: integer
                      minimum: -9007199254740991
                      maximum: 9007199254740991
                  required:
                    - budget_tokens
                max_completion_tokens:
                  nullable: true
                  type: integer
                  minimum: -9007199254740991
                  maximum: 9007199254740991
                frequency_penalty:
                  default: 0
                  nullable: true
                  type: number
                  minimum: -2
                  maximum: 2
                presence_penalty:
                  default: 0
                  nullable: true
                  type: number
                  minimum: -2
                  maximum: 2
                response_format:
                  anyOf:
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - text
                      required:
                        - type
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - json_schema
                        json_schema:
                          type: object
                          properties:
                            description:
                              type: string
                            name:
                              type: string
                            schema:
                              type: object
                              properties: {}
                            strict:
                              anyOf:
                                - type: boolean
                                - type: string
                                  nullable: true
                                  enum:
                                    - null
                          required:
                            - name
                      required:
                        - type
                        - json_schema
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - json_object
                      required:
                        - type
                store:
                  default: false
                  nullable: true
                  type: boolean
                stream:
                  default: false
                  nullable: true
                  type: boolean
                stop:
                  nullable: true
                  anyOf:
                    - type: string
                    - type: array
                      items:
                        type: string
                logit_bias:
                  default: null
                  nullable: true
                  type: object
                  additionalProperties:
                    type: integer
                    minimum: -9007199254740991
                    maximum: 9007199254740991
                logprobs:
                  default: false
                  nullable: true
                  type: boolean
                max_tokens:
                  nullable: true
                  type: integer
                  minimum: -9007199254740991
                  maximum: 9007199254740991
                'n':
                  default: 1
                  nullable: true
                  type: integer
                  minimum: 1
                  maximum: 128
                prediction:
                  nullable: true
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - content
                    content:
                      anyOf:
                        - type: string
                        - type: array
                          items:
                            type: object
                            properties:
                              type:
                                type: string
                                enum:
                                  - text
                              text:
                                type: string
                            required:
                              - type
                              - text
                    reasoning:
                      type: string
                  required:
                    - type
                    - content
                seed:
                  nullable: true
                  type: integer
                  minimum: -9007199254740991
                  maximum: 9007199254740991
                stream_options:
                  anyOf:
                    - type: object
                      properties:
                        include_usage:
                          type: boolean
                        include_obfuscation:
                          type: boolean
                    - type: string
                      nullable: true
                      enum:
                        - null
                tools:
                  type: array
                  items:
                    anyOf:
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - function
                          function:
                            type: object
                            properties:
                              description:
                                type: string
                              name:
                                type: string
                              parameters:
                                type: object
                                properties: {}
                              strict:
                                anyOf:
                                  - type: boolean
                                  - type: string
                                    nullable: true
                                    enum:
                                      - null
                            required:
                              - name
                        required:
                          - type
                          - function
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - custom
                          custom:
                            type: object
                            properties:
                              name:
                                type: string
                              description:
                                type: string
                              format:
                                anyOf:
                                  - type: object
                                    properties:
                                      type:
                                        type: string
                                        enum:
                                          - text
                                    required:
                                      - type
                                  - type: object
                                    properties:
                                      type:
                                        type: string
                                        enum:
                                          - grammar
                                      grammar:
                                        type: object
                                        properties:
                                          definition:
                                            type: string
                                          syntax:
                                            type: string
                                            enum:
                                              - lark
                                              - regex
                                        required:
                                          - definition
                                          - syntax
                                    required:
                                      - type
                                      - grammar
                            required:
                              - name
                        required:
                          - type
                          - custom
                tool_choice:
                  anyOf:
                    - type: string
                      enum:
                        - none
                        - auto
                        - required
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - allowed_tools
                        allowed_tools:
                          type: object
                          properties:
                            mode:
                              type: string
                              enum:
                                - auto
                                - required
                            tools:
                              type: array
                              items:
                                type: object
                                properties: {}
                          required:
                            - mode
                            - tools
                      required:
                        - type
                        - allowed_tools
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - function
                        function:
                          type: object
                          properties:
                            name:
                              type: string
                          required:
                            - name
                      required:
                        - type
                        - function
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - custom
                        custom:
                          type: object
                          properties:
                            name:
                              type: string
                          required:
                            - name
                      required:
                        - type
                        - custom
                parallel_tool_calls:
                  default: true
                  type: boolean
                function_call:
                  anyOf:
                    - type: string
                      enum:
                        - none
                        - auto
                    - type: object
                      properties:
                        name:
                          type: string
                      required:
                        - name
                functions:
                  minItems: 1
                  maxItems: 128
                  type: array
                  items:
                    type: object
                    properties:
                      description:
                        type: string
                      name:
                        type: string
                      parameters:
                        type: object
                        properties: {}
                    required:
                      - name
                context_editing:
                  type: object
                  properties:
                    enabled:
                      type: boolean
                    clear_tool_uses:
                      type: object
                      properties:
                        trigger:
                          type: integer
                          minimum: -9007199254740991
                          maximum: 9007199254740991
                        keep:
                          type: integer
                          minimum: -9007199254740991
                          maximum: 9007199254740991
                        clear_at_least:
                          type: integer
                          minimum: -9007199254740991
                          maximum: 9007199254740991
                        exclude_tools:
                          type: array
                          items:
                            type: string
                        clear_tool_inputs:
                          type: boolean
                      additionalProperties: false
                    clear_thinking:
                      type: object
                      properties:
                        keep:
                          anyOf:
                            - type: integer
                              minimum: -9007199254740991
                              maximum: 9007199254740991
                            - type: string
                              enum:
                                - all
                      additionalProperties: false
                  required:
                    - enabled
                  additionalProperties: false
                image_generation:
                  type: object
                  properties:
                    aspect_ratio:
                      type: string
                    image_size:
                      type: string
                  required:
                    - aspect_ratio
                    - image_size
              required:
                - messages
                - model
              additionalProperties: false
      responses:
        '200':
          description: Request accepted

````