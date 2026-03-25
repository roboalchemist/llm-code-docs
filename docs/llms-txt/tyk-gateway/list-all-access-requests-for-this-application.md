# Source: https://tyk.io/docs/api-reference/applications-and-credentials/list-all-access-requests-for-this-application.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all access requests for this application

> List all access requests for this application

## OpenAPI

````yaml swagger/5.8/enterprise-developer-portal-swagger.yaml get /apps/{app_id}/access-requests
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
  /apps/{app_id}/access-requests:
    get:
      tags:
        - Applications and credentials
      summary: List all access requests for this application
      description: List all access requests for this application
      operationId: list-access-requests-from-app
      parameters:
        - description: UID of this application
          in: path
          name: app_id
          required: true
          schema:
            type: integer
            example: 1
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccessRequest-index'
          description: OK
      security:
        - AdminAPIToken: []
components:
  schemas:
    AccessRequest-index:
      type: array
      items:
        $ref: '#/components/schemas/AccessRequest-index-elem'
    AccessRequest-index-elem:
      allOf:
        - $ref: '#/components/schemas/AccessRequest-basic'
        - type: object
          properties:
            Products:
              type: string
              description: Names of products included in this access request
              example: Payment API
            Credentials:
              items:
                $ref: '#/components/schemas/Credential'
              type: array
      type: object
    AccessRequest-basic:
      allOf:
        - $ref: '#/components/schemas/AccessRequest-internal'
        - type: object
          properties:
            AuthType:
              type: string
              description: >-
                Authentication type of APIs that are included in this API
                Product
              example: authToken
            DCREnabled:
              type: boolean
              description: >-
                Identifies if this access request was created using Dynamic
                client registration
              example: false
            ID:
              type: integer
              description: UID of access request
              example: 1
            ProvisionImmediately:
              type: boolean
              description: Identifies if this access request was approved automatically
              example: true
            Status:
              enum:
                - approved
                - rejected
                - pending
              description: Approval status of this access request
    Credential:
      properties:
        AccessRequest:
          type: string
          description: Access request description
          example: AccessRequest#2
        Credential:
          type: string
          description: >-
            Auth token from the Tyk API Gateway. For OAuth2.0 credentials it's
            an empty string
          example: >-
            eyJvcmciOiI1ZTlkOTU0NGExZGNkNjAwMDFkMGVkMjAiLCJpZCI6IjY4MjZjZGViMmVlMzQ3ZGQ5ZjQ1ZWZmMjEyMTlhOWU1IiwiaCI6Im11cm11cjY0In0=
        CredentialHash:
          type: string
          description: >-
            Hash of an auth token from the Tyk API Gateway. For OAuth2.0
            credentials it's an empty string
          example: e1212449778b7ba4
        DCRRegistrationAccessToken:
          type: string
          description: >-
            Access token for Dynamic client registration that is associated with
            credentials. Has non-empty value only for OAuth2.0 credentials
          example: >-
            eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJmZjIyNmYyZi0yMDA0LTRlOWItOTFmOC1iOGYzOTA2ZDJmYTQifQ.eyJleHAiOjAsImlhdCI6MTY4NzczNzM5MCwianRpIjoiNjc3OTgwYjktZjgwMS00MmQ2LWI4OTItZDdkNDk1MmFhMjU5IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo5OTk5L3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0Ojk5OTkvcmVhbG1zL21hc3RlciIsInR5cCI6IlJlZ2lzdHJhdGlvbkFjY2Vzc1Rva2VuIiwicmVnaXN0cmF0aW9uX2F1dGgiOiJhdXRoZW50aWNhdGVkIn0.wyE93vktqlCywgtyJ8HBTjRPG9NvZEDR3zpSMncdwno
        DCRRegistrationClientURI:
          type: string
          description: >-
            DCR client registration URI that is associated with credentials. Has
            non-empty value only for OAuth2.0 credentials
          example: >-
            http://idp-host/realms/master/clients-registrations/openid-connect/cf4ab76c-c437-4ba2-8e94-1323269b5090
        DCRResponse:
          type: string
          description: >-
            Cached client registration response from the Identity Provider. Has
            non-empty value only for OAuth2.0 credentials
          example: >-
            {"redirect_uris":["http://app-host/auth"],"token_endpoint_auth_method":"client_secret_basic","grant_types":["implicit","client_credentials"],"response_types":["id_token","id_token
            token"],"client_id":"cf4ab76c-c437-4ba2-8e94-1323269b5090","client_secret":"iDe9fkFNBDbVS5JOtYNUDIO8w8N6dWzf","client_name":"OAuth2.0
            client","scope":"address phone offline_access
            microprofile-jwt","subject_type":"public","request_uris":[],"tls_client_certificate_bound_access_tokens":false,"client_id_issued_at":1687737390,"client_secret_expires_at":0,"registration_client_uri":"http://idp-host/realms/master/clients-registrations/openid-connect/cf4ab76c-c437-4ba2-8e94-1323269b5090","registration_access_token":"eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJmZjIyNmYyZi0yMDA0LTRlOWItOTFmOC1iOGYzOTA2ZDJmYTQifQ.eyJleHAiOjAsImlhdCI6MTY4NzczNzM5MCwianRpIjoiNjc3OTgwYjktZjgwMS00MmQ2LWI4OTItZDdkNDk1MmFhMjU5IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo5OTk5L3JlYWxtcy9tYXN0ZXIiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0Ojk5OTkvcmVhbG1zL21hc3RlciIsInR5cCI6IlJlZ2lzdHJhdGlvbkFjY2Vzc1Rva2VuIiwicmVnaXN0cmF0aW9uX2F1dGgiOiJhdXRoZW50aWNhdGVkIn0.wyE93vktqlCywgtyJ8HBTjRPG9NvZEDR3zpSMncdwno","backchannel_logout_session_required":false,"require_pushed_authorization_requests":false,"frontchannel_logout_session_required":false}
        Expires:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          example: 1969-12-31 19:00
          description: Date-time when this credential expires
        OAuthClientID:
          type: string
          description: >-
            OAuth2.0 client ID. Has non-empty value only for OAuth2.0
            credentials
          example: cf4ab76c-c437-4ba2-8e94-1323269b5090
        OAuthClientSecret:
          type: string
          description: >-
            OAuth2.0 client secret. Has non-empty value only for OAuth2.0
            credentials
          example: iDe9fkFNBDbVS5JOtYNUDIO8w8N6dWzf
        RedirectURI:
          type: string
          description: Redirect URI for OAuth2.0 authorization_code and PKCE grant types
          example: https://app-host/auth
        ResponseType:
          type: string
          description: >-
            Response types supported by this credential. Has non-empty value
            only for OAuth2.0 credentials
          example: id_token token
        Scope:
          type: string
          description: >-
            OAuth2.0 scope available to this credential. Has non-empty value
            only for OAuth2.0 credentials
          example: payment client
        TokenEndpoints:
          type: string
          description: >-
            OAuth2.0 `token_endpoint_auth_method` that this credential uses. Has
            non-empty value only for OAuth2.0 credentials
          example: payment client
      type: object
    AccessRequest-internal:
      properties:
        Catalogue:
          type: string
          description: Catalogue of API Products included in this access request
          example: Public Catalogue
        Client:
          type: string
          description: Name of the developer app
          example: Payment application
        CreatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this access request was created
          example: 2023-06-25 13:37
        UpdatedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this access request was updated the last time
          example: 2023-06-25 13:37
        DeletedAt:
          pattern: ^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$
          type: string
          description: Timestamp of when this access request was removed
          example: 2023-06-25 13:37
        Plan:
          type: string
          description: Name of a plan included in this access request
          example: Free plan
        User:
          type: string
          description: Descriptor of a user to whom this access request belongs
          example: User#1
      type: object
  securitySchemes:
    AdminAPIToken:
      type: apiKey
      in: header
      name: Authorization

````

Built with [Mintlify](https://mintlify.com).
