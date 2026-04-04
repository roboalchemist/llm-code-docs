# Source: https://tyk.io/docs/api-reference/plans/list-all-plans.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all plans

> List all plans that exist in the portal



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /plans
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
  /plans:
    get:
      tags:
        - Plans
      summary: List all plans
      description: List all plans that exist in the portal
      operationId: list-plans
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan-index'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    Plan-index:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/PlanSummary'
    PlanSummary:
      type: object
      properties:
        ID:
          type: integer
          description: Unique identifier of the plan
          example: 1
        Name:
          type: string
          description: Name of the plan
          example: free_plan_2
        DisplayName:
          type: string
          description: Display name of the plan
          example: Free plan
        AutoApproveAccessRequests:
          type: boolean
          description: Whether access requests are automatically approved
          example: true
        RateLimit:
          type: number
          description: Rate limit for the plan
          example: 5
        Quota:
          type: integer
          description: Quota for the plan
          example: 0
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).