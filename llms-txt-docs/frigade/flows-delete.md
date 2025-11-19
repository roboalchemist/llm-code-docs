# Source: https://docs.frigade.com/api-reference/flows/flows-delete.md

# Delete Flow

> Delete a Flow

## OpenAPI

````yaml delete /v1/flows/{numericFlowId}
paths:
  path: /v1/flows/{numericFlowId}
  method: delete
  request:
    security:
      - title: bearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Authentication header of the form `Bearer: <token>`, where
                `<token>` is either your public or private API key. [See when to
                use which](/v2/api-reference/authorization)
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The Flow has been successfully deleted.
        examples: {}
        description: The Flow has been successfully deleted.
  deprecated: false
  type: path
components:
  schemas: {}

````