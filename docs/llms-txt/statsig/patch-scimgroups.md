# Source: https://docs.statsig.com/api-reference/scim-groups/patch-scimgroups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Patch scimgroups



## OpenAPI

````yaml access-management/scim/scimopenapi.json patch /scim/Groups/{id}
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
  /scim/Groups/{id}:
    patch:
      tags:
        - SCIM Groups
      operationId: GroupsController_genPatchGroup
      parameters:
        - name: id
          required: true
          in: path
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScimPartialUpdateGroupDto'
      responses:
        '200':
          description: ''
components:
  schemas:
    ScimPartialUpdateGroupDto:
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
              path:
                type: string
              value:
                type: array
                items:
                  type: object
                  properties:
                    value:
                      type: string
                    display:
                      type: string
                  required:
                    - value
                    - display
            required:
              - op
              - path
              - value
      required:
        - Operations

````

Built with [Mintlify](https://mintlify.com).