# Source: https://tyk.io/docs/api-reference/pages-and-content/list-all-content-blocks-which-are-displayed-on-this-page.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all content blocks which are displayed on this page

> List all content blocks which are displayed on this page

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /pages/{page_id}/content-blocks
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
  /pages/{page_id}/content-blocks:
    get:
      tags:
        - Pages and content
      summary: List all content blocks which are displayed on this page
      description: List all content blocks which are displayed on this page
      operationId: list-content-blocks
      parameters:
        - description: UID of the page
          in: path
          name: page_id
          required: true
          schema:
            type: integer
            example: 1
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ContentBlock-index'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    ContentBlock-index:
      items:
        $ref: '#/components/schemas/ContentBlock-index-elem'
      type: array
    ContentBlock-index-elem:
      allOf:
        - $ref: '#/components/schemas/ContentBlock-basic'
        - type: object
          properties:
            ID:
              description: UID of the content block
              type: integer
              example: 1
            PageID:
              type: integer
              description: UID of a page where the content block belong
              example: 1
    ContentBlock-basic:
      properties:
        Content:
          type: string
          description: Content of this content block
          example: "<p>Everything would be better connected, but the internet is messy, imperfect and unpredictable.</p>\n\t\t\t\t<p>Our engineers are dedicated to making it simple, fast and affordable to connect every system in the world.</p>\n\t\t\t\t<p>We ensure you can trust our systems to look after yours.</p>"
        Name:
          type: string
          description: >-
            Name of the content block. In order to succeesfully render this
            page, `name` should with a reference in the template for this page.
            For instance, HeaderDescription will be rendered in {{safe
            .blocks.HeaderDescription.Content}} section of the template
          example: HeaderDescription
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).
