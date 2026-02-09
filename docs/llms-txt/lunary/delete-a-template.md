# Source: https://docs.lunary.ai/docs/api/templates/delete-a-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a template



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/templates/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/templates/{id}:
    delete:
      tags:
        - Templates
      summary: Delete a template
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '204':
          description: Successful deletion

````