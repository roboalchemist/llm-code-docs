# Source: https://tyk.io/docs/api-reference/plans/update-a-plan.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a plan

> Update a plan



## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml put /plans/{plan_id}
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
  /plans/{plan_id}:
    put:
      tags:
        - Plans
      summary: Update a plan
      description: Update a plan
      operationId: update-plan
      parameters:
        - description: ID of the plan
          in: path
          name: plan_id
          required: true
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PlanRequest'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Plan'
          description: OK
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Not found
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OnlyErrors'
          description: Validation error
      security:
        - AdminAPIToken: []
components:
  schemas:
    PlanRequest:
      type: object
      properties:
        CID:
          type: string
          description: Client ID for the plan
          example: 2r7p8aUnkzby17hCJk8w2XvK3K6
        AutoApproveAccessRequests:
          type: boolean
          description: Whether access requests are automatically approved
          example: true
        Catalogues:
          type: array
          description: List of catalogue IDs this plan belongs to
          items:
            type: integer
          example:
            - 1
        DisplayName:
          type: string
          description: Display name of the plan
          example: Free plan
        Description:
          type: string
          description: Description of the plan
          example: Free plan offers only basic functionality
        JWTScope:
          type: string
          description: JWT scope for the plan
          example: free-plan
        KeyExpiresIn:
          type: integer
          description: Key expiration time in seconds
          example: 3600
        MetaData:
          type: object
          description: Additional metadata for the plan
          example:
            data1: '1'
            data2: '2'
          additionalProperties: true
        Name:
          type: string
          description: Name of the plan
          example: free_plan_2
        Per:
          type: number
          description: Time period for rate limiting in seconds
          example: 10
        PlanQuota:
          type: integer
          description: Plan quota value
          example: 2
        PlanQuotaRenewalRate:
          type: integer
          description: Plan quota renewal rate in seconds
          example: 3600
        Quota:
          type: integer
          description: Quota value
          example: 0
        QuotaRenewalRate:
          type: integer
          description: Quota renewal rate in seconds
          example: -1
        RateLimit:
          type: number
          description: Rate limit for the plan
          example: 5
        UnlimitedQuota:
          type: boolean
          description: Whether the plan has unlimited quota
          example: true
        UnlimitedRateLimit:
          type: boolean
          description: Whether the plan has unlimited rate limit
          example: false
        ProviderID:
          type: integer
          description: ID of the provider
          example: 1
      required:
        - Name
        - ProviderID
    Plan:
      allOf:
        - $ref: '#/components/schemas/PlanRequest'
        - type: object
          properties:
            ID:
              type: integer
              description: Unique identifier of the plan
              example: 1
            ReferenceID:
              type: string
              description: Reference ID of the plan in the provider system
              example: 6490fd451ba6a6000108864e
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