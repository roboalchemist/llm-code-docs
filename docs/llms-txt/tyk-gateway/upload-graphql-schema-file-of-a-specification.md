# Source: https://tyk.io/docs/api-reference/api-documentation-for-api-products/upload-graphql-schema-file-of-a-specification.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload GraphQL schema file of a Specification

> Upload a GraphQL schema file for a Specification inside a Documentation Product

## OpenAPI

````yaml swagger/5.10/enterprise-developer-portal-swagger.yaml put /products/{product_id}/spec-details/{spec-id}/graphql/schema
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
  /products/{product_id}/spec-details/{spec-id}/graphql/schema:
    put:
      tags:
        - API documentation for API Products
      summary: Upload GraphQL schema file of a Specification
      description: >-
        Upload a GraphQL schema file for a Specification inside a Documentation
        Product
      operationId: upload-spec-graphql-schema
      parameters:
        - name: product_id
          in: path
          schema:
            type: integer
          required: true
          description: UID of an API Product
        - description: ID of the Specification
          in: path
          name: spec-id
          required: true
          schema:
            type: integer
            example: 1
        - name: dry_run
          in: query
          schema:
            type: boolean
            default: false
          required: false
          description: If true, only validates the file without saving it
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                  description: >-
                    GraphQL schema file (.graphql, .gql, or .json) - only 1 file
                    at a time
      responses:
        '200':
          description: OK
        '400':
          content:
            application/json:
              schema:
                type: string
                example: >-
                  invalid file format, multiple files uploaded, or validation
                  failed
          description: >-
            Bad Request - Invalid file format, multiple files uploaded, or
            validation failed
      security:
        - AdminAPIToken: []
components:
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).
