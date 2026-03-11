# Source: https://tyk.io/docs/api-reference/posts/get-a-post-by-id.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a post by ID

> Get a specific post by its ID.

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /posts/{post_id}
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
  /posts/{post_id}:
    get:
      tags:
        - Posts
      summary: Get a post by ID
      description: Get a specific post by its ID.
      operationId: get-post
      parameters:
        - name: post_id
          in: path
          required: true
          schema:
            type: integer
            example: 1
          description: UID of a post
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Post-show'
      security:
        - AdminAPIToken: []
components:
  schemas:
    Post-show:
      type: object
      properties:
        ID:
          type: string
          description: Unique identifier for the post
        Title:
          type: string
          description: Title of the post
        Lede:
          type: string
          description: Short summary or lead paragraph of the post
        Content:
          type: string
          description: Full content of the post
        Status:
          type: string
          description: Status of the post (e.g., draft, published)
        Path:
          type: string
          description: URL path for the post
        Categories:
          type: array
          description: List of categories associated with the post
          items:
            $ref: '#/components/schemas/Category-show'
        Tags:
          type: array
          description: List of tags associated with the post
          items:
            $ref: '#/components/schemas/Tag-show'
        MarkdownEnabled:
          type: boolean
          description: Whether Markdown is enabled for this post
        MarkdownContent:
          type: string
          description: Content of the post in Markdown format, if Markdown is enabled
        PreviewContent:
          type: string
          description: Preview content of the post
        CreatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this post was created
          example: 2023-06-25 13:37
        UpdatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this post was last updated
          example: 2023-06-25 13:37
    Category-show:
      type: object
      properties:
        ID:
          type: string
          description: Unique identifier for the category
        Name:
          type: string
          description: Name of the category
        CreatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this category was created
          example: 2023-06-25 13:37
        UpdatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this category was last updated
          example: 2023-06-25 13:37
    Tag-show:
      type: object
      properties:
        ID:
          type: string
          description: Unique identifier for the tag
        Name:
          type: string
          description: Name of the tag
        CreatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this tag was created
          example: 2023-06-25 13:37
        UpdatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this tag was last updated
          example: 2023-06-25 13:37
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).
