# Source: https://tyk.io/docs/api-reference/users/allow-password-reset-for-a-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Allow password reset for a User

> Allow password reset for a User.



## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml put /admin/users/{userId}/actions/allow_reset_passwords
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
  /admin/users/{userId}/actions/allow_reset_passwords:
    put:
      tags:
        - Users
      summary: Allow password reset for a User
      description: Allow password reset for a User.
      operationId: allowResetPassword
      parameters:
        - description: User ID of the user whose password is being reset
          example: 614215edb2d47190f98b3b79
          in: path
          name: userId
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              example:
                Message: User updated
                Meta:
                  PWHistory: []
                  access_key: 68b225c4376748207453c235ed8e2a82
                  active: true
                  created_at: '2021-09-15T15:49:01Z'
                  email_address: john@test.com
                  first_name: John
                  group_id: ''
                  id: 614215edb2d47190f98b3b79
                  last_login_date: '2021-09-15T15:49:49.754Z'
                  last_name: Doe
                  org_id: 60ef3a1dcb83670001bf2df9
                  password_max_days: 0
                  password_updated: '2021-09-15T15:49:01.863Z'
                  user_permissions:
                    IsAdmin: admin
                    ResetPassword: admin
                Status: OK
              schema:
                $ref: '#/components/schemas/ApiError'
          description: OK
        '403':
          content:
            application/json:
              example:
                Message: Failed to update User object to DB
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Forbidden
        '404':
          content:
            application/json:
              example:
                Message: Could not retrieve user detail
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: User not found
components:
  schemas:
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