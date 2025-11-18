# Source: https://docs.agent.ai/api-reference/use-ai/use-genai-llm.md

# Use GenAI (LLM)

> Invoke a language model (LLM) to generate text based on input instructions, enabling creative and dynamic text outputs.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/invoke_llm
paths:
  path: /action/invoke_llm
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              instructions:
                allOf:
                  - type: string
                    description: >-
                      Enter detailed instructions for the language model, such
                      as 'Write a summary of the document' or 'Create an
                      engaging email subject line.
                    example: What is an AI agent?
              llm_engine:
                allOf:
                  - type: string
                    enum:
                      - auto
                      - gpt-5
                      - gpt-5-mini
                      - gpt-5-nano
                      - gpt-4.1
                      - gpt4o
                      - gpt-4o-mini
                      - o1
                      - o1-mini
                      - o1-pro
                      - o3-mini
                      - gpt_4v
                      - claude_sonnet_4.1
                      - claude_opus_4.1
                      - claude_sonnet_4
                      - claude_opus_4
                      - claude_sonnet_35
                      - claude_sonnet_35_vision
                      - claude_opus
                      - perplexity
                      - gemini-2.5-pro-preview-05-06
                      - gemini-2.5-flash-image-preview
                      - gemini-2.0-flash-exp-image-generation
                      - gemini-2.5-pro-exp-03-25
                      - gemini-2.0-pro-exp-02-05
                      - gemini-2.0-flash-exp
                      - gemini-2.0-flash-thinking-exp-1219
                      - gemini_15_pro
                      - gemini_15_flash
                      - gemma-7b-it
                      - gemma2-9b-it
                      - llama-3.3-70b-versatile
                      - deepseek-r1-distill-llama-70b
                      - mixtral-8x7b-32768
                      - gpt45
                      - meta-llama/llama-4-scout-17b-16e-instruct
                      - meta-llama/llama-4-maverick-17b-128e-instruct
                    default: gpt4o
                    description: LLM model to use for text generation.
            required: true
            requiredProperties:
              - instructions
              - llm_engine
        examples:
          example:
            value:
              instructions: What is an AI agent?
              llm_engine: gpt4o
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response: >-
                An AI agent is a software entity that performs tasks
                autonomously using artificial intelligence techniques. It
                perceives its environment through sensors, processes the
                information, and takes actions to achieve specific goals. AI
                agents can range from simple programs that perform basic tasks
                to complex systems capable of learning and adapting to new
                situations. They are used in various applications, including
                virtual assistants, autonomous vehicles, recommendation systems,
                and more. AI agents can be classified based on their
                capabilities, such as reactive agents, which respond to stimuli
                without internal state, and cognitive agents, which have memory
                and reasoning abilities.
        description: Use GenAI (LLM)
  deprecated: false
  type: path
components:
  schemas: {}

````