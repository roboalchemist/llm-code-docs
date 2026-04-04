# Source: https://docs.frigade.com/api-reference/users/users-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a User



## OpenAPI

````yaml delete /v1/users
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
  /v1/users:
    delete:
      tags:
        - users
      summary: Delete a user by foreign id
      operationId: UsersController_delete
      parameters:
        - name: foreignId
          required: false
          in: query
          deprecated: true
          description: Deprecated. Use userId instead.
          schema:
            type: string
        - name: userId
          required: true
          in: query
          description: The ID of the user
          schema:
            type: string
      responses:
        '200':
          description: The user has been successfully deleted.
        '404':
          description: The user was not found.
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