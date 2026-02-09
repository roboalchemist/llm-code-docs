# Source: https://exa.ai/docs/websets/api/websets/preview-a-webset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Preview a webset

> Preview how a search query will be decomposed before creating a webset. This endpoint performs the same query analysis that happens during webset creation, allowing you to see the detected entity type, generated search criteria, and available enrichment columns in advance.

Use this to help users understand how their search will be interpreted before committing to a full webset creation.



## OpenAPI

````yaml post /v0/websets/preview
openapi: 3.1.0
info:
  title: Websets
  description: ''
  version: '0'
  contact: {}
servers:
  - url: https://api.exa.ai/websets/
    description: Production
security: []
tags: []
paths:
  /v0/websets/preview:
    post:
      tags:
        - Websets Preview
      summary: Preview a webset
      description: >-
        Preview how a search query will be decomposed before creating a webset.
        This endpoint performs the same query analysis that happens during
        webset creation, allowing you to see the detected entity type, generated
        search criteria, and available enrichment columns in advance.


        Use this to help users understand how their search will be interpreted
        before committing to a full webset creation.
      operationId: websets-preview
      parameters:
        - name: search
          required: false
          in: path
          description: Weather you want to search for a preview list of items or not
          schema:
            type: boolean
      requestBody:
        required: true
        description: Search parameters
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PreviewWebsetParameters'
      responses:
        '200':
          description: Preview of the webset
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PreviewWebsetResponse'
          headers:
            X-Request-Id:
              schema:
                type: string
              description: Unique identifier for the request.
              example: req_N6SsgoiaOQOPqsYKKiw5
              required: true
        '422':
          description: Unable to detect entity or criteria from query
          headers:
            X-Request-Id:
              schema:
                type: string
              description: Unique identifier for the request.
              example: req_N6SsgoiaOQOPqsYKKiw5
              required: true
      security:
        - api_key: []
components:
  schemas:
    PreviewWebsetParameters:
      type:
        - object
      properties:
        search:
          type:
            - object
          properties:
            query:
              type:
                - string
              minLength: 1
              maxLength: 5000
              description: >-
                Natural language search query describing what you are looking
                for.


                Be specific and descriptive about your requirements,
                characteristics, and any constraints that help narrow down the
                results.
              examples:
                - >-
                  Marketing agencies based in the US, that focus on consumer
                  products. Get brands worked with and city
                - AI startups in Europe that raised Series A funding in 2024
                - SaaS companies with 50-200 employees in the fintech space
            entity:
              $ref: '#/components/schemas/Entity'
              description: >-
                Entity used to inform the decomposition.


                It is not required to provide it, we automatically detect the
                entity from all the information provided in the query. Only use
                this when you need more fine control.
            count:
              default: 10
              type:
                - number
              minimum: 1
              maximum: 10
              description: >-
                When query parameter search=true, the number of preview items to
                return.
          required:
            - query
      required:
        - search
    PreviewWebsetResponse:
      type:
        - object
      properties:
        search:
          type:
            - object
          properties:
            entity:
              oneOf:
                - $ref: '#/components/schemas/CompanyEntity'
                  type:
                    - object
                - $ref: '#/components/schemas/PersonEntity'
                  type:
                    - object
                - $ref: '#/components/schemas/ArticleEntity'
                  type:
                    - object
                - $ref: '#/components/schemas/ResearchPaperEntity'
                  type:
                    - object
                - $ref: '#/components/schemas/CustomEntity'
                  type:
                    - object
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
          type:
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
                description: When format is options, the options detected from the query.
            required:
              - description
              - format
          description: Detected enrichments from the query.
        items:
          type:
            - array
          items:
            $ref: '#/components/schemas/WebsetItemPreview'
            type:
              - object
          description: Preview items matching the search criteria.
      required:
        - search
        - enrichments
        - items
    Entity:
      oneOf:
        - $ref: '#/components/schemas/CompanyEntity'
          type:
            - object
        - $ref: '#/components/schemas/PersonEntity'
          type:
            - object
        - $ref: '#/components/schemas/ArticleEntity'
          type:
            - object
        - $ref: '#/components/schemas/ResearchPaperEntity'
          type:
            - object
        - $ref: '#/components/schemas/CustomEntity'
          type:
            - object
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
            - $ref: '#/components/schemas/WebsetItemPersonProperties'
              type:
                - object
              title: Person
            - $ref: '#/components/schemas/WebsetItemCompanyProperties'
              type:
                - object
              title: Company
            - $ref: '#/components/schemas/WebsetItemArticleProperties'
              type:
                - object
              title: Article
            - $ref: '#/components/schemas/WebsetItemResearchPaperProperties'
              type:
                - object
              title: Research Paper
            - $ref: '#/components/schemas/WebsetItemCustomProperties'
              type:
                - object
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
  securitySchemes:
    api_key:
      type: apiKey
      in: header
      name: x-api-key
      description: Your Exa API key

````