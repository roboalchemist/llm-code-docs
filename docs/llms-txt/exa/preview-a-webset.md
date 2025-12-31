# Source: https://docs.exa.ai/websets/api/websets/preview-a-webset.md

# Preview a webset

> Preview how a search query will be decomposed before creating a webset. This endpoint performs the same query analysis that happens during webset creation, allowing you to see the detected entity type, generated search criteria, and available enrichment columns in advance.

Use this to help users understand how their search will be interpreted before committing to a full webset creation.

## OpenAPI

````yaml post /v0/websets/preview
paths:
  path: /v0/websets/preview
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
        search:
          schema:
            - type: boolean
              required: true
              description: Weather you want to search for a preview list of items or not
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              search:
                allOf:
                  - type:
                      - object
                    properties:
                      query:
                        type:
                          - string
                        minLength: 1
                        maxLength: 5000
                        description: >-
                          Natural language search query describing what you are
                          looking for.


                          Be specific and descriptive about your requirements,
                          characteristics, and any constraints that help narrow
                          down the results.
                        examples:
                          - >-
                            Marketing agencies based in the US, that focus on
                            consumer products. Get brands worked with and city
                          - >-
                            AI startups in Europe that raised Series A funding
                            in 2024
                          - >-
                            SaaS companies with 50-200 employees in the fintech
                            space
                      entity:
                        $ref: '#/components/schemas/Entity'
                        description: >-
                          Entity used to inform the decomposition.


                          It is not required to provide it, we automatically
                          detect the entity from all the information provided in
                          the query. Only use this when you need more fine
                          control.
                      count:
                        default: 10
                        type:
                          - number
                        minimum: 1
                        maximum: 10
                        description: >-
                          When query parameter search=true, the number of
                          preview items to return.
                    required:
                      - query
            required: true
            refIdentifier: '#/components/schemas/PreviewWebsetParameters'
            requiredProperties:
              - search
        examples:
          example:
            value:
              search:
                query: >-
                  Marketing agencies based in the US, that focus on consumer
                  products. Get brands worked with and city
                entity:
                  type: company
                count: 10
        description: Search parameters
    codeSamples:
      - label: JavaScript
        lang: javascript
        source: |-
          // npm install exa-js
          import Exa from 'exa-js';
          const exa = new Exa('YOUR_EXA_API_KEY');

          const preview = await exa.websets.preview({
            search: {
              query:
                'Marketing agencies based in the US, that focus on consumer products. Get brands worked with and city',
            },
          });

          console.log('Search criteria:', preview.search.criteria);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          preview = exa.websets.preview(params={
              'query': 'Marketing agencies based in the US, that focus on consumer products. Get brands worked with and city'
          })

          print('Search criteria:', preview.search.criteria)
          print('Available enrichments:', len(preview.enrichments))
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              search:
                allOf:
                  - type:
                      - object
                    properties:
                      entity:
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
                        description: Detected entity from the query.
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
                          required:
                            - description
                        description: Detected criteria from the query.
                    required:
                      - entity
                      - criteria
              enrichments:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      properties:
                        description:
                          type:
                            - string
                          description: Description of the enrichment.
                        format:
                          type:
                            - string
                          enum:
                            - text
                            - date
                            - number
                            - options
                            - email
                            - phone
                            - url
                          description: Format of the enrichment.
                        options:
                          type:
                            - array
                          items:
                            type:
                              - object
                            properties:
                              label:
                                type:
                                  - string
                                description: Label of the option.
                            required:
                              - label
                          description: >-
                            When format is options, the options detected from
                            the query.
                      required:
                        - description
                        - format
                    description: Detected enrichments from the query.
              items:
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/WebsetItemPreview'
                    description: Preview items matching the search criteria.
            refIdentifier: '#/components/schemas/PreviewWebsetResponse'
            requiredProperties:
              - search
              - enrichments
              - items
        examples:
          example:
            value:
              search:
                entity:
                  type: company
                criteria:
                  - description: <string>
              enrichments:
                - description: <string>
                  format: text
                  options:
                    - label: <string>
              items:
                - id: <string>
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
                  createdAt: '2023-11-07T05:31:56Z'
        description: Preview of the webset
    '422':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unable to detect entity or criteria from query
        examples: {}
        description: Unable to detect entity or criteria from query
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
    WebsetItemPreview:
      type:
        - object
      properties:
        id:
          type:
            - string
          description: The unique identifier for the preview item
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
          description: The properties of the preview item
        createdAt:
          type:
            - string
          format: date-time
          description: The date and time the preview was created
      required:
        - id
        - properties
        - createdAt

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt