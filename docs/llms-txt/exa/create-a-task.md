# Source: https://docs.exa.ai/reference/research/create-a-task.md

# Create a task

> Create an asynchronous research task that explores the web, gathers sources, synthesizes findings, and returns results with citations. Can be used to generate:
1. Structured JSON matching an `outputSchema` you provide.
2. A detailed markdown report when no schema is provided.

The API responds immediately with a `researchId` for polling completion status. For more details, see [Exa Research](/reference/exa-research).

Alternatively, you can use the OpenAI compatible [chat completions interface](/reference/chat-completions#research).


## OpenAPI

````yaml post /research/v1
paths:
  path: /research/v1
  method: post
  servers:
    - url: https://api.exa.ai/research/v1/
      description: Production
  request:
    security: []
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
              model:
                allOf:
                  - default: exa-research
                    type:
                      - string
                    enum:
                      - exa-research-fast
                      - exa-research
                      - exa-research-pro
                    description: >-
                      Research model to use. exa-research is faster and cheaper,
                      while exa-research-pro provides more thorough analysis and
                      stronger reasoning.
              instructions:
                allOf:
                  - type:
                      - string
                    maxLength: 4096
                    description: >-
                      Instructions for what you would like research on. A good
                      prompt clearly defines what information you want to find,
                      how research should be conducted, and what the output
                      should look like.
              outputSchema:
                allOf:
                  - type:
                      - object
                    additionalProperties: {}
                    description: >-
                      JSON Schema to enforce structured output. When provided,
                      the research output will be validated against this schema
                      and returned as parsed JSON.
            required: true
            refIdentifier: '#/components/schemas/ResearchCreateRequestDtoClass'
            examples:
              - model: exa-research
                instructions: What species of ant are similar to honeypot ants?
            requiredProperties:
              - instructions
            example:
              model: exa-research
              instructions: What species of ant are similar to honeypot ants?
        examples:
          example:
            value:
              model: exa-research
              instructions: What species of ant are similar to honeypot ants?
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              researchId:
                allOf:
                  - type:
                      - string
                    description: >-
                      Unique identifier for tracking and retrieving this
                      research request
              createdAt:
                allOf:
                  - type:
                      - number
                    description: >-
                      When the research was created (Unix timestamp in
                      milliseconds)
              model:
                allOf:
                  - default: exa-research
                    type:
                      - string
                    enum:
                      - exa-research-fast
                      - exa-research
                      - exa-research-pro
                    description: The model used for this research request
              instructions:
                allOf:
                  - type:
                      - string
                    description: The original research instructions provided
              outputSchema:
                allOf:
                  - type:
                      - object
                    additionalProperties: {}
                    description: The JSON Schema used to validate the output, if provided
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - pending
            title: Pending
            refIdentifier: '#/components/schemas/ResearchDtoClass'
            examples: &ref_1
              - &ref_0
                researchId: 01jszdfs0052sg4jc552sg4jc5
                model: exa-research
                instructions: What species of ant are similar to honeypot ants?
                status: running
              - researchId: 01jszdfs0052sg4jc552sg4jc5
                model: exa-research
                instructions: What species of ant are similar to honeypot ants?
                status: completed
                output: Melophorus bagoti
            requiredProperties:
              - researchId
              - createdAt
              - instructions
              - status
            example: *ref_0
          - type: object
            properties:
              researchId:
                allOf:
                  - type:
                      - string
                    description: >-
                      Unique identifier for tracking and retrieving this
                      research request
              createdAt:
                allOf:
                  - type:
                      - number
                    description: >-
                      When the research was created (Unix timestamp in
                      milliseconds)
              model:
                allOf:
                  - default: exa-research
                    type:
                      - string
                    enum:
                      - exa-research-fast
                      - exa-research
                      - exa-research-pro
                    description: The model used for this research request
              instructions:
                allOf:
                  - type:
                      - string
                    description: The original research instructions provided
              outputSchema:
                allOf:
                  - type:
                      - object
                    additionalProperties: {}
                    description: The JSON Schema used to validate the output, if provided
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - running
              events:
                allOf:
                  - type:
                      - array
                    items:
                      $ref: '#/components/schemas/ResearchEventDtoClass'
                    description: >-
                      Real-time log of operations as research progresses. Poll
                      this endpoint or use ?stream=true for live updates.
            title: Running
            refIdentifier: '#/components/schemas/ResearchDtoClass'
            examples: *ref_1
            requiredProperties:
              - researchId
              - createdAt
              - instructions
              - status
            example: *ref_0
          - type: object
            properties:
              researchId:
                allOf:
                  - type:
                      - string
                    description: >-
                      Unique identifier for tracking and retrieving this
                      research request
              createdAt:
                allOf:
                  - type:
                      - number
                    description: >-
                      When the research was created (Unix timestamp in
                      milliseconds)
              model:
                allOf:
                  - default: exa-research
                    type:
                      - string
                    enum:
                      - exa-research-fast
                      - exa-research
                      - exa-research-pro
                    description: The model used for this research request
              instructions:
                allOf:
                  - type:
                      - string
                    description: The original research instructions provided
              outputSchema:
                allOf:
                  - type:
                      - object
                    additionalProperties: {}
                    description: The JSON Schema used to validate the output, if provided
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - completed
              events:
                allOf:
                  - type:
                      - array
                    items:
                      $ref: '#/components/schemas/ResearchEventDtoClass'
                    description: >-
                      Detailed log of all operations performed during research.
                      Use ?events=true to include this field for debugging or
                      monitoring progress.
              output:
                allOf:
                  - type:
                      - object
                    properties:
                      content:
                        type:
                          - string
                        description: >-
                          The complete research output as text. If outputSchema
                          was provided, this is a JSON string.
                      parsed:
                        type:
                          - object
                        additionalProperties: {}
                        description: >-
                          Structured JSON object matching your outputSchema.
                          Only present when outputSchema was provided and the
                          output successfully validated.
                    required:
                      - content
                    description: >-
                      The final research results, containing both raw text and
                      parsed JSON if outputSchema was provided
              costDollars:
                allOf:
                  - type:
                      - object
                    properties:
                      total:
                        type:
                          - number
                        description: Total cost in USD for this research request
                      numSearches:
                        type:
                          - number
                        description: >-
                          Count of web searches performed. Each search query
                          counts as one search.
                      numPages:
                        type:
                          - number
                        description: >-
                          Count of web pages fully crawled and processed. Only
                          pages that were read in detail are counted.
                      reasoningTokens:
                        type:
                          - number
                        description: >-
                          Total AI tokens used for reasoning, planning, and
                          generating the final output
                    required:
                      - total
                      - numSearches
                      - numPages
                      - reasoningTokens
                    description: Detailed cost breakdown for billing purposes
              finishedAt:
                allOf:
                  - type:
                      - number
                    description: >-
                      When the research completed (Unix timestamp in
                      milliseconds)
            title: Completed
            refIdentifier: '#/components/schemas/ResearchDtoClass'
            examples: *ref_1
            requiredProperties:
              - researchId
              - createdAt
              - instructions
              - status
              - output
              - costDollars
              - finishedAt
            example: *ref_0
          - type: object
            properties:
              researchId:
                allOf:
                  - type:
                      - string
                    description: >-
                      Unique identifier for tracking and retrieving this
                      research request
              createdAt:
                allOf:
                  - type:
                      - number
                    description: >-
                      When the research was created (Unix timestamp in
                      milliseconds)
              model:
                allOf:
                  - default: exa-research
                    type:
                      - string
                    enum:
                      - exa-research-fast
                      - exa-research
                      - exa-research-pro
                    description: The model used for this research request
              instructions:
                allOf:
                  - type:
                      - string
                    description: The original research instructions provided
              outputSchema:
                allOf:
                  - type:
                      - object
                    additionalProperties: {}
                    description: The JSON Schema used to validate the output, if provided
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - canceled
              events:
                allOf:
                  - type:
                      - array
                    items:
                      $ref: '#/components/schemas/ResearchEventDtoClass'
                    description: >-
                      Detailed log of all operations performed during research.
                      Use ?events=true to include this field for debugging or
                      monitoring progress.
              finishedAt:
                allOf:
                  - type:
                      - number
                    description: >-
                      When the research was canceled (Unix timestamp in
                      milliseconds)
            title: Canceled
            refIdentifier: '#/components/schemas/ResearchDtoClass'
            examples: *ref_1
            requiredProperties:
              - researchId
              - createdAt
              - instructions
              - status
              - finishedAt
            example: *ref_0
          - type: object
            properties:
              researchId:
                allOf:
                  - type:
                      - string
                    description: >-
                      Unique identifier for tracking and retrieving this
                      research request
              createdAt:
                allOf:
                  - type:
                      - number
                    description: >-
                      When the research was created (Unix timestamp in
                      milliseconds)
              model:
                allOf:
                  - default: exa-research
                    type:
                      - string
                    enum:
                      - exa-research-fast
                      - exa-research
                      - exa-research-pro
                    description: The model used for this research request
              instructions:
                allOf:
                  - type:
                      - string
                    description: The original research instructions provided
              outputSchema:
                allOf:
                  - type:
                      - object
                    additionalProperties: {}
                    description: The JSON Schema used to validate the output, if provided
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - failed
              events:
                allOf:
                  - type:
                      - array
                    items:
                      $ref: '#/components/schemas/ResearchEventDtoClass'
                    description: >-
                      Detailed log of all operations performed during research.
                      Use ?events=true to include this field for debugging or
                      monitoring progress.
              error:
                allOf:
                  - type:
                      - string
                    description: Human-readable error message explaining what went wrong.
              finishedAt:
                allOf:
                  - type:
                      - number
                    description: When the research failed (Unix timestamp in milliseconds)
            title: Failed
            refIdentifier: '#/components/schemas/ResearchDtoClass'
            examples: *ref_1
            requiredProperties:
              - researchId
              - createdAt
              - instructions
              - status
              - error
              - finishedAt
            example: *ref_0
        examples:
          example:
            value:
              researchId: 01jszdfs0052sg4jc552sg4jc5
              model: exa-research
              instructions: What species of ant are similar to honeypot ants?
              status: running
        description: Research request created
  deprecated: false
  type: path
components:
  schemas:
    ResearchEventDtoClass:
      oneOf:
        - discriminator:
            propertyName: eventType
          oneOf:
            - type:
                - object
              properties:
                eventType:
                  type:
                    - string
                  enum:
                    - research-definition
                instructions:
                  type:
                    - string
                  description: The complete research instructions as provided
                outputSchema:
                  type:
                    - object
                  additionalProperties: {}
                  description: The JSON Schema that will validate the final output
                createdAt:
                  type:
                    - number
                  description: When this event occurred (Unix timestamp in milliseconds)
                researchId:
                  type:
                    - string
                  description: The research request this event belongs to
              required:
                - eventType
                - instructions
                - createdAt
                - researchId
              title: Research Definition
            - type:
                - object
              properties:
                eventType:
                  type:
                    - string
                  enum:
                    - research-output
                output:
                  discriminator:
                    propertyName: outputType
                  oneOf:
                    - type:
                        - object
                      properties:
                        outputType:
                          type:
                            - string
                          enum:
                            - completed
                        costDollars:
                          type:
                            - object
                          properties:
                            total:
                              type:
                                - number
                              description: Total cost in USD for this research request
                            numSearches:
                              type:
                                - number
                              description: >-
                                Count of web searches performed. Each search
                                query counts as one search.
                            numPages:
                              type:
                                - number
                              description: >-
                                Count of web pages fully crawled and processed.
                                Only pages that were read in detail are counted.
                            reasoningTokens:
                              type:
                                - number
                              description: >-
                                Total AI tokens used for reasoning, planning,
                                and generating the final output
                          required:
                            - total
                            - numSearches
                            - numPages
                            - reasoningTokens
                        content:
                          type:
                            - string
                          description: >-
                            The complete research output as text. If
                            outputSchema was provided, this is a JSON string.
                        parsed:
                          type:
                            - object
                          additionalProperties: {}
                          description: >-
                            Structured JSON object matching your outputSchema.
                            Only present when outputSchema was provided and the
                            output successfully validated.
                      required:
                        - outputType
                        - costDollars
                        - content
                      title: Completed
                    - type:
                        - object
                      properties:
                        outputType:
                          type:
                            - string
                          enum:
                            - failed
                        error:
                          type:
                            - string
                          description: >-
                            Detailed error message explaining why the research
                            failed
                      required:
                        - outputType
                        - error
                      title: Failed
                  description: >-
                    The final research result, either successful with data or
                    failed with error
                createdAt:
                  type:
                    - number
                  description: When this event occurred (Unix timestamp in milliseconds)
                researchId:
                  type:
                    - string
                  description: The research request this event belongs to
              required:
                - eventType
                - output
                - createdAt
                - researchId
              title: Research Output
        - discriminator:
            propertyName: eventType
          oneOf:
            - type:
                - object
              properties:
                eventType:
                  type:
                    - string
                  enum:
                    - plan-definition
                planId:
                  type:
                    - string
                  description: Identifier for this planning cycle
                createdAt:
                  type:
                    - number
                  description: When this event occurred (Unix timestamp in milliseconds)
                researchId:
                  type:
                    - string
                  description: The research request this event belongs to
              required:
                - eventType
                - planId
                - createdAt
                - researchId
              title: Plan Definition
            - type:
                - object
              properties:
                eventType:
                  type:
                    - string
                  enum:
                    - plan-operation
                planId:
                  type:
                    - string
                  description: Which plan this operation belongs to
                operationId:
                  type:
                    - string
                  description: Unique identifier for this specific operation
                data:
                  discriminator:
                    propertyName: type
                  oneOf:
                    - type:
                        - object
                      properties:
                        type:
                          type:
                            - string
                          enum:
                            - think
                        content:
                          type:
                            - string
                          description: The AI's reasoning process and decision-making steps
                      required:
                        - type
                        - content
                      title: Think
                    - type:
                        - object
                      properties:
                        type:
                          type:
                            - string
                          enum:
                            - search
                        searchType:
                          type:
                            - string
                          enum:
                            - neural
                            - auto
                            - fast
                          description: >-
                            Search algorithm used (neural for semantic search,
                            auto for intelligent search method selection)
                        goal:
                          type:
                            - string
                          description: What the AI is trying to find with this search
                        query:
                          type:
                            - string
                          description: The exact search query sent to the search engine
                        results:
                          type:
                            - array
                          items:
                            type:
                              - object
                            properties:
                              url:
                                type:
                                  - string
                            required:
                              - url
                          description: URLs returned by the search, ranked by relevance
                        pageTokens:
                          type:
                            - number
                          description: Token cost for processing search result snippets
                      required:
                        - type
                        - searchType
                        - query
                        - results
                        - pageTokens
                      title: Search
                    - type:
                        - object
                      properties:
                        type:
                          type:
                            - string
                          enum:
                            - crawl
                        goal:
                          type:
                            - string
                          description: What information the AI expects to find on this page
                        result:
                          type:
                            - object
                          properties:
                            url:
                              type:
                                - string
                          required:
                            - url
                          description: The specific page that was crawled
                        pageTokens:
                          type:
                            - number
                          description: Token cost for processing the full page content
                      required:
                        - type
                        - result
                        - pageTokens
                      title: Crawl
                  description: The actual operation performed (think, search, or crawl)
                createdAt:
                  type:
                    - number
                  description: When this event occurred (Unix timestamp in milliseconds)
                researchId:
                  type:
                    - string
                  description: The research request this event belongs to
              required:
                - eventType
                - planId
                - operationId
                - data
                - createdAt
                - researchId
              title: Plan Operation
            - type:
                - object
              properties:
                eventType:
                  type:
                    - string
                  enum:
                    - plan-output
                planId:
                  type:
                    - string
                  description: Which plan is producing this output
                output:
                  discriminator:
                    propertyName: outputType
                  oneOf:
                    - type:
                        - object
                      properties:
                        outputType:
                          type:
                            - string
                          enum:
                            - tasks
                        reasoning:
                          type:
                            - string
                          description: Why these specific tasks were chosen
                        tasksInstructions:
                          type:
                            - array
                          items:
                            type:
                              - string
                          description: >-
                            List of task instructions that will be executed in
                            parallel
                      required:
                        - outputType
                        - reasoning
                        - tasksInstructions
                      title: Tasks
                    - type:
                        - object
                      properties:
                        outputType:
                          type:
                            - string
                          enum:
                            - stop
                        reasoning:
                          type:
                            - string
                          description: Why the AI decided to stop researching
                      required:
                        - outputType
                        - reasoning
                      title: Stop
                  description: >-
                    The plan's decision: either generate tasks or stop
                    researching
                createdAt:
                  type:
                    - number
                  description: When this event occurred (Unix timestamp in milliseconds)
                researchId:
                  type:
                    - string
                  description: The research request this event belongs to
              required:
                - eventType
                - planId
                - output
                - createdAt
                - researchId
              title: Plan Output
        - discriminator:
            propertyName: eventType
          oneOf:
            - type:
                - object
              properties:
                eventType:
                  type:
                    - string
                  enum:
                    - task-definition
                planId:
                  type:
                    - string
                  description: The plan that generated this task
                taskId:
                  type:
                    - string
                  description: Identifier for tracking this specific task
                instructions:
                  type:
                    - string
                  description: What this task should accomplish
                createdAt:
                  type:
                    - number
                  description: When this event occurred (Unix timestamp in milliseconds)
                researchId:
                  type:
                    - string
                  description: The research request this event belongs to
              required:
                - eventType
                - planId
                - taskId
                - instructions
                - createdAt
                - researchId
              title: Task Definition
            - type:
                - object
              properties:
                eventType:
                  type:
                    - string
                  enum:
                    - task-operation
                planId:
                  type:
                    - string
                  description: The plan that owns this task
                taskId:
                  type:
                    - string
                  description: Which task is performing this operation
                operationId:
                  type:
                    - string
                  description: Unique identifier for this specific operation
                data:
                  discriminator:
                    propertyName: type
                  oneOf:
                    - type:
                        - object
                      properties:
                        type:
                          type:
                            - string
                          enum:
                            - think
                        content:
                          type:
                            - string
                          description: The AI's reasoning process and decision-making steps
                      required:
                        - type
                        - content
                      title: Think
                    - type:
                        - object
                      properties:
                        type:
                          type:
                            - string
                          enum:
                            - search
                        searchType:
                          type:
                            - string
                          enum:
                            - neural
                            - auto
                            - fast
                          description: >-
                            Search algorithm used (neural for semantic search,
                            auto for intelligent search method selection)
                        goal:
                          type:
                            - string
                          description: What the AI is trying to find with this search
                        query:
                          type:
                            - string
                          description: The exact search query sent to the search engine
                        results:
                          type:
                            - array
                          items:
                            type:
                              - object
                            properties:
                              url:
                                type:
                                  - string
                            required:
                              - url
                          description: URLs returned by the search, ranked by relevance
                        pageTokens:
                          type:
                            - number
                          description: Token cost for processing search result snippets
                      required:
                        - type
                        - searchType
                        - query
                        - results
                        - pageTokens
                      title: Search
                    - type:
                        - object
                      properties:
                        type:
                          type:
                            - string
                          enum:
                            - crawl
                        goal:
                          type:
                            - string
                          description: What information the AI expects to find on this page
                        result:
                          type:
                            - object
                          properties:
                            url:
                              type:
                                - string
                          required:
                            - url
                          description: The specific page that was crawled
                        pageTokens:
                          type:
                            - number
                          description: Token cost for processing the full page content
                      required:
                        - type
                        - result
                        - pageTokens
                      title: Crawl
                  description: The actual operation performed within this task
                createdAt:
                  type:
                    - number
                  description: When this event occurred (Unix timestamp in milliseconds)
                researchId:
                  type:
                    - string
                  description: The research request this event belongs to
              required:
                - eventType
                - planId
                - taskId
                - operationId
                - data
                - createdAt
                - researchId
              title: Task Operation
            - type:
                - object
              properties:
                eventType:
                  type:
                    - string
                  enum:
                    - task-output
                planId:
                  type:
                    - string
                  description: The plan that owns this task
                taskId:
                  type:
                    - string
                  description: Which task produced this output
                output:
                  type:
                    - object
                  properties:
                    outputType:
                      type:
                        - string
                      enum:
                        - completed
                    content:
                      type:
                        - string
                      description: The information gathered by this task
                  required:
                    - outputType
                    - content
                  description: The successful completion result of this task
                createdAt:
                  type:
                    - number
                  description: When this event occurred (Unix timestamp in milliseconds)
                researchId:
                  type:
                    - string
                  description: The research request this event belongs to
              required:
                - eventType
                - planId
                - taskId
                - output
                - createdAt
                - researchId
              title: Task Output

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt