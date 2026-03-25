# Source: https://tyk.io/docs/api-reference/teams/update-a-team-for-an-organisation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a team for an organisation

> Update a team for an organisation by adding or removing users, or changing the name of the team



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml put /organisations/{organisation_id}/teams/{team_id}
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
  /organisations/{organisation_id}/teams/{team_id}:
    put:
      tags:
        - Teams
      summary: Update a team for an organisation
      description: >-
        Update a team for an organisation by adding or removing users, or
        changing the name of the team
      operationId: update-team
      parameters:
        - description: UID of a team
          in: path
          name: team_id
          required: true
          schema:
            type: integer
            example: 2
        - description: UID of an organisation
          in: path
          name: organisation_id
          required: true
          schema:
            type: integer
            example: 2
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Team-update'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Team-show'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    Team-update:
      properties:
        Name:
          type: string
          description: Name of this team
          example: Default Organisation All users
        Users:
          items:
            type: integer
            description: UID of a user
            example: 1
          type: array
          description: UID of users included into this team
      type: object
    Team-show:
      properties:
        Name:
          type: string
          description: Name of this team
          example: Default Organisation All users
        ID:
          type: integer
          description: UID of this team
          example: 11
        CreatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          description: Date-time when a team is created
          example: 2023-06-23 21:02
          type: string
        UpdatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          description: Date-time when a team was updated the last time
          example: 2023-06-23 21:02
          type: string
        Users:
          items:
            type: string
            example: User#6
            description: User ID
          type: array
          description: >-
            Users included in this organisation. For newly created organisation
            will an empty array
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).