# Source: https://docs.lunary.ai/docs/api/views/delete-a-view.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a view

> Deletes a specific view by its ID.



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/views/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/views/{id}:
    delete:
      tags:
        - Views
      summary: Delete a view
      description: Deletes a specific view by its ID.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful deletion
          content:
            application/json:
              example:
                message: View successfully deleted

````