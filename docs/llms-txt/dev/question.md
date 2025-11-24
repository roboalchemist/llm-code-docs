# Source: https://dev.writer.com/api-reference/kg-api/question.md

# Question

> Ask a question to specified Knowledge Graphs.

## OpenAPI

````yaml post /v1/graphs/question
paths:
  path: /v1/graphs/question
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
              graph_ids:
                allOf:
                  - type: array
                    items:
                      type: string
                      format: uuid
                    minItems: 1
                    description: The unique identifiers of the Knowledge Graphs to query.
              subqueries:
                allOf:
                  - type: boolean
                    description: Specify whether to include subqueries.
                    default: false
              question:
                allOf:
                  - type: string
                    description: The question to answer using the Knowledge Graph.
              stream:
                allOf:
                  - type: boolean
                    description: >-
                      Determines whether the model's output should be streamed.
                      If true, the output is generated and sent incrementally,
                      which can be useful for real-time applications.
                    default: false
              query_config:
                allOf:
                  - $ref: '#/components/schemas/graph_query_config'
                    description: >-
                      Configuration options for Knowledge Graph queries,
                      including search parameters and citation settings.
            required: true
            title: question_request
            refIdentifier: '#/components/schemas/question_request'
            requiredProperties:
              - graph_ids
              - question
        examples:
          example:
            value:
              graph_ids:
                - 3c90c3cc-0d44-4b50-8888-8dd25736052a
              subqueries: false
              question: <string>
              stream: false
              query_config:
                max_subquestions: 6
                search_weight: 50
                grounding_level: 0
                max_snippets: 30
                max_tokens: 4000
                keyword_threshold: 0.7
                semantic_threshold: 0.7
                inline_citations: false
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST
          https://api.writer.com/v1/graphs/question \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw
          '{"graph_ids":["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],"question":"What
          is the generic name for the drug Bavencio?"}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const question = await client.graphs.question({
              graph_ids: ['182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e'],
              question: 'What is the generic name for the drug Bavencio?'
          });

            console.log(question.answer);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              # This is the default and can be omitted
              api_key=os.environ.get("WRITER_API_KEY"),
          )
          question = client.graphs.question(
              graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
              question="What is the generic name for the drug Bavencio?"
          )
          print(question.answer)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              question:
                allOf:
                  - &ref_1
                    type: string
                    description: The question that was asked.
              answer:
                allOf:
                  - &ref_2
                    type: string
                    description: The answer to the question.
              sources:
                allOf:
                  - &ref_3
                    type: array
                    items:
                      $ref: '#/components/schemas/source'
              subqueries:
                allOf:
                  - &ref_4
                    type: array
                    items:
                      $ref: '#/components/schemas/sub_query'
              references:
                allOf:
                  - &ref_5
                    $ref: '#/components/schemas/references'
            title: question_response
            refIdentifier: '#/components/schemas/question_response'
            requiredProperties: &ref_0
              - question
              - answer
              - sources
        examples:
          example:
            value:
              question: What is the generic name for the drug Bavencio?
              answer: avelumab
              sources:
                - file_id: '1234'
                  snippet: Bavencio is the brand name for avelumab.
        description: ''
      text/event-stream:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/question_response'
            refIdentifier: '#/components/schemas/question_response_chunk'
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                - question: What is the generic name for the drug Bavencio?
                  answer: avelumab
                  sources:
                    - file_id: '1234'
                      snippet: Bavencio is the brand name for avelumab.
        description: ''
  deprecated: false
  type: path
components:
  schemas:
    question_response:
      title: question_response
      required: *ref_0
      type: object
      properties:
        question: *ref_1
        answer: *ref_2
        sources: *ref_3
        subqueries: *ref_4
        references: *ref_5
    source:
      title: source
      description: >-
        A source snippet containing text and fileId from Knowledge Graph
        content.
      required:
        - file_id
        - snippet
      type: object
      nullable: true
      properties:
        file_id:
          type: string
          description: The unique identifier of the file in your Writer account.
        snippet:
          type: string
          description: >-
            The exact text snippet from the source document that was used to
            support the response.
    sub_query:
      title: sub_query
      description: >-
        A sub-question generated to break down complex queries into more
        manageable parts, along with its answer and supporting sources.
      required:
        - query
        - answer
        - sources
      type: object
      nullable: true
      properties:
        query:
          type: string
          description: The subquery that was generated to help answer the main question.
        answer:
          type: string
          description: The answer to the subquery based on Knowledge Graph content.
        sources:
          type: array
          description: Array of source snippets that were used to answer this subquery.
          items:
            $ref: '#/components/schemas/source'
    graph_query_config:
      title: graph_query_config
      description: Configuration options for Knowledge Graph queries.
      type: object
      properties:
        max_subquestions:
          type: integer
          format: int32
          minimum: 1
          maximum: 10
          default: 6
          description: >-
            Maximum number of subquestions to generate when processing complex
            queries. Set higher to improve detail, set lower to reduce response
            time. Range: 1-10, Default: 6.
        search_weight:
          type: integer
          format: int32
          minimum: 0
          maximum: 100
          default: 50
          description: >-
            Weight given to search results when ranking and selecting relevant
            information. Higher values (closer to 100) prioritize keyword-based
            matching, while lower values (closer to 0) prioritize semantic
            similarity matching. Use higher values for exact keyword searches,
            lower values for conceptual similarity searches. Range: 0-100,
            Default: 50.
        grounding_level:
          type: number
          format: double
          minimum: 0
          maximum: 1
          default: 0
          description: >-
            Level of grounding required for responses, controlling how closely
            answers must be tied to source material. Set lower for grounded
            outputs, higher for creativity. Higher values (closer to 1.0) allow
            more creative interpretation, while lower values (closer to 0.0)
            stick more closely to source material. Range: 0.0-1.0, Default: 0.0.
        max_snippets:
          type: integer
          format: int32
          minimum: 1
          maximum: 60
          default: 30
          description: >-
            Maximum number of text snippets to retrieve from the Knowledge Graph
            for context. Works in concert with `search_weight` to control best
            matches vs broader coverage. While technically supports 1-60, values
            below 5 may return no results due to RAG implementation. Recommended
            range: 5-25. Due to RAG system behavior, you may see more snippets
            than requested. Range: 1-60, Default: 30.
        max_tokens:
          type: integer
          format: int32
          minimum: 100
          maximum: 8000
          default: 4000
          description: >-
            Maximum number of tokens the model can generate in the response.
            This controls the length of the AI's answer. Set higher for longer
            answers, set lower for shorter, faster answers. Range: 100-8000,
            Default: 4000.
        keyword_threshold:
          type: number
          format: double
          minimum: 0
          maximum: 1
          default: 0.7
          description: >-
            Threshold for keyword-based matching when searching Knowledge Graph
            content. Set higher for stricter relevance, lower for broader range.
            Higher values (closer to 1.0) require stronger keyword matches,
            while lower values (closer to 0.0) allow more lenient matching.
            Range: 0.0-1.0, Default: 0.7.
        semantic_threshold:
          type: number
          format: double
          minimum: 0
          maximum: 1
          default: 0.7
          description: >-
            Threshold for semantic similarity matching when searching Knowledge
            Graph content. Set higher for stricter relevance, lower for broader
            range. Higher values (closer to 1.0) require stronger semantic
            similarity, while lower values (closer to 0.0) allow more lenient
            semantic matching. Range: 0.0-1.0, Default: 0.7.
        inline_citations:
          type: boolean
          default: false
          description: >-
            Whether to include inline citations in the response, showing which
            Knowledge Graph sources were used. Default: false.
    references:
      title: references
      description: >-
        Detailed source information organized by reference type, providing
        comprehensive metadata about the sources used to generate the response.
      type: object
      properties:
        files:
          type: array
          description: >-
            Array of file-based references from uploaded documents in the
            Knowledge Graph.
          items:
            $ref: '#/components/schemas/file'
          minItems: 1
        web:
          type: array
          description: >-
            Array of web-based references from online sources accessed during
            the query.
          items:
            $ref: '#/components/schemas/web'
          minItems: 1
    file:
      title: file
      description: >-
        A file-based reference containing text snippets from uploaded documents
        in the Knowledge Graph.
      required:
        - text
        - fileId
        - score
      type: object
      properties:
        text:
          type: string
          description: >-
            The exact text snippet from the source document that was used to
            support the response.
        fileId:
          type: string
          description: The unique identifier of the file in your Writer account.
        score:
          type: number
          description: >-
            Internal score used during the retrieval process for ranking and
            selecting relevant snippets.
        page:
          type: integer
          format: int32
          description: Page number where this snippet was found in the source document.
        cite:
          type: string
          description: >-
            Unique citation ID that appears in inline citations within the
            response text (null if not cited).
    web:
      title: web
      description: >-
        A web-based reference containing text snippets from online sources
        accessed during the query.
      required:
        - text
        - url
        - title
        - score
      type: object
      properties:
        text:
          type: string
          description: >-
            The exact text snippet from the web source that was used to support
            the response.
        url:
          type: string
          description: The URL of the web page where this content was found.
          format: uri
        title:
          type: string
          description: The title of the web page where this content was found.
        score:
          type: number
          description: >-
            Internal score used during the retrieval process for ranking and
            selecting relevant snippets.

````