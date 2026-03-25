# Source: https://docs.edgeimpulse.com/apis/studio/organizationdatacampaigns/get-data-campaigns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data campaigns

> Get a list of all data campaigns for a dashboard



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/campaign-dashboard/{campaignDashboardId}/campaigns
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
  /api/organizations/{organizationId}/campaign-dashboard/{campaignDashboardId}/campaigns:
    get:
      tags:
        - OrganizationDataCampaigns
      summary: Get data campaigns
      description: Get a list of all data campaigns for a dashboard
      operationId: getOrganizationDataCampaignsForDashboard
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
                $ref: '#/components/schemas/GetOrganizationDataCampaignsResponse'
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
    GetOrganizationDataCampaignsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - campaigns
          properties:
            campaigns:
              type: array
              items:
                type: object
                required:
                  - campaign
                  - graphs
                properties:
                  campaign:
                    $ref: '#/components/schemas/DataCampaign'
                  graphs:
                    type: array
                    items:
                      $ref: '#/components/schemas/DataCampaignGraph'
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
    DataCampaign:
      type: object
      required:
        - id
        - dataCampaignDashboardId
        - created
        - name
        - description
        - coordinatorUids
        - pipelineIds
        - queries
        - links
        - datasets
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
    DataCampaignGraph:
      type: object
      required:
        - title
        - link
        - xData
        - yTicks
        - nextUpdate
      properties:
        title:
          type: string
        link:
          type: string
        xData:
          type: array
          items:
            type: object
            required:
              - color
              - popupText
              - legendText
              - values
              - dataType
            properties:
              color:
                type: string
              legendText:
                type: string
              popupText:
                type: string
              values:
                type: array
                items:
                  type: object
                  required:
                    - id
                  properties:
                    id:
                      type: integer
                    value:
                      type: number
              dataset:
                type: string
              query:
                type: string
              dataType:
                type: string
                enum:
                  - dataItems
                  - time
                  - percentage
        yTicks:
          type: array
          items:
            type: string
            format: date-time
        nextUpdate:
          type: string
          format: date-time
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