# Source: https://docs.embedchain.ai/examples/rest-api/deploy.md

# Source: https://docs.embedchain.ai/api-reference/app/deploy.md

# Source: https://docs.embedchain.ai/examples/rest-api/deploy.md

# Deploy app

> Deploy an existing app.

## OpenAPI

````yaml post /{app_id}/deploy
paths:
  path: /{app_id}/deploy
  method: post
  request:
    security: []
    parameters:
      path:
        app_id:
          schema:
            - type: string
              required: true
              title: App Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              api_key:
                allOf:
                  - type: string
                    title: Api Key
                    description: >-
                      The Embedchain API key for app deployments. You get the
                      api key on the Embedchain platform by visiting
                      [https://app.embedchain.ai](https://app.embedchain.ai)
                    default: ''
            required: true
            title: DeployAppRequest
            refIdentifier: '#/components/schemas/DeployAppRequest'
            example:
              api_key: ec-xxx
        examples:
          example:
            value:
              api_key: ec-xxx
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              response:
                allOf:
                  - type: string
                    title: Response
            title: DefaultResponse
            refIdentifier: '#/components/schemas/DefaultResponse'
            requiredProperties:
              - response
        examples:
          example:
            value:
              response: <string>
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````