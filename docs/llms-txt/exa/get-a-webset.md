# Source: https://docs.exa.ai/websets/api/websets/get-a-webset.md

# Get a Webset

## OpenAPI

````yaml get /v0/websets/{id}
paths:
  path: /v0/websets/{id}
  method: get
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
        id:
          schema:
            - type: string
              required: true
              description: The id or externalId of the Webset.
      query:
        expand:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
                    enum:
                      - items
              required: false
              description: Expand the response with the specified resources
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: |-
          // npm install exa-js
          import Exa from 'exa-js';
          const exa = new Exa('YOUR_EXA_API_KEY');

          const webset = await exa.websets.get('webset_id');

          console.log(`Webset: ${webset.id} - ${webset.status}`);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          webset = exa.websets.get('webset_id')

          print(f'Webset: {webset.id} - {webset.status}')
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
                    description: The unique identifier for the webset
              object:
                allOf:
                  - type: string
                    const: webset
                    default: webset
              status:
                allOf:
                  - type:
                      - string
                    enum:
                      - idle
                      - pending
                      - running
                      - paused
                    description: The status of the webset
                    title: WebsetStatus
              externalId:
                allOf:
                  - type: string
                    description: The external identifier for the webset
                    nullable: true
              title:
                allOf:
                  - type: string
                    description: The title of the webset
                    nullable: true
              searches:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/WebsetSearch'
                    description: The searches that have been performed on the webset.
              imports:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/Import'
                    description: Imports that have been performed on the webset.
              enrichments:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/WebsetEnrichment'
                    description: The Enrichments to apply to the Webset Items.
              monitors:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/Monitor'
                    description: The Monitors for the Webset.
              excludes:
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
                      The Excludes sources (existing imports or websets) that
                      apply to all operations within this Webset. Any results
                      found within these sources will be omitted across all
                      search and import operations.
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
              createdAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the webset was created
              updatedAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the webset was updated
              items:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/WebsetItem'
                    description: >-
                      When expand query parameter contains `items`, this will
                      contain the items in the webset
            refIdentifier: '#/components/schemas/Webset'
            requiredProperties:
              - id
              - object
              - status
              - externalId
              - title
              - searches
              - imports
              - enrichments
              - monitors
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              id: <string>
              object: webset
              status: idle
              externalId: <string>
              title: <string>
              searches:
                - id: <string>
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
              imports:
                - id: <string>
                  object: import
                  status: pending
                  format: csv
                  entity:
                    type: <string>
                  title: <string>
                  count: 123
                  metadata: {}
                  failedReason: invalid_format
                  failedAt: '2023-11-07T05:31:56Z'
                  failedMessage: <string>
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
              enrichments:
                - id: <string>
                  object: webset_enrichment
                  status: pending
                  websetId: <string>
                  title: <string>
                  description: <string>
                  format: text
                  options:
                    - label: <string>
                  instructions: <string>
                  metadata: {}
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
              monitors:
                - id: <string>
                  object: monitor
                  status: enabled
                  websetId: <string>
                  cadence:
                    cron: <string>
                    timezone: Etc/UTC
                  behavior:
                    type: search
                    config:
                      query: <string>
                      criteria:
                        - description: <string>
                      entity:
                        type: <string>
                      count: 123
                      behavior: append
                  lastRun:
                    id: <string>
                    object: monitor_run
                    status: created
                    monitorId: <string>
                    type: search
                    completedAt: '2023-11-07T05:31:56Z'
                    failedAt: '2023-11-07T05:31:56Z'
                    failedReason: <string>
                    canceledAt: '2023-11-07T05:31:56Z'
                    createdAt: '2023-11-07T05:31:56Z'
                    updatedAt: '2023-11-07T05:31:56Z'
                  nextRunAt: '2023-11-07T05:31:56Z'
                  metadata: {}
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
              excludes:
                - source: import
                  id: <string>
              metadata: {}
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
              items:
                - id: <string>
                  object: webset_item
                  source: search
                  sourceId: <string>
                  websetId: <string>
                  properties:
                    type: person
                    url: <string>
                    description: <string>
                    person:
                      name: <string>
                      location: <string>
                      position: <string>
                      company:
                        name: <string>
                        location: <string>
                      pictureUrl: <string>
                  evaluations:
                    - criterion: <string>
                      reasoning: <string>
                      satisfied: 'yes'
                      references: []
                  enrichments:
                    - object: enrichment_result
                      status: pending
                      format: text
                      result:
                        - <string>
                      reasoning: <string>
                      references:
                        - title: <string>
                          snippet: <string>
                          url: <string>
                      enrichmentId: <string>
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
        description: Webset
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Webset not found
        examples: {}
        description: Webset not found
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
    WebsetSearch:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the search
        object:
          type: string
          const: webset_search
          default: webset_search
        status:
          type:
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
          type:
            - string
          description: The unique identifier for the Webset this search belongs to
        query:
          description: The query used to create the search.
          type:
            - string
          minLength: 1
          maxLength: 5000
        entity:
          $ref: '#/components/schemas/Entity'
          description: >-
            The entity the search will return results for.


            When no entity is provided during creation, we will automatically
            select the best entity based on the query.
          nullable: true
        criteria:
          type:
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
                  Value between 0 and 100 representing the percentage of results
                  that meet the criterion.
            required:
              - description
              - successRate
          description: >-
            The criteria the search will use to evaluate the results. If not
            provided, we will automatically generate them for you.
        count:
          type:
            - number
          minimum: 1
          description: >-
            The number of results the search will attempt to find. The actual
            number of results may be less than this number depending on the
            search complexity.
        behavior:
          default: override
          type:
            - string
          $ref: '#/components/schemas/WebsetSearchBehavior'
          description: >-
            The behavior of the search when it is added to a Webset.


            - `override`: the search will replace the existing Items found in
            the Webset and evaluate them against the new criteria. Any Items
            that don't match the new criteria will be discarded.

            - `append`: the search will add the new Items found to the existing
            Webset. Any Items that don't match the new criteria will be
            discarded.
        exclude:
          type:
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
            Sources (existing imports or websets) used to omit certain results
            to be found during the search.
        scope:
          type:
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
                      What the relationship of the entities you hope to find is
                      relative to the entities contained in the provided source.
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
            The scope of the search. By default, there is no scope - thus
            searching the web.


            If provided during creation, the search will only be performed on
            the sources provided.
        progress:
          type:
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
              description: The estimated time remaining in seconds, null if unknown
              nullable: true
          required:
            - found
            - analyzed
            - completion
            - timeLeft
          description: The progress of the search
        recall:
          type: object
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
                      description: The minimum estimated total number of potential matches
                    max:
                      type:
                        - number
                      description: The maximum estimated total number of potential matches
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
          default: {}
          description: Set of key-value pairs you want to associate with this object.
          type:
            - object
          additionalProperties:
            type:
              - string
            maxLength: 1000
        canceledAt:
          type: string
          format: date-time
          description: The date and time the search was canceled
          nullable: true
        canceledReason:
          type: string
          $ref: '#/components/schemas/WebsetSearchCanceledReason'
          description: The reason the search was canceled
          nullable: true
        createdAt:
          type:
            - string
          format: date-time
          description: The date and time the search was created
        updatedAt:
          type:
            - string
          format: date-time
          description: The date and time the search was updated
      required:
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
    Import:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the Import
        object:
          type:
            - string
          enum:
            - import
          description: The type of object
        status:
          type:
            - string
          enum:
            - pending
            - processing
            - completed
            - failed
          description: The status of the Import
        format:
          type:
            - string
          enum:
            - csv
            - webset
          description: The format of the import.
        entity:
          $ref: '#/components/schemas/Entity'
          description: The type of entity the import contains.
          nullable: true
        title:
          type:
            - string
          description: The title of the import
        count:
          type:
            - number
          description: The number of entities in the import
        metadata:
          description: Set of key-value pairs you want to associate with this object.
          type:
            - object
          additionalProperties:
            type:
              - string
            maxLength: 1000
        failedReason:
          type: string
          enum:
            - invalid_format
            - invalid_file_content
            - missing_identifier
          description: The reason the import failed
          nullable: true
        failedAt:
          type: string
          format: date-time
          description: When the import failed
          nullable: true
        failedMessage:
          type: string
          description: A human readable message of the import failure
          nullable: true
        createdAt:
          type:
            - string
          format: date-time
          description: When the import was created
        updatedAt:
          type:
            - string
          format: date-time
          description: When the import was last updated
      required:
        - id
        - object
        - status
        - format
        - entity
        - title
        - count
        - metadata
        - failedReason
        - failedAt
        - failedMessage
        - createdAt
        - updatedAt
    WebsetEnrichment:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the enrichment
        object:
          type: string
          const: webset_enrichment
          default: webset_enrichment
        status:
          type:
            - string
          enum:
            - pending
            - canceled
            - completed
          description: The status of the enrichment
          title: WebsetEnrichmentStatus
        websetId:
          type:
            - string
          description: The unique identifier for the Webset this enrichment belongs to.
        title:
          type: string
          description: >-
            The title of the enrichment.


            This will be automatically generated based on the description and
            format.
          nullable: true
        description:
          type:
            - string
          description: >-
            The description of the enrichment task provided during the creation
            of the enrichment.
        format:
          type: string
          $ref: '#/components/schemas/WebsetEnrichmentFormat'
          description: The format of the enrichment response.
          nullable: true
        options:
          type: array
          items:
            type:
              - object
            properties:
              label:
                type:
                  - string
                description: The label of the option
            required:
              - label
          description: >-
            When the format is options, the different options for the enrichment
            agent to choose from.
          title: WebsetEnrichmentOptions
          nullable: true
        instructions:
          type: string
          description: >-
            The instructions for the enrichment Agent.


            This will be automatically generated based on the description and
            format.
          nullable: true
        metadata:
          default: {}
          description: The metadata of the enrichment
          type:
            - object
          additionalProperties:
            type:
              - string
            maxLength: 1000
        createdAt:
          type:
            - string
          format: date-time
          description: The date and time the enrichment was created
        updatedAt:
          type:
            - string
          format: date-time
          description: The date and time the enrichment was updated
      required:
        - id
        - object
        - status
        - websetId
        - title
        - description
        - format
        - options
        - instructions
        - createdAt
        - updatedAt
    MonitorRun:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the Monitor Run
        object:
          type:
            - string
          enum:
            - monitor_run
          description: The type of object
        status:
          type:
            - string
          enum:
            - created
            - running
            - completed
            - canceled
            - failed
          description: The status of the Monitor Run
        monitorId:
          type:
            - string
          description: The monitor that the run is associated with
        type:
          type:
            - string
          enum:
            - search
            - refresh
          description: The type of the Monitor Run
        completedAt:
          type: string
          format: date-time
          description: When the run completed
          nullable: true
        failedAt:
          type: string
          format: date-time
          description: When the run failed
          nullable: true
        failedReason:
          type: string
          description: The reason the run failed
          nullable: true
        canceledAt:
          type: string
          format: date-time
          description: When the run was canceled
          nullable: true
        createdAt:
          type:
            - string
          format: date-time
          description: When the run was created
        updatedAt:
          type:
            - string
          format: date-time
          description: When the run was last updated
      required:
        - id
        - object
        - monitorId
        - status
        - type
        - completedAt
        - failedAt
        - failedReason
        - canceledAt
        - createdAt
        - updatedAt
    Monitor:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the Monitor
        object:
          type:
            - string
          enum:
            - monitor
          description: The type of object
        status:
          type:
            - string
          enum:
            - enabled
            - disabled
          description: The status of the Monitor
        websetId:
          type:
            - string
          description: The id of the Webset the Monitor belongs to
        cadence:
          type:
            - object
          properties:
            cron:
              description: >-
                Cron expression for monitor cadence (must be a valid Unix cron
                with 5 fields). The schedule must trigger at most once per day.
              type:
                - string
            timezone:
              description: IANA timezone (e.g., "America/New_York")
              default: Etc/UTC
              type:
                - string
          required:
            - cron
          description: How often the monitor will run
        behavior:
          type:
            - object
          properties:
            type:
              type: string
              const: search
              default: search
            config:
              type:
                - object
              properties:
                query:
                  type:
                    - string
                  minLength: 2
                  maxLength: 10000
                  description: >-
                    The query to search for. By default, the query from the last
                    search is used.
                criteria:
                  type:
                    - array
                  items:
                    type:
                      - object
                    properties:
                      description:
                        type:
                          - string
                        minLength: 2
                        maxLength: 1000
                    required:
                      - description
                  maxItems: 5
                  description: >-
                    The criteria to search for. By default, the criteria from
                    the last search is used.
                entity:
                  $ref: '#/components/schemas/Entity'
                  title: Entity
                  description: >-
                    The entity to search for. By default, the entity from the
                    last search/import is used.
                count:
                  type:
                    - number
                  exclusiveMinimum: 0
                  description: The maximum number of results to find
                behavior:
                  default: append
                  type:
                    - string
                  enum:
                    - override
                    - append
                  description: The behaviour of the Search when it is added to a Webset.
              required:
                - count
              description: >-
                Specify the search parameters for the Monitor.


                By default, the search parameters (query, entity and criteria)
                from the last search are used when no parameters are provided.
          required:
            - type
            - config
          description: Behavior to perform when monitor runs
        lastRun:
          type: object
          $ref: '#/components/schemas/MonitorRun'
          title: MonitorRun
          description: The last run of the monitor
          nullable: true
        nextRunAt:
          type: string
          format: date-time
          description: Date and time when the next run will occur in
          nullable: true
        metadata:
          description: Set of key-value pairs you want to associate with this object.
          type:
            - object
          additionalProperties:
            type:
              - string
            maxLength: 1000
        createdAt:
          type:
            - string
          format: date-time
          description: When the monitor was created
        updatedAt:
          type:
            - string
          format: date-time
          description: When the monitor was last updated
      required:
        - id
        - object
        - status
        - websetId
        - cadence
        - behavior
        - lastRun
        - nextRunAt
        - metadata
        - createdAt
        - updatedAt
    WebsetItemPersonProperties:
      type:
        - object
      properties:
        type:
          type: string
          const: person
          default: person
        url:
          type:
            - string
          format: uri
          description: The URL of the person profile
        description:
          type:
            - string
          description: Short description of the relevance of the person
        person:
          type:
            - object
          properties:
            name:
              type:
                - string
              description: The name of the person
            location:
              type: string
              description: The location of the person
              nullable: true
            position:
              type: string
              description: The current work position of the person
              nullable: true
            company:
              type: object
              properties:
                name:
                  type:
                    - string
                  description: The name of the company
                location:
                  type: string
                  description: The location the person is working at the company
                  nullable: true
              required:
                - name
                - location
              title: WebsetItemPersonCompanyPropertiesFields
              nullable: true
            pictureUrl:
              type: string
              format: uri
              description: The image URL of the person
              nullable: true
          required:
            - name
            - location
            - position
            - company
            - pictureUrl
          title: WebsetItemPersonPropertiesFields
      required:
        - type
        - url
        - description
        - person
    WebsetItemCompanyProperties:
      type:
        - object
      properties:
        type:
          type: string
          const: company
          default: company
        url:
          type:
            - string
          format: uri
          description: The URL of the company website
        description:
          type:
            - string
          description: Short description of the relevance of the company
        content:
          type: string
          description: The text content of the company website
          nullable: true
        company:
          type:
            - object
          properties:
            name:
              type:
                - string
              description: The name of the company
            location:
              type: string
              description: The main location of the company
              nullable: true
            employees:
              type: number
              description: The number of employees of the company
              nullable: true
            industry:
              type: string
              description: The industry of the company
              nullable: true
            about:
              type: string
              description: A short description of the company
              nullable: true
            logoUrl:
              type: string
              format: uri
              description: The logo URL of the company
              nullable: true
          required:
            - name
            - location
            - employees
            - industry
            - about
            - logoUrl
          title: WebsetItemCompanyPropertiesFields
      required:
        - type
        - url
        - description
        - content
        - company
    WebsetItemArticleProperties:
      type:
        - object
      properties:
        type:
          type: string
          const: article
          default: article
        url:
          type:
            - string
          format: uri
          description: The URL of the article
        description:
          type:
            - string
          description: Short description of the relevance of the article
        content:
          type: string
          description: The text content for the article
          nullable: true
        article:
          type:
            - object
          properties:
            title:
              type: string
              description: The title of the article
              nullable: true
            author:
              type: string
              description: The author(s) of the article
              nullable: true
            publishedAt:
              type: string
              description: The date and time the article was published
              nullable: true
          required:
            - title
            - author
            - publishedAt
          title: WebsetItemArticlePropertiesFields
      required:
        - type
        - url
        - description
        - content
        - article
    WebsetItemResearchPaperProperties:
      type:
        - object
      properties:
        type:
          type: string
          const: research_paper
          default: research_paper
        url:
          type:
            - string
          format: uri
          description: The URL of the research paper
        description:
          type:
            - string
          description: Short description of the relevance of the research paper
        content:
          type: string
          description: The text content of the research paper
          nullable: true
        researchPaper:
          type:
            - object
          properties:
            title:
              type: string
              description: The title of the research paper
              nullable: true
            author:
              type: string
              description: The author(s) of the research paper
              nullable: true
            publishedAt:
              type: string
              description: The date and time the research paper was published
              nullable: true
          required:
            - title
            - author
            - publishedAt
          title: WebsetItemResearchPaperPropertiesFields
      required:
        - type
        - url
        - description
        - content
        - researchPaper
    WebsetItemCustomProperties:
      type:
        - object
      properties:
        type:
          type: string
          const: custom
          default: custom
        url:
          type:
            - string
          format: uri
          description: The URL of the Item
        description:
          type:
            - string
          description: Short description of the Item
        content:
          type: string
          description: The text content of the Item
          nullable: true
        custom:
          type:
            - object
          properties:
            title:
              type: string
              description: The title of the website
              nullable: true
            author:
              type: string
              description: The author(s) of the website
              nullable: true
            publishedAt:
              type: string
              description: The date and time the website was published
              nullable: true
          required:
            - title
            - author
            - publishedAt
          title: WebsetItemCustomPropertiesFields
      required:
        - type
        - url
        - description
        - content
        - custom
    WebsetItemEvaluation:
      type:
        - object
      properties:
        criterion:
          type:
            - string
          description: The description of the criterion
        reasoning:
          type:
            - string
          description: The reasoning for the result of the evaluation
        satisfied:
          type:
            - string
          enum:
            - 'yes'
            - 'no'
            - unclear
          description: The satisfaction of the criterion
        references:
          default: []
          type:
            - array
          items:
            type:
              - object
            properties:
              title:
                type: string
                description: The title of the reference
                nullable: true
              snippet:
                type: string
                description: The relevant snippet of the reference content
                nullable: true
              url:
                type:
                  - string
                format: uri
                description: The URL of the reference
            required:
              - title
              - snippet
              - url
          description: The references used to generate the result.
      required:
        - criterion
        - reasoning
        - satisfied
    EnrichmentResult:
      type:
        - object
      properties:
        object:
          type: string
          const: enrichment_result
          default: enrichment_result
        status:
          type:
            - string
          enum:
            - pending
            - completed
            - canceled
          description: The status of the enrichment result.
        format:
          type:
            - string
          $ref: '#/components/schemas/WebsetEnrichmentFormat'
        result:
          type: array
          items:
            type:
              - string
          description: The result of the enrichment.
          nullable: true
        reasoning:
          type: string
          description: The reasoning for the result when an Agent is used.
          nullable: true
        references:
          type:
            - array
          items:
            type:
              - object
            properties:
              title:
                type: string
                description: The title of the reference
                nullable: true
              snippet:
                type: string
                description: The relevant snippet of the reference content
                nullable: true
              url:
                type:
                  - string
                format: uri
                description: The URL of the reference
            required:
              - title
              - snippet
              - url
          description: The references used to generate the result.
        enrichmentId:
          type:
            - string
          description: The id of the Enrichment that generated the result
      required:
        - object
        - status
        - format
        - result
        - reasoning
        - references
        - enrichmentId
    WebsetItem:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the Webset Item
        object:
          type: string
          const: webset_item
          default: webset_item
        source:
          type:
            - string
          enum:
            - search
            - import
          description: The source of the Item
        sourceId:
          type:
            - string
          description: The unique identifier for the source
        websetId:
          type:
            - string
          description: The unique identifier for the Webset this Item belongs to.
        properties:
          oneOf:
            - type:
                - object
              $ref: '#/components/schemas/WebsetItemPersonProperties'
              title: Person
            - type:
                - object
              $ref: '#/components/schemas/WebsetItemCompanyProperties'
              title: Company
            - type:
                - object
              $ref: '#/components/schemas/WebsetItemArticleProperties'
              title: Article
            - type:
                - object
              $ref: '#/components/schemas/WebsetItemResearchPaperProperties'
              title: Research Paper
            - type:
                - object
              $ref: '#/components/schemas/WebsetItemCustomProperties'
              title: Custom
          description: The properties of the Item
        evaluations:
          type:
            - array
          items:
            type:
              - object
            $ref: '#/components/schemas/WebsetItemEvaluation'
          description: The criteria evaluations of the item
        enrichments:
          type: array
          items:
            type:
              - object
            $ref: '#/components/schemas/EnrichmentResult'
          description: The enrichments results of the Webset item
          nullable: true
        createdAt:
          type:
            - string
          format: date-time
          description: The date and time the item was created
        updatedAt:
          type:
            - string
          format: date-time
          description: The date and time the item was last updated
      required:
        - id
        - object
        - source
        - sourceId
        - websetId
        - properties
        - evaluations
        - enrichments
        - createdAt
        - updatedAt
    WebsetEnrichmentFormat:
      type: string
      enum:
        - text
        - date
        - number
        - options
        - email
        - phone
        - url
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