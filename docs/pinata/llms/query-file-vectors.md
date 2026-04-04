# Source: https://docs.pinata.cloud/api-reference/endpoint/query-file-vectors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Query File Vectors

> `org:write`




## OpenAPI

````yaml post /vectorize/groups/{group_id}/query
openapi: 3.0.0
info:
  title: Private IPFS API
  version: 1.0.0
servers:
  - url: https://uploads.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /vectorize/groups/{group_id}/query:
    post:
      tags:
        - Private Files
      summary: Query File Vectors
      description: |
        `org:write`
      parameters:
        - schema:
            type: string
            description: ID of the target group
            format: uuid
          required: true
          name: group_id
          in: path
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                text:
                  type: string
                  description: Query string
      responses:
        '200':
          description: Vectorize File Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      count:
                        type: number
                      matches:
                        type: array
                        items:
                          type: object
                          properties:
                            file_id:
                              type: string
                            cid:
                              type: string
                            score:
                              type: number
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````