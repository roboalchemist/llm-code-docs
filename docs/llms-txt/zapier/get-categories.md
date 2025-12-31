# Source: https://docs.zapier.com/powered-by-zapier/api-reference/categories/get-categories.md

# Get Categories

> List of Zap categories

## OpenAPI

````yaml https://api.zapier.com/schema get /v1/categories
paths:
  path: /v1/categories
  method: get
  servers:
    - url: https://api.zapier.com
  request:
    security: []
    parameters:
      path: {}
      query:
        limit:
          schema:
            - type: number
              description: Limit the number of Zap categories returned.
              default: 10
        offset:
          schema:
            - type: number
              description: >-
                The number of Zap categories to skip over. The default value is
                0, which is the offset of the first item.
              default: 0
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/CategoriesResponse'
        examples:
          /v1/categories:
            value:
              - next: https://api.zapier.com/v1/categories?offset=10&limit=10
                previous: null
                count: 90
                objects:
                  - id: 78
                    title: Ads & Conversion
                    slug: ads-conversion
                    description: Tools to track and reach an audience online.
                    url: >-
                      https://zapier.com/api/v4/app-directory/categories/ads-conversion/
                    type_of: curated
                    featured_entry_slug: boost-google-ads-ROI-with-zapier
                    role: child
                  - id: 1
                    title: Accounting
                    slug: accounting
                    description: Tools for accounting and finance.
                    url: >-
                      https://zapier.com/api/v4/app-directory/categories/accounting/
                    type_of: curated
                    featured_entry_slug: favorite-zaps-accounting
                    role: child
                  - id: 14
                    title: AI Tools
                    slug: ai-tools
                    description: >-
                      Unlock the potential of artificial intelligence in your
                      workflow with these AI integrations. These apps use AI to
                      tackle everything from natural language processing to
                      image classification, providing you with unparalleled
                      automation power.
                    url: >-
                      https://zapier.com/api/v4/app-directory/categories/ai-tools/
                    type_of: curated
                    featured_entry_slug: null
                    role: parent
                  - id: 97
                    title: All
                    slug: all
                    description: Contains all the services.
                    url: https://zapier.com/api/v4/app-directory/categories/all/
                    type_of: auto
                    featured_entry_slug: null
                    role: parent
                  - id: 37
                    title: Amazon
                    slug: aws
                    description: >-
                      Tools from Amazon to host and manage sites and
                      applications on the Amazon cloud.
                    url: https://zapier.com/api/v4/app-directory/categories/aws/
                    type_of: curated
                    featured_entry_slug: what-you-should-automate
                    role: child
                  - id: 84
                    title: Analytics
                    slug: analytics
                    description: Tools to measure and report on success
                    url: >-
                      https://zapier.com/api/v4/app-directory/categories/analytics/
                    type_of: curated
                    featured_entry_slug: automate-analytics-tools
                    role: child
                  - id: 21
                    title: App Builder
                    slug: app-builder
                    description: Tools to build a custom app with forms and databases.
                    url: >-
                      https://zapier.com/api/v4/app-directory/categories/app-builder/
                    type_of: curated
                    featured_entry_slug: null
                    role: child
                  - id: 35
                    title: App Families
                    slug: app-families
                    description: ''
                    url: >-
                      https://zapier.com/api/v4/app-directory/categories/app-families/
                    type_of: curated
                    featured_entry_slug: null
                    role: parent
                  - id: 155
                    title: Artificial Intelligence
                    slug: artificial-intelligence
                    description: >-
                      Unlock the potential of artificial intelligence in your
                      workflow with these AI integrations. These apps use AI to
                      tackle everything from natural language processing to
                      image classification, providing you with unparalleled
                      automation power.
                    url: >-
                      https://zapier.com/api/v4/app-directory/categories/artificial-intelligence/
                    type_of: curated
                    featured_entry_slug: null
                    role: parent
                  - id: 46
                    title: Beta
                    slug: beta
                    description: Beta services.
                    url: https://zapier.com/api/v4/app-directory/categories/beta/
                    type_of: auto
                    featured_entry_slug: null
                    role: child
        description: ''
    '401':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 401 Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 403 Response
    '409':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 409 Response
    '429':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 429 Response
    '503':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 503 Response
  deprecated: false
  type: path
components:
  schemas:
    AppCategory:
      type: object
      description: Category an app belongs to.
      properties:
        id:
          type: integer
          description: The unique ID for this Category
        title:
          type: string
          description: The title of this Category
        slug:
          type: string
          description: The shortened slug for this Category
        description:
          type: string
          description: The description of this Categeory
        url:
          type: string
          description: The URL for this Category
        type_of:
          type: string
          description: The type of this Category
        featured_entry_slug:
          type:
            - string
            - 'null'
          description: The featured entry for this Category (if present)
        role:
          type: string
          description: This Category's role
      required:
        - description
        - featured_entry_slug
        - id
        - role
        - slug
        - title
        - type_of
        - url
    CategoriesResponse:
      type: object
      description: A page of returned Categories.
      properties:
        next:
          type:
            - string
            - 'null'
          format: uri
          readOnly: true
          description: The URL to call to get the next set of Categories
        previous:
          type:
            - string
            - 'null'
          format: uri
          readOnly: true
          description: The URL to call to get the prior set of Categories
        count:
          type: integer
          description: How many Categories exist for the given query
        objects:
          type: array
          items:
            $ref: '#/components/schemas/AppCategory'
          description: The list of matching Category data
      required:
        - count
        - next
        - objects
        - previous

````