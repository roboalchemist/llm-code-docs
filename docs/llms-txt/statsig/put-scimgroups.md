# Source: https://docs.statsig.com/api-reference/scim-groups/put-scimgroups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Put scimgroups



## OpenAPI

````yaml access-management/scim/scimopenapi.json put /scim/Groups/{id}
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
    put:
      tags:
        - SCIM Groups
      operationId: GroupsController_genFullUpdateGroup
      parameters:
        - name: id
          required: true
          in: path
          schema:
            type: string
      responses:
        '200':
          description: ''

````

Built with [Mintlify](https://mintlify.com).