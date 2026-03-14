# Source: https://docs.statsig.com/api-reference/scim-users/get-scimusers-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get scimusers 1



## OpenAPI

````yaml access-management/scim/scimopenapi.json get /scim/Users/{id}
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
    get:
      tags:
        - SCIM Users
      operationId: UserController_genUser
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