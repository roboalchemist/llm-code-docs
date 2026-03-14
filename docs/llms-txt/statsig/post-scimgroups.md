# Source: https://docs.statsig.com/api-reference/scim-groups/post-scimgroups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Post scimgroups



## OpenAPI

````yaml access-management/scim/scimopenapi.json post /scim/Groups
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
    post:
      tags:
        - SCIM Groups
      operationId: GroupsController_genCreateGroup
      parameters: []
      responses:
        '201':
          description: ''

````

Built with [Mintlify](https://mintlify.com).