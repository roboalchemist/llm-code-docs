# Source: https://tyk.io/docs/api-reference/tags/get-a-tag.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a tag

> Get a tag



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /tags/{tag_id}
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
  /tags/{tag_id}:
    get:
      tags:
        - Tags
      summary: Get a tag
      description: Get a tag
      operationId: get-tag
      parameters:
        - description: UID of a tag
          in: path
          name: tag_id
          required: true
          schema:
            type: integer
            example: 1
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Tag-show-tags'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    Tag-show-tags:
      type: object
      properties:
        ID:
          type: integer
          description: Unique identifier for the tag
          example: 1
        Name:
          type: string
          description: Name of the tag
          example: monetization
        Posts:
          type: array
          description: List of posts associated with this tag
          items:
            type: object
            properties:
              ID:
                type: integer
                description: Unique identifier for the post
                example: 1
              Title:
                type: string
                description: Title of the post
                example: How to write a blog post
              Lede:
                type: string
                description: Short summary or lead paragraph of the post
              Status:
                type: string
                description: Status of the post (e.g., draft, published)
                example: published
              Path:
                type: string
                description: URL path for the post
                example: ten-tips-for-gaining-advantage
              AuthorID:
                type: integer
                description: Unique identifier of the post's author
                example: 1
        Products:
          type: array
          description: List of products associated with this tag
          items:
            type: object
            properties:
              ID:
                type: integer
                description: Unique identifier for the product
                example: 1
              Name:
                type: string
                description: Name of the product
                example: public_product
              DisplayName:
                type: string
                description: Display name of the product
              Path:
                type: string
                description: URL path for the product
                example: public_product-1
              ReferenceID:
                type: string
                description: Reference ID of the product
                example: 61a89e5b5146370001de74d4
              Feature:
                type: boolean
                description: Indicates if the product is featured
                example: false
              DCREnabled:
                type: boolean
                description: >-
                  Indicates if Dynamic Client Registration is enabled for this
                  product
                example: false
              ProviderID:
                type: integer
                description: Unique identifier of the product's provider
                example: 1
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).