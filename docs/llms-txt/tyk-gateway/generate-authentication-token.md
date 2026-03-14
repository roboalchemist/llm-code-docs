# Source: https://tyk.io/docs/api-reference/single-sign-on/generate-authentication-token.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate authentication token

> The Dashboard exposes the /admin/sso Dashboard API which allows you to generate a temporary authentication token, valid for 60 seconds.

## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml post /admin/sso
openapi: 3.0.3
info:
  contact:
    email: support@tyk.io
    name: Tyk Technologies
    url: https://tyk.io/contact
  description: >-
    <img src="https://tyk.io/docs/img/dashboard_admin_swagger_image.png"
    width="963" height="250">


    For Tyk On-Premises installations only, the Dashboard Admin API has two
    endpoints and is used to set up and provision a Tyk Dashboard instance
    without the command line.


    In order to use the Dashboard Admin API, you'll need to get the
    `admin_secret` value from your Tyk Dashboard configurations.


    The secret you set should then be sent along as a header with each Dashboard
    Admin API Request in order for it to be successful:


    ```

    admin-auth: <your-secret>

    ```
  license:
    name: Mozilla Public License Version 2.0
    url: https://github.com/TykTechnologies/tyk/blob/master/LICENSE.md
  title: Tyk Dashboard Admin API
  version: 5.8.0
servers:
  - url: https://{tenant}
    variables:
      tenant:
        default: localhost:3000
        description: Your dashboard host
security:
  - api_key: []
tags:
  - description: >-
      The import API enables you to add Organisations, APIs and Policies back
      into a Tyk installation while retaining their base IDs so that they work
      together.
    name: Import
  - description: >-
      To make Tyk installations more portable, the Export API enables you to
      export key configuration objects required to back-up and re-deploy a basic
      Tyk Pro installation.
    name: Export
  - description: >-
      The admin portion of the users API gives you the ability to manage
      password reset policies for your Dashboard users.
    name: Users
  - description: >-
      Since the Dashboard can have multiple URLs associated with it. It is
      possible to force a URL reload by calling an API endpoint of the Dashboard
      API.
    name: Dashboard URL Reload
  - description: >-
      The organisations API gives the ability to manage your Tyk
      organisation(s).
    name: Organisations
  - description: >-
      The Dashboard exposes the /admin/sso Dashboard API which allows you to
      generate a temporary authentication token, valid for 60 seconds.
    name: Single Sign On
paths:
  /admin/sso:
    post:
      tags:
        - Single Sign On
      summary: Generate authentication token
      description: >-
        The Dashboard exposes the /admin/sso Dashboard API which allows you to
        generate a temporary authentication token, valid for 60 seconds.
      operationId: generateAuthToken
      requestBody:
        content:
          application/json:
            example:
              DisplayName: ''
              EmailAddress: name@somewhere.com
              ForSection: dashboard
              GroupID: ''
              GroupsIDs: null
              OrgID: 588b4f0bb275ff0001cc7471
              SSOOnlyForRegisteredUsers: false
              UserNotAllowed: false
            schema:
              $ref: '#/components/schemas/SSOAccessData'
      responses:
        '200':
          content:
            application/json:
              example:
                Message: SSO Nonce created
                Meta: YTNiOGUzZjctYWZkYi00OTNhLTYwODItZTAzMDI3MjM0OTEw
                Status: OK
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Additional Permissions updated successfully.
        '400':
          content:
            application/json:
              example:
                Message: >-
                  Cannot create an SSO session for an invalid payload: [Error:
                  Org id not found ('588b4f0bb275ff0001cc7471').]
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Back Request.
        '401':
          content:
            application/json:
              example:
                Message: Not authorised
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Unauthorized
        '403':
          content:
            application/json:
              example:
                Message: Failed to save new SSO object to DB
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Failed to save new SSO object to DB
        '500':
          content:
            application/json:
              example:
                Message: Failed to read response body, body empty
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Could not read request body
components:
  schemas:
    SSOAccessData:
      properties:
        DisplayName:
          type: string
        EmailAddress:
          type: string
        ForSection:
          type: string
        GroupID:
          type: string
        GroupsIDs:
          items:
            type: string
          nullable: true
          type: array
        OrgID:
          type: string
        SSOOnlyForRegisteredUsers:
          type: boolean
        UserNotAllowed:
          type: boolean
      type: object
    ApiError:
      properties:
        ID:
          type: string
        Message:
          type: string
        Meta: {}
        Status:
          type: string
      type: object
  securitySchemes:
    api_key:
      description: Api key
      in: header
      name: Admin-Auth
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).
