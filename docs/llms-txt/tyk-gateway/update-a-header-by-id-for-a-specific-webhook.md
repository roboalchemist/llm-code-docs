# Source: https://tyk.io/docs/api-reference/webhooks/update-a-header-by-id-for-a-specific-webhook.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a header by ID for a specific webhook

> Updates an existing header in a webhook.

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml put /webhooks/{webhook_id}/headers/{header_id}
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
  /webhooks/{webhook_id}/headers/{header_id}:
    put:
      tags:
        - Webhooks
      summary: Update a header by ID for a specific webhook
      description: Updates an existing header in a webhook.
      operationId: update-webhook-header
      parameters:
        - name: webhook_id
          in: path
          required: true
          schema:
            type: string
        - name: header_id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        description: Header object that needs to be updated
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WebhookHeader-update'
      responses:
        '200':
          description: Header updated successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WebhookHeader-update'
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Bad request
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Validation error
components:
  schemas:
    WebhookHeader-update:
      type: object
      description: Details of a webhook header
      properties:
        Name:
          type: string
          description: Name of the header
        Value:
          type: string
          description: Value of the header
    OnlyErrors:
      properties:
        errors:
          type: array
          description: Human-readable description of the errors
          items:
            type: string
      type: object

````

Built with [Mintlify](https://mintlify.com).
