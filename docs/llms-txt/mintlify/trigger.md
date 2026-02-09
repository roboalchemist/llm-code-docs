# Source: https://www.mintlify.com/docs/api/update/trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger update

> Queue a deployment update for your documentation project. Returns a status ID that can be used to track the update progress. The update is triggered from your configured deployment branch.



## OpenAPI

````yaml openapi.json post /project/update/{projectId}
openapi: 3.0.1
info:
  title: Mintlify External API
  description: An API for Mintlify documentation management and resource access.
  version: 1.0.0
servers:
  - url: https://api.mintlify.com/v1
security:
  - bearerAuth: []
paths:
  /project/update/{projectId}:
    post:
      summary: Trigger update
      description: >-
        Queue a deployment update for your documentation project. Returns a
        status ID that can be used to track the update progress. The update is
        triggered from your configured deployment branch.
      parameters:
        - name: projectId
          in: path
          description: >-
            Your project ID. Can be copied from the [API
            keys](https://dashboard.mintlify.com/settings/organization/api-keys)
            page in your dashboard.
          required: true
          schema:
            type: string
      responses:
        '202':
          description: A successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  statusId:
                    type: string
                    description: The status ID of the triggered updated.
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        The Authorization header expects a Bearer token. Use an admin API key
        (prefixed with `mint_`). This is a server-side secret key. Generate one
        on the [API keys
        page](https://dashboard.mintlify.com/settings/organization/api-keys) in
        your dashboard.

````