# Source: https://docs.statsig.com/api-reference/scim-groups/get-scimgroups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get scimgroups



## OpenAPI

````yaml access-management/scim/scimopenapi.json get /scim/Groups
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
  /scim/Groups:
    get:
      tags:
        - SCIM Groups
      operationId: GroupsController_genListGroups
      parameters:
        - name: filter
          required: false
          in: query
          schema:
            type: string
        - name: startIndex
          required: false
          in: query
          schema:
            oneOf:
              - type: string
              - type: number
        - name: count
          required: false
          in: query
          schema:
            oneOf:
              - type: string
              - type: number
      responses:
        '200':
          description: ''

````

Built with [Mintlify](https://mintlify.com).