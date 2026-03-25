# Source: https://tyk.io/docs/api-reference/access-requests/list-all-access-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all access requests

> List all access requests that exist in the portal



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /access_requests
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
  /access_requests:
    get:
      tags:
        - Access requests
      summary: List all access requests
      description: List all access requests that exist in the portal
      operationId: list-access-requests
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccessRequest-basic-index'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    AccessRequest-basic-index:
      items:
        $ref: '#/components/schemas/AccessRequest-basic-elem'
      type: array
    AccessRequest-basic-elem:
      allOf:
        - $ref: '#/components/schemas/AccessRequest-basic'
        - type: object
          properties:
            Products:
              type: string
              description: Names of products included in this access request
              example: Payment API
    AccessRequest-basic:
      allOf:
        - $ref: '#/components/schemas/AccessRequest-internal'
        - type: object
          properties:
            AuthType:
              type: string
              description: >-
                Authentication type of APIs that are included in this API
                Product
              example: authToken
            DCREnabled:
              type: boolean
              description: >-
                Identifies if this access request was created using Dynamic
                client registration
              example: false
            ID:
              type: integer
              description: UID of access request
              example: 1
            ProvisionImmediately:
              type: boolean
              description: Identifies if this access request was approved automatically
              example: true
            Status:
              enum:
                - approved
                - rejected
                - pending
              description: Approval status of this access request
    AccessRequest-internal:
      properties:
        Catalogue:
          type: string
          description: Catalogue of API Products included in this access request
          example: Public Catalogue
        Client:
          type: string
          description: Name of the developer app
          example: Payment application
        CreatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this access request was created
          example: 2023-06-25 13:37
        UpdatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this access request was updated the last time
          example: 2023-06-25 13:37
        DeletedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this access request was removed
          example: 2023-06-25 13:37
        Plan:
          type: string
          description: Name of a plan included in this access request
          example: Free plan
        User:
          type: string
          description: Descriptor of a user to whom this access request belongs
          example: User#1
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).