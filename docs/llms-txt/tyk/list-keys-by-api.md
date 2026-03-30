# Source: https://tyk.io/docs/api-reference/keys/list-keys-by-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List keys by API.

> Lists keys that grant access to the API with the ID {apiID}.



## OpenAPI

````yaml swagger/5.8/dashboard-admin-swagger.yml get /admin/org/keys
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
  /admin/org/keys:
    get:
      tags:
        - keys
      summary: List keys by API.
      description: Lists keys that grant access to the API with the ID {apiID}.
      operationId: getAllKeys
      responses:
        '200':
          content:
            application/json:
              example:
                data:
                  keys:
                    - 5e9d9544a1dcd60001d0ed20a28c495beff140a4a6d8c272a1956b99
                    - 5e9d9544a1dcd60001d0ed20e7f75f9e03534825b7aef9df749582e5
                    - 5e9d9544a1dcd60001d0ed2060ff87c0deab4a508dd2ac18ccb8b664
                pages: 1
              schema:
                $ref: '#/components/schemas/Keys'
          description: Paginated key IDs.
        '404':
          content:
            application/json:
              example:
                Message: Could not retrieve keys
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Not Found
        '500':
          content:
            application/json:
              example:
                Message: Failed to unmarshal keys data from Tyk API
                Meta: null
                Status: Error
              schema:
                $ref: '#/components/schemas/ApiError'
          description: Internal Server Error
components:
  schemas:
    Keys:
      properties:
        data:
          $ref: '#/components/schemas/AllKeys'
        pages:
          type: integer
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
    AllKeys:
      properties:
        keys:
          items:
            type: string
          nullable: true
          type: array
      type: object
  securitySchemes:
    api_key:
      description: Api key
      in: header
      name: Admin-Auth
      type: apiKey

````

Built with [Mintlify](https://mintlify.com).