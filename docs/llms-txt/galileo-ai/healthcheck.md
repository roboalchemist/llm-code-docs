# Source: https://docs.galileo.ai/api-reference/health/healthcheck.md

# Healthcheck

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json get /v1/healthcheck
paths:
  path: /v1/healthcheck
  method: get
  servers:
    - url: https://api.acme.rungalileo.io
      description: Galileo Public APIs - acme
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              api_version:
                allOf:
                  - type: string
                    title: Api Version
              message:
                allOf:
                  - type: string
                    title: Message
              version:
                allOf:
                  - type: string
                    title: Version
            title: HealthcheckResponse
            refIdentifier: '#/components/schemas/HealthcheckResponse'
            requiredProperties:
              - api_version
              - message
              - version
        examples:
          example:
            value:
              api_version: <string>
              message: <string>
              version: <string>
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas: {}

````