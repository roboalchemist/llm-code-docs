# Source: https://docs.edenai.co/api-reference/user-management/delete-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Token



## OpenAPI

````yaml openapi/v3-user.json delete /user/custom_token/{name}/
openapi: 3.0.3
info:
  title: User Management
  version: '2.0'
  description: Your project description
servers:
  - url: https://api.edenai.run/v2
security: []
paths:
  /user/custom_token/{name}/:
    delete:
      tags:
        - User Management
      summary: Delete Token
      operationId: user_root_destroy
      parameters:
        - in: path
          name: name
          schema:
            type: string
          required: true
      responses:
        '204':
          description: No response body
      security:
        - FeatureApiAuth: []
components:
  securitySchemes:
    FeatureApiAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````

Built with [Mintlify](https://mintlify.com).