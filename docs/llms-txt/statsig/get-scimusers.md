# Source: https://docs.statsig.com/api-reference/scim-users/get-scimusers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get scimusers



## OpenAPI

````yaml access-management/scim/scimopenapi.json get /scim/Users
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
  /scim/Users:
    get:
      tags:
        - SCIM Users
      operationId: UserController_genListUsers
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