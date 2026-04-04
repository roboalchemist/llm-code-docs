# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/uninstall-gateway-plugin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Uninstall Gateway Plugin

> `org:gateways:write`




## OpenAPI

````yaml delete /gateways/plugins/{gateway_id}/plugin/{plugin_id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/plugins/{gateway_id}/plugin/{plugin_id}:
    delete:
      tags:
        - default
      summary: Uninstall Gateway Plugin
      description: |
        `org:gateways:write`
      parameters:
        - name: gateway_id
          in: path
          schema:
            type: string
          required: true
          example: 3ced949f-2013-47a0-8f4a-f8d8e8ee14ac
        - name: plugin_id
          in: path
          schema:
            type: integer
          required: true
          example: '1'
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Mon, 22 Jul 2024 17:51:21 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '14'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: eed30883b20f63ef34936ae933bd64bd
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
              example:
                data: null
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````