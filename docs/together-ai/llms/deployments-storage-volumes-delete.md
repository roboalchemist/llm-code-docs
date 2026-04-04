# Source: https://docs.together.ai/reference/deployments-storage-volumes-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Storage Volume

> Delete an existing volume



## OpenAPI

````yaml DELETE /deployments/storage/volumes/{id}
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /deployments/storage/volumes/{id}:
    delete:
      tags:
        - Volumes
      summary: Delete a volume
      description: Delete an existing volume
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: Volume ID or name
            type: string
      responses:
        '200':
          description: Volume deleted successfully
          content:
            application/json:
              schema:
                type: object
        '404':
          description: Volume not found
          content:
            application/json:
              schema:
                type: object
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).