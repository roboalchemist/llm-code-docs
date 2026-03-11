# Source: https://docs.edgeimpulse.com/apis/studio/organizationdatacampaigns/add-a-data-campaign.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a data campaign

> Add a new data campaign to a data campaign dashboard



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/campaigns
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
  /api/organizations/{organizationId}/campaigns:
    post:
      tags:
        - OrganizationDataCampaigns
      summary: Add a data campaign
      description: Add a new data campaign to a data campaign dashboard
      operationId: addOrganizationDataCampaign
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddOrganizationDataCampaignRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AddOrganizationDataCampaignResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
  schemas:
    AddOrganizationDataCampaignRequest:
      type: object
      required:
        - dataCampaignDashboardId
        - name
        - description
        - coordinatorUids
        - queries
        - links
        - datasets
        - pipelineIds
        - projectIds
      properties:
        id:
          type: integer
        dataCampaignDashboardId:
          type: integer
        created:
          type: string
          format: date-time
        name:
          type: string
        description:
          type: string
        coordinatorUids:
          description: List of user IDs that coordinate this campaign
          type: array
          items:
            type: integer
        logo:
          type: string
        queries:
          type: array
          items:
            $ref: '#/components/schemas/DataCampaignQuery'
        links:
          type: array
          items:
            $ref: '#/components/schemas/DataCampaignLink'
        datasets:
          type: array
          items:
            type: string
        pipelineIds:
          type: array
          items:
            type: integer
        projectIds:
          type: array
          items:
            type: integer
    AddOrganizationDataCampaignResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - dataCampaignId
          properties:
            dataCampaignId:
              type: integer
    DataCampaignQuery:
      type: object
      required:
        - name
        - dataset
        - query
      properties:
        name:
          type: string
        dataset:
          type: string
        query:
          type: string
    DataCampaignLink:
      type: object
      required:
        - icon
        - name
        - link
      properties:
        icon:
          type: string
        name:
          type: string
        link:
          type: string
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