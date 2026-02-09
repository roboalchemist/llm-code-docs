# Source: https://www.activepieces.com/docs/endpoints/user-invitations/delete.md

# Source: https://www.activepieces.com/docs/endpoints/templates/delete.md

# Source: https://www.activepieces.com/docs/endpoints/projects/delete.md

# Source: https://www.activepieces.com/docs/endpoints/project-members/delete.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/delete.md

# Source: https://www.activepieces.com/docs/endpoints/folders/delete.md

# Source: https://www.activepieces.com/docs/endpoints/flows/delete.md

# Source: https://www.activepieces.com/docs/endpoints/connections/delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Connection

> Delete an app connection



## OpenAPI

````yaml DELETE /v1/app-connections/{id}
openapi: 3.0.3
info:
  title: Activepieces Documentation
  version: 0.0.0
servers:
  - url: https://cloud.activepieces.com/api
    description: Production Server
security: []
externalDocs:
  url: https://www.activepieces.com/docs
  description: Find more info here
paths:
  /v1/app-connections/{id}:
    delete:
      tags:
        - app-connections
      description: Delete an app connection
      parameters:
        - schema:
            pattern: ^[0-9a-zA-Z]{21}$
            type: string
          in: path
          name: id
          required: true
      responses:
        '204':
          description: Default Response
          content:
            application/json:
              schema:
                not: {}
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: http
      description: Use your api key generated from the admin console
      scheme: bearer

````