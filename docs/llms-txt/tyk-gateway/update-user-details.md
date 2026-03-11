# Source: https://tyk.io/docs/api-reference/users/update-user-details.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update user details

> Update user details with the user ID

## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml put /admin/users/{userId}
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
  /admin/users/{userId}:
    put:
      tags:
        - Users
      summary: Update user details
      description: Update user details with the user ID
      operationId: updateUser
      parameters:
        - description: The Id of the user you want to update
          example: 679a02465715ecdd507d7273
          in: path
          name: userId
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            example:
              access_key: c8251902f3f44dfa729e0267d0d62859
              active: false
              email_address: itachisasuke@gmail.com
              first_name: itachi
              id: 679a02465715ecdd507d7273
              last_name: sasuke
              org_id: ''
            schema:
              $ref: '#/components/schemas/User'
      responses:
        '200':
          content:
            application/json:
              example:
                Message: c8251902f3f44dfa729e0267d0d62859
                Meta:
                  access_key: c8251902f3f44dfa729e0267d0d62859
                  active: false
                  api_model: {}
                  created_at: '2025-03-10T11:10:52.986309+03:00'
                  email_address: itachisasuke@gmail.com
                  first_name: itachi
                  group_id: ''
                  id: '363739613032343635373135656364643530376437323733'
                  last_login_date: '0001-01-01T00:00:00Z'
                  last_name: sasuke
                  org_id: ''
                  password_max_days: 0
                  password_updated: '0001-01-01T00:00:00Z'
                  user_permissions:
                    IsAdmin: admin
                    ResetPassword: admin
                Status: OK
              schema:
                $ref: '#/components/schemas/ApiError'
          description: User updated successfully
        '403':
          content:
            application/json:
              example:
                Message: Request body malformed
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Unmarshalling request body failed, malformed
        '404':
          content:
            application/json:
              example:
                Message: User not found
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: User not found
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
    User:
      properties:
        access_key:
          type: string
        active:
          type: boolean
        api_model:
          $ref: '#/components/schemas/ApiModel'
        email_address:
          type: string
        first_name:
          type: string
        group_id:
          type: string
        id:
          type: string
        last_login_date:
          format: date-time
          type: string
        last_name:
          type: string
        org_id:
          type: string
        password_max_days:
          type: integer
        password_updated:
          format: date-time
          type: string
        user_permissions:
          $ref: '#/components/schemas/ConfigUserPermissionObject'
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
    ApiModel:
      type: object
    ConfigUserPermissionObject:
      additionalProperties:
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
