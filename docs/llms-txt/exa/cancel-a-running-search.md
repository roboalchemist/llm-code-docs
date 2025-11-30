# Source: https://docs.exa.ai/websets/api/websets/searches/cancel-a-running-search.md

# Cancel a running Search

> Cancels a currently running Search.

You can cancel all searches at once by using the `websets/:webset/cancel` endpoint.

## OpenAPI

````yaml post /v0/websets/{webset}/searches/{id}/cancel
paths:
  path: /v0/websets/{webset}/searches/{id}/cancel
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
        id:
          schema:
            - type: string
              required: true
              description: The id of the Search
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: >-
          // npm install exa-js

          import Exa from 'exa-js';

          const exa = new Exa('YOUR_EXA_API_KEY');


          const search = await exa.websets.searches.cancel('webset_id',
          'search_id');


          console.log(`Cancelled search: ${search.id}`);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          search = exa.websets.searches.cancel('webset_id', 'search_id')

          print(f'Cancelled search: {search.id}')
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
        description: Search canceled
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