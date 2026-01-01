# Source: https://docs.promptlayer.com/reference/prompt-labels-delete.md

# Delete a Prompt Template Label

Delete a prompt label from a prompt version.


## OpenAPI

````yaml DELETE /prompt-labels/{prompt_label_id}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /prompt-labels/{prompt_label_id}:
    delete:
      tags:
        - prompt-templates
        - release-labels
      summary: Delete Prompt Template Label
      operationId: delete_prompt_templates_labels_prompt_label_id
      parameters:
        - name: prompt_label_id
          in: path
          required: true
          schema:
            type: integer
            title: prompt_label_id
        - required: true
          schema:
            type: string
            title: X-Api-Key
          name: X-API-KEY
          in: header
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                type: string

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt