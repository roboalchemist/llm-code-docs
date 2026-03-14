# Source: https://tyk.io/docs/api-reference/custom-attributes/get-an-extended-model-detail.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an extended model detail

> Get an extended attribute detail



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /extended_attributes/{extended_attribute_id}
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
  /extended_attributes/{extended_attribute_id}:
    get:
      tags:
        - Custom Attributes
      summary: Get an extended model detail
      description: Get an extended attribute detail
      operationId: get-extended-attribute
      parameters:
        - description: UID of extended attribute
          in: path
          name: extended_attribute_id
          required: true
          schema:
            type: integer
            example: 1
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Extended-attributes-show'
          description: OK
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Extended-attributes-show'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    Extended-attributes-show:
      allOf:
        - $ref: '#/components/schemas/Extended-attributes-elem'
        - type: object
          properties:
            CustomAttributes:
              type: array
              description: custom attributes extended for this model
              items:
                $ref: '#/components/schemas/Custom-attribute-element'
            DefaultAttributes:
              type: array
              description: default attributes included for this model
              items:
                $ref: '#/components/schemas/Default-attribute-element'
    Extended-attributes-elem:
      properties:
        ID:
          type: integer
          description: UID of this extended attribute
          example: 1
        ModelName:
          type: string
          description: Name of the model for which the custom attributes are extended
          example: User
        LastUpdatedBy:
          type: string
          description: >-
            User that made the last update of one of the custom attributes for
            the extended model
          example: John Smith - john@tyk.io
        UpdatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of the last update
          example: 2023-06-25 13:37
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
    Default-attribute-element:
      allOf:
        - $ref: '#/components/schemas/Default-attribute-basic'
        - type: object
          properties:
            ID:
              type: integer
              description: UID of this default attribute
              example: 1
            Label:
              type: string
              description: Name of default attribute field
              example: First Name
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
    Default-attribute-basic:
      properties:
        AddToKeyMetadata:
          type: boolean
          description: >-
            If set to true the value for this default attribute will be injected
            in the credential metadata
          example: true
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).