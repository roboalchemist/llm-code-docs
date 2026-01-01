# Source: https://docs.lunary.ai/docs/api/runs/delete-a-run.md

# Delete a run

> Delete a specific run by its ID. This action is irreversible.



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/runs/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs/{id}:
    delete:
      tags:
        - Runs
      summary: Delete a run
      description: Delete a specific run by its ID. This action is irreversible.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '204':
          description: Run successfully deleted
        '403':
          description: Forbidden - User doesn't have permission to delete runs
        '404':
          description: Run not found

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt