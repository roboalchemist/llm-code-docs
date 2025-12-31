# Source: https://dev.writer.com/home/ai-detect.md

# Source: https://dev.writer.com/api-reference/tool-api/ai-detect.md

# Source: https://dev.writer.com/home/ai-detect.md

# Source: https://dev.writer.com/api-reference/tool-api/ai-detect.md

# Source: https://dev.writer.com/home/ai-detect.md

# Source: https://dev.writer.com/api-reference/tool-api/ai-detect.md

# Source: https://dev.writer.com/home/ai-detect.md

# Source: https://dev.writer.com/api-reference/tool-api/ai-detect.md

# AI detection

> Detects if content is AI- or human-generated, with a confidence score. Content must have at least 350 characters

## OpenAPI

````yaml post /v1/tools/ai-detect
paths:
  path: /v1/tools/ai-detect
  method: post
  servers:
    - url: https://api.writer.com
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
                Bearer authentication header of the form `Bearer <token>`, where
                `<token>` is your [Writer API
                key](https://dev.writer.com/api-reference/api-keys).
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
              input:
                allOf:
                  - type: string
                    description: >-
                      The content to determine if it is AI- or human-generated.
                      Content must have at least 350 characters.
                    example: >-
                      AI and ML continue to be at the forefront of technological
                      advancements. In 2025, we can expect more sophisticated AI
                      systems that can handle complex tasks with greater
                      efficiency. AI will play a crucial role in various
                      sectors, including healthcare, finance, and manufacturing.
                      For instance, AI-powered diagnostic tools will become more
                      accurate, helping doctors detect diseases at an early
                      stage. In finance, AI algorithms will enhance fraud
                      detection and risk management.
            title: ai_detection_request
            refIdentifier: '#/components/schemas/ai_detection_request'
            requiredProperties:
              - input
        examples:
          example:
            value:
              input: >-
                AI and ML continue to be at the forefront of technological
                advancements. In 2025, we can expect more sophisticated AI
                systems that can handle complex tasks with greater efficiency.
                AI will play a crucial role in various sectors, including
                healthcare, finance, and manufacturing. For instance, AI-powered
                diagnostic tools will become more accurate, helping doctors
                detect diseases at an early stage. In finance, AI algorithms
                will enhance fraud detection and risk management.
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST
          https://api.writer.com/v1/tools/ai-detect \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw '{"input":"AI and ML continue to be at the forefront of
          technological advancements. In 2025, we can expect more sophisticated
          AI systems that can handle complex tasks with greater efficiency. AI
          will play a crucial role in various sectors, including healthcare,
          finance, and manufacturing. For instance, AI-powered diagnostic tools
          will become more accurate, helping doctors detect diseases at an early
          stage. In finance, AI algorithms will enhance fraud detection and risk
          management."}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const response = await client.tools.aiDetect({
              input:
                'AI and ML continue to be at the forefront of technological advancements. In 2025, we can expect more sophisticated AI systems that can handle complex tasks with greater efficiency. AI will play a crucial role in various sectors, including healthcare, finance, and manufacturing. For instance, AI-powered diagnostic tools will become more accurate, helping doctors detect diseases at an early stage. In finance, AI algorithms will enhance fraud detection and risk management.',
            });

            console.log(response.label);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )
          response = client.tools.ai_detect(
              input="AI and ML continue to be at the forefront of technological advancements. In 2025, we can expect more sophisticated AI systems that can handle complex tasks with greater efficiency. AI will play a crucial role in various sectors, including healthcare, finance, and manufacturing. For instance, AI-powered diagnostic tools will become more accurate, helping doctors detect diseases at an early stage. In finance, AI algorithms will enhance fraud detection and risk management.",
          )
          print(response.label)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              label:
                allOf:
                  - type: string
                    enum:
                      - fake
                      - real
                    example: fake
              score:
                allOf:
                  - type: number
                    format: double
                    example: 0.6265060305595398
            title: ai_detection_response
            refIdentifier: '#/components/schemas/ai_detection_response'
            requiredProperties:
              - label
              - score
        examples:
          example:
            value:
              label: fake
              score: 0.6265060305595398
        description: Successful
  deprecated: false
  type: path
components:
  schemas: {}

````