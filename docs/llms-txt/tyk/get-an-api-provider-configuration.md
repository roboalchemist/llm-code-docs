# Source: https://tyk.io/docs/api-reference/providers/get-an-api-provider-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an API Provider configuration

> Get an API Provider configuration



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /providers/{provider_id}
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
  /providers/{provider_id}:
    get:
      tags:
        - Providers
      summary: Get an API Provider configuration
      description: Get an API Provider configuration
      operationId: get-provider
      parameters:
        - description: UID of an API provider
          in: path
          name: provider_id
          required: true
          schema:
            type: integer
            example: 1
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Provider-show'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    Provider-show:
      allOf:
        - $ref: '#/components/schemas/Provider-index-elem'
        - type: object
          properties:
            Configuration:
              $ref: '#/components/schemas/ProviderConfig'
            UpdatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              type: string
              description: When this API Provider was updated the last time
              example: 2023-06-23 19:13
            CreatedAt:
              pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
              type: string
              description: When this API Provider was created
              example: 2023-06-23 19:13
    Provider-index-elem:
      properties:
        LastSyncedAt:
          type: string
          description: The last time this provider was synchronized with the portal
          example: 7 minutes 5 seconds ago
        ID:
          type: integer
          description: UUID of this API provider in the portal's database
          example: 1
        Name:
          type: string
          description: Name of this API Provider
          example: Tyk Dashboard
        Status:
          type: string
          description: Identifies if this API Provider is Up and ready for synchronization
          example: Up
        Type:
          type: string
          description: Type of API gateway used by this API Provider e.g. Tyk or AWS
          example: tyk-pro
      type: object
    ProviderConfig:
      properties:
        MetaData:
          type: string
          description: Connection settings for this API Provider
          example: >-
            {"URL":"http://localhost:3002","Secret":"04d31017802f482f76414a372db30fc2","OrgID":"5e9d9544a1dcd60001d0ed20","Gateway":"","PoliciesTags":[],"InsecureSkipVerify":false}
        ID:
          type: integer
          description: UID of an API provider's metadata
          example: 1
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).