# Source: https://docs.statsig.com/api-reference/scim-users/put-scimusers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Put scimusers



## OpenAPI

````yaml access-management/scim/scimopenapi.json put /scim/Users/{id}
openapi: 3.0.0
info:
  title: SCIM API
  description: |2-

          APIs for SCIM compliance.
          
  version: '1.0'
  contact: {}
servers:
  - url: https://statsigapi.net
security: []
tags: []
paths:
  /scim/Users/{id}:
    put:
      tags:
        - SCIM Users
      operationId: UserController_genFullUpdateUser
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScimCreateUserDto'
      responses:
        '200':
          description: ''
components:
  schemas:
    ScimCreateUserDto:
      type: object
      properties:
        id:
          type: string
        userName:
          type: string
        name:
          type: object
          properties:
            givenName:
              type: string
            middleName:
              type: string
            familyName:
              type: string
          required:
            - givenName
            - familyName
        emails:
          type: array
          items:
            type: object
            properties:
              primary:
                type: boolean
              value:
                type: string
              type:
                type: string
            required:
              - value
        active:
          type: boolean
        statsigOrgRole:
          type: string
          nullable: true
        schemas:
          type: array
          items:
            type: string
        password:
          type: string
      required:
        - userName
        - name
        - emails

````

Built with [Mintlify](https://mintlify.com).