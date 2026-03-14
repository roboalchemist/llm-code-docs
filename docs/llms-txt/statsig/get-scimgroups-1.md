# Source: https://docs.statsig.com/api-reference/scim-groups/get-scimgroups-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get scimgroups 1



## OpenAPI

````yaml access-management/scim/scimopenapi.json get /scim/Groups/{id}
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
    get:
      tags:
        - SCIM Groups
      operationId: GroupsController_genGroup
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