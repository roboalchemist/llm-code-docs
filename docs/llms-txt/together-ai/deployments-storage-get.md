# Source: https://docs.together.ai/reference/deployments-storage-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Storage File

> Download a file by redirecting to a signed URL



## OpenAPI

````yaml GET /deployments/storage/{filename}
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
  /deployments/storage/{filename}:
    get:
      tags:
        - DeploymentsStorage
      summary: Download a file
      description: Download a file by redirecting to a signed URL
      parameters:
        - name: filename
          in: path
          required: true
          schema:
            description: Filename
            type: string
      responses:
        '307':
          description: Redirect to signed download URL
          content:
            application/json:
              schema:
                type: string
        '400':
          description: Invalid request
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
                type: object
        '404':
          description: File not found
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
                type: object
        '500':
          description: Internal error
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
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