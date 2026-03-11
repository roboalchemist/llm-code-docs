# Source: https://tyk.io/docs/api-reference/custom-attributes/update-a-custom-attribute.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a custom attribute

> Update a custom attribute for a particular extended model

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml put /extended_attributes/{extended_attribute_id}/custom-attributes/{custom_attribute_id}
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
  /extended_attributes/{extended_attribute_id}/custom-attributes/{custom_attribute_id}:
    put:
      tags:
        - Custom Attributes
      summary: Update a custom attribute
      description: Update a custom attribute for a particular extended model
      operationId: update-custom-attribute
      parameters:
        - description: UID of the extended attribute
          in: path
          name: extended_attribute_id
          required: true
          schema:
            type: integer
            example: 1
        - description: UID of the custom attribute
          in: path
          name: custom_attribute_id
          required: true
          schema:
            type: integer
            example: 1
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Custom-attribute-basic'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Custom-attribute-element'
          description: OK
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Bad request or Not found
      security:
        - AdminAPIToken: []
components:
  schemas:
    Custom-attribute-basic:
      properties:
        Name:
          type: string
          description: Label for custom attribute
          example: Terms of use
        Identifier:
          type: string
          description: Unique string identifier for custom attribute
          example: terms-of-use
        Description:
          type: string
          description: Description for custom attribute
          example: I have read and agreed with...
        Behaviour:
          type: integer
          enum:
            - 1
            - 2
            - 3
          description: >-
            custom attribute behaviour: 1 -> Developers can view and edit the
            attribute, 2 -> Developers can only view the attribute, 3 ->
            Developers cannot see the attribute
          example: 3
        DropdownValues:
          type: string
          description: Values to display in dropdown options if the attribute type is 2
          example: Fleet_management,Cities,EV_management
        ValidationRegExp:
          type: string
          description: Validation to be applied for string type attributes (type 1)
          example: www\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+
        AddToKeyMetadata:
          type: boolean
          description: >-
            Defines if the value of this custom attribute should be injected
            into the credential's metadata
          example: true
        Required:
          type: boolean
          description: >-
            Defines if the value of this custom attribute is required to create
            a new object
          example: true
        ShowOnSignUp:
          type: boolean
          description: >-
            Defines if this custom attribute should be displayed in the sign up
            form
          example: true
        WriteOnceReadMany:
          type: boolean
          description: If set to true the value is set only once for the first time
          example: true
      type: object
    Custom-attribute-element:
      allOf:
        - $ref: '#/components/schemas/Custom-attribute-basic'
        - type: object
          properties:
            ID:
              type: integer
              description: UID of this custom attribute
              example: 1
            Type:
              type: integer
              enum:
                - 1
                - 2
                - 3
                - 4
              description: >-
                custom attribute type: 1 -> String, 2 -> Dropdown, 3 -> Boolean,
                4 -> Number
              example: 2
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
