# Source: https://docs.statsig.com/api-reference/scim-users/patch-scimusers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Patch scimusers



## OpenAPI

````yaml access-management/scim/scimopenapi.json patch /scim/Users/{id}
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
    patch:
      tags:
        - SCIM Users
      operationId: UserController_genPartialUpdateUser
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScimPartialUpdateUserDto'
      responses:
        '200':
          description: ''
components:
  schemas:
    ScimPartialUpdateUserDto:
      type: object
      properties:
        schemas:
          type: array
          items:
            type: string
        Operations:
          type: array
          items:
            type: object
            properties:
              op:
                type: string
                enum:
                  - replace
                  - add
                  - remove
              value:
                type: object
                properties:
                  active:
                    type: boolean
            required:
              - op
              - value
      required:
        - Operations

````

Built with [Mintlify](https://mintlify.com).