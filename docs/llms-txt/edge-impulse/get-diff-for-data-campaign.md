# Source: https://docs.edgeimpulse.com/apis/studio/organizationdatacampaigns/get-diff-for-data-campaign.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get diff for data campaign

> Get which items have changed for a data campaign. You post the data points and we'll return which data items are different in the past day.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/campaigns/{campaignId}/diff
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
  /api/organizations/{organizationId}/campaigns/{campaignId}/diff:
    post:
      tags:
        - OrganizationDataCampaigns
      summary: Get diff for data campaign
      description: >-
        Get which items have changed for a data campaign. You post the data
        points and we'll return which data items are different in the past day.
      operationId: getOrganizationDataCampaignDiff
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDataCampaignIdPathParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrganizationDataCampaignDiffRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrganizationDataCampaignDiffResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    OrganizationDataCampaignIdPathParameter:
      name: campaignId
      in: path
      required: true
      schema:
        type: integer
  schemas:
    OrganizationDataCampaignDiffRequest:
      type: object
      required:
        - queries
      properties:
        queries:
          type: array
          items:
            type: object
            required:
              - dataset
              - query
              - graphValueId
            properties:
              dataset:
                type: string
              query:
                type: string
              graphValueId:
                type: integer
                description: Which point in the graph was clicked (from "graphs.values")
    OrganizationDataCampaignDiffResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - date
            - queries
          properties:
            date:
              type: string
              format: date-time
            queries:
              type: array
              items:
                type: object
                required:
                  - title
                  - dataset
                  - query
                  - newItems
                  - deletedItems
                properties:
                  title:
                    type: string
                  dataset:
                    type: string
                  query:
                    type: string
                  newItems:
                    type: array
                    items:
                      type: string
                  deletedItems:
                    type: array
                    items:
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