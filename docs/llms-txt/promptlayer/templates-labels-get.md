# Source: https://docs.promptlayer.com/reference/templates-labels-get.md

# Get Prompt Template Labels

Retrieve all the release labels assigned to a prompt template. Identifiers can be either `prompt_name` or `prompt_id`.


## OpenAPI

````yaml GET /prompt-templates/{identifier}/labels
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /prompt-templates/{identifier}/labels:
    get:
      tags:
        - prompt-templates
        - release-labels
      summary: Get Prompt Template Labels
      operationId: get_prompt_templates_labels_prompt_identifier__post
      parameters:
        - required: true
          schema:
            type: string
            title: X-Api-Key
          name: X-API-KEY
          in: header
        - name: identifier
          in: path
          required: true
          schema:
            type: string
            title: identifier
            description: The identifier can be either the prompt name or the prompt id.
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPromptTemplateLabelResponse'
        '404':
          description: Not Found
components:
  schemas:
    GetPromptTemplateLabelResponse:
      properties:
        release_labels:
          type: array
          items:
            type: object
            properties:
              prompt_version_id:
                type: integer
              prompt_version_number:
                type: integer
              release_label:
                type: string
              release_label_id:
                type: integer
            required:
              - prompt_version_id
              - prompt_version_number
              - release_label
              - release_label_id
          title: Release Labels
      type: object
      required:
        - release_labels
      title: GetPromptTemplateLabelResponse

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt