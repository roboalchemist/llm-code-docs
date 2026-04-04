# Source: https://tyk.io/docs/api-reference/webhooks/list-all-webhooks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all webhooks

> Retrieves all configured webhooks.

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /webhooks
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
  /webhooks:
    get:
      tags:
        - Webhooks
      summary: List all webhooks
      description: Retrieves all configured webhooks.
      operationId: list-webhooks
      responses:
        '200':
          description: A list of webhooks.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Webhook-index'
components:
  schemas:
    Webhook-index:
      type: array
      items:
        $ref: '#/components/schemas/Webhook-index-elem'
    Webhook-index-elem:
      type: object
      properties:
        ID:
          type: string
          description: Unique identifier for the webhook
        Name:
          type: string
          description: Name of the webhook
        URL:
          type: string
          description: URL to which the webhook will send requests
        Method:
          type: string
          description: HTTP method used by the webhook (e.g., GET, POST)
        Timeout:
          type: integer
          description: Timeout in seconds for the webhook request
        Headers:
          type: array
          description: List of custom headers included in the webhook request
          items:
            $ref: '#/components/schemas/WebhookHeader'
        Events:
          type: array
          description: List of event types that trigger the webhook
          items:
            type: string
            enum:
              - AccessRequestApproved
              - AccessRequestRejected
              - AccessRequestCreated
              - OrganisationRequestCreated
              - UserRegistered
              - OrganisationRequestApproved
              - OrganisationRequestRejected
              - PasswordReset
              - RegisterInvite
              - UserAccountActivated
              - UserAccountDeactivated
              - ApplicationRegistered
              - CredentialRegistered
              - OrganisationRegistered
    WebhookHeader:
      type: object
      description: Details of a webhook header
      properties:
        ID:
          type: string
          description: Unique identifier for the header
        Name:
          type: string
          description: Name of the header
        Value:
          type: string
          description: Value of the header

````

Built with [Mintlify](https://mintlify.com).
