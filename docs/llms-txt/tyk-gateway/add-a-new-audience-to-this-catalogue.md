# Source: https://tyk.io/docs/api-reference/catalogue-audiences/add-a-new-audience-to-this-catalogue.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a new audience to this catalogue

> Add a new audience to this catalogue. Please note that if the catalog's visibility is set to 'public', the audiences will be ignored

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml post /catalogues/{catalogue_id}/audiences
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
  /catalogues/{catalogue_id}/audiences:
    post:
      tags:
        - Catalogue audiences
      summary: Add a new audience to this catalogue
      description: >-
        Add a new audience to this catalogue. Please note that if the catalog's
        visibility is set to 'public', the audiences will be ignored
      operationId: create-audience
      parameters:
        - description: UID of a catalogue
          in: path
          name: catalogue_id
          required: true
          schema:
            type: integer
            example: 1
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrganisationCatalogue-create'
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrganisationCatalogue-show'
          description: OK
        '422':
          description: Not found or bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
      security:
        - AdminAPIToken: []
components:
  schemas:
    OrganisationCatalogue-create:
      properties:
        OrganisationID:
          type: integer
          description: UID of an organisation
          example: 1
        TeamID:
          type: integer
          description: UID of a team
          example: 1
      type: object
    OrganisationCatalogue-show:
      properties:
        ID:
          type: integer
          description: UID of this audience
          example: 1
        OrganisationID:
          type: integer
          description: UID of this audience
          example: 1
        TeamID:
          type: integer
          description: UID of this audience
          example: 1
        CreatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          description: Date-time when this audience is created
          example: 2023-06-23 21:02
          type: string
        UpdatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          description: Date-time when this audience is updated the last time
          example: 2023-06-23 21:02
          type: string
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
