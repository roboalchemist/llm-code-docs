# Source: https://docs.statsig.com/api-reference/scim-groups/delete-scimgroups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete scimgroups



## OpenAPI

````yaml access-management/scim/scimopenapi.json delete /scim/Groups/{id}
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
    delete:
      tags:
        - SCIM Groups
      operationId: GroupsController_genDeleteGroup
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