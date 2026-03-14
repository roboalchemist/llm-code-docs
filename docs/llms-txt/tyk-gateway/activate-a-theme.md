# Source: https://tyk.io/docs/api-reference/themes/activate-a-theme.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Activate a theme

> Activate a theme. When a new theme is activated, it becomes the current theme for the live portal and is displayed to all developers visiting the portal

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml put /themes/{theme_id}/activate
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
  /themes/{theme_id}/activate:
    put:
      tags:
        - Themes
      summary: Activate a theme
      description: >-
        Activate a theme. When a new theme is activated, it becomes the current
        theme for the live portal and is displayed to all developers visiting
        the portal
      operationId: activate-theme
      parameters:
        - description: '`name` of the theme from the theme.json file'
          in: path
          name: theme_id
          required: true
          schema:
            type: string
            example: default
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusWithMessage'
          description: OK
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusWithErrors'
          description: Not found or issues were encountered activating the theme
      security:
        - AdminAPIToken: []
components:
  schemas:
    StatusWithMessage:
      properties:
        status:
          type: string
          description: Status of the operation
          example: ok
        message:
          type: string
          description: Human-readable description of the status
          example: 'Action Synchronize: Executed successfully'
      type: object
    StatusWithErrors:
      properties:
        status:
          type: string
          description: Status of the operation
          example: error
        errors:
          type: array
          description: Human-readable description of the errors
          items:
            type: string
            example: >-
              Failed to sync provider Tyk Dashboard (Edit Me): TykPro.Sync.
              getting available products: fetching policies: Get
              "http://localhost:30023/api/portal/policies/?p=-2": dial tcp
              [::1]:30023: connect: connection refused
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).
