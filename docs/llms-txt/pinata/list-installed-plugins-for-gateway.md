# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-installed-plugins-for-gateway.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# List Installed Plugins for Gateway

> `org:gateways:read`




## OpenAPI

````yaml get /ipfs/gateway_plugins/{gateway_id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /ipfs/gateway_plugins/{gateway_id}:
    get:
      tags:
        - default
      summary: List Installed Plugins for Gateway
      description: |
        `org:gateways:read`
      parameters:
        - name: gateway_id
          in: path
          schema:
            type: string
          required: true
          example: 2bfaa2ae-b590-4cb4-bb9c-5af43c2c9541
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Mon, 22 Jul 2024 17:53:24 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '147'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 81ee012022a1ae7dccdff5cbf8e10d9a
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        gateway_id:
                          type: string
                        plugin_id:
                          type: number
              example:
                data:
                  - gateway_id: 2bfaa2ae-b590-4cb4-bb9c-5af43c2c9541
                    plugin_id: 1
                  - gateway_id: 2bfaa2ae-b590-4cb4-bb9c-5af43c2c9541
                    plugin_id: 2
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````