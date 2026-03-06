# Source: https://io.net/docs/reference/rag/retrieval/prompt-based-completion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt-Based Completion

> The R2R Completion endpoint generates text completions directly from a language model. It accepts structured messages, supports configurable generation parameters, and enables both streaming and non-streaming responses for flexible AI interaction.

The **Prompt-Based Completion** endpoint allows direct interaction with a language model by sending raw prompts or structured message sequences.

It provides a simple interface for generating completions, summaries, or other free-form outputs without performing any retrieval or grounding from the document corpus.

This endpoint is ideal for open-ended generation tasks such as text drafting, classification, rewriting, summarization, and chat-like conversations that do not require knowledge integration from R2R’s retrieval pipeline.

### Request Body

The request must include a `messages` list representing the conversational context and an optional `generation_config` object to control model behavior.


## OpenAPI

````yaml openapi/rag-retrieval/prompt-based-completion.json post /api/r2r/v3/retrieval/completion
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/retrieval/completion:
    post:
      summary: Prompt-based completion
      description: Sends a raw prompt for direct completion using a selected model.
      operationId: prompt-based-completion
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                messages:
                  type: object
                  description: The input prompt
                  required:
                    - role
                  properties:
                    role:
                      type: string
                      description: Or allowed string *
                      enum:
                        - system
                        - user
                        - assistant
                        - function
                        - tool
                    content:
                      type: string
                    name:
                      type: string
                    function_call:
                      type: array
                    tool_calls:
                      type: array
                    tool_call_id:
                      type: string
                    metadata:
                      type: array
                    structured_content:
                      type: array
                    image_url:
                      type: string
                    image_data:
                      type: array
                generation_config:
                  type: object
                  description: Model to use (e.g., gpt-4)
                  properties:
                    model:
                      type: string
                    temperature:
                      type: number
                      format: double
                    top_p:
                      type: number
                      format: double
                    max_tokens_to_sample:
                      type: integer
                      format: int32
                    stream:
                      type: boolean
                    functions:
                      type: array
                    tools:
                      type: array
                    add_generation_kwargs:
                      type: array
                    api_base:
                      type: string
                    response_format:
                      type: array
                      items:
                        properties:
                          Base Model:
                            type: object
                        type: object
                    extended_thinking:
                      type: boolean
                      description: >-
                        Flag to enable extended thinking mode (for Anthropic
                        providers)
                      default: false
                    thinking_budget:
                      type: integer
                      description: >-
                        Token budget for internal reasoning when extended
                        thinking mode is enabled. Must be less than
                        max_tokens_to_sample.
                      format: int32
                    reasoning_effort:
                      type: string
                      description: >-
                        Effort level for internal reasoning when extended
                        thinking mode is enabled, low, medium, or high.Only
                        applicable to OpenAI providers.
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
        '422':
          description: '422'
          content:
            text/plain:
              examples:
                Result:
                  value: ''
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````