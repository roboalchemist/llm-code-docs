# Source: https://docs.exa.ai/websets/api/websets/items/get-an-item.md

# Get an Item

> Returns a Webset Item.

## OpenAPI

````yaml get /v0/websets/{webset}/items/{id}
paths:
  path: /v0/websets/{webset}/items/{id}
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
        webset:
          schema:
            - type: string
              required: true
              description: The id or externalId of the Webset
        id:
          schema:
            - type: string
              required: true
              description: The id of the Webset item
      query: {}
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

          const item = await exa.websets.items.get('webset_id', 'item_id');

          console.log(`Item: ${item.id} - ${item.properties.name}`);
      - label: Python
        lang: python
        source: |-
          # pip install exa-py
          from exa_py import Exa
          exa = Exa('YOUR_EXA_API_KEY')

          item = exa.websets.items.get('webset_id', 'item_id')

          print(f'Item: {item.id} - {item.properties.name}')
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
                    description: The unique identifier for the Webset Item
              object:
                allOf:
                  - type: string
                    const: webset_item
                    default: webset_item
              source:
                allOf:
                  - type:
                      - string
                    enum:
                      - search
                      - import
                    description: The source of the Item
              sourceId:
                allOf:
                  - type:
                      - string
                    description: The unique identifier for the source
              websetId:
                allOf:
                  - type:
                      - string
                    description: The unique identifier for the Webset this Item belongs to.
              properties:
                allOf:
                  - oneOf:
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
                allOf:
                  - type:
                      - array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/WebsetItemEvaluation'
                    description: The criteria evaluations of the item
              enrichments:
                allOf:
                  - type: array
                    items:
                      type:
                        - object
                      $ref: '#/components/schemas/EnrichmentResult'
                    description: The enrichments results of the Webset item
                    nullable: true
              createdAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the item was created
              updatedAt:
                allOf:
                  - type:
                      - string
                    format: date-time
                    description: The date and time the item was last updated
            refIdentifier: '#/components/schemas/WebsetItem'
            requiredProperties:
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
        examples:
          example:
            value:
              id: <string>
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
        description: Webset Item
  deprecated: false
  type: path
components:
  schemas:
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

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt