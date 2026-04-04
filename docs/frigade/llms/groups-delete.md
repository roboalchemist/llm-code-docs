# Source: https://docs.frigade.com/api-reference/groups/groups-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Group



## OpenAPI

````yaml delete /v1/groups
openapi: 3.0.0
info:
  title: Frigade API
  description: Official Frigade API documentation
  version: '1.0'
  contact: {}
servers: []
security: []
tags: []
paths:
  /v1/groups:
    delete:
      tags:
        - groups
      summary: Delete a group by foreign id
      operationId: UserGroupsController_delete
      parameters:
        - name: groupId
          required: true
          in: query
          description: The ID of the group
          schema:
            type: string
      responses:
        '200':
          description: The group has been successfully deleted.
        '404':
          description: The group was not found.
      security:
        - bearer: []
components:
  securitySchemes:
    bearer:
      scheme: bearer
      bearerFormat: JWT
      type: http
      description: >-
        Authentication header of the form `Bearer: <token>`, where `<token>` is
        either your public or private API key. [See when to use
        which](/v2/api-reference/authorization)

````