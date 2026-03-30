# Source: https://tyk.io/docs/api-reference/products/create-a-new-product.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new product

> Create a new product (regular API product or documentation-only product)

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml post /products
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
  /products:
    post:
      tags:
        - Products
      summary: Create a new product
      description: Create a new product (regular API product or documentation-only product)
      operationId: create-product
      requestBody:
        required: true
        content:
          application/json:
            examples:
              regular-product:
                summary: Regular API Product
                value:
                  APIDetails:
                    - APIID: 3108a5fc970946ef66c1835cf73ba7a5
                      Description: This API provides payment endpoints
                      OASUrl: https://petstore.swagger.io/v2/swagger.json
                  Catalogues:
                    - 1
                  CID: 2r7p8aUnkzby17hCJk8w2XvK3K6
                  Content: <p>Description goes here</p>
                  DCREnabled: true
                  Description: Description goes here
                  DisplayName: ACME Payment API
                  Feature: true
                  IsDocumentationOnly: false
                  Name: payment_api
                  ProviderID: 1
                  Scopes: payments,clients
                  Tags:
                    - 1
                  Templates:
                    - 1
              documentation-product:
                summary: Documentation only Product
                value:
                  SpecDetails:
                    - SpecAlias: payment_api
                      OASUrl: https://petstore.swagger.io/v2/swagger.json
                  Catalogues:
                    - 1
                  CID: 2r7p8aUnkzby17hCJk8w2XvK3K6
                  Content: <p>Description goes here</p>
                  DCREnabled: true
                  Description: Description goes here
                  DisplayName: Doc only Product
                  Feature: true
                  IsDocumentationOnly: true
                  Name: doc_only
                  Tags:
                    - 1
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Product-show'
          description: Created
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Validation Error
      security:
        - AdminAPIToken: []
components:
  schemas:
    Product-show:
      type: object
      properties:
        ID:
          type: integer
          description: UID of this API Product
          example: 2
        APIDetails:
          items:
            $ref: '#/components/schemas/Product-APIDetail'
          type: array
          description: APIs included in this API Product
        AuthType:
          type: string
          description: Authentication type of APIs that are included in this API Product
          example: authToken
        Catalogues:
          type: array
          description: Catalogues in which this API Product is listed
          items:
            type: string
            description: Catalogue name
            example: Public Catalogue
        CID:
          type: string
          description: Client ID for this API Product
          example: 2r7p8aUnkzby17hCJk8w2XvK3K6
        Content:
          type: string
          description: >-
            Marketing description of an API Product formated as HTML text
            fragment
          example: <p>Description goes here</p>
        DCREnabled:
          type: boolean
          description: >-
            Defines if Dynamic Client Registration is enabled for this API
            Product
          example: true
        Description:
          type: string
          description: >-
            Short description of this API Product which is displayed in the
            Catalogue page
          example: Description goes here
        DisplayName:
          type: string
          description: >-
            Name of an API Product that is displayed in the API Product Details
            and Catalogue pages
          example: ACME Payment API
        Feature:
          type: boolean
          description: >-
            Defines if this product should be featured on the home page of the
            portal
          example: true
        IsDocumentationOnly:
          type: boolean
          default: false
          description: Must be false for regular API products
        Logo:
          type: string
          description: Path to the logo image for this API Product
          example: /system/products/2/logo/logo.png
        Name:
          type: string
          description: name of this API Product as it comes from the API Provider
          example: Payment API
        Path:
          type: string
          description: >-
            URI fragment that is specific for this product. `Path` is added to
            the catalogue path to form URI to this product:
            /portal/catalogue-products/`Path`
          example: acme-payment-api
        ReferenceID:
          type: string
          description: UID of this API Product in the API Provider
          example: 6490fd2a1ba6a6000108864d
        Scopes:
          type: string
          description: >-
            OAuth2.0 scopes that will be assigned to OAuth2.0 clients that use
            this API Product. Should be comma-separated string
          example: payments,clients
        SpecDetails:
          type: array
          description: Specification details for documentation-only products
          items:
            type: object
          nullable: true
        Tags:
          items:
            type: string
            example: payment
            description: Name of a tag
          type: array
          description: Tags assigned to this API Product
        Templates:
          items:
            type: string
            description: Name of an OAuth2.0 template
            example: Web application
          type: array
          description: OAuth2.0 templates that are assigned to this API Product
    OnlyErrors:
      properties:
        errors:
          type: array
          description: Human-readable description of the errors
          items:
            type: string
      type: object
    Product-APIDetail:
      properties:
        APIID:
          type: string
          description: API ID from the Tyk Gateway
          example: a0ce49d559ce49d64fe608ea3728082a
        APIType:
          type: string
          description: Authentication type of an API
          example: authToken
        Description:
          type: string
          description: Human-readable description of an API added by the portal admins
          example: This API provides payment endpoints
        ListenPath:
          type: string
          description: Listen path which is defined for this API in the gateway
          example: /payments/
        Name:
          type: string
          description: Name of an API as it is defined in the gateway
          example: Payment API
        OASUrl:
          type: string
          description: >-
            URL of OpenAPI Specification for this API. The document must be a
            valid OAS document
          example: https://petstore.swagger.io/v2/swagger.json
        Status:
          type: boolean
          description: >-
            Status of this API: `true` means the API is up and `false`
            identifies that it is down
          example: true
        TargetURL:
          type: string
          description: Upstream URL of this API
          example: http://httpbin.org/
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).
