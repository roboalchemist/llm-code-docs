# Source: https://docs.zapier.com/powered-by-zapier/api-reference/categories/get-categories.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Categories

> List of Zap categories

This API is [rate limited](/powered-by-zapier/api-reference/rate-limiting).


## OpenAPI

````yaml https://api.zapier.com/schema get /v1/categories
openapi: 3.1.0
info:
  title: Partner API
  version: 2024.11.0
  description: >

    ## Introduction


    The Partner API is the best tool for complete style control over a user's
    Zapier experience within your app.

    Essentially, it lets you customize how you present Zapier within your
    product without sacrificing your app's look,

    feel, and flow.


    Think of it as a native Zapier integration, helping you showcase your best
    Zapier-powered workflows where it's most

    helpful to your users (within the flow of your tool). You can customize
    styling, streamline Zap set-up for users,

    expose relevant Zap information, and more!


    With the Partner API, you can:


    - Get a list of all the apps available in Zapier's app directory so you can
    power your app directory and show your

    users all the integration possibilities with your Zapier integration.

    - Have complete style control over how you present Zap templates in your
    product. The Partner API gives you access

    to the raw Zap Template data so you can give your users access to your Zap
    template with your product's style, look

    and feel.

    - Get access to all your Zap templates and give your users the ability to
    search to quickly find the one they need.

    - Streamline Zap setup by pre-filling fields on behalf of your users.

    - Show users the Zaps they have set up from right within your product
    keeping them on your site longer and giving them

    complete confidence in their Zapier integration.

    - Embed our Zapier Editor to allow your users to create new Zaps and modify
    existing ones, without needing to leave

    your product.


    ## Authentication


    There are two ways to authenticate with the Partner API.


    1. Your application's `client_id` which you will receive once you are
    approved for access to the API

    (Client ID Authentication)

    2. A user's access token (Access Token Authentication).


    Which authentication method you should use depends on which endpoint(s) you
    are using.

    Review each endpoint's documentation to understand which parameters are
    required.


    > Note: while we do generate a `client_secret`, the type of grant we use
    (implicit) doesn't

    need it so it's not something we provide.'


    ## Learn more


    See the [Workflow API
    documentation](https://docs.zapier.com/partner-solutions/workflow-api/intro)
    for more information.
  contact:
    name: Zapier
    url: https://developer.zapier.com/contact
servers:
  - url: https://api.zapier.com
security: []
tags:
  - name: Accounts
    description: Refers to resources interacting with 'Accounts' associated resources
  - name: Actions
    description: Refers to resources interacting with 'Actions' associated resources
  - name: Apps
    description: Refers to resources interacting with 'Apps' associated resources
  - name: Authentications
    description: >-
      Refers to resources interacting with 'Authentications' associated
      resources
  - name: Categories
    description: Refers to resources interacting with 'Categories' associated resources
  - name: Experimental
    description: Refers to resources interacting with 'Experimental' associated resources
  - name: Inputs
    description: Refers to resources interacting with 'Inputs' associated resources
  - name: Outputs
    description: Refers to resources interacting with 'Outputs' associated resources
  - name: Zaps
    description: Refers to resources interacting with 'Zaps' associated resources
  - name: Zap Templates
    description: Refers to resources interacting with 'Zap Templates' associated resources
paths:
  /v1/categories:
    get:
      tags:
        - Categories
      summary: Get Categories
      description: List of Zap categories
      operationId: v1_categories_list
      parameters:
        - in: query
          name: limit
          schema:
            type: number
            default: 10
          description: Limit the number of Zap categories returned.
        - in: query
          name: offset
          schema:
            type: number
            default: 0
          description: >-
            The number of Zap categories to skip over. The default value is 0,
            which is the offset of the first item.
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/CategoriesResponse'
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
                            Unlock the potential of artificial intelligence in
                            your workflow with these AI integrations. These apps
                            use AI to tackle everything from natural language
                            processing to image classification, providing you
                            with unparalleled automation power.
                          url: >-
                            https://zapier.com/api/v4/app-directory/categories/ai-tools/
                          type_of: curated
                          featured_entry_slug: null
                          role: parent
                        - id: 97
                          title: All
                          slug: all
                          description: Contains all the services.
                          url: >-
                            https://zapier.com/api/v4/app-directory/categories/all/
                          type_of: auto
                          featured_entry_slug: null
                          role: parent
                        - id: 37
                          title: Amazon
                          slug: aws
                          description: >-
                            Tools from Amazon to host and manage sites and
                            applications on the Amazon cloud.
                          url: >-
                            https://zapier.com/api/v4/app-directory/categories/aws/
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
                          description: >-
                            Tools to build a custom app with forms and
                            databases.
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
                            Unlock the potential of artificial intelligence in
                            your workflow with these AI integrations. These apps
                            use AI to tackle everything from natural language
                            processing to image classification, providing you
                            with unparalleled automation power.
                          url: >-
                            https://zapier.com/api/v4/app-directory/categories/artificial-intelligence/
                          type_of: curated
                          featured_entry_slug: null
                          role: parent
                        - id: 46
                          title: Beta
                          slug: beta
                          description: Beta services.
                          url: >-
                            https://zapier.com/api/v4/app-directory/categories/beta/
                          type_of: auto
                          featured_entry_slug: null
                          role: child
          description: ''
        '401':
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 401 Response
        '403':
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 403 Response
        '409':
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 409 Response
        '429':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 429 Response
        '503':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 503 Response
        '504':
          content:
            application/json:
              schema:
                type: object
                additionalProperties: {}
          description: 504 Response
components:
  schemas:
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

````