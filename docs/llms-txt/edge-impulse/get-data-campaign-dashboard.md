# Source: https://docs.edgeimpulse.com/apis/studio/organizationdatacampaigns/get-data-campaign-dashboard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data campaign dashboard

> Get a data campaign dashboard



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/campaign-dashboard/{campaignDashboardId}
openapi: 3.0.0
info:
  title: Edge Impulse API
  version: 1.0.0
servers:
  - url: https://studio.edgeimpulse.com/v1
security:
  - ApiKeyAuthentication: []
  - JWTAuthentication: []
  - JWTHttpHeaderAuthentication: []
  - OAuth2: []
paths:
  /api/organizations/{organizationId}/campaign-dashboard/{campaignDashboardId}:
    get:
      tags:
        - OrganizationDataCampaigns
      summary: Get data campaign dashboard
      description: Get a data campaign dashboard
      operationId: getOrganizationDataCampaignDashboard
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: >-
            #/components/parameters/OrganizationDataCampaignDashboardIdPathParameter
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/GetOrganizationDataCampaignDashboardResponse
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    OrganizationDataCampaignDashboardIdPathParameter:
      name: campaignDashboardId
      in: path
      required: true
      schema:
        type: integer
  schemas:
    GetOrganizationDataCampaignDashboardResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - dashboard
          properties:
            dashboard:
              $ref: '#/components/schemas/DataCampaignDashboard'
    GenericApiResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
          description: Whether the operation succeeded
        error:
          type: string
          description: Optional error description (set if 'success' was false)
    DataCampaignDashboard:
      type: object
      required:
        - id
        - created
        - name
        - emailRecipientUids
        - whenToEmail
        - showNoOfDays
      properties:
        id:
          type: integer
        created:
          type: string
          format: date-time
        name:
          type: string
        emailRecipientUids:
          description: List of user IDs to notify for this dashboard (sent daily)
          type: array
          items:
            type: integer
        latestScreenshot:
          type: string
        whenToEmail:
          type: string
          enum:
            - always
            - on_changes
            - never
        showNoOfDays:
          type: integer
  securitySchemes:
    ApiKeyAuthentication:
      type: apiKey
      in: header
      name: x-api-key
    JWTAuthentication:
      type: apiKey
      in: cookie
      name: jwt
    JWTHttpHeaderAuthentication:
      type: apiKey
      in: header
      name: x-jwt-token
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: /v1/oauth/authorize
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        implicit:
          authorizationUrl: /v1/oauth/authorize
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        password:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        clientCredentials:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information

````

Built with [Mintlify](https://mintlify.com).