# Source: https://docs.promptlayer.com/reference/prompt-labels-patch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Move Prompt Template Labels

Move a prompt label from one prompt version to another


## OpenAPI

````yaml PATCH /prompt-labels/{prompt_label_id}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /prompt-labels/{prompt_label_id}:
    patch:
      tags:
        - prompt-templates
        - release-labels
      summary: Move Prompt Template Labels
      operationId: prompt_templates_labels_prompt_label_id__patch
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt_version_number:
                  type: integer
              required:
                - prompt_version_number
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  created_at:
                    type: string
                    format: date-time
                  id:
                    type: integer
                  name:
                    type: string
                  prompt_id:
                    type: integer
                  prompt_version_id:
                    type: integer
                required:
                  - created_at
                  - id
                  - name
                  - prompt_id
                  - prompt_version_id

````