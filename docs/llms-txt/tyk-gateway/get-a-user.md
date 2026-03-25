# Source: https://tyk.io/docs/api-reference/users/get-a-user.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a user

> Get a user

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /users/{user_id}
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
  /users/{user_id}:
    get:
      tags:
        - Users
      summary: Get a user
      description: Get a user
      operationId: get-user
      parameters:
        - description: UID of a user
          in: path
          name: user_id
          required: true
          schema:
            type: integer
            example: 1
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User-show'
          description: OK
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User-show'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    User-show:
      allOf:
        - $ref: '#/components/schemas/User-basis'
        - type: object
          properties:
            JWTToken:
              type: string
              description: >-
                API access credentials to the admin APIs that are described in
                this spectification
              example: >-
                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJQcm92aWRlciI6Im5vbmUiLCJVc2VySUQiOiIkMmEkMTAkMFhRUEtCSC9nenFWMVhnRkRzUWViLk90bmdzVVlsQk9VSE14T045bWZveEs3ek9zSzVKLnkifQ.SHZtWNA-sYHUwSLEkWFo1r049WBWcQJVco_WH21jXHs
            APITokenCreatedAt:
              pattern: ^\d{4}-\d{2}-\d{2}$
              description: Date-time when the `JWTToken` is created
              example: '2023-06-23'
              type: string
            Organisation:
              type: string
              description: Name of an rganisation where this user belongs to
              example: Default Organisation
            ResetPassword:
              type: boolean
              description: >-
                Determines if a user must change their password at the next
                login
              example: false
            Teams:
              items:
                type: string
                description: Name of this user's teams
                example: Default Organisation All users
              type: array
            ID:
              type: integer
              description: UID of a user
              example: 1
            CreatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              description: Date-time when a user is created
              example: 2023-06-23 21:02
              type: string
            UpdatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              description: Date-time when a user is updated the last time
              example: 2023-06-23 21:02
              type: string
    User-basis:
      type: object
      properties:
        Active:
          description: Defines if this user is active and can login to the portal
          type: boolean
          example: true
        Email:
          description: Email of a user
          type: string
          example: admin@acme.com
        First:
          type: string
          description: First name of a user
          example: John
        Last:
          type: string
          description: Last name of a user
          example: Doe
        OrganisationID:
          type: integer
          description: >-
            ID of an organisation where this user belongs to. For admin users it
            is always equal to 0
          example: 1
        Role:
          type: string
          description: Role of a user in their organisation
          example: consumer-team-member
        Provider:
          type: string
          description: Type of identity provider for this user, e.g. password, github, etc.
          example: password
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).
