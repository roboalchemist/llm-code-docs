# Source: https://www.activepieces.com/docs/endpoints/user-invitations/delete.md

# Source: https://www.activepieces.com/docs/endpoints/templates/delete.md

# Source: https://www.activepieces.com/docs/endpoints/projects/delete.md

# Source: https://www.activepieces.com/docs/endpoints/project-members/delete.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/delete.md

# Source: https://www.activepieces.com/docs/endpoints/folders/delete.md

# Source: https://www.activepieces.com/docs/endpoints/flows/delete.md

# Source: https://www.activepieces.com/docs/endpoints/connections/delete.md

# Source: https://www.activepieces.com/docs/endpoints/user-invitations/delete.md

# Source: https://www.activepieces.com/docs/endpoints/templates/delete.md

# Source: https://www.activepieces.com/docs/endpoints/projects/delete.md

# Source: https://www.activepieces.com/docs/endpoints/project-members/delete.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/delete.md

# Source: https://www.activepieces.com/docs/endpoints/folders/delete.md

# Source: https://www.activepieces.com/docs/endpoints/flows/delete.md

# Source: https://www.activepieces.com/docs/endpoints/connections/delete.md

# Source: https://www.activepieces.com/docs/endpoints/user-invitations/delete.md

# Source: https://www.activepieces.com/docs/endpoints/projects/delete.md

# Source: https://www.activepieces.com/docs/endpoints/project-members/delete.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/delete.md

# Source: https://www.activepieces.com/docs/endpoints/folders/delete.md

# Source: https://www.activepieces.com/docs/endpoints/flows/delete.md

# Source: https://www.activepieces.com/docs/endpoints/flow-templates/delete.md

# Source: https://www.activepieces.com/docs/endpoints/connections/delete.md

# Delete Connection

> Delete an app connection

## OpenAPI

````yaml DELETE /v1/app-connections/{id}
paths:
  path: /v1/app-connections/{id}
  method: delete
  servers:
    - url: https://cloud.activepieces.com/api
      description: Production Server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Use your api key generated from the admin console
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````