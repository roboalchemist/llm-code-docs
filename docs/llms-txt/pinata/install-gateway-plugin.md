# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/install-gateway-plugin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Install Gateway Plugin

> `org:gateways:write`




## OpenAPI

````yaml post /gateways/plugins/{gateway_id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/plugins/{gateway_id}:
    post:
      tags:
        - default
      summary: Install Gateway Plugin
      description: |
        `org:gateways:write`
      parameters:
        - name: gateway_id
          in: path
          schema:
            type: string
          required: true
          example: 58516d3b-a882-438c-8951-aef528ab7114
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                plugin_id:
                  type: number
                  description: ID of the plugin to install to target gateway
              example:
                plugin_id: 1
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Mon, 22 Jul 2024 17:49:07 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '77'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 4d535ee9329b744a929edb4bcaf33bc4
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
                    type: object
                    properties:
                      gateway_id:
                        type: string
                      plugin_id:
                        type: number
              example:
                data:
                  gateway_id: 3ced949f-2013-47a0-8f4a-f8d8e8ee14ac
                  plugin_id: 1
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````