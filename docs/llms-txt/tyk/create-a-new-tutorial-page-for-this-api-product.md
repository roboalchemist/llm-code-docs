# Source: https://tyk.io/docs/api-reference/tutorials-for-api-products/create-a-new-tutorial-page-for-this-api-product.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new tutorial page for this API Product

> Create a new tutorial page for this API Product



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml post /products/{product_id}/docs
openapi: 3.1.0
info:
  title: Tyk Developer Portal
  description: >-

    <img src="https://tyk.io/docs/img/developer_portal_swagger_image.png"
    width="963" height="250">

    ## <a name="introduction"></a> Introduction

    The Tyk Enterprise Developer Portal Management API offers programmatic
    access to all portal resources that your instance of the portal manages.
    This API repeats functionality of the user interface and enables APIs
    consumers integrating their portal instances with their other IT systems
    such as billings, CRMs, ITSM systems and other software.


    ## Authentication

    This API requires an admin authorisation token that is available for admin
    users of the portal in the profile page.
  version: 1.14.0
servers:
  - url: http://localhost:3001/portal-api
security: []
tags:
  - name: Providers
    description: API Providers connected to this portal instance
  - name: Users
    description: Portal admins and API consumers
  - name: Organisations
    description: Organisation of API consumers and the portal admins
  - name: Teams
    description: Teams of API consumers and the portal admins
  - name: Products
    description: >-
      Marketing description and visibility of the API Products surfaced in this
      portal instance
  - name: Tutorials for API Products
    description: Tutorials that are defined for the API products
  - name: API documentation for API Products
    description: OpenAPI specs for APIs included into the API Prodcuts
  - name: Plans
    description: >-
      Marketing description and visibility settings of usage plans defined in
      this portal instance
  - name: Catalogues
    description: Catalogues of API Products listed on this portal instance
  - name: Catalogue audiences
    description: Audience management
  - name: Access requests
    description: Access requests to API Products
  - name: Applications and credentials
    description: Developer applications and API credential for developers
  - name: Portal configuration
    description: Show the current portal configuration
  - name: Pages and content
    description: Pages and content on the pages
  - name: Themes
    description: Management of the portal's visual themes
  - name: Custom Attributes
    description: Extend already existing models (User) by adding custom attributes
  - name: OAuth2.0 providers
    description: OAuth2.0 providers registered in the portal
  - name: Webhooks
    description: Webhooks management
  - name: Posts
    description: Posts management
  - name: SSO Profiles
    description: SSO Profiles management
  - name: Tags
    description: >-
      Tags management: link API Products to blog posts and control their
      display.
paths:
  /products/{product_id}/docs:
    post:
      tags:
        - Tutorials for API Products
      summary: Create a new tutorial page for this API Product
      description: Create a new tutorial page for this API Product
      operationId: create-docs
      parameters:
        - description: UID of an API Product
          in: path
          name: product_id
          required: true
          schema:
            type: integer
            example: 1
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Post-create'
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Post-create'
          description: OK
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    Post-create:
      properties:
        Content:
          type: string
          description: Full content of the post
          example: "# Title\r\n## Subtitle\r\nContent goes here"
        MarkdownEnabled:
          type: boolean
          description: Whether Markdown is enabled for this post
          example: true
        Status:
          enum:
            - published
            - draft
            - review
          description: Status of the post (e.g., draft, published)
          example: published
          type: string
        Title:
          type: string
          description: Title of the post
          example: Get started this API Product
        Lede:
          type: string
          description: Short summary or lead paragraph of the post
        Path:
          type: string
          description: URL path for the post
        Categories:
          type: array
          description: List of category IDs to associate with the post
          items:
            type: string
        Tags:
          type: array
          description: List of tag IDs to associate with the post
          items:
            type: string
        MarkdownContent:
          type: string
          description: Content of the post in Markdown format, if Markdown is enabled
        PreviewContent:
          type: string
          description: Preview content of the post
      type: object
    OnlyErrors:
      properties:
        errors:
          type: array
          description: Human-readable description of the errors
          items:
            type: string
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).