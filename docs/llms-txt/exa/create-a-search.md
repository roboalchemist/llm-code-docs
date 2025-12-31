# Source: https://docs.exa.ai/websets/api/websets/searches/create-a-search.md

# Create a Search

> Creates a new Search for the Webset.

The default behavior is to reuse the previous Search results and evaluate them against the new criteria.

## OpenAPI

````yaml post /v0/websets/{webset}/searches
paths:
  path: /v0/websets/{webset}/searches
  method: post
  servers:
    - url: https://api.exa.ai/websets/
      description: Production
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: Your Exa API key
          cookie: {}
    parameters:
      path:
        webset:
          schema:
            - type: string
              required: true
              description: The id of the Webset
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              count:
                allOf:
                  - type:
                      - number
                    minimum: 1
                    description: >-
                      Number of Items the Search will attempt to find.


                      The actual number of Items found may be less than this
                      number depending on the query complexity.
              query:
                allOf:
                  - type:
                      - string
                    minLength: 1
                    maxLength: 5000
                    description: >-
                      Natural language search query describing what you are
                      looking for.


                      Be specific and descriptive about your requirements,
                      characteristics, and any constraints that help narrow down
                      the results.


                      Any URLs provided will be crawled and used as additional
                      context for the search.
                    examples:
                      - >-
                        Marketing agencies based in the US, that focus on
                        consumer products. Get brands worked with and city
                      - >-
                        AI startups in Europe that raised Series A funding in
                        2024
                      - >-
                        SaaS companies with 50-200 employees in the fintech
                        space
              entity:
                allOf:
                  - $ref: '#/components/schemas/Entity'
                    description: >-
                      Entity the search will return results for.


                      It is not required to provide it, we automatically detect
                      the entity from all the information provided in the query.
                      Only use this when you need more fine control.
              criteria:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/CreateCriterionParameters'
                      title: CreateCriterionParameters
                    minItems: 1
                    maxItems: 5
                    description: >-
                      Criteria every item is evaluated against.


                      It's not required to provide your own criteria, we
                      automatically detect the criteria from all the information
                      provided in the query. Only use this when you need more
                      fine control.
              exclude:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      properties:
                        source:
                          type:
                            - string
                          enum:
                            - import
                            - webset
                        id:
                          description: The ID of the source to exclude.
                          type:
                            - string
                          minLength: 1
                      required:
                        - source
                        - id
                    description: >-
                      Sources (existing imports or websets) to exclude from
                      search results. Any results found within these sources
                      will be omitted to prevent finding them during search.
              scope:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      properties:
                        source:
                          type:
                            - string
                          enum:
                            - import
                            - webset
                        id:
                          type:
                            - string
                          minLength: 1
                          description: The ID of the source to search.
                        relationship:
                          type:
                            - object
                          properties:
                            definition:
                              type:
                                - string
                              description: >-
                                What the relationship of the entities you hope
                                to find is relative to the entities contained in
                                the provided source.
                            limit:
                              type:
                                - number
                              minimum: 1
                              maximum: 10
                          required:
                            - definition
                            - limit
                      required:
                        - source
                        - id
                    description: >-
                      Limit the search to specific sources (existing imports).
                      Any results found within these sources matching the search
                      criteria will be included in the Webset.
              recall:
                allOf:
                  - type:
                      - boolean
                    description: >-
                      Whether to provide an estimate of how many total relevant
                      results could exist for this search.

                      Result of the analysis will be available in the `recall`
                      field within the search request.
              behavior:
                allOf:
                  - default: override
                    type:
                      - string
                    description: >-
                      How this search interacts with existing items in the
                      Webset:


                      - **override**: Replace existing items and evaluate all
                      items against new criteria

                      - **append**: Add new items to existing ones, keeping
                      items that match the new criteria
                    $ref: '#/components/schemas/WebsetSearchBehavior'
              metadata:
                allOf:
                  - description: >-
                      Set of key-value pairs you want to associate with this
                      object.
                    type:
                      - object
                    additionalProperties:
                      type:
                        - string
                      maxLength: 1000
            required: true
            refIdentifier: '#/components/schemas/CreateWebsetSearchParameters'
            requiredProperties:
              - count
              - query
        examples:
          example:
            value:
              count: 2
              query: >-
                Marketing agencies based in the US, that focus on consumer
                products. Get brands worked with and city
              entity:
                type: company
              criteria:
                - description: <string>
              exclude:
                - source: import
                  id: <string>
              scope:
                - source: import
                  id: <string>
                  relationship:
                    definition: <string>
                    limit: 5.5
              recall: true
              behavior: override
              metadata: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: |-
          // npm install exa-js
          import Exa from 'exa-js';
          const exa = new Exa('YOUR_EXA_API_KEY');

          const search = await exa.websets.searches.create('webset_id', {
            query: 'additional companies to add',
            count: 5
          });

          console.log(`Created search: ${search.id}`);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          search = exa.websets.searches.create('webset_id', params={
              'query': 'additional companies to add',
              'count': 5
          })

          print(f'Created search: {search.id}')
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type:
                      - string
                    description: The unique identifier for the search
              object:
                allOf:
                  - type: string
                    const: webset_search
                    default: webset_search
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - created
                      - pending
                      - running
                      - completed
                      - canceled
                    description: The status of the search
                    title: WebsetSearchStatus
              websetId:
                allOf:
                  - type:
                      - string
                    description: >-
                      The unique identifier for the Webset this search belongs
                      to
              query:
                allOf:
                  - description: The query used to create the search.
                    type:
                      - string
                    minLength: 1
                    maxLength: 5000
              entity:
                allOf:
                  - $ref: '#/components/schemas/Entity'
                    description: >-
                      The entity the search will return results for.


                      When no entity is provided during creation, we will
                      automatically select the best entity based on the query.
                    nullable: true
              criteria:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      properties:
                        description:
                          description: The description of the criterion
                          type:
                            - string
                          minLength: 1
                          maxLength: 1000
                        successRate:
                          type:
                            - number
                          minimum: 0
                          maximum: 100
                          description: >-
                            Value between 0 and 100 representing the percentage
                            of results that meet the criterion.
                      required:
                        - description
                        - successRate
                    description: >-
                      The criteria the search will use to evaluate the results.
                      If not provided, we will automatically generate them for
                      you.
              count:
                allOf:
                  - type:
                      - number
                    minimum: 1
                    description: >-
                      The number of results the search will attempt to find. The
                      actual number of results may be less than this number
                      depending on the search complexity.
              behavior:
                allOf:
                  - default: override
                    type:
                      - string
                    $ref: '#/components/schemas/WebsetSearchBehavior'
                    description: >-
                      The behavior of the search when it is added to a Webset.


                      - `override`: the search will replace the existing Items
                      found in the Webset and evaluate them against the new
                      criteria. Any Items that don't match the new criteria will
                      be discarded.

                      - `append`: the search will add the new Items found to the
                      existing Webset. Any Items that don't match the new
                      criteria will be discarded.
              exclude:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      properties:
                        source:
                          type:
                            - string
                          enum:
                            - import
                            - webset
                        id:
                          type:
                            - string
                      required:
                        - source
                        - id
                    description: >-
                      Sources (existing imports or websets) used to omit certain
                      results to be found during the search.
              scope:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      properties:
                        source:
                          type:
                            - string
                          enum:
                            - import
                            - webset
                        id:
                          type:
                            - string
                        relationship:
                          type:
                            - object
                          properties:
                            definition:
                              type:
                                - string
                              description: >-
                                What the relationship of the entities you hope
                                to find is relative to the entities contained in
                                the provided source.
                            limit:
                              type:
                                - number
                              minimum: 1
                              maximum: 10
                          required:
                            - definition
                            - limit
                      required:
                        - source
                        - id
                    description: >-
                      The scope of the search. By default, there is no scope -
                      thus searching the web.


                      If provided during creation, the search will only be
                      performed on the sources provided.
              progress:
                allOf:
                  - type:
                      - object
                    properties:
                      found:
                        type:
                          - number
                        description: The number of results found so far
                      analyzed:
                        type:
                          - number
                        description: The number of results analyzed so far
                      completion:
                        type:
                          - number
                        minimum: 0
                        maximum: 100
                        description: The completion percentage of the search
                      timeLeft:
                        type: number
                        description: >-
                          The estimated time remaining in seconds, null if
                          unknown
                        nullable: true
                    required:
                      - found
                      - analyzed
                      - completion
                      - timeLeft
                    description: The progress of the search
              recall:
                allOf:
                  - type: object
                    properties:
                      expected:
                        type:
                          - object
                        properties:
                          total:
                            type:
                              - number
                            description: The estimated total number of potential matches
                          confidence:
                            type:
                              - string
                            enum:
                              - high
                              - medium
                              - low
                            description: The confidence in the estimate
                          bounds:
                            type:
                              - object
                            properties:
                              min:
                                type:
                                  - number
                                description: >-
                                  The minimum estimated total number of
                                  potential matches
                              max:
                                type:
                                  - number
                                description: >-
                                  The maximum estimated total number of
                                  potential matches
                            required:
                              - min
                              - max
                        required:
                          - total
                          - confidence
                          - bounds
                      reasoning:
                        type:
                          - string
                        description: The reasoning for the estimate
                    required:
                      - expected
                      - reasoning
                    description: >-
                      Recall metrics for the search, null if not yet computed or
                      requested.
                    nullable: true
              metadata:
                allOf:
                  - default: {}
                    description: >-
                      Set of key-value pairs you want to associate with this
                      object.
                    type:
                      - object
                    additionalProperties:
                      type:
                        - string
                      maxLength: 1000
              canceledAt:
                allOf:
                  - type: string
                    format: date-time
                    description: The date and time the search was canceled
                    nullable: true
              canceledReason:
                allOf:
                  - type: string
                    $ref: '#/components/schemas/WebsetSearchCanceledReason'
                    description: The reason the search was canceled
                    nullable: true
              createdAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the search was created
              updatedAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the search was updated
            refIdentifier: '#/components/schemas/WebsetSearch'
            requiredProperties:
              - id
              - object
              - websetId
              - status
              - query
              - entity
              - criteria
              - count
              - exclude
              - scope
              - progress
              - recall
              - canceledAt
              - canceledReason
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              object: webset_search
              status: created
              websetId: <string>
              query: <string>
              entity:
                type: company
              criteria:
                - description: <string>
                  successRate: 50
              count: 2
              behavior: override
              exclude:
                - source: import
                  id: <string>
              scope:
                - source: import
                  id: <string>
                  relationship:
                    definition: <string>
                    limit: 5.5
              progress:
                found: 123
                analyzed: 123
                completion: 50
                timeLeft: 123
              recall:
                expected:
                  total: 123
                  confidence: high
                  bounds:
                    min: 123
                    max: 123
                reasoning: <string>
              metadata: {}
              canceledAt: '2023-11-07T05:31:56Z'
              canceledReason: webset_deleted
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
        description: Webset Search created
  deprecated: false
  type: path
components:
  schemas:
    CompanyEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: company
          default: company
      required:
        - type
      title: Company
    PersonEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: person
          default: person
      required:
        - type
      title: Person
    ArticleEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: article
          default: article
      required:
        - type
      title: Article
    ResearchPaperEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: research_paper
          default: research_paper
      required:
        - type
      title: Research Paper
    CustomEntity:
      type:
        - object
      properties:
        type:
          type: string
          const: custom
          default: custom
        description:
          type:
            - string
          minLength: 2
          maxLength: 200
      required:
        - type
        - description
      title: Custom
    Entity:
      oneOf:
        - type:
            - object
          $ref: '#/components/schemas/CompanyEntity'
        - type:
            - object
          $ref: '#/components/schemas/PersonEntity'
        - type:
            - object
          $ref: '#/components/schemas/ArticleEntity'
        - type:
            - object
          $ref: '#/components/schemas/ResearchPaperEntity'
        - type:
            - object
          $ref: '#/components/schemas/CustomEntity'
    CreateCriterionParameters:
      type:
        - object
      properties:
        description:
          type:
            - string
          minLength: 1
          maxLength: 1000
          description: The description of the criterion
      required:
        - description
    WebsetSearchBehavior:
      type: string
      enum:
        - override
        - append
    WebsetSearchCanceledReason:
      type: string
      enum:
        - webset_deleted
        - webset_canceled

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt